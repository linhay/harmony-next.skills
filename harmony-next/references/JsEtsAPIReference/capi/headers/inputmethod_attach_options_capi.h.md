# inputmethod_attach_options_capi.h

#### 概述

提供输入法绑定选项对象的创建、销毁与读写方法。

**引用文件：** <inputmethod/inputmethod_attach_options_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：**[InputMethod](../../topics/input/InputMethod.md)

#### 汇总

#### 结构体

名称typedef关键字描述[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)InputMethod_AttachOptions输入法绑定选项。绑定输入法时携带的选项。

#### 函数

名称描述[InputMethod_AttachOptions *OH_AttachOptions_Create(bool showKeyboard)](#ZH-CN_TOPIC_0000002529285285__oh_attachoptions_create)创建一个新的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。[InputMethod_AttachOptions *OH_AttachOptions_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod_RequestKeyboardReason requestKeyboardReason)](#ZH-CN_TOPIC_0000002529285285__oh_attachoptions_createwithrequestkeyboardreason)创建一个新的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。[void OH_AttachOptions_Destroy(InputMethod_AttachOptions *options)](#ZH-CN_TOPIC_0000002529285285__oh_attachoptions_destroy)销毁一个[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。[InputMethod_ErrorCode OH_AttachOptions_IsShowKeyboard(InputMethod_AttachOptions *options, bool *showKeyboard)](#ZH-CN_TOPIC_0000002529285285__oh_attachoptions_isshowkeyboard)从[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)中获取是否显示键盘的值。[InputMethod_ErrorCode OH_AttachOptions_GetRequestKeyboardReason(InputMethod_AttachOptions *options, int *requestKeyboardReason)](#ZH-CN_TOPIC_0000002529285285__oh_attachoptions_getrequestkeyboardreason)从[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)中获取请求软键盘输入的原因。

#### 函数说明

#### OH_AttachOptions_Create()

```ets
InputMethod_AttachOptions *OH_AttachOptions_Create(bool showKeyboard)
```

**描述**

创建一个新的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。

**起始版本：** 12

**参数：**

参数项描述bool showKeyboard表示绑定时是否显示键盘。true - 表示绑定完成时需要显示键盘。false - 表示绑定完成时不需要显示键盘。

**返回：**

类型说明[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md) *

如果创建成功，返回一个指向新创建的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例的指针。

 如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。

#### OH_AttachOptions_CreateWithRequestKeyboardReason()

```ets
InputMethod_AttachOptions *OH_AttachOptions_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod_RequestKeyboardReason requestKeyboardReason)
```

**描述**

创建一个新的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。

**起始版本：** 15

**参数：**

参数项描述bool showKeyboard表示绑定时是否显示键盘。true - 表示绑定完成时需要显示键盘。false - 表示绑定完成时不需要显示键盘。[InputMethod_RequestKeyboardReason](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_requestkeyboardreason) requestKeyboardReason表示请求键盘输入的原因。

**返回：**

类型说明[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md) *

如果创建成功，返回一个指向新创建的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例的指针。

 如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。

#### OH_AttachOptions_Destroy()

```ets
void OH_AttachOptions_Destroy(InputMethod_AttachOptions *options)
```

**描述**

销毁一个[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md) *options表示即将被销毁的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。

#### OH_AttachOptions_IsShowKeyboard()

```ets
InputMethod_ErrorCode OH_AttachOptions_IsShowKeyboard(InputMethod_AttachOptions *options, bool *showKeyboard)
```

**描述**

从[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)中获取是否显示键盘的值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md) *options表示被读取值的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。bool *showKeyboard表示绑定时是否显示键盘。true - 表示绑定完成时需要显示键盘。false - 表示绑定完成时不需要显示键盘。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_AttachOptions_GetRequestKeyboardReason()

```ets
InputMethod_ErrorCode OH_AttachOptions_GetRequestKeyboardReason(InputMethod_AttachOptions *options, int *requestKeyboardReason)
```

**描述**

从[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)中获取请求键盘的原因。

**起始版本：** 15

**参数：**

参数项描述[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md) *options表示被读取值的[InputMethod_AttachOptions](../../topics/input/InputMethod_AttachOptions.md)实例。int *requestKeyboardReason表示请求键盘输入的原因。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。