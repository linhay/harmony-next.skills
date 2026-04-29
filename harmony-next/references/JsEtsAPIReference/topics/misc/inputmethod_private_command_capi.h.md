# inputmethod_private_command_capi.h

**概述**

提供私有数据对象的创建、销毁与读写方法。

引用文件： <inputmethod/inputmethod_private_command_capi.h>

库： libohinputmethod.so

系统能力： SystemCapability.MiscServices.InputMethodFramework

起始版本： 12

相关模块： [InputMethod](InputMethod.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| InputMethod_PrivateCommand | InputMethod_PrivateCommand | 表示私有数据的结构体类型。输入框和输入法应用之间交互的私有数据。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *OH_PrivateCommand_Create(char key[], size_t keyLength) | 创建一个新的InputMethod_PrivateCommand实例。 |
| void OH_PrivateCommand_Destroy(InputMethod_PrivateCommand *command) | 销毁一个InputMethod_PrivateCommand实例。 |
| InputMethod_ErrorCode OH_PrivateCommand_SetKey(InputMethod_PrivateCommand *command, char key[], size_t keyLength) | 设置InputMethod_PrivateCommand的key值。 |
| InputMethod_ErrorCode OH_PrivateCommand_SetBoolValue(InputMethod_PrivateCommand *command, bool value) | 设置InputMethod_PrivateCommand的布尔类型value值。 |
| InputMethod_ErrorCode OH_PrivateCommand_SetIntValue(InputMethod_PrivateCommand *command, int32_t value) | 设置InputMethod_PrivateCommand的整数类型value值。 |
| InputMethod_ErrorCode OH_PrivateCommand_SetStrValue(InputMethod_PrivateCommand *command, char value[], size_t valueLength) | 设置InputMethod_PrivateCommand的字符串类型value值。 |
| InputMethod_ErrorCode OH_PrivateCommand_GetKey(InputMethod_PrivateCommand *command, const char **key, size_t *keyLength) | 从InputMethod_PrivateCommand获取key值。 |
| InputMethod_ErrorCode OH_PrivateCommand_GetValueType(InputMethod_PrivateCommand *command, InputMethod_CommandValueType *type) | 从InputMethod_PrivateCommand获取value的数据类型。 |
| InputMethod_ErrorCode OH_PrivateCommand_GetBoolValue(InputMethod_PrivateCommand *command, bool *value) | 从InputMethod_PrivateCommand获取布尔类型的value的值。 |
| InputMethod_ErrorCode OH_PrivateCommand_GetIntValue(InputMethod_PrivateCommand *command, int32_t *value) | 从InputMethod_PrivateCommand获取整数类型的value的值。 |
| InputMethod_ErrorCode OH_PrivateCommand_GetStrValue(InputMethod_PrivateCommand *command, const char **value, size_t *valueLength) | 从InputMethod_PrivateCommand获取字符串类型的value的值。 |

**函数说明**

**OH_PrivateCommand_Create()**

```ets
InputMethod_PrivateCommand *OH_PrivateCommand_Create(char key[], size_t keyLength)
```

描述

创建一个新的[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| char key[] | 私有数据的key值。 |
| size_t keyLength | key长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_PrivateCommand * | 如果创建成功，返回一个指向新创建的InputMethod_PrivateCommand实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

**OH_PrivateCommand_Destroy()**

```ets
void OH_PrivateCommand_Destroy(InputMethod_PrivateCommand *command)
```

描述

销毁一个[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被销毁的InputMethod_PrivateCommand实例的指针。 |

**OH_PrivateCommand_SetKey()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetKey(InputMethod_PrivateCommand *command, char key[], size_t keyLength)
```

描述

设置[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)的key值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被设置的InputMethod_PrivateCommand实例的指针。 |
| char key[] | key值。 |
| size_t keyLength | key长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_SetBoolValue()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetBoolValue(InputMethod_PrivateCommand *command, bool value)
```

描述

设置[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)的布尔类型value值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被设置的InputMethod_PrivateCommand实例的指针。 |
| bool value | 布尔类型value值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_SetIntValue()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetIntValue(InputMethod_PrivateCommand *command, int32_t value)
```

描述

设置[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)的整数类型value值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被设置的InputMethod_PrivateCommand实例的指针。 |
| int32_t value | 整数类型的value的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_SetStrValue()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_SetStrValue(InputMethod_PrivateCommand *command, char value[], size_t valueLength)
```

描述

设置[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)的字符串类型value值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被设置的InputMethod_PrivateCommand实例的指针。 |
| char value[] | 字符串类型value值。 |
| size_t valueLength | 表示字符串数据值的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_GetKey()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetKey(InputMethod_PrivateCommand *command, const char **key, size_t *keyLength)
```

描述

从[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)获取key值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被获取key值的InputMethod_PrivateCommand实例的指针。 |
| const char **key | key的生命周期和command一致。不要直接保存key地址，或者直接写key。建议拷贝后使用。 |
| size_t *keyLength | key长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_GetValueType()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetValueType(InputMethod_PrivateCommand *command, InputMethod_CommandValueType *type)
```

描述

从[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)获取value的数据类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被获取value值的InputMethod_PrivateCommand实例的指针。 |
| InputMethod_CommandValueType *type | 表示指向 InputMethod_CommandValueType 实例的指针。 用于value值的数据类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_GetBoolValue()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetBoolValue(InputMethod_PrivateCommand *command, bool *value)
```

描述

从[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)获取布尔类型的value的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被获取value值的InputMethod_PrivateCommand实例的指针。 |
| bool *value | 布尔类型的value的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  IME_ERR_QUERY_FAILED - 查询失败，命令中没有布尔值。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_GetIntValue()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetIntValue(InputMethod_PrivateCommand *command, int32_t *value)
```

描述

从[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)获取整数类型的value的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被获取value值的InputMethod_PrivateCommand实例的指针。 |
| int32_t *value | 整数类型的value的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  IME_ERR_QUERY_FAILED - 查询失败，命令中没有整数值。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_PrivateCommand_GetStrValue()**

```ets
InputMethod_ErrorCode OH_PrivateCommand_GetStrValue(InputMethod_PrivateCommand *command, const char **value, size_t *valueLength)
```

描述

从[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)获取字符串类型的value的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_PrivateCommand *command | 指向即将被获取value值的InputMethod_PrivateCommand实例的指针。 |
| const char **value | 字符串类型的value的值。 |
| size_t *valueLength | value的生命周期和command一致。不要直接保存value地址，或者直接写value。建议拷贝后使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  IME_ERR_QUERY_FAILED - 查询失败，命令中没有字符串值。  具体错误码可以参考 InputMethod_ErrorCode。 |