# Rcp_Request

#### 概述

网络请求。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char [id](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a63dfa45000ae0a04ad62077593507ae8) [[RCP_MAX_REQUEST_ID_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga34b7468983f894581c9e908295c6d92e)]

每个请求的唯一ID。由系统生成。

char * [url](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a39a1cc0a1ad666d8d9ad40eec4b52de7)

请求URL。

const char * [method](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a7ed7d494ed73e3a6ee9ebc03703424ad)

请求方法。默认值为GET。

[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) * [headers](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a4ebc6011dc454a18c04eca049f8e95cd)

请求标头。

[Rcp_RequestContent](Rcp_RequestContent.md) * [content](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__ae1768fc61b69a42fcc051cc75e5b1267)

请求体。

[Rcp_Configuration](Rcp_Configuration.md) * [configuration](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__ac932aa050c8e51b76783f27a07273b05)

请求配置。请参见[Rcp_Configuration](Rcp_Configuration.md)。

[Rcp_TransferRange](Rcp_TransferRange.md) * [transferRange](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a165e2b6e37dc667cd91cb7393544d91b)

HTTP传输范围。该设置将转换为HTTP Range标头。

[Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50) * [cookies](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a4233d0d064ac2209accfb25a701047c9)

请求Cookie。该设置将转换为HTTP Cookie标头。

void * [requestPrivate](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a1685876d0e7dc370afbded8c9bc028b3)

可扩展字段。

#### 结构体成员变量说明

#### configuration

```ets
[Rcp_Configuration](Rcp_Configuration.md)* Rcp_Request::configuration
```

**描述**

请求配置。请参见[Rcp_Configuration](Rcp_Configuration.md)。

#### content

```ets
[Rcp_RequestContent](Rcp_RequestContent.md)* Rcp_Request::content
```

**描述**

请求体。

#### cookies

```ets
[Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50)* Rcp_Request::cookies
```

**描述**

请求Cookie。该设置将转换为HTTP Cookie标头。

#### headers

```ets
[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982)* Rcp_Request::headers
```

**描述**

请求标头。

#### id

```ets
char Rcp_Request::id[[RCP_MAX_REQUEST_ID_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga34b7468983f894581c9e908295c6d92e)]
```

**描述**

每个请求的唯一ID。由系统生成。

#### method

```ets
const char* Rcp_Request::method
```

**描述**

请求方法。默认值为GET。

#### requestPrivate

```ets
void* Rcp_Request::requestPrivate
```

**描述**

可扩展字段。

#### transferRange

```ets
[Rcp_TransferRange](Rcp_TransferRange.md)* Rcp_Request::transferRange
```

**描述**

HTTP传输范围。该设置将转换为HTTP Range标头。

#### url

```ets
char* Rcp_Request::url
```

**描述**

请求URL。