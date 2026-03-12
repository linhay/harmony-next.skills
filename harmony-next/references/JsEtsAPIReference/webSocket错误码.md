# webSocket错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](通用错误码.md)说明文档。

#### 200 连接失败

**错误信息**

Websocket connect failed.

**错误描述**

Websocket连接失败。

**可能原因**

1.

服务器拒绝客户端连接、协议出现问题导致握手失败或证书验证失败。

1.

客户端或服务端断开连接时无状态码。

**处理步骤**

检查协议是否有效、证书校验是否通过，重新连接。

#### 2302001 Websocket URL错误

**错误信息**

Websocket url error.

**错误描述**

Websocket URL错误。

**可能原因**

未配置正确的URL。

**处理步骤**

1.检查URL是否为空或者未包含正确的协议（ws://或wss://)。

2.检查URL长度是否超过2048个字符。

#### 2302002 Websocket 证书不存在

**错误信息**

Websocket certificate file does not exist.

**错误描述**

Websocket 证书不存在。

**可能原因**

证书路径错误或未配置证书。

**处理步骤**

1.检查CA证书路径是否有效。

2.如指定了WebSocketRequestOptions.clientCert，请检查证书路径与私钥路径是否有效。

#### 2302003 Websocket 连接已经存在

**错误信息**

Websocket connection already exists.

**错误描述**

Websocket 连接已经存在。

**可能原因**

Websocket 连接已经建立。

**处理步骤**

已建立websocket连接，无需重复调用WebSocket.connect进行建连。无其他处理步骤。

#### 2302004 WebsocketServer 无法在指定的NIC（网络接口）上进行网络监听

**错误信息**

Can't listen to the given NIC.

**错误描述**

WebsocketServer无法在指定的NIC上进行网络监听。

**可能原因**

WebsocketServer服务器配置文件中的ip地址无效。

**处理步骤**

检查网络连接是否正常，检查ip地址有效性。

#### 2302005 WebsocketServer 无法在指定的端口上进行网络监听

**错误信息**

Can't listen to the given Port.

**错误描述**

WebsocketServer无法在指定的端口上进行网络监听。

**可能原因**

WebsocketServer服务器配置文件中的端口号无效。

**处理步骤**

检查端口号的有效性。

#### 2302998 不允许访问域名

**错误信息**

It is not allowed to access this domain.

**错误描述**

不允许访问此域名。

**可能原因**

元服务应用未正确配置服务器域名。

**处理步骤**

可参考[配置服务器域名](https://developer.huawei.com/consumer/cn/doc/atomic-guides/agc-help-harmonyos-server-domain)文档完成服务器域名相关配置。

#### 2302999 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

空指针异常、内存分配异常等。

**处理步骤**

重启机器重试。