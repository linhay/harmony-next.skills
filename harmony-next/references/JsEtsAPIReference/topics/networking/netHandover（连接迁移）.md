# netHandover（连接迁移）

本模块提供网络连接迁移能力，以便在弱网环境下，系统发起多网迁移（WiFi<->蜂窝，主卡<->副卡等）的过程中，给应用提供连接迁移开始和完成通知，应用根据连接迁移通知的建议进行重建，快速恢复业务，给用户带来平滑、高速、低时延的上网体验。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { netHandover } from '@kit.NetworkBoostKit';
```

#### netHandover.on( 'handoverChange')

on(type: 'handoverChange', callback: Callback<HandoverInfo>): void

订阅连接迁移信息。

**需要权限：**ohos.permission.GET_NETWORK_INFO

**系统能力:** SystemCapability.Communication.NetworkBoost.Core

**起始版本:** 5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"handoverChange"字符串，表示连接迁移变化事件。

callback

Callback<[HandoverInfo](#section5777123521219)>

是

回调函数，返回连接迁移开始和完成的详细信息。

**错误码：**

涉及错误码均为通用错误码，[通用错误码详细描述查看](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

401

参数检查失败。

801

设备不支持该API。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.on('handoverChange', (info: netHandover.HandoverInfo) => {
    if (info.handoverStart) {
      // 连接迁移开始回调，应用按照HandoverStart的建议调整数传策略
      console.info('handover start');
    } else if (info.handoverComplete) {
      // 连接迁移完成回调，应用按照HandoverComplete的建议进行调速和重建恢复
      console.info('handover complete');
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.off( 'handoverChange')

off(type: 'handoverChange', callback?: Callback<HandoverInfo>): void

取消订阅连接迁移信息。

**需要权限：**ohos.permission.GET_NETWORK_INFO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"handoverChange"字符串，表示连接状态变化事件。

callback

Callback<[HandoverInfo](#section5777123521219)>

否

需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

涉及错误码均为通用错误码，[通用错误码详细描述查看](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

401

参数检查失败。

801

设备不支持该API。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.off('handoverChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.setHandoverMode

setHandoverMode(mode: HandoverMode): void

应用可通过该接口变更连接迁移模式，包括委托模式由系统发起连接迁移，和自主模式由应用发起连接迁移，默认为委托模式。设置失败，接口会抛出异常。

**需要权限：**ohos.permission.GET_NETWORK_INFO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

mode

[HandoverMode](#section85513341136)

是

表示应用需要通知系统侧的迁移模式。

**错误码：**

涉及错误码均为通用错误码，[通用错误码详细描述查看](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

401

参数检查失败。

801

设备不支持该API。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  // 设置为自主模式，由应用发起连接迁移
  let mode: netHandover.HandoverMode = netHandover.HandoverMode.DISCRETION;
  netHandover.setHandoverMode(mode);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.getMultiPathQuotaStats

getMultiPathQuotaStats(): MultiPathQuota

获取当前应用多网使用的配额，包括已使用的配额信息和剩余配额信息。

**需要权限：**ohos.permission.LINKTURBO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

[MultiPathQuota](#section168911430203320)

应用配额信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部管理状态机异常。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  let multiquota : netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
  console.info('getMultiPathQuotaStats multiPathQuota.used.count is:' + multiquota.used.count)
  console.info('getMultiPathQuotaStats multiPathQuota.used.duration is:' + multiquota.used.duration)
  console.info('getMultiPathQuotaStats multiPathQuota.remaining.count is:' + multiquota.remaining.count)
  console.info('getMultiPathQuotaStats multiPathQuota.remaining.durationis:' + multiquota.remaining.duration)
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.requestMultiPath

requestMultiPath(callback: Callback<MultiPathRequestResult>): void

发起多网请求。

**需要权限：**ohos.permission.LINKTURBO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

callback

Callback<[MultiPathRequestResult](#section1578014618195)>

是

回调函数，返回发起多网的结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

1013620000

多网功能没有使能。

1013620001

多网已经激活或者是在激活的过程中。

1013620002

应用多网请求已经达到上限。

1013620003

功耗限制不允许发起多网。

1013620004

限额耗尽。

1013620005

多网请求场景的冲突。

1013620006

多网发起太频繁。

1013620007

没有合适的多网链路可用。

1013620008

流量不足。

1013620009

不支持并发。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.requestMultiPath((data: netHandover.MultiPathRequestResult) => {
   console.info(` requestMultiPath result:` + JSON.stringify(data));
  });
 } catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.releaseMultiPath

releaseMultiPath(): void

释放多网请求。

**需要权限：**ohos.permission.LINKTURBO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

1013620100

多网已经激活状态，但是多网不是当前发起release的应用拉起的。

1013620101

多网不在激活态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.releaseMultiPath();
 } catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.on('multiPathStateChange')

on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void

订阅多网状态变化事件。

**需要权限：**ohos.permission.LINKTURBO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"multiPathStateChange"字符串，表示多网状态变化事件。

callback

Callback<[MultiPathStateInfo](#section166554717569)>

是

回调函数，返回多网状态变化信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
    // 回调信息处理
    console.info("on multiPathStateChange: " + JSON.stringify(data));
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.off('multiPathStateChange')

off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void

取消订阅多网状态变化事件。

**需要权限：**ohos.permission.LINKTURBO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"multiPathStateChange"字符串，表示多网状态变化事件。

callback

Callback<[MultiPathStateInfo](#section166554717569)>

否

需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部管理状态机异常。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.off('multiPathStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.on('multiPathRecommendation')

on(type: 'multiPathRecommendation', callback: Callback<MultiPathRecommendationInfo>): void

订阅系统多网建议变化事件。

**需要权限：**ohos.permission.LINKTURBO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"multiPathRecommendation"字符串，表示系统多网建议变化事件。

callback

Callback<[MultiPathRecommendationInfo](#section1557733015378)>

是

回调函数，返回多网建议变化信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.on('multiPathRecommendation', (data: netHandover.MultiPathRecommendationInfo) => {
    // 回调信息处理
    console.info("on multiPathRecommendation: " + JSON.stringify(data));
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netHandover.off('multiPathRecommendation')

off(type: 'multiPathRecommendation', callback?: Callback<MultiPathRecommendationInfo>): void

取消订阅系统多网建议变化事件。

**需要权限：**ohos.permission.LINKTURBO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"multiPathRecommendation"字符串，表示系统多网建议变化事件。

callback

Callback<[MultiPathRecommendationInfo](#section1557733015378)>

否

需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.off('multiPathRecommendation');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### HandoverInfo

连接迁移回调信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

handoverStart

[HandoverStart](#section1593261915415)

是

是

表示连接迁移开始信息。

handoverComplete

[HandoverComplete](#section16119482176)

是

是

表示连接迁移完成信息。

#### HandoverStart

连接迁移开始信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

expires

number

否

否

连接迁移全流程的超时时间，单位为秒，取值为任意正整数或者0。

dataSpeedAction

[DataSpeedAction](#section136319552227)

否

否

老链路的发包建议。

#### HandoverComplete

连接迁移完成信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

result

[ErrorResult](#section1823191782614)

否

否

连接迁移结果。

handoverContinue

boolean

否

否

是否还有HandoverComplete消息。

true表示还有新链路待激活，系统还会上报HandoverComplete消息，一般发生在连接迁移到多个网络的场景。

false表示当前已经是最后一个HandoverComplete消息，连接迁移流程完成。

oldPathLifetime

number

否

否

老链路的剩余生存时长，单位为秒，取值为任意正整数或0。

oldDataSpeedAction

[DataSpeedAction](#section136319552227)

否

否

老链路发包建议。

pathTypeChanged

boolean

否

否

新老链路类型是否发生变更。true表示发生变化，如WiFi<->蜂窝。false表示没有发生变化。

newNetHandle

[connection.NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#nethandle)

否

是

新链路的NetHandle信息。

reEstAction

[ReEstAction](#section575241112914)

否

否

链路重建类型。

newDataSpeedAction

[DataSpeedAction](#section136319552227)

否

否

新链路发包建议。

#### DataSpeedAction

发包速率建议。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

dataSpeedSimpleAction

[netQuality.DataSpeedSimpleAction](netQuality（网络质量）.md#section23982281626)

否

否

应用发包策略的简单建议。

linkUpBandwidth

[netQuality.RateBps](netQuality（网络质量）.md#section786722592713)

否

否

老链路上行带宽。

linkDownBandwidth

[netQuality.RateBps](netQuality（网络质量）.md#section786722592713)

否

否

老链路下行带宽。

#### MultiPathStateInfo

多网状态信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

multiPathState

[MultiPathState](#section1635319535411)

否

否

多网状态。

cause

[MultiPathChangeCause](#section155215540412)

否

否

多网状态变化原因。

netHandle

[connection.NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#nethandle)

否

否

多网链路的netHandle。

pathState

[PathState](#section6391255134310)

否

否

多网链路状态。

pathType

[netQuality.PathType](netQuality（网络质量）.md#section45141941132511)

否

否

多网链路类型。

#### MultiPathRecommendationInfo

多网推荐信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

action

[MultiPathAction](#section186801623193513)

否

否

多网推荐动作。

#### MultiPathQuota

应用配额使用信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

used

[MultiPathQuotaInfo](#section1338164523216)

是

否

应用已使用配额信息。

remaining

[MultiPathQuotaInfo](#section1338164523216)

是

否

应用剩余使用配额信息。

#### MultiPathQuotaInfo

配额信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

count

number

否

否

配额次数信息。

duration

number

否

否

配额时长信息，单位为秒。

#### MultiPathRequestResult

多网请求结果。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

result

[MultiPathErrorResult](#section1689645144117)

否

否

多网请求结果。

#### MultiPathAction

多网推荐动作的枚举。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

值

说明

MULTIPATH_ACTION_REQUEST

0

建议发起多网请求。

MULTIPATH_ACTION_RELEASE

1

建议释放多网请求。

#### MultiPathErrorResult

多网建立结果的枚举。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

值

说明

MULTIPATH_ERROR_NONE

0

多网建立成功。

MULTIPATH_ERROR_NETWORK_REFUSED

1

多网请求被网络拒绝。

MULTIPATH_ERROR_TIMEOUT

2

多网建立超时。

MULTIPATH_ERROR_LOCAL

3

多网建立过程中，本地释放，例如在建立过程中数据开关关闭，或者其他事件发生，已经不满足拉起多网的条件。

#### MultiPathState

多网状态。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

值

说明

MULTIPATH_IDLE

0

多网处于空闲状态。

MULTIPATH_CREATING

1

多网正在建立中。

MULTIPATH_CREATED

2

多网已建立。

MULTIPATH_RELEASING

3

多网正在释放中。

#### PathState

多网链路状态。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

值

说明

PATH_IDLE

0

多网链路处于空闲状态。

PATH_CONNECTED

1

多网链路已连接。

PATH_SUSPENDED

2

多网链路处于挂起状态。

#### MultiPathChangeCause

多网变化原因的枚举。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

值

说明

MULTIPATH_CHANGE_CAUSE_REQUEST_NORMAL

0

正常发起多网请求。

MULTIPATH_CHANGE_CAUSE_RELEASE_NORMAL

50

正常释放多网请求。

MULTIPATH_CHANGE_CAUSE_RELEASE_NETWORK

51

网络原因释放多网。

MULTIPATH_CHANGE_CAUSE_RELEASE_USER_REFUSED

52

用户操作开关释放多网。

MULTIPATH_CHANGE_CAUSE_RELEASE_NO_QUOTA

53

配额耗尽释放多网。

MULTIPATH_CHANGE_CAUSE_RELEASE_POWER_CONSUMPTION

54

功耗原因释放多网。

MULTIPATH_CHANGE_CAUSE_RELEASE_INSUFFICIENT_TRAFFIC

55

流量原因释放多网。

MULTIPATH_CHANGE_CAUSE_RELEASE_CONFLICT

56

场景冲突释放多网。

MULTIPATH_CHANGE_CAUSE_RELEASE_SYS_FUSING

57

应用使用不规范，比如长时间拉起多网不释放，系统释放多网。

MULTIPATH_CHANGE_CAUSE_RELEASE_SYS_DEFAULT

99

系统网络状态变化释放多网。

MULTIPATH_CHANGE_CAUSE_SUSPEND_ENTER

100

多网进入挂起状态，此时多网虽未释放，但是实际链路无法传输数据。

MULTIPATH_CHANGE_CAUSE_SUSPEND_LEAVE

101

多网退出挂起状态。

MULTIPATH_CHANGE_CAUSE_CONN_PROPERTIES_UPDATE

102

多网链路的链接属性信息更新，比如IP地址更新。

#### HandoverMode

表示连接迁移模式枚举。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

值

说明

DELEGATION

0

委托模式，表示由系统发起连接迁移。应用未调用setHandoverMode接口则默认为该模式。

DISCRETION

1

自主模式，表示由应用发起连接迁移。应用可以通过该接口禁止系统发起连接迁移。在某些场景下，比如该应用切换到后台时，依旧有可能由系统触发切换。

#### ReEstAction

表示重建枚举。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

值

说明

DEFAULT

0

表示应用需要使用同样的远端IP，进行重建链路。

QUERY_DNS

1

表示数据链路类型发生变化，比如WiFi <-> CELL，或者是数据链路所在的运营商信息等变化。

CHANGE_REMOTE_IP

2

表示应用需要使用不同的远端IP进行重建。

CHANGE_IP_VERSION

3

表示应用需要修改IP类型进行重建，比如IPV4 <-> IPV6。

NO_EST

4

表示应用应该在老链路进行立即重试，再次发起网络资源请求和交互，无需重建链路。

#### ErrorResult

表示连接迁移结果枚举。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

值

说明

ERROR_NONE

0

表示连接迁移成功。

ERROR_HANDOVER_TIMEOUT

1

表示连接迁移超时。

ERROR_NEW_PATH_ACTIVATION_FAILED

2

表示连接迁移时新链路激活失败。

ERROR_ABORT

3

表示连接迁移被取消。