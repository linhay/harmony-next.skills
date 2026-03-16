# inputmethod_private_command_capi.h

#### 概述

提供私有数据对象的创建、销毁与读写方法。

**引用文件：** <inputmethod/inputmethod_private_command_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：**[InputMethod](../../topics/input/InputMethod.md)

#### 汇总

#### 结构体

名称typedef关键字描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)InputMethod_PrivateCommand表示私有数据的结构体类型。输入框和输入法应用之间交互的私有数据。

#### 函数

名称描述[InputMethod_PrivateCommand *OH_PrivateCommand_Create(char key[], size_t keyLength)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_create)创建一个新的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例。[void OH_PrivateCommand_Destroy(InputMethod_PrivateCommand *command)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_destroy)销毁一个[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例。[InputMethod_ErrorCode OH_PrivateCommand_SetKey(InputMethod_PrivateCommand *command, char key[], size_t keyLength)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_setkey)设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的key值。[InputMethod_ErrorCode OH_PrivateCommand_SetBoolValue(InputMethod_PrivateCommand *command, bool value)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_setboolvalue)设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的布尔类型value值。[InputMethod_ErrorCode OH_PrivateCommand_SetIntValue(InputMethod_PrivateCommand *command, int32_t value)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_setintvalue)设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的整数类型value值。[InputMethod_ErrorCode OH_PrivateCommand_SetStrValue(InputMethod_PrivateCommand *command, char value[], size_t valueLength)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_setstrvalue)设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的字符串类型value值。[InputMethod_ErrorCode OH_PrivateCommand_GetKey(InputMethod_PrivateCommand *command, const char **key, size_t *keyLength)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_getkey)从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取key值。[InputMethod_ErrorCode OH_PrivateCommand_GetValueType(InputMethod_PrivateCommand *command, InputMethod_CommandValueType *type)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_getvaluetype)从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取value的数据类型。[InputMethod_ErrorCode OH_PrivateCommand_GetBoolValue(InputMethod_PrivateCommand *command, bool *value)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_getboolvalue)从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取布尔类型的value的值。[InputMethod_ErrorCode OH_PrivateCommand_GetIntValue(InputMethod_PrivateCommand *command, int32_t *value)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_getintvalue)从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取整数类型的value的值。[InputMethod_ErrorCode OH_PrivateCommand_GetStrValue(InputMethod_PrivateCommand *command, const char **value, size_t *valueLength)](#ZH-CN_TOPIC_0000002529285287__oh_privatecommand_getstrvalue)从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取字符串类型的value的值。

#### 函数说明

#### OH_PrivateCommand_Create()

```ets
InputMethod_PrivateCommand *OH_PrivateCommand_Create(char key[], size_t keyLength)
```

**描述**

创建一个新的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例。

**起始版本：** 12

**参数：**

参数项描述char key[]私有数据的key值。size_t keyLengthkey长度。

**返回：**

类型说明[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *

如果创建成功，返回一个指向新创建的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。

 如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。

#### OH_PrivateCommand_Destroy()

```ets
void OH_PrivateCommand_Destroy(InputMethod_PrivateCommand *command)
```

**描述**

销毁一个[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被销毁的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。

#### OH_PrivateCommand_SetKey()

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetKey(InputMethod_PrivateCommand *command, char key[], size_t keyLength)
```

**描述**

设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的key值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被设置的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。char key[]key值。size_t keyLengthkey长度。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_SetBoolValue()

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetBoolValue(InputMethod_PrivateCommand *command, bool value)
```

**描述**

设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的布尔类型value值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被设置的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。bool value布尔类型value值。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_SetIntValue()

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetIntValue(InputMethod_PrivateCommand *command, int32_t value)
```

**描述**

设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的整数类型value值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被设置的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。int32_t value整型value值。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_SetStrValue()

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetStrValue(InputMethod_PrivateCommand *command, char value[], size_t valueLength)
```

**描述**

设置[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)的字符串类型value值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被设置的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。char value[]字符串类型value值。size_t valueLength表示字符串数据值的长度。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_GetKey()

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetKey(InputMethod_PrivateCommand *command, const char **key, size_t *keyLength)
```

**描述**

从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取key值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被获取key值的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。const char **keykey的生命周期和command一致。不要直接保存key地址，或者直接写key。建议拷贝后使用。size_t *keyLengthkey长度。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_GetValueType()

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetValueType(InputMethod_PrivateCommand *command, InputMethod_CommandValueType *type)
```

**描述**

从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取value的数据类型。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被获取value值的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。[InputMethod_CommandValueType](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_commandvaluetype) *type表示指向 [InputMethod_CommandValueType](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_commandvaluetype) 实例的指针。 用于value值的数据类型。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_GetBoolValue()

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetBoolValue(InputMethod_PrivateCommand *command, bool *value)
```

**描述**

从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取布尔类型的value的值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被获取value值的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。bool *value布尔类型的value的值。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

[IME_ERR_QUERY_FAILED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 查询失败，命令中没有布尔值。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_GetIntValue()

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetIntValue(InputMethod_PrivateCommand *command, int32_t *value)
```

**描述**

从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取整数类型的value的值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被获取value值的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。int32_t *value整数类型的value的值。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

[IME_ERR_QUERY_FAILED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 查询失败，命令中没有布尔值。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_PrivateCommand_GetStrValue()

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetStrValue(InputMethod_PrivateCommand *command, const char **value, size_t *valueLength)
```

**描述**

从[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)获取字符串类型的value的值。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md) *command指向即将被获取value值的[InputMethod_PrivateCommand](../../topics/input/InputMethod_PrivateCommand.md)实例的指针。const char **value字符串类型的value的值。size_t *valueLengthvalue的生命周期和command一致。不要直接保存value地址，或者直接写value。建议拷贝后使用。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

[IME_ERR_QUERY_FAILED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 查询失败，命令中没有布尔值。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。