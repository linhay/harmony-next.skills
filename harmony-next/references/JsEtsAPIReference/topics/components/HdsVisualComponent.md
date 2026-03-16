# HdsVisualComponent

HdsVisualComponent组件承载复杂视效实现，应用开发者通过HdsVisualComponent选择具体视效场景完成复杂视效的开发。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { HdsVisualComponent, HdsSceneController, HdsSceneType, HdsVisualComponentAttribute, hdsEffect } from '@kit.UIDesignKit';
```

#### 子组件

无

#### 接口

HdsVisualComponent()

创建HdsVisualComponent通用视效组件。

**系统能力****：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)，还支持以下属性：

#### scene

scene(sceneType: HdsSceneType, controller: HdsSceneController, callback?: HdsSceneFinishCallback, frameRateRange?: hdsEffect.ExpectedFrameRateRange)

设置视效场景

**系统能力****：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

参数名

类型

必填

说明

sceneType

[HdsSceneType](#section92774418495)

是

视效场景类型。

controller

[HdsSceneController](#section19696213112)

是

视效场景控制器。

callback

[HdsSceneFinishCallback](#section010418487170)

否

视效场景结束回调。

frameRateRange

hdsEffect.[ExpectedFrameRateRange](../misc/hdsEffect.md#section19809172171211)

否

视效场景帧率配置。

#### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

#### HdsSceneType

视效场景。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

名称

值

**说明**

DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK

0

自带背景的双边流光。

 说明：

该场景在TV中无效果，在其他设备类型中可正常显示。

#### HdsSceneFinishCallback

type HdsSceneFinishCallback = () => void

场景视效结束回调函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### HdsSceneController

场景控制器。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### constructor

constructor()

HdsSceneController的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### start

start(): void

开始视效场景。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### pause

pause(): void

暂停视效场景。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### resume

resume(): void

恢复视效场景。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### stop

stop(): void

停止视效场景。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### setSceneParams

setSceneParams(params: SceneParams): HdsSceneController

设置场景参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

params

[SceneParams](#section1636545113020)

是

场景参数。

**返回值：**

类型

说明

[HdsSceneController](#section19696213112)

返回[HdsSceneController](#section19696213112)对象。

#### SceneParams

type SceneParams = DualEdgeFlowLightWithMaskParam

场景视效参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

类型

说明

[DualEdgeFlowLightWithMaskParam](#section12461104631817)

双边边缘流光视效参数。

#### DualEdgeFlowLightWithMaskParam

双边边缘流光视效参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

**名称**

**类型**

只读

可选

**说明**

backgroundMaskColors

Array<[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)>

否

否

背景蒙层颜色数组。

firstEdgeFlowLight

hdsEffect.[EdgeFlowLightParam](../misc/hdsEffect.md#section63471415181915)

否

否

第一条流光参数配置。

secondEdgeFlowLight

hdsEffect.[EdgeFlowLightParam](../misc/hdsEffect.md#section63471415181915)

否

否

第二条流光参数配置。

#### 示例

```ets
import { HdsVisualComponent, HdsSceneController, HdsSceneType, HdsVisualComponentAttribute } from '@kit.UIDesignKit';

@Entry
@Component
struct EdgeFlowLightVisualComponent {
  @State sceneController: HdsSceneController = new HdsSceneController()
    .setSceneParams({
      backgroundMaskColors: [Color.Green, Color.Red],
      firstEdgeFlowLight: {
        startPos: 0,
        endPos: 0.5,
        color: Color.Red
      },
      secondEdgeFlowLight: {
        startPos: 0,
        endPos: -0.5,
        color: Color.Green
      }
    })

  build() {
    Stack() {
      HdsVisualComponent()
        .scene(HdsSceneType.DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK, this.sceneController, () => {
          console.info('Succeeded in finishing');
        })
        .width('100%')
        .height('50%')
    }
  }
}
```