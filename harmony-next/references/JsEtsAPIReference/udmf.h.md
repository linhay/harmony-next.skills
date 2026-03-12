# udmf.h

#### 概述

提供访问统一数据管理框架数据的接口、数据结构、枚举类型。

**引用文件：** <database/udmf/udmf.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：**[UDMF](UDMF.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_UdmfData](OH_UdmfData.md)OH_UdmfData定义统一数据对象数据结构。[OH_UdmfRecord](OH_UdmfRecord.md)OH_UdmfRecord定义统一数据对象中记录数据的数据结构，称为数据记录。[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)OH_UdmfRecordProvider定义统一数据对象中的数据提供者。[OH_UdmfProperty](OH_UdmfProperty.md)OH_UdmfProperty定义统一数据对象中数据记录的属性结构。[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)OH_Udmf_ProgressInfo定义进度信息的数据结构。[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)OH_UdmfGetDataParams定义异步获取UDMF数据的请求参数。[OH_UdmfOptions](OH_UdmfOptions.md)OH_UdmfOptions数据操作选项，定义数据操作的可选参数。[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)OH_UdmfDataLoadParams表示数据加载参数结构体。[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)OH_UdmfDataLoadInfo表示数据加载信息结构体。

#### 枚举

名称typedef关键字描述[Udmf_Intention](#ZH-CN_TOPIC_0000002497444728__udmf_intention)Udmf_Intention描述UDMF数据通路枚举类型。[Udmf_ShareOption](#ZH-CN_TOPIC_0000002497444728__udmf_shareoption)Udmf_ShareOptionUDMF支持的设备内使用范围类型枚举。[Udmf_FileConflictOptions](#ZH-CN_TOPIC_0000002497444728__udmf_fileconflictoptions)Udmf_FileConflictOptions定义文件拷贝冲突时的选项。[Udmf_ProgressIndicator](#ZH-CN_TOPIC_0000002497444728__udmf_progressindicator)Udmf_ProgressIndicator定义进度条指示选项，可选择是否采用系统默认进度显示。[Udmf_Visibility](#ZH-CN_TOPIC_0000002497444728__udmf_visibility)Udmf_Visibility定义数据的可见性等级。

#### 函数

名称typedef关键字描述[UDMF_KEY_BUFFER_LEN (512)](#ZH-CN_TOPIC_0000002497444728__udmf_key_buffer_len)-统一数据对象唯一标识符最小空间长度。[typedef void (*OH_Udmf_DataProgressListener)(OH_Udmf_ProgressInfo* progressInfo, OH_UdmfData* data)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_dataprogresslistener)OH_Udmf_DataProgressListener

定义获取进度信息和数据的监听回调函数。

使用时需要判断数据是否返回空指针。只有当进度达到100%时，才会返回数据。

[OH_UdmfData* OH_UdmfData_Create()](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_create)-创建统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfData_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdmfData_Destroy(OH_UdmfData* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_destroy)-销毁统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)指针指向的实例对象。[int OH_UdmfData_AddRecord(OH_UdmfData* pThis, OH_UdmfRecord* record)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_addrecord)-添加一个数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)到统一数据对象[OH_UdmfData](OH_UdmfData.md)中。[bool OH_UdmfData_HasType(OH_UdmfData* pThis, const char* type)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_hastype)-检查统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)中是否存在指定类型。[char** OH_UdmfData_GetTypes(OH_UdmfData* pThis, unsigned int* count)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_gettypes)-获取统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)中包含的所有类型结果集。[OH_UdmfRecord** OH_UdmfData_GetRecords(OH_UdmfData* pThis, unsigned int* count)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_getrecords)-获取统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)中包含的所有记录结果集。[typedef void (*UdmfData_Finalize)(void* context)](#ZH-CN_TOPIC_0000002497444728__udmfdata_finalize)UdmfData_Finalize定义用于释放上下文的回调函数，统一数据提供者对象销毁时触发。[OH_UdmfRecordProvider* OH_UdmfRecordProvider_Create()](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_create)-创建一个统一数据提供者[OH_UdmfRecordProvider](zh-cn_topic_0000002497444746.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfRecordProvider_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_destroy)销毁实例对象，否则会导致内存泄漏。[int OH_UdmfRecordProvider_Destroy(OH_UdmfRecordProvider* provider)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_destroy)-销毁统一数据提供者[OH_UdmfRecordProvider](zh-cn_topic_0000002497444746.html)指针指向的实例对象。[typedef void* (*OH_UdmfRecordProvider_GetData)(void* context, const char* type)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_getdata)OH_UdmfRecordProvider_GetData定义用于按类型获取数据的回调函数。当从OH_UdmfRecord中获取数据时，会触发此回调函数，得到的数据就是这个回调函数返回的数据。[int OH_UdmfRecordProvider_SetData(OH_UdmfRecordProvider* provider, void* context, const OH_UdmfRecordProvider_GetData callback, const UdmfData_Finalize finalize)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_setdata)-设置统一数据提供者的数据提供回调函数。[OH_UdmfRecord* OH_UdmfRecord_Create()](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_create)-创建统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfRecord_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdmfRecord_Destroy(OH_UdmfRecord* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_destroy)-销毁统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)指针指向的实例对象。[int OH_UdmfRecord_AddGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char* entry, unsigned int count)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addgeneralentry)-添加用户自定义的通用数据至统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中。对于已定义UDS的类型（比如PlainText、Link、Pixelmap等）不可使用该接口。[int OH_UdmfRecord_AddPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addplaintext)-增加纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_AddHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addhyperlink)-增加超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_AddHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addhtml)-增加超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_AddAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addappitem)-增加桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_AddFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addfileuri)-增加文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_AddPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addpixelmap)-增加像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_AddArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addarraybuffer)-增加一个ArrayBuffer类型[OH_UdsArrayBuffer](zh-cn_topic_0000002529284723.html)的数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_AddContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_addcontentform)-增加一个内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)的数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[char** OH_UdmfRecord_GetTypes(OH_UdmfRecord* pThis, unsigned int* count)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_gettypes)-获取统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中所有类型的结果集。[int OH_UdmfRecord_GetGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char** entry, unsigned int* count)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_getgeneralentry)-获取统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中的特定类型的数据结果集。[int OH_UdmfRecord_GetPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_getplaintext)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据。[int OH_UdmfRecord_GetHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_gethyperlink)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)数据。[int OH_UdmfRecord_GetHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_gethtml)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据。[int OH_UdmfRecord_GetAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_getappitem)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)数据。[int OH_UdmfRecord_SetProvider(OH_UdmfRecord* pThis, const char* const* types, unsigned int count, OH_UdmfRecordProvider* provider)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_setprovider)-将指定类型的统一数据提供者[OH_UdmfRecordProvider](zh-cn_topic_0000002497444746.html)设置至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。[int OH_UdmfRecord_GetFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_getfileuri)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)数据。[int OH_UdmfRecord_GetPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_getpixelmap)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)数据。[int OH_UdmfRecord_GetArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_getarraybuffer)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)数据。[int OH_UdmfRecord_GetContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm)](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_getcontentform)-从统一数据记录[OH_UdmfRecord](zh-cn_topic_0000002497604724.html)中获取内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)数据。[int OH_UdmfData_GetPrimaryPlainText(OH_UdmfData* data, OH_UdsPlainText* plainText)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_getprimaryplaintext)-从统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)中获取第一个纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据。[int OH_UdmfData_GetPrimaryHtml(OH_UdmfData* data, OH_UdsHtml* html)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_getprimaryhtml)-从统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)中获取第一个超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据。[int OH_UdmfData_GetRecordCount(OH_UdmfData* data)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_getrecordcount)-获取统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)中包含的所有记录数量。[OH_UdmfRecord* OH_UdmfData_GetRecord(OH_UdmfData* data, unsigned int index)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_getrecord)-获取统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)中指定位置的数据记录。[bool OH_UdmfData_IsLocal(OH_UdmfData* data)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_islocal)-检查统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)是否是来自本端设备的数据。[OH_UdmfProperty* OH_UdmfProperty_Create(OH_UdmfData* unifiedData)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_create)-创建统一数据对象中数据记录属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfProperty_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdmfProperty_Destroy(OH_UdmfProperty* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_destroy)-销毁数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)指针指向的实例对象。[const char* OH_UdmfProperty_GetTag(OH_UdmfProperty* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_gettag)-从数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)中获取用户自定义标签值。[int64_t OH_UdmfProperty_GetTimestamp(OH_UdmfProperty* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_gettimestamp)-从数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)中获取时间戳。[Udmf_ShareOption OH_UdmfProperty_GetShareOption(OH_UdmfProperty* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_getshareoption)-从数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)中获取设备内适用范围属性。[int OH_UdmfProperty_GetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int defaultValue)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_getextrasintparam)-从数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)中获取自定义的附加整型参数。[const char* OH_UdmfProperty_GetExtrasStringParam(OH_UdmfProperty* pThis, const char* key)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_getextrasstringparam)-从数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)中获取自定义的附加字符串参数。[int OH_UdmfProperty_SetTag(OH_UdmfProperty* pThis, const char* tag)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_settag)-设置数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)的自定义标签值。[int OH_UdmfProperty_SetShareOption(OH_UdmfProperty* pThis, Udmf_ShareOption option)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_setshareoption)-设置数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)的设备内适用范围[Udmf_ShareOption](udmf.h.md#ZH-CN_TOPIC_0000002497444728__udmf_shareoption)参数。[int OH_UdmfProperty_SetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int param)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_setextrasintparam)-设置数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)的附加整型参数。[int OH_UdmfProperty_SetExtrasStringParam(OH_UdmfProperty* pThis, const char* key, const char* param)](#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_setextrasstringparam)-设置数据属性[OH_UdmfProperty](zh-cn_topic_0000002529284717.html)的附加字符串参数。[OH_UdmfOptions* OH_UdmfOptions_Create()](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_create)-创建指向[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例的指针。[void OH_UdmfOptions_Destroy(OH_UdmfOptions* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_destroy)-销毁指向[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例的指针。[const char* OH_UdmfOptions_GetKey(OH_UdmfOptions* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_getkey)-从数据操作选项[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例中获取数据的唯一标识符信息。[int OH_UdmfOptions_SetKey(OH_UdmfOptions* pThis, const char* key)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_setkey)-设置数据操作选项[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例中的数据的唯一标识符内容参数。[Udmf_Intention OH_UdmfOptions_GetIntention(OH_UdmfOptions* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_getintention)-从数据操作选项[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例中获取数据通路信息。[int OH_UdmfOptions_SetIntention(OH_UdmfOptions* pThis, Udmf_Intention intention)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_setintention)-设置数据操作选项[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例中的数据通路内容参数。[int OH_UdmfOptions_Reset(OH_UdmfOptions* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_reset)-重置数据操作选项[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例为空。[int OH_Udmf_GetUnifiedData(const char* key, Udmf_Intention intention, OH_UdmfData* unifiedData)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_getunifieddata)-从统一数据管理框架数据库中获取统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)数据。[int OH_Udmf_GetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_getunifieddatabyoptions)-通过数据通路类型从统一数据管理框架数据库中获取统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)数据。[int OH_Udmf_SetUnifiedData(Udmf_Intention intention, OH_UdmfData* unifiedData, char* key, unsigned int keyLen)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_setunifieddata)-从统一数据管理框架数据库中写入统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)数据。[int OH_Udmf_SetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData *unifiedData, char *key, unsigned int keyLen)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_setunifieddatabyoptions)-从统一数据管理框架数据库中写入统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)数据。[int OH_Udmf_UpdateUnifiedData(OH_UdmfOptions* options, OH_UdmfData* unifiedData)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_updateunifieddata)-对统一数据管理框架数据库中的统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)数据进行数据更改。[int OH_Udmf_DeleteUnifiedData(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_deleteunifieddata)-删除统一数据管理框架数据库中的统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)数据。[void OH_Udmf_DestroyDataArray(OH_UdmfData** dataArray, unsigned int dataSize)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_destroydataarray)-销毁数据数组内存。[int OH_UdmfProgressInfo_GetProgress(OH_Udmf_ProgressInfo* progressInfo)](#ZH-CN_TOPIC_0000002497444728__oh_udmfprogressinfo_getprogress)-从进度信息[OH_Udmf_ProgressInfo](zh-cn_topic_0000002529444691.html)中获取进度百分比数据。[int OH_UdmfProgressInfo_GetStatus(OH_Udmf_ProgressInfo* progressInfo)](#ZH-CN_TOPIC_0000002497444728__oh_udmfprogressinfo_getstatus)-从进度信息[OH_Udmf_ProgressInfo](zh-cn_topic_0000002529444691.html)中获取状态信息。[OH_UdmfGetDataParams* OH_UdmfGetDataParams_Create()](#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_create)-

创建异步获取UDMF数据的请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)指针及实例对象。

当不再需要使用指针时，请使用[OH_UdmfGetDataParams_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_destroy)销毁实例对象，否则会导致内存泄漏。

[void OH_UdmfGetDataParams_Destroy(OH_UdmfGetDataParams* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_destroy)-销毁异步请求参数[OH_UdmfGetDataParams](zh-cn_topic_0000002497604726.html)指针指向的实例对象。[void OH_UdmfGetDataParams_SetDestUri(OH_UdmfGetDataParams* params, const char* destUri)](#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_setdesturi)-

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的目标路径。

若设置了目标路径，会将文件类型的数据进行拷贝到指定路径。回调中获取到的文件类型数据会被替换为目标路径的URI。

若不设置目标路径，则不会执行拷贝文件操作。回调中获取到的文件类型数据为源端路径URI。

若应用涉及复杂文件处理策略，或需要将文件拷贝在多个路径下时，建议不设置此参数，由应用自行完成文件拷贝相关处理。

[void OH_UdmfGetDataParams_SetFileConflictOptions(OH_UdmfGetDataParams* params, const Udmf_FileConflictOptions options)](#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_setfileconflictoptions)-设置异步请求参数[OH_UdmfGetDataParams](zh-cn_topic_0000002497604726.html)中的文件冲突选项。[void OH_UdmfGetDataParams_SetProgressIndicator(OH_UdmfGetDataParams* params, const Udmf_ProgressIndicator progressIndicator)](#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_setprogressindicator)-设置异步请求参数[OH_UdmfGetDataParams](zh-cn_topic_0000002497604726.html)中的进度条指示选项。[void OH_UdmfGetDataParams_SetDataProgressListener(OH_UdmfGetDataParams* params, const OH_Udmf_DataProgressListener dataProgressListener)](#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_setdataprogresslistener)-设置异步请求参数[OH_UdmfGetDataParams](zh-cn_topic_0000002497604726.html)中的监听回调函数。[Udmf_Visibility OH_UdmfOptions_GetVisibility(OH_UdmfOptions* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_getvisibility)-从数据操作选项[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例中获取数据可见性等级。[int OH_UdmfOptions_SetVisibility(OH_UdmfOptions* pThis, Udmf_Visibility visibility)](#ZH-CN_TOPIC_0000002497444728__oh_udmfoptions_setvisibility)-设置数据操作选项[OH_UdmfOptions](zh-cn_topic_0000002497444748.html)实例中的数据可见性等级。[typedef OH_UdmfData* (*OH_Udmf_DataLoadHandler)(OH_UdmfDataLoadInfo* acceptableInfo)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_dataloadhandler)OH_Udmf_DataLoadHandler表示用于加载数据的回调函数。[OH_UdmfDataLoadParams* OH_UdmfDataLoadParams_Create()](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadparams_create)-创建指向数据加载参数[OH_UdmfDataLoadParams](zh-cn_topic_0000002529284719.html)实例的指针。[void OH_UdmfDataLoadParams_Destroy(OH_UdmfDataLoadParams* pThis)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadparams_destroy)-销毁数据加载参数[OH_UdmfDataLoadParams](zh-cn_topic_0000002529284719.html)指针指向的实例对象。[void OH_UdmfDataLoadParams_SetLoadHandler(OH_UdmfDataLoadParams* params, const OH_Udmf_DataLoadHandler dataLoadHandler)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadparams_setloadhandler)-设置数据加载参数[OH_UdmfDataLoadParams](zh-cn_topic_0000002529284719.html)中的数据加载处理函数。[void OH_UdmfDataLoadParams_SetDataLoadInfo(OH_UdmfDataLoadParams* params, OH_UdmfDataLoadInfo* dataLoadInfo)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadparams_setdataloadinfo)-设置数据加载参数[OH_UdmfDataLoadParams](zh-cn_topic_0000002529284719.html)中的数据加载信息。[OH_UdmfDataLoadInfo* OH_UdmfDataLoadInfo_Create()](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadinfo_create)-创建指向数据加载信息[OH_UdmfDataLoadInfo](zh-cn_topic_0000002529444693.html)实例的指针。[void OH_UdmfDataLoadInfo_Destroy(OH_UdmfDataLoadInfo* dataLoadInfo)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadinfo_destroy)-销毁数据加载信息[OH_UdmfDataLoadInfo](zh-cn_topic_0000002529444693.html)指针指向的实例对象。[char** OH_UdmfDataLoadInfo_GetTypes(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int* count)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadinfo_gettypes)-从数据加载信息[OH_UdmfDataLoadInfo](zh-cn_topic_0000002529444693.html)中获取数据类型列表。[void OH_UdmfDataLoadInfo_SetType(OH_UdmfDataLoadInfo* dataLoadInfo, const char* type)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadinfo_settype)-设置数据加载信息[OH_UdmfDataLoadInfo](zh-cn_topic_0000002529444693.html)中的数据类型。[int OH_UdmfDataLoadInfo_GetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadinfo_getrecordcount)-获取数据加载信息[OH_UdmfDataLoadInfo](zh-cn_topic_0000002529444693.html)中的记录数量。[void OH_UdmfDataLoadInfo_SetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int recordCount)](#ZH-CN_TOPIC_0000002497444728__oh_udmfdataloadinfo_setrecordcount)-设置数据加载信息[OH_UdmfDataLoadInfo](zh-cn_topic_0000002529444693.html)中的记录数量。[OH_UdmfData* OH_UDMF_GetDataElementAt(OH_UdmfData** dataArray, unsigned int index)](#ZH-CN_TOPIC_0000002497444728__oh_udmf_getdataelementat)-从统一数据对象[OH_UdmfData](zh-cn_topic_0000002529444689.html)数组中获取指定下标的统一数据对象数据。

#### 枚举类型说明

#### Udmf_Intention

```ets
enum Udmf_Intention
```

**描述**

描述UDMF数据通路枚举类型。

**起始版本：** 12

枚举项描述UDMF_INTENTION_DRAG拖拽数据通路。UDMF_INTENTION_PASTEBOARD剪贴板数据通路。UDMF_INTENTION_DATA_HUB

公共数据通路。

**起始版本：** 20

UDMF_INTENTION_SYSTEM_SHARE

系统分享数据通路。

**起始版本：** 20

UDMF_INTENTION_PICKER

Picker数据通路。

**起始版本：** 20

UDMF_INTENTION_MENU

菜单数据通路。

**起始版本：** 20

#### Udmf_ShareOption

```ets
enum Udmf_ShareOption
```

**描述**

UDMF支持的设备内使用范围类型枚举。

**起始版本：** 12

枚举项描述SHARE_OPTIONS_INVALID表示不合法的使用范围类型。SHARE_OPTIONS_IN_APP表示允许在本设备同应用内使用。SHARE_OPTIONS_CROSS_APP表示允许在本设备内跨应用使用。

#### Udmf_FileConflictOptions

```ets
enum Udmf_FileConflictOptions
```

**描述**

定义文件拷贝冲突时的选项。

**起始版本：** 15

枚举项描述UDMF_OVERWRITE = 0目标路径存在同文件名时覆盖。若不配置策略，默认使用改策略。UDMF_SKIP = 1目标路径存在同文件名时跳过。

#### Udmf_ProgressIndicator

```ets
enum Udmf_ProgressIndicator
```

**描述**

定义进度条指示选项，可选择是否采用系统默认进度显示。

**起始版本：** 15

枚举项描述UDMF_NONE = 0不采用系统默认进度显示。UDMF_DEFAULT = 1采用系统默认进度显示，500ms内获取数据完成将不会拉起默认进度条。

#### Udmf_Visibility

```ets
enum Udmf_Visibility
```

**描述**

定义数据的可见性等级。

**起始版本：** 20

枚举项描述UDMF_ALL可见性等级，所有应用可见。UDMF_OWN_PROCESS可见性等级，仅数据提供者可见。

#### 函数说明

#### OH_UdmfGetDataParams_SetAcceptableInfo()

```ets
void OH_UdmfGetDataParams_SetAcceptableInfo(OH_UdmfGetDataParams* params, OH_UdmfDataLoadInfo* acceptableInfo)
```

**描述**

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中可接收的数据描述信息。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)* params表示指向[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)实例的指针。[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* acceptableInfo表示指向[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。

#### OH_UdmfDataLoadParams_Create()

```ets
OH_UdmfDataLoadParams* OH_UdmfDataLoadParams_Create()
```

**描述**

创建指向数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)实例的指针。

**起始版本：** 20

**返回：**

类型说明[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)*如果创建成功，返回一个指向数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)实例的指针；否则返回nullptr。

#### OH_UdmfDataLoadParams_Destroy()

```ets
void OH_UdmfDataLoadParams_Destroy(OH_UdmfDataLoadParams* pThis)
```

**描述**

销毁数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)指针指向的实例对象。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)* pThis表示指向数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)实例的指针。

#### OH_UdmfDataLoadParams_SetLoadHandler()

```ets
void OH_UdmfDataLoadParams_SetLoadHandler(OH_UdmfDataLoadParams* params, const OH_Udmf_DataLoadHandler dataLoadHandler)
```

**描述**

设置数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)中的数据加载处理函数。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)* params表示指向数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)实例的指针。[const OH_Udmf_DataLoadHandler](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmf_dataloadhandler) dataLoadHandler表示用户定义的数据加载处理函数。

#### OH_UdmfDataLoadParams_SetDataLoadInfo()

```ets
void OH_UdmfDataLoadParams_SetDataLoadInfo(OH_UdmfDataLoadParams* params, OH_UdmfDataLoadInfo* dataLoadInfo)
```

**描述**

设置数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)中的数据加载信息。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)* params表示指向数据加载参数[OH_UdmfDataLoadParams](OH_UdmfDataLoadParams.md)实例的指针。[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* dataLoadInfo表示指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。

#### OH_UdmfDataLoadInfo_Create()

```ets
OH_UdmfDataLoadInfo* OH_UdmfDataLoadInfo_Create()
```

**描述**

创建指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。

**起始版本：** 20

**返回：**

类型说明[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)*如果创建成功，返回一个指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针；否则返回nullptr。

#### OH_UdmfDataLoadInfo_Destroy()

```ets
void OH_UdmfDataLoadInfo_Destroy(OH_UdmfDataLoadInfo* dataLoadInfo)
```

**描述**

销毁数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)指针指向的实例对象。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* dataLoadInfo表示指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。

#### OH_UdmfDataLoadInfo_GetTypes()

```ets
char** OH_UdmfDataLoadInfo_GetTypes(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int* count)
```

**描述**

从数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中获取数据类型列表。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* dataLoadInfo表示指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。unsigned int* count返回的数据类型数量。

**返回：**

类型说明char**返回数据类型的字符串数组。

#### OH_UdmfDataLoadInfo_SetType()

```ets
void OH_UdmfDataLoadInfo_SetType(OH_UdmfDataLoadInfo* dataLoadInfo, const char* type)
```

**描述**

设置数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中的数据类型。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* dataLoadInfo表示指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。const char* type表示数据类型的字符串。

#### OH_UdmfDataLoadInfo_GetRecordCount()

```ets
int OH_UdmfDataLoadInfo_GetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo)
```

**描述**

获取数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中的记录数量。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* dataLoadInfo表示指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。

**返回：**

类型说明int返回记录的数量。

#### OH_UdmfDataLoadInfo_SetRecordCount()

```ets
void OH_UdmfDataLoadInfo_SetRecordCount(OH_UdmfDataLoadInfo* dataLoadInfo, unsigned int recordCount)
```

**描述**

设置数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)中的记录数量。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* dataLoadInfo表示指向数据加载信息[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)实例的指针。unsigned int recordCount表示记录的数量。

#### OH_Udmf_DataLoadHandler()

```ets
typedef OH_UdmfData* (*OH_Udmf_DataLoadHandler)(OH_UdmfDataLoadInfo* acceptableInfo)
```

**描述**

表示用于加载数据的回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfDataLoadInfo](OH_UdmfDataLoadInfo.md)* acceptableInfo表示接收端可接收的数据类型和数量信息。

**返回：**

类型说明[OH_UdmfData](OH_UdmfData.md)* (*OH_Udmf_DataLoadHandler)返回待加载的数据。

#### OH_UdmfOptions_GetVisibility()

```ets
Udmf_Visibility OH_UdmfOptions_GetVisibility(OH_UdmfOptions* pThis)
```

**描述**

从数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中获取数据可见性等级。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

**返回：**

类型说明[Udmf_Visibility](udmf.h.md#ZH-CN_TOPIC_0000002497444728__udmf_visibility)返回数据可见性等级[Udmf_Visibility](udmf.h.md#ZH-CN_TOPIC_0000002497444728__udmf_visibility)的值。

#### OH_UdmfOptions_SetVisibility()

```ets
int OH_UdmfOptions_SetVisibility(OH_UdmfOptions* pThis, Udmf_Visibility visibility)
```

**描述**

设置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中的数据可见性等级。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。[Udmf_Visibility](udmf.h.md#ZH-CN_TOPIC_0000002497444728__udmf_visibility) visibility数据可见性等级[Udmf_Visibility](udmf.h.md#ZH-CN_TOPIC_0000002497444728__udmf_visibility)参数。

**返回：**

类型说明int

返回执行结果。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

 若返回UDMF_E_OK，表示执行成功。

 若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### UDMF_KEY_BUFFER_LEN()

```ets
UDMF_KEY_BUFFER_LEN (512)
```

**描述**

统一数据对象唯一标识符最小空间长度。

**起始版本：** 12

#### OH_Udmf_DataProgressListener()

```ets
typedef void (*OH_Udmf_DataProgressListener)(OH_Udmf_ProgressInfo* progressInfo, OH_UdmfData* data)
```

**描述**

定义获取进度信息和数据的监听回调函数。

使用时需要判断数据是否返回空指针。只有当进度达到100%时，才会返回数据。

**起始版本：** 15

**参数：**

参数项描述[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)* progressInfo进度信息，作为出参使用。[OH_UdmfData](OH_UdmfData.md)* data返回的统一数据对象，作为出参使用。

#### OH_UdmfData_Create()

```ets
OH_UdmfData* OH_UdmfData_Create()
```

**描述**

创建统一数据对象[OH_UdmfData](OH_UdmfData.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfData_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfdata_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

类型说明[OH_UdmfData](OH_UdmfData.md)*执行成功则返回一个指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例对象的指针，否则返回nullptr。

**参考：**

OH_UdmfData

#### OH_UdmfData_Destroy()

```ets
void OH_UdmfData_Destroy(OH_UdmfData* pThis)
```

**描述**

销毁统一数据对象[OH_UdmfData](OH_UdmfData.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* pThis表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。

**参考：**

OH_UdmfData

#### OH_UdmfData_AddRecord()

```ets
int OH_UdmfData_AddRecord(OH_UdmfData* pThis, OH_UdmfRecord* record)
```

**描述**

添加一个数据记录[OH_UdmfRecord](OH_UdmfRecord.md)到统一数据对象[OH_UdmfData](OH_UdmfData.md)中。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* pThis表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。[OH_UdmfRecord](OH_UdmfRecord.md)* record表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfData_HasType()

```ets
bool OH_UdmfData_HasType(OH_UdmfData* pThis, const char* type)
```

**描述**

检查统一数据对象[OH_UdmfData](OH_UdmfData.md)中是否存在指定类型。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* pThis表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。const char* type表示指定类型的字符串指针。

**返回：**

类型说明bool返回查找类型的状态。返回false表示不存在指定类型，返回true表示存在指定类型。

#### OH_UdmfData_GetTypes()

```ets
char** OH_UdmfData_GetTypes(OH_UdmfData* pThis, unsigned int* count)
```

**描述**

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中包含的所有类型结果集。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* pThis表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。unsigned int* count该参数是输出参数，结果集中的类型数量会写入该变量。

**返回：**

类型说明char**执行成功时返回统一数据对象的类型结果集，否则返回nullptr。

#### OH_UdmfData_GetRecords()

```ets
OH_UdmfRecord** OH_UdmfData_GetRecords(OH_UdmfData* pThis, unsigned int* count)
```

**描述**

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中包含的所有记录结果集。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* pThis表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。unsigned int* count该参数是输出参数，结果集中的记录数量会写入该变量。

**返回：**

类型说明[OH_UdmfRecord](OH_UdmfRecord.md)**执行成功时返回统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)结果集，否则返回nullptr。

#### UdmfData_Finalize()

```ets
typedef void (*UdmfData_Finalize)(void* context)
```

**描述**

定义用于释放上下文的回调函数，统一数据提供者对象销毁时触发。

**起始版本：** 13

**参数：**

参数项描述void* context要释放的上下文指针。

#### OH_UdmfRecordProvider_Create()

```ets
OH_UdmfRecordProvider* OH_UdmfRecordProvider_Create()
```

**描述**

创建一个统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfRecordProvider_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 13

**返回：**

类型说明[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)*执行成功时返回一个指向统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)实例对象的指针，否则返回nullptr。

#### OH_UdmfRecordProvider_Destroy()

```ets
int OH_UdmfRecordProvider_Destroy(OH_UdmfRecordProvider* provider)
```

**描述**

销毁统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)指针指向的实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)* provider表示指向统一数据提供者对象[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecordProvider_GetData()

```ets
typedef void* (*OH_UdmfRecordProvider_GetData)(void* context, const char* type)
```

**描述**

定义用于按类型获取数据的回调函数。当从OH_UdmfRecord中获取数据时，会触发此回调函数，得到的数据就是这个回调函数返回的数据。

**起始版本：** 13

**参数：**

参数项描述void* context用[OH_UdmfRecordProvider_SetData](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_setdata)设置的上下文指针。const char* type要获取的数据类型。详细类型信息见[udmf_meta.h](udmf_meta.h.md)。

**返回：**

类型说明void*需要返回一个标准化数据。

#### OH_UdmfRecordProvider_SetData()

```ets
int OH_UdmfRecordProvider_SetData(OH_UdmfRecordProvider* provider, void* context, const OH_UdmfRecordProvider_GetData callback, const UdmfData_Finalize finalize)
```

**描述**

设置统一数据提供者的数据提供回调函数。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)* provider指向统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)实例对象的指针。void* context上下文指针，将作为第一个参数传入[OH_UdmfRecordProvider_GetData](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_getdata)。const [OH_UdmfRecordProvider_GetData](#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_getdata) callback获取数据的回调函数。详见：[OH_UdmfRecordProvider_GetData](zh-cn_topic_0000002497444728.html#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_getdata)。const [UdmfData_Finalize](#ZH-CN_TOPIC_0000002497444728__udmfdata_finalize) finalize可选的回调函数，可以用于统一数据提供者销毁时释放上下文数据。详见：[UdmfData_Finalize](zh-cn_topic_0000002497444728.html#ZH-CN_TOPIC_0000002497444728__udmfdata_finalize)。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_Create()

```ets
OH_UdmfRecord* OH_UdmfRecord_Create()
```

**描述**

创建统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfRecord_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecord_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

类型说明[OH_UdmfRecord](OH_UdmfRecord.md)*执行成功则返回一个指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例对象的指针，否则返回nullptr。

#### OH_UdmfRecord_Destroy()

```ets
void OH_UdmfRecord_Destroy(OH_UdmfRecord* pThis)
```

**描述**

销毁统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据对象[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。

#### OH_UdmfRecord_AddGeneralEntry()

```ets
int OH_UdmfRecord_AddGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char* entry, unsigned int count)
```

**描述**

添加用户自定义的通用数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。对于已定义UDS的类型（比如PlainText、Link、Pixelmap等）不可使用该接口。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。const char* typeId表示数据类型标识，为和系统定义的类型进行区分，建议以'ApplicationDefined'开头。unsigned char* entry表示用户自定义数据。unsigned int count表示用户自定义数据的大小。数据大小不超过4KB。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddPlainText()

```ets
int OH_UdmfRecord_AddPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText)
```

**描述**

增加纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsPlainText](OH_UdsPlainText.md)* plainText表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddHyperlink()

```ets
int OH_UdmfRecord_AddHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink)
```

**描述**

增加超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsHyperlink](OH_UdsHyperlink.md)* hyperlink表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddHtml()

```ets
int OH_UdmfRecord_AddHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html)
```

**描述**

增加超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsHtml](OH_UdsHtml.md)* html表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddAppItem()

```ets
int OH_UdmfRecord_AddAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem)
```

**描述**

增加桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsAppItem](OH_UdsAppItem.md)* appItem表示指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddFileUri()

```ets
int OH_UdmfRecord_AddFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri)
```

**描述**

增加文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsFileUri](OH_UdsFileUri.md)* fileUri表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddPixelMap()

```ets
int OH_UdmfRecord_AddPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap)
```

**描述**

增加像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsPixelMap](OH_UdsPixelMap.md)* pixelMap表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddArrayBuffer()

```ets
int OH_UdmfRecord_AddArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer)
```

**描述**

增加一个ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)的数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* record表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。const char* type表示自定义的ArrayBuffer数据的数据类型标识，不可与已有的数据类型标识重复。[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)* buffer表示指向ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_AddContentForm()

```ets
int OH_UdmfRecord_AddContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm)
```

**描述**

增加一个内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)的数据至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 14

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsContentForm](OH_UdsContentForm.md)* contentForm表示指向内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_GetTypes()

```ets
char** OH_UdmfRecord_GetTypes(OH_UdmfRecord* pThis, unsigned int* count)
```

**描述**

获取统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中所有类型的结果集。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。unsigned int* count该参数是输出参数，结果集中的类型数量会写入该变量。

**返回：**

类型说明char**执行成功时返回类型列表，否则返回nullptr。

#### OH_UdmfRecord_GetGeneralEntry()

```ets
int OH_UdmfRecord_GetGeneralEntry(OH_UdmfRecord* pThis, const char* typeId, unsigned char** entry, unsigned int* count)
```

**描述**

获取统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中的特定类型的数据结果集。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。const char* typeId表示数据类型标识。unsigned char** entry该参数是输出参数，结果集中数据的具体信息会写入该变量。unsigned int* count该参数是输出参数，结果集中的数据长度会写入该变量。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。

#### OH_UdmfRecord_GetPlainText()

```ets
int OH_UdmfRecord_GetPlainText(OH_UdmfRecord* pThis, OH_UdsPlainText* plainText)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsPlainText](OH_UdsPlainText.md)* plainText该参数是输出参数，表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。

#### OH_UdmfRecord_GetHyperlink()

```ets
int OH_UdmfRecord_GetHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)数据。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsHyperlink](OH_UdsHyperlink.md)* hyperlink该参数是输出参数，表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。

#### OH_UdmfRecord_GetHtml()

```ets
int OH_UdmfRecord_GetHtml(OH_UdmfRecord* pThis, OH_UdsHtml* html)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsHtml](OH_UdsHtml.md)* html该参数是输出参数，表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。

#### OH_UdmfRecord_GetAppItem()

```ets
int OH_UdmfRecord_GetAppItem(OH_UdmfRecord* pThis, OH_UdsAppItem* appItem)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)数据。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsAppItem](OH_UdsAppItem.md)* appItem该参数是输出参数，表示指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。

#### OH_UdmfRecord_SetProvider()

```ets
int OH_UdmfRecord_SetProvider(OH_UdmfRecord* pThis, const char* const* types, unsigned int count, OH_UdmfRecordProvider* provider)
```

**描述**

将指定类型的统一数据提供者[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)设置至统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。const char* const* types表示一组指定的要提供的数据类型。unsigned int count表示指定的数据类型的数量。[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)* provider表示指向统一数据提供者对象[OH_UdmfRecordProvider](OH_UdmfRecordProvider.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_GetFileUri()

```ets
int OH_UdmfRecord_GetFileUri(OH_UdmfRecord* pThis, OH_UdsFileUri* fileUri)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)数据。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsFileUri](OH_UdsFileUri.md)* fileUri该参数是输出参数，表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_GetPixelMap()

```ets
int OH_UdmfRecord_GetPixelMap(OH_UdmfRecord* pThis, OH_UdsPixelMap* pixelMap)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)数据。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsPixelMap](OH_UdsPixelMap.md)* pixelMap该参数是输出参数，表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_GetArrayBuffer()

```ets
int OH_UdmfRecord_GetArrayBuffer(OH_UdmfRecord* record, const char* type, OH_UdsArrayBuffer* buffer)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)数据。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* record表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。const char* type表示要获取的ArrayBuffer类型数据的数据类型标识。[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)* buffer该参数是输出参数，表示指向ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfRecord_GetContentForm()

```ets
int OH_UdmfRecord_GetContentForm(OH_UdmfRecord* pThis, OH_UdsContentForm* contentForm)
```

**描述**

从统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)中获取内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)数据。

**起始版本：** 14

**参数：**

参数项描述[OH_UdmfRecord](OH_UdmfRecord.md)* pThis表示指向统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。[OH_UdsContentForm](OH_UdsContentForm.md)* contentForm该参数是输出参数，表示指向内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfData_GetPrimaryPlainText()

```ets
int OH_UdmfData_GetPrimaryPlainText(OH_UdmfData* data, OH_UdsPlainText* plainText)
```

**描述**

从统一数据对象[OH_UdmfData](OH_UdmfData.md)中获取第一个纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)数据。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* data表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。[OH_UdsPlainText](OH_UdsPlainText.md)* plainText该参数是输出参数，表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfData_GetPrimaryHtml()

```ets
int OH_UdmfData_GetPrimaryHtml(OH_UdmfData* data, OH_UdsHtml* html)
```

**描述**

从统一数据对象[OH_UdmfData](OH_UdmfData.md)中获取第一个超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)数据。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* data表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。[OH_UdsHtml](OH_UdsHtml.md)* html该参数是输出参数，表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfData_GetRecordCount()

```ets
int OH_UdmfData_GetRecordCount(OH_UdmfData* data)
```

**描述**

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中包含的所有记录数量。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* data表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。

**返回：**

类型说明int返回统一数据对象[OH_UdmfRecord](OH_UdmfRecord.md)的数量。

#### OH_UdmfData_GetRecord()

```ets
OH_UdmfRecord* OH_UdmfData_GetRecord(OH_UdmfData* data, unsigned int index)
```

**描述**

获取统一数据对象[OH_UdmfData](OH_UdmfData.md)中指定位置的数据记录。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* data表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。unsigned int index表示要获取的统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)在统一数据对象[OH_UdmfData](OH_UdmfData.md)中的下标。

**返回：**

类型说明[OH_UdmfRecord](OH_UdmfRecord.md)*执行成功时返回统一数据记录[OH_UdmfRecord](OH_UdmfRecord.md)实例对象的指针，否则返回nullptr。

#### OH_UdmfData_IsLocal()

```ets
bool OH_UdmfData_IsLocal(OH_UdmfData* data)
```

**描述**

检查统一数据对象[OH_UdmfData](OH_UdmfData.md)是否是来自本端设备的数据。

**起始版本：** 13

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* data表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。

**返回：**

类型说明bool返回数据是否是来自本端设备。返回true表示来自本端设备，返回false表示来自远端设备。

#### OH_UdmfProperty_Create()

```ets
OH_UdmfProperty* OH_UdmfProperty_Create(OH_UdmfData* unifiedData)
```

**描述**

创建统一数据对象中数据记录属性[OH_UdmfProperty](OH_UdmfProperty.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdmfProperty_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfproperty_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)* unifiedData表示指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。

**返回：**

类型说明[OH_UdmfProperty](OH_UdmfProperty.md)*执行成功则返回一个指向属性[OH_UdmfProperty](OH_UdmfProperty.md)实例对象的指针，否则返回nullptr。

#### OH_UdmfProperty_Destroy()

```ets
void OH_UdmfProperty_Destroy(OH_UdmfProperty* pThis)
```

**描述**

销毁数据属性[OH_UdmfProperty](OH_UdmfProperty.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。

#### OH_UdmfProperty_GetTag()

```ets
const char* OH_UdmfProperty_GetTag(OH_UdmfProperty* pThis)
```

**描述**

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取用户自定义标签值。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。

**返回：**

类型说明const char*执行成功时返回自定义标签值的字符串指针，否则返回nullptr。

#### OH_UdmfProperty_GetTimestamp()

```ets
int64_t OH_UdmfProperty_GetTimestamp(OH_UdmfProperty* pThis)
```

**描述**

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取时间戳。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。

**返回：**

类型说明int64_t返回时间戳值。

#### OH_UdmfProperty_GetShareOption()

```ets
Udmf_ShareOption OH_UdmfProperty_GetShareOption(OH_UdmfProperty* pThis)
```

**描述**

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取设备内适用范围属性。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。

**返回：**

类型说明[Udmf_ShareOption](#ZH-CN_TOPIC_0000002497444728__udmf_shareoption)返回设备内适用范围属性[Udmf_ShareOption](zh-cn_topic_0000002497444728.html#ZH-CN_TOPIC_0000002497444728__udmf_shareoption)值。

#### OH_UdmfProperty_GetExtrasIntParam()

```ets
int OH_UdmfProperty_GetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int defaultValue)
```

**描述**

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取自定义的附加整型参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。const char* key表示键值对的键。int defaultValue用于用户自行设置获取值失败时的默认值。

**返回：**

类型说明int执行成功返回指定的键关联的整型值，否则返回用户设置的默认值defaultValue。

#### OH_UdmfProperty_GetExtrasStringParam()

```ets
const char* OH_UdmfProperty_GetExtrasStringParam(OH_UdmfProperty* pThis, const char* key)
```

**描述**

从数据属性[OH_UdmfProperty](OH_UdmfProperty.md)中获取自定义的附加字符串参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。const char* key表示键值对的键。

**返回：**

类型说明const char*执行成功时返回指定的键关联的字符串值的指针，否则返回nullptr。

#### OH_UdmfProperty_SetTag()

```ets
int OH_UdmfProperty_SetTag(OH_UdmfProperty* pThis, const char* tag)
```

**描述**

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的自定义标签值。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。const char* tag表示自定义标签值。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfProperty_SetShareOption()

```ets
int OH_UdmfProperty_SetShareOption(OH_UdmfProperty* pThis, Udmf_ShareOption option)
```

**描述**

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的设备内适用范围[Udmf_ShareOption](udmf.h.md#ZH-CN_TOPIC_0000002497444728__udmf_shareoption)参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfProperty](OH_UdmfProperty.md)实例的指针。[Udmf_ShareOption](#ZH-CN_TOPIC_0000002497444728__udmf_shareoption) option表示设备内适用范围[Udmf_ShareOption](zh-cn_topic_0000002497444728.html#ZH-CN_TOPIC_0000002497444728__udmf_shareoption)参数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfProperty_SetExtrasIntParam()

```ets
int OH_UdmfProperty_SetExtrasIntParam(OH_UdmfProperty* pThis, const char* key, int param)
```

**描述**

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的附加整型参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。const char* key表示键值对的键。int param表示键值对的值。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfProperty_SetExtrasStringParam()

```ets
int OH_UdmfProperty_SetExtrasStringParam(OH_UdmfProperty* pThis, const char* key, const char* param)
```

**描述**

设置数据属性[OH_UdmfProperty](OH_UdmfProperty.md)的附加字符串参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdmfProperty](OH_UdmfProperty.md)* pThis表示指向数据属性[OH_UdmfRecord](OH_UdmfRecord.md)实例的指针。const char* key表示键值对的键。const char* param表示键值对的值。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfOptions_Create()

```ets
OH_UdmfOptions* OH_UdmfOptions_Create()
```

**描述**

创建指向[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

**起始版本：** 20

**返回：**

类型说明[OH_UdmfOptions](OH_UdmfOptions.md)*执行成功则返回一个指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针，否则返回nullptr。

#### OH_UdmfOptions_Destroy()

```ets
void OH_UdmfOptions_Destroy(OH_UdmfOptions* pThis)
```

**描述**

销毁指向[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

#### OH_UdmfOptions_GetKey()

```ets
const char* OH_UdmfOptions_GetKey(OH_UdmfOptions* pThis)
```

**描述**

从数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中获取数据的唯一标识符信息。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回符串指针，否则返回nullptr。

#### OH_UdmfOptions_SetKey()

```ets
int OH_UdmfOptions_SetKey(OH_UdmfOptions* pThis, const char* key)
```

**描述**

设置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中的数据的唯一标识符内容参数。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。const char* key数据的唯一标识符的新字符串值。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfOptions_GetIntention()

```ets
Udmf_Intention OH_UdmfOptions_GetIntention(OH_UdmfOptions* pThis)
```

**描述**

从数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中获取数据通路信息。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

**返回：**

类型说明[Udmf_Intention](#ZH-CN_TOPIC_0000002497444728__udmf_intention)返回[Udmf_Intention](zh-cn_topic_0000002497444728.html#ZH-CN_TOPIC_0000002497444728__udmf_intention)的值。

#### OH_UdmfOptions_SetIntention()

```ets
int OH_UdmfOptions_SetIntention(OH_UdmfOptions* pThis, Udmf_Intention intention)
```

**描述**

设置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例中的数据通路内容参数。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。[Udmf_Intention](#ZH-CN_TOPIC_0000002497444728__udmf_intention) intention数据通路类型参数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdmfOptions_Reset()

```ets
int OH_UdmfOptions_Reset(OH_UdmfOptions* pThis)
```

**描述**

重置数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例为空。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* pThis指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_Udmf_GetUnifiedData()

```ets
int OH_Udmf_GetUnifiedData(const char* key, Udmf_Intention intention, OH_UdmfData* unifiedData)
```

**描述**

从统一数据管理框架数据库中获取统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

**起始版本：** 12

**参数：**

参数项描述const char* key表示数据库存储的唯一标识符。[Udmf_Intention](#ZH-CN_TOPIC_0000002497444728__udmf_intention) intention表示数据通路类型[Udmf_Intention](zh-cn_topic_0000002497444728.html#ZH-CN_TOPIC_0000002497444728__udmf_intention)。[OH_UdmfData](OH_UdmfData.md)* unifiedData该参数是输出参数，获取到的统一数据对象[OH_UdmfData](OH_UdmfData.md)会写入该变量。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。

#### OH_Udmf_GetUnifiedDataByOptions()

```ets
int OH_Udmf_GetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize)
```

**描述**

通过数据通路类型从统一数据管理框架数据库中获取统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* options指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。[OH_UdmfData](OH_UdmfData.md)** dataArray

该参数是输出参数，表示统一数据对象[OH_UdmfData](OH_UdmfData.md)列表。

需要使用[OH_UDMF_GetDataElementAt](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmf_getdataelementat)函数通过下标访问每个元素。

此指针需要使用[OH_Udmf_DestroyDataArray](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmf_destroydataarray)函数释放。

unsigned int* dataSize该参数是输出参数，表示获取到的统一数据对象个数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。

#### OH_Udmf_SetUnifiedData()

```ets
int OH_Udmf_SetUnifiedData(Udmf_Intention intention, OH_UdmfData* unifiedData, char* key, unsigned int keyLen)
```

**描述**

从统一数据管理框架数据库中写入统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

**起始版本：** 12

**参数：**

参数项描述[Udmf_Intention](#ZH-CN_TOPIC_0000002497444728__udmf_intention) intention表示数据通路类型[Udmf_Intention](zh-cn_topic_0000002497444728.html#ZH-CN_TOPIC_0000002497444728__udmf_intention)。[OH_UdmfData](OH_UdmfData.md)* unifiedData表示统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。char* key表示成功将数据设置到数据库后对应数据的唯一标识符。unsigned int keyLen表示唯一标识符参数的空间大小，内存大小不小于512字节。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。

#### OH_Udmf_SetUnifiedDataByOptions()

```ets
int OH_Udmf_SetUnifiedDataByOptions(OH_UdmfOptions* options, OH_UdmfData *unifiedData, char *key, unsigned int keyLen)
```

**描述**

从统一数据管理框架数据库中写入统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* options指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。[OH_UdmfData](OH_UdmfData.md) *unifiedData指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。char *key成功将数据设置到数据库后对应数据的唯一标识符，内存大小不小于[UDMF_KEY_BUFFER_LEN](#ZH-CN_TOPIC_0000002497444728__udmf_key_buffer_len)。unsigned int keyLen唯一标识符参数的空间大小。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。

#### OH_Udmf_UpdateUnifiedData()

```ets
int OH_Udmf_UpdateUnifiedData(OH_UdmfOptions* options, OH_UdmfData* unifiedData)
```

**描述**

对统一数据管理框架数据库中的统一数据对象[OH_UdmfData](OH_UdmfData.md)数据进行数据更改。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* options指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。[OH_UdmfData](OH_UdmfData.md)* unifiedData指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。

#### OH_Udmf_DeleteUnifiedData()

```ets
int OH_Udmf_DeleteUnifiedData(OH_UdmfOptions* options, OH_UdmfData** dataArray, unsigned int* dataSize)
```

**描述**

删除统一数据管理框架数据库中的统一数据对象[OH_UdmfData](OH_UdmfData.md)数据。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfOptions](OH_UdmfOptions.md)* options指向数据操作选项[OH_UdmfOptions](OH_UdmfOptions.md)实例的指针。[OH_UdmfData](OH_UdmfData.md)** dataArray该参数是输出参数，统一数据对象[OH_UdmfData](OH_UdmfData.md)列表，需要使用[OH_UDMF_GetDataElementAt](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmf_getdataelementat)函数通过下标访问每个元素。此指针需要使用[OH_Udmf_DestroyDataArray](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmf_destroydataarray)函数释放。unsigned int* dataSize该参数是输出参数，表示获取到的统一数据对象个数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。

#### OH_Udmf_DestroyDataArray()

```ets
void OH_Udmf_DestroyDataArray(OH_UdmfData** dataArray, unsigned int dataSize)
```

**描述**

销毁数据数组内存。

**起始版本：** 20

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)** dataArray指向统一数据对象[OH_UdmfData](OH_UdmfData.md)的指针列表。unsigned int dataSize列表中的数据大小。

**参考：**

OH_UdmfData

#### OH_UdmfProgressInfo_GetProgress()

```ets
int OH_UdmfProgressInfo_GetProgress(OH_Udmf_ProgressInfo* progressInfo)
```

**描述**

从进度信息[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)中获取进度百分比数据。

**起始版本：** 15

**参数：**

参数项描述[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)* progressInfo表示进度信息[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)。

**返回：**

类型说明int返回进度百分比数据。

#### OH_UdmfProgressInfo_GetStatus()

```ets
int OH_UdmfProgressInfo_GetStatus(OH_Udmf_ProgressInfo* progressInfo)
```

**描述**

从进度信息[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)中获取状态信息。

**起始版本：** 15

**参数：**

参数项描述[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)* progressInfo表示进度信息[OH_Udmf_ProgressInfo](OH_Udmf_ProgressInfo.md)。

**返回：**

类型说明int返回状态信息。

#### OH_UdmfGetDataParams_Create()

```ets
OH_UdmfGetDataParams* OH_UdmfGetDataParams_Create()
```

**描述**

创建异步获取UDMF数据的请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)指针及实例对象。

当不再需要使用指针时，请使用[OH_UdmfGetDataParams_Destroy](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfgetdataparams_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 15

**返回：**

类型说明[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)*执行成功则返回一个指向属性[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)实例对象的指针，否则返回nullptr。

#### OH_UdmfGetDataParams_Destroy()

```ets
void OH_UdmfGetDataParams_Destroy(OH_UdmfGetDataParams* pThis)
```

**描述**

销毁异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)指针指向的实例对象。

**起始版本：** 15

**参数：**

参数项描述[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)* pThis表示指向异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)实例的指针。

#### OH_UdmfGetDataParams_SetDestUri()

```ets
void OH_UdmfGetDataParams_SetDestUri(OH_UdmfGetDataParams* params, const char* destUri)
```

**描述**

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的目标路径。

若设置了目标路径，会将文件类型的数据进行拷贝到指定路径。回调中获取到的文件类型数据会被替换为目标路径的URI。

若不设置目标路径，则不会执行拷贝文件操作。回调中获取到的文件类型数据为源端路径URI。

若应用涉及复杂文件处理策略，或需要将文件拷贝在多个路径下时，建议不设置此参数，由应用自行完成文件拷贝相关处理。

**起始版本：** 15

**参数：**

参数项描述[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)* params表示指向异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)实例的指针。const char* destUri表示目标路径地址。

#### OH_UdmfGetDataParams_SetFileConflictOptions()

```ets
void OH_UdmfGetDataParams_SetFileConflictOptions(OH_UdmfGetDataParams* params, const Udmf_FileConflictOptions options)
```

**描述**

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的文件冲突选项。

**起始版本：** 15

**参数：**

参数项描述[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)* params表示指向异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)实例的指针。const [Udmf_FileConflictOptions](#ZH-CN_TOPIC_0000002497444728__udmf_fileconflictoptions) options表示文件拷贝冲突时的选项。

#### OH_UdmfGetDataParams_SetProgressIndicator()

```ets
void OH_UdmfGetDataParams_SetProgressIndicator(OH_UdmfGetDataParams* params, const Udmf_ProgressIndicator progressIndicator)
```

**描述**

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的进度条指示选项。

**起始版本：** 15

**参数：**

参数项描述[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)* params表示指向异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)实例的指针。const [Udmf_ProgressIndicator](#ZH-CN_TOPIC_0000002497444728__udmf_progressindicator) progressIndicator表示是否使用默认进度条选项。

#### OH_UdmfGetDataParams_SetDataProgressListener()

```ets
void OH_UdmfGetDataParams_SetDataProgressListener(OH_UdmfGetDataParams* params, const OH_Udmf_DataProgressListener dataProgressListener)
```

**描述**

设置异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)中的监听回调函数。

**起始版本：** 15

**参数：**

参数项描述[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)* params表示指向异步请求参数[OH_UdmfGetDataParams](OH_UdmfGetDataParams.md)实例的指针。const [OH_Udmf_DataProgressListener](#ZH-CN_TOPIC_0000002497444728__oh_udmf_dataprogresslistener) dataProgressListener用户自定义的监听回调函数，可用于获取进度信息和数据。

#### OH_UDMF_GetDataElementAt()

```ets
OH_UdmfData* OH_UDMF_GetDataElementAt(OH_UdmfData** dataArray, unsigned int index)
```

**描述**

从统一数据对象[OH_UdmfData](OH_UdmfData.md)数组中获取指定下标的统一数据对象数据。

**起始版本：** 22

**参数：**

参数项描述[OH_UdmfData](OH_UdmfData.md)** dataArray

指向统一数据对象[OH_UdmfData](OH_UdmfData.md)的指针数组。

只接受从[OH_Udmf_GetUnifiedDataByOptions](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmf_getunifieddatabyoptions)和[OH_Udmf_DeleteUnifiedData](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmf_deleteunifieddata)接口中获得的指针数组。

unsigned int index表示要获取到的统一数据对象的下标。请确保该值不超出数组范围，否则会出现数组越界。

**返回：**

类型说明[OH_UdmfData*](OH_UdmfData.md)执行成功则返回一个指向统一数据对象[OH_UdmfData](OH_UdmfData.md)实例对象的指针，如果输入数组为空，则返回空。