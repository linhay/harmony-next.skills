# ArkWeb_WebMessagePortAPI

```ets
typedef struct {...} ArkWeb_WebMessagePortAPI
```

#### 概述

Post Message相关的Native API结构体。在调用接口前建议通过[ARKWEB_MEMBER_MISSING](arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__宏定义)校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessagePort相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。

**起始版本：** 12

**相关模块：**[Web](Web.md)

**所在头文件：**[arkweb_type.h](arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述size_t size结构体的大小。

#### 成员函数

名称描述[ArkWeb_ErrorCode (*postMessage)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, const ArkWeb_WebMessagePtr webMessage)](#ZH-CN_TOPIC_0000002497445256__postmessage)发送消息到HTML。[void (*close)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag)](#ZH-CN_TOPIC_0000002497445256__close)关闭消息端口。[void (*setMessageEventHandler)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, ArkWeb_OnMessageEventHandler messageEventHandler, void* userData)](#ZH-CN_TOPIC_0000002497445256__setmessageeventhandler)设置接收HTML消息的回调。

#### 成员函数说明

#### postMessage()

```ets
ArkWeb_ErrorCode (*postMessage)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, const ArkWeb_WebMessagePtr webMessage)
```

**描述：**

发送消息到HTML。

**参数：**

参数项描述const [ArkWeb_WebMessagePortPtr](ArkWeb_WebMessagePort_.md) webMessagePortPost Message端口结构体指针。const char* webTagWeb组件名称。const [ArkWeb_WebMessagePtr](ArkWeb_WebMessage_.md) webMessage需要发送的消息。

**返回：**

类型说明[ArkWeb_ErrorCode](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode)

[ARKWEB_SUCCESS](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) 执行成功。

[ARKWEB_INVALID_PARAM](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) 参数无效。

[ARKWEB_INIT_ERROR](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) 初始化失败，没有找到与webTag绑定的Web组件。

#### close()

```ets
void (*close)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag)
```

**描述：**

关闭消息端口。

**参数：**

参数项描述const [ArkWeb_WebMessagePortPtr](ArkWeb_WebMessagePort_.md) webMessagePortPost Message端口结构体指针。const char* webTagWeb组件名称。

#### setMessageEventHandler()

```ets
void (*setMessageEventHandler)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag,
        ArkWeb_OnMessageEventHandler messageEventHandler, void* userData)
```

**描述：**

设置接收HTML消息的回调。

**参数：**

参数项描述const [ArkWeb_WebMessagePortPtr](ArkWeb_WebMessagePort_.md) webMessagePortPost Message端口结构体指针。const char* webTagWeb组件名称。[ArkWeb_OnMessageEventHandler](arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__arkweb_onmessageeventhandler) messageEventHandler处理消息的回调。void* userData用户自定义数据。