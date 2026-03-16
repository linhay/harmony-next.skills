[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1003500001 系统错误

**错误信息**

Internal error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

系统内部错误。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1003500002 序列化或反序列化失败

**错误信息**

Marshalling or unmarshalling error.

**错误描述**

序列化或反序列化错误时，将返回该错误码。

**可能原因**

实况窗服务异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1003500003 连接服务失败

**错误信息**

Failed to connect service.

**错误描述**

当连接实况窗服务发生错误时，将返回该错误码。

**可能原因**

实况窗服务繁忙或异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1003500004 实况窗开关关闭

**错误信息**

LiveView is not enabled.

**错误描述**

当实况窗开关为关闭状态时，方法将返回该错误码。

**可能原因**

应用的实况窗开关为关闭状态。

**处理步骤**

在“设置 > 应用和元服务”中，选择应用开启实况窗开关。

[]()[]()

#### 1003500005 实况窗权益未申请

**错误信息**

The right of liveView is not enabled.

**错误描述**

当实况窗权益未申请时，将返回该错误码。

**可能原因**

应用未申请对应场景的权益。

**处理步骤**

若已申请实况窗权益，请确认event字段与开通权益的场景匹配；若未申请实况窗权益，请到AGC平台开通实况窗权益。

[]()[]()

#### 1003500006 实况窗已存在

**错误信息**

The liveView already exists.

**错误描述**

当创建实况窗id重复时，将返回该错误码。

**可能原因**

应用创建的实况窗id与已创建的重复。

**处理步骤**

请更换[实况窗id](../topics/misc/liveViewManager.md#section411410371767)。

[]()[]()

#### 1003500007 无法连接服务器

**错误信息**

Couldn't connect to server.

**错误描述**

当网络不可达时，将返回该错误码。

**可能原因**

设备未联网。

**处理步骤**

请检查网络。

[]()[]()

#### 1003500008 实况窗频度超过限制

**错误信息**

Over max number liveViews per second.

**错误描述**

当实况窗频率超过限制时，将返回该错误码。

**可能原因**

对同一个应用的实况窗创建频率超过每秒10个或更新频率超过每秒20个。

**处理步骤**

请降低实况窗调用频率。

[]()[]()

#### 1003500009 实况窗id不存在

**错误信息**

The liveView does not exist.

**错误描述**

当实况窗id不存在时，将返回该错误码。

**可能原因**

实况窗id不存在或者实况窗已被删除。

**处理步骤**

1. 检查[创建实况窗](../topics/misc/liveViewManager.md#section195321751104612)是否成功。
1. 若创建成功，检查端侧通知中心实况窗是否存在。若不存在，请停止调用此[实况窗id](../topics/misc/liveViewManager.md#section411410371767)的接口。

[]()[]()

#### 1003500010 实况窗已结束

**错误信息**

The liveView has ended.

**错误描述**

当实况窗已经结束，继续更新或结束该实况窗时，将返回该错误码。

**可能原因**

当应用调用[liveViewManager.stopLiveView](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveveiw-liveviewmanager#section929145112243)函数结束实况窗后，在应用设置的keepTime内实况窗仍保留在通知中心。此时调用[liveViewManager.updateLiveView](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveveiw-liveviewmanager#section1310319579406)或[liveViewManager.stopLiveView](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveveiw-liveviewmanager#section929145112243)更新或结束同一id的实况窗。

**处理步骤**

请应用在实况窗在通知中心消失前，停止调用接口更新或结束此[实况窗id](../topics/misc/liveViewManager.md#section411410371767)。

[]()[]()

#### 1003500011 实况窗顺序不正确

**错误信息**

The liveView sequence is incorrect.

**错误描述**

当应用更新/结束实况窗的序列号小于等于当前的序列号时，将返回该错误码。

**可能原因**

应用调用更新或结束的序列号小于等于当前的序列号。

**处理步骤**

请修改序列号[sequence](../topics/misc/liveViewManager.md#section411410371767)后重新更新或结束实况窗。

[]()[]()

#### 1003500012 订阅次数超出限制

**错误信息**

The number of subscription times exceeds the upper limit of 2000.

**错误描述**

订阅次数超出限制。

**可能原因**

单个用户每个应用最多有2000个订阅关系。

**处理步骤**

请调整订阅次数。

[]()[]()

#### 1003500013 无效的实况窗订阅场景

**错误信息**

Invalid event type.

**错误描述**

无效的实况窗订阅场景。

**可能原因**

event传值不正确。

**处理步骤**

请检查event参数。

[]()[]()

#### 1003500014 实况窗提醒时间距当前时间过长

**错误信息**

Time exceeds valid period.

**错误描述**

实况窗提醒时间距当前时间过长。

**可能原因**

当前时间距离alertTime超过30天。

**处理步骤**

请检查alertTime、startTime参数。

[]()[]()

#### 1003500015 实况窗订阅失败

**错误信息**

Subscribe failed.

**错误描述**

实况窗订阅失败。

**可能原因**

云侧内部异常。

**处理步骤**

进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1003500016 请求频次超限

**错误信息**

Request subscribe liveView exceed.

**错误描述**

请求频次超限。

**可能原因**

短时间内订阅次数过多。

**处理步骤**

请调整订阅频次。