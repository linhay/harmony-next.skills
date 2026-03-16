# netBoost（网络加速）

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { netBoost } from '@kit.NetworkBoostKit';
```

#### netBoost.setSceneDesc

setSceneDesc(sceneDesc : SceneDesc): void

设置业务场景。

**需要权限：**ohos.permission.INTERNET

**系统能力:** SystemCapability.Communication.NetworkBoost.Core

**起始版本:** 6.0.0(20)

**参数：**

参数名

类型

必填

说明

sceneDesc

[SceneDesc](#section5777123521219)

是

要设置的业务场景信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码

说明

201

权限校验失败。

1013600001

内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002

系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { netBoost } from '@kit.NetworkBoostKit';
try {
  let sceneDesc : netBoost.SceneDesc = {
    scene : 'realtimeVoice',
    sceneEvent : netBoost.SceneEvent.SCENE_EVENT_ENTER
  }
  netBoost.setSceneDesc(sceneDesc);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### SceneDesc

业务场景描述信息。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

scene

[netQuality.ServiceType](netQuality（网络质量）.md#section18954312204111)

否

否

表示业务场景类型。

sceneEvent

[SceneEvent](#section1278885681816)

否

否

表示业务场景事件。

startTime

number

否

是

表示要经过多长时间进入到sceneEvent事件，单位为s。

- 0表示立即发生sceneEvent事件，默认为0。
- 大于0表示预测未来多长时间进入sceneEvent事件。

duration

number

否

是

预计持续的时长，单位为s。0表示持续时长未知，以SceneEvent的离开事件表示终止。

例如应用即将在10s后进入秒杀场景，预计持续20s，scene可以传入'seckillService'类型，sceneEvent填写SCENE_EVENT_ENTER，startTime可填写10，duration填写20。开发者可以依据实际的场景类型进行选填。

#### SceneEvent

表示业务事件枚举。

**系统能力：**SystemCapability.Communication.NetworkBoost.Core

**起始版本：**6.0.0(20)

名称

值

说明

SCENE_EVENT_ENTER

0

进入业务场景。

SCENE_EVENT_UPDATE

1

更新上一次的业务事件信息。

SCENE_EVENT_LEAVE

2

离开业务场景。