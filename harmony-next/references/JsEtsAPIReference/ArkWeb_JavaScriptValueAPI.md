# ArkWeb_JavaScriptValueAPI

```ets
typedef struct {...} ArkWeb_JavaScriptValueAPI
```

#### 概述

定义了ArkWeb的JavaScriptValue接口。在调用接口之前，建议使用[ARKWEB_MEMBER_MISSING](arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__宏定义)检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。

**起始版本：** 18

**相关模块：**[Web](Web.md)

**所在头文件：**[arkweb_type.h](arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述size_t size结构体的大小。

#### 成员函数

名称描述[ArkWeb_JavaScriptValuePtr (*createJavaScriptValue)(ArkWeb_JavaScriptValueType type, void* data, size_t dataLength)](#ZH-CN_TOPIC_0000002497605236__createjavascriptvalue)创建一个JavaScript值，用于返回给HTML。

#### 成员函数说明

#### createJavaScriptValue()

```ets
ArkWeb_JavaScriptValuePtr (*createJavaScriptValue)(ArkWeb_JavaScriptValueType type, void* data, size_t dataLength)
```

**描述：**

创建一个JavaScript值，用于返回给HTML。

**起始版本：** 18

**参数：**

参数项描述ArkWeb_JavaScriptValueType typeJavaScript值的类型。void* dataJavaScript值的数据缓冲区。size_t dataLengthJavaScript值的缓冲区大小。

**返回：**

类型说明[ArkWeb_JavaScriptValuePtr](ArkWeb_JavaScriptValue_.md)创建出来的JavaScript值。