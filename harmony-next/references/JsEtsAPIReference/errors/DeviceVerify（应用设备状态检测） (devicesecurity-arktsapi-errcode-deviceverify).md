[]()[]()

# DeviceVerify（应用设备状态检测）

以下仅介绍本模块客户端特有错误码及原因分析，若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 201 权限校验失败

**错误描述**

权限校验失败。

**可能原因**

应用hap未开通Device Security服务。

**处理步骤**

1. 请参见[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)在AppGallery Connect开启“应用设备状态检测”开关。
1. 重新[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugprofile-0000001914423102)，将新申请到的Profile作为工程的签名文件后重试。

[]()[]()

#### 1003300005 内部异常

**错误描述**

内部异常。

**可能原因**

接口执行流程中调用系统其它接口出现异常。

**处理步骤**

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

[]()[]()

#### 1003300006 访问云端服务器异常

**错误描述**

访问云端服务器异常。

**可能原因**

设备未联网或设备网络不稳定。

**处理步骤**

如未联网，请连接网络后重新发起请求，如联网，可能是网络不稳定，请重试。