[]()[]()

# SafetyDetect（安全检测）

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 201 权限校验失败

**错误描述**

权限校验失败。

**可能原因**

应用hap未开通Device Security服务。

**处理步骤**

1. 请参见[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)在AppGallery Connect开通“安全检测服务”。
1. 重新[申请Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-profile-0000002270709473)，将新申请到的Profile作为工程的签名文件后重试。

[]()[]()

#### 1010800001 内部异常

**错误描述**

内部异常。

**可能原因**

接口执行流程中调用系统其它接口出现异常。

**处理步骤**

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

[]()[]()

#### 1010800002 设备网络异常

**错误描述**

设备网络异常。

**可能原因**

设备未联网。

**处理步骤**

连接网络后重新发起请求。

[]()[]()

#### 1010800003 访问云端服务器异常

**错误描述**

访问云端服务器异常。

**可能原因**

云侧服务不稳定或异常。

**处理步骤**

重新发起请求。

[]()[]()

#### 1010800004 校验capability失败

**错误描述**

应用未开通安全检测服务。

**可能原因**

应用未开通安全检测服务。

**处理步骤**

开通安全检测服务

1. 参考[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)在AppGallery Connect开通“安全检测服务”。
1. 重新[申请Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugprofile-0000001914423102)，将新申请到的Profile作为工程的签名文件后重试。

[]()[]()

#### 1010800005 调用数量超过并行阈值

**错误描述**

接口被同时调用的数量超出最大阈值。

5.1.0(18)版本开始新增该错误码。

**可能原因**

开发者应用并发调用该接口或者其他应用同时调用该接口，调用数量超出最大阈值。

每个设备上最多支持5个并发调用。

**处理步骤**

建议延迟重试，比如延迟1秒。

[]()[]()

#### 1010800006 调用频率超过阈值

**错误描述**

接口被在单位时间内调用次数超出最大阈值。

5.1.0(18)版本开始新增该错误码。

每个应用在每个设备上每天最多可以调用1万次接口、每分钟最多可以调用5次系统完整性检测接口。

**可能原因**

应用过多的调用该接口。

**处理步骤**

控制应用调用次数，此时不应重试，需在下一个统计周期再调用该接口。

[]()[]()

#### 1010800007 操作超时

**错误描述**

接口执行超时。

5.1.0(18)版本开始新增该错误码。

**可能原因**

系统高负载或者网络拥堵。

**处理步骤**

重新发起请求。

[]()[]()

#### 1010800008 云服务流量超过阈值

**错误描述**

云服务请求量过多，超出限流阈值。

5.1.0(18)版本开始新增该错误码。

**可能原因**

大范围设备同时调用云侧接口。

**处理步骤**

建议延迟重试，比如延迟5秒重试，如果重试再次失败，则每次以指数递增间隔重试。