# ArkTS组件错误码

本模块错误码请参考以下链接。

[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)

[Map Kit错误码](ArkTS API错误码.md)

[Ability Kit错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-errcode)

[Account Kit错误码](ArkTS错误码.md)

[Live View Kit错误码](ArkTS API错误码.md)

[Push Kit错误码](ArkTS API错误码.md)

[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)

[REST API错误码](REST API错误码.md)

#### 10004 系统内部异常
**错误信息**

Internal error.

**错误描述**

系统内部异常。

**可能原因**

系统内部异常。

**处理步骤**

检查是否是网络问题, 如果是服务动态授权码Button报错查看是否对子场景进行了邮件申请，[参考文档](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-timeline#section18702113217305)。

#### 10006 获取分享数据失败
**错误信息**

Failed to get data.

**错误描述**

获取分享数据失败。

**可能原因**

系统内部异常。

**处理步骤**

检查网络环境，如非网络环境影响需要结合具体日志分析。

#### 10008 调用方非元服务
**错误信息**

Not atomic service.

**错误描述**

调用方非元服务。

**可能原因**

非元服务调用了此接口。

**处理步骤**

通过元服务应用调用此接口。