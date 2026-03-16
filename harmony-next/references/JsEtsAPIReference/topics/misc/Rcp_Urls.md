# Rcp_Urls

#### 概述

URLs，用于确定主机是否正在使用代理。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

const char * [url](Rcp_Urls.md#ZH-CN_TOPIC_0000002317039101__affd57b9b241b419c449bd85b6e881be2)

匹配的URL。

struct [Rcp_Urls](Rcp_Urls.md) * [next](Rcp_Urls.md#ZH-CN_TOPIC_0000002317039101__ab15dafafb47202da262f9bbb2f1c23bd)

链式存储。指向下一个[Rcp_Urls](Rcp_Urls.md)的指针。

#### 结构体成员变量说明

#### next

```ets
struct [Rcp_Urls](Rcp_Urls.md)* Rcp_Urls::next
```

**描述**

链式存储。指向下一个[Rcp_Urls](Rcp_Urls.md)的指针。

#### url

```ets
const char* Rcp_Urls::url
```

**描述**

匹配的URL。