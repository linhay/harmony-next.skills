# inputmethod_text_avoid_info_capi.h

**概述**

提供输入框避让信息对象的创建、销毁与读写方法。

引用文件： <inputmethod/inputmethod_text_avoid_info_capi.h>

库： libohinputmethod.so

系统能力： SystemCapability.MiscServices.InputMethodFramework

起始版本： 12

相关模块： [InputMethod](InputMethod.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| InputMethod_TextAvoidInfo | InputMethod_TextAvoidInfo | 输入框避让信息。输入框用于避让键盘的信息。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| InputMethod_TextAvoidInfo *OH_TextAvoidInfo_Create(double positionY, double height) | 创建一个新的InputMethod_TextAvoidInfo实例。 |
| void OH_TextAvoidInfo_Destroy(InputMethod_TextAvoidInfo *info) | 销毁一个InputMethod_TextAvoidInfo实例。 |
| InputMethod_ErrorCode OH_TextAvoidInfo_SetPositionY(InputMethod_TextAvoidInfo *info, double positionY) | 设置InputMethod_TextAvoidInfo中的Y坐标值。 |
| InputMethod_ErrorCode OH_TextAvoidInfo_SetHeight(InputMethod_TextAvoidInfo *info, double height) | 设置InputMethod_TextAvoidInfo中的高度值。 |
| InputMethod_ErrorCode OH_TextAvoidInfo_GetPositionY(InputMethod_TextAvoidInfo *info, double *positionY) | 从InputMethod_TextAvoidInfo获取Y坐标值。 |
| InputMethod_ErrorCode OH_TextAvoidInfo_GetHeight(InputMethod_TextAvoidInfo *info, double *height) | 从InputMethod_TextAvoidInfo获取高度值。 |

**函数说明**

**OH_TextAvoidInfo_Create()**

```ets
InputMethod_TextAvoidInfo *OH_TextAvoidInfo_Create(double positionY, double height)
```

描述

创建一个新的[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| double positionY | 表示输入框位置的Y坐标值，单位px。 |
| double height | 表示输入框高度，单位px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_TextAvoidInfo * | 如果创建成功，返回一个指向新创建的InputMethod_TextAvoidInfo实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

**OH_TextAvoidInfo_Destroy()**

```ets
void OH_TextAvoidInfo_Destroy(InputMethod_TextAvoidInfo *info)
```

描述

销毁一个[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextAvoidInfo *info | 表示指向即将被销毁的InputMethod_TextAvoidInfo实例的指针。 |

**OH_TextAvoidInfo_SetPositionY()**

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_SetPositionY(InputMethod_TextAvoidInfo *info, double positionY)
```

描述

设置[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)中的Y坐标值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextAvoidInfo *info | 指向即将被设置值的InputMethod_TextAvoidInfo实例的指针。 |
| double positionY | Y坐标值，即输入框顶点与物理屏幕上侧距离的绝对值，单位px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextAvoidInfo_SetHeight()**

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_SetHeight(InputMethod_TextAvoidInfo *info, double height)
```

描述

设置[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)中的高度值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextAvoidInfo *info | 指向即将被设置值的InputMethod_TextAvoidInfo实例的指针。 |
| double height | 高度值，单位px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextAvoidInfo_GetPositionY()**

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_GetPositionY(InputMethod_TextAvoidInfo *info, double *positionY)
```

描述

从[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)获取Y坐标值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextAvoidInfo *info | 指向即将被获取值的InputMethod_TextAvoidInfo实例的指针。 |
| double *positionY | Y坐标值，即输入框顶点与物理屏幕上侧距离的绝对值，单位px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextAvoidInfo_GetHeight()**

```ets
InputMethod_ErrorCode OH_TextAvoidInfo_GetHeight(InputMethod_TextAvoidInfo *info, double *height)
```

描述

从[InputMethod_TextAvoidInfo](InputMethod_TextAvoidInfo.md)获取高度值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextAvoidInfo *info | 指向即将被获取值的InputMethod_TextAvoidInfo实例的指针。 |
| double *height | 输入框高度，单位px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |