# net_connection.h

#### 概述

为网络管理数据网络连接模块提供C接口。

**引用文件：** <network/netmanager/net_connection.h>

**库：** libnet_connection.so

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

#### 汇总

#### 函数

名称描述[int32_t OH_NetConn_HasDefaultNet(int32_t *hasDefaultNet)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_hasdefaultnet)查询是否有默认激活的数据网络。[int32_t OH_NetConn_GetDefaultNet(NetConn_NetHandle *netHandle)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_getdefaultnet)获取激活的默认的数据网络。[int32_t OH_NetConn_IsDefaultNetMetered(int32_t *isMetered)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_isdefaultnetmetered)查询默认网络是否按流量计费。[int32_t OH_NetConn_GetConnectionProperties(NetConn_NetHandle *netHandle, NetConn_ConnectionProperties *prop)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_getconnectionproperties)查询某个数据网络的链路信息。[int32_t OH_NetConn_GetNetCapabilities(NetConn_NetHandle *netHandle, NetConn_NetCapabilities *netCapabilities)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_getnetcapabilities)查询某个网络的能力集。[int32_t OH_NetConn_GetDefaultHttpProxy(NetConn_HttpProxy *httpProxy)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_getdefaulthttpproxy)查询默认的网络代理。[int32_t OH_NetConn_GetAddrInfo(char *host, char *serv, struct addrinfo *hint, struct addrinfo **res, int32_t netId)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_getaddrinfo)通过netId获取DNS结果。[int32_t OH_NetConn_FreeDnsResult(struct addrinfo *res)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_freednsresult)释放DNS结果。[int32_t OH_NetConn_GetAllNets(NetConn_NetHandleList *netHandleList)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_getallnets)查询所有激活的数据网络。[int32_t OHOS_NetConn_RegisterDnsResolver(OH_NetConn_CustomDnsResolver resolver)](#ZH-CN_TOPIC_0000002497445478__ohos_netconn_registerdnsresolver)注册自定义DNS解析器。[int32_t OHOS_NetConn_UnregisterDnsResolver(void)](#ZH-CN_TOPIC_0000002497445478__ohos_netconn_unregisterdnsresolver)取消注册自定义DNS解析器。[int32_t OH_NetConn_RegisterDnsResolver(OH_NetConn_CustomDnsResolver resolver)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_registerdnsresolver)注册自定义DNS解析器。[int32_t OH_NetConn_UnregisterDnsResolver(void)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_unregisterdnsresolver)取消注册自定义DNS解析器。[int32_t OH_NetConn_BindSocket(int32_t socketFd, NetConn_NetHandle *netHandle)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_bindsocket)将套接字绑定到特定的网络。[int32_t OH_NetConn_SetAppHttpProxy(NetConn_HttpProxy *httpProxy)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_setapphttpproxy)为当前应用设置http代理配置信息。[int32_t OH_NetConn_RegisterAppHttpProxyCallback(OH_NetConn_AppHttpProxyChange appHttpProxyChange, uint32_t *callbackId)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_registerapphttpproxycallback)注册监听应用http代理变化的回调。[void OH_NetConn_UnregisterAppHttpProxyCallback(uint32_t callbackId)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_unregisterapphttpproxycallback)注销监听应用http代理变化的回调。[int32_t OH_NetConn_RegisterNetConnCallback(NetConn_NetSpecifier *specifier, NetConn_NetConnCallback *netConnCallback,uint32_t timeout, uint32_t *callbackId)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_registernetconncallback)注册监听网络状态变化的回调。[int32_t OH_NetConn_RegisterDefaultNetConnCallback(NetConn_NetConnCallback *netConnCallback, uint32_t *callbackId)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_registerdefaultnetconncallback)注册监听默认网络状态变化的回调。[int32_t OH_NetConn_UnregisterNetConnCallback(uint32_t callBackId)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_unregisternetconncallback)注销监听网络状态变化的回调。[NetConn_ErrorCode OH_NetConn_SetPacUrl(const char *pacUrl)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_setpacurl)设置系统级代理自动配置（PAC）脚本地址。[NetConn_ErrorCode OH_NetConn_GetPacUrl(char *pacUrl)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_getpacurl)获取系统级代理自动配置（PAC）脚本地址。[int32_t OH_NetConn_QueryProbeResult(char *destination, int32_t duration, NetConn_ProbeResultInfo *probeResultInfo)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_queryproberesult)查询网络探测结果。[int32_t OH_NetConn_QueryTraceRoute(char *destination, NetConn_TraceRouteOption *option,NetConn_TraceRouteInfo *traceRouteInfo)](#ZH-CN_TOPIC_0000002497445478__oh_netconn_querytraceroute)查询网络跟踪路由。

#### 函数说明

#### OH_NetConn_HasDefaultNet()

```ets
int32_t OH_NetConn_HasDefaultNet(int32_t *hasDefaultNet)
```

**描述**

查询是否有默认激活的数据网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 11

**参数：**

参数项描述int32_t *hasDefaultNet是否有默认网络。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误。 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_GetDefaultNet()

```ets
int32_t OH_NetConn_GetDefaultNet(NetConn_NetHandle *netHandle)
```

**描述**

获取激活的默认的数据网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 11

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle存放网络ID。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误。 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_IsDefaultNetMetered()

```ets
int32_t OH_NetConn_IsDefaultNetMetered(int32_t *isMetered)
```

**描述**

查询默认数据网络是否计流量。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 11

**参数：**

参数项描述int32_t *isMetered是否激活。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误。 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_GetConnectionProperties()

```ets
int32_t OH_NetConn_GetConnectionProperties(NetConn_NetHandle *netHandle, NetConn_ConnectionProperties *prop)
```

**描述**

查询某个数据网络的链路信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 11

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle存放网络ID。[NetConn_ConnectionProperties](NetConn_ConnectionProperties.md) *prop存放链路信息。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误。 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_GetNetCapabilities()

```ets
int32_t OH_NetConn_GetNetCapabilities(NetConn_NetHandle *netHandle, NetConn_NetCapabilities *netCapabilities)
```

**描述**

查询某个网络的能力集。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 11

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle存放网络ID。[NetConn_NetCapabilities](NetConn_NetCapabilities.md) *netCapabilities存放能力集。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误. 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_GetDefaultHttpProxy()

```ets
int32_t OH_NetConn_GetDefaultHttpProxy(NetConn_HttpProxy *httpProxy)
```

**描述**

查询默认的网络代理。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**参数：**

参数项描述[NetConn_HttpProxy](NetConn_HttpProxy.md) *httpProxy存放代理配置信息。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误. 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_GetAddrInfo()

```ets
int32_t OH_NetConn_GetAddrInfo(char *host, char *serv, struct addrinfo *hint, struct addrinfo **res, int32_t netId)
```

**描述**

通过netId获取DNS结果。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

参数项描述char *host所需查询的host名。char *serv服务名。struct addrinfo *hint指向addrinfo结构体的指针。struct addrinfo **res存放DNS查询结果，以链表形式返回。int32_t netIdDNS查询netId为0时，使用默认netid查询。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误。 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_FreeDnsResult()

```ets
int32_t OH_NetConn_FreeDnsResult(struct addrinfo *res)
```

**描述**

释放DNS结果。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

参数项描述struct addrinfo *resDNS查询结果链表头。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误。 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_GetAllNets()

```ets
int32_t OH_NetConn_GetAllNets(NetConn_NetHandleList *netHandleList)
```

**描述**

查询所有激活的数据网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 11

**参数：**

参数项描述[NetConn_NetHandleList](NetConn_NetHandleList.md) *netHandleList网络信息列表。

**返回：**

类型说明int32_t

0 - 成功。 201 - 缺少权限。

 401 - 参数错误。 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OHOS_NetConn_RegisterDnsResolver()

```ets
int32_t OHOS_NetConn_RegisterDnsResolver(OH_NetConn_CustomDnsResolver resolver)
```

**描述**

注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**废弃版本：** 13

**替代接口：** OH_NetConn_RegisterDnsResolver

**参数：**

参数项描述[OH_NetConn_CustomDnsResolver](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_customdnsresolver) resolver指向自定义DNS解析器的指针。

**返回：**

类型说明int32_t

0 - 成功。 401 - 参数错误。

 2100002 - 无法连接到服务。 2100003 - 内部错误。

#### OHOS_NetConn_UnregisterDnsResolver()

```ets
int32_t OHOS_NetConn_UnregisterDnsResolver(void)
```

**描述**

取消注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**废弃版本：** 13

**替代接口：** OH_NetConn_UnregisterDnsResolver

**返回：**

类型说明int32_t

0 - 成功。

2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_RegisterDnsResolver()

```ets
int32_t OH_NetConn_RegisterDnsResolver(OH_NetConn_CustomDnsResolver resolver)
```

**描述**

注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 13

**参数：**

参数项描述[OH_NetConn_CustomDnsResolver](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_customdnsresolver) resolver指向自定义DNS解析器的指针。

**返回：**

类型说明int32_t

返回结果码。

 NETMANAGER_EXT_SUCCESS 如果操作成功。

 NETMANAGER_ERR_PARAMETER_ERROR 参数错误。请输入正确的参数。

#### OH_NetConn_UnregisterDnsResolver()

```ets
int32_t OH_NetConn_UnregisterDnsResolver(void)
```

**描述**

取消注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 13

**返回：**

类型说明int32_t

0 - 成功。

 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_BindSocket()

```ets
int32_t OH_NetConn_BindSocket(int32_t socketFd, NetConn_NetHandle *netHandle)
```

**描述**

将套接字绑定到特定的网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

参数项描述int32_t socketFd由用户构造的套接字。[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle指针类型，指向包含网络ID的网络句柄。

**返回：**

类型说明int32_t

0 - 成功。

 401 - 参数错误。

 2100002 - 无法连接到服务。

 2100003 - 内部错误。

#### OH_NetConn_SetAppHttpProxy()

```ets
int32_t OH_NetConn_SetAppHttpProxy(NetConn_HttpProxy *httpProxy)
```

**描述**

为当前应用设置http代理配置信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

参数项描述[NetConn_HttpProxy](NetConn_HttpProxy.md) *httpProxy需要设置的http代理配置信息。

**返回：**

类型说明int32_t

0 - 成功。

 401 - 参数错误。

#### OH_NetConn_RegisterAppHttpProxyCallback()

```ets
int32_t OH_NetConn_RegisterAppHttpProxyCallback(OH_NetConn_AppHttpProxyChange appHttpProxyChange, uint32_t *callbackId)
```

**描述**

注册监听应用http代理变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

参数项描述[OH_NetConn_AppHttpProxyChange](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_apphttpproxychange) appHttpProxyChange需要注册的监听回调。uint32_t *callbackId回调注册后生成的id, 关联已注册的回调。

**返回：**

类型说明int32_t

0 - 成功。

 401 - 参数错误。

#### OH_NetConn_UnregisterAppHttpProxyCallback()

```ets
void OH_NetConn_UnregisterAppHttpProxyCallback(uint32_t callbackId)
```

**描述**

注销监听应用http代理变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

参数项描述uint32_t callbackId需要被注销的回调所对应的id。

#### OH_NetConn_RegisterNetConnCallback()

```ets
int32_t OH_NetConn_RegisterNetConnCallback(NetConn_NetSpecifier *specifier, NetConn_NetConnCallback *netConnCallback,uint32_t timeout, uint32_t *callbackId)
```

**描述**

注册监听网络状态变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 12

**参数：**

参数项描述netSpecifier网络特征集。callback注册的回调函数集合。uint32_t timeout超时时间，单位为毫秒，为0时表示无限等待。uint32_t *callbackId出参，对应本次注册成功的回调。

**返回：**

类型说明int32_t

0 - 成功。

 201 - 缺少权限。

 401 - 参数错误。

 2100002 - 无法连接到服务。

 2100003 - 内部错误。

 2101008 - 回调已注册。

 2101022 - 请求数超出了允许的最大值。

#### OH_NetConn_RegisterDefaultNetConnCallback()

```ets
int32_t OH_NetConn_RegisterDefaultNetConnCallback(NetConn_NetConnCallback *netConnCallback, uint32_t *callbackId)
```

**描述**

注册监听默认网络状态变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 12

**参数：**

参数项描述callback注册的回调函数集合。uint32_t *callbackId出参，对应本次注册成功的回调。

**返回：**

类型说明int32_t

0 - 成功。

 201 - 缺少权限。

 401 - 参数错误。

 2100002 - 无法连接到服务。

 2100003 - 内部错误。

 2101008 - 回调已注册。

 2101022 - 请求数超出了允许的最大值。

#### OH_NetConn_UnregisterNetConnCallback()

```ets
int32_t OH_NetConn_UnregisterNetConnCallback(uint32_t callBackId)
```

**描述**

注销监听网络状态变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 12

**参数：**

参数项描述uint32_t callBackId需要被注销的回调对应id。

**返回：**

类型说明int32_t

0 - 成功。

 201 - 缺少权限。

 401 - 参数错误。

 2100002 - 无法连接到服务。

 2100003 - 内部错误。

 2101007 - 回调不存在。

#### OH_NetConn_SetPacUrl()

```ets
NetConn_ErrorCode OH_NetConn_SetPacUrl(const char *pacUrl)
```

**描述**

设置当前PAC脚本（Proxy Auto-Configuration Script，代理自动配置脚本）的URL地址，比如：[http://127.0.0.1:21998/PacProxyScript.pac。通过解析脚本地址可以获取代理信息。](http://127.0.0.1:21998/PacProxyScript.pac。通过解析脚本地址可以获取代理信息。)

**需要权限：** ohos.permission.SET_PAC_URL

**起始版本：** 15

**参数：**

参数项描述const char *pacUrl需要设置的PAC脚本地址。

**返回：**

类型说明[NetConn_ErrorCode](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode)

结果定义在 [NetConn_ErrorCode](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode)。

[NETCONN_SUCCESS](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 成功。

[NETCONN_PERMISSION_DENIED](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 缺少权限。

[NETCONN_PARAMETER_ERROR](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 参数错误。

[NETCONN_OPERATION_FAILED](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 无法连接到服务。

[NETCONN_INTERNAL_ERROR](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 内部错误。

#### OH_NetConn_GetPacUrl()

```ets
NetConn_ErrorCode OH_NetConn_GetPacUrl(char *pacUrl)
```

**描述**

获取系统级代理自动配置（PAC）脚本地址。

**起始版本：** 15

**参数：**

参数项描述char *pacUrl获取的PAC脚本地址。

**返回：**

类型说明[NetConn_ErrorCode](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode)

结果定义在 [NetConn_ErrorCode](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode)。

[NETCONN_SUCCESS](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 成功。

[NETCONN_PARAMETER_ERROR](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 参数错误。

[NETCONN_OPERATION_FAILED](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 无法连接到服务。

[NETCONN_INTERNAL_ERROR](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_errorcode) 内部错误。

#### OH_NetConn_QueryProbeResult()

```ets
int32_t OH_NetConn_QueryProbeResult(char *destination, int32_t duration, NetConn_ProbeResultInfo *probeResultInfo)
```

**描述**

查询网络探测结果。

**需要权限：** ohos.permission.INTERNET

**起始版本：** 20

**参数：**

参数项描述char *destination目的地址。int32_t duration探测持续时间。单位：秒。[NetConn_ProbeResultInfo](NetConn_ProbeResultInfo.md) *probeResultInfo丢包率和往返时间（RTT）。

**返回：**

类型说明int32_t

0 - 成功。

 201 - 缺少权限。

 401 - 参数错误。

 2100003 - 内部错误。

#### OH_NetConn_QueryTraceRoute()

```ets
int32_t OH_NetConn_QueryTraceRoute(char *destination, NetConn_TraceRouteOption *option,NetConn_TraceRouteInfo *traceRouteInfo)
```

**描述**

查询网络跟踪路由。

**需要权限：** ohos.permission.INTERNET、ohos.permission.LOCATION 和 ohos.permission.ACCESS_NET_TRACE_INFO

**起始版本：** 20

**参数：**

参数项描述char *destination目的地址。[NetConn_TraceRouteOption](NetConn_TraceRouteOption.md) *option路由参数选项。[NetConn_TraceRouteInfo](NetConn_TraceRouteInfo.md) *traceRouteInfo路由结果。需传入数组指针，数组大小代表路由跳数，默认30跳。若自定义跳数，则需保证数组大小与option字段中的maxJumpNumber数值保持一致。

**返回：**

类型说明int32_t

0 - 成功。

 201 - 缺少权限。