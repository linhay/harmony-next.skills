[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1000900001 系统错误

**错误信息**

System internal error.

**错误描述**

当系统内部发生错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

1. 请进行重试操作。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
1. [pushService.on('tokenUpdate')](../topics/system-services/pushService（推送服务基础能力）.md#section1730794845210)接口返回1000900001， 优先排查是否重复注册了。

[]()[]()

#### 1000900002 Extension不存在

**错误信息**

Extension does not exist.

**错误描述**

ExtensionAbility不存在。

**可能原因**

启动ExtensionAbility时，系统中不存在该ExtensionAbility。

**处理步骤**

请根据场景化消息类型，检查工程的src/main/module.json5文件的extensionAbilities模块配置是否正确。

[]()[]()

#### 1000900003 Extension回调执行失败

**错误信息**

Extension callback execution failed.

**错误描述**

ExtensionAbility回调执行失败。

**可能原因**

执行ExtensionAbility的[onReceiveMessage](../topics/system-services/RemoteNotificationExtensionAbility（通知扩展Ability）.md#section455013322919)()回调时出现执行异常。

**处理步骤**

请检查ExtensionAbility的[onReceiveMessage](../topics/system-services/RemoteNotificationExtensionAbility（通知扩展Ability）.md#section455013322919)()回调中的代码执行逻辑。

[]()[]()

#### 1000900004 ExtensionAbility回调执行超时

**错误信息**

Extension callback execution timed out.

**错误描述**

ExtensionAbility回调执行超时。

**可能原因**

执行ExtensionAbility的[onReceiveMessage](../topics/system-services/RemoteNotificationExtensionAbility（通知扩展Ability）.md#section455013322919)()回调超时。

**处理步骤**

请检查ExtensionAbility的[onReceiveMessage](../topics/system-services/RemoteNotificationExtensionAbility（通知扩展Ability）.md#section455013322919)()回调中的代码执行逻辑。

[]()[]()

#### 1000900005 不允许重复注册相同的场景化消息

**错误信息**

Messages of the same push type cannot be received repeatedly.

**错误描述**

当重复注册相同类型的场景化消息，将返回该错误码。

**可能原因**

重复调用pushService.[receiveMessage](../topics/system-services/pushService（推送服务基础能力）.md#section125883044911)()注册相同类型的场景化消息。

**处理步骤**

请删除多余的pushService.[receiveMessage](../topics/system-services/pushService（推送服务基础能力）.md#section125883044911)()调用，仅在同一个回调中处理接收到的场景化消息。

[]()[]()

#### 1000900006 连接AAID服务失败

**错误信息**

Failed to connect to the AAID service.

**错误描述**

当连接PushService发生错误时，将返回该错误码。

**可能原因**

PushService运行异常。

**处理步骤**

1. 请进行重试操作。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1000900007 AAID服务内部错误

**错误信息**

Internal error of the AAID service.

**错误描述**

PushService内部处理任务时发生异常，将返回该错误码。

**可能原因**

PushService内部处理超时或异常。

**处理步骤**

1. 请进行重试操作。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1000900008 连接Push服务失败

**错误信息**

Failed to connect to the push service.

**错误描述**

当连接PushService发生错误时，将返回该错误码。

**可能原因**

PushService运行异常。

**处理步骤**

1. 请进行重试操作。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1000900009 推送服务内部错误

**错误信息**

Internal error of the push service.

**错误描述**

PushService内部处理任务时发生异常，将返回该错误码。

**可能原因**

1. Push服务端请求失败。
1. 网络不可用。
1. Push内部处理超时或异常。

**处理步骤**

1. 请尝试重启设备。
1. 切换到新网络或您的热点网络重试。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1000900010 APP身份验证失败

**错误信息**

Illegal application identity.

**错误描述**

应用身份存在异常状态，将返回该错误码。

**可能原因**

- 应用配置错误：

  - 应用在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上创建时未选择HarmonyOS应用类型。
  - 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)的“项目设置 > 开放能力管理”中未启用“推送服务”。请参见[开通推送服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting#section13206419341)步骤5、步骤6完成对应阶段的签名。
  - 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)的“项目设置 > 开放能力管理”中已启用“推送服务”，但未重新申请Profile文件。请参见[开通推送服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting#section13206419341)步骤5、步骤6完成对应阶段的签名。

- 网络不可用。
- 华为服务端异常。
- 不支持云真机调试。

**处理步骤**

1. 请确认应用配置是否正确。
1. 请检查您的网络，确保网络正常可用。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1000900011 网络不可用

**错误信息**

The network is unavailable.

**错误描述**

网络异常，将返回该错误码。

**可能原因**

网络不可用。

**处理步骤**

1. 网络异常，请稍后重试，或重连网络。
1. 终端设备连接的推送服务器的IP是动态分配的，无法通过配置IP白名单方式放行。建议连接不受限的网络或放通5223、443端口重试。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1000900012 未开通推送服务权益

**错误信息**

Push rights are not activated.

**错误描述**

应用未在AGC上开通推送服务权益时，将返回该错误码。

**可能原因**

应用未在AGC上开通推送服务权益。

**处理步骤**

请在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，打开项目，在左侧导航栏选择“增长 > 推送服务”开通推送服务，详情参考指导[操作步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting#section13206419341)第3点。

[]()[]()

#### 1000900013 不允许跨区申请Token

**错误信息**

Cross-location application is not allowed to obtain the token.

**错误描述**

应用跨越数据存储地申请推送服务Token，将返回该错误码。

**可能原因**

应用申请推送服务Token时，存在跨越数据存储地的行为。

**处理步骤**

请检查设备所在地与AGC上设置的[数据处理位置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting#section18206161914419)是否匹配。

[]()[]()

#### 1000900014 设备不支持申请Token

**错误信息**

The device does not support getting token.

**错误描述**

该设备目前不支持申请Token。

**可能原因**

该设备目前不支持申请Token。

**处理步骤**

请使用Phone、Tablet或PC/2in1设备进行调试。从5.1.0(18)版本开始新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

[]()[]()

#### 1000900015 绑定的应用内账号数量达到上限

**错误信息**

The number of bound profile-app relationships exceeds the maximum.

**错误描述**

绑定的应用内账号数量达到上限，特指三方账号对应的用户。

**可能原因**

绑定的应用内账号太多，超过系统限制10个。

**处理步骤**

请调用pushService.[unbindAppProfileId](../topics/system-services/pushService（推送服务基础能力）.md#section915174525214)()解绑若干账号后重试，推荐的绑定和解绑时机请参见[开发通知消息账号校验](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-send-alert#section1677618118810)。

[]()[]()

#### 1000900016 华为账号未登录

**错误信息**

The os distributed account is not logged in.

**错误描述**

华为账号未登录。

**可能原因**

当尝试绑定华为账号时，华为账号未登录。

**处理步骤**

请在“设置”中检查华为账号是否登录，若未登录，则登录华为账号后重试。

[]()[]()

#### 1000900017 不支持当前操作

**错误信息**

The device does not support current operation.

**错误描述**

当前设备或所属国家不支持请求订阅通知授权，将返回该错误码。

**可能原因**

元服务基于账号订阅时，该设备非Phone、Tablet，或者订阅时元服务不在前台。

**处理步骤**

元服务基于账号订阅时，检查订阅时应用是否处于前台。检查设备订阅设备是否为Phone或Tablet。

[]()[]()

#### 1000900018 请求频次超限

**错误信息**

Number of calls exceeded.

**错误描述**

接口请求过于频繁，将返回该错误码。

**可能原因**

短时间内请求该接口的次数过多。

**处理步骤**

请调整接口调用频次。

[]()[]()

#### 1000900019 模板ID非法

**错误信息**

Illegal entity id.

**错误描述**

传入非法的模板ID，将返回该错误码。

**可能原因**

元服务基于账号订阅时，模板ID不是从服务通知领用的合法模板。

**处理步骤**

元服务基于账号订阅时，请从服务通知中选用合法模板。详情见[选用订阅模板](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-service-noti#section880418143379)。

[]()[]()

#### 1000900020 应用的推送服务Token为空

**错误信息**

App token is empty.

**错误描述**

应用推送服务token为空，将返回该错误码。

**可能原因**

在请求该接口前未申请推送服务token。

**处理步骤**

请先[申请推送服务token](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-get-token)后再请求该接口。

[]()[]()

#### 1000900021 应用未在AGC上注册

**错误信息**

App is not available or not registered.

**错误描述**

在AGC上未查找到该应用或元服务，将返回该错误码。

**可能原因**

1. 应用或元服务未在AGC上注册。

2. 订阅类型[type](../topics/system-services/serviceNotification（服务通知）.md#section11384539111610)与应用类型不匹配。

**处理步骤**

1. 检查应用或元服务是否在AGC上完成注册，详情请参见[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)。

2. 检查订阅类型[type](../topics/system-services/serviceNotification（服务通知）.md#section11384539111610)与应用类型是否匹配，仅元服务支持通过华为账号订阅。

[]()[]()

#### 1000900022 通知开关状态为关闭

**错误信息**

Notification switch off.

**错误描述**

应用开关状态为关闭时，将返回该错误码。

**可能原因**

应用开关为关闭状态。

**处理步骤**

请在“设置 > 通知和状态栏”中打开对应应用通知开关。

[]()[]()

#### 1000900023 模板ID数量超过上限

**错误信息**

Number of entity ids exceed the upper limit.

**错误描述**

传入的模板ID数量超过规定上限时，将返回该错误码。

**可能原因**

传入的模板ID数量超过规定上限。

**处理步骤**

请检查传入的模板ID数量是否超过3个。

[]()[]()

#### 1000900024 展示订阅通知授权弹窗失败

**错误信息**

Failed to display subscription UI.

**错误描述**

当展示订阅通知授权弹框失败，将返回该错误码。

**可能原因**

当前订阅通知授权弹窗已经在前台展示。

**处理步骤**

请检查当前前台是否有订阅通知授权弹窗正在展示。

[]()[]()

#### 1000900025 没有使用该模板ID的权益

**错误信息**

No rights to access entity id.

**错误描述**

应用或者元服务未开通消息订阅权益时，将返回该错误码。

**可能原因**

元服务基于账号订阅时，未开通服务通知。

**处理步骤**

元服务基于账号订阅时，请参见[开通服务通知并选用订阅模板](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-service-noti)。

[]()[]()

#### 1000900026 模板ID的类型非法

**错误信息**

Illegal entity type.

**错误描述**

针对某些特定类型模板ID，一次性订阅最多只允许传入一种类型的模板ID，否则将返回该错误码。

**可能原因**

元服务基于账号订阅时，传入了长期订阅模板类型。

**处理步骤**

元服务订阅时，是否传入了长期订阅类型的模板ID。

[]()[]()

#### 1000900030 用户未登录华为账号

**错误信息**

The user has not logged in with HUAWEI ID.

**错误描述**

通过华为账号订阅时，用户未登录华为账号。

**可能原因**

订阅时用户未登录华为账号。

**处理步骤**

请在“设置”中检查华为账号是否登录，确认在登录华为账号后再发起订阅。

[]()[]()

#### 1000900031 同类型的回调只能注册一次

**错误信息**

The same type of callback can be registered only once.

**错误描述**

同类型的回调只能注册一次。

**可能原因**

调用pushService.on('distributedMessageReceive')接口重复注册。

**处理步骤**

排查是否调用[pushService.on('distributedMessageReceive')](../topics/system-services/pushService（推送服务基础能力）.md#section679412149361)接口重复注册。