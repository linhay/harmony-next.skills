# oh_pasteboard.h

#### 概述

提供访问系统剪贴板的接口、数据结构、枚举类型。

**引用文件：** <database/pasteboard/oh_pasteboard.h>

**库：** libpasteboard.so

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 13

**相关模块：**[Pasteboard](../../topics/payment/Pasteboard.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Pasteboard_ProgressInfo](../../topics/components/Pasteboard_ProgressInfo.md)Pasteboard_ProgressInfo定义进度上报的数据结构。[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)Pasteboard_GetDataParams表示从剪贴板获取粘贴数据和进度时需要写入的参数。[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)OH_PasteboardObserver定义剪贴板数据变更观察者。[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)OH_Pasteboard定义剪贴板对象，用以操作系统剪贴板。

#### 宏定义

名称描述[PASTEBOARD_MIMETYPE_TEXT_PLAIN](#ZH-CN_TOPIC_0000002497445552__pasteboard_mimetype_text_plain) "text/plain"纯文本类型。[PASTEBOARD_MIMETYPE_TEXT_URI](#ZH-CN_TOPIC_0000002497445552__pasteboard_mimetype_text_uri) "text/uri"URI类型。[PASTEBOARD_MIMETYPE_TEXT_HTML](#ZH-CN_TOPIC_0000002497445552__pasteboard_mimetype_text_html) "text/html"HTML类型。[PASTEBOARD_MIMETYPE_PIXELMAP](#ZH-CN_TOPIC_0000002497445552__pasteboard_mimetype_pixelmap) "pixelMap"pixelMap类型。[PASTEBOARD_MIMETYPE_TEXT_WANT](#ZH-CN_TOPIC_0000002497445552__pasteboard_mimetype_text_want) "text/want"want类型。

#### 枚举

名称typedef关键字描述[Pasteboard_NotifyType](#ZH-CN_TOPIC_0000002497445552__pasteboard_notifytype)Pasteboard_NotifyType剪贴板的数据变更类型。[Pasteboard_FileConflictOptions](#ZH-CN_TOPIC_0000002497445552__pasteboard_fileconflictoptions)Pasteboard_FileConflictOptions定义文件拷贝冲突时的选项。[Pasteboard_ProgressIndicator](#ZH-CN_TOPIC_0000002497445552__pasteboard_progressindicator)Pasteboard_ProgressIndicator定义进度条指示选项，可选择是否采用系统默认进度显示。

#### 函数

名称typedef关键字描述[typedef void (*OH_Pasteboard_ProgressListener)(Pasteboard_ProgressInfo* progressInfo)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_progresslistener)OH_Pasteboard_ProgressListener用于在不使用系统默认进度显示时，通知应用拷贝粘贴任务进度。[typedef void (*Pasteboard_Notify)(void* context, Pasteboard_NotifyType type)](#ZH-CN_TOPIC_0000002497445552__pasteboard_notify)Pasteboard_Notify定义剪贴板内容变更时触发的回调函数。[typedef void (*Pasteboard_Finalize)(void* context)](#ZH-CN_TOPIC_0000002497445552__pasteboard_finalize)Pasteboard_Finalize定义用于释放上下文的回调函数，剪贴板数据变更观察者对象销毁时触发。[OH_PasteboardObserver* OH_PasteboardObserver_Create()](#ZH-CN_TOPIC_0000002497445552__oh_pasteboardobserver_create)-创建一个剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)指针及实例对象。[int OH_PasteboardObserver_Destroy(OH_PasteboardObserver* observer)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboardobserver_destroy)-销毁剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)指针指向的实例对象。[int OH_PasteboardObserver_SetData(OH_PasteboardObserver* observer, void* context,const Pasteboard_Notify callback, const Pasteboard_Finalize finalize)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboardobserver_setdata)-向剪贴板数据变更观察者设置回调函数。[OH_Pasteboard* OH_Pasteboard_Create()](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_create)-创建剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)指针及实例对象。[void OH_Pasteboard_Destroy(OH_Pasteboard* pasteboard)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_destroy)-销毁剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例对象。[int OH_Pasteboard_Subscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_subscribe)-订阅剪贴板的数据变更事件。[int OH_Pasteboard_Unsubscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_unsubscribe)-取消对剪贴板数据变更事件的订阅。[bool OH_Pasteboard_IsRemoteData(OH_Pasteboard* pasteboard)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_isremotedata)-判断剪贴板中的数据是否来自远端设备。[int OH_Pasteboard_GetDataSource(OH_Pasteboard* pasteboard, char* source, unsigned int len)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdatasource)-获取剪贴板中数据的数据源。[bool OH_Pasteboard_HasType(OH_Pasteboard* pasteboard, const char* type)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_hastype)-判断剪贴板中是否有指定类型的数据。[bool OH_Pasteboard_HasData(OH_Pasteboard* pasteboard)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_hasdata)-判断剪贴板中是否有数据。[OH_UdmfData* OH_Pasteboard_GetData(OH_Pasteboard* pasteboard, int* status)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdata)-获取剪贴板中的数据。[int OH_Pasteboard_SetData(OH_Pasteboard* pasteboard, OH_UdmfData* data)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_setdata)-将统一数据对象数据写入剪贴板。[int OH_Pasteboard_ClearData(OH_Pasteboard* pasteboard)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_cleardata)-清空剪贴板中的数据。[char **OH_Pasteboard_GetMimeTypes(OH_Pasteboard *pasteboard, unsigned int *count)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getmimetypes)-获取剪贴板中的MIME类型。[Pasteboard_GetDataParams *OH_Pasteboard_GetDataParams_Create(void)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdataparams_create)-创建剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)指针及实例对象。[void OH_Pasteboard_GetDataParams_Destroy(Pasteboard_GetDataParams* params)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdataparams_destroy)-销毁剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)指针指向的实例对象。[void OH_Pasteboard_GetDataParams_SetProgressIndicator(Pasteboard_GetDataParams* params,Pasteboard_ProgressIndicator progressIndicator)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdataparams_setprogressindicator)-向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)设置进度条指示选项，可选择是否采用系统默认进度显示。[void OH_Pasteboard_GetDataParams_SetDestUri(Pasteboard_GetDataParams* params, const char* destUri, uint32_t destUriLen)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdataparams_setdesturi)-向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)设置拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。[void OH_Pasteboard_GetDataParams_SetFileConflictOptions(Pasteboard_GetDataParams* params,Pasteboard_FileConflictOptions option)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdataparams_setfileconflictoptions)-向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)设置文件冲突选项。[void OH_Pasteboard_GetDataParams_SetProgressListener(Pasteboard_GetDataParams* params,const OH_Pasteboard_ProgressListener listener)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdataparams_setprogresslistener)-向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)设置进度上报回调函数。[int OH_Pasteboard_ProgressInfo_GetProgress(Pasteboard_ProgressInfo* progressInfo)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_progressinfo_getprogress)-从[Pasteboard_ProgressInfo](../../topics/components/Pasteboard_ProgressInfo.md)获取粘贴进度。[void OH_Pasteboard_ProgressCancel(Pasteboard_GetDataParams* params)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_progresscancel)-定义取消函数，用于在获取粘贴数据时取消正在进行的粘贴动作。[OH_UdmfData* OH_Pasteboard_GetDataWithProgress(OH_Pasteboard* pasteboard, Pasteboard_GetDataParams* params,int* status)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdatawithprogress)-获取剪贴板的数据以及粘贴进度，不支持对文件夹的拷贝。[uint32_t OH_Pasteboard_GetChangeCount(OH_Pasteboard *pasteboard)](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getchangecount)-获取剪贴板内容的变化次数。[void OH_Pasteboard_SyncDelayedDataAsync(OH_Pasteboard* pasteboard, void (*callback)(int errorCode))](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_syncdelayeddataasync)-通知剪贴板从应用同步所有延迟数据，与延迟复制接口[OH_UdmfRecordProvider_SetData](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_setdata)搭配使用。当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH_Pasteboard_SetData](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_setdata)接口主动提交所有复制数据或调用此接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。

#### 宏定义说明

#### PASTEBOARD_MIMETYPE_TEXT_PLAIN

```ets
#define PASTEBOARD_MIMETYPE_TEXT_PLAIN "text/plain"
```

**描述**

纯文本类型。

**起始版本：** 22

#### PASTEBOARD_MIMETYPE_TEXT_URI

```ets
#define PASTEBOARD_MIMETYPE_TEXT_URI "text/uri"
```

**描述**

URI类型。

**起始版本：** 22

#### PASTEBOARD_MIMETYPE_TEXT_HTML

```ets
#define PASTEBOARD_MIMETYPE_TEXT_HTML "text/html"
```

**描述**

HTML类型。

**起始版本：** 22

#### PASTEBOARD_MIMETYPE_PIXELMAP

```ets
#define PASTEBOARD_MIMETYPE_PIXELMAP "pixelMap"
```

**描述**

pixelMap类型。

**起始版本：** 22

#### PASTEBOARD_MIMETYPE_TEXT_WANT

```ets
#define PASTEBOARD_MIMETYPE_TEXT_WANT "text/want"
```

**描述**

want类型。

**起始版本：** 22

#### 枚举类型说明

#### Pasteboard_NotifyType

```ets
enum Pasteboard_NotifyType
```

**描述：**

剪贴板的数据变更类型。

**起始版本：** 13

枚举项描述NOTIFY_LOCAL_DATA_CHANGE = 1本地设备剪贴板数据变更。NOTIFY_REMOTE_DATA_CHANGE = 2组网内的非本地设备剪贴板数据变更。

#### Pasteboard_FileConflictOptions

```ets
enum Pasteboard_FileConflictOptions
```

**描述：**

定义文件拷贝冲突时的选项。

**起始版本：** 15

枚举项描述PASTEBOARD_OVERWRITE = 0目标路径存在同文件名时覆盖。PASTEBOARD_SKIP = 1目标路径存在同文件名时跳过。

#### Pasteboard_ProgressIndicator

```ets
enum Pasteboard_ProgressIndicator
```

**描述：**

定义进度条指示选项，可选择是否采用系统默认进度显示。

**起始版本：** 15

枚举项描述PASTEBOARD_NONE = 0不采用系统默认进度显示。PASTEBOARD_DEFAULT = 1采用系统默认进度显示。

#### 函数说明

#### OH_Pasteboard_ProgressListener()

```ets
typedef void (*OH_Pasteboard_ProgressListener)(Pasteboard_ProgressInfo* progressInfo)
```

**描述：**

用于在不使用系统默认进度显示时，通知应用拷贝粘贴任务进度。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_ProgressInfo](../../topics/components/Pasteboard_ProgressInfo.md)* progressInfo定义进度上报的数据结构，且仅当进度指示选项[Pasteboard_ProgressInfo](../../topics/components/Pasteboard_ProgressInfo.md)设置为NONE时才会上报此信息。

#### Pasteboard_Notify()

```ets
typedef void (*Pasteboard_Notify)(void* context, Pasteboard_NotifyType type)
```

**描述：**

定义剪贴板内容变更时触发的回调函数。

**起始版本：** 13

**参数：**

参数项描述void* context上下文信息，由函数[OH_PasteboardObserver_SetData](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__oh_pasteboardobserver_setdata)传入。[Pasteboard_NotifyType](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_notifytype) type数据变更的类型。详见：[Pasteboard_NotifyType](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_notifytype)。

#### Pasteboard_Finalize()

```ets
typedef void (*Pasteboard_Finalize)(void* context)
```

**描述：**

定义用于释放上下文的回调函数，剪贴板数据变更观察者对象销毁时触发。

**起始版本：** 13

**参数：**

参数项描述void* context要释放的上下文指针。

#### OH_PasteboardObserver_Create()

```ets
OH_PasteboardObserver* OH_PasteboardObserver_Create()
```

**描述：**

创建一个剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)指针及实例对象。

**起始版本：** 13

**返回：**

类型说明[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)*

执行成功时返回一个指向剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)实例对象的指针，否则返回空指针。

当不再需要使用指针时，请使用[OH_PasteboardObserver_Destroy](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__oh_pasteboardobserver_destroy)销毁实例对象，否则会导致内存泄漏。

#### OH_PasteboardObserver_Destroy()

```ets
int OH_PasteboardObserver_Destroy(OH_PasteboardObserver* observer)
```

**描述：**

销毁剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)指针指向的实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)* observer表示指向剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

若返回[ERR_OK](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示指向成功。

若返回[ERR_INVALID_PARAMETER](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示传入了无效参数。

#### OH_PasteboardObserver_SetData()

```ets
int OH_PasteboardObserver_SetData(OH_PasteboardObserver* observer, void* context,const Pasteboard_Notify callback, const Pasteboard_Finalize finalize)
```

**描述：**

向剪贴板数据变更观察者设置回调函数。

**起始版本：** 13

**参数：**

参数项描述[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)* observer表示指向剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)实例的指针。void* context表示指向上下文数据的指针，将作为第一个参数传入[Pasteboard_Notify](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_notify)。const [Pasteboard_Notify](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_notify) callback表示数据变更回调函数。详见：[Pasteboard_Notify](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_notify)。const [Pasteboard_Finalize](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_finalize) finalize表示可选的回调函数，可以用于剪贴板数据变更观察者销毁时释放上下文数据。详见：[Pasteboard_Finalize](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_finalize)。

**返回：**

类型说明int

返回执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

若返回[ERR_OK](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示指向成功。

若返回[ERR_INVALID_PARAMETER](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示传入了无效参数。

#### OH_Pasteboard_Create()

```ets
OH_Pasteboard* OH_Pasteboard_Create()
```

**描述：**

创建剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)指针及实例对象。

**起始版本：** 13

**返回：**

类型说明[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)*执行成功则返回一个指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例对象的指针，否则返回nullptr。

#### OH_Pasteboard_Destroy()

```ets
void OH_Pasteboard_Destroy(OH_Pasteboard* pasteboard)
```

**描述：**

销毁剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。

#### OH_Pasteboard_Subscribe()

```ets
int OH_Pasteboard_Subscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)
```

**描述：**

订阅剪贴板的数据变更事件。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。int type表示订阅的剪贴板数据变更类型，详见：[Pasteboard_NotifyType](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_notifytype)。const [OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)* observer表示指向剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)实例的指针。它指定了剪贴板数据变更时触发的回调函数，详见：[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)。

**返回：**

类型说明int

返回执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

若返回[ERR_OK](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示指向成功。

若返回[ERR_INVALID_PARAMETER](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示传入了无效参数。

#### OH_Pasteboard_Unsubscribe()

```ets
int OH_Pasteboard_Unsubscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)
```

**描述：**

取消对剪贴板数据变更事件的订阅。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。int type表示订阅的剪贴板数据变更类型，详见：[Pasteboard_NotifyType](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__pasteboard_notifytype)。const [OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)* observer表示指向剪贴板数据变更观察者[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)实例的指针。它指定了剪贴板数据变更时触发的回调函数，详见：[OH_PasteboardObserver](../../topics/payment/OH_PasteboardObserver.md)。

**返回：**

类型说明int

返回执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

若返回[ERR_OK](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示指向成功。

若返回[ERR_INVALID_PARAMETER](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示传入了无效参数。

#### OH_Pasteboard_IsRemoteData()

```ets
bool OH_Pasteboard_IsRemoteData(OH_Pasteboard* pasteboard)
```

**描述：**

判断剪贴板中的数据是否来自远端设备。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。

**返回：**

类型说明bool返回剪贴板中的数据是否来自远端设备。返回true表示剪贴板中的数据来自远端设备，返回false表示剪贴板中数据来自本端设备。

#### OH_Pasteboard_GetDataSource()

```ets
int OH_Pasteboard_GetDataSource(OH_Pasteboard* pasteboard, char* source, unsigned int len)
```

**描述：**

获取剪贴板中数据的数据源。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。char* source表示用于存放剪贴板数据源实例的指针，开发者需在调用接口前申请指针指向的内存。unsigned int len表示source指针对应的内存长度，当内存长度不足时调用接口会失败，建议长度：128。

**返回：**

类型说明int

返回执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

若返回[ERR_OK](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示指向成功。

若返回[ERR_INVALID_PARAMETER](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示传入了无效参数。

#### OH_Pasteboard_HasType()

```ets
bool OH_Pasteboard_HasType(OH_Pasteboard* pasteboard, const char* type)
```

**描述：**

判断剪贴板中是否有指定类型的数据。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。const char* type表示要检查的数据类型。包含剪贴板基础数据类型与自定义数据类型，其中剪贴板基础数据类型有："text/plain"、"text/html"、"text/uri"、"text/want"和"pixelMap"。

**返回：**

类型说明bool返回剪贴板中是否有指定类型的数据。返回true表示剪贴板中包含指定类型的数据，返回false表示剪贴板中没有指定类型的数据。

#### OH_Pasteboard_HasData()

```ets
bool OH_Pasteboard_HasData(OH_Pasteboard* pasteboard)
```

**描述：**

判断剪贴板中是否有数据。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。

**返回：**

类型说明bool返回剪贴板中是否有数据。返回true表示剪贴板中有数据，返回false表示剪贴板中没有数据。

#### OH_Pasteboard_GetData()

```ets
OH_UdmfData* OH_Pasteboard_GetData(OH_Pasteboard* pasteboard, int* status)
```

**描述：**

获取剪贴板中的数据。

**起始版本：** 13

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。int* status该参数是输出参数，表示执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

**返回：**

类型说明[OH_UdmfData](../../topics/misc/OH_UdmfData.md)*执行成功时返回统一数据对象[OH_UdmfData](../../topics/misc/OH_UdmfData.md)实例的指针。否则返回空指针。

#### OH_Pasteboard_SetData()

```ets
int OH_Pasteboard_SetData(OH_Pasteboard* pasteboard, OH_UdmfData* data)
```

**描述：**

将统一数据对象数据写入剪贴板。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。[OH_UdmfData](../../topics/misc/OH_UdmfData.md)* data表示指向统一数据对象[OH_UdmfData](../../topics/misc/OH_UdmfData.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

若返回[ERR_OK](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示指向成功。

若返回[ERR_INVALID_PARAMETER](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示传入了无效参数。

#### OH_Pasteboard_ClearData()

```ets
int OH_Pasteboard_ClearData(OH_Pasteboard* pasteboard)
```

**描述：**

清空剪贴板中的数据。

**起始版本：** 13

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。

**返回：**

类型说明int

返回执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

若返回[ERR_OK](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示指向成功。

若返回[ERR_INVALID_PARAMETER](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)，表示传入了无效参数。

#### OH_Pasteboard_GetMimeTypes()

```ets
char **OH_Pasteboard_GetMimeTypes(OH_Pasteboard *pasteboard, unsigned int *count)
```

**描述：**

获取剪贴板中的MIME类型。

**起始版本：** 14

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md) *pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。unsigned int *count该参数是输出参数，结果集中的类型数量会写入该变量。

**返回：**

类型说明char执行成功时返回剪贴板所有内容的MIME类型，否则返回nullptr。

#### OH_Pasteboard_GetDataParams_Create()

```ets
Pasteboard_GetDataParams *OH_Pasteboard_GetDataParams_Create(void)
```

**描述：**

创建剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)指针及实例对象。

**起始版本：** 15

**返回：**

类型说明[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)

执行成功时返回一个指向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)实例对象的指针，否则返回空指针。

当不再需要使用指针时，请使用[OH_Pasteboard_GetDataParams_Destroy](oh_pasteboard.h.md#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_getdataparams_destroy)销毁实例对象，否则会导致内存泄漏。

#### OH_Pasteboard_GetDataParams_Destroy()

```ets
void OH_Pasteboard_GetDataParams_Destroy(Pasteboard_GetDataParams* params)
```

**描述：**

销毁剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)指针指向的实例对象。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)* params表示指向剪贴板OH_Pasteboard_GetDataParams的指针。

#### OH_Pasteboard_GetDataParams_SetProgressIndicator()

```ets
void OH_Pasteboard_GetDataParams_SetProgressIndicator(Pasteboard_GetDataParams* params,Pasteboard_ProgressIndicator progressIndicator)
```

**描述：**

向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)设置进度条指示选项，可选择是否采用系统默认进度显示。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)* params表示指向剪贴板OH_Pasteboard_GetDataParams的指针。[Pasteboard_ProgressIndicator](#ZH-CN_TOPIC_0000002497445552__pasteboard_progressindicator) progressIndicator定义进度条指示选项。

#### OH_Pasteboard_GetDataParams_SetDestUri()

```ets
void OH_Pasteboard_GetDataParams_SetDestUri(Pasteboard_GetDataParams* params, const char* destUri, uint32_t destUriLen)
```

**描述：**

设置拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)* params表示指向剪贴板OH_Pasteboard_GetDataParams的指针。const char* destUri定义拷贝文件目标路径。uint32_t destUriLen定义拷贝文件目标路径长度。

#### OH_Pasteboard_GetDataParams_SetFileConflictOptions()

```ets
void OH_Pasteboard_GetDataParams_SetFileConflictOptions(Pasteboard_GetDataParams* params,Pasteboard_FileConflictOptions option)
```

**描述：**

向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)设置文件冲突选项。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)* params表示指向剪贴板OH_Pasteboard_GetDataParams的指针。[Pasteboard_FileConflictOptions](#ZH-CN_TOPIC_0000002497445552__pasteboard_fileconflictoptions) option定义文件拷贝冲突时的选项，默认为PASTEBOARD_OVERWRITE。

#### OH_Pasteboard_GetDataParams_SetProgressListener()

```ets
void OH_Pasteboard_GetDataParams_SetProgressListener(Pasteboard_GetDataParams* params,const OH_Pasteboard_ProgressListener listener)
```

**描述：**

向剪贴板[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)设置进度上报回调函数。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)* params表示指向剪贴板OH_Pasteboard_GetDataParams的指针。const [OH_Pasteboard_ProgressListener](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_progresslistener) listener表示进度上报回调函数。

#### OH_Pasteboard_ProgressInfo_GetProgress()

```ets
int OH_Pasteboard_ProgressInfo_GetProgress(Pasteboard_ProgressInfo* progressInfo)
```

**描述：**

从[Pasteboard_ProgressInfo](../../topics/components/Pasteboard_ProgressInfo.md)获取粘贴进度。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_ProgressInfo](../../topics/components/Pasteboard_ProgressInfo.md)* progressInfo表示指向剪贴板[Pasteboard_ProgressInfo](../../topics/components/Pasteboard_ProgressInfo.md)的指针。

**返回：**

类型说明int返回粘贴进度百分比。

#### OH_Pasteboard_ProgressCancel()

```ets
void OH_Pasteboard_ProgressCancel(Pasteboard_GetDataParams* params)
```

**描述：**

定义取消函数，用于在获取粘贴数据时取消正在进行的粘贴动作。

**起始版本：** 15

**参数：**

参数项描述[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)* params表示指向剪贴板OH_Pasteboard_GetDataParams的指针。

#### OH_Pasteboard_GetDataWithProgress()

```ets
OH_UdmfData* OH_Pasteboard_GetDataWithProgress(OH_Pasteboard* pasteboard, Pasteboard_GetDataParams* params,int* status)
```

**描述：**

获取剪贴板的数据以及粘贴进度，不支持对文件夹的拷贝。

**起始版本：** 15

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)* pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。[Pasteboard_GetDataParams](../../topics/payment/Pasteboard_GetDataParams.md)* params表示指向剪贴板OH_Pasteboard_GetDataParams的指针。int* status该参数是输出参数，表示执行的错误码。错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。

**返回：**

类型说明[OH_UdmfData](../../topics/misc/OH_UdmfData.md)*执行成功时返回统一数据对象OH_PasteData实例的指针。否则返回空指针。

#### OH_Pasteboard_GetChangeCount()

```ets
uint32_t OH_Pasteboard_GetChangeCount(OH_Pasteboard *pasteboard)
```

**描述：**

获取剪贴板内容的变化次数。

**起始版本：** 18

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md) *pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。

**返回：**

类型说明uint32_t

执行成功时返回剪贴板内容的变化次数，否则返回0。

当剪贴板内容过期或调用OH_Pasteboard_ClearData等接口导致剪贴板内容为空时，内容变化次数不会因此改变。

系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被视作多次更改，每次复制均会导致内容变化次数增加。

#### OH_Pasteboard_SyncDelayedDataAsync()

```ets
void OH_Pasteboard_SyncDelayedDataAsync(OH_Pasteboard* pasteboard, void (*callback)(int errorCode))
```

**描述：**

通知剪贴板从应用同步所有延迟数据，与延迟复制接口[OH_UdmfRecordProvider_SetData](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_setdata)搭配使用。当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH_Pasteboard_SetData](#ZH-CN_TOPIC_0000002497445552__oh_pasteboard_setdata)接口主动提交所有复制数据或调用此接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。

- 调用此接口会延长退出过程，建议应用直接设置数据到剪贴板，而不是调用延迟复制接口[OH_UdmfRecordProvider_SetData](udmf.h.md#ZH-CN_TOPIC_0000002497444728__oh_udmfrecordprovider_setdata)和此接口。

**起始版本：** 21

**参数：**

参数项描述[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md) *pasteboard表示指向剪贴板[OH_Pasteboard](../../topics/payment/OH_Pasteboard.md)实例的指针。void (*callback)(int errorCode)数据同步完成后调用的回调函数指针，errorCode表示同步任务的结果，错误码定义详见[PASTEBOARD_ErrCode](oh_pasteboard_err_code.h.md#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)。