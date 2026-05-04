# Panel

可滑动面板，提供一种轻量的内容展示窗口，方便在不同尺寸中切换。


从API version 12开始，该组件不再维护，推荐使用通用属性[bindSheet](半模态转场.md)。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

可以包含子组件。


子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../../guides/if-else：条件渲染.md)、[ForEach](ForEach.md)和[LazyForEach](LazyForEach.md)）。

**接口**

Panel(show: boolean)

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 控制Panel显示或隐藏。 说明： 如果设置为false时，则不占位隐藏。Visible.None或者show之间有一个生效时，都会生效不占位隐藏。 |

#### 属性

除支持[通用属性](通用属性.md)外，还支持以下属性：

**type**

type(value: PanelType)

可滑动面板的类型。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | PanelType | 是 | 设置可滑动面板的类型。 默认值：PanelType.Foldable |

**mode**

mode(value: PanelMode)

可滑动面板的初始状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | PanelMode | 是 | 设置可滑动面板的初始状态。 Minibar类型默认值：PanelMode.Mini；其余类型默认值：PanelMode.Half 从API version 10开始，该属性支持$$双向绑定变量。 |

**dragBar**

dragBar(value: boolean)

设置是否存在控制条。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置是否存在控制条，true表示存在，false表示不存在。 默认值：true |

**customHeight10+**

customHeight(value: Dimension | PanelHeight)

指定PanelType.CUSTOM状态下的高度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Dimension | PanelHeight | 是 | 指定PanelType.CUSTOM状态下的高度。 默认值：0 说明： 不支持设置百分比。 |

**fullHeight**

fullHeight(value: number | string)

指定PanelType.Full状态下的高度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 指定PanelMode.Full状态下的高度。 默认值：当前组件主轴大小减去8vp空白区 说明： 不支持设置百分比。 |

**halfHeight**

halfHeight(value: number | string)

指定PanelMode.Half状态下的高度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 指定PanelMode.Half状态下的高度。 默认值：当前组件主轴大小的一半。 说明： 不支持设置百分比。 |

**miniHeight**

miniHeight(value: number | string)

指定PanelMode.Mini状态下的高度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 指定PanelMode.Mini状态下的高度。 默认值：48 单位：vp 说明： 不支持设置百分比。 |

**show**

show(value: boolean)

当滑动面板弹出时调用。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当滑动面板弹出时调用，true显示面板，false不显示面板。 默认值：true 说明： 该属性的优先级高于参数show。 |

**backgroundMask9+**

backgroundMask(color: ResourceColor)

指定Panel的背景蒙层。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | ResourceColor | 是 | 指定Panel的背景蒙层。 默认值：'#08182431' |

**showCloseIcon10+**

showCloseIcon(value: boolean)

设置是否显示关闭图标。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置是否显示关闭图标，true表示显示，false表示不显示。 默认值：false |

**PanelType枚举说明**

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| Minibar | 提供minibar和类全屏展示切换效果。 |
| Foldable | 内容永久展示类，提供大（类全屏）、中（类半屏）、小三种尺寸展示切换效果。 |
| Temporary | 内容临时展示区，提供大（类全屏）、中（类半屏）两种尺寸展示切换效果。 |
| CUSTOM10+ | 配置自适应内容高度，不支持尺寸切换效果。 |

**PanelMode枚举说明**

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Mini | 0 | 类型为minibar和foldable时，为最小状态；类型为temporary，则不生效。 |
| Half | 1 | 类型为foldable和temporary时，为类半屏状态；类型为minibar，则不生效。 |
| Full | 2 | 类全屏状态。 |

**PanelHeight10+枚举说明**

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| WRAP_CONTENT | 类型为CUSTOM时，自适应内容高度。 |

#### 事件

除支持[通用事件](通用事件.md)外，还支持以下事件：

**onChange**

onChange(event: (width: number, height: number, mode: PanelMode) => void)

当可滑动面板发生状态变化时触发。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 内容区的宽度值。 |
| height | number | 是 | 内容区的高度值。 当dragBar属性为true时，panel本身的高度值为dragBar高度加上内容区高度。 |
| mode | PanelMode | 是 | 面板的状态。 |

**onHeightChange9+**

onHeightChange(callback: (value: number) => void)

当可滑动面板发生高度变化时触发。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内容区的高度值，默认返回值单位为px。 当dragBar属性为true时，panel本身的高度值为dragBar高度加上内容区高度。 因用户体验设计原因，panel最高只能滑到 fullHeight-8vp。 |

#### 示例

```ets
// xxx.ets
@Entry
@Component
struct PanelExample {
  @State show: boolean = false

  build() {
    Column() {
      Text('2021-09-30    Today Calendar: 1.afternoon......Click for details')
        .width('90%')
        .height(50)
        .borderRadius(10)
        .backgroundColor(0xFFFFFF)
        .padding({ left: 20 })
        .onClick(() => {
          this.show = !this.show
        })
      Panel(this.show) { // 展示日程
        Column() {
          Text('Today Calendar')
          Divider()
          Text('1. afternoon 4:00 The project meeting')
}
      .type(PanelType.Foldable)
      .mode(PanelMode.Half)
      .dragBar(true) // 默认开启
      .halfHeight(500) // 默认一半
      .showCloseIcon(true) // 显示关闭图标
      .onChange((width: number, height: number, mode: PanelMode) => {
        console.info(`width:${width},height:${height},mode:${mode}`)
      })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
}
```

![image](public_sys-resources/zh-cn_image_0000002522085436.webp)