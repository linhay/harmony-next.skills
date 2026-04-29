# Rcp_TransferConfiguration

**概述**

传输配置。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| bool autoRedirect | 是否自动遵循HTTP重定向响应。默认为True。 |
| Rcp_Timeouttimeout | 超时配置。如果未设置此选项，将应用默认超时。 |
| bool assumesHTTP3Capable | 是否假定目标服务器支持HTTP/3。默认值为false。 |
| Rcp_PathPreferencepathPreference | 请求路径首选项。 |

**结构体成员变量说明**

**assumesHTTP3Capable**

```ets
bool Rcp_TransferConfiguration::assumesHTTP3Capable
```

描述

是否假定目标服务器支持HTTP/3。默认值为false。

**autoRedirect**

```ets
bool Rcp_TransferConfiguration::autoRedirect
```

描述

是否自动遵循HTTP重定向响应。默认为True。

**pathPreference**

```ets
Rcp_PathPreference Rcp_TransferConfiguration::pathPreference
```

描述

请求路径首选项。

**timeout**

```ets
Rcp_Timeout Rcp_TransferConfiguration::timeout
```

描述

超时配置。如果未设置此选项，将应用默认超时。如果已配置，则使用配置的超时时间。