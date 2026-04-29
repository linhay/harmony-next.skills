# net_connection_type.h

**概述**

为网络管理数据网络连接模块提供C接口。

引用文件： <network/netmanager/net_connection_type.h>

库： libnet_connection.so

系统能力： SystemCapability.Communication.NetManager.Core

起始版本： 11

相关模块： [NetConnection](NetConnection.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NetConn_NetHandle | NetConn_NetHandle | 存放网络ID。 |
| NetConn_NetCapabilities | NetConn_NetCapabilities | 网络能力集。 |
| NetConn_NetAddr | NetConn_NetAddr | 网络地址。 |
| NetConn_Route | NetConn_Route | 路由配置信息。 |
| NetConn_HttpProxy | NetConn_HttpProxy | 代理配置信息。 |
| NetConn_ConnectionProperties | NetConn_ConnectionProperties | 网络连接信息。 |
| NetConn_NetHandleList | NetConn_NetHandleList | 网络列表。 |
| NetConn_NetSpecifier | NetConn_NetSpecifier | 网络的特征集。 |
| NetConn_NetConnCallback | NetConn_NetConnCallback | 网络状态监听回调集合。 |
| NetConn_ProbeResultInfo | NetConn_ProbeResultInfo | 定义探测结果信息。 |
| NetConn_TraceRouteOption | NetConn_TraceRouteOption | 定义网络跟踪路由选项。 |
| NetConn_TraceRouteInfo | NetConn_TraceRouteInfo | 定义跟踪路由信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NetConn_NetCap | NetConn_NetCap | 网络能力集。 |
| NetConn_NetBearerType | NetConn_NetBearerType | 网络载体类型。 |
| NetConn_ErrorCode | NetConn_ErrorCode | 网络连接返回值错误码。 |
| NetConn_PacketsType | NetConn_PacketsType | 枚举跟踪路由的数据包类型。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| NETCONN_MAX_RTT_NUM 4 | NetConn_ProbeResultInfo的成员变量rtt数组的长度。 起始版本： 11 |
| NETCONN_MAX_NET_SIZE 32 | NetConn_NetHandleList的成员变量netHandles数组的长度。 起始版本： 11 |
| NETCONN_MAX_BEARER_TYPE_SIZE 32 | NetConn_NetCapabilities的成员变量bearerTypes数组的长度。 起始版本： 11 |
| NETCONN_MAX_CAP_SIZE 32 | NetConn_NetCapabilities的成员变量netCaps数组的长度。 起始版本： 11 |
| NETCONN_MAX_ADDR_SIZE 32 | NetConn_ConnectionProperties的成员变量netAddrList、dnsList数组的长度。 起始版本： 11 |
| NETCONN_MAX_ROUTE_SIZE 64 | NetConn_ConnectionProperties的成员变量routeList数组的长度。 起始版本： 11 |
| NETCONN_MAX_EXCLUSION_SIZE 256 | NetConn_HttpProxy的成员变量exclusionList数组的长度。 起始版本： 11 |
| NETCONN_MAX_STR_LEN 256 | NetConn_HttpProxy的成员变量host数组的长度。 起始版本： 11 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef int (*OH_NetConn_CustomDnsResolver)(const char *host, const char *serv,const struct addrinfo *hint, struct addrinfo **res) | OH_NetConn_CustomDnsResolver | 指向自定义DNS解析器的指针。 |
| typedef void (*OH_NetConn_AppHttpProxyChange)(NetConn_HttpProxy *proxy) | OH_NetConn_AppHttpProxyChange | 应用的http代理信息变化回调。 |
| typedef void (*OH_NetConn_NetworkAvailable)(NetConn_NetHandle *netHandle) | OH_NetConn_NetworkAvailable | 网络可用回调。 |
| typedef void (*OH_NetConn_NetCapabilitiesChange)(NetConn_NetHandle *netHandle,NetConn_NetCapabilities *netCapabilities) | OH_NetConn_NetCapabilitiesChange | 网络能力集变更回调。 |
| typedef void (*OH_NetConn_NetConnectionPropertiesChange)(NetConn_NetHandle *netHandle,NetConn_ConnectionProperties *connConnetionProperties) | OH_NetConn_NetConnectionPropertiesChange | 网络连接属性变更回调。 |
| typedef void (*OH_NetConn_NetLost)(NetConn_NetHandle *netHandle) | OH_NetConn_NetLost | 网络断开回调。 |
| typedef void (*OH_NetConn_NetUnavailable)(void) | OH_NetConn_NetUnavailable | 网络不可用回调，在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。 |
| typedef void (*OH_NetConn_NetBlockStatusChange)(NetConn_NetHandle *netHandle, bool blocked) | OH_NetConn_NetBlockStatusChange | 网络阻塞状态变更回调。 |

**枚举类型说明**

**NetConn_NetCap**

```ets
enum NetConn_NetCap
```

描述

网络能力集。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| NETCONN_NET_CAPABILITY_MMS = 0 | MMS |
| NETCONN_NET_CAPABILITY_NOT_METERED = 11 | 非计量网络 |
| NETCONN_NET_CAPABILITY_INTERNET = 12 | Internet |
| NETCONN_NET_CAPABILITY_NOT_VPN = 15 | 非VPN |
| NETCONN_NET_CAPABILITY_VALIDATED = 16 | 已验证 |
| NETCONN_NET_CAPABILITY_PORTAL = 17 | Portal 起始版本： 12 |
| NETCONN_NET_CAPABILITY_CHECKING_CONNECTIVITY = 31 | 检测连通性中。 起始版本： 12 |

**NetConn_NetBearerType**

```ets
enum NetConn_NetBearerType
```

描述

网络载体类型。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| NETCONN_BEARER_CELLULAR = 0 | 蜂窝网络 |
| NETCONN_BEARER_WIFI = 1 | WIFI |
| NETCONN_BEARER_BLUETOOTH = 2 | 蓝牙 起始版本： 12 |
| NETCONN_BEARER_ETHERNET = 3 | Ethernet |
| NETCONN_BEARER_VPN = 4 | VPN 起始版本： 12 |

**NetConn_ErrorCode**

```ets
enum NetConn_ErrorCode
```

描述

网络连接返回值错误码。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| NETCONN_SUCCESS = 0 | 成功 |
| NETCONN_PERMISSION_DENIED = 201 | 缺少权限 |
| NETCONN_PARAMETER_ERROR = 401 | 参数错误 |
| NETCONN_OPERATION_FAILED = 2100002 | 无法连接到服务 |
| NETCONN_INTERNAL_ERROR = 2100003 | 内部错误。1. 内存异常, 比如内存不足或内存拷贝失败。2. 空指针, 比如访问已释放内存的指针。 |

**NetConn_PacketsType**

```ets
enum NetConn_PacketsType
```

描述

枚举跟踪路由的数据包类型。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| NETCONN_PACKETS_ICMP = 0 | 互联网控制消息协议。 |
| NETCONN_PACKETS_UDP = 1 | 用户数据报协议。 |

**函数说明**

**OH_NetConn_CustomDnsResolver()**

```ets
typedef int (*OH_NetConn_CustomDnsResolver)(const char *host, const char *serv,const struct addrinfo *hint, struct addrinfo **res)
```

描述

指向自定义DNS解析器的指针。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *host | 要查询的主机名。 |
| const char *serv | 服务名称。 |
| const struct addrinfo *hint | 指向addrinfo结构的指针。 |
| struct addrinfo **res | 存储DNS查询结果并以链表形式返回。 |

**OH_NetConn_AppHttpProxyChange()**

```ets
typedef void (*OH_NetConn_AppHttpProxyChange)(NetConn_HttpProxy *proxy)
```

描述

应用的http代理信息变化回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| NetConn_HttpProxy *proxy | 变化的代理配置信息,可能是空指针。 |

**OH_NetConn_NetworkAvailable()**

```ets
typedef void (*OH_NetConn_NetworkAvailable)(NetConn_NetHandle *netHandle)
```

描述

网络可用回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| NetConn_NetHandle *netHandle | 网络句柄。 |

**OH_NetConn_NetCapabilitiesChange()**

```ets
typedef void (*OH_NetConn_NetCapabilitiesChange)(NetConn_NetHandle *netHandle,NetConn_NetCapabilities *netCapabilities)
```

描述

网络能力集变更回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| NetConn_NetHandle *netHandle | 网络句柄。 |
| NetConn_NetCapabilities *netCapabilities | 网络能力集。 |

**OH_NetConn_NetConnectionPropertiesChange()**

```ets
typedef void (*OH_NetConn_NetConnectionPropertiesChange)(NetConn_NetHandle *netHandle,NetConn_ConnectionProperties *connConnetionProperties)
```

描述

网络连接属性变更回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| NetConn_NetHandle *netHandle | 网络句柄。 |
| NetConn_ConnectionProperties *connConnetionProperties | 网络连接属性。 |

**OH_NetConn_NetLost()**

```ets
typedef void (*OH_NetConn_NetLost)(NetConn_NetHandle *netHandle)
```

描述

网络断开回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| NetConn_NetHandle *netHandle | 网络句柄。 |

**OH_NetConn_NetUnavailable()**

```ets
typedef void (*OH_NetConn_NetUnavailable)(void)
```

描述

网络不可用回调，在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。

起始版本： 12

**OH_NetConn_NetBlockStatusChange()**

```ets
typedef void (*OH_NetConn_NetBlockStatusChange)(NetConn_NetHandle *netHandle, bool blocked)
```

描述

网络阻塞状态变更回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| NetConn_NetHandle *netHandle | 网络句柄。 |
| bool blocked | 指示网络是否将被阻塞的标志。true表示网络被阻塞，false表示网络未被阻塞。 |