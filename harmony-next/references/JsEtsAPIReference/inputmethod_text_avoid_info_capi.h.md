# inputmethod_text_avoid_info_capi.h

#### 概述

提供输入框避让信息对象的创建、销毁与读写方法。

**引用文件：** <inputmethod/inputmethod_text_avoid_info_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：**[InputMethod](InputMethod.md)

#### 汇总

#### 结构体

名称typedef关键字描述[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)InputMethod_TextAvoidInfo输入框避让信息。输入框用于避让键盘的信息。

#### 函数

名称描述[InputMethod_TextAvoidInfo *OH_TextAvoidInfo_Create(double positionY, double height)](#ZH-CN_TOPIC_0000002529445261__oh_textavoidinfo_create)创建一个新的[InputMethod_TextAvoidInfo](zh-cn_topic_0000002497605300.html)实例。[void OH_TextAvoidInfo_Destroy(InputMethod_TextAvoidInfo *info)](#ZH-CN_TOPIC_0000002529445261__oh_textavoidinfo_destroy)销毁一个[InputMethod_TextAvoidInfo](zh-cn_topic_0000002497605300.html)实例。[InputMethod_ErrorCode OH_TextAvoidInfo_SetPositionY(InputMethod_TextAvoidInfo *info, double positionY)](#ZH-CN_TOPIC_0000002529445261__oh_textavoidinfo_setpositiony)设置[InputMethod_TextAvoidInfo](zh-cn_topic_0000002497605300.html)中的Y坐标值。[InputMethod_ErrorCode OH_TextAvoidInfo_SetHeight(InputMethod_TextAvoidInfo *info, double height)](#ZH-CN_TOPIC_0000002529445261__oh_textavoidinfo_setheight)设置[InputMethod_TextAvoidInfo](zh-cn_topic_0000002497605300.html)中的高度值。[InputMethod_ErrorCode OH_TextAvoidInfo_GetPositionY(InputMethod_TextAvoidInfo *info, double *positionY)](#ZH-CN_TOPIC_0000002529445261__oh_textavoidinfo_getpositiony)从[InputMethod_TextAvoidInfo](zh-cn_topic_0000002497605300.html)获取Y坐标值。[InputMethod_ErrorCode OH_TextAvoidInfo_GetHeight(InputMethod_TextAvoidInfo *info, double *height)](#ZH-CN_TOPIC_0000002529445261__oh_textavoidinfo_getheight)从[InputMethod_TextAvoidInfo](zh-cn_topic_0000002497605300.html)获取高度值。

#### 函数说明

#### OH_TextAvoidInfo_Create()

```ets
InputMethod_TextAvoidInfo *OH_TextAvoidInfo_Create(double positionY, double height)
```

**描述**

创建一个新的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例。

**起始版本：** 12

**参数：**

参数项描述double positionY表示输入框位置的Y坐标值。double height表示输入框高度。

**返回：**

类型说明[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md) *

如果创建成功，返回一个指向新创建的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例的指针。

 如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。

#### OH_TextAvoidInfo_Destroy()

```ets
void OH_TextAvoidInfo_Destroy(InputMethod_TextAvoidInfo *info)
```

**描述**

销毁一个[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md) *info表示指向即将被销毁的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例的指针。

#### OH_TextAvoidInfo_SetPositionY()

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_SetPositionY(InputMethod_TextAvoidInfo *info, double positionY)
```

**描述**

设置[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)中的Y坐标值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md) *info指向即将被设置值的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例的指针。double positionYpositionY值，即输入框顶点与物理屏幕上侧距离的绝对值，单位px。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_TextAvoidInfo_SetHeight()

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_SetHeight(InputMethod_TextAvoidInfo *info, double height)
```

**描述**

设置[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)中的高度值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md) *info指向即将被设置值的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例的指针。double height高度值。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_TextAvoidInfo_GetPositionY()

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_GetPositionY(InputMethod_TextAvoidInfo *info, double *positionY)
```

**描述**

从[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)获取Y坐标值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md) *info指向即将被获取值的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例的指针。double *positionY即输入框顶点与物理屏幕上侧距离的绝对值，单位px。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_TextAvoidInfo_GetHeight()

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_GetHeight(InputMethod_TextAvoidInfo *info, double *height)
```

**描述**

从[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)获取高度值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md) *info指向即将被获取值的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例的指针。double *height输入框高度。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。