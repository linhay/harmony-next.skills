# Toggle

组件提供勾选框样式、状态按钮样式和开关样式。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

仅当ToggleType设置为Button时，可包含子组件。

**接口**

Toggle(options: ToggleOptions)

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ToggleOptions | 是 | Toggle的信息。 |

**ToggleOptions18+对象说明**

Toggle的信息。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type8+ | ToggleType | 否 | 否 | 开关的样式。 默认值：ToggleType.Switch 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isOn8+ | boolean | 否 | 是 | 开关是否打开。 true：打开；false：关闭。 默认值：false 该属性支持$$双向绑定变量。 该属性支持!!双向绑定变量。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**ToggleType枚举说明**

Toggle的样式。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Checkbox | 0 | 提供单选框样式。 说明： API version 11开始，Checkbox默认样式由圆角方形变为圆形。 通用属性margin的默认值为： { top: '14px', right: '14px', bottom: '14px', left: '14px' }。 默认尺寸为： {width:'20vp', height:'20vp'}。 |
| Switch | 1 | 提供开关样式。 说明： 通用属性margin默认值为： { top: '6px', right: '14px', bottom: '6px', left: '14px' }。 默认尺寸为： {width:'36vp', height:'20vp'}。 |
| Button | 2 | 提供状态按钮样式。如子组件设置文本，文本内容将显示在按钮内。默认高度为28vp，宽度无默认值。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

**selectedColor**

selectedColor(value: ResourceColor)

设置组件在打开状态下的背景颜色。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 组件打开状态的背景颜色。 默认值： 当ToggleType为Switch时，默认值为$r('sys.color.ohos_id_color_emphasize')。 当ToggleType为Checkbox时，默认值为$r('sys.color.ohos_id_color_emphasize')。 当ToggleType为Button时，默认值为$r('sys.color.ohos_id_color_emphasize')混合$r('sys.float.ohos_id_alpha_highlight_bg')的透明度。 |

**switchPointColor**

switchPointColor(color: ResourceColor)

设置Switch类型的圆形滑块颜色。仅当type为ToggleType.Switch生效。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | ResourceColor | 是 | Switch类型的圆形滑块颜色。 默认值：$r('sys.color.ohos_id_color_foreground_contrary') |

**switchStyle12+**

switchStyle(value: SwitchStyle)

设置Switch类型的样式。仅当type为ToggleType.Switch生效。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SwitchStyle | 是 | Switch样式风格。 |

**contentModifier12+**

contentModifier(modifier: ContentModifier<ToggleConfiguration>)

定制Toggle内容区的方法。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | ContentModifier<ToggleConfiguration> | 是 | 在Toggle组件上，定制内容区的方法。 modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

**SwitchStyle12+对象说明**

Switch类型的样式。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pointRadius | number | Resource | 否 | 是 | 设置Switch类型的圆形滑块半径，单位为vp。 说明： 不支持百分比，设定值小于0时按照默认算法设置，设定值大于等于0时按照设定值设置。 未设定此属性时，圆形滑块半径根据默认算法设置。 默认算法：（组件高度（单位：vp） / 2） - （2vp * 组件高度（单位：vp） / 20vp）。 |
| unselectedColor | ResourceColor | 否 | 是 | 设置Switch类型关闭状态的背景颜色。 默认值：深色和浅色模式下均为0x337F7F7F。从API version 20开始，如果开启了优化深浅色模式切换开销能力，浅色模式下默认值为0x19000000，表现效果为10%透明度的黑色；深色模式下默认值为0x19FFFFFF，表现效果为10%透明度的白色。 |
| pointColor | ResourceColor | 否 | 是 | 设置Switch类型的圆形滑块颜色。 默认值：$r('sys.color.ohos_id_color_foreground_contrary') |
| trackBorderRadius | number | Resource | 否 | 是 | 设置Switch类型的滑轨的圆角，单位为vp。 说明： 不支持百分比，设定值小于0时按照默认算法设置，设定值大于组件高度一半时按照组件高度一半设置，其他场合按照设定值设置。 未设定此属性时，滑轨圆角根据默认算法设置。 默认算法：组件高度（单位：vp） / 2。 |

**事件**

除支持[通用事件](通用事件.md)外，还支持以下事件：

**onChange**

onChange(callback: (isOn: boolean) => void)

开关状态切换时触发该事件。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isOn | boolean | 是 | 开关的状态。 true：状态从关切换为开；false：状态从开切换为关。 |

**ToggleConfiguration12+对象说明**

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](自定义内容.md#ZH-CN_TOPIC_0000002553360727__commonconfigurationt)。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isOn | boolean | 否 | 否 | 开关是否打开。 true：开关打开；false：开关关闭。 默认值：false |
| enabled | boolean | 否 | 否 | 是否可以切换状态。 true：可以切换状态；false：不可以切换状态。 默认值：true |
| triggerChange | Callback<boolean> | 否 | 否 | 触发switch选中状态变化。 true：状态从关切换为开；false：状态从开切换为关。 |

**示例**

**示例1（设置开关的样式）**

该示例通过配置ToggleType设置Toggle的勾选框样式、状态按钮样式及开关样式。

```ets
// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Checkbox, isOn: false })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Checkbox, isOn: true })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Button, isOn: false }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })

        Toggle({ type: ToggleType.Button, isOn: true }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })
      }
    }.width('100%').padding(24)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084966.webp)

**示例2（自定义开关类型的样式）**

该示例实现了自定义设置Toggle组件Switch样式，包括圆形滑块半径、关闭状态的背景颜色、圆形滑块颜色、滑轨的圆角。

```ets
// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }
    }.width('100%').padding(24)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364881.webp)

**示例3（自定义Toggle样式）**

该示例实现自定义Toggle样式，通过按钮切换圆形背景颜色：点击蓝圆按钮，背景变蓝色；点击黄圆按钮，背景变黄色。

```ets
// xxx.ets
class MySwitchStyle implements ContentModifier<ToggleConfiguration> {
  selectedColor: Color = Color.White;
  lamp: string = 'string';

  constructor(selectedColor: Color, lamp: string) {
    this.selectedColor = selectedColor;
    this.lamp = lamp;
  }

  applyContent(): WrappedBuilder<[ToggleConfiguration]> {
    return wrapBuilder(buildSwitch);
  }

@Builder
function buildSwitch(config: ToggleConfiguration) {
  Column({ space: 50 }) {
    Circle({ width: 150, height: 150 })
      .fill(config.isOn ? (config.contentModifier as MySwitchStyle).selectedColor : Color.Blue)
    Row() {
      Button('蓝' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(false);
        })
      Button('黄' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(true);
        })
    }

@Entry
@Component
struct Index {
  build() {
    Column({ space: 50 }) {
      Toggle({ type: ToggleType.Switch })
        .enabled(true)
        .contentModifier(new MySwitchStyle(Color.Yellow, '灯'))
        .onChange((isOn: boolean) => {
          console.info('Switch Log:' + isOn);
        })
    }.height('100%').width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244960.webp)