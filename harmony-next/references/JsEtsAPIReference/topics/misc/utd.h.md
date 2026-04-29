# utd.h

**概述**

提供标准化数据类型描述相关接口和数据结构。

引用文件： <database/udmf/utd.h>

库： libudmf.so

系统能力： SystemCapability.DistributedDataManager.UDMF.Core

起始版本： 12

相关模块： [UDMF](UDMF.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Utd | OH_Utd | 统一数据类型描述符。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Utd* OH_Utd_Create(const char* typeId) | 创建统一数据类型OH_Utd指针及实例对象。 |
| void OH_Utd_Destroy(OH_Utd* pThis) | 销毁统一数据类型OH_Utd指针指向的实例对象。 |
| const char* OH_Utd_GetTypeId(OH_Utd* pThis) | 获取统一数据类型OH_Utd中的类型ID。 |
| const char* OH_Utd_GetDescription(OH_Utd* pThis) | 获取统一数据类型OH_Utd中的描述信息。 |
| const char* OH_Utd_GetReferenceUrl(OH_Utd* pThis) | 获取统一数据类型OH_Utd中的URL信息。 |
| const char* OH_Utd_GetIconFile(OH_Utd* pThis) | 获取统一数据类型OH_Utd中的默认图标文件路径。 |
| const char** OH_Utd_GetBelongingToTypes(OH_Utd* pThis, unsigned int* count) | 获取统一数据类型OH_Utd中的归属关系结果集。 |
| const char** OH_Utd_GetFilenameExtensions(OH_Utd* pThis, unsigned int* count) | 获取统一数据类型OH_Utd所关联的文件名后缀结果集。 |
| const char** OH_Utd_GetMimeTypes(OH_Utd* pThis, unsigned int* count) | 获取OH_Utd所关联的MIME类型结果集。 |
| const char** OH_Utd_GetTypesByFilenameExtension(const char* extension, unsigned int* count) | 通过文件名后缀获取关联的统一标准数据描述类型结果集。 |
| const char** OH_Utd_GetTypesByMimeType(const char* mimeType, unsigned int* count) | 通过MIME类型获取所关联的标准数据类型结果集。 |
| bool OH_Utd_BelongsTo(const char* srcTypeId, const char* destTypeId) | 判断两个标准化数据描述类型是否存在归属关系。 |
| bool OH_Utd_IsLower(const char* srcTypeId, const char* destTypeId) | 判断原标准化数据类型是否是目标标准化数据类型的低层级类型。例如TYPE_SCRIPT为SOURCE_CODE的低层级类型，TYPE_SCRIPT和SOURCE_CODE为PLAIN_TEXT的低层级类型。 |
| bool OH_Utd_IsHigher(const char* srcTypeId, const char* destTypeId) | 判断原标准化数据类型是否是目标标准化数据类型的高层级类型。例如SOURCE_CODE为TYPE_SCRIPT的高层级类型，PLAIN_TEXT为SOURCE_CODE和TYPE_SCRIPT的高层级类型。 |
| bool OH_Utd_Equals(OH_Utd* utd1, OH_Utd* utd2) | 判断两个标准化数据描述类型是否相等。 |
| void OH_Utd_DestroyStringList(const char** list, unsigned int count) | 销毁标准数据描述类型结果集字符串列表。 |

**函数说明**

**OH_Utd_Create()**

```ets
OH_Utd* OH_Utd_Create(const char* typeId)
```

描述

创建统一数据类型[OH_Utd](OH_Utd.md)指针及实例对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* typeId | 表示统一数据类型ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Utd* | 执行成功则返回一个指向统一数据类型OH_Utd实例对象的指针，否则返回nullptr。 当不再需要使用指针时，请使用OH_Utd_Destroy销毁实例对象，否则会导致内存泄漏。 |

**OH_Utd_Destroy()**

```ets
void OH_Utd_Destroy(OH_Utd* pThis)
```

描述

销毁统一数据类型[OH_Utd](OH_Utd.md)指针指向的实例对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示指向统一数据类型OH_Utd实例的指针。 |

**OH_Utd_GetTypeId()**

```ets
const char* OH_Utd_GetTypeId(OH_Utd* pThis)
```

描述

获取统一数据类型[OH_Utd](OH_Utd.md)中的类型ID。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示一个指向统一数据类型OH_Utd对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 当入参有效时返回指向类型ID的字符串指针，否则返回nullptr。 |

**OH_Utd_GetDescription()**

```ets
const char* OH_Utd_GetDescription(OH_Utd* pThis)
```

描述

获取统一数据类型[OH_Utd](OH_Utd.md)中的描述信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示一个指向统一数据类型OH_Utd对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 当入参有效时返回指向描述信息的字符串指针，否则返回nullptr。 |

**OH_Utd_GetReferenceUrl()**

```ets
const char* OH_Utd_GetReferenceUrl(OH_Utd* pThis)
```

描述

获取统一数据类型[OH_Utd](OH_Utd.md)中的URL信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示一个指向统一数据类型OH_Utd对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 当入参有效时返回指向URL信息的字符串指针，否则返回nullptr。 |

**OH_Utd_GetIconFile()**

```ets
const char* OH_Utd_GetIconFile(OH_Utd* pThis)
```

描述

获取统一数据类型[OH_Utd](OH_Utd.md)中的默认图标文件路径。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示一个指向统一数据类型OH_Utd对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 当入参有效时返回指向默认图标文件路径的字符串指针，否则返回nullptr。 |

**OH_Utd_GetBelongingToTypes()**

```ets
const char** OH_Utd_GetBelongingToTypes(OH_Utd* pThis, unsigned int* count)
```

描述

获取统一数据类型[OH_Utd](OH_Utd.md)中的归属关系结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示一个指向统一数据类型OH_Utd对象的指针。 |
| unsigned int* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char** | 当入参有效时返回归属关系结果集的字符串指针列表，否则返回nullptr。 |

**OH_Utd_GetFilenameExtensions()**

```ets
const char** OH_Utd_GetFilenameExtensions(OH_Utd* pThis, unsigned int* count)
```

描述

获取统一数据类型[OH_Utd](OH_Utd.md)所关联的文件名后缀结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示一个指向统一数据类型OH_Utd对象的指针。 |
| unsigned int* count | 该参数是输出参数，结果集中的文件后缀名数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char** | 当入参有效时返回文件名后缀结果集的字符串指针列表，否则返回nullptr。 |

**OH_Utd_GetMimeTypes()**

```ets
const char** OH_Utd_GetMimeTypes(OH_Utd* pThis, unsigned int* count)
```

描述

获取[OH_Utd](OH_Utd.md)所关联的MIME类型结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* pThis | 表示一个指向统一数据类型OH_Utd对象的指针。 |
| unsigned int* count | 该参数是输出参数，结果集中的MIME类型数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char** | 当入参有效时返回MIME类型结果集的字符串指针列表，否则返回nullptr。 |

**OH_Utd_GetTypesByFilenameExtension()**

```ets
const char** OH_Utd_GetTypesByFilenameExtension(const char* extension, unsigned int* count)
```

描述

通过文件名后缀获取关联的统一标准数据描述类型结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* extension | 表示文件名后缀。 |
| unsigned int* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char** | 返回标准数据描述类型结果集字符串列表。 当不再需要使用指针时，请及时使用OH_Utd_DestroyStringList销毁对应的实例，否则会导致内存泄漏。 |

**OH_Utd_GetTypesByMimeType()**

```ets
const char** OH_Utd_GetTypesByMimeType(const char* mimeType, unsigned int* count)
```

描述

通过MIME类型获取所关联的标准数据类型结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* mimeType | 表示MIME类型字符串。 |
| unsigned int* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char** | 返回标准数据描述类型结果集字符串列表。 当不再需要使用指针时，请及时使用OH_Utd_DestroyStringList销毁对应的实例，否则会导致内存泄漏。 |

**OH_Utd_BelongsTo()**

```ets
bool OH_Utd_BelongsTo(const char* srcTypeId, const char* destTypeId)
```

描述

判断两个标准化数据描述类型是否存在归属关系。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* srcTypeId | 表示原标准化数据类型。 |
| const char* destTypeId | 表示目标标准化数据类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | false表示原类型不属于目标类型，true表示原类型属于目标类型。 |

**OH_Utd_IsLower()**

```ets
bool OH_Utd_IsLower(const char* srcTypeId, const char* destTypeId)
```

描述

判断原标准化数据类型是否是目标标准化数据类型的低层级类型。例如TYPE_SCRIPT为SOURCE_CODE的低层级类型，TYPE_SCRIPT和SOURCE_CODE为PLAIN_TEXT的低层级类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* srcTypeId | 表示原标准化数据类型。 |
| const char* destTypeId | 表示目标标准化数据类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | false表示原类型不低于目标类型；true表示原类型低于目标类型。 |

**OH_Utd_IsHigher()**

```ets
bool OH_Utd_IsHigher(const char* srcTypeId, const char* destTypeId)
```

描述

判断原标准化数据类型是否是目标标准化数据类型的高层级类型。例如SOURCE_CODE为TYPE_SCRIPT的高层级类型，PLAIN_TEXT为SOURCE_CODE和TYPE_SCRIPT的高层级类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* srcTypeId | 表示原标准化数据类型。 |
| const char* destTypeId | 表示目标标准化数据类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | false表示原类型不高于目标类型，true表示原类型高于目标类型。 |

**OH_Utd_Equals()**

```ets
bool OH_Utd_Equals(OH_Utd* utd1, OH_Utd* utd2)
```

描述

判断两个标准化数据描述类型是否相等。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Utd* utd1 | 表示一个指向标准化数据描述类型OH_Utd对象的指针。 |
| OH_Utd* utd2 | 表示一个指向标准化数据描述类型OH_Utd对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | false表示两种类型不相等，true表示两种类型相等。 |

**OH_Utd_DestroyStringList()**

```ets
void OH_Utd_DestroyStringList(const char** list, unsigned int count)
```

描述

销毁标准数据描述类型结果集字符串列表。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char** list | 表示字符串列表指针。 |
| unsigned int count | 表示字符串列表list参数中的列表长度。 |