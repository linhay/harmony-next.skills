# ToolBar

工具栏组件，用于展示针对当前界面内容的操作选项，在界面底部显示。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。


-

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

该组件仅可在Stage模型下使用。

-

如果ToolBar设置[通用属性](通用属性.md)和[通用事件](通用事件.md)，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到ToolBar本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ToolBar设置通用属性和通用事件。

#### 导入模块

```ets
import { SymbolGlyphModifier, DividerModifier, ToolBar, ToolBarOptions, ToolBarModifier, ItemState, LengthMetrics } from '@kit.ArkUI';
```

#### 子组件

无

#### ToolBar

Toolbar({toolBarList: ToolBarOptions, activateIndex?: number, controller: [TabsController](tabs.md#ZH-CN_TOPIC_0000002497604882__tabscontroller), dividerModifier?: DividerModifier, toolBarModifier?: ToolBarModifier})

工具栏组件，用于展示针对当前界面内容的操作选项，在界面底部显示。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| toolBarList | ToolBarOptions | 是 | @ObjectLink | 工具栏列表。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| activateIndex | number | 否 | @Prop | 激活态的子项。 取值范围：大于等于-1。 默认值：-1，没有激活态的子项。若设置数值小于-1，按没有激活项处理。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| controller | [TabsController](tabs.md#ZH-CN_TOPIC_0000002497604882__tabscontroller) | 是 | - | 工具栏控制器，不支持控制工具栏子项。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| dividerModifier13+ | [DividerModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__自定义modifier) | 否 | @Prop | 工具栏头部分割线属性，可设置分割线高度、颜色等。 默认值：系统默认值。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| toolBarModifier13+ | ToolBarModifier | 否 | @Prop | 工具栏属性，可设置工具栏高度、背景色、内边距（仅在工具栏子项数量小于5时生效）、是否显示按压态。 默认值： 工具栏高度：56vp 背景色：ohos_id_toolbar_bg 内边距：24vp 显示按压态。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |

#### ToolBarOptions

继承于 Array<[ToolBarOption](#ZH-CN_TOPIC_0000002522240916__toolbaroption)>。

**装饰器类型：**@Observed

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

#### ToolBarOption

ToolBarOption({content?: [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr), action?: () => void, icon?: Resource, state?: ItemState, iconColor?: ResourceColor, activatedIconColor?: ResourceColor, textColor?: ResourceColor, activatedTextColor?: ResourceColor, toolBarSymbolOptions?: ToolBarSymbolGlyphOptions, accessibilityText?: ResourceStr, accessibilityDescription?: ResourceStr, accessibilityLevel?: string})

定义工具栏的列表内容和属性。

**装饰器类型：**@Observed

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 否 | 工具栏子项的文本。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 工具栏子项点击事件。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| icon | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 工具栏子项的图标。 默认不设置或者设置为undefined，图标不显示。 toolBarSymbolOptions有传入参数时，icon不生效。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| state | ItemState | 否 | 是 | 工具栏子项的状态。 默认为ItemState.ENABLE。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| iconColor13+ | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 是 | 工具栏子项的图标填充颜色。 默认值为$r('sys.color.icon_primary')。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| activatedIconColor13+ | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Color | 否 | 是 | 工具栏子项激活态的图标填充颜色。 默认值为$r('sys.color.icon_emphasize')。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| textColor13+ | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Color | 否 | 是 | 工具栏子项的文本颜色。 默认值为$r('sys.color.font_primary')。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| activatedTextColor13+ | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Color | 否 | 是 | 工具栏子项激活态的文本颜色。 默认值为$r('sys.color.font_emphasize')。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| toolBarSymbolOptions13+ | ToolBarSymbolGlyphOptions | 否 | 是 | 工具栏子项的图标属性，symbol类型。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 工具栏子项的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。 默认值为当前项content属性内容。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 工具栏子项的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。 默认值为“单指双击即可执行”。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 工具栏子项无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。 支持的值为： "auto"：当前组件会转换"yes"。 "yes"：当前组件可被无障碍辅助服务所识别。 "no"：当前组件不可被无障碍辅助服务所识别。 "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。 默认值："auto" 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### ToolBarModifier13+

ToolBarModifier提供设置工具栏高度(height)、背景色(backgroundColor)、左右内边距（padding，仅在item小于5个时生效）、是否显示按压态（stateEffect）的方法。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

#### backgroundColor13+

backgroundColor(backgroundColor: [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)): ToolBarModifier

自定义绘制工具栏背景色的接口，若重载该方法则可进行工具栏背景色的自定义绘制。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundColor | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 是 | 工具栏背景色。 默认背景色为$r('sys.color.ohos_id_color_toolbar_bg')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ToolBarModifier | 设置backgroundColor后的ToolBarModifier对象。 |

#### padding13+

padding(padding: [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)): ToolBarModifier

自定义绘制工具栏左右内边距的接口，若重载该方法则可进行工具栏左右内边距的自定义绘制。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12) | 是 | 工具栏左右内边距，仅在item小于5个时生效。 工具栏默认在item小于5个时padding为24vp，大于等于5个时为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ToolBarModifier | 设置padding后的ToolBarModifier对象。 |

#### height13+

height(height: [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)): ToolBarModifier

自定义绘制工具栏高度的接口，若重载该方法则可进行工具栏高度的自定义绘制，此高度不包含分割线高度。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12) | 是 | 工具栏高度。 工具栏高度默认为56vp（不包含分割线）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ToolBarModifier | 设置height后的ToolBarModifier对象。 |

#### stateEffect13+

stateEffect(stateEffect: boolean): ToolBarModifier

设置是否显示按压态效果的接口。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateEffect | boolean | 是 | 工具栏是否显示按压态效果。 true为显示按压态效果，false为移除按压态效果，默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ToolBarModifier | 设置stateEffect后的ToolBarModifier对象。 |

#### ItemState

定义工具栏子项的当前状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENABLE | 1 | 工具栏子项为正常可点击状态。 |
| DISABLE | 2 | 工具栏子项为不可点击状态。 |
| ACTIVATE | 3 | 工具栏子项为激活状态，可点击。 |

#### ToolBarSymbolGlyphOptions13+

ToolBarSymbolGlyphOptions({normal?: [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier), activated?: SymbolGlyphModifier})

ToolBarSymbolGlyphOptions定义图标的属性。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier) | 否 | 是 | 工具栏symbol图标普通态样式。 默认值：fontColor：$r('sys.color.icon_primary')，fontSize：24vp。 |
| activated | [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier) | 否 | 是 | 工具栏symbol图标激活态样式。 默认值：fontColor：$r('sys.color.icon_emphasize')，fontSize：24vp。 |

#### 事件

不支持[通用事件](通用事件.md)。

#### 示例

#### 示例1（工具栏不同状态的默认效果）

该示例展示了工具栏子项state属性分别设置ENABLE、DISABLE、ACTIVATE状态的不同显示效果。

```ets
import { ToolBar, ToolBarOptions, ItemState } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State toolbarList: ToolBarOptions = new ToolBarOptions();

  aboutToAppear() {
    this.toolbarList.push({
      content: '剪贴我是超超超超超超超超超长样式',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: '拷贝',
      icon: $r('sys.media.ohos_ic_public_copy'),
      action: () => {
      },
      state: ItemState.DISABLE
    })
    this.toolbarList.push({
      content: '粘贴',
      icon: $r('sys.media.ohos_ic_public_paste'),
      action: () => {
      },
      state: ItemState.ACTIVATE
    })
    this.toolbarList.push({
      content: '全选',
      icon: $r('sys.media.ohos_ic_public_select_all'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: '分享',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: '分享',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBar({
            activateIndex: 2,
            toolBarList: this.toolbarList,
          })
        }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245400.webp)

#### 示例2（设置工具栏自定义样式）

从API version 13开始，该示例通过设置属性ToolBarModifier自定义工具栏高度、背景色、按压效果等样式。

```ets
import {
  SymbolGlyphModifier,
  DividerModifier,
  ToolBar,
  ToolBarOptions,
  ToolBarModifier,
  ItemState,
  LengthMetrics,
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State toolbarList: ToolBarOptions = new ToolBarOptions();
  // 自定义工具栏样式
  private toolBarModifier: ToolBarModifier =
    new ToolBarModifier().height(LengthMetrics.vp(52)).backgroundColor(Color.Transparent).stateEffect(false);
  @State dividerModifier: DividerModifier = new DividerModifier().height(0);

  aboutToAppear() {
    // 添加工具栏子项
    this.toolbarList.push({
      content: 'Long long long long long long long long text',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
      state: ItemState.ACTIVATE,
      toolBarSymbolOptions: {
        normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Green]), // 普通态symbol图标
        activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]), // 激活态symbol图标
      },
      activatedTextColor: $r('sys.color.font_primary'),
    })
    this.toolbarList.push({
      content: 'Copy',
      icon: $r('sys.media.ohos_ic_public_copy'),
      action: () => {
      },
      state: ItemState.DISABLE,
      iconColor: '#ff18cb53',
      activatedIconColor: '#ffec5d5d', // 激活态icon颜色
      activatedTextColor: '#ffec5d5d', // 激活态文本颜色
    })
    this.toolbarList.push({
      content: 'Paste',
      icon: $r('sys.media.ohos_ic_public_paste'),
      action: () => {
      },
      state: ItemState.ACTIVATE,
      textColor: '#ff18cb53',
    })
    this.toolbarList.push({
      content: 'All',
      icon: $r('sys.media.ohos_ic_public_select_all'),
      action: () => {
      },
      state: ItemState.ACTIVATE,
    })
    this.toolbarList.push({
      content: '分享',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: '分享',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBar({
            toolBarModifier: this.toolBarModifier,
            dividerModifier: this.dividerModifier,
            activateIndex: 0,
            toolBarList: this.toolbarList,
          })
            .height(52)
        }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002553205363.webp)

#### 示例3（设置工具栏自定义播报）

从API version 18开始，该示例通过设置工具栏子项属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```ets
import { ToolBar, ToolBarOptions, ItemState } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State toolbarList: ToolBarOptions = new ToolBarOptions();

  aboutToAppear() {
    // 添加工具栏子项
    this.toolbarList.push({
      content: '剪贴我是超超超超超超超超超长样式',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
      accessibilityText: '剪贴', // 该项屏幕朗读播报文本为‘剪贴’
      accessibilityDescription: '单指双击即可剪贴', // 该项屏幕朗读播报描述为'单指双击即可剪贴'
      accessibilityLevel: 'yes' // 该项可被无障碍屏幕朗读聚焦
    })
    this.toolbarList.push({
      content: '拷贝',
      icon: $r('sys.media.ohos_ic_public_copy'),
      action: () => {
      },
      state: ItemState.DISABLE,
      accessibilityLevel: 'no' // 该项将无法被屏幕朗读服务所识别，屏幕朗读不可聚焦
    })
    this.toolbarList.push({
      content: '粘贴',
      icon: $r('sys.media.ohos_ic_public_paste'),
      action: () => {
      },
      state: ItemState.ACTIVATE
    })
    this.toolbarList.push({
      content: '全选',
      icon: $r('sys.media.ohos_ic_public_select_all'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: '分享',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: '分享',
      icon: $r('sys.media.ohos_ic_public_share'),
      action: () => {
      },
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBar({
            activateIndex: 2,
            toolBarList: this.toolbarList,
          })
        }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245400.webp)
