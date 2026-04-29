# hdsEffect

本模块提供组件的拓展视效能力，包括组件点光源效果、按压光效、动画控制。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { hdsEffect } from '@kit.UIDesignKit';
```

#### HdsEffectBuilder

将创建的视效参数添加到VisualEffect对象上，构建VisualEffect对象。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### constructor

constructor()

HdsEffectBuilder的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### pointLight

pointLight(value: PointLightEffect): HdsEffectBuilder

创建一个组件点光源效果，单个组件最多同时受12个光源照亮。支持点光源效果的组件范围如下：Button、Toggle、Row、Column、Image、Flex、Stack、Select、Menu、MenuItem。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | PointLightEffect | 是 | 设置组件点光源属性。通过设置光源和被照亮的类型，实现点光源照亮周围组件的UI效果。 说明：光源位置初始化为组件正中心，不会跟着组件的位移而变化位置，因此不建议在滚动组件中使用点光源效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HdsEffectBuilder | 返回HdsEffectBuilder对象。 |

**示例：**

```ets
import { hdsEffect } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  @State lightSourceType: hdsEffect.PointLightSourceType = hdsEffect.PointLightSourceType.NONE;
  build() {
    Column({ space: 10 }) {
      Row({ space: 10 }) {
        Column() {
          Text('illuminated').padding(10).fontColor(Color.White)
        }
        .visualEffect(new hdsEffect.HdsEffectBuilder()
          .pointLight({
            illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
          })
          .buildEffect())
      }
      Row({ space: 10 }) {
        Button('lightSource')
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pointLight({
              sourceType: this.lightSourceType,
              illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
            })
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.lightSourceType = hdsEffect.PointLightSourceType.BRIGHT;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.lightSourceType = hdsEffect.PointLightSourceType.NONE;
            }
          })
      }
      Row({ space: 10 }) {
        Column() {
          Text('illuminated').padding(10).fontColor(Color.White)
        }
        .visualEffect(new hdsEffect.HdsEffectBuilder()
          .pointLight({
            illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
          })
          .buildEffect())
      }
    .backgroundColor(Color.Black)
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
```

#### pressShadow

pressShadow(type: PressShadowType): HdsEffectBuilder

设置当前组件按压阴影效果，一般用于组件按压后背景色变化。仅在Button组件上生效。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | PressShadowType | 是 | 设置组件按压阴影效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HdsEffectBuilder | 返回HdsEffectBuilder对象。 |

**示例：**

```ets
import { hdsEffect } from '@kit.UIDesignKit';

@Entry
@Component
struct PressShadowExample {
  @State button_blend_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
  @State button_gradient_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;

  build() {
    NavDestination() {
      Column({ space: 50 }) {
        Button("BLEND_WHITE", { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.button_blend_state)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.button_blend_state =  hdsEffect.PressShadowType.BLEND_WHITE;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.button_blend_state =  hdsEffect.PressShadowType.NONE;
            }
          })

        Button("GRADIENT", { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.button_gradient_state)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.button_gradient_state =  hdsEffect.PressShadowType.BLEND_GRADIENT;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.button_gradient_state =  hdsEffect.PressShadowType.NONE;
            }
          })
      }
      .height('70%')
      .justifyContent(FlexAlign.Center)
    }
    .width('100%')
    .height('100%')
    .title('Button example')
    .backgroundColor('#040404')
  }
```

#### shaderEffect

shaderEffect(params: ShaderEffectParams): HdsEffectBuilder

创建一个shader视效。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | ShaderEffectParams | 是 | shader视效参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HdsEffectBuilder | 返回HdsEffectBuilder对象。 |

**示例：**

```ets
import { hdsEffect } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();

  build() {
    Column() {
      Stack() {
      }
      .visualEffect(new hdsEffect.HdsEffectBuilder()
        .shaderEffect({
          effectType: hdsEffect.EffectType.DUAL_EDGE_FLOW_LIGHT,
          animation: {
            duration: 4000,
            iterations: -1,
            autoPlay: true,
            onFinish: () => {
              console.info('Succeeded in finishing');
            }
          },
          controller: this.controller,
          params: {
            firstEdgeFlowLight: {
              startPos: 0,
              endPos: 1.0,
              color: '#1AD0F1',
            },
            secondEdgeFlowLight: {
              startPos: 0.5,
              endPos: 1.5,
              color: '#FFA4E5',
            }
        })
        .buildEffect())
      .width(200)
      .borderRadius('50%')
      .clip(true)
      .height(200)
      .backgroundColor('#383838')
    }
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.Black)
    .width('100%')
    .height('100%')
  }
```

#### buildEffect

buildEffect(): VisualEffect

将上文中设置的所有组件视效添加到VisualEffect对象上。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| VisualEffect | 返回带有各种视觉效果的VisualEffect。 |

#### ShaderEffectParams

shaderEffect视效配置。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| effectType | EffectType | 否 | 否 | 视效类型。 |
| animation | AnimationParams | 否 | 是 | 视效动画参数配置。 |
| params | EffectParams | 否 | 是 | shader参数配置。 |
| controller | ShaderEffectController | 否 | 是 | 视效控制器。 |

#### EffectType

视效类型。

设备行为差异： 该视效在TV中无效果，在其他设备类型中可正常显示。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DUAL_EDGE_FLOW_LIGHT | 0 | 双边边缘流光。 |
| UV_BACKGROUND_FLOW_LIGHT | 1 | UV背景流光。 |

#### AnimationParams

视效动画参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 视效动画播放一次时间，单位为ms(毫秒)。 默认值：1000。 说明： - 设置小于0的值时按0处理。 - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| iterations | number | 否 | 是 | 播放次数，-1为重复执行。 取值范围：[-1,+∞)。 默认值：1。 说明： - 设置超出取值范围的值时按默认值处理。 - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| curve | Curve | 否 | 是 | 动画曲线。 |
| delay | number | 否 | 是 | 视觉动画延迟播放时间，单位为ms(毫秒)。 默认值：0。 取值范围：(-∞, +∞)。 说明： - delay>=0为延迟播放，delay<0表示提前播放。对于delay<0的情况：当delay的绝对值小于实际视效动画时长，视效动画将在开始后第一帧直接运动到delay绝对值的时刻的状态；当delay的绝对值大于等于实际视效动画时长，视效动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。 - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| autoPlay | boolean | 否 | 是 | 是否自动执行。true：自动执行；false不自动执行。 默认值：true。 |
| onFinish | OnFinishCallback | 否 | 是 | 结束时回调函数。 |
| expectedFrameRateRange | ExpectedFrameRateRange | 否 | 是 | 帧率设置。 |

#### OnFinishCallback

type OnFinishCallback = () => void

视效结束回调函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### ExpectedFrameRateRange

视效帧率配置。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| expected | FrameRateType | 否 | 否 | 目标帧率。 |
| min | FrameRateType | 否 | 否 | 最小帧率。 |
| max | FrameRateType | 否 | 否 | 最大帧率。 |

#### FrameRateType

视效帧率。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FRAME_RATE_15 | 15 | 帧率15FPS。 |
| FRAME_RATE_30 | 30 | 帧率30FPS。 |
| FRAME_RATE_60 | 60 | 帧率60FPS。 |

#### EffectParams

type EffectParams = DualEdgeFlowLightParam | UVFlowLightColorParam

视觉效果参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| DualEdgeFlowLightParam | 双边边缘流光视效参数。 |
| UVFlowLightColorParam | UV流光视效参数。 |

#### DualEdgeFlowLightParam

双边边缘流光视效参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| firstEdgeFlowLight | EdgeFlowLightParam | 否 | 否 | 第一条流光参数配置。 |
| secondEdgeFlowLight | EdgeFlowLightParam | 否 | 否 | 第二条流光参数配置。 |

#### UVFlowLightColorParam

UV流光视效参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorSource | Array<ResourceColor> | 否 | 否 | 背景流光颜色。 |
| colorTarget | Array<ResourceColor> | 否 | 是 | 目标渐变颜色。默认流光颜色不渐变。 |

#### EdgeFlowLightParam

边缘流光视效参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startPos | number | 否 | 否 | 流光开始位置。以视效容器的上边缘的中点为起始点，取值单位为起始点沿着容器边缘至目标位置的距离与容器周长的比值。沿着容器边缘逆时针为正方向，顺时针为负方向。 |
| endPos | number | 否 | 否 | 流光结束位置。以视效容器的上边缘的中点为起始点，取值单位为起始点沿着容器边缘至目标位置的距离与容器周长的比值。沿着容器边缘逆时针为正方向，顺时针为负方向。 |
| color | ResourceColor | 否 | 否 | 流光颜色。 |

#### ShaderEffectController

视效控制器。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### constructor

constructor()

ShaderEffectController的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### play

play(): void

开始执行视效。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### pause

pause(): void

暂停视效。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### resume

resume(): void

继续执行视效。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### reverse

reverse(): void

反转视效。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### stop

stop(): void

停止视效。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

#### setEffectParams

setEffectParams(params: EffectParams): void

设置视效shader参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | EffectParams | 是 | shaders视效参数。 |

#### PointLightEffect

点光源效果属性。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sourceType | PointLightSourceType | 否 | 是 | 组件发光效果类型，发光会影响到周围标记为可以被照亮的组件，并在组件上产生光效。 默认值：NONE，不发光。 |
| illuminatedType | PointLightIlluminatedType | 否 | 是 | 组件受光效果类型，设置当前组件是否可以被光源照亮，以及被照亮的类型。 默认值：NONE，不受光。 说明：受光组件如果设置了border的颜色和宽度，会覆盖掉点光源效果。 |
| options | PointLightOptions | 否 | 是 | 组件自定义发光参数选项。 |


sourceType的优先级高于options。当同时设置sourceType和options时，options自定义发光参数不会生效。

#### PointLightSourceType

组件发光效果类型。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 组件光源类型：点光源不生效，组件无发光效果。 |
| SOFT | 1 | 组件光源类型：柔和点光源，发光强度较弱，周围照亮范围较小。 |
| BRIGHT | 2 | 组件光源类型：明亮点光源，发光强度较高，周围照亮范围较大。 |

#### PointLightIlluminatedType

组件受光效果类型。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 组件受光类型：不被照亮。 |
| BORDER | 1 | 组件受光类型：边缘被照亮。 |
| CONTENT | 2 | 组件受光类型：内容被照亮。 |
| BORDER_CONTENT | 3 | 组件受光类型：边缘和内容被照亮。 |
| DEFAULT_FEATHERING_BORDER | 20 | 组件受光类型：边缘被照亮，并且有羽化效果。 |

#### PointLightOptions

组件自定义发光参数选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | ResourceColor | 否 | 是 | 光源颜色。 默认值：Color.White。 |
| intensity | number | 否 | 是 | 光源强度，建议取值范围0~1。数值越大，光源越强，当光源强度为0时，光源不发光。 默认值：0。 |
| height | Dimension | 否 | 是 | 光源高度。光源越高，照射范围越大。 默认值：0。 |
| bloom | number | 否 | 是 | 设置组件的泛光效果强度，建议取值范围为0~1。数值越大，泛光范围越大。 默认值：0。 |

#### PressShadowType

组件按压阴影效果。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无按压阴影效果。 |
| BLEND_GRADIENT | 1 | 按压阴影为椭圆形径向渐变的白色，中心为透明度85%的白色，边界为不透明的白色。叠加在组件背景色之上。 |
| BLEND_WHITE | 2 | 按压阴影为15%透明度的白色。叠加在组件背景色之上。 |