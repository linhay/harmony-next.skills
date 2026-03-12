# Rcp_Exclusions

#### 概述

代理配置中用于过滤不使用代理的urls。

如果[Rcp_Request.url](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a39a1cc0a1ad666d8d9ad40eec4b52de7)匹配[Rcp_Exclusions](Rcp_Exclusions.md)规则，则[Rcp_Request](Rcp_Request.md)不会使用代理。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_ExclusionsValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga1f5ed8748d80bca8e803ea26d63d1ecf)[type](Rcp_Exclusions.md#ZH-CN_TOPIC_0000002317126025__adea8e4bddc87a6c451c94abbec909fbe)

表示union中使用的数据类型。

****union {

union结构。

[Rcp_Urls](Rcp_Urls.md) * [urls](Rcp_Exclusions.md#ZH-CN_TOPIC_0000002317126025__abd535558039767647290d03621389486)

Urls。链式存储url。

[Rcp_ExclusionFunction](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac6517b72e4a8c0feaf864f3669d2c127)[exclusionFunction](Rcp_Exclusions.md#ZH-CN_TOPIC_0000002317126025__ad99a237a7685adc45de3d3a728112922)

回调函数。通过回调函数过滤url。

} **data**

data中使用的数据由type进行区分。

#### 结构体成员变量说明

#### exclusionFunction

```ets
[Rcp_ExclusionFunction](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac6517b72e4a8c0feaf864f3669d2c127) Rcp_Exclusions::exclusionFunction
```

**描述**

通过回调过滤。

#### type

```ets
[Rcp_ExclusionsValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga1f5ed8748d80bca8e803ea26d63d1ecf) Rcp_Exclusions::type
```

**描述**

表示union中使用的数据类型。

#### urls

```ets
[Rcp_Urls](Rcp_Urls.md)* Rcp_Exclusions::urls
```

**描述**

Urls。