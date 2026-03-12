# UIExtension错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 1011 Ability启动失败

**错误信息**

Failed to start the UIExtension ability.

**错误描述**

扩展Ability拉起失败，请检查扩展Ability的Want参数。

**可能原因**

1. Want参数配置错误；
1. type类型不一致；
1. 提供方应用未安装；

**处理步骤**

检查Want参数配置、应用是否安装等。

#### 1012 Ability切后台失败

**错误信息**

Failed to switch the UIExtension ability to the background.

**错误描述**

扩展Ability切后台失败。

**可能原因**

扩展Ability切后台失败，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 1013 Ability终止失败

**错误信息**

Failed to destroy the UIExtension ability.

**错误描述**

扩展Ability终止失败。

**可能原因**

扩展Ability终止失败，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 100011 未注册同步回调

**错误信息**

No callback has been registered to respond to this request.

**错误描述**

扩展Ability未注册同步回调。

**可能原因**

组件使用方调用sendSync接口向被拉起的Ability发送数据前，扩展Ability未注册同步回调监听。

**处理步骤**

1. 扩展Ability注册同步回调监听；
1. 组件使用方调用sendSync接口向被拉起的Ability发送数据。

#### 100012 数据发送失败

**错误信息**

Transferring data failed.

**错误描述**

数据发送失败。

**可能原因**

数据发送失败，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 100013 禁止嵌套

**错误信息**

Cascading UIExtension components is not allowed.

**错误描述**

拉取另一个嵌入式组件失败，UIExtension存在特殊场景嵌套。

**可能原因**

可能存在UIExtension组件间嵌套。

**处理步骤**

请确认UIExtension组件规格，避免特殊场景嵌套。

#### 100014 Ability退出异常

**错误信息**

The UIExtension ability exited unexpectedly.

**错误描述**

扩展Ability退出异常。

**可能原因**

扩展Ability退出异常，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 100015 生命周期超时

**错误信息**

The lifecycle of the UIExtension ability has timed out.

**错误描述**

扩展Ability生命周期超时。

**可能原因**

扩展Ability生命周期超时，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 100016 Key事件处理超时

**错误信息**

Key event processing by the UIExtension ability has timed out.

**错误描述**

扩展Ability处理Key事件超时。

**可能原因**

扩展Ability处理Key事件超时，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 100018 Ability启动失败

**错误信息**

Failed to start the UIExtension ability.

**错误描述**

设置onTerminated回调场景下，扩展Ability拉起失败，请检查扩展Ability的Want参数。

**可能原因**

1. Want参数配置错误；
1. type类型不一致，具体请参考[EmbeddedComponent组件](EmbeddedComponent.md#ZH-CN_TOPIC_0000002497444946__接口)；
1. 提供方应用未安装；
1. 设备类型不支持；

**处理步骤**

检查Want参数配置、应用是否安装、当前能力是否支持此设备类型等。

#### 100019 Ability切后台失败

**错误信息**

Failed to switch the UIExtension ability to the background.

**错误描述**

设置onTerminated回调场景下，扩展Ability切后台失败。

**可能原因**

扩展Ability切后台失败，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 100020 Ability终止失败

**错误信息**

Failed to destroy the UIExtension ability.

**错误描述**

设置onTerminated回调场景下，扩展Ability终止失败。

**可能原因**

扩展Ability终止失败，需根据AMS日志具体分析。

**处理步骤**

根据AMS日志进行分析。

#### 100021 窗口透明检测

**错误信息**

Transparent node is detected in the UIExtension ability.

**错误描述**

扩展Ability存在透明节点。

**可能原因**

检测到扩展Ability存在透明节点，可能导致阻塞。

**处理步骤**

终止透明节点，避免阻塞事件。