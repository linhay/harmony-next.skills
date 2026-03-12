# DistributedSchedule错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 16600001 系统服务工作异常

**错误信息**

The system ability works abnormally.

**错误描述**

当系统服务工作异常时，会报此错误码。

**可能原因**

该错误码表示系统服务工作异常，可能原因如下。

1. DMS服务没有正常启动。
1. DMS的binder对象无法正常获取。
1. 流转依赖的其他服务没有正常启动或者binder对象无法获取。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备尝试。

#### 16600002 指定的token或callback未注册

**错误信息**

The specified token or callback is not registered.

**错误描述**

当调用continuationManager相关的接口时传入的token或callback未提前注册，会报此错误码。

**可能原因**

该错误码可能原因是指定的token或callback未注册。

**处理步骤**

请先注册token或callback。

#### 16600003 应用注册token已达到最大次数限制

**错误信息**

The number of token registration times has reached the upper limit.

**错误描述**

当调用continuationManager.registerContinuation接口时次数过多超出限制（最大值为600），会报此错误码。

**可能原因**

该错误码可能原因是应用注册token已达到最大次数限制。

**处理步骤**

请勿频繁注册，请使用已注册的token。

#### 16600004 指定的callback已注册

**错误信息**

The specified callback has been registered.

**错误描述**

当使用相同的callback调用continuationManager的on接口时，会报此错误码。

**可能原因**

该错误码表示指定的callback已注册，可能原因是使用相同的callback重复注册。

**处理步骤**

请勿使用相同的callback重复注册。

#### 16300501 系统服务工作异常

**错误信息**

The system ability works abnormally.

**错误描述**

当系统服务工作异常时，会报此错误码。

**可能原因**

该错误码表示系统服务工作异常，可能原因如下。

1. DMS服务没有正常启动。
1. DMS的binder对象无法正常获取。
1. 流转依赖的其他服务没有正常启动或者binder对象无法获取。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备尝试。

#### 16300502 获取指定的missionId的missionInfo失败

**错误信息**

Failed to get the missionInfo of the specified missionId.

**错误描述**

当调用distributedMissionManager.continueMission接口获取指定missionId的missionInfo失败时，会报此错误码。

**可能原因**

该错误码表示获取指定的missionId的missionInfo失败，可能原因如下。

1. missionId输入错误。
1. missionId对应的missionInfo确实不存在。

**处理步骤**

请检查输入的missionId是否正确。

#### 16300503 远端未安装应用且不支持免安装

**错误信息**

The application is not installed on the remote end and installation-free is not supported.

**错误描述**

当调用distributedMissionManager.continueMission接口使用迁移功能时，若远端未安装应用且不支持免安装，会报此错误码。

**可能原因**

该错误码可能原因是远端未安装迁移应用并且不支持免安装。

**处理步骤**

1. 请检查远端是否已安装需要迁移的应用。
1. 请检查远端是否支持免安装。

#### 16300504 远端未安装应用但支持免安装，需使用免安装标识重试

**错误信息**

The application is not installed on the remote end and installation-free is supported. Try again with the freeInstall flag.

**错误描述**

当调用distributedMissionManager.continueMission接口使用迁移功能时，若远端未安装应用但支持免安装，会报此错误码。

**可能原因**

该错误码可能原因是远端未安装应用但支持免安装，使用时未使用免安装的标识。

**处理步骤**

请使用免安装的标识重试。

#### 16300505 操作设备必须是迁移的应用所在的设备或需迁移到的目标设备

**错误信息**

The operation device must be the device where the application to be continued is currently located or the target device.

**错误描述**

当调用distributedMissionManager.continueMission接口使用迁移功能时，若操作设备不是迁移的应用所在的设备或需迁移到的目标设备，会报此错误码。

**可能原因**

该错误码可能原因是操作设备不是迁移的应用所在的设备或需迁移到的目标设备。

**处理步骤**

请检查操作设备是否是迁移的应用所在的设备或需迁移到的目标设备。

#### 16300506 本地迁移任务已在进行中

**错误信息**

The local continuation task is already in progress.

**错误描述**

当调用distributedMissionManager.continueMission接口使用迁移功能时，若本地迁移任务已在进行中，会报此错误码。

**可能原因**

该错误码表示本地迁移任务已在进行中，可能原因是已经发起了迁移任务还未结束。

**处理步骤**

请检查是否已经发起了迁移并未结束。

#### 16300507 获取指定的bundleName的missionInfo失败

**错误信息**

Failed to get the missionInfo of the specified bundle name.

**错误描述**

当调用distributedMissionManager.continueMission接口获取指定bundleName的missionInfo失败时，会报此错误码。

**可能原因**

该错误码表示获取指定的bundleName的missionInfo失败，可能原因如下。

1. bundleName输入错误。
1. bundleName对应的missionInfo确实不存在。

**处理步骤**

请检查输入的bundleName是否正确。

#### 29360207 注册超出最大次数

**错误信息**

The number of registrations has reached the upper limit.

**错误描述**

当调用continuationManager.register接口时次数过多超出限制，会报此错误码。

**可能原因**

该错误码可能原因是设备频繁注册，次数超出最大次数限制。

**处理步骤**

重启服务并且避免频繁注册。

#### 29360208 token未注册

**错误信息**

The token is not registered.

**错误描述**

当调用continuationManager相关接口时使用未注册的token，会报此错误码。

**可能原因**

该错误码可能原因是未注册token。

**处理步骤**

注册token并使用已注册的token。

#### 29360209 callback已注册

**错误信息**

The callback has been registered.

**错误描述**

当使用相同的callback重复调用continuationManager.on接口时，会报此错误码。

**可能原因**

该错误码能原因是指定的callback已经注册过。

**处理步骤**

请勿使用相同的callback重复注册。

#### 29360210 callback未注册

**错误信息**

The callback is not registered.

**错误描述**

当调用continuationManager的off、updateConnectStatus和startDeviceManager等接口时，若未提前调用on接口注册callback，会报此错误码。

**可能原因**

该错误码可能原因是指定的callback未注册。

**处理步骤**

注册callback并使用已注册的callback。

#### 29360211 连接ability失败

**错误信息**

Failed to connect to the ability.

**错误描述**

当调用continuationManager的startDeviceManager接口时，若连接相应Ability失败时，会报此错误码。

**可能原因**

该错误码可能原因是指定token连接ability失败。

**处理步骤**

检查token是否有效以及相应ability是否正常服务，重新启动服务或重启设备。

#### 29360214 callback类型错误

**错误信息**

The type of callback is not supported.

**错误描述**

当调用continuationManager的on和off接口时，若参数callback类型错误时，会报此错误码。

**可能原因**

该错误码表示callback类型错误，可能原因是不支持传入的callback类型。

**处理步骤**

请使用系统支持的callback类型并传入。

#### 29360215 无效的连接状态

**错误信息**

Invalid connection state.

**错误描述**

当调用continuationManager的updateConnectStatus接口时，若参数status为无效值时，会报此错误码。

**可能原因**

该错误码表示无效的连接状态，可能原因是入参DeviceConnectState为非指定值。

**处理步骤**

设置指定合法的DeviceConnectState值。

#### 29360216 无效的流转模式

**错误信息**

Invalid continuation mode.

**错误描述**

当调用continuationManager的register和startDeviceManager接口时，若参数ContinuationExtraParams.continuationMode为无效值时，会报此错误码。

**可能原因**

该错误码可能原因是入参ContinuationExtraParams.continuationMode为非指定值。

**处理步骤**

设置指定合法的ContinuationExtraParams.continuationMode值。