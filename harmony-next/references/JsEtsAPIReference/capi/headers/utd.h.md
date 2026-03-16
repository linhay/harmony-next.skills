# utd.h

#### 概述

提供标准化数据类型描述相关接口和数据结构。

**引用文件：** <database/udmf/utd.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：**[UDMF](../../topics/misc/UDMF.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_Utd](../../topics/misc/OH_Utd.md)OH_Utd统一数据类型描述符。

#### 函数

名称描述[OH_Utd* OH_Utd_Create(const char* typeId)](#ZH-CN_TOPIC_0000002497444730__oh_utd_create)创建统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)指针及实例对象。[void OH_Utd_Destroy(OH_Utd* pThis)](#ZH-CN_TOPIC_0000002497444730__oh_utd_destroy)销毁统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)指针指向的实例对象。[const char* OH_Utd_GetTypeId(OH_Utd* pThis)](#ZH-CN_TOPIC_0000002497444730__oh_utd_gettypeid)获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的类型ID。[const char* OH_Utd_GetDescription(OH_Utd* pThis)](#ZH-CN_TOPIC_0000002497444730__oh_utd_getdescription)获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的描述信息。[const char* OH_Utd_GetReferenceUrl(OH_Utd* pThis)](#ZH-CN_TOPIC_0000002497444730__oh_utd_getreferenceurl)获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的URL信息。[const char* OH_Utd_GetIconFile(OH_Utd* pThis)](#ZH-CN_TOPIC_0000002497444730__oh_utd_geticonfile)获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的默认图标文件路径。[const char** OH_Utd_GetBelongingToTypes(OH_Utd* pThis, unsigned int* count)](#ZH-CN_TOPIC_0000002497444730__oh_utd_getbelongingtotypes)获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的归属关系结果集。[const char** OH_Utd_GetFilenameExtensions(OH_Utd* pThis, unsigned int* count)](#ZH-CN_TOPIC_0000002497444730__oh_utd_getfilenameextensions)获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)所关联的文件名后缀结果集。[const char** OH_Utd_GetMimeTypes(OH_Utd* pThis, unsigned int* count)](#ZH-CN_TOPIC_0000002497444730__oh_utd_getmimetypes)获取[OH_Utd](../../topics/misc/OH_Utd.md)所关联的MIME类型结果集。[const char** OH_Utd_GetTypesByFilenameExtension(const char* extension, unsigned int* count)](#ZH-CN_TOPIC_0000002497444730__oh_utd_gettypesbyfilenameextension)通过文件名后缀获取关联的统一标准数据描述类型结果集。[const char** OH_Utd_GetTypesByMimeType(const char* mimeType, unsigned int* count)](#ZH-CN_TOPIC_0000002497444730__oh_utd_gettypesbymimetype)通过MIME类型获取所关联的标准数据类型结果集。[bool OH_Utd_BelongsTo(const char* srcTypeId, const char* destTypeId)](#ZH-CN_TOPIC_0000002497444730__oh_utd_belongsto)判断两个标准化数据描述类型是否存在归属关系。[bool OH_Utd_IsLower(const char* srcTypeId, const char* destTypeId)](#ZH-CN_TOPIC_0000002497444730__oh_utd_islower)判断原标准化数据类型是否是目标标准化数据类型的低层级类型。例如TYPE_SCRIPT为SOURCE_CODE的低层级类型，TYPE_SCRIPT和SOURCE_CODE为PLAIN_TEXT的低层级类型。[bool OH_Utd_IsHigher(const char* srcTypeId, const char* destTypeId)](#ZH-CN_TOPIC_0000002497444730__oh_utd_ishigher)判断原标准化数据类型是否是目标标准化数据类型的高层级类型。例如SOURCE_CODE为TYPE_SCRIPT的高层级类型，PLAIN_TEXT为SOURCE_CODE和TYPE_SCRIPT的高层级类型。[bool OH_Utd_Equals(OH_Utd* utd1, OH_Utd* utd2)](#ZH-CN_TOPIC_0000002497444730__oh_utd_equals)判断两个标准化数据描述类型是否相等。[void OH_Utd_DestroyStringList(const char** list, unsigned int count)](#ZH-CN_TOPIC_0000002497444730__oh_utd_destroystringlist)销毁标准数据描述类型结果集字符串列表。

#### 函数说明

#### OH_Utd_Create()

```ets
OH_Utd* OH_Utd_Create(const char* typeId)
```

**描述**

创建统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)指针及实例对象。

**起始版本：** 12

**参数：**

参数项描述const char* typeId表示统一数据类型ID。

**返回：**

类型说明[OH_Utd](../../topics/misc/OH_Utd.md)*

执行成功则返回一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)实例对象的指针，否则返回nullptr。

当不再需要使用指针时，请使用[OH_Utd_Destroy](utd.h.md#ZH-CN_TOPIC_0000002497444730__oh_utd_destroy)销毁实例对象，否则会导致内存泄漏。

#### OH_Utd_Destroy()

```ets
void OH_Utd_Destroy(OH_Utd* pThis)
```

**描述**

销毁统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)实例的指针。

#### OH_Utd_GetTypeId()

```ets
const char* OH_Utd_GetTypeId(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的类型ID。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。

**返回：**

类型说明const char*当入参有效时返回指向类型ID的字符串指针，否则返回nullptr。

#### OH_Utd_GetDescription()

```ets
const char* OH_Utd_GetDescription(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的描述信息。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。

**返回：**

类型说明const char*当入参有效时返回指向描述信息的字符串指针，否则返回nullptr。

#### OH_Utd_GetReferenceUrl()

```ets
const char* OH_Utd_GetReferenceUrl(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的URL信息。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。

**返回：**

类型说明const char*当入参有效时返回指向URL信息的字符串指针，否则返回nullptr。

#### OH_Utd_GetIconFile()

```ets
const char* OH_Utd_GetIconFile(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的默认图标文件路径。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。

**返回：**

类型说明const char*当入参有效时返回指向默认图标文件路径的字符串指针，否则返回nullptr。

#### OH_Utd_GetBelongingToTypes()

```ets
const char** OH_Utd_GetBelongingToTypes(OH_Utd* pThis, unsigned int* count)
```

**描述**

获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)中的归属关系结果集。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。unsigned int* count该参数是输出参数，结果集中的类型数量会写入该变量。

**返回：**

类型说明const char**当入参有效时返回归属关系结果集的字符串指针列表，否则返回nullptr。

#### OH_Utd_GetFilenameExtensions()

```ets
const char** OH_Utd_GetFilenameExtensions(OH_Utd* pThis, unsigned int* count)
```

**描述**

获取统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)所关联的文件名后缀结果集。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。unsigned int* count该参数是输出参数，结果集中的文件后缀名数量会写入该变量。

**返回：**

类型说明const char**当入参有效时返回文件名后缀结果集的字符串指针列表，否则返回nullptr。

#### OH_Utd_GetMimeTypes()

```ets
const char** OH_Utd_GetMimeTypes(OH_Utd* pThis, unsigned int* count)
```

**描述**

获取[OH_Utd](../../topics/misc/OH_Utd.md)所关联的MIME类型结果集。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* pThis表示一个指向统一数据类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。unsigned int* count该参数是输出参数，结果集中的MIME类型数量会写入该变量。

**返回：**

类型说明const char**当入参有效时返回MIME类型结果集的字符串指针列表，否则返回nullptr。

#### OH_Utd_GetTypesByFilenameExtension()

```ets
const char** OH_Utd_GetTypesByFilenameExtension(const char* extension, unsigned int* count)
```

**描述**

通过文件名后缀获取关联的统一标准数据描述类型结果集。

**起始版本：** 12

**参数：**

参数项描述const char* extension表示文件名后缀。unsigned int* count该参数是输出参数，结果集中的类型数量会写入该变量。

**返回：**

类型说明const char**

返回标准数据描述类型结果集字符串列表。

当不再需要使用指针时，请及时使用[OH_Utd_DestroyStringList](utd.h.md#ZH-CN_TOPIC_0000002497444730__oh_utd_destroystringlist)销毁对应的实例，否则会导致内存泄漏。

#### OH_Utd_GetTypesByMimeType()

```ets
const char** OH_Utd_GetTypesByMimeType(const char* mimeType, unsigned int* count)
```

**描述**

通过MIME类型获取所关联的标准数据类型结果集。

**起始版本：** 12

**参数：**

参数项描述const char* mimeType表示MIME类型字符串。unsigned int* count该参数是输出参数，结果集中的类型数量会写入该变量。

**返回：**

类型说明const char**

返回标准数据描述类型结果集字符串列表。

当不再需要使用指针时，请及时使用[OH_Utd_DestroyStringList](utd.h.md#ZH-CN_TOPIC_0000002497444730__oh_utd_destroystringlist)销毁对应的实例，否则会导致内存泄漏。

#### OH_Utd_BelongsTo()

```ets
bool OH_Utd_BelongsTo(const char* srcTypeId, const char* destTypeId)
```

**描述**

判断两个标准化数据描述类型是否存在归属关系。

**起始版本：** 12

**参数：**

参数项描述const char* srcTypeId表示原标准化数据类型。const char* destTypeId表示目标标准化数据类型。

**返回：**

类型说明boolfalse表示原类型不属于目标类型，true表示原类型属于目标类型。

#### OH_Utd_IsLower()

```ets
bool OH_Utd_IsLower(const char* srcTypeId, const char* destTypeId)
```

**描述**

判断原标准化数据类型是否是目标标准化数据类型的低层级类型。例如TYPE_SCRIPT为SOURCE_CODE的低层级类型，TYPE_SCRIPT和SOURCE_CODE为PLAIN_TEXT的低层级类型。

**起始版本：** 12

**参数：**

参数项描述const char* srcTypeId表示原标准化数据类型。const char* destTypeId表示目标标准化数据类型。

**返回：**

类型说明boolfalse表示原类型不低于目标类型；true表示原类型低于目标类型。

#### OH_Utd_IsHigher()

```ets
bool OH_Utd_IsHigher(const char* srcTypeId, const char* destTypeId)
```

**描述**

判断原标准化数据类型是否是目标标准化数据类型的高层级类型。例如SOURCE_CODE为TYPE_SCRIPT的高层级类型，PLAIN_TEXT为SOURCE_CODE和TYPE_SCRIPT的高层级类型。

**起始版本：** 12

**参数：**

参数项描述const char* srcTypeId表示原标准化数据类型。const char* destTypeId表示目标标准化数据类型。

**返回：**

类型说明boolfalse表示原类型不高于目标类型，true表示原类型高于目标类型。

#### OH_Utd_Equals()

```ets
bool OH_Utd_Equals(OH_Utd* utd1, OH_Utd* utd2)
```

**描述**

判断两个标准化数据描述类型是否相等。

**起始版本：** 12

**参数：**

参数项描述[OH_Utd](../../topics/misc/OH_Utd.md)* utd1表示一个指向标准化数据描述类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。[OH_Utd](../../topics/misc/OH_Utd.md)* utd2表示一个指向标准化数据描述类型[OH_Utd](../../topics/misc/OH_Utd.md)对象的指针。

**返回：**

类型说明boolfalse表示两种类型不相等，true表示两种类型相等。

#### OH_Utd_DestroyStringList()

```ets
void OH_Utd_DestroyStringList(const char** list, unsigned int count)
```

**描述**

销毁标准数据描述类型结果集字符串列表。

**起始版本：** 12

**参数：**

参数项描述const char** list表示字符串列表指针。unsigned int count表示字符串列表list参数中的列表长度。