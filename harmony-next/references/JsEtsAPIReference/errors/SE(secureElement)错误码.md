# SE(secureElement)错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 3300101 SE服务状态异常

**错误信息**

IllegalStateError, an attempt is made to use an SE session that has been closed.

**错误描述**

SE服务状态异常。

**可能原因**

1. SE服务状态已断开。

**处理步骤**

1. 关闭SE服务。
1. 重新和SE服务建立连接。

#### 3300102 找不到对应SE安全单元异常

**错误信息**

NoSuchElementError, the AID on the SE is not available or cannot be selected.

**错误描述**

找不到对应SE安全单元异常。

**可能原因**

1. 参数的aid值不正确。
1. SE通道被占用。

**处理步骤**

1. 传入正确的aid值后尝试。
1. 关闭SE通道后重新建立连接。
1. 重启设备后尝试。

#### 3300103 无法获取访问控制规则异常

**错误信息**

SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.

**错误描述**

无法获取访问控制规则异常。

**可能原因**

1. 安全单元上没有应用所依赖的访问规则。

**处理步骤**

1. 写入正确的访问规则到安全单元上。
1. 关闭SE服务后重新建立连接。

#### 3300104 SE芯片IO异常

**错误信息**

IOError, there is a communication problem to the reader or the SE.

**错误描述**

SE芯片IO异常。

**可能原因**

1. 和SE芯片通信异常。
1. SE芯片状态异常。

**处理步骤**

1. 关闭SE服务后重新建立连接。
1. 重启设备尝试。