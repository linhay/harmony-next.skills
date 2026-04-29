# native_huks_param.h

**概述**

提供参数集构造、使用和销毁的API。

引用文件： <huks/native_huks_param.h>

库： libhuks_ndk.z.so

系统能力： SystemCapability.Security.Huks.Core

在API 9-19，系统能力为SystemCapability.Security.Huks；从API 20起，系统能力变更为SystemCapability.Security.Huks.Core

起始版本： 9

相关模块： [HuksParamSetApi](HuksParamSetApi.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| struct OH_Huks_Result OH_Huks_InitParamSet(struct OH_Huks_ParamSet **paramSet) | 初始化参数集，无参数信息，分配参数集默认可用内存空间。初始化后的参数集需要通过OH_Huks_FreeParamSet释放。添加参数的参数集需要使用OH_Huks_AddParams添加参数并且必须使用OH_Huks_BuildParamSet构造参数集。 |
| struct OH_Huks_Result OH_Huks_AddParams(struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Param *params, uint32_t paramCnt) | 添加参数到参数集里面。 |
| struct OH_Huks_Result OH_Huks_BuildParamSet(struct OH_Huks_ParamSet **paramSet) | 构造参数集，在初始化参数集和添加参数操作之后，序列化参数集，将blob类型的数据拷贝到paramSet结构尾部相邻内存区域。 |
| void OH_Huks_FreeParamSet(struct OH_Huks_ParamSet **paramSet) | 销毁参数集。 |
| struct OH_Huks_Result OH_Huks_CopyParamSet(const struct OH_Huks_ParamSet *fromParamSet, uint32_t fromParamSetSize, struct OH_Huks_ParamSet **paramSet) | 复制参数集（深拷贝）。 |
| struct OH_Huks_Result OH_Huks_GetParam(const struct OH_Huks_ParamSet *paramSet, uint32_t tag, struct OH_Huks_Param **param) | 从参数集中获取参数。 |
| struct OH_Huks_Result OH_Huks_FreshParamSet(struct OH_Huks_ParamSet *paramSet, bool isCopy) | 刷新参数集内OH_Huks_Blob类型的数据。 |
| struct OH_Huks_Result OH_Huks_IsParamSetTagValid(const struct OH_Huks_ParamSet *paramSet) | 检查参数集中的参数是否有效、是否有重复。 |
| struct OH_Huks_Result OH_Huks_IsParamSetValid(const struct OH_Huks_ParamSet *paramSet, uint32_t size) | 检查参数集大小是否有效。 |
| struct OH_Huks_Result OH_Huks_CheckParamMatch(const struct OH_Huks_Param *baseParam, const struct OH_Huks_Param *param) | 比较两个参数是否相同。 |
| void OH_Huks_FreeKeyAliasSet(struct OH_Huks_KeyAliasSet *keyAliasSet) | 销毁密钥别名的参数集。 |

**函数说明**

**OH_Huks_InitParamSet()**

```ets
struct OH_Huks_Result OH_Huks_InitParamSet(struct OH_Huks_ParamSet **paramSet)
```

描述

初始化参数集，无参数信息，分配参数集默认可用内存空间。初始化后的参数集需要通过OH_Huks_FreeParamSet释放。添加参数的参数集需要使用OH_Huks_AddParams添加参数并且必须使用OH_Huks_BuildParamSet构造参数集。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_Huks_ParamSet **paramSet | 指向要初始化的参数集的指针地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：初始化操作成功。  OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数paramSet无效。 |

**OH_Huks_AddParams()**

```ets
struct OH_Huks_Result OH_Huks_AddParams(struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Param *params, uint32_t paramCnt)
```

描述

添加参数到参数集里面。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_Huks_ParamSet *paramSet | 指向要被添加参数的参数集的指针。 |
| const struct OH_Huks_Param *params | 指向要添加的参数数组的指针。 |
| uint32_t paramCnt | 待添加参数数组的参数个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：操作成功。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：params为null或者paramSet无效。 |

**OH_Huks_BuildParamSet()**

```ets
struct OH_Huks_Result OH_Huks_BuildParamSet(struct OH_Huks_ParamSet **paramSet)
```

描述

构造参数集，在初始化参数集和添加参数操作之后，序列化参数集，将blob类型的数据拷贝到paramSet结构尾部相邻内存区域。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_Huks_ParamSet **paramSet | 指向要被正式构造的参数集的指针地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：操作成功。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数paramSet无效。  OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。 |

**OH_Huks_FreeParamSet()**

```ets
void OH_Huks_FreeParamSet(struct OH_Huks_ParamSet **paramSet)
```

描述

销毁参数集。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_Huks_ParamSet **paramSet | 指向要被销毁的参数集的指针地址。 |

**OH_Huks_CopyParamSet()**

```ets
struct OH_Huks_Result OH_Huks_CopyParamSet(const struct OH_Huks_ParamSet *fromParamSet, uint32_t fromParamSetSize, struct OH_Huks_ParamSet **paramSet)
```

描述

复制参数集（深拷贝）。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const struct OH_Huks_ParamSet *fromParamSet | 指向要被复制的参数集的指针。 |
| uint32_t fromParamSetSize | 被复制的参数集占用内存的大小。 |
| struct OH_Huks_ParamSet **paramSet | 指向生成新的参数集的指针地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：操作成功。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数fromParamSet、fromParamSetSize、paramSet有一个无效。  OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。 |

**OH_Huks_GetParam()**

```ets
struct OH_Huks_Result OH_Huks_GetParam(const struct OH_Huks_ParamSet *paramSet, uint32_t tag, struct OH_Huks_Param **param)
```

描述

从参数集中获取参数。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const struct OH_Huks_ParamSet *paramSet | 指向参数集的指针。 |
| uint32_t tag | 要获取的对应参数的值。 |
| struct OH_Huks_Param **param | 指向获取到的参数的指针地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：操作成功。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数paramSet或者param无效，或者参数param不在paramSet里面。 |

**OH_Huks_FreshParamSet()**

```ets
struct OH_Huks_Result OH_Huks_FreshParamSet(struct OH_Huks_ParamSet *paramSet, bool isCopy)
```

描述

刷新参数集内[OH_Huks_Blob](OH_Huks_Blob.md)类型的数据。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_Huks_ParamSet *paramSet | 指向参数集的指针。 |
| bool isCopy | 如果为true，刷新OH_Huks_Blob类型数据的地址并复制到参数集。如果为false，只会刷新OH_Huks_Blob类型数据的地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：操作成功。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数paramSet无效。  OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。 |

**OH_Huks_IsParamSetTagValid()**

```ets
struct OH_Huks_Result OH_Huks_IsParamSetTagValid(const struct OH_Huks_ParamSet *paramSet)
```

描述

检查参数集中的参数是否有效、是否有重复。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const struct OH_Huks_ParamSet *paramSet | 指向参数集的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：paramSet中的参数都有效。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数paramSet无效或者参数集中有无效、重复、不正确的标签。 |

**OH_Huks_IsParamSetValid()**

```ets
struct OH_Huks_Result OH_Huks_IsParamSetValid(const struct OH_Huks_ParamSet *paramSet, uint32_t size)
```

描述

检查参数集大小是否有效。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const struct OH_Huks_ParamSet *paramSet | 指向参数集的指针。 |
| uint32_t size | 参数集占用的内存大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：参数集大小合法。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数paramSet无效。 |

**OH_Huks_CheckParamMatch()**

```ets
struct OH_Huks_Result OH_Huks_CheckParamMatch(const struct OH_Huks_Param *baseParam, const struct OH_Huks_Param *param)
```

描述

比较两个参数是否相同。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const struct OH_Huks_Param *baseParam | 指向被比较的参数的指针。 |
| const struct OH_Huks_Param *param | 指向比较的参数的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct OH_Huks_Result | 可能的返回码（errorCode）：  OH_HUKS_SUCCESS = 0 ：比较的两个参数相同。  OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：其中一个参数集是无效的，或者参数不匹配，  或者内部有无效标签。 |

**OH_Huks_FreeKeyAliasSet()**

```ets
void OH_Huks_FreeKeyAliasSet(struct OH_Huks_KeyAliasSet *keyAliasSet)
```

描述

销毁密钥别名的参数集。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_Huks_KeyAliasSet *keyAliasSet | 指向要被销毁的密钥别名的参数集的指针地址。 |