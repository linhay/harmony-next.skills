# inputmethod_attach_options_capi.h

**概述**

提供输入法绑定选项对象的创建、销毁与读写方法。

引用文件： <inputmethod/inputmethod_attach_options_capi.h>

库： libohinputmethod.so

系统能力： SystemCapability.MiscServices.InputMethodFramework

起始版本： 12

相关模块： [InputMethod](InputMethod.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| InputMethod_AttachOptions | InputMethod_AttachOptions | 输入法绑定选项。绑定输入法时携带的选项。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| InputMethod_AttachOptions *OH_AttachOptions_Create(bool showKeyboard) | 创建一个新的InputMethod_AttachOptions实例。 |
| InputMethod_AttachOptions *OH_AttachOptions_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod_RequestKeyboardReason requestKeyboardReason) | 创建一个新的InputMethod_AttachOptions实例。 |
| void OH_AttachOptions_Destroy(InputMethod_AttachOptions *options) | 销毁一个InputMethod_AttachOptions实例。 |
| InputMethod_ErrorCode OH_AttachOptions_IsShowKeyboard(InputMethod_AttachOptions *options, bool *showKeyboard) | 从InputMethod_AttachOptions中获取是否显示键盘的值。 |
| InputMethod_ErrorCode OH_AttachOptions_GetRequestKeyboardReason(InputMethod_AttachOptions *options, int *requestKeyboardReason) | 从InputMethod_AttachOptions中获取触发输入法拉起的场景原因。 |

**函数说明**

**OH_AttachOptions_Create()**

```ets
InputMethod_AttachOptions *OH_AttachOptions_Create(bool showKeyboard)
```

描述

创建一个新的[InputMethod_AttachOptions](InputMethod_AttachOptions.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| bool showKeyboard | 表示绑定时是否显示键盘。true - 表示绑定完成时需要显示键盘。false - 表示绑定完成时不需要显示键盘。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_AttachOptions * | 如果创建成功，返回一个指向新创建的InputMethod_AttachOptions实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

**OH_AttachOptions_CreateWithRequestKeyboardReason()**

```ets
InputMethod_AttachOptions *OH_AttachOptions_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod_RequestKeyboardReason requestKeyboardReason)
```

描述

创建一个新的[InputMethod_AttachOptions](InputMethod_AttachOptions.md)实例。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| bool showKeyboard | 表示绑定时是否显示键盘。true - 表示绑定完成时需要显示键盘。false - 表示绑定完成时不需要显示键盘。 |
| InputMethod_RequestKeyboardReason requestKeyboardReason | 表示请求键盘输入的原因。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_AttachOptions * | 如果创建成功，返回一个指向新创建的InputMethod_AttachOptions实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

**OH_AttachOptions_Destroy()**

```ets
void OH_AttachOptions_Destroy(InputMethod_AttachOptions *options)
```

描述

销毁一个[InputMethod_AttachOptions](InputMethod_AttachOptions.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_AttachOptions *options | 表示即将被销毁的InputMethod_AttachOptions实例。 |

**OH_AttachOptions_IsShowKeyboard()**

```ets
InputMethod_ErrorCode OH_AttachOptions_IsShowKeyboard(InputMethod_AttachOptions *options, bool *showKeyboard)
```

描述

从[InputMethod_AttachOptions](InputMethod_AttachOptions.md)中获取是否显示键盘的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_AttachOptions *options | 表示被读取值的InputMethod_AttachOptions实例。 |
| bool *showKeyboard | 表示绑定时是否显示键盘。true - 表示绑定完成时需要显示键盘。false - 表示绑定完成时不需要显示键盘。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_AttachOptions_GetRequestKeyboardReason()**

```ets
InputMethod_ErrorCode OH_AttachOptions_GetRequestKeyboardReason(InputMethod_AttachOptions *options, int *requestKeyboardReason)
```

描述

从[InputMethod_AttachOptions](InputMethod_AttachOptions.md)中获取请求键盘的原因。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_AttachOptions *options | 表示被读取值的InputMethod_AttachOptions实例。 |
| int *requestKeyboardReason | 表示请求键盘输入的原因。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |