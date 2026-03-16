[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1009700003

**错误信息**

NearLink is off.

**错误描述**

当星闪开关未打开时调用接口，将返回该错误码。

**可能原因**

星闪开关未打开。

**处理步骤**

在设备的设置界面，通过“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径打开星闪后重试，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1009700020

**错误信息**

The UUID is already registered.

**错误描述**

当对应UUID的端口通道已经被注册，将返回该错误码。

**可能原因**

重复调用注册端口通道接口并传入相同UUID。

**处理步骤**

调用dataTransfer.destroyPort接口销毁对应UUID的端口通道，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1009700021

**错误信息**

The number of ports exceeds the upper limit.

**错误描述**

端口注册数量超上限，将返回该错误码。

**可能原因**

数传业务通道分配达到上限。

**处理步骤**

调用dataTransfer.destroyPort接口销毁其他已注册的端口通道，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1009700023

**错误信息**

The data writing process is congested.

**错误描述**

发送数传数据异常。

**可能原因**

协议层或芯片处理数据拥塞。

**处理步骤**

控制数据写入流量，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1009700099

**错误信息**

Operation failed.

**错误描述**

当系统内部处理出错，将返回该错误码。

**可能原因**

其他未知错误。

在设备已配对的情况下再调用[startPairing](../topics/system-services/remoteDevice（对端设备的连接能力）.md#section65252361113)发起配对，会返回该错误码。

**处理步骤**

进行重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。