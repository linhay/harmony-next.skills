# Rcp_FormFieldFileValue

#### 概述

表单字段文件值。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char [contentType](Rcp_FormFieldFileValue.md#ZH-CN_TOPIC_0000002282446454__a392fa25d67da5371742d2e837b582660) [[RCP_MAX_CONTENT_TYPE_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga994193494eac9591a85c49f1e3200930)]

多部分表单数据内容类型。

char [remoteFileName](Rcp_FormFieldFileValue.md#ZH-CN_TOPIC_0000002282446454__ac5dc6ae6cece1f6b6ecbab3f2fa65153) [[RCP_MAX_FILENAME_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaef0f15d9c2cacf9df70ba148cfff171b)]

多部分表单数据远程文件名。

[Rcp_ContentOrPathOrCallback](Rcp_ContentOrPathOrCallback.md)[contentOrPathOrCb](Rcp_FormFieldFileValue.md#ZH-CN_TOPIC_0000002282446454__ae23c275b9e2f237b5e4492f998a7e7e4)

多部分表单数据内容。

#### 结构体成员变量说明

#### contentOrPathOrCb

```ets
[Rcp_ContentOrPathOrCallback](Rcp_ContentOrPathOrCallback.md) Rcp_FormFieldFileValue::contentOrPathOrCb
```

**描述**

多部分表单数据内容。

#### contentType

```ets
char Rcp_FormFieldFileValue::contentType[[RCP_MAX_CONTENT_TYPE_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga994193494eac9591a85c49f1e3200930)]
```

**描述**

多部分表单数据内容类型。

#### remoteFileName

```ets
char Rcp_FormFieldFileValue::remoteFileName[[RCP_MAX_FILENAME_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaef0f15d9c2cacf9df70ba148cfff171b)]
```

**描述**

多部分表单数据远程文件名。