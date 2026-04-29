# inputmethod_text_config_capi.h

**概述**

提供输入框配置信息对象的创建、销毁与读写方法。

引用文件： <inputmethod/inputmethod_text_config_capi.h>

库： libohinputmethod.so

系统能力： SystemCapability.MiscServices.InputMethodFramework

起始版本： 12

相关模块： [InputMethod](InputMethod.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| InputMethod_TextConfig | InputMethod_TextConfig | 输入框的配置信息。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| InputMethod_TextConfig *OH_TextConfig_Create(void) | 创建一个新的InputMethod_TextConfig实例。 |
| void OH_TextConfig_Destroy(InputMethod_TextConfig *config) | 销毁一个InputMethod_TextConfig实例。 |
| InputMethod_ErrorCode OH_TextConfig_SetInputType(InputMethod_TextConfig *config, InputMethod_TextInputType inputType) | 设置文本配置信息中的输入框类型。 |
| InputMethod_ErrorCode OH_TextConfig_SetEnterKeyType(InputMethod_TextConfig *config, InputMethod_EnterKeyType enterKeyType) | 设置文本配置信息中的回车键功能类型。 |
| InputMethod_ErrorCode OH_TextConfig_SetPreviewTextSupport(InputMethod_TextConfig *config, bool supported) | 将预上屏支持情况设置到文本配置信息中。 |
| InputMethod_ErrorCode OH_TextConfig_SetSelection(InputMethod_TextConfig *config, int32_t start, int32_t end) | 设置文本配置信息中的选中文本范围。 |
| InputMethod_ErrorCode OH_TextConfig_SetWindowId(InputMethod_TextConfig *config, int32_t windowId) | 设置文本配置信息中所属窗口的窗口id。 |
| InputMethod_ErrorCode OH_TextConfig_SetPlaceholder(InputMethod_TextConfig *config, const char16_t *placeholder,size_t length) | 设置文本配置信息中的占位符文本信息。 |
| InputMethod_ErrorCode OH_TextConfig_SetAbilityName(InputMethod_TextConfig *config, const char16_t *abilityName,size_t length) | 设置文本配置信息中的abilityName信息。 |
| InputMethod_ErrorCode OH_TextConfig_GetInputType(InputMethod_TextConfig *config, InputMethod_TextInputType *inputType) | 获取文本配置信息中的输入框类型。 |
| InputMethod_ErrorCode OH_TextConfig_GetEnterKeyType(InputMethod_TextConfig *config, InputMethod_EnterKeyType *enterKeyType) | 获取文本配置信息中的回车键功能类型。 |
| InputMethod_ErrorCode OH_TextConfig_IsPreviewTextSupported(InputMethod_TextConfig *config, bool *supported) | 获取文本配置中是否支持预上屏。 |
| InputMethod_ErrorCode OH_TextConfig_GetCursorInfo(InputMethod_TextConfig *config, InputMethod_CursorInfo **cursorInfo) | 获取文本配置信息中的光标信息。 |
| InputMethod_ErrorCode OH_TextConfig_GetTextAvoidInfo(InputMethod_TextConfig *config, InputMethod_TextAvoidInfo **avoidInfo) | 获取文本配置信息中的避让信息。 |
| InputMethod_ErrorCode OH_TextConfig_GetSelection(InputMethod_TextConfig *config, int32_t *start, int32_t *end) | 获取文本配置信息中的选区范围信息。 |
| InputMethod_ErrorCode OH_TextConfig_GetWindowId(InputMethod_TextConfig *config, int32_t *windowId) | 获取文本配置信息中所属窗口的窗口id。 |
| InputMethod_ErrorCode OH_TextConfig_GetPlaceholder(InputMethod_TextConfig *config, char16_t *placeholder,size_t *length) | 获取文本配置信息中的占位符文本信息。 |
| InputMethod_ErrorCode OH_TextConfig_GetAbilityName(InputMethod_TextConfig *config, char16_t *abilityName,size_t *length) | 获取文本配置信息中的abilityName信息。 |

**函数说明**

**OH_TextConfig_Create()**

```ets
InputMethod_TextConfig *OH_TextConfig_Create(void)
```

描述

创建一个新的[InputMethod_TextConfig](InputMethod_TextConfig.md)实例。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_TextConfig * | 如果创建成功，返回一个指向新创建的InputMethod_TextConfig实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

**OH_TextConfig_Destroy()**

```ets
void OH_TextConfig_Destroy(InputMethod_TextConfig *config)
```

描述

销毁一个[InputMethod_TextConfig](InputMethod_TextConfig.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 表示指向即将被销毁的InputMethod_TextConfig实例的指针。 |

**OH_TextConfig_SetInputType()**

```ets
InputMethod_ErrorCode OH_TextConfig_SetInputType(InputMethod_TextConfig *config, InputMethod_TextInputType inputType)
```

描述

设置文本配置信息中的输入框类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被设置值的InputMethod_TextConfig实例的指针。 |
| InputMethod_TextInputType inputType | 输入框的输入类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_SetEnterKeyType()**

```ets
InputMethod_ErrorCode OH_TextConfig_SetEnterKeyType(InputMethod_TextConfig *config, InputMethod_EnterKeyType enterKeyType)
```

描述

设置文本配置信息中的回车键功能类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被设置值的InputMethod_TextConfig实例的指针。 |
| InputMethod_EnterKeyType enterKeyType | 回车键功能类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_SetPreviewTextSupport()**

```ets
InputMethod_ErrorCode OH_TextConfig_SetPreviewTextSupport(InputMethod_TextConfig *config, bool supported)
```

描述

将预上屏支持情况设置到文本配置信息中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被设置值的InputMethod_TextConfig实例的指针。 |
| bool supported | 表示输入框是否支持预上屏。true - 表示支持预上屏。false - 表示不支持预上屏。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_SetSelection()**

```ets
InputMethod_ErrorCode OH_TextConfig_SetSelection(InputMethod_TextConfig *config, int32_t start, int32_t end)
```

描述

设置文本配置信息中的选中文本范围。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被设置值的InputMethod_TextConfig实例的指针。 |
| int32_t start | 所选文本的起始位置。 |
| int32_t end | 所选文本的结束位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_SetWindowId()**

```ets
InputMethod_ErrorCode OH_TextConfig_SetWindowId(InputMethod_TextConfig *config, int32_t windowId)
```

描述

设置文本配置信息中所属窗口的窗口id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被设置值的InputMethod_TextConfig实例的指针。 |
| int32_t windowId | 绑定输入法的应用所属窗口的窗口id。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_SetPlaceholder()**

```ets
InputMethod_ErrorCode OH_TextConfig_SetPlaceholder(InputMethod_TextConfig *config, const char16_t *placeholder,size_t length)
```

描述

设置文本配置信息中的占位符文本信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被设置值的InputMethod_TextConfig实例的指针。 |
| const char16_t *placeholder | 指向UTF-16编码的双字节指针；若传空指针，则会将占位文本信息设置为空字符串。 |
| size_t length | placeholder指针指向内存所包含的元素个数，包含最后的字符串结尾符，计数单位为双字节。1. 如果长度为0，占位文本信息会被设置为空字符串。2. UTF-16编码的最大长度为255个字符（如果最后一位是字符串结尾符，不包含在计数中），超过255个字符数将会被截断。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | InputMethod_ErrorCode：  IME_ERR_OK = 0：表示成功。  IME_ERR_NULL_POINTER = 12802000：非预期的空指针。 |

**OH_TextConfig_SetAbilityName()**

```ets
InputMethod_ErrorCode OH_TextConfig_SetAbilityName(InputMethod_TextConfig *config, const char16_t *abilityName,size_t length)
```

描述

设置文本配置信息中的abilityName信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被设置值的InputMethod_TextConfig实例的指针。 |
| const char16_t *abilityName | 指向UTF-16编码的双字节指针；若传空指针，则会将abilityName设置为空字符串。 |
| size_t length | abilityName指针指向内存所包含的元素个数，包含最后的字符串结尾符，计数单位为双字节。1. 如果长度为0，abilityName会被设置为空字符串。2. UTF-16编码的最大长度为127个字符（如果最后一位是字符串结尾符，不包含在计数中），超过127个字符数将会被截断。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | InputMethod_ErrorCode：  IME_ERR_OK = 0：表示成功。  IME_ERR_NULL_POINTER = 12802000：非预期的空指针。 |

**OH_TextConfig_GetInputType()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetInputType(InputMethod_TextConfig *config, InputMethod_TextInputType *inputType)
```

描述

获取文本配置信息中的输入框类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| InputMethod_TextInputType *inputType | 表示指向InputMethod_TextInputType实例的指针。 输入框的输入类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_GetEnterKeyType()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetEnterKeyType(InputMethod_TextConfig *config, InputMethod_EnterKeyType *enterKeyType)
```

描述

获取文本配置信息中的回车键功能类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| InputMethod_EnterKeyType *enterKeyType | 表示指向InputMethod_EnterKeyType实例的指针。 输入框的回车键功能类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_IsPreviewTextSupported()**

```ets
InputMethod_ErrorCode OH_TextConfig_IsPreviewTextSupported(InputMethod_TextConfig *config, bool *supported)
```

描述

获取文本配置中是否支持预上屏。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| bool *supported | 表示输入框是否支持预上屏。true - 表示支持预上屏。false - 表示不支持预上屏。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_GetCursorInfo()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetCursorInfo(InputMethod_TextConfig *config, InputMethod_CursorInfo **cursorInfo)
```

描述

获取文本配置信息中的光标信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| InputMethod_CursorInfo **cursorInfo | 光标信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_GetTextAvoidInfo()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetTextAvoidInfo(InputMethod_TextConfig *config, InputMethod_TextAvoidInfo **avoidInfo)
```

描述

获取文本配置信息中的避让信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 表示文本配置信息。 |
| InputMethod_TextAvoidInfo **avoidInfo | 输入框避让信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_GetSelection()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetSelection(InputMethod_TextConfig *config, int32_t *start, int32_t *end)
```

描述

获取文本配置信息中的选区范围信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| int32_t *start | 所选文本的起始位置。 |
| int32_t *end | 所选文本的结束位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_GetWindowId()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetWindowId(InputMethod_TextConfig *config, int32_t *windowId)
```

描述

获取文本配置信息中所属窗口的窗口id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| int32_t *windowId | 绑定输入法的应用所属窗口的窗口id。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_TextConfig_GetPlaceholder()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetPlaceholder(InputMethod_TextConfig *config, char16_t *placeholder,size_t *length)
```

描述

获取文本配置信息中的占位符文本信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| char16_t *placeholder | 用于存放占位文本信息，该指针内存由调用者维护。 |
| size_t *length | 占位文本信息长度，计数单位为双字节，长度包含字符串结尾符。1. 作为入参，代表placeholder指向的内存可用长度。作为出参，代表实际的占位文本长度。2. 如果placeholder为空指针，且length指向有效内存，则length会被填充实际的占位文本长度。接口会返错。3. 如果placeholder和length都指向有效内存，但length传入的长度小于实际的占位文本长度，则length会被填充实际的占位文本长度。接口会返错。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | InputMethod_ErrorCode：  IME_ERR_OK = 0：表示成功。  IME_ERR_PARAMCHECK = 401：参数检查失败。  IME_ERR_NULL_POINTER = 12802000：非预期的空指针。 |

**OH_TextConfig_GetAbilityName()**

```ets
InputMethod_ErrorCode OH_TextConfig_GetAbilityName(InputMethod_TextConfig *config, char16_t *abilityName,size_t *length)
```

描述

获取文本配置信息中的abilityName信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextConfig *config | 指向即将被获取值的InputMethod_TextConfig实例的指针。 |
| char16_t *abilityName | 用于存放abilityName，该指针内存由调用者维护。 |
| size_t *length | abilityName长度，计数单位为双字节，长度包含字符串结尾符。1. 作为入参，代表abilityName指向的内存可用长度。作为出参，代表实际的abilityName长度。2. 如果abilityName为空指针，且length指向有效内存，则length会被填充实际的abilityName长度。接口会返错。3. 如果abilityName和length都指向有效内存，但length传入的长度小于实际的abilityName长度，则length会被填充实际的abilityName长度。接口会返错。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | InputMethod_ErrorCode：  IME_ERR_OK = 0：表示成功。  IME_ERR_PARAMCHECK = 401：参数检查失败。  IME_ERR_NULL_POINTER = 12802000：非预期的空指针。 |