# udmf.h

**概述**

提供访问统一数据管理框架数据的接口、数据结构、枚举类型。

引用文件： <database/udmf/udmf.h>

库： libudmf.so

系统能力： SystemCapability.DistributedDataManager.UDMF.Core

起始版本： 12

相关模块： [UDMF](UDMF.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_UdmfData | OH_UdmfData | 定义统一数据对象数据结构。 |
| OH_UdmfRecord | OH_UdmfRecord | 定义统一数据对象中记录数据的数据结构，称为数据记录。 |
| OH_UdmfRecordProvider | OH_UdmfRecordProvider | 定义统一数据对象中的数据提供者。 |
| OH_UdmfProperty | OH_UdmfProperty | 定义统一数据对象中数据记录的属性结构。 |
| OH_Udmf_ProgressInfo | OH_Udmf_ProgressInfo | 定义进度信息的数据结构。 |
| OH_UdmfGetDataParams | OH_UdmfGetDataParams | 定义异步获取UDMF数据的请求参数。 |
| OH_UdmfOptions | OH_UdmfOptions | 数据操作选项，定义数据操作的可选参数。 |
| OH_UdmfDataLoadParams | OH_UdmfDataLoadParams | 表示数据加载参数结构体。 |
| OH_UdmfDataLoadInfo | OH_UdmfDataLoadInfo | 表示数据加载信息结构体。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Udmf_Intention | Udmf_Intention | 描述UDMF数据通路枚举类型。 |
| Udmf_ShareOption | Udmf_ShareOption | UDMF支持的设备内使用范围类型枚举。 |
| Udmf_FileConflictOptions | Udmf_FileConflictOptions | 定义文件拷贝冲突时的选项。 |
| Udmf_ProgressIndicator | Udmf_ProgressIndicator | 定义进度条指示选项，可选择是否采用系统默认进度显示。 |
| Udmf_Visibility | Udmf_Visibility | 定义数据的可见性等级。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| UDMF_KEY_BUFFER_LEN (512) | - | 统一数据对象唯一标识符最小空间长度。 |
| typedef void (*OH_Udmf_DataProgressListener)(OH_Udmf_ProgressInfo* progressInfo, OH_UdmfData* data) | OH_Udmf_DataProgressListener | 定义获取进度信息和数据的监听回调函数。 使用时需要判断数据是否返回空指针。只有当进度达到100%时，才会返回数据。 |
| OH_UdmfData* OH_UdmfData_Create() | - | 创建统一数据对象OH_UdmfData指针及实例对象。当不再需要使用指针时，请使用OH_UdmfData_Destroy销毁实例对象，否则会导致内存泄漏。 |
| void OH_UdmfData_Destroy(OH_UdmfData* pThis) | - | 销毁统一数据对象OH_UdmfData指针指向的实例对象。 |
| int OH_UdmfData_AddRecord(OH_UdmfData* pThis, OH_UdmfRecord* record) | - | 添加一个数据记录OH_UdmfRecord到统一数据对象OH_UdmfData中。 |
| bool OH_UdmfData_HasType(OH_UdmfData* pThis, const char* type) | - | 检查统一数据对象OH_UdmfData中是否存在指定类型。 |
| char** OH_UdmfData_GetTypes(OH_UdmfData* pThis, unsigned int* count) | - | 获取统一数据对象OH_UdmfData中包含的所有类型结果集。 |
| OH_UdmfRecord** OH_UdmfData_GetRecords(OH_UdmfData* pThis, unsigned int* count) | - | 获取统一数据对象OH_UdmfData中包含的所有记录结果集。 |
| typedef void (*UdmfData_Finalize)(void* context) | UdmfData_Finalize | 定义用于释放上下文的回调函数，统一数据提供者对象销毁时触发。 |
| OH_UdmfRecordProvider* OH_UdmfRecordProvider_Create() | - | 创建一个统一数据提供者OH_UdmfRecordProvider指针及实例对象。当不再需要使用指针时，请使用OH_UdmfRecordProvider_Destroy销毁实例对象，否则会导致内存泄漏。 |
| int OH_UdmfRecordProvider_Destroy(OH_UdmfRecordProvider* provider) | - | 销毁统一数据提供者OH_UdmfRecordProvider指针指向的实例对象。 |
| typedef void* (*OH_UdmfRecordProvider_GetData)(void* context, const char* type) | OH_UdmfRecordProvider_GetData | 定义用于按类型获取数据的回调函数。当从OH_UdmfRecord中获取数据时，会触发此回调函数，得到的数据就是这个回调函数返回的数据。 |
| int OH_UdmfRecordProvider_SetData(OH_UdmfRecordProvider* provider, void* context, const OH_UdmfRecordProvider_GetData callback, const UdmfData_Finalize finalize) | - | 设置统一数据提供者的数据提供回调函数。 |
| OH_UdmfRecord* OH_UdmfRecord_Create() | - | 创建统一数据记录OH_UdmfRecord指针及实例对象。当不再需要使用指针时，请使用OH_UdmfRecord_Destroy销毁实例对象，否则会导致内存泄漏。 |
| void OH_UdmfRecord_Destroy(OH_UdmfRecord* pThis) | - | 销毁统一数据记录OH_UdmfRecord指针指向的实例对象。 |
| int OH_UdmfRecord_AddGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char* entry, unsigned int count) | - | 添加用户自定义的通用数据至统一数据记录OH_UdmfRecord中。对于已定义UDS的类型（比如PlainText、Link、Pixelmap等）不可使用该接口。 |
| int OH_UdmfRecord_AddPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText) | - | 增加纯文本类型OH_UdsPlainText数据至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_AddHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink) | - | 增加超链接类型OH_UdsHyperlink数据至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_AddHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html) | - | 增加超文本标记语言类型OH_UdsHtml数据至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_AddAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem) | - | 增加桌面图标类型OH_UdsAppItem数据至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_AddFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri) | - | 增加文件Uri类型OH_UdsFileUri数据至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_AddPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap) | - | 增加像素图片类型OH_UdsPixelMap数据至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_AddArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer) | - | 增加一个ArrayBuffer类型OH_UdsArrayBuffer的数据至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_AddContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm) | - | 增加一个内容卡片类型OH_UdsContentForm的数据至统一数据记录OH_UdmfRecord中。 |
| char** OH_UdmfRecord_GetTypes(OH_UdmfRecord* pThis, unsigned int* count) | - | 获取统一数据记录OH_UdmfRecord中所有类型的结果集。 |
| int OH_UdmfRecord_GetGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char** entry, unsigned int* count) | - | 获取统一数据记录OH_UdmfRecord中的特定类型的数据结果集。 |
| int OH_UdmfRecord_GetPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText) | - | 从统一数据记录OH_UdmfRecord中获取纯文本类型OH_UdsPlainText数据。 |
| int OH_UdmfRecord_GetHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink) | - | 从统一数据记录OH_UdmfRecord中获取超链接类型OH_UdsHyperlink数据。 |
| int OH_UdmfRecord_GetHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html) | - | 从统一数据记录OH_UdmfRecord中获取超文本标记语言类型OH_UdsHtml数据。 |
| int OH_UdmfRecord_GetAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem) | - | 从统一数据记录OH_UdmfRecord中获取桌面图标类型OH_UdsAppItem数据。 |
| int OH_UdmfRecord_SetProvider(OH_UdmfRecord* pThis, const char* const* types, unsigned int count, OH_UdmfRecordProvider* provider) | - | 将指定类型的统一数据提供者OH_UdmfRecordProvider设置至统一数据记录OH_UdmfRecord中。 |
| int OH_UdmfRecord_GetFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri) | - | 从统一数据记录OH_UdmfRecord中获取文件Uri类型OH_UdsFileUri数据。 |
| int OH_UdmfRecord_GetPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap) | - | 从统一数据记录OH_UdmfRecord中获取像素图片类型OH_UdsPixelMap数据。 |
| int OH_UdmfRecord_GetArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer) | - | 从统一数据记录OH_UdmfRecord中获取ArrayBuffer类型OH_UdsArrayBuffer数据。 |
| int OH_UdmfRecord_GetContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm) | - | 从统一数据记录OH_UdmfRecord中获取内容卡片类型OH_UdsContentForm数据。 |
| int OH_UdmfData_GetPrimaryPlainText(OH_UdmfData* data, OH_UdsPlainText* plainText) | - | 从统一数据对象OH_UdmfData中获取第一个纯文本类型OH_UdsPlainText数据。 |
| int OH_UdmfData_GetPrimaryHtml(OH_UdmfData* data, OH_UdsHtml* html) | - | 从统一数据对象OH_UdmfData中获取第一个超文本标记语言类型OH_UdsHtml数据。 |
| int OH_UdmfData_GetRecordCount(OH_UdmfData* data) | - | 获取统一数据对象OH_UdmfData中包含的所有记录数量。 |
| OH_UdmfRecord* OH_UdmfData_GetRecord(OH_UdmfData* data, unsigned int index) | - | 获取统一数据对象OH_UdmfData中指定位置的数据记录。 |
| bool OH_UdmfData_IsLocal(OH_UdmfData* data) | - | 检查统一数据对象OH_UdmfData是否是来自本端设备的数据。 |
| OH_UdmfProperty* OH_UdmfProperty_Create(OH_UdmfData* unifiedData) | - | 创建统一数据对象中数据记录属性OH_UdmfProperty指针及实例对象。当不再需要使用指针时，请使用OH_UdmfProperty_Destroy销毁实例对象，否则会导致内存泄漏。 |
| void OH_UdmfProperty_Destroy(OH_UdmfProperty* pThis) | - | 销毁数据属性OH_UdmfProperty指针指向的实例对象。 |
| const char* OH_UdmfProperty_GetTag(OH_UdmfProperty* pThis) | - | 从数据属性OH_UdmfProperty中获取用户自定义标签值。 |
| int64_t OH_UdmfProperty_GetTimestamp(OH_UdmfProperty* pThis) | - | 从数据属性OH_UdmfProperty中获取时间戳。 |
| Udmf_ShareOption OH_UdmfProperty_GetShareOption(OH_UdmfProperty* pThis) | - | 从数据属性OH_UdmfProperty中获取设备内适用范围属性。 |
| int OH_UdmfProperty_GetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int defaultValue) | - | 从数据属性OH_UdmfProperty中获取自定义的附加整型参数。 |
| const char* OH_UdmfProperty_GetExtrasStringParam(OH_UdmfProperty* pThis, const char* key) | - | 从数据属性OH_UdmfProperty中获取自定义的附加字符串参数。 |
| int OH_UdmfProperty_SetTag(OH_UdmfProperty* pThis, const char* tag) | - | 设置数据属性OH_UdmfProperty的自定义标签值。 |
| int OH_UdmfProperty_SetShareOption(OH_UdmfProperty* pThis, Udmf_ShareOption option) | - | 设置数据属性OH_UdmfProperty的设备内适用范围Udmf_ShareOption参数。 |
| int OH_UdmfProperty_SetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int param) | - | 设置数据属性OH_UdmfProperty的附加整型参数。 |
| int OH_UdmfProperty_SetExtrasStringParam(OH_UdmfProperty* pThis, const char* key, const char* param) | - | 设置数据属性OH_UdmfProperty的附加字符串参数。 |
| OH_UdmfOptions* OH_UdmfOptions_Create() | - | 创建指向OH_UdmfOptions实例的指针。当不再需要使用指针时，请使用OH_UdmfOptions_Destroy销毁实例对象，否则会导致内存泄漏。 |
| void OH_UdmfOptions_Destroy(OH_UdmfOptions* pThis) | - | 销毁指向OH_UdmfOptions实例的指针。 |
| const char* OH_UdmfOptions_GetKey(OH_UdmfOptions* pThis) | - | 从数据操作选项OH_UdmfOptions实例中获取数据的唯一标识符信息。 |
| int OH_UdmfOptions_SetKey(OH_UdmfOptions* pThis, const char* key) | - | 设置数据操作选项OH_UdmfOptions实例中的数据的唯一标识符内容参数。 |
| Udmf_Intention OH_UdmfOptions_GetIntention(OH_UdmfOptions* pThis) | - | 从数据操作选项OH_UdmfOptions实例中获取数据通路信息。 |
| int OH_UdmfOptions_SetIntention(OH_UdmfOptions* pThis, Udmf_Intention intention) | - | 设置数据操作选项OH_UdmfOptions实例中的数据通路内容参数。 |
| int OH_UdmfOptions_Reset(OH_UdmfOptions* pThis) | - | 重置数据操作选项OH_UdmfOptions实例为空。 |
| int OH_Udmf_GetUnifiedData(const char* key, Udmf_Intention intention, OH_UdmfData* unifiedData) | - | 从统一数据管理框架数据库中获取统一数据对象OH_UdmfData数据。 |
| int OH_Udmf_GetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize) | - | 通过数据通路类型从统一数据管理框架数据库中获取统一数据对象OH_UdmfData数据。 |
| int OH_Udmf_SetUnifiedData(Udmf_Intention intention, OH_UdmfData* unifiedData, char* key, unsigned int keyLen) | - | 从统一数据管理框架数据库中写入统一数据对象OH_UdmfData数据。 |
| int OH_Udmf_SetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData *unifiedData, char *key, unsigned int keyLen) | - | 从统一数据管理框架数据库中写入统一数据对象OH_UdmfData数据。 |
| int OH_Udmf_UpdateUnifiedData(OH_UdmfOptions* options, OH_UdmfData* unifiedData) | - | 对统一数据管理框架数据库中的统一数据对象OH_UdmfData数据进行数据更改。 |
| int OH_Udmf_DeleteUnifiedData(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize) | - | 删除统一数据管理框架数据库中的统一数据对象OH_UdmfData数据。 |
| void OH_Udmf_DestroyDataArray(OH_UdmfData** dataArray, unsigned int dataSize) | - | 销毁数据数组内存。 |
| int OH_UdmfProgressInfo_GetProgress(OH_Udmf_ProgressInfo* progressInfo) | - | 从进度信息OH_Udmf_ProgressInfo中获取进度百分比数据。 |
| int OH_UdmfProgressInfo_GetStatus(OH_Udmf_ProgressInfo* progressInfo) | - | 从进度信息OH_Udmf_ProgressInfo中获取状态信息。 |
| OH_UdmfGetDataParams* OH_UdmfGetDataParams_Create() | - | 创建异步获取UDMF数据的请求参数OH_UdmfGetDataParams指针及实例对象。 当不再需要使用指针时，请使用OH_UdmfGetDataParams_Destroy销毁实例对象，否则会导致内存泄漏。 |
| void OH_UdmfGetDataParams_Destroy(OH_UdmfGetDataParams* pThis) | - | 销毁异步请求参数OH_UdmfGetDataParams指针指向的实例对象。 |
| void OH_UdmfGetDataParams_SetDestUri(OH_UdmfGetDataParams* params, const char* destUri) | - | 设置异步请求参数OH_UdmfGetDataParams中的目标路径。 若设置了目标路径，会将文件类型的数据进行拷贝到指定路径。回调中获取到的文件类型数据会被替换为目标路径的URI。 若不设置目标路径，则不会执行拷贝文件操作。回调中获取到的文件类型数据为源端路径URI。 若应用涉及复杂文件处理策略，或需要将文件拷贝在多个路径下时，建议不设置此参数，由应用自行完成文件拷贝相关处理。 |
| void OH_UdmfGetDataParams_SetFileConflictOptions(OH_UdmfGetDataParams* params, const Udmf_FileConflictOptions options) | - | 设置异步请求参数OH_UdmfGetDataParams中的文件冲突选项。 |
| void OH_UdmfGetDataParams_SetProgressIndicator(OH_UdmfGetDataParams* params, const Udmf_ProgressIndicator progressIndicator) | - | 设置异步请求参数OH_UdmfGetDataParams中的进度条指示选项。 |
| void OH_UdmfGetDataParams_SetDataProgressListener(OH_UdmfGetDataParams* params, const OH_Udmf_DataProgressListener dataProgressListener) | - | 设置异步请求参数OH_UdmfGetDataParams中的监听回调函数。 |
| Udmf_Visibility OH_UdmfOptions_GetVisibility(OH_UdmfOptions* pThis) | - | 从数据操作选项OH_UdmfOptions实例中获取数据可见性等级。 |
| int OH_UdmfOptions_SetVisibility(OH_UdmfOptions* pThis, Udmf_Visibility visibility) | - | 设置数据操作选项OH_UdmfOptions实例中的数据可见性等级。 |
| typedef OH_UdmfData* (*OH_Udmf_DataLoadHandler)(OH_UdmfDataLoadInfo* acceptableInfo) | OH_Udmf_DataLoadHandler | 表示用于加载数据的回调函数。 |
| OH_UdmfDataLoadParams* OH_UdmfDataLoadParams_Create() | - | 创建指向数据加载参数OH_UdmfDataLoadParams实例的指针。 |
| void OH_UdmfDataLoadParams_Destroy(OH_UdmfDataLoadParams* pThis) | - | 销毁数据加载参数OH_UdmfDataLoadParams指针指向的实例对象。 |
| void OH_UdmfDataLoadParams_SetLoadHandler(OH_UdmfDataLoadParams* params, const OH_Udmf_DataLoadHandler dataLoadHandler) | - | 设置数据加载参数OH_UdmfDataLoadParams中的数据加载处理函数。 |
| void OH_UdmfDataLoadParams_SetDataLoadInfo(OH_UdmfDataLoadParams* params, OH_UdmfDataLoadInfo* dataLoadInfo) | - | 设置数据加载参数OH_UdmfDataLoadParams中的数据加载信息。 |
| OH_UdmfDataLoadInfo* OH_UdmfDataLoadInfo_Create() | - | 创建指向数据加载信息OH_UdmfDataLoadInfo实例的指针。 |
| void OH_UdmfDataLoadInfo_Destroy(OH_UdmfDataLoadInfo* dataLoadInfo) | - | 销毁数据加载信息OH_UdmfDataLoadInfo指针指向的实例对象。 |
| char** OH_UdmfDataLoadInfo_GetTypes(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int* count) | - | 从数据加载信息OH_UdmfDataLoadInfo中获取数据类型列表。 |
| void OH_UdmfDataLoadInfo_SetType(OH_UdmfDataLoadInfo* dataLoadInfo, const char* type) | - | 设置数据加载信息OH_UdmfDataLoadInfo中的数据类型。 |
| int OH_UdmfDataLoadInfo_GetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo) | - | 获取数据加载信息OH_UdmfDataLoadInfo中的记录数量。 |
| void OH_UdmfDataLoadInfo_SetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int recordCount) | - | 设置数据加载信息OH_UdmfDataLoadInfo中的记录数量。 |
| OH_UdmfData* OH_UDMF_GetDataElementAt(OH_UdmfData** dataArray, unsigned int index) | - | 从统一数据对象OH_UdmfData数组中获取指定下标的统一数据对象数据。 |

**枚举类型说明**

**Udmf_Intention**

```ets
enum Udmf_Intention
```

描述

描述UDMF数据通路枚举类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| UDMF_INTENTION_DRAG | 拖拽数据通路。 |
| UDMF_INTENTION_PASTEBOARD | 剪贴板数据通路。 |
| UDMF_INTENTION_DATA_HUB | 公共数据通路。 起始版本： 20 |
| UDMF_INTENTION_SYSTEM_SHARE | 系统分享数据通路。 起始版本： 20 |
| UDMF_INTENTION_PICKER | Picker数据通路。 起始版本： 20 |
| UDMF_INTENTION_MENU | 菜单数据通路。 起始版本： 20 |

**Udmf_ShareOption**

```ets
enum Udmf_ShareOption
```

描述

UDMF支持的设备内使用范围类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| SHARE_OPTIONS_INVALID | 表示不合法的使用范围类型。 |
| SHARE_OPTIONS_IN_APP | 表示允许在本设备同应用内使用。 |
| SHARE_OPTIONS_CROSS_APP | 表示允许在本设备内跨应用使用。 |

**Udmf_FileConflictOptions**

```ets
enum Udmf_FileConflictOptions
```

描述

定义文件拷贝冲突时的选项。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| UDMF_OVERWRITE = 0 | 目标路径存在同文件名时覆盖。若不配置策略，默认使用改策略。 |
| UDMF_SKIP = 1 | 目标路径存在同文件名时跳过。 |

**Udmf_ProgressIndicator**

```ets
enum Udmf_ProgressIndicator
```

描述

定义进度条指示选项，可选择是否采用系统默认进度显示。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| UDMF_NONE = 0 | 不采用系统默认进度显示。 |
| UDMF_DEFAULT = 1 | 采用系统默认进度显示，500ms内获取数据完成将不会拉起默认进度条。 |

**Udmf_Visibility**

```ets
enum Udmf_Visibility
```

描述

定义数据的可见性等级。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| UDMF_ALL | 可见性等级，所有应用可见。 |
| UDMF_OWN_PROCESS | 可见性等级，仅数据提供者可见。 |

**函数说明**

**OH_UdmfGetDataParams_SetAcceptableInfo()**

```ets
void OH_UdmfGetDataParams_SetAcceptableInfo(OH_UdmfGetDataParams* params, OH_UdmfDataLoadInfo* acceptableInfo)
```

描述

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中可接收的数据描述信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfGetDataParams* params | 表示指向OH_UdmfGetDataParams实例的指针。 |
| OH_UdmfDataLoadInfo* acceptableInfo | 表示指向OH_UdmfDataLoadInfo实例的指针。 |

**OH_UdmfDataLoadParams_Create()**

```ets
OH_UdmfDataLoadParams* OH_UdmfDataLoadParams_Create()
```

描述

创建指向数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)实例的指针。

起始版本： 20

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfDataLoadParams* | 如果创建成功，返回一个指向数据加载参数OH_UdmfDataLoadParams实例的指针；否则返回nullptr。 |

**OH_UdmfDataLoadParams_Destroy()**

```ets
void OH_UdmfDataLoadParams_Destroy(OH_UdmfDataLoadParams* pThis)
```

描述

销毁数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)指针指向的实例对象。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadParams* pThis | 表示指向数据加载参数OH_UdmfDataLoadParams实例的指针。 |

**OH_UdmfDataLoadParams_SetLoadHandler()**

```ets
void OH_UdmfDataLoadParams_SetLoadHandler(OH_UdmfDataLoadParams* params, const OH_Udmf_DataLoadHandler dataLoadHandler)
```

描述

设置数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)中的数据加载处理函数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadParams* params | 表示指向数据加载参数OH_UdmfDataLoadParams实例的指针。 |
| const OH_Udmf_DataLoadHandler dataLoadHandler | 表示用户定义的数据加载处理函数。 |

**OH_UdmfDataLoadParams_SetDataLoadInfo()**

```ets
void OH_UdmfDataLoadParams_SetDataLoadInfo(OH_UdmfDataLoadParams* params, OH_UdmfDataLoadInfo* dataLoadInfo)
```

描述

设置数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)中的数据加载信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadParams* params | 表示指向数据加载参数OH_UdmfDataLoadParams实例的指针。 |
| OH_UdmfDataLoadInfo* dataLoadInfo | 表示指向数据加载信息OH_UdmfDataLoadInfo实例的指针。 |

**OH_UdmfDataLoadInfo_Create()**

```ets
OH_UdmfDataLoadInfo* OH_UdmfDataLoadInfo_Create()
```

描述

创建指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。

起始版本： 20

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfDataLoadInfo* | 如果创建成功，返回一个指向数据加载信息OH_UdmfDataLoadInfo实例的指针；否则返回nullptr。 |

**OH_UdmfDataLoadInfo_Destroy()**

```ets
void OH_UdmfDataLoadInfo_Destroy(OH_UdmfDataLoadInfo* dataLoadInfo)
```

描述

销毁数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)指针指向的实例对象。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadInfo* dataLoadInfo | 表示指向数据加载信息OH_UdmfDataLoadInfo实例的指针。 |

**OH_UdmfDataLoadInfo_GetTypes()**

```ets
char** OH_UdmfDataLoadInfo_GetTypes(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int* count)
```

描述

从数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中获取数据类型列表。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadInfo* dataLoadInfo | 表示指向数据加载信息OH_UdmfDataLoadInfo实例的指针。 |
| unsigned int* count | 返回的数据类型数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| char** | 返回数据类型的字符串数组。 |

**OH_UdmfDataLoadInfo_SetType()**

```ets
void OH_UdmfDataLoadInfo_SetType(OH_UdmfDataLoadInfo* dataLoadInfo, const char* type)
```

描述

设置数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中的数据类型。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadInfo* dataLoadInfo | 表示指向数据加载信息OH_UdmfDataLoadInfo实例的指针。 |
| const char* type | 表示数据类型的字符串。 |

**OH_UdmfDataLoadInfo_GetRecordCount()**

```ets
int OH_UdmfDataLoadInfo_GetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo)
```

描述

获取数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中的记录数量。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadInfo* dataLoadInfo | 表示指向数据加载信息OH_UdmfDataLoadInfo实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回记录的数量。 |

**OH_UdmfDataLoadInfo_SetRecordCount()**

```ets
void OH_UdmfDataLoadInfo_SetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int recordCount)
```

描述

设置数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中的记录数量。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadInfo* dataLoadInfo | 表示指向数据加载信息OH_UdmfDataLoadInfo实例的指针。 |
| unsigned int recordCount | 表示记录的数量。 |

**OH_Udmf_DataLoadHandler()**

```ets
typedef OH_UdmfData* (*OH_Udmf_DataLoadHandler)(OH_UdmfDataLoadInfo* acceptableInfo)
```

描述

表示用于加载数据的回调函数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfDataLoadInfo* acceptableInfo | 表示接收端可接收的数据类型和数量信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfData* (*OH_Udmf_DataLoadHandler) | 返回待加载的数据。 |

**OH_UdmfOptions_GetVisibility()**

```ets
Udmf_Visibility OH_UdmfOptions_GetVisibility(OH_UdmfOptions* pThis)
```

描述

从数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中获取数据可见性等级。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Udmf_Visibility | 返回数据可见性等级Udmf_Visibility的值。 |

**OH_UdmfOptions_SetVisibility()**

```ets
int OH_UdmfOptions_SetVisibility(OH_UdmfOptions* pThis, Udmf_Visibility visibility)
```

描述

设置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中的数据可见性等级。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |
| Udmf_Visibility visibility | 数据可见性等级Udmf_Visibility参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。请参阅错误码定义Udmf_ErrCode。  若返回UDMF_E_OK，表示执行成功。  若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**UDMF_KEY_BUFFER_LEN()**

```ets
UDMF_KEY_BUFFER_LEN (512)
```

描述

统一数据对象唯一标识符最小空间长度。

起始版本： 12

**OH_Udmf_DataProgressListener()**

```ets
typedef void (*OH_Udmf_DataProgressListener)(OH_Udmf_ProgressInfo* progressInfo, OH_UdmfData* data)
```

描述

定义获取进度信息和数据的监听回调函数。

使用时需要判断数据是否返回空指针。只有当进度达到100%时，才会返回数据。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Udmf_ProgressInfo* progressInfo | 进度信息，作为出参使用。 |
| OH_UdmfData* data | 返回的统一数据对象，作为出参使用。 |

**OH_UdmfData_Create()**

```ets
OH_UdmfData* OH_UdmfData_Create()
```

描述

创建统一数据对象[OH_UdmfData](OH_UdmfData.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfData_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfdata_destroy)销毁实例对象，否则会导致内存泄漏。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfData* | 执行成功则返回一个指向统一数据对象OH_UdmfData实例对象的指针，否则返回nullptr。 |

参考：

OH_UdmfData

**OH_UdmfData_Destroy()**

```ets
void OH_UdmfData_Destroy(OH_UdmfData* pThis)
```

描述

销毁统一数据对象[OH_UdmfData](OH_UdmfData.md)指针指向的实例对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* pThis | 表示指向统一数据对象OH_UdmfData实例的指针。 |

参考：

OH_UdmfData

**OH_UdmfData_AddRecord()**

```ets
int OH_UdmfData_AddRecord(OH_UdmfData* pThis, OH_UdmfRecord* record)
```

描述

添加一个数据记录[OH_UdmfRecord](OH_UdmfRecord.md)到统一数据对象[OH_UdmfData](OH_UdmfData.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* pThis | 表示指向统一数据对象OH_UdmfData实例的指针。 |
| OH_UdmfRecord* record | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfData_HasType()**

```ets
bool OH_UdmfData_HasType(OH_UdmfData* pThis, const char* type)
```

描述

检查统一数据对象[OH_UdmfData](OH_UdmfData.md)中是否存在指定类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* pThis | 表示指向统一数据对象OH_UdmfData实例的指针。 |
| const char* type | 表示指定类型的字符串指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回查找类型的状态。返回false表示不存在指定类型，返回true表示存在指定类型。 |

**OH_UdmfData_GetTypes()**

```ets
char** OH_UdmfData_GetTypes(OH_UdmfData* pThis, unsigned int* count)
```

描述

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中包含的所有类型结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* pThis | 表示指向统一数据对象OH_UdmfData实例的指针。 |
| unsigned int* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| char** | 执行成功时返回统一数据对象的类型结果集，否则返回nullptr。 |

**OH_UdmfData_GetRecords()**

```ets
OH_UdmfRecord** OH_UdmfData_GetRecords(OH_UdmfData* pThis, unsigned int* count)
```

描述

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中包含的所有记录结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* pThis | 表示指向统一数据对象OH_UdmfData实例的指针。 |
| unsigned int* count | 该参数是输出参数，结果集中的记录数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfRecord** | 执行成功时返回统一数据记录OH_UdmfRecord结果集，否则返回nullptr。 |

**UdmfData_Finalize()**

```ets
typedef void (*UdmfData_Finalize)(void* context)
```

描述

定义用于释放上下文的回调函数，统一数据提供者对象销毁时触发。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| void* context | 要释放的上下文指针。 |

**OH_UdmfRecordProvider_Create()**

```ets
OH_UdmfRecordProvider* OH_UdmfRecordProvider_Create()
```

描述

创建一个统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfRecordProvider_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfrecordprovider_destroy)销毁实例对象，否则会导致内存泄漏。

起始版本： 13

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfRecordProvider* | 执行成功时返回一个指向统一数据提供者OH_UdmfRecordProvider实例对象的指针，否则返回nullptr。 |

**OH_UdmfRecordProvider_Destroy()**

```ets
int OH_UdmfRecordProvider_Destroy(OH_UdmfRecordProvider* provider)
```

描述

销毁统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)指针指向的实例对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecordProvider* provider | 表示指向统一数据提供者对象OH_UdmfRecordProvider实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecordProvider_GetData()**

```ets
typedef void* (*OH_UdmfRecordProvider_GetData)(void* context, const char* type)
```

描述

定义用于按类型获取数据的回调函数。当从OH_UdmfRecord中获取数据时，会触发此回调函数，得到的数据就是这个回调函数返回的数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| void* context | 用OH_UdmfRecordProvider_SetData设置的上下文指针。 |
| const char* type | 要获取的数据类型。详细类型信息见udmf_meta.h。 |

返回：

| 类型 | 说明 |
| --- | --- |
| void* | 需要返回一个标准化数据。 |

**OH_UdmfRecordProvider_SetData()**

```ets
int OH_UdmfRecordProvider_SetData(OH_UdmfRecordProvider* provider, void* context, const OH_UdmfRecordProvider_GetData callback, const UdmfData_Finalize finalize)
```

描述

设置统一数据提供者的数据提供回调函数。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecordProvider* provider | 指向统一数据提供者OH_UdmfRecordProvider实例对象的指针。 |
| void* context | 上下文指针，将作为第一个参数传入OH_UdmfRecordProvider_GetData。 |
| const OH_UdmfRecordProvider_GetData callback | 获取数据的回调函数。详见：OH_UdmfRecordProvider_GetData。 |
| const UdmfData_Finalize finalize | 可选的回调函数，可以用于统一数据提供者销毁时释放上下文数据。详见：UdmfData_Finalize。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_Create()**

```ets
OH_UdmfRecord* OH_UdmfRecord_Create()
```

描述

创建统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfRecord_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfrecord_destroy)销毁实例对象，否则会导致内存泄漏。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfRecord* | 执行成功则返回一个指向统一数据记录OH_UdmfRecord实例对象的指针，否则返回nullptr。 |

**OH_UdmfRecord_Destroy()**

```ets
void OH_UdmfRecord_Destroy(OH_UdmfRecord* pThis)
```

描述

销毁统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)指针指向的实例对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据对象OH_UdmfRecord实例的指针。 |

**OH_UdmfRecord_AddGeneralEntry()**

```ets
int OH_UdmfRecord_AddGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char* entry, unsigned int count)
```

描述

添加用户自定义的通用数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。对于已定义UDS的类型（比如PlainText、Link、Pixelmap等）不可使用该接口。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| const char* typeId | 表示数据类型标识，为和系统定义的类型进行区分，建议以'ApplicationDefined'开头。 |
| unsigned char* entry | 表示用户自定义数据。 |
| unsigned int count | 表示用户自定义数据的大小。数据大小不超过4KB。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddPlainText()**

```ets
int OH_UdmfRecord_AddPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText)
```

描述

增加纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsPlainText* plainText | 表示指向纯文本类型OH_UdsPlainText实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddHyperlink()**

```ets
int OH_UdmfRecord_AddHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink)
```

描述

增加超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsHyperlink* hyperlink | 表示指向超链接类型OH_UdsHyperlink实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddHtml()**

```ets
int OH_UdmfRecord_AddHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html)
```

描述

增加超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsHtml* html | 表示指向超文本标记语言类型OH_UdsHtml实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddAppItem()**

```ets
int OH_UdmfRecord_AddAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem)
```

描述

增加桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsAppItem* appItem | 表示指向桌面图标类型OH_UdsAppItem实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddFileUri()**

```ets
int OH_UdmfRecord_AddFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri)
```

描述

增加文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsFileUri* fileUri | 表示指向文件Uri类型OH_UdsFileUri实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddPixelMap()**

```ets
int OH_UdmfRecord_AddPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap)
```

描述

增加像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsPixelMap* pixelMap | 表示指向像素图片类型OH_UdsPixelMap实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddArrayBuffer()**

```ets
int OH_UdmfRecord_AddArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer)
```

描述

增加一个ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)的数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* record | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| const char* type | 表示自定义的ArrayBuffer数据的数据类型标识，不可与已有的数据类型标识重复。 |
| OH_UdsArrayBuffer* buffer | 表示指向ArrayBuffer类型OH_UdsArrayBuffer实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_AddContentForm()**

```ets
int OH_UdmfRecord_AddContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm)
```

描述

增加一个内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)的数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsContentForm* contentForm | 表示指向内容卡片类型OH_UdsContentForm实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_GetTypes()**

```ets
char** OH_UdmfRecord_GetTypes(OH_UdmfRecord* pThis, unsigned int* count)
```

描述

获取统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中所有类型的结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| unsigned int* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| char** | 执行成功时返回类型列表，否则返回nullptr。 |

**OH_UdmfRecord_GetGeneralEntry()**

```ets
int OH_UdmfRecord_GetGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char** entry, unsigned int* count)
```

描述

获取统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中的特定类型的数据结果集。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| const char* typeId | 表示数据类型标识。 |
| unsigned char** entry | 该参数是输出参数，结果集中数据的具体信息会写入该变量。 |
| unsigned int* count | 该参数是输出参数，结果集中的数据长度会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。 |

**OH_UdmfRecord_GetPlainText()**

```ets
int OH_UdmfRecord_GetPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsPlainText* plainText | 该参数是输出参数，表示指向纯文本类型OH_UdsPlainText实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。 |

**OH_UdmfRecord_GetHyperlink()**

```ets
int OH_UdmfRecord_GetHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsHyperlink* hyperlink | 该参数是输出参数，表示指向超链接类型OH_UdsHyperlink实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。 |

**OH_UdmfRecord_GetHtml()**

```ets
int OH_UdmfRecord_GetHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsHtml* html | 该参数是输出参数，表示指向超文本标记语言类型OH_UdsHtml实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。 |

**OH_UdmfRecord_GetAppItem()**

```ets
int OH_UdmfRecord_GetAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsAppItem* appItem | 该参数是输出参数，表示指向桌面图标类型OH_UdsAppItem实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。 |

**OH_UdmfRecord_SetProvider()**

```ets
int OH_UdmfRecord_SetProvider(OH_UdmfRecord* pThis, const char* const* types, unsigned int count, OH_UdmfRecordProvider* provider)
```

描述

将指定类型的统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)设置至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| const char* const* types | 表示一组指定的要提供的数据类型。 |
| unsigned int count | 表示指定的数据类型的数量。 |
| OH_UdmfRecordProvider* provider | 表示指向统一数据提供者对象OH_UdmfRecordProvider实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_GetFileUri()**

```ets
int OH_UdmfRecord_GetFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsFileUri* fileUri | 该参数是输出参数，表示指向文件Uri类型OH_UdsFileUri实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_GetPixelMap()**

```ets
int OH_UdmfRecord_GetPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsPixelMap* pixelMap | 该参数是输出参数，表示指向像素图片类型OH_UdsPixelMap实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_GetArrayBuffer()**

```ets
int OH_UdmfRecord_GetArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* record | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| const char* type | 表示要获取的ArrayBuffer类型数据的数据类型标识。 |
| OH_UdsArrayBuffer* buffer | 该参数是输出参数，表示指向ArrayBuffer类型OH_UdsArrayBuffer实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfRecord_GetContentForm()**

```ets
int OH_UdmfRecord_GetContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm)
```

描述

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)数据。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfRecord* pThis | 表示指向统一数据记录OH_UdmfRecord实例的指针。 |
| OH_UdsContentForm* contentForm | 该参数是输出参数，表示指向内容卡片类型OH_UdsContentForm实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfData_GetPrimaryPlainText()**

```ets
int OH_UdmfData_GetPrimaryPlainText(OH_UdmfData* data, OH_UdsPlainText* plainText)
```

描述

从统一数据对象[OH_UdmfData](OH_UdmfData.md)中获取第一个纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* data | 表示指向统一数据对象OH_UdmfData实例的指针。 |
| OH_UdsPlainText* plainText | 该参数是输出参数，表示指向纯文本类型OH_UdsPlainText实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfData_GetPrimaryHtml()**

```ets
int OH_UdmfData_GetPrimaryHtml(OH_UdmfData* data, OH_UdsHtml* html)
```

描述

从统一数据对象[OH_UdmfData](OH_UdmfData.md)中获取第一个超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* data | 表示指向统一数据对象OH_UdmfData实例的指针。 |
| OH_UdsHtml* html | 该参数是输出参数，表示指向超文本标记语言类型OH_UdsHtml实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfData_GetRecordCount()**

```ets
int OH_UdmfData_GetRecordCount(OH_UdmfData* data)
```

描述

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中包含的所有记录数量。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* data | 表示指向统一数据对象OH_UdmfData实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回统一数据对象OH_UdmfRecord的数量。 |

**OH_UdmfData_GetRecord()**

```ets
OH_UdmfRecord* OH_UdmfData_GetRecord(OH_UdmfData* data, unsigned int index)
```

描述

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中指定位置的数据记录。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* data | 表示指向统一数据对象OH_UdmfData实例的指针。 |
| unsigned int index | 表示要获取的统一数据记录OH_UdmfRecord在统一数据对象OH_UdmfData中的下标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfRecord* | 执行成功时返回统一数据记录OH_UdmfRecord实例对象的指针，否则返回nullptr。 |

**OH_UdmfData_IsLocal()**

```ets
bool OH_UdmfData_IsLocal(OH_UdmfData* data)
```

描述

检查统一数据对象[OH_UdmfData](OH_UdmfData.md)是否是来自本端设备的数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* data | 表示指向统一数据对象OH_UdmfData实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回数据是否是来自本端设备。返回true表示来自本端设备，返回false表示来自远端设备。 |

**OH_UdmfProperty_Create()**

```ets
OH_UdmfProperty* OH_UdmfProperty_Create(OH_UdmfData* unifiedData)
```

描述

创建统一数据对象中数据记录属性[OH_UdmfProperty](OH_UdmfProperty.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfProperty_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfproperty_destroy)销毁实例对象，否则会导致内存泄漏。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData* unifiedData | 表示指向统一数据对象OH_UdmfData实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfProperty* | 执行成功则返回一个指向属性OH_UdmfProperty实例对象的指针，否则返回nullptr。 |

**OH_UdmfProperty_Destroy()**

```ets
void OH_UdmfProperty_Destroy(OH_UdmfProperty* pThis)
```

描述

销毁数据属性[OH_UdmfProperty](OH_UdmfProperty.md)指针指向的实例对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |

**OH_UdmfProperty_GetTag()**

```ets
const char* OH_UdmfProperty_GetTag(OH_UdmfProperty* pThis)
```

描述

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取用户自定义标签值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 执行成功时返回自定义标签值的字符串指针，否则返回nullptr。 |

**OH_UdmfProperty_GetTimestamp()**

```ets
int64_t OH_UdmfProperty_GetTimestamp(OH_UdmfProperty* pThis)
```

描述

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取时间戳。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int64_t | 返回时间戳值。 |

**OH_UdmfProperty_GetShareOption()**

```ets
Udmf_ShareOption OH_UdmfProperty_GetShareOption(OH_UdmfProperty* pThis)
```

描述

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取设备内适用范围属性。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Udmf_ShareOption | 返回设备内适用范围属性Udmf_ShareOption值。 |

**OH_UdmfProperty_GetExtrasIntParam()**

```ets
int OH_UdmfProperty_GetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int defaultValue)
```

描述

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取自定义的附加整型参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |
| const char* key | 表示键值对的键。 |
| int defaultValue | 用于用户自行设置获取值失败时的默认值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 执行成功返回指定的键关联的整型值，否则返回用户设置的默认值defaultValue。 |

**OH_UdmfProperty_GetExtrasStringParam()**

```ets
const char* OH_UdmfProperty_GetExtrasStringParam(OH_UdmfProperty* pThis, const char* key)
```

描述

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取自定义的附加字符串参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |
| const char* key | 表示键值对的键。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 执行成功时返回指定的键关联的字符串值的指针，否则返回nullptr。 |

**OH_UdmfProperty_SetTag()**

```ets
int OH_UdmfProperty_SetTag(OH_UdmfProperty* pThis, const char* tag)
```

描述

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的自定义标签值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |
| const char* tag | 表示自定义标签值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfProperty_SetShareOption()**

```ets
int OH_UdmfProperty_SetShareOption(OH_UdmfProperty* pThis, Udmf_ShareOption option)
```

描述

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的设备内适用范围[Udmf_ShareOption](udmf.h.md#ZH-CN_TOPIC_0000002522240654__udmf_shareoption)参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfProperty实例的指针。 |
| Udmf_ShareOption option | 表示设备内适用范围Udmf_ShareOption参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfProperty_SetExtrasIntParam()**

```ets
int OH_UdmfProperty_SetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int param)
```

描述

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的附加整型参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向OH_UdmfRecord实例的指针。 |
| const char* key | 表示键值对的键。 |
| int param | 表示键值对的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfProperty_SetExtrasStringParam()**

```ets
int OH_UdmfProperty_SetExtrasStringParam(OH_UdmfProperty* pThis, const char* key, const char* param)
```

描述

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的附加字符串参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfProperty* pThis | 表示指向数据属性OH_UdmfRecord实例的指针。 |
| const char* key | 表示键值对的键。 |
| const char* param | 表示键值对的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfOptions_Create()**

```ets
OH_UdmfOptions* OH_UdmfOptions_Create()
```

描述

创建指向[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。当不再需要使用指针时，请使用[OH_UdmfOptions_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfoptions_destroy)销毁实例对象，否则会导致内存泄漏。

起始版本： 20

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfOptions* | 执行成功则返回一个指向数据操作选项OH_UdmfOptions实例的指针，否则返回nullptr。 |

**OH_UdmfOptions_Destroy()**

```ets
void OH_UdmfOptions_Destroy(OH_UdmfOptions* pThis)
```

描述

销毁指向[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |

**OH_UdmfOptions_GetKey()**

```ets
const char* OH_UdmfOptions_GetKey(OH_UdmfOptions* pThis)
```

描述

从数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中获取数据的唯一标识符信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 输入有效入参时返回符串指针，否则返回nullptr。 |

**OH_UdmfOptions_SetKey()**

```ets
int OH_UdmfOptions_SetKey(OH_UdmfOptions* pThis, const char* key)
```

描述

设置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中的数据的唯一标识符内容参数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |
| const char* key | 数据的唯一标识符的新字符串值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfOptions_GetIntention()**

```ets
Udmf_Intention OH_UdmfOptions_GetIntention(OH_UdmfOptions* pThis)
```

描述

从数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中获取数据通路信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Udmf_Intention | 返回Udmf_Intention的值。 |

**OH_UdmfOptions_SetIntention()**

```ets
int OH_UdmfOptions_SetIntention(OH_UdmfOptions* pThis, Udmf_Intention intention)
```

描述

设置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中的数据通路内容参数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |
| Udmf_Intention intention | 数据通路类型参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_UdmfOptions_Reset()**

```ets
int OH_UdmfOptions_Reset(OH_UdmfOptions* pThis)
```

描述

重置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例为空。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* pThis | 指向数据操作选项OH_UdmfOptions实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 |

**OH_Udmf_GetUnifiedData()**

```ets
int OH_Udmf_GetUnifiedData(const char* key, Udmf_Intention intention, OH_UdmfData* unifiedData)
```

描述

从统一数据管理框架数据库中获取统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* key | 表示数据库存储的唯一标识符。 |
| Udmf_Intention intention | 表示数据通路类型Udmf_Intention。 |
| OH_UdmfData* unifiedData | 该参数是输出参数，获取到的统一数据对象OH_UdmfData会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。 |

**OH_Udmf_GetUnifiedDataByOptions()**

```ets
int OH_Udmf_GetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize)
```

描述

通过数据通路类型从统一数据管理框架数据库中获取统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* options | 指向数据操作选项OH_UdmfOptions实例的指针。 |
| OH_UdmfData** dataArray | 该参数是输出参数，表示统一数据对象OH_UdmfData列表。 需要使用OH_UDMF_GetDataElementAt函数通过下标访问每个元素。 此指针需要使用OH_Udmf_DestroyDataArray函数释放。 |
| unsigned int* dataSize | 该参数是输出参数，表示获取到的统一数据对象个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。 |

**OH_Udmf_SetUnifiedData()**

```ets
int OH_Udmf_SetUnifiedData(Udmf_Intention intention, OH_UdmfData* unifiedData, char* key, unsigned int keyLen)
```

描述

从统一数据管理框架数据库中写入统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Udmf_Intention intention | 表示数据通路类型Udmf_Intention。 |
| OH_UdmfData* unifiedData | 表示统一数据对象OH_UdmfData数据。 |
| char* key | 表示成功将数据设置到数据库后对应数据的唯一标识符。 |
| unsigned int keyLen | 表示唯一标识符参数的空间大小，内存大小不小于512字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。 |

**OH_Udmf_SetUnifiedDataByOptions()**

```ets
int OH_Udmf_SetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData *unifiedData, char *key, unsigned int keyLen)
```

描述

从统一数据管理框架数据库中写入统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* options | 指向数据操作选项OH_UdmfOptions实例的指针。 |
| OH_UdmfData *unifiedData | 指向统一数据对象OH_UdmfData实例的指针。 |
| char *key | 成功将数据设置到数据库后对应数据的唯一标识符，内存大小不小于UDMF_KEY_BUFFER_LEN。 |
| unsigned int keyLen | 唯一标识符参数的空间大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。 |

**OH_Udmf_UpdateUnifiedData()**

```ets
int OH_Udmf_UpdateUnifiedData(OH_UdmfOptions* options, OH_UdmfData* unifiedData)
```

描述

对统一数据管理框架数据库中的统一数据对象[OH_UdmfData](OH_UdmfData.md)数据进行数据更改。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* options | 指向数据操作选项OH_UdmfOptions实例的指针。 |
| OH_UdmfData* unifiedData | 指向统一数据对象OH_UdmfData实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。 |

**OH_Udmf_DeleteUnifiedData()**

```ets
int OH_Udmf_DeleteUnifiedData(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize)
```

描述

删除统一数据管理框架数据库中的统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfOptions* options | 指向数据操作选项OH_UdmfOptions实例的指针。 |
| OH_UdmfData** dataArray | 该参数是输出参数，统一数据对象OH_UdmfData列表，需要使用OH_UDMF_GetDataElementAt函数通过下标访问每个元素。此指针需要使用OH_Udmf_DestroyDataArray函数释放。 |
| unsigned int* dataSize | 该参数是输出参数，表示获取到的统一数据对象个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。请参阅错误码定义Udmf_ErrCode。 若返回UDMF_E_OK，表示执行成功。 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。 若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。 |

**OH_Udmf_DestroyDataArray()**

```ets
void OH_Udmf_DestroyDataArray(OH_UdmfData** dataArray, unsigned int dataSize)
```

描述

销毁数据数组内存。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData** dataArray | 指向统一数据对象OH_UdmfData的指针列表。 |
| unsigned int dataSize | 列表中的数据大小。 |

参考：

OH_UdmfData

**OH_UdmfProgressInfo_GetProgress()**

```ets
int OH_UdmfProgressInfo_GetProgress(OH_Udmf_ProgressInfo* progressInfo)
```

描述

从进度信息[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)中获取进度百分比数据。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Udmf_ProgressInfo* progressInfo | 表示进度信息OH_Udmf_ProgressInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回进度百分比数据。 |

**OH_UdmfProgressInfo_GetStatus()**

```ets
int OH_UdmfProgressInfo_GetStatus(OH_Udmf_ProgressInfo* progressInfo)
```

描述

从进度信息[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)中获取状态信息。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Udmf_ProgressInfo* progressInfo | 表示进度信息OH_Udmf_ProgressInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回状态信息。 |

**OH_UdmfGetDataParams_Create()**

```ets
OH_UdmfGetDataParams* OH_UdmfGetDataParams_Create()
```

描述

创建异步获取UDMF数据的请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)指针及实例对象。

当不再需要使用指针时，请使用[OH_UdmfGetDataParams_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfgetdataparams_destroy)销毁实例对象，否则会导致内存泄漏。

起始版本： 15

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfGetDataParams* | 执行成功则返回一个指向属性OH_UdmfGetDataParams实例对象的指针，否则返回nullptr。 |

**OH_UdmfGetDataParams_Destroy()**

```ets
void OH_UdmfGetDataParams_Destroy(OH_UdmfGetDataParams* pThis)
```

描述

销毁异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)指针指向的实例对象。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfGetDataParams* pThis | 表示指向异步请求参数OH_UdmfGetDataParams实例的指针。 |

**OH_UdmfGetDataParams_SetDestUri()**

```ets
void OH_UdmfGetDataParams_SetDestUri(OH_UdmfGetDataParams* params, const char* destUri)
```

描述

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的目标路径。

若设置了目标路径，会将文件类型的数据进行拷贝到指定路径。回调中获取到的文件类型数据会被替换为目标路径的URI。

若不设置目标路径，则不会执行拷贝文件操作。回调中获取到的文件类型数据为源端路径URI。

若应用涉及复杂文件处理策略，或需要将文件拷贝在多个路径下时，建议不设置此参数，由应用自行完成文件拷贝相关处理。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfGetDataParams* params | 表示指向异步请求参数OH_UdmfGetDataParams实例的指针。 |
| const char* destUri | 表示目标路径地址。 |

**OH_UdmfGetDataParams_SetFileConflictOptions()**

```ets
void OH_UdmfGetDataParams_SetFileConflictOptions(OH_UdmfGetDataParams* params, const Udmf_FileConflictOptions options)
```

描述

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的文件冲突选项。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfGetDataParams* params | 表示指向异步请求参数OH_UdmfGetDataParams实例的指针。 |
| const Udmf_FileConflictOptions options | 表示文件拷贝冲突时的选项。 |

**OH_UdmfGetDataParams_SetProgressIndicator()**

```ets
void OH_UdmfGetDataParams_SetProgressIndicator(OH_UdmfGetDataParams* params, const Udmf_ProgressIndicator progressIndicator)
```

描述

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的进度条指示选项。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfGetDataParams* params | 表示指向异步请求参数OH_UdmfGetDataParams实例的指针。 |
| const Udmf_ProgressIndicator progressIndicator | 表示是否使用默认进度条选项。 |

**OH_UdmfGetDataParams_SetDataProgressListener()**

```ets
void OH_UdmfGetDataParams_SetDataProgressListener(OH_UdmfGetDataParams* params, const OH_Udmf_DataProgressListener dataProgressListener)
```

描述

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的监听回调函数。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfGetDataParams* params | 表示指向异步请求参数OH_UdmfGetDataParams实例的指针。 |
| const OH_Udmf_DataProgressListener dataProgressListener | 用户自定义的监听回调函数，可用于获取进度信息和数据。 |

**OH_UDMF_GetDataElementAt()**

```ets
OH_UdmfData* OH_UDMF_GetDataElementAt(OH_UdmfData** dataArray, unsigned int index)
```

描述

从统一数据对象[OH_UdmfData](OH_UdmfData.md)数组中获取指定下标的统一数据对象数据。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_UdmfData** dataArray | 指向统一数据对象OH_UdmfData的指针数组。 只接受从OH_Udmf_GetUnifiedDataByOptions和OH_Udmf_DeleteUnifiedData接口中获得的指针数组。 |
| unsigned int index | 表示要获取到的统一数据对象的下标。请确保该值不超出数组范围，否则会出现数组越界。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_UdmfData* | 执行成功则返回一个指向统一数据对象OH_UdmfData实例对象的指针，如果输入数组为空，则返回空。 |