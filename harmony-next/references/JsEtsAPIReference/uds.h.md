# uds.h

#### 概述

提供标准化数据结构相关接口函数、结构体定义。

**引用文件：** <database/udmf/uds.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：**[UDMF](UDMF.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_UdsPlainText](OH_UdsPlainText.md)OH_UdsPlainText描述纯文本类型数据的统一数据结构。[OH_UdsHyperlink](OH_UdsHyperlink.md)OH_UdsHyperlink描述超链接类型的统一数据结构。[OH_UdsHtml](OH_UdsHtml.md)OH_UdsHtml描述超文本标记语言类型的统一数据结构。[OH_UdsAppItem](OH_UdsAppItem.md)OH_UdsAppItem描述桌面图标类型的统一数据结构。[OH_UdsFileUri](OH_UdsFileUri.md)OH_UdsFileUri描述文件Uri类型的统一数据结构。[OH_UdsPixelMap](OH_UdsPixelMap.md)OH_UdsPixelMap描述像素图片类型的统一数据结构。[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)OH_UdsArrayBuffer描述ArrayBuffer类型的统一数据结构。[OH_UdsContentForm](OH_UdsContentForm.md)OH_UdsContentForm描述内容卡片类型的统一数据结构。[OH_UdsDetails](OH_UdsDetails.md)OH_UdsDetails描述字典类型的统一数据结构。

#### 函数

名称描述[OH_UdsPlainText* OH_UdsPlainText_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_create)创建纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsPlainText_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdsPlainText_Destroy(OH_UdsPlainText* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_destroy)销毁纯文本类型数据[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)指针指向的实例对象。[const char* OH_UdsPlainText_GetType(OH_UdsPlainText* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_gettype)从纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)中获取类型ID。[const char* OH_UdsPlainText_GetContent(OH_UdsPlainText* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_getcontent)从纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)中获取纯文本内容信息。[const char* OH_UdsPlainText_GetAbstract(OH_UdsPlainText* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_getabstract)从纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)中获取纯文本摘要信息。[int OH_UdsPlainText_SetContent(OH_UdsPlainText* pThis, const char* content)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_setcontent)设置纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)中的纯文本内容参数。[int OH_UdsPlainText_SetAbstract(OH_UdsPlainText* pThis, const char* abstract)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_setabstract)设置纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)中的纯文本摘要参数。[OH_UdsHyperlink* OH_UdsHyperlink_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_create)创建超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsHyperlink_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdsHyperlink_Destroy(OH_UdsHyperlink* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_destroy)销毁超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)指针指向的实例对象。[const char* OH_UdsHyperlink_GetType(OH_UdsHyperlink* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_gettype)从超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)中获取类型ID。[const char* OH_UdsHyperlink_GetUrl(OH_UdsHyperlink* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_geturl)从超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)中获取URL参数。[const char* OH_UdsHyperlink_GetDescription(OH_UdsHyperlink* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_getdescription)从超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)中获取描述参数。[int OH_UdsHyperlink_SetUrl(OH_UdsHyperlink* pThis, const char* url)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_seturl)设置超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)实例中URL参数。[int OH_UdsHyperlink_SetDescription(OH_UdsHyperlink* pThis, const char* description)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_setdescription)设置超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)实例中描述参数。[OH_UdsHtml* OH_UdsHtml_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_create)创建超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsHtml_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-uds-h_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdsHtml_Destroy(OH_UdsHtml* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_destroy)销毁超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)指针指向的实例对象。[const char* OH_UdsHtml_GetType(OH_UdsHtml* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_gettype)获取超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)对象中类型ID。[const char* OH_UdsHtml_GetContent(OH_UdsHtml* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_getcontent)获取超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)对象中HTML格式内容参数。[const char* OH_UdsHtml_GetPlainContent(OH_UdsHtml* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_getplaincontent)获取超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)对象中的纯文本内容参数。[int OH_UdsHtml_SetContent(OH_UdsHtml* pThis, const char* content)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_setcontent)设置超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)中的HTML格式内容参数。[int OH_UdsHtml_SetPlainContent(OH_UdsHtml* pThis, const char* plainContent)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_setplaincontent)设置超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)中的纯文本内容参数。[OH_UdsAppItem* OH_UdsAppItem_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_create)创建桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsAppItem_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdsAppItem_Destroy(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_destroy)销毁桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)指针指向的实例对象。[const char* OH_UdsAppItem_GetType(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_gettype)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例获取类型ID。[const char* OH_UdsAppItem_GetId(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_getid)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例中获取应用ID。[const char* OH_UdsAppItem_GetName(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_getname)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例中获取应用名称。[const char* OH_UdsAppItem_GetIconId(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_geticonid)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例中获取图片ID。[const char* OH_UdsAppItem_GetLabelId(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_getlabelid)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例中获取标签ID。[const char* OH_UdsAppItem_GetBundleName(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_getbundlename)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例中获取bundle名称。[const char* OH_UdsAppItem_GetAbilityName(OH_UdsAppItem* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_getabilityname)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例中ability名称。[int OH_UdsAppItem_SetId(OH_UdsAppItem* pThis, const char* appId)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_setid)设置桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)对象的应用ID。[int OH_UdsAppItem_SetName(OH_UdsAppItem* pThis, const char* appName)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_setname)设置桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)对象的应用名称。[int OH_UdsAppItem_SetIconId(OH_UdsAppItem* pThis, const char* appIconId)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_seticonid)设置桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)对象的图片ID。[int OH_UdsAppItem_SetLabelId(OH_UdsAppItem* pThis, const char* appLabelId)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_setlabelid)设置桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)对象的标签ID。[int OH_UdsAppItem_SetBundleName(OH_UdsAppItem* pThis, const char* bundleName)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_setbundlename)设置桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)对象的bundle名称。[int OH_UdsAppItem_SetAbilityName(OH_UdsAppItem* pThis, const char* abilityName)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_setabilityname)设置桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)对象的ability名称。[OH_UdsFileUri* OH_UdsFileUri_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_create)创建文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH_UdsFileUri_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdsFileUri_Destroy(OH_UdsFileUri* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_destroy)销毁文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)的实例对象。[const char* OH_UdsFileUri_GetType(OH_UdsFileUri* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_gettype)从文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)实例中获取类型ID。[const char* OH_UdsFileUri_GetFileUri(OH_UdsFileUri* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_getfileuri)从文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)实例中获取文件Uri。[const char* OH_UdsFileUri_GetFileType(OH_UdsFileUri* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_getfiletype)从文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)实例中获取文件类型。[int OH_UdsFileUri_SetFileUri(OH_UdsFileUri* pThis, const char* fileUri)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_setfileuri)设置文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)对象的Uri信息。[int OH_UdsFileUri_SetFileType(OH_UdsFileUri* pThis, const char* fileType)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_setfiletype)设置文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)对象的文件类型。[OH_UdsPixelMap* OH_UdsPixelMap_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_create)创建像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH_UdsPixelMap_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_destroy)销毁实例对象，否则会导致内存泄漏。[void OH_UdsPixelMap_Destroy(OH_UdsPixelMap* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_destroy)销毁像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)的实例对象。[const char* OH_UdsPixelMap_GetType(OH_UdsPixelMap* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_gettype)从像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)实例中获取类型ID。[void OH_UdsPixelMap_GetPixelMap(OH_UdsPixelMap* pThis, OH_PixelmapNative* pixelmapNative)](#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_getpixelmap)从像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)实例中获取像素图片[OH_PixelmapNative](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel)实例的指针。[int OH_UdsPixelMap_SetPixelMap(OH_UdsPixelMap* pThis, OH_PixelmapNative* pixelmapNative)](#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_setpixelmap)设置像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)对象的像素图片内容。[OH_UdsArrayBuffer* OH_UdsArrayBuffer_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udsarraybuffer_create)创建ArrayBuffer类型[OH_UdsArrayBuffer](zh-cn_topic_0000002529284723.html)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH_UdsArrayBuffer_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsarraybuffer_destroy)销毁实例对象，否则会导致内存泄漏。[int OH_UdsArrayBuffer_Destroy(OH_UdsArrayBuffer* buffer)](#ZH-CN_TOPIC_0000002497604708__oh_udsarraybuffer_destroy)销毁ArrayBuffer类型[OH_UdsArrayBuffer](zh-cn_topic_0000002529284723.html)的实例对象。[int OH_UdsArrayBuffer_SetData(OH_UdsArrayBuffer* buffer, unsigned char* data, unsigned int len)](#ZH-CN_TOPIC_0000002497604708__oh_udsarraybuffer_setdata)设置ArrayBuffer类型[OH_UdsArrayBuffer](zh-cn_topic_0000002529284723.html)对象的数据内容。[int OH_UdsArrayBuffer_GetData(OH_UdsArrayBuffer* buffer, unsigned char** data, unsigned int* len)](#ZH-CN_TOPIC_0000002497604708__oh_udsarraybuffer_getdata)从ArrayBuffer类型[OH_UdsArrayBuffer](zh-cn_topic_0000002529284723.html)实例中获取用户自定义的ArrayBuffer数据内容。[OH_UdsContentForm* OH_UdsContentForm_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_create)创建内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)指针及实例对象。[void OH_UdsContentForm_Destroy(OH_UdsContentForm* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_destroy)销毁内容卡片类型数据[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)指针指向的实例对象。[const char* OH_UdsContentForm_GetType(OH_UdsContentForm* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_gettype)从内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中获取类型ID。[int OH_UdsContentForm_GetThumbData(OH_UdsContentForm* pThis, unsigned char** thumbData, unsigned int* len)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_getthumbdata)从内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中获取图片数据。[const char* OH_UdsContentForm_GetDescription(OH_UdsContentForm* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_getdescription)从内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中获取描述信息。[const char* OH_UdsContentForm_GetTitle(OH_UdsContentForm* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_gettitle)从内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中获取标题信息。[int OH_UdsContentForm_GetAppIcon(OH_UdsContentForm* pThis, unsigned char** appIcon, unsigned int* len)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_getappicon)从内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中获取应用图标数据。[const char* OH_UdsContentForm_GetAppName(OH_UdsContentForm* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_getappname)从内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中获取应用名称信息。[const char* OH_UdsContentForm_GetLinkUri(OH_UdsContentForm* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_getlinkuri)从内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中获取超链接信息。[int OH_UdsContentForm_SetThumbData(OH_UdsContentForm* pThis, const unsigned char* thumbData, unsigned int len)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_setthumbdata)设置内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中的图片数据。[int OH_UdsContentForm_SetDescription(OH_UdsContentForm* pThis, const char* description)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_setdescription)设置内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中的描述信息。[int OH_UdsContentForm_SetTitle(OH_UdsContentForm* pThis, const char* title)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_settitle)设置内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中的标题信息。[int OH_UdsContentForm_SetAppIcon(OH_UdsContentForm* pThis, const unsigned char* appIcon, unsigned int len)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_setappicon)设置内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中的应用图标数据。[int OH_UdsContentForm_SetAppName(OH_UdsContentForm* pThis, const char* appName)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_setappname)设置内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中的应用名称数据。[int OH_UdsContentForm_SetLinkUri(OH_UdsContentForm* pThis, const char* linkUri)](#ZH-CN_TOPIC_0000002497604708__oh_udscontentform_setlinkuri)设置内容卡片类型[OH_UdsContentForm](zh-cn_topic_0000002529444697.html)中的超链接数据。[int OH_UdsPlainText_GetDetails(OH_UdsPlainText* pThis, OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_getdetails)从纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。[int OH_UdsPlainText_SetDetails(OH_UdsPlainText* pThis, const OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_setdetails)设置纯文本类型[OH_UdsPlainText](zh-cn_topic_0000002497604728.html)中的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。[int OH_UdsHyperlink_GetDetails(OH_UdsHyperlink* pThis, OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_getdetails)从超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。[int OH_UdsHyperlink_SetDetails(OH_UdsHyperlink* pThis, const OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_setdetails)设置超链接类型[OH_UdsHyperlink](zh-cn_topic_0000002497444750.html)实例中的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。[int OH_UdsHtml_GetDetails(OH_UdsHtml* pThis, OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_getdetails)从超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)对象中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。[int OH_UdsHtml_SetDetails(OH_UdsHtml* pThis, const OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udshtml_setdetails)设置超文本标记语言类型[OH_UdsHtml](zh-cn_topic_0000002529284721.html)中的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。[int OH_UdsAppItem_GetDetails(OH_UdsAppItem* pThis, OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_getdetails)从桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)实例中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。[int OH_UdsAppItem_SetDetails(OH_UdsAppItem* pThis, const OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_setdetails)设置桌面图标类型[OH_UdsAppItem](zh-cn_topic_0000002529444695.html)对象的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。[int OH_UdsFileUri_GetDetails(OH_UdsFileUri* pThis, OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_getdetails)从文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)实例中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。[int OH_UdsFileUri_SetDetails(OH_UdsFileUri* pThis, const OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_setdetails)设置文件Uri类型[OH_UdsFileUri](zh-cn_topic_0000002497604730.html)对象的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。[int OH_UdsPixelMap_GetDetails(OH_UdsPixelMap* pThis, OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_getdetails)从像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)实例中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。[int OH_UdsPixelMap_SetDetails(OH_UdsPixelMap* pThis, const OH_UdsDetails* details)](#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_setdetails)设置像素图片类型[OH_UdsPixelMap](zh-cn_topic_0000002497444752.html)对象的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。[OH_UdsDetails* OH_UdsDetails_Create()](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_create)

创建字典类型[OH_UdsDetails](OH_UdsDetails.md)指针及实例对象。

当不再需要使用指针时，请使用[OH_UdsDetails_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_destroy)销毁实例对象，否则会导致内存泄漏。

[void OH_UdsDetails_Destroy(OH_UdsDetails* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_destroy)销毁字典类型[OH_UdsDetails](zh-cn_topic_0000002497604732.html)指针指向的实例对象。[bool OH_UdsDetails_HasKey(const OH_UdsDetails* pThis, const char* key)](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_haskey)检查字典类型[OH_UdsDetails](zh-cn_topic_0000002497604732.html)中是否存在指定键。[int OH_UdsDetails_Remove(OH_UdsDetails* pThis, const char* key)](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_remove)删除字典类型[OH_UdsDetails](zh-cn_topic_0000002497604732.html)中指定键值对。[int OH_UdsDetails_Clear(OH_UdsDetails* pThis)](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_clear)清除字典类型[OH_UdsDetails](zh-cn_topic_0000002497604732.html)中所有数据。[int OH_UdsDetails_SetValue(OH_UdsDetails* pThis, const char* key, const char* value)](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_setvalue)向字典类型[OH_UdsDetails](zh-cn_topic_0000002497604732.html)中添加键值对数据。[const char* OH_UdsDetails_GetValue(const OH_UdsDetails* pThis, const char* key)](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_getvalue)获取字典类型[OH_UdsDetails](zh-cn_topic_0000002497604732.html)中指定的键对应的值。[char** OH_UdsDetails_GetAllKeys(OH_UdsDetails* pThis, unsigned int* count)](#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_getallkeys)获取字典类型[OH_UdsDetails](zh-cn_topic_0000002497604732.html)中所有键的结果集。

#### 函数说明

#### OH_UdsPlainText_Create()

```ets
OH_UdsPlainText* OH_UdsPlainText_Create()
```

**描述**

创建纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsPlainText_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsplaintext_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

类型说明[OH_UdsPlainText](OH_UdsPlainText.md)*执行成功则返回一个指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例对象的指针，否则返回nullptr。

#### OH_UdsPlainText_Destroy()

```ets
void OH_UdsPlainText_Destroy(OH_UdsPlainText* pThis)
```

**描述**

销毁纯文本类型数据[OH_UdsPlainText](OH_UdsPlainText.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。

#### OH_UdsPlainText_GetType()

```ets
const char* OH_UdsPlainText_GetType(OH_UdsPlainText* pThis)
```

**描述**

从纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)中获取类型ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回类型ID的字符串指针，否则返回nullptr。

#### OH_UdsPlainText_GetContent()

```ets
const char* OH_UdsPlainText_GetContent(OH_UdsPlainText* pThis)
```

**描述**

从纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)中获取纯文本内容信息。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回纯文本内容信息的字符串指针，否则返回nullptr。

#### OH_UdsPlainText_GetAbstract()

```ets
const char* OH_UdsPlainText_GetAbstract(OH_UdsPlainText* pThis)
```

**描述**

从纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)中获取纯文本摘要信息。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回纯文本摘要信息的字符串指针，否则返回nullptr。

OH_UdsPlainText

#### OH_UdsPlainText_SetContent()

```ets
int OH_UdsPlainText_SetContent(OH_UdsPlainText* pThis, const char* content)
```

**描述**

设置纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)中的纯文本内容参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。const char* content表示纯文本内容参数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsPlainText_SetAbstract()

```ets
int OH_UdsPlainText_SetAbstract(OH_UdsPlainText* pThis, const char* abstract)
```

**描述**

设置纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)中的纯文本摘要参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。const char* abstract表示纯文本摘要参数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHyperlink_Create()

```ets
OH_UdsHyperlink* OH_UdsHyperlink_Create()
```

**描述**

创建超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsHyperlink_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udshyperlink_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

类型说明OH_UdsHyperlink*执行成功则返回一个指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例对象的指针，否则返回nullptr。

#### OH_UdsHyperlink_Destroy()

```ets
void OH_UdsHyperlink_Destroy(OH_UdsHyperlink* pThis)
```

**描述**

销毁超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。

#### OH_UdsHyperlink_GetType()

```ets
const char* OH_UdsHyperlink_GetType(OH_UdsHyperlink* pThis)
```

**描述**

从超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)中获取类型ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回类型ID的字符串指针，否则返回nullptr。

#### OH_UdsHyperlink_GetUrl()

```ets
const char* OH_UdsHyperlink_GetUrl(OH_UdsHyperlink* pThis)
```

**描述**

从超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)中获取URL参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回URL参数的字符串指针，否则返回nullptr。

#### OH_UdsHyperlink_GetDescription()

```ets
const char* OH_UdsHyperlink_GetDescription(OH_UdsHyperlink* pThis)
```

**描述**

从超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)中获取描述参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回描述参数的字符串指针，否则返回nullptr。

#### OH_UdsHyperlink_SetUrl()

```ets
int OH_UdsHyperlink_SetUrl(OH_UdsHyperlink* pThis, const char* url)
```

**描述**

设置超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例中URL参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。const char* url表示URL参数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHyperlink_SetDescription()

```ets
int OH_UdsHyperlink_SetDescription(OH_UdsHyperlink* pThis, const char* description)
```

**描述**

设置超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例中描述参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。const char* description表示描述信息。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHtml_Create()

```ets
OH_UdsHtml* OH_UdsHtml_Create()
```

**描述**

创建超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsHtml_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-uds-h_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

类型说明[OH_UdsHtml](OH_UdsHtml.md)*执行成功则返回一个指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例对象的指针，否则返回nullptr。

#### OH_UdsHtml_Destroy()

```ets
void OH_UdsHtml_Destroy(OH_UdsHtml* pThis)
```

**描述**

销毁超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。

#### OH_UdsHtml_GetType()

```ets
const char* OH_UdsHtml_GetType(OH_UdsHtml* pThis)
```

**描述**

获取超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)对象中类型ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回类型ID的字符串指针，否则返回nullptr。

#### OH_UdsHtml_GetContent()

```ets
const char* OH_UdsHtml_GetContent(OH_UdsHtml* pThis)
```

**描述**

获取超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)对象中HTML格式内容参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回HTML格式内容的字符串指针，否则返回nullptr。

#### OH_UdsHtml_GetPlainContent()

```ets
const char* OH_UdsHtml_GetPlainContent(OH_UdsHtml* pThis)
```

**描述**

获取超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)对象中的纯文本内容参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回纯文本内容的字符串指针，否则返回nullptr。

#### OH_UdsHtml_SetContent()

```ets
int OH_UdsHtml_SetContent(OH_UdsHtml* pThis, const char* content)
```

**描述**

设置超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)中的HTML格式内容参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。const char* content表示HTML格式内容参数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHtml_SetPlainContent()

```ets
int OH_UdsHtml_SetPlainContent(OH_UdsHtml* pThis, const char* plainContent)
```

**描述**

设置超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)中的纯文本内容参数。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。const char* plainContent表示纯文本内容参数。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_Create()

```ets
OH_UdsAppItem* OH_UdsAppItem_Create()
```

**描述**

创建桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)指针及实例对象。当不再需要使用指针时，请使用[OH_UdsAppItem_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsappitem_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

类型说明[OH_UdsAppItem](OH_UdsAppItem.md)*执行成功则返回一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例对象的指针，否则返回nullptr。

#### OH_UdsAppItem_Destroy()

```ets
void OH_UdsAppItem_Destroy(OH_UdsAppItem* pThis)
```

**描述**

销毁桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

#### OH_UdsAppItem_GetType()

```ets
const char* OH_UdsAppItem_GetType(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例获取类型ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

**返回：**

类型说明const char*输入有效入参时返回类型ID的字符串指针，否则返回nullptr。

#### OH_UdsAppItem_GetId()

```ets
const char* OH_UdsAppItem_GetId(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例中获取应用ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

**返回：**

类型说明const char*输入有效入参时返回应用ID的字符串指针，否则返回nullptr。

#### OH_UdsAppItem_GetName()

```ets
const char* OH_UdsAppItem_GetName(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例中获取应用名称。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

**返回：**

类型说明const char*输入有效入参时返回应用名称的字符串指针，否则返回nullptr。

#### OH_UdsAppItem_GetIconId()

```ets
const char* OH_UdsAppItem_GetIconId(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例中获取图片ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

**返回：**

类型说明const char*输入有效入参时返回图片ID的字符串指针，否则返回nullptr。

#### OH_UdsAppItem_GetLabelId()

```ets
const char* OH_UdsAppItem_GetLabelId(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例中获取标签ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

**返回：**

类型说明const char*输入有效入参时返回标签ID的字符串指针，否则返回nullptr。

#### OH_UdsAppItem_GetBundleName()

```ets
const char* OH_UdsAppItem_GetBundleName(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例中获取bundle名称。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

**返回：**

类型说明const char*输入有效入参时返回bundle名称的字符串指针，否则返回nullptr。

#### OH_UdsAppItem_GetAbilityName()

```ets
const char* OH_UdsAppItem_GetAbilityName(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例中获取ability名称。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。

**返回：**

类型说明const char*输入有效入参时返回ability名称的字符串指针，否则返回nullptr。

#### OH_UdsAppItem_SetId()

```ets
int OH_UdsAppItem_SetId(OH_UdsAppItem* pThis, const char* appId)
```

**描述**

设置桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的应用ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。const char* appId表示应用ID。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_SetName()

```ets
int OH_UdsAppItem_SetName(OH_UdsAppItem* pThis, const char* appName)
```

**描述**

设置桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的应用名称。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。const char* appName表示应用名称。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_SetIconId()

```ets
int OH_UdsAppItem_SetIconId(OH_UdsAppItem* pThis, const char* appIconId)
```

**描述**

设置桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的图片ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。const char* appIconId表示图片ID。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_SetLabelId()

```ets
int OH_UdsAppItem_SetLabelId(OH_UdsAppItem* pThis, const char* appLabelId)
```

**描述**

设置桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的标签ID。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。const char* appLabelId表示标签ID。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_SetBundleName()

```ets
int OH_UdsAppItem_SetBundleName(OH_UdsAppItem* pThis, const char* bundleName)
```

**描述**

设置桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的bundle名称。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。const char* bundleName表示bundle名称。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_SetAbilityName()

```ets
int OH_UdsAppItem_SetAbilityName(OH_UdsAppItem* pThis, const char* abilityName)
```

**描述**

设置桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的ability名称。

**起始版本：** 12

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。const char* abilityName表示ability名称。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsFileUri_Create()

```ets
OH_UdsFileUri* OH_UdsFileUri_Create()
```

**描述**

创建文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH_UdsFileUri_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsfileuri_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 13

**返回：**

类型说明[OH_UdsFileUri](OH_UdsFileUri.md)*执行成功则返回一个指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例对象的指针，否则返回nullptr。

#### OH_UdsFileUri_Destroy()

```ets
void OH_UdsFileUri_Destroy(OH_UdsFileUri* pThis)
```

**描述**

销毁文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)的实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。

#### OH_UdsFileUri_GetType()

```ets
const char* OH_UdsFileUri_GetType(OH_UdsFileUri* pThis)
```

**描述**

从文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例中获取类型ID。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回类型ID的字符串指针，否则返回nullptr。

#### OH_UdsFileUri_GetFileUri()

```ets
const char* OH_UdsFileUri_GetFileUri(OH_UdsFileUri* pThis)
```

**描述**

从文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例中获取文件Uri。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回文件Uri的字符串指针，否则返回nullptr。

#### OH_UdsFileUri_GetFileType()

```ets
const char* OH_UdsFileUri_GetFileType(OH_UdsFileUri* pThis)
```

**描述**

从文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例中获取文件类型。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回文件类型的字符串指针，否则返回nullptr。

#### OH_UdsFileUri_SetFileUri()

```ets
int OH_UdsFileUri_SetFileUri(OH_UdsFileUri* pThis, const char* fileUri)
```

**描述**

设置文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)对象的Uri信息。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。const char* fileUri表示文件Uri。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsFileUri_SetFileType()

```ets
int OH_UdsFileUri_SetFileType(OH_UdsFileUri* pThis, const char* fileType)
```

**描述**

设置文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)对象的文件类型。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。const char* fileType表示文件类型。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsPixelMap_Create()

```ets
OH_UdsPixelMap* OH_UdsPixelMap_Create()
```

**描述**

创建像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH_UdsPixelMap_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udspixelmap_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 13

**返回：**

类型说明[OH_UdsPixelMap](OH_UdsPixelMap.md)*执行成功则返回一个指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例对象的指针，否则返回nullptr。

#### OH_UdsPixelMap_Destroy()

```ets
void OH_UdsPixelMap_Destroy(OH_UdsPixelMap* pThis)
```

**描述**

销毁像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)的实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsPixelMap](OH_UdsPixelMap.md)* pThis表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。

#### OH_UdsPixelMap_GetType()

```ets
const char* OH_UdsPixelMap_GetType(OH_UdsPixelMap* pThis)
```

**描述**

从像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例中获取类型ID。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsPixelMap](OH_UdsPixelMap.md)* pThis表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回类型ID的字符串指针，否则返回nullptr。

#### OH_UdsPixelMap_GetPixelMap()

```ets
void OH_UdsPixelMap_GetPixelMap(OH_UdsPixelMap* pThis, OH_PixelmapNative* pixelmapNative)
```

**描述**

从像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例中获取像素图片[OH_PixelmapNative](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel)实例的指针。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsPixelMap](OH_UdsPixelMap.md)* pThis表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。OH_PixelmapNative* pixelmapNative该参数是输出参数，表示指向像素图片[OH_PixelmapNative](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel)实例的指针。

#### OH_UdsPixelMap_SetPixelMap()

```ets
int OH_UdsPixelMap_SetPixelMap(OH_UdsPixelMap* pThis, OH_PixelmapNative* pixelmapNative)
```

**描述**

设置像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)对象的像素图片内容。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsPixelMap](OH_UdsPixelMap.md)* pThis表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。OH_PixelmapNative* pixelmapNative表示指向像素图片[OH_PixelmapNative](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel)实例的指针

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsArrayBuffer_Create()

```ets
OH_UdsArrayBuffer* OH_UdsArrayBuffer_Create()
```

**描述**

创建ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH_UdsArrayBuffer_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsarraybuffer_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 13

**返回：**

类型说明[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)*执行成功则返回一个指向ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)实例对象的指针，否则返回nullptr。

#### OH_UdsArrayBuffer_Destroy()

```ets
int OH_UdsArrayBuffer_Destroy(OH_UdsArrayBuffer* buffer)
```

**描述**

销毁ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)的实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)* buffer表示指向ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsArrayBuffer_SetData()

```ets
int OH_UdsArrayBuffer_SetData(OH_UdsArrayBuffer* buffer, unsigned char* data, unsigned int len)
```

**描述**

设置ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)对象的数据内容。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)* buffer表示指向ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)实例的指针。unsigned char* data表示用户自定义的ArrayBuffer数据。unsigned int len表示用户自定义的ArrayBuffer数据的大小。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsArrayBuffer_GetData()

```ets
int OH_UdsArrayBuffer_GetData(OH_UdsArrayBuffer* buffer, unsigned char** data, unsigned int* len)
```

**描述**

从ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)实例中获取用户自定义的ArrayBuffer数据内容。

**起始版本：** 13

**参数：**

参数项描述[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)* buffer表示指向ArrayBuffer类型[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)实例的指针。unsigned char** data该参数是输出参数，表示用户自定义的ArrayBuffer数据。unsigned int* len该参数是输出参数，表示用户自定义的ArrayBuffer数据的大小。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsArrayBuffer](OH_UdsArrayBuffer.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsContentForm_Create()

```ets
OH_UdsContentForm* OH_UdsContentForm_Create()
```

**描述**

创建内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)指针及实例对象。

**起始版本：** 14

**返回：**

类型说明[OH_UdsContentForm](OH_UdsContentForm.md)*执行成功则返回一个指向内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)实例对象的指针，否则返回nullptr。

#### OH_UdsContentForm_Destroy()

```ets
void OH_UdsContentForm_Destroy(OH_UdsContentForm* pThis)
```

**描述**

销毁内容卡片类型数据[OH_UdsContentForm](OH_UdsContentForm.md)指针指向的实例对象。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

#### OH_UdsContentForm_GetType()

```ets
const char* OH_UdsContentForm_GetType(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中获取类型ID。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回类型ID的字符串指针，否则返回nullptr。

#### OH_UdsContentForm_GetThumbData()

```ets
int OH_UdsContentForm_GetThumbData(OH_UdsContentForm* pThis, unsigned char** thumbData, unsigned int* len)
```

**描述**

从内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中获取图片数据。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。unsigned char** thumbData该参数是输出参数，表示内容卡片中的图片二进制数据。unsigned int* len该参数是输出参数，表示内容卡片中的图片二进制数据的大小。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsContentForm](OH_UdsContentForm.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示出现了内部系统错误。

#### OH_UdsContentForm_GetDescription()

```ets
const char* OH_UdsContentForm_GetDescription(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中获取描述信息。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回描述信息的字符串指针，否则返回nullptr。

#### OH_UdsContentForm_GetTitle()

```ets
const char* OH_UdsContentForm_GetTitle(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中获取标题信息。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回标题信息的字符串指针，否则返回nullptr。

#### OH_UdsContentForm_GetAppIcon()

```ets
int OH_UdsContentForm_GetAppIcon(OH_UdsContentForm* pThis, unsigned char** appIcon, unsigned int* len)
```

**描述**

从内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中获取应用图标数据。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。unsigned char** appIcon该参数是输出参数，表示内容卡片中的应用图标二进制数据。unsigned int* len该参数是输出参数，表示内容卡片中的应用图标二进制数据的大小。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsContentForm](OH_UdsContentForm.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

若返回UDMF_ERR，表示出现了内部系统错误。

#### OH_UdsContentForm_GetAppName()

```ets
const char* OH_UdsContentForm_GetAppName(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中获取应用名称信息。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回应用名称信息的字符串指针，否则返回nullptr。

#### OH_UdsContentForm_GetLinkUri()

```ets
const char* OH_UdsContentForm_GetLinkUri(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中获取超链接信息。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。

**返回：**

类型说明const char*输入有效入参时返回超链接的字符串指针，否则返回nullptr。

#### OH_UdsContentForm_SetThumbData()

```ets
int OH_UdsContentForm_SetThumbData(OH_UdsContentForm* pThis, const unsigned char* thumbData, unsigned int len)
```

**描述**

设置内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中的图片数据。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。const unsigned char* thumbData表示内容卡片中的图片二进制数据。unsigned int len表示内容卡片中的图片二进制数据的大小。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsContentForm](OH_UdsContentForm.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsContentForm_SetDescription()

```ets
int OH_UdsContentForm_SetDescription(OH_UdsContentForm* pThis, const char* description)
```

**描述**

设置内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中的描述信息。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。const char* description表示描述信息。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsContentForm](OH_UdsContentForm.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsContentForm_SetTitle()

```ets
int OH_UdsContentForm_SetTitle(OH_UdsContentForm* pThis, const char* title)
```

**描述**

设置内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中的标题信息。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。const char* title表示标题信息。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[OH_UdsContentForm](OH_UdsContentForm.md)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsContentForm_SetAppIcon()

```ets
int OH_UdsContentForm_SetAppIcon(OH_UdsContentForm* pThis, const unsigned char* appIcon, unsigned int len)
```

**描述**

设置内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中的应用图标数据。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。const unsigned char* appIcon表示内容卡片中的应用图标二进制数据。unsigned int len表示内容卡片中的应用图标二进制数据的大小。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsContentForm_SetAppName()

```ets
int OH_UdsContentForm_SetAppName(OH_UdsContentForm* pThis, const char* appName)
```

**描述**

设置内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中的应用名称数据。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。const char* appName表示内容卡片中的应用名称。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsContentForm_SetLinkUri()

```ets
int OH_UdsContentForm_SetLinkUri(OH_UdsContentForm* pThis, const char* linkUri)
```

**描述**

设置内容卡片类型[OH_UdsContentForm](OH_UdsContentForm.md)中的超链接数据。

**起始版本：** 14

**参数：**

参数项描述[OH_UdsContentForm](OH_UdsContentForm.md)* pThis表示指向[OH_UdsContentForm](OH_UdsContentForm.md)实例的指针。const char* linkUri表示内容卡片中的超链接。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsPlainText_GetDetails()

```ets
int OH_UdsPlainText_GetDetails(OH_UdsPlainText* pThis, OH_UdsDetails* details)
```

**描述**

从纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。[OH_UdsDetails](OH_UdsDetails.md)* details该参数是输出参数，表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsPlainText_SetDetails()

```ets
int OH_UdsPlainText_SetDetails(OH_UdsPlainText* pThis, const OH_UdsDetails* details)
```

**描述**

设置纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)中的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsPlainText](OH_UdsPlainText.md)* pThis表示指向纯文本类型[OH_UdsPlainText](OH_UdsPlainText.md)实例的指针。[const OH_UdsDetails](OH_UdsDetails.md)* details表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHyperlink_GetDetails()

```ets
int OH_UdsHyperlink_GetDetails(OH_UdsHyperlink* pThis, OH_UdsDetails* details)
```

**描述**

从超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。[OH_UdsDetails](OH_UdsDetails.md)* details该参数是输出参数，表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHyperlink_SetDetails()

```ets
int OH_UdsHyperlink_SetDetails(OH_UdsHyperlink* pThis, const OH_UdsDetails* details)
```

**描述**

设置超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例中的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsHyperlink](OH_UdsHyperlink.md)* pThis表示指向超链接类型[OH_UdsHyperlink](OH_UdsHyperlink.md)实例的指针。[const OH_UdsDetails](OH_UdsDetails.md)* details表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHtml_GetDetails()

```ets
int OH_UdsHtml_GetDetails(OH_UdsHtml* pThis, OH_UdsDetails* details)
```

**描述**

从超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)对象中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。[OH_UdsDetails](OH_UdsDetails.md)* details该参数是输出参数，表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsHtml_SetDetails()

```ets
int OH_UdsHtml_SetDetails(OH_UdsHtml* pThis, const OH_UdsDetails* details)
```

**描述**

设置超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)中的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsHtml](OH_UdsHtml.md)* pThis表示指向超文本标记语言类型[OH_UdsHtml](OH_UdsHtml.md)实例的指针。[const OH_UdsDetails](OH_UdsDetails.md)* details表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_GetDetails()

```ets
int OH_UdsAppItem_GetDetails(OH_UdsAppItem* pThis, OH_UdsDetails* details)
```

**描述**

从桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)实例中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。[OH_UdsDetails](OH_UdsDetails.md)* details该参数是输出参数，表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsAppItem_SetDetails()

```ets
int OH_UdsAppItem_SetDetails(OH_UdsAppItem* pThis, const OH_UdsDetails* details)
```

**描述**

设置桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsAppItem](OH_UdsAppItem.md)* pThis表示一个指向桌面图标类型[OH_UdsAppItem](OH_UdsAppItem.md)对象的指针。[const OH_UdsDetails](OH_UdsDetails.md)* details表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsFileUri_GetDetails()

```ets
int OH_UdsFileUri_GetDetails(OH_UdsFileUri* pThis, OH_UdsDetails* details)
```

**描述**

从文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。[OH_UdsDetails](OH_UdsDetails.md)* details该参数是输出参数，表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsFileUri_SetDetails()

```ets
int OH_UdsFileUri_SetDetails(OH_UdsFileUri* pThis, const OH_UdsDetails* details)
```

**描述**

设置文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)对象的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsFileUri](OH_UdsFileUri.md)* pThis表示指向文件Uri类型[OH_UdsFileUri](OH_UdsFileUri.md)实例的指针。[const OH_UdsDetails](OH_UdsDetails.md)* details表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsPixelMap_GetDetails()

```ets
int OH_UdsPixelMap_GetDetails(OH_UdsPixelMap* pThis, OH_UdsDetails* details)
```

**描述**

从像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例中获取字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsPixelMap](OH_UdsPixelMap.md)* pThis表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。[OH_UdsDetails](OH_UdsDetails.md)* details该参数是输出参数，表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsPixelMap_SetDetails()

```ets
int OH_UdsPixelMap_SetDetails(OH_UdsPixelMap* pThis, const OH_UdsDetails* details)
```

**描述**

设置像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)对象的字典类型[OH_UdsDetails](OH_UdsDetails.md)参数。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsPixelMap](OH_UdsPixelMap.md)* pThis表示指向像素图片类型[OH_UdsPixelMap](OH_UdsPixelMap.md)实例的指针。[const OH_UdsDetails](OH_UdsDetails.md)* details表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针，该指针不能为空。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效参数。

#### OH_UdsDetails_Create()

```ets
OH_UdsDetails* OH_UdsDetails_Create()
```

**描述**

创建字典类型[OH_UdsDetails](OH_UdsDetails.md)指针及实例对象。

当不再需要使用指针时，请使用[OH_UdsDetails_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 22

**返回：**

类型说明[OH_UdsDetails*](OH_UdsDetails.md)执行成功则返回一个指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例对象的指针，否则返回nullptr。

#### OH_UdsDetails_Destroy()

```ets
void OH_UdsDetails_Destroy(OH_UdsDetails* pThis)
```

**描述**

销毁字典类型[OH_UdsDetails](OH_UdsDetails.md)指针指向的实例对象。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsDetails](OH_UdsDetails.md)* pThis表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

#### OH_UdsDetails_HasKey()

```ets
bool OH_UdsDetails_HasKey(const OH_UdsDetails* pThis, const char* key)
```

**描述**

检查字典类型[OH_UdsDetails](OH_UdsDetails.md)中是否存在指定键。

**起始版本：** 22

**参数：**

参数项描述[const OH_UdsDetails](OH_UdsDetails.md)* pThis表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。const char* key表示字典类型中键值对的键。

**返回：**

类型说明bool返回查找结果的状态。返回false表示不存在指定键，返回true表示存在指定键。

#### OH_UdsDetails_Remove()

```ets
int OH_UdsDetails_Remove(OH_UdsDetails* pThis, const char* key)
```

**描述**

删除字典类型[OH_UdsDetails](OH_UdsDetails.md)中指定键值对。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsDetails](OH_UdsDetails.md)* pThis表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。const char* key表示字典类型中键值对的键。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsDetails_Clear()

```ets
int OH_UdsDetails_Clear(OH_UdsDetails* pThis)
```

**描述**

清除字典类型[OH_UdsDetails](OH_UdsDetails.md)中所有数据。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsDetails](OH_UdsDetails.md)* pThis表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsDetails_SetValue()

```ets
int OH_UdsDetails_SetValue(OH_UdsDetails* pThis, const char* key, const char* value)
```

**描述**

向字典类型[OH_UdsDetails](OH_UdsDetails.md)中添加键值对数据。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsDetails](OH_UdsDetails.md)* pThis表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。const char* key表示字典类型中键值对的键。const char* value表示字典类型中键值对的值。

**返回：**

类型说明int

返回执行的错误码。请参阅错误码定义[Udmf_ErrCode](udmf_err_code.h.md#ZH-CN_TOPIC_0000002529284699__udmf_errcode)。

若返回UDMF_E_OK，表示执行成功。

若返回UDMF_E_INVALID_PARAM，表示传入了无效的参数。

#### OH_UdsDetails_GetValue()

```ets
const char* OH_UdsDetails_GetValue(const OH_UdsDetails* pThis, const char* key)
```

**描述**

获取字典类型[OH_UdsDetails](OH_UdsDetails.md)中指定的键对应的值。

**起始版本：** 22

**参数：**

参数项描述[const OH_UdsDetails](OH_UdsDetails.md)* pThis表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。const char* key表示字典类型中键值对的键。

**返回：**

类型说明const char*当入参有效时返回指向字典类型中值的指针，否则返回nullptr。

#### OH_UdsDetails_GetAllKeys()

```ets
char** OH_UdsDetails_GetAllKeys(OH_UdsDetails* pThis, unsigned int* count)
```

**描述**

获取字典类型[OH_UdsDetails](OH_UdsDetails.md)中所有键的结果集。

**起始版本：** 22

**参数：**

参数项描述[OH_UdsDetails](OH_UdsDetails.md)* pThis表示指向字典类型[OH_UdsDetails](OH_UdsDetails.md)实例的指针。unsigned int* count该参数是输出参数，表示结果集的长度。

**返回：**

类型说明char**

执行成功时返回字典类型中键的结果集，否则返回nullptr。

当使用[OH_UdsDetails_Destroy](uds.h.md#ZH-CN_TOPIC_0000002497604708__oh_udsdetails_destroy)销毁字典类型[OH_UdsDetails](OH_UdsDetails.md)指针指向的实例对象，该返回值也会被释放。