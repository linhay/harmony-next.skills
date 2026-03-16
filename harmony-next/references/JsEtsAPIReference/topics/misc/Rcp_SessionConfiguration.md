# Rcp_SessionConfiguration

#### 概述

会话配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_SessionType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4fa3aa6821b16425c260d837deace956)[type](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__aa8a73daba70f67827cac073d5d159de2)

会话类型。

[Rcp_InterceptorArray](../media/Rcp_InterceptorArray.md)[interceptors](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a1f3ed29c8781479e514020921933fa77)

用户自定义的异步拦截器数组。

[Rcp_SyncInterceptorArray](../media/Rcp_SyncInterceptorArray.md)[syncInterceptors](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a2ae808955d10d5fdf3bf91950ff8a2c9)

用户定义的同步拦截器数组。

const char * [baseUrl](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a8cb997b4f5fdcdf28aad95f975ed2a0c)

基本URL。

[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) * [headers](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a83eabab4e8f469be1d4fe9afa5a885e8)

请求标头。

[Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50) * [cookies](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a16b3f819c4b51898edb1da8cf6341752)

请求的Cookie。

[Rcp_SessionListener](../components/Rcp_SessionListener.md)[sessionListener](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a76757231607687f3c609d4563dfdd401)

回调函数，供session监听close()或cancel()事件。

[Rcp_Configuration](Rcp_Configuration.md) * [requestConfiguration](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__acdfb8368e9de0b0383286a082f90d973)

默认请求配置。这些选项可以通过**[Request.configuration](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__ac932aa050c8e51b76783f27a07273b05)**来覆盖。

[Rcp_ConnectionConfiguration](../networking/Rcp_ConnectionConfiguration.md)[connectionConfiguration](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a5867f7ed6493d37300c5146bf07b8e4a)

连接配置。

#### 结构体成员变量说明

#### baseUrl

```ets
const char* Rcp_SessionConfiguration::baseUrl
```

**描述**

基本URL。

举例， 如果请求的url为 '?name=value', 基本url是 '[https://example.com'](https://example.com')，那么最后当请求被送往服务端时的最终url为 '[https://example.com?name=value'](https://example.com?name=value')。

#### connectionConfiguration

```ets
[Rcp_ConnectionConfiguration](../networking/Rcp_ConnectionConfiguration.md) Rcp_SessionConfiguration::connectionConfiguration
```

**描述**

连接配置。

它用于指定此会话中允许的最大同时连接总数以及允许连接到单个主机的最大同时连接数。

#### cookies

```ets
[Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50)* Rcp_SessionConfiguration::cookies
```

**描述**

请求的Cookie。

如果调用了[HMS_Rcp_Fetch](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7ea546b69b9ea60ea4716ee64e8b04cb)或者[HMS_Rcp_FetchSync](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga48a83535a4658e9872ded4b0dd8c812f)，在参数中的[Rcp_Request](Rcp_Request.md)中没有[Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50)，则[Rcp_SessionConfiguration.cookies](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a16b3f819c4b51898edb1da8cf6341752)将是[Rcp_Request.cookies](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a4233d0d064ac2209accfb25a701047c9)，如果两者都存在，则将它们合并。

#### headers

```ets
[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982)* Rcp_SessionConfiguration::headers
```

**描述**

请求标头。

如果调用了[HMS_Rcp_Fetch](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7ea546b69b9ea60ea4716ee64e8b04cb)或[HMS_Rcp_FetchSync](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga48a83535a4658e9872ded4b0dd8c812f)，并且[Rcp_Request](Rcp_Request.md)中没有[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982)，[Rcp_SessionConfiguration.headers](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a83eabab4e8f469be1d4fe9afa5a885e8)将是[Rcp_Request.headers](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a4ebc6011dc454a18c04eca049f8e95cd)，如果两者都存在，则将它们合并。

#### interceptors

```ets
[Rcp_InterceptorArray](../media/Rcp_InterceptorArray.md) Rcp_SessionConfiguration::interceptors
```

**描述**

用户自定义的异步拦截器数组。

异步拦截器将被制成拦截器链。

输入: [A, B, C, D]， 处理逻辑将为 A->B->C->D->defaultHandler。

#### requestConfiguration

```ets
[Rcp_Configuration](Rcp_Configuration.md)* Rcp_SessionConfiguration::requestConfiguration
```

**描述**

默认请求配置。这些选项可以通过**Request.configuration**来覆盖。

#### sessionListener

```ets
[Rcp_SessionListener](../components/Rcp_SessionListener.md) Rcp_SessionConfiguration::sessionListener
```

**描述**

回调函数，供session监听close()或cancel()事件。

#### syncInterceptors

```ets
[Rcp_SyncInterceptorArray](../media/Rcp_SyncInterceptorArray.md) Rcp_SessionConfiguration::syncInterceptors
```

**描述**

用户定义的同步拦截器数组。

同步拦截器会被做成拦截器链。

输入: [A, B, C, D], 处理逻辑将为 A->B->C->D->defaultHandler。

#### type

```ets
[Rcp_SessionType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4fa3aa6821b16425c260d837deace956) Rcp_SessionConfiguration::type
```

**描述**

会话类型。