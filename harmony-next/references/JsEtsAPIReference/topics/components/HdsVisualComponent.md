# HdsVisualComponent

HdsVisualComponent组件承载复杂视效实现，应用开发者通过HdsVisualComponent选择具体视效场景完成复杂视效的开发。

**起始版本：**6.0.0(20)

#### 导入模块


- HdsVisualComponentAttribute是用于配置HdsVisualComponent组件属性的关键接口。6.0.1(21)及之前版本，导入HdsVisualComponent组件后需要开发者手动导入HdsVisualComponentAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入HdsVisualComponent组件后，会自动导入HdsVisualComponentAttribute，无需开发者手动导入。

- 如果开发者手动导入HdsVisualComponentAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```ets
import { HdsVisualComponent, HdsVisualComponentAttribute, HdsSceneController, HdsSceneType, hdsEffect } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```ets
import { HdsVisualComponent, HdsSceneController, HdsSceneType, hdsEffect } from '@kit.UIDesignKit';
```

#### 子组件

无

#### 接口

HdsVisualComponent()

创建HdsVisualComponent通用视效组件。

模型约束： 此接口仅可在Stage模型下使用。

卡片能力： 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力****：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)，还支持以下属性：

#### scene

scene(sceneType: HdsSceneType, controller: HdsSceneController, callback?: HdsSceneFinishCallback, frameRateRange?: hdsEffect.[ExpectedFrameRateRange](../misc/hdsEffect.md#section19809172171211))

设置视效场景

模型约束： 此接口仅可在Stage模型下使用。

卡片能力： 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力****：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | HdsSceneType | 是 | 视效场景类型。 |
| controller | HdsSceneController | 是 | 视效场景控制器。 |
| callback | HdsSceneFinishCallback | 否 | 视效场景结束回调。 |
| frameRateRange | hdsEffect.[ExpectedFrameRateRange](../misc/hdsEffect.md#section19809172171211) | 否 | 视效场景帧率配置。 |

#### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

#### HdsSceneType

视效场景。

模型约束： 此接口仅可在Stage模型下使用。

卡片能力： 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK | 0 | 自带背景的双边流光。 说明：该场景在TV中无效果，在其他设备类型中可正常显示。 |

#### HdsSceneFinishCallback

type HdsSceneFinishCallback = () => void

场景视效结束回调函数。

模型约束： 此接口仅可在Stage模型下使用。

卡片能力： 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### HdsSceneController

场景控制器。

模型约束： 此接口仅可在Stage模型下使用。

卡片能力： 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### constructor

constructor()

HdsSceneController的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

卡片能力： 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### start

start(): void

开始视效场景。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### pause

pause(): void

暂停视效场景。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### resume

resume(): void

恢复视效场景。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### stop

stop(): void

停止视效场景。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### setSceneParams

setSceneParams(params: SceneParams): HdsSceneController

设置场景参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | SceneParams | 是 | 场景参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HdsSceneController | 返回HdsSceneController对象。 |

#### SceneParams

type SceneParams = DualEdgeFlowLightWithMaskParam

场景视效参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| DualEdgeFlowLightWithMaskParam | 双边边缘流光视效参数。 |

#### DualEdgeFlowLightWithMaskParam

双边边缘流光视效参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundMaskColors | Array<[Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Color> | 否 | 否 | 背景蒙层颜色数组。 |
| firstEdgeFlowLight | hdsEffect.[EdgeFlowLightParam](../misc/hdsEffect.md#section63471415181915) | 否 | 否 | 第一条流光参数配置。 |
| secondEdgeFlowLight | hdsEffect.[EdgeFlowLightParam](../misc/hdsEffect.md#section63471415181915) | 否 | 否 | 第二条流光参数配置。 |

#### 示例

```ets
// 从6.0.2(22)版本开始，无需手动导入HdsVisualComponentAttribute。具体请参考HdsVisualComponent的导入模块说明。
import { HdsVisualComponent, HdsVisualComponentAttribute, HdsSceneController, HdsSceneType } from '@kit.UIDesignKit';

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
```

![image](public_sys-resources/zh-cn_image_0000002553205749.webp)
