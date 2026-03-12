# ArkWeb_WebMessageAPI

```ets
typedef struct {...} ArkWeb_WebMessageAPI
```

#### 概述

Post Message数据相关的Native API结构体。在调用接口前建议通过[ARKWEB_MEMBER_MISSING](arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__宏定义)校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessage相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。

**起始版本：** 12

**相关模块：**[Web](Web.md)

**所在头文件：**[arkweb_type.h](arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述size_t size结构体的大小。

#### 成员函数

名称描述[ArkWeb_WebMessagePtr (*createWebMessage)()](#ZH-CN_TOPIC_0000002529285227__createwebmessage)创建消息。[void (*destroyWebMessage)(ArkWeb_WebMessagePtr* webMessage)](#ZH-CN_TOPIC_0000002529285227__destroywebmessage)销毁消息。[void (*setType)(ArkWeb_WebMessagePtr webMessage, ArkWeb_WebMessageType type)](#ZH-CN_TOPIC_0000002529285227__settype)设置消息类型。[ArkWeb_WebMessageType (*getType)(ArkWeb_WebMessagePtr webMessage)](#ZH-CN_TOPIC_0000002529285227__gettype)获取消息类型。[void (*setData)(ArkWeb_WebMessagePtr webMessage, void* data, size_t dataLength)](#ZH-CN_TOPIC_0000002529285227__setdata)设置数据。[void* (*getData)(ArkWeb_WebMessagePtr webMessage, size_t* dataLength)](#ZH-CN_TOPIC_0000002529285227__getdata)获取数据。

#### 成员函数说明

#### createWebMessage()

```ets
ArkWeb_WebMessagePtr (*createWebMessage)()
```

**描述**

创建消息。

**返回：**

类型说明[ArkWeb_WebMessagePtr](ArkWeb_WebMessage_.md)消息结构体。

#### destroyWebMessage()

```ets
void (*destroyWebMessage)(ArkWeb_WebMessagePtr* webMessage)
```

**描述**

销毁消息。

**参数：**

参数项描述[ArkWeb_WebMessagePtr](ArkWeb_WebMessage_.md)* webMessage需要销毁的消息。

#### setType()

```ets
void (*setType)(ArkWeb_WebMessagePtr webMessage, ArkWeb_WebMessageType type)
```

**描述**

设置消息类型。@param webMessage 消息结构体指针。@param type 消息类型。

**参数：**

参数项描述[ArkWeb_WebMessagePtr](ArkWeb_WebMessage_.md) webMessage消息结构体指针。[ArkWeb_WebMessageType](arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__arkweb_webmessagetype) type消息类型。

#### getType()

```ets
ArkWeb_WebMessageType (*getType)(ArkWeb_WebMessagePtr webMessage)
```

**描述**

获取消息类型。

**参数：**

参数项描述[ArkWeb_WebMessagePtr](ArkWeb_WebMessage_.md) webMessage消息结构体指针。

#### setData()

```ets
void (*setData)(ArkWeb_WebMessagePtr webMessage, void* data, size_t dataLength)
```

**描述**

设置数据。

**参数：**

参数项描述[ArkWeb_WebMessagePtr](ArkWeb_WebMessage_.md) webMessage消息结构体指针。void* data数据指针。size_t dataLength数据长度。

#### getData()

```ets
void* (*getData)(ArkWeb_WebMessagePtr webMessage, size_t* dataLength)
```

**描述**

获取数据。

**参数：**

参数项描述[ArkWeb_WebMessagePtr](ArkWeb_WebMessage_.md) webMessage消息结构体指针。size_t* dataLength出参，数据长度。

**返回：**

类型说明void*数据指针。