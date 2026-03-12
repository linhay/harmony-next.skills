# net_connection_type.h

#### 概述

为网络管理数据网络连接模块提供C接口。

**引用文件：** <network/netmanager/net_connection_type.h>

**库：** libnet_connection.so

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

#### 汇总

#### 结构体

名称typedef关键字描述[NetConn_NetHandle](NetConn_NetHandle.md)NetConn_NetHandle存放网络ID。[NetConn_NetCapabilities](NetConn_NetCapabilities.md)NetConn_NetCapabilities网络能力集。[NetConn_NetAddr](NetConn_NetAddr.md)NetConn_NetAddr网络地址。[NetConn_Route](NetConn_Route.md)NetConn_Route路由配置信息。[NetConn_HttpProxy](NetConn_HttpProxy.md)NetConn_HttpProxy代理配置信息。[NetConn_ConnectionProperties](NetConn_ConnectionProperties.md)NetConn_ConnectionProperties网络链接信息。[NetConn_NetHandleList](NetConn_NetHandleList.md)NetConn_NetHandleList网络列表。[NetConn_NetSpecifier](NetConn_NetSpecifier.md)NetConn_NetSpecifier网络的特征集。[NetConn_NetConnCallback](NetConn_NetConnCallback.md)NetConn_NetConnCallback网络状态监听回调集合。[NetConn_ProbeResultInfo](NetConn_ProbeResultInfo.md)NetConn_ProbeResultInfo定义探测结果信息。[NetConn_TraceRouteOption](NetConn_TraceRouteOption.md)NetConn_TraceRouteOption定义网络跟踪路由选项。[NetConn_TraceRouteInfo](NetConn_TraceRouteInfo.md)NetConn_TraceRouteInfo定义跟踪路由信息。

#### 枚举

名称typedef关键字描述[NetConn_NetCap](#ZH-CN_TOPIC_0000002529285449__netconn_netcap)NetConn_NetCap网络能力集。[NetConn_NetBearerType](#ZH-CN_TOPIC_0000002529285449__netconn_netbearertype)NetConn_NetBearerType网络载体类型。[NetConn_ErrorCode](#ZH-CN_TOPIC_0000002529285449__netconn_errorcode)NetConn_ErrorCode网络连接返回值错误码。[NetConn_PacketsType](#ZH-CN_TOPIC_0000002529285449__netconn_packetstype)NetConn_PacketsType枚举跟踪路由的数据包类型。

#### 宏定义

名称描述**NETCONN_MAX_RTT_NUM**4**NETCONN_MAX_NET_SIZE**32**NETCONN_MAX_BEARER_TYPE_SIZE**32**NETCONN_MAX_CAP_SIZE**32**NETCONN_MAX_ADDR_SIZE**32**NETCONN_MAX_ROUTE_SIZE**64**NETCONN_MAX_EXCLUSION_SIZE**256**NETCONN_MAX_STR_LEN**256

#### 函数

名称typedef关键字描述[typedef int (*OH_NetConn_CustomDnsResolver)(const char *host, const char *serv,const struct addrinfo *hint, struct addrinfo **res)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_customdnsresolver)OH_NetConn_CustomDnsResolver指向自定义DNS解析器的指针。[typedef void (*OH_NetConn_AppHttpProxyChange)(NetConn_HttpProxy *proxy)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_apphttpproxychange)OH_NetConn_AppHttpProxyChange应用的http代理信息变化回调。[typedef void (*OH_NetConn_NetworkAvailable)(NetConn_NetHandle *netHandle)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_networkavailable)OH_NetConn_NetworkAvailable网络可用回调。[typedef void (*OH_NetConn_NetCapabilitiesChange)(NetConn_NetHandle *netHandle,NetConn_NetCapabilities *netCapabilities)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_netcapabilitieschange)OH_NetConn_NetCapabilitiesChange网络能力集变更回调。[typedef void (*OH_NetConn_NetConnectionPropertiesChange)(NetConn_NetHandle *netHandle,NetConn_ConnectionProperties *connConnetionProperties)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_netconnectionpropertieschange)OH_NetConn_NetConnectionPropertiesChange网络连接属性变更回调。[typedef void (*OH_NetConn_NetLost)(NetConn_NetHandle *netHandle)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_netlost)OH_NetConn_NetLost网络断开回调。[typedef void (*OH_NetConn_NetUnavailable)(void)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_netunavailable)OH_NetConn_NetUnavailable网络不可用回调，在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。[typedef void (*OH_NetConn_NetBlockStatusChange)(NetConn_NetHandle *netHandle, bool blocked)](#ZH-CN_TOPIC_0000002529285449__oh_netconn_netblockstatuschange)OH_NetConn_NetBlockStatusChange网络阻塞状态变更回调。

#### 枚举类型说明

#### NetConn_NetCap

```ets
enum NetConn_NetCap
```

**描述**

网络能力集。

**起始版本：** 11

枚举项描述NETCONN_NET_CAPABILITY_MMS = 0MMSNETCONN_NET_CAPABILITY_NOT_METERED = 11非计量网络NETCONN_NET_CAPABILITY_INTERNET = 12InternetNETCONN_NET_CAPABILITY_NOT_VPN = 15非VPNNETCONN_NET_CAPABILITY_VALIDATED = 16已验证NETCONN_NET_CAPABILITY_PORTAL = 17

Portal

**起始版本：** 12

NETCONN_NET_CAPABILITY_CHECKING_CONNECTIVITY = 31

检测连通性中。

**起始版本：** 12

#### NetConn_NetBearerType

```ets
enum NetConn_NetBearerType
```

**描述**

网络载体类型。

**起始版本：** 11

枚举项描述NETCONN_BEARER_CELLULAR = 0蜂窝网络NETCONN_BEARER_WIFI = 1WIFINETCONN_BEARER_BLUETOOTH = 2

蓝牙

**起始版本：** 12

NETCONN_BEARER_ETHERNET = 3EthernetNETCONN_BEARER_VPN = 4

VPN

**起始版本：** 12

#### NetConn_ErrorCode

```ets
enum NetConn_ErrorCode
```

**描述**

网络连接返回值错误码。

**起始版本：** 15

枚举项描述NETCONN_SUCCESS = 0成功NETCONN_PERMISSION_DENIED = 201缺少权限NETCONN_PARAMETER_ERROR = 401参数错误NETCONN_OPERATION_FAILED = 2100002无法连接到服务NETCONN_INTERNAL_ERROR = 2100003内部错误。1. 内存异常, 比如内存不足或内存拷贝失败。2. 空指针, 比如访问已释放内存的指针。

#### NetConn_PacketsType

```ets
enum NetConn_PacketsType
```

**描述**

枚举跟踪路由的数据包类型。

**起始版本：** 20

枚举项描述NETCONN_PACKETS_ICMP = 0互联网控制消息协议。NETCONN_PACKETS_UDP = 1用户数据报协议。

#### 函数说明

#### OH_NetConn_CustomDnsResolver()

```ets
typedef int (*OH_NetConn_CustomDnsResolver)(const char *host, const char *serv,const struct addrinfo *hint, struct addrinfo **res)
```

**描述**

指向自定义DNS解析器的指针。

**起始版本：** 11

**参数：**

参数项描述const char *host要查询的主机名。const char *serv服务名称。const struct addrinfo *hint指向addrinfo结构的指针。struct addrinfo **res存储DNS查询结果并以链表形式返回。

#### OH_NetConn_AppHttpProxyChange()

```ets
typedef void (*OH_NetConn_AppHttpProxyChange)(NetConn_HttpProxy *proxy)
```

**描述**

应用的http代理信息变化回调。

**起始版本：** 12

**参数：**

参数项描述[NetConn_HttpProxy](NetConn_HttpProxy.md) *proxy变化的代理配置信息,可能是空指针。

#### OH_NetConn_NetworkAvailable()

```ets
typedef void (*OH_NetConn_NetworkAvailable)(NetConn_NetHandle *netHandle)
```

**描述**

网络可用回调。

**起始版本：** 12

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle网络句柄。

#### OH_NetConn_NetCapabilitiesChange()

```ets
typedef void (*OH_NetConn_NetCapabilitiesChange)(NetConn_NetHandle *netHandle,NetConn_NetCapabilities *netCapabilities)
```

**描述**

网络能力集变更回调。

**起始版本：** 12

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle网络句柄。[NetConn_NetCapabilities](NetConn_NetCapabilities.md) *netCapabilities网络能力集。

#### OH_NetConn_NetConnectionPropertiesChange()

```ets
typedef void (*OH_NetConn_NetConnectionPropertiesChange)(NetConn_NetHandle *netHandle,NetConn_ConnectionProperties *connConnetionProperties)
```

**描述**

网络连接属性变更回调。

**起始版本：** 12

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle网络句柄。[NetConn_ConnectionProperties](NetConn_ConnectionProperties.md) *connConnetionProperties网络连接属性。

#### OH_NetConn_NetLost()

```ets
typedef void (*OH_NetConn_NetLost)(NetConn_NetHandle *netHandle)
```

**描述**

网络断开回调。

**起始版本：** 12

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle网络句柄。

#### OH_NetConn_NetUnavailable()

```ets
typedef void (*OH_NetConn_NetUnavailable)(void)
```

**描述**

网络不可用回调，在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。

**起始版本：** 12

#### OH_NetConn_NetBlockStatusChange()

```ets
typedef void (*OH_NetConn_NetBlockStatusChange)(NetConn_NetHandle *netHandle, bool blocked)
```

**描述**

网络阻塞状态变更回调。

**起始版本：** 12

**参数：**

参数项描述[NetConn_NetHandle](NetConn_NetHandle.md) *netHandle网络句柄。bool blocked指示网络是否将被阻塞的标志。