# netQuality（网络质量）

本模块提供网络质量实时评估、网络场景识别以及弱信号预测等能力，以便应用针对弱网等环境下实现网络自适应，包括缓存、码率、帧率、分辨率等策略的调整。应用也可以通过网络质量中的应用传输体验反馈接口，触发系统进行网络加速。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { netQuality } from '@kit.NetworkBoostKit';
```

#### netQuality.on( 'netQosChange')

on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void

订阅网络质量信息。

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

固定填写"netQosChange"字符串，表示网络质量变化事件。

callback

Callback<Array<[NetworkQos](#section5777123521219)>>

是

回调函数，返回网络Qos变化的详细信息。

**错误码**：

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.on('netQosChange', (list: Array<netQuality.NetworkQos>) => {
    if (list.length > 0) {
      list.forEach((qos) => {
        // 回调信息处理
        console.info(`Succeeded receive netQosChange info`);
      });
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netQuality.off( 'netQosChange')

off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void

取消订阅网络质量信息。

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

固定填写"netQosChange"字符串，表示连接状态变化事件。

callback

Callback<Array<[NetworkQos](#section5777123521219)>>

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.off('netQosChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netQuality.on( 'netSceneChange')

on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void

订阅网络场景信息。

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

固定填写"netSceneChange"字符串，表示网络场景变化事件。

callback

Callback<Array<[NetworkScene](#section19886656145619)>>

是

回调函数，返回网络场景变化的详细信息。

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.on('netSceneChange', (list: Array<netQuality.NetworkScene>) => {
    if (list.length > 0) {
      list.forEach((scene) => {
        // 回调信息处理
        console.info(`Succeeded receive netSceneChange info`);
        if (scene.weakSignalPrediction) {
          // 弱信号预测处理
        }
      });
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netQuality.off( 'netSceneChange')

off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void

取消订阅网络场景信息。

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

固定填写"netSceneChange"字符串，表示网络场景变化事件。

callback

Callback<Array<[NetworkScene](#section19886656145619)>>

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.off('netSceneChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### netQuality.reportQoe

reportQoe(appQoe: AppQoe): void

应用传输体验反馈，上报失败，接口会抛出异常。

**需要权限：**ohos.permission.GET_NETWORK_INFO

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

appQoe

[AppQoe](#section25523227370)

是

表示应用需要反馈的传输体验信息。

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  let serviceType: netQuality.ServiceType = 'shortVideo';
  let qoeType: netQuality.BadQoeCause = 'serverErr';
  let appQoe: netQuality.AppQoe = {
    serviceType,
    qoeType
  };
  netQuality.reportQoe(appQoe);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### AppQoe

应用传输体验信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

serviceType

[ServiceType](#section18954312204111)

否

否

应用的业务类型。

qoeType

[QoeType](#section819973417438)

否

否

应用体验类型。

#### NetworkQos

网络质量回调信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

pathType

[PathType](#section45141941132511)

否

否

表明相应的数据路径上的网络质量信息。

linkUpBandwidth

[RateBps](#section786722592713)

否

否

上行带宽信息，单位为bps。

linkDownBandwidth

[RateBps](#section786722592713)

否

否

下行带宽信息，单位为bps。

linkUpRate

[RateBps](#section786722592713)

否

否

上行速率，单位为bps。

linkDownRate

[RateBps](#section786722592713)

否

否

下行速率，单位为bps。

rttMs

number

否

否

RTT时延，表示统计时间间隔内，pathType对应数据路径上，所有的TCP上下行数据包的平均往返时延，单位为ms。

如果在统计时间间隔内没有收到某次TCP请求的回复，则该次的RTT时延不在该统计时间间隔内统计，取值范围是任意正数。

linkUpBufferDelayMs

number

否

否

上行发送空口缓冲时延，取值范围是任意正数。

linkUpBufferCongestionPercent

number

否

是

上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。

#### PathType

数据路径类型，枚举值。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

值

说明

CELLULAR_PRIMARY

0

蜂窝主卡。

CELLULAR_SECONDARY

1

蜂窝副卡。

WIFI_PRIMARY

2

主WiFi。

WIFI_SECONDARY

3

辅WiFi。

#### RateBps

type RateBps = number

带宽或速率的抽象表示。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

类型

说明

number

表示值的类型为number，可取任意正数，单位为bps。

#### ServiceType

type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 'transaction' | 'shopping' | 'detection' | 'cloudService' | 'voiceConference' | 'videoConference' | 'audio' | 'navigation' | 'seckillService' | 'login'

应用业务类型。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

类型

说明

'default'

表示默认服务类型，值固定为'default'字符串。

'background'

表示后台类型，值固定为'background'字符串。

'realtimeVoice'

表示实时语音类型，值固定为'realtimeVoice'字符串。

'realtimeVideo'

表示实时视频类型，值固定为'realtimeVideo'字符串。

'callSignaling'

表示语音信令类型，值固定为'default'字符串。

'realtimeGame'

表示实时游戏类型，值固定为'realtimeGame'字符串。

'normalGame'

表示普通游戏类型，值固定为'normalGame'字符串。

'shortVideo'

表示短视频类型，值固定为'shortVideo'字符串。

'longVideo'

表示长视频类型，值固定为'longVideo'字符串。

'livestreamingAnchor'

表示直播主播类型，值固定为'livestreamingAnchor'字符串。

'livestreamingWatcher'

表示直播观看类型，值固定为'livestreamingWatcher'字符串。

'download'

表示下载类型，值固定为'download'字符串。

'upload'

表示上传类型，值固定为'upload'字符串。

'browser'

表示浏览页面类型，值固定为'browser'字符串。

'transaction'

表示交易支付或者扫码类型，值固定为'transaction'字符串。该类型从API 20开始支持。

'shopping'

表示购物类型，值固定为'shopping'字符串。该类型从API 20开始支持。

'detection'

表示探测类型，值固定为'detection'字符串。该类型从API 20开始支持。

'cloudService'

表示云业务、云游戏类型，值固定为'cloudService'字符串。该类型从API 20开始支持。

'voiceConference'

表示语音会议类型，值固定为'voiceConference'字符串。该类型从API 20开始支持。

'videoConference'

表示视频会议类型，值固定为'videoConference'字符串。该类型从API 20开始支持。

'audio'

表示音乐、音频类型，值固定为'audio'字符串。该类型从API 20开始支持。

'navigation'

表示导航定位类型，值固定为'navigation'字符串。该类型从API 20开始支持。

'seckillService'

表示秒杀业务类型，如抢票、抢购、抢单、抢红包等，值固定为'seckillService'字符串。该类型从API 20开始支持。

'login'

表示登录（含一键登录）类型，值固定为'login'字符串。该类型从API 20开始支持。

#### QoeType

type QoeType = 'good' | BadQoeCause

应用体验类型。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

类型

说明

'good'

表示体验良好，值固定为'good'字符串。

[BadQoeCause](#section327672810449)

表示体验差类型。

#### BadQoeCause

type BadQoeCause = 'unknown' | 'serverErr' | 'noData' | 'packetLost' | 'packetOutOfOrder' | 'highJitter' | 'highLatency'

应用体验差类型。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

类型

说明

'unknown'

表示未知原因，值固定为'unknown'字符串。

'serverErr'

表示服务器异常，值固定为'serverErr'字符串。

'noData'

表示无数据，值固定为'noData'字符串。

'packetLost'

表示丢包，值固定为'packetLost'字符串。

'packetOutOfOrder'

表示乱序，值固定为'packetOutOfOrder'字符串。

'highJitter'

表示高抖动，值固定为'highJitter'字符串。

'highLatency'

表示高时延，值固定为'highLatency'字符串。

#### 速率带宽级别

定义了多个速率或带宽的常量值。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

值

说明

BPS

number

1

1bps

KBPS

number

1000

1kbps

MBPS

number

1000000

1Mbps

GBPS

number

1000000000

1Gbps

TBPS

number

1000000000000

1Tbps

#### NetworkScene

网络场景状态变更回调信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

pathType

[PathType](#section45141941132511)

否

否

表明相应的数据路径上的网络场景信息。

scene

[Scene](#section18341052913)

否

否

场景状态。

recommendedAction

[RecommendedAction](#section1272138831)

否

否

建议的数传策略。

weakSignalPrediction

[WeakSignalPrediction](#section1593261915415)

否

是

弱信号预测相关信息。

#### WeakSignalPrediction

弱信号预测相关信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

isLastPredictionValid

boolean

否

否

最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。

startTime

number

否

否

预计多长时间进入弱信号（单位：秒），取值范围为0和任意正数。

duration

number

否

否

预计在弱信号区域停留时长（单位：秒），取任意正数。取值0，此次预测结果无效。

#### Scene

type Scene = 'normal' | 'congestion' | 'frequentHandover' | 'weakSignal'

场景类型。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

类型

说明

'normal'

表示正常场景，值固定为'normal'字符串。

'congestion'

表示拥塞场景，值固定为'congestion'字符串。

'frequentHandover'

表示小区切换频繁场景，值固定为'frequentHandover'字符串。

'weakSignal'

表示弱信号场景，值固定为'weakSignal'字符串。

#### DataSpeedSimpleAction

type DataSpeedSimpleAction = 'suspendData' | 'decreaseData' | 'increaseData' | 'keepData'

应用发包策略的简单建议。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

类型

说明

'suspendData'

表示停止发包，值固定为'suspendData'字符串。

'decreaseData'

表示降低发包速率，值固定为'decreaseData'字符串。

'increaseData'

表示增加发包速率，值固定为'increaseData'字符串。

'keepData'

表示保持当前发包速率，值固定为'keepData'字符串。

#### RecommendedAction

type RecommendedAction = 'doCaching' | DataSpeedSimpleAction

应用数传策略建议。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**5.0.0(12)

类型

说明

'doCaching'

表示做缓存动作，值固定为'doCaching'字符串。

[DataSpeedSimpleAction](#section23982281626)

应用发包策略的简单建议。