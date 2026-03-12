# oh_commonevent.h

#### 概述

定义公共事件订阅与退订API接口与枚举错误码。

**库：** libohcommonevent.so

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**相关模块：**[OH_CommonEvent](OH_CommonEvent.md)

#### 汇总

#### 结构体

名称typedef关键字描述[CommonEvent_SubscribeInfo](CommonEvent_SubscribeInfo.md)CommonEvent_SubscribeInfo提供CommonEvent_SubscribeInfo订阅者信息结构体声明。[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)CommonEvent_PublishInfo发布公共事件时使用的公共事件属性对象。[CommonEvent_RcvData](CommonEvent_RcvData.md)CommonEvent_RcvData提供CommonEvent_RcvData公共事件回调数据结构体声明。

#### 变量

名称typedef关键字描述voidCommonEvent_Subscriber提供CommonEvent_Subscriber订阅者结构体声明。voidCommonEvent_Parameters提供CommonEvent_RcvData公共事件附件信息结构体声明。

#### 枚举

名称typedef关键字描述[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)CommonEvent_ErrCode枚举错误码。

#### 函数

名称typedef关键字描述[typedef void (*CommonEvent_ReceiveCallback)(const CommonEvent_RcvData *data)](#ZH-CN_TOPIC_0000002529445495__commonevent_receivecallback)CommonEvent_ReceiveCallback提供CommonEvent_ReceiveCallback回调函数声明。[CommonEvent_SubscribeInfo* OH_CommonEvent_CreateSubscribeInfo(const char* events[], int32_t eventsNum)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_createsubscribeinfo)-创建订阅者信息。[CommonEvent_ErrCode OH_CommonEvent_SetPublisherPermission(CommonEvent_SubscribeInfo* info, const char* permission)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setpublisherpermission)-设置订阅者权限。[CommonEvent_ErrCode OH_CommonEvent_SetPublisherBundleName(CommonEvent_SubscribeInfo* info, const char* bundleName)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setpublisherbundlename)-设置订阅者包名称。[void OH_CommonEvent_DestroySubscribeInfo(CommonEvent_SubscribeInfo* info)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_destroysubscribeinfo)-释放订阅者信息。[CommonEvent_Subscriber* OH_CommonEvent_CreateSubscriber(const CommonEvent_SubscribeInfo* info,CommonEvent_ReceiveCallback callback)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_createsubscriber)-创建订阅者。[void OH_CommonEvent_DestroySubscriber(CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_destroysubscriber)-释放订阅者。[CommonEvent_ErrCode OH_CommonEvent_Subscribe(const CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_subscribe)-订阅公共事件。[CommonEvent_ErrCode OH_CommonEvent_UnSubscribe(const CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_unsubscribe)-退订公共事件。[const char* OH_CommonEvent_GetEventFromRcvData(const CommonEvent_RcvData* rcvData)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_geteventfromrcvdata)-获取当前接收的公共事件名称。[int32_t OH_CommonEvent_GetCodeFromRcvData(const CommonEvent_RcvData* rcvData)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getcodefromrcvdata)-获取接收到的公共事件数据，整数类型。[const char* OH_CommonEvent_GetDataStrFromRcvData(const CommonEvent_RcvData* rcvData)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getdatastrfromrcvdata)-获取接收到的公共事件数据，字符串类型。[const char* OH_CommonEvent_GetBundleNameFromRcvData(const CommonEvent_RcvData* rcvData)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getbundlenamefromrcvdata)-获取接收到的公共事件的包名称信息。[const CommonEvent_Parameters* OH_CommonEvent_GetParametersFromRcvData(const CommonEvent_RcvData* rcvData)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getparametersfromrcvdata)-获取接收到的公共事件的附加信息。[CommonEvent_PublishInfo* OH_CommonEvent_CreatePublishInfo(bool ordered)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_createpublishinfo)-创建公共事件属性对象。[void OH_CommonEvent_DestroyPublishInfo(CommonEvent_PublishInfo* info)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_destroypublishinfo)-销毁公共事件属性对象。[CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoBundleName(CommonEvent_PublishInfo* info, const char* bundleName)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setpublishinfobundlename)-设置公共事件订阅者包名称。[CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoPermissions(CommonEvent_PublishInfo* info,const char* permissions[], int32_t num)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setpublishinfopermissions)-设置公共事件订阅者权限。[CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoCode(CommonEvent_PublishInfo* info, int32_t code)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setpublishinfocode)-设置公共事件传递的数据，整数类型。[CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoData(CommonEvent_PublishInfo* info,const char* data, size_t length)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setpublishinfodata)-设置公共事件传递的数据，字符串类型。[CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoParameters(CommonEvent_PublishInfo* info,CommonEvent_Parameters* param)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setpublishinfoparameters)-设置公共事件传递的附加信息。[CommonEvent_Parameters* OH_CommonEvent_CreateParameters()](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_createparameters)-创建公共事件附加信息对象。[void OH_CommonEvent_DestroyParameters(CommonEvent_Parameters* param)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_destroyparameters)-销毁公共事件附加信息对象。[bool OH_CommonEvent_HasKeyInParameters(const CommonEvent_Parameters* para, const char* key)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_haskeyinparameters)-检查附加信息中是否包含键值对信息。[int OH_CommonEvent_GetIntFromParameters(const CommonEvent_Parameters* para, const char* key, const int defaultValue)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getintfromparameters)-获取公共事件附加信息中键为key的int类型内容。[CommonEvent_ErrCode OH_CommonEvent_SetIntToParameters(CommonEvent_Parameters* param, const char* key, int value)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setinttoparameters)-设置公共事件附加信息的int类型内容。[int32_t OH_CommonEvent_GetIntArrayFromParameters(const CommonEvent_Parameters* para, const char* key, int** array)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getintarrayfromparameters)-获取公共事件附加信息中键为key的int数组数据。[CommonEvent_ErrCode OH_CommonEvent_SetIntArrayToParameters(CommonEvent_Parameters* param, const char* key,const int* value, size_t num)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setintarraytoparameters)-设置公共事件附加信息的int数组内容。[long OH_CommonEvent_GetLongFromParameters(const CommonEvent_Parameters* para, const char* key, const long defaultValue)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getlongfromparameters)-获取公共事件附加信息中键为key的long类型数据。[CommonEvent_ErrCode OH_CommonEvent_SetLongToParameters(CommonEvent_Parameters* param, const char* key, long value)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setlongtoparameters)-设置公共事件附加信息的long类型内容。[int32_t OH_CommonEvent_GetLongArrayFromParameters(const CommonEvent_Parameters* para, const char* key, long** array)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getlongarrayfromparameters)-获取公共事件附加信息的long数组内容。[CommonEvent_ErrCode OH_CommonEvent_SetLongArrayToParameters(CommonEvent_Parameters* param, const char* key,const long* value, size_t num)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setlongarraytoparameters)-设置公共事件附加信息的long数组内容。[bool OH_CommonEvent_GetBoolFromParameters(const CommonEvent_Parameters* para, const char* key, const bool defaultValue)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getboolfromparameters)-获取公共事件附加信息中键为key的布尔类型数据。[CommonEvent_ErrCode OH_CommonEvent_SetBoolToParameters(CommonEvent_Parameters* param, const char* key, bool value)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setbooltoparameters)-设置公共事件附加信息的布尔类型内容。[int32_t OH_CommonEvent_GetBoolArrayFromParameters(const CommonEvent_Parameters* para, const char* key, bool** array)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getboolarrayfromparameters)-获取公共事件附加信息的布尔数组内容。[CommonEvent_ErrCode OH_CommonEvent_SetBoolArrayToParameters(CommonEvent_Parameters* param, const char* key,const bool* value, size_t num)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setboolarraytoparameters)-设置公共事件附加信息的布尔数组内容。[char OH_CommonEvent_GetCharFromParameters(const CommonEvent_Parameters* para, const char* key, const char defaultValue)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getcharfromparameters)-获取公共事件附加信息中键为key的字符类型数据。[CommonEvent_ErrCode OH_CommonEvent_SetCharToParameters(CommonEvent_Parameters* param, const char* key, char value)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setchartoparameters)-设置公共事件附加信息的字符类型内容。[int32_t OH_CommonEvent_GetCharArrayFromParameters(const CommonEvent_Parameters* para, const char* key, char** array)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getchararrayfromparameters)-获取公共事件附加信息的字符数组内容。[CommonEvent_ErrCode OH_CommonEvent_SetCharArrayToParameters(CommonEvent_Parameters* param, const char* key,const char* value, size_t num)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setchararraytoparameters)-设置公共事件附加信息的字符数组内容。[double OH_CommonEvent_GetDoubleFromParameters(const CommonEvent_Parameters* para, const char* key,const double defaultValue)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getdoublefromparameters)-获取公共事件附加信息的double类型内容。[CommonEvent_ErrCode OH_CommonEvent_SetDoubleToParameters(CommonEvent_Parameters* param, const char* key,double value)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setdoubletoparameters)-设置公共事件附加信息的double类型内容。[int32_t OH_CommonEvent_GetDoubleArrayFromParameters(const CommonEvent_Parameters* para, const char* key,double** array)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getdoublearrayfromparameters)-获取公共事件附加信息中键为key的double数组数据。[CommonEvent_ErrCode OH_CommonEvent_SetDoubleArrayToParameters(CommonEvent_Parameters* param, const char* key,const double* value, size_t num)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setdoublearraytoparameters)-设置公共事件附加信息的double数组内容。[CommonEvent_ErrCode OH_CommonEvent_Publish(const char* event)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_publish)-发布公共事件。[CommonEvent_ErrCode OH_CommonEvent_PublishWithInfo(const char* event, const CommonEvent_PublishInfo* info)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_publishwithinfo)-发布带有指定属性的公共事件。[bool OH_CommonEvent_IsOrderedCommonEvent(const CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_isorderedcommonevent)-查询当前公共事件是否为有序公共事件。[bool OH_CommonEvent_FinishCommonEvent(CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_finishcommonevent)-用于订阅者结束对当前有序公共事件的处理。[bool OH_CommonEvent_GetAbortCommonEvent(const CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getabortcommonevent)-获取当前有序公共事件是否处于中止状态。[bool OH_CommonEvent_AbortCommonEvent(CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_abortcommonevent)-该接口与[OH_CommonEvent_FinishCommonEvent](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。[bool OH_CommonEvent_ClearAbortCommonEvent(CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_clearabortcommonevent)-该接口与[OH_CommonEvent_FinishCommonEvent](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。[int32_t OH_CommonEvent_GetCodeFromSubscriber(const CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getcodefromsubscriber)-获取有序公共事件传递的数据，整数类型。[bool OH_CommonEvent_SetCodeToSubscriber(CommonEvent_Subscriber* subscriber, int32_t code)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setcodetosubscriber)-设置有序公共事件传递的数据，整数类型。[const char* OH_CommonEvent_GetDataFromSubscriber(const CommonEvent_Subscriber* subscriber)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_getdatafromsubscriber)-获取有序公共事件传递的数据，字符串类型。[bool OH_CommonEvent_SetDataToSubscriber(CommonEvent_Subscriber* subscriber, const char* data, size_t length)](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_setdatatosubscriber)-设置有序公共事件传递的数据，字符串类型。

#### 枚举类型说明

#### CommonEvent_ErrCode

```ets
enum CommonEvent_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 12

枚举项描述COMMONEVENT_ERR_OK = 0成功。COMMONEVENT_ERR_PERMISSION_ERROR = 201权限错误。COMMONEVENT_ERR_INVALID_PARAMETER = 401参数错误。COMMONEVENT_ERR_SENDING_LIMIT_EXCEEDED = 1500003

事件发送频率过高。

**起始版本：** 20

COMMONEVENT_ERR_NOT_SYSTEM_SERVICE = 1500004三方应用无法发送系统公共事件。COMMONEVENT_ERR_SENDING_REQUEST_FAILED = 1500007IPC发送失败。COMMONEVENT_ERR_INIT_UNDONE = 1500008服务未初始化。COMMONEVENT_ERR_OBTAIN_SYSTEM_PARAMS = 1500009系统错误。COMMONEVENT_ERR_SUBSCRIBER_NUM_EXCEEDED = 1500010订阅者数量超过限制。COMMONEVENT_ERR_ALLOC_MEMORY_FAILED = 1500011内存分配失败。

#### 函数说明

#### CommonEvent_ReceiveCallback()

```ets
typedef void (*CommonEvent_ReceiveCallback)(const CommonEvent_RcvData *data)
```

**描述**

提供CommonEvent_ReceiveCallback回调函数声明。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_RcvData](CommonEvent_RcvData.md) *data公共事件回调数据。

#### OH_CommonEvent_CreateSubscribeInfo()

```ets
CommonEvent_SubscribeInfo* OH_CommonEvent_CreateSubscribeInfo(const char* events[], int32_t eventsNum)
```

**描述**

创建订阅者信息。

**起始版本：** 12

**参数：**

参数项描述const char* events[]订阅的公共事件，实际订阅的公共事件数量为eventsNum与events数组长度的最小值。int32_t eventsNum订阅的公共事件数量。

**返回：**

类型说明[CommonEvent_SubscribeInfo](CommonEvent_SubscribeInfo.md)*成功则返回订阅者信息,失败则返回NULL。

#### OH_CommonEvent_SetPublisherPermission()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetPublisherPermission(CommonEvent_SubscribeInfo* info, const char* permission)
```

**描述**

设置订阅者权限。

**起始版本：** 12

**参数：**

参数项描述[CommonEvent_SubscribeInfo](CommonEvent_SubscribeInfo.md)* info订阅者信息。const char* permission权限名称。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_SetPublisherBundleName()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetPublisherBundleName(CommonEvent_SubscribeInfo* info, const char* bundleName)
```

**描述**

设置订阅者包名称。

**起始版本：** 12

**参数：**

参数项描述[CommonEvent_SubscribeInfo](CommonEvent_SubscribeInfo.md)* info订阅者信息。const char* bundleName包名称。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_DestroySubscribeInfo()

```ets
void OH_CommonEvent_DestroySubscribeInfo(CommonEvent_SubscribeInfo* info)
```

**描述**

释放订阅者信息。

**起始版本：** 12

**参数：**

参数项描述[CommonEvent_SubscribeInfo](CommonEvent_SubscribeInfo.md)* info订阅者信息。

#### OH_CommonEvent_CreateSubscriber()

```ets
CommonEvent_Subscriber* OH_CommonEvent_CreateSubscriber(const CommonEvent_SubscribeInfo* info,CommonEvent_ReceiveCallback callback)
```

**描述**

创建订阅者。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_SubscribeInfo](CommonEvent_SubscribeInfo.md)* info订阅者信息。[CommonEvent_ReceiveCallback](#ZH-CN_TOPIC_0000002529445495__commonevent_receivecallback) callback公共事件回调函数

**返回：**

类型说明[CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)*成功则返回订阅者,失败则返回NULL。

#### OH_CommonEvent_DestroySubscriber()

```ets
void OH_CommonEvent_DestroySubscriber(CommonEvent_Subscriber* subscriber)
```

**描述**

释放订阅者。

**起始版本：** 12

**参数：**

参数项描述[CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber订阅者。

#### OH_CommonEvent_Subscribe()

```ets
CommonEvent_ErrCode OH_CommonEvent_Subscribe(const CommonEvent_Subscriber* subscriber)
```

**描述**

订阅公共事件。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber订阅者。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数subscriber无效。

 返回[COMMONEVENT_ERR_SENDING_REQUEST_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示IPC请求发送失败。

 返回[COMMONEVENT_ERR_INIT_UNDONE](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示公共事件服务未初始化。

 返回[COMMONEVENT_ERR_SUBSCRIBER_NUM_EXCEEDED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示进程订阅者数量超过200个。

 返回[COMMONEVENT_ERR_ALLOC_MEMORY_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)系统分配内存失败。

#### OH_CommonEvent_UnSubscribe()

```ets
CommonEvent_ErrCode OH_CommonEvent_UnSubscribe(const CommonEvent_Subscriber* subscriber)
```

**描述**

退订公共事件。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber订阅者。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数subscriber无效。

 返回[COMMONEVENT_ERR_SENDING_REQUEST_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示IPC请求发送失败。

 返回[COMMONEVENT_ERR_INIT_UNDONE](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示公共事件服务未初始化。

#### OH_CommonEvent_GetEventFromRcvData()

```ets
const char* OH_CommonEvent_GetEventFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取当前接收的公共事件名称。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_RcvData](CommonEvent_RcvData.md)* rcvData公共事件回调数据。

**返回：**

类型说明const char*返回事件名称。

#### OH_CommonEvent_GetCodeFromRcvData()

```ets
int32_t OH_CommonEvent_GetCodeFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取公共事件传递的数据，整数类型。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_RcvData](CommonEvent_RcvData.md)* rcvData公共事件回调数据。

**返回：**

类型说明int32_t返回公共事件传递的数据，整数类型。

#### OH_CommonEvent_GetDataStrFromRcvData()

```ets
const char* OH_CommonEvent_GetDataStrFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取公共事件传递的数据，字符串类型。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_RcvData](CommonEvent_RcvData.md)* rcvData公共事件回调数据。

**返回：**

类型说明const char*返回公共事件传递的数据，字符串类型。

#### OH_CommonEvent_GetBundleNameFromRcvData()

```ets
const char* OH_CommonEvent_GetBundleNameFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取接收到的公共事件的包名称信息。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_RcvData](CommonEvent_RcvData.md)* rcvData公共事件回调数据。

**返回：**

类型说明const char*返回公共事件的包名称。

#### OH_CommonEvent_GetParametersFromRcvData()

```ets
const CommonEvent_Parameters* OH_CommonEvent_GetParametersFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取公共事件附加信息。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_RcvData](CommonEvent_RcvData.md)* rcvData公共事件回调数据。

**返回：**

类型说明const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)*返回公共事件附加信息。

#### OH_CommonEvent_CreatePublishInfo()

```ets
CommonEvent_PublishInfo* OH_CommonEvent_CreatePublishInfo(bool ordered)
```

**描述**

创建公共事件属性对象。

**起始版本：** 18

**参数：**

参数项描述bool ordered

是否为有序公共事件。

 - true：有序公共事件。

 - false：无序公共事件。

**返回：**

类型说明[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)*创建的公共事件属性对象，创建失败时，返回null。

#### OH_CommonEvent_DestroyPublishInfo()

```ets
void OH_CommonEvent_DestroyPublishInfo(CommonEvent_PublishInfo* info)
```

**描述**

销毁公共事件属性对象。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)* info要销毁的公共事件属性对象。

#### OH_CommonEvent_SetPublishInfoBundleName()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoBundleName(CommonEvent_PublishInfo* info, const char* bundleName)
```

**描述**

设置公共事件订阅者包名称。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)* info公共事件属性对象。const char* bundleName设置的订阅者包名称。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_SetPublishInfoPermissions()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoPermissions(CommonEvent_PublishInfo* info,const char* permissions[], int32_t num)
```

**描述**

设置公共事件订阅者权限。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)* info公共事件属性对象。const char* permissions[]订阅者权限名称数组，生效数量为num与permissions数组长度的最小值。int32_t num权限的数量。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_SetPublishInfoCode()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoCode(CommonEvent_PublishInfo* info, int32_t code)
```

**描述**

设置公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)* info公共事件属性对象。int32_t code公共事件传递的数据，整数类型。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_SetPublishInfoData()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoData(CommonEvent_PublishInfo* info,const char* data, size_t length)
```

**描述**

设置公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)* info公共事件属性对象。const char* data公共事件传递的数据，字符串类型，实际有效数据长度为length和data字符串长度的最小值。size_t length结果数据的长度。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_SetPublishInfoParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoParameters(CommonEvent_PublishInfo* info,CommonEvent_Parameters* param)
```

**描述**

设置公共事件附加信息。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)* info公共事件属性对象。CommonEvent_Parameters* param设置的附加信息。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_CreateParameters()

```ets
CommonEvent_Parameters* OH_CommonEvent_CreateParameters()
```

**描述**

创建公共事件附加信息对象。

**起始版本：** 18

**返回：**

类型说明[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)*返回公共事件附加信息，创建失败时，返回null。

#### OH_CommonEvent_DestroyParameters()

```ets
void OH_CommonEvent_DestroyParameters(CommonEvent_Parameters* param)
```

**描述**

销毁公共事件附加信息对象。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。

#### OH_CommonEvent_HasKeyInParameters()

```ets
bool OH_CommonEvent_HasKeyInParameters(const CommonEvent_Parameters* para, const char* key)
```

**描述**

检查附加信息中是否包含键值对信息。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。

**返回：**

类型说明bool

返回数据键是否存在。

 - true：存在。

 - false：不存在。

#### OH_CommonEvent_GetIntFromParameters()

```ets
int OH_CommonEvent_GetIntFromParameters(const CommonEvent_Parameters* para, const char* key, const int defaultValue)
```

**描述**

获取公共事件附加信息中键为key的int类型内容。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。const int defaultValue默认值。

**返回：**

类型说明int返回查询的int类型数据。

#### OH_CommonEvent_SetIntToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetIntToParameters(CommonEvent_Parameters* param, const char* key, int value)
```

**描述**

设置公共事件附加信息的int类型内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。int value设置的int类型内容。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_GetIntArrayFromParameters()

```ets
int32_t OH_CommonEvent_GetIntArrayFromParameters(const CommonEvent_Parameters* para, const char* key, int** array)
```

**描述**

获取公共事件附加信息中键为key的int数组数据。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。int** array查询的数组。

**返回：**

类型说明int32_t返回查询的数组长度，默认值为0。

#### OH_CommonEvent_SetIntArrayToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetIntArrayToParameters(CommonEvent_Parameters* param, const char* key,const int* value, size_t num)
```

**描述**

设置公共事件附加信息的int数组内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。const int* value设置的int数组内容。size_t num设置的int数组内容中元素的个数。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

 返回[COMMONEVENT_ERR_ALLOC_MEMORY_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示内存分配失败。

#### OH_CommonEvent_GetLongFromParameters()

```ets
long OH_CommonEvent_GetLongFromParameters(const CommonEvent_Parameters* para, const char* key, const long defaultValue)
```

**描述**

获取公共事件附加信息中键为key的long类型数据。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。const long defaultValue默认值。

**返回：**

类型说明long返回查询的long类型数据。

#### OH_CommonEvent_SetLongToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetLongToParameters(CommonEvent_Parameters* param, const char* key, long value)
```

**描述**

设置公共事件附加信息的long类型内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。long value设置的long类型内容。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_GetLongArrayFromParameters()

```ets
int32_t OH_CommonEvent_GetLongArrayFromParameters(const CommonEvent_Parameters* para, const char* key, long** array)
```

**描述**

获取公共事件附加信息的long数组内容。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。long** array查询的数组。

**返回：**

类型说明int32_t返回查询的数组长度，默认值为0。

#### OH_CommonEvent_SetLongArrayToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetLongArrayToParameters(CommonEvent_Parameters* param, const char* key,const long* value, size_t num)
```

**描述**

设置公共事件附加信息的long数组内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。const long* value设置的long数组内容。size_t num设置的long数组内容中元素的个数。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

 返回[COMMONEVENT_ERR_ALLOC_MEMORY_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示内存分配失败。

#### OH_CommonEvent_GetBoolFromParameters()

```ets
bool OH_CommonEvent_GetBoolFromParameters(const CommonEvent_Parameters* para, const char* key, const bool defaultValue)
```

**描述**

获取公共事件附加信息中键为key的布尔类型数据。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。const bool defaultValue默认值。

**返回：**

类型说明bool返回查询的bool类型数据。

#### OH_CommonEvent_SetBoolToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetBoolToParameters(CommonEvent_Parameters* param, const char* key, bool value)
```

**描述**

设置公共事件附加信息的布尔类型内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。bool value设置的布尔类型内容。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_GetBoolArrayFromParameters()

```ets
int32_t OH_CommonEvent_GetBoolArrayFromParameters(const CommonEvent_Parameters* para, const char* key, bool** array)
```

**描述**

获取公共事件附加信息的布尔数组内容。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。bool** array查询的数组。

**返回：**

类型说明int32_t返回查询的数组长度，默认值为0。

#### OH_CommonEvent_SetBoolArrayToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetBoolArrayToParameters(CommonEvent_Parameters* param, const char* key,const bool* value, size_t num)
```

**描述**

设置公共事件附加信息的布尔数组内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。const bool* value设置的布尔数组内容。size_t num设置的布尔数组内容中元素的个数。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

 返回[COMMONEVENT_ERR_ALLOC_MEMORY_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示内存分配失败。

#### OH_CommonEvent_GetCharFromParameters()

```ets
char OH_CommonEvent_GetCharFromParameters(const CommonEvent_Parameters* para, const char* key, const char defaultValue)
```

**描述**

获取公共事件附加信息中键为key的字符类型数据。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。const char defaultValue默认值。

**返回：**

类型说明char返回查询的char类型数据。

#### OH_CommonEvent_SetCharToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetCharToParameters(CommonEvent_Parameters* param, const char* key, char value)
```

**描述**

设置公共事件附加信息的字符类型内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。char value设置的字符类型内容。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_GetCharArrayFromParameters()

```ets
int32_t OH_CommonEvent_GetCharArrayFromParameters(const CommonEvent_Parameters* para, const char* key, char** array)
```

**描述**

获取公共事件附加信息的字符数组内容。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。char** array查询的数组。

**返回：**

类型说明int32_t返回查询的数组长度，默认值为0。

#### OH_CommonEvent_SetCharArrayToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetCharArrayToParameters(CommonEvent_Parameters* param, const char* key,const char* value, size_t num)
```

**描述**

设置公共事件附加信息的字符数组内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。const char* value设置的字符数组内容。size_t num设置的字符数组内容中元素的个数。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_GetDoubleFromParameters()

```ets
double OH_CommonEvent_GetDoubleFromParameters(const CommonEvent_Parameters* para, const char* key,const double defaultValue)
```

**描述**

获取公共事件附加信息的double类型内容。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。const double defaultValue默认值。

**返回：**

类型说明double返回查询的double类型数据。

#### OH_CommonEvent_SetDoubleToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetDoubleToParameters(CommonEvent_Parameters* param, const char* key,double value)
```

**描述**

设置公共事件附加信息的double类型内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。double value设置的double类型内容。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

#### OH_CommonEvent_GetDoubleArrayFromParameters()

```ets
int32_t OH_CommonEvent_GetDoubleArrayFromParameters(const CommonEvent_Parameters* para, const char* key,double** array)
```

**描述**

获取公共事件附加信息中键为key的double数组数据。

**起始版本：** 12

**参数：**

参数项描述const [CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* para公共事件附加信息。const char* key数据键。double** array查询的数组。

**返回：**

类型说明int32_t返回查询的数组长度，默认值为0。

#### OH_CommonEvent_SetDoubleArrayToParameters()

```ets
CommonEvent_ErrCode OH_CommonEvent_SetDoubleArrayToParameters(CommonEvent_Parameters* param, const char* key,const double* value, size_t num)
```

**描述**

设置公共事件附加信息的double数组内容。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Parameters](#ZH-CN_TOPIC_0000002529445495__变量)* param公共事件附加信息。const char* key数据键。const double* value设置的double数组内容。size_t num设置的double数组内容中元素的个数。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

 返回[COMMONEVENT_ERR_ALLOC_MEMORY_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示内存分配失败。

#### OH_CommonEvent_Publish()

```ets
CommonEvent_ErrCode OH_CommonEvent_Publish(const char* event)
```

**描述**

发布公共事件。

**起始版本：** 18

**参数：**

参数项描述const char* event公共事件名称。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

 返回[COMMONEVENT_ERR_SENDING_LIMIT_EXCEEDED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示事件发送频率过高。

 返回[COMMONEVENT_ERR_SENDING_REQUEST_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示IPC请求发送失败。

 返回[COMMONEVENT_ERR_INIT_UNDONE](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示公共事件服务未初始化。

#### OH_CommonEvent_PublishWithInfo()

```ets
CommonEvent_ErrCode OH_CommonEvent_PublishWithInfo(const char* event, const CommonEvent_PublishInfo* info)
```

**描述**

发布带有指定属性的公共事件。

**起始版本：** 18

**参数：**

参数项描述const char* event公共事件名称。const [CommonEvent_PublishInfo](CommonEvent_PublishInfo.md)* info设置的公共事件属性。

**返回：**

类型说明[CommonEvent_ErrCode](#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)

返回错误码。

 返回[COMMONEVENT_ERR_OK](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示成功。

 返回[COMMONEVENT_ERR_INVALID_PARAMETER](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示参数错误。

 返回[COMMONEVENT_ERR_SENDING_LIMIT_EXCEEDED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示事件发送频率过高。

 返回[COMMONEVENT_ERR_SENDING_REQUEST_FAILED](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示IPC请求发送失败。

 返回[COMMONEVENT_ERR_INIT_UNDONE](oh_commonevent.h.md#ZH-CN_TOPIC_0000002529445495__commonevent_errcode)表示公共事件服务未初始化。

#### OH_CommonEvent_IsOrderedCommonEvent()

```ets
bool OH_CommonEvent_IsOrderedCommonEvent(const CommonEvent_Subscriber* subscriber)
```

**描述**

查询当前公共事件是否为有序公共事件。

**起始版本：** 18

**参数：**

参数项描述const [CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。

**返回：**

类型说明bool返回true表示有序公共事件；返回false表示无序公共事件。

#### OH_CommonEvent_FinishCommonEvent()

```ets
bool OH_CommonEvent_FinishCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

用于订阅者结束对当前有序公共事件的处理。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。

**返回：**

类型说明bool返回true表示操作成功；返回false表示操作失败。

#### OH_CommonEvent_GetAbortCommonEvent()

```ets
bool OH_CommonEvent_GetAbortCommonEvent(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取当前有序公共事件是否处于中止状态。

**起始版本：** 18

**参数：**

参数项描述const [CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。

**返回：**

类型说明bool返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。

#### OH_CommonEvent_AbortCommonEvent()

```ets
bool OH_CommonEvent_AbortCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

该接口与[OH_CommonEvent_FinishCommonEvent](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。

**返回：**

类型说明bool返回true表示操作成功；返回false表示操作失败。

#### OH_CommonEvent_ClearAbortCommonEvent()

```ets
bool OH_CommonEvent_ClearAbortCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

该接口与[OH_CommonEvent_FinishCommonEvent](#ZH-CN_TOPIC_0000002529445495__oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。

**返回：**

类型说明bool返回true表示操作成功；返回false表示操作失败。

#### OH_CommonEvent_GetCodeFromSubscriber()

```ets
int32_t OH_CommonEvent_GetCodeFromSubscriber(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取有序公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

参数项描述const [CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。

**返回：**

类型说明int32_t返回有序公共事件传递的数据，整数类型，无法获取时返回0。

#### OH_CommonEvent_SetCodeToSubscriber()

```ets
bool OH_CommonEvent_SetCodeToSubscriber(CommonEvent_Subscriber* subscriber, int32_t code)
```

**描述**

设置有序公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。int32_t code有序公共事件传递的数据，整数类型。

**返回：**

类型说明bool返回true表示操作成功；返回false表示操作失败。

#### OH_CommonEvent_GetDataFromSubscriber()

```ets
const char* OH_CommonEvent_GetDataFromSubscriber(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取有序公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

参数项描述const [CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。

**返回：**

类型说明const char*返回有序公共事件传递的数据，字符串类型，无法获取时返回null。

#### OH_CommonEvent_SetDataToSubscriber()

```ets
bool OH_CommonEvent_SetDataToSubscriber(CommonEvent_Subscriber* subscriber, const char* data, size_t length)
```

**描述**

设置有序公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

参数项描述[CommonEvent_Subscriber](#ZH-CN_TOPIC_0000002529445495__变量)* subscriber公共事件的订阅者对象。const char* data有序公共事件传递的数据，字符串类型，实际有效数据长度为length与data字符串长度的较小值。size_t length数据的长度。

**返回：**

类型说明bool返回true表示操作成功；返回false表示操作失败。