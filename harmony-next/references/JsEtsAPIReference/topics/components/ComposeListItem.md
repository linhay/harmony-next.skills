# ComposeListItem

该组件用于展示一系列宽度相同的列表项，适用于展示连续、多行的同类数据组合（如图片与文本）。


-

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

该组件仅可在Stage模型下使用。

-

如果ComposeListItem设置[通用属性]([通用属性](../misc/通用属性.md).md)和[通用事件](通用事件.md)，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到ComposeListItem本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ComposeListItem设置通用属性和通用事件。

#### 导入模块

```ets
import { ComposeListItem } from "@kit.ArkUI";
```

#### 子组件

无

#### ComposeListItem

ComposeListItem({contentItem?: ContentItem, operateItem?: OperateItem})

列表组件，可自定义列表左侧、中间元素以及右侧显示内容。

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| contentItem | ContentItem | 否 | @Prop | 定义左侧以及中间元素。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| operateItem | OperateItem | 否 | @Prop | 定义右侧元素。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### ContentItem

列表左侧显示的图标、图标大小以及中间元素文字内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconStyle | IconType | 否 | 是 | 左侧元素的图标样式。 默认不设置或设置为undefined，icon图标资源不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| icon | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 左侧元素的图标资源。 默认不设置或设置为undefined，icon图标资源不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier) | 否 | 是 | 左侧元素的Symbol图标资源，优先级大于icon，同时设置了icon和Symbol图标，只显示Symbol图标。 默认不设置或设置为undefined，Symbol图标不显示。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| primaryText | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 中间元素的标题内容。 默认不设置或设置为undefined，标题内容不显示。 文字处理规则： 文本超长后无限换行显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryText | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 中间元素的副标题内容。 默认不设置或设置为undefined，副标题内容不显示。 文字处理规则： 文本超长后无限换行显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| description | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 中间元素的描述内容。 默认不设置或设置为undefined，描述内容不显示。 文字处理规则： 文本超长后无限换行显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### IconType

列表左侧图标类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BADGE | 1 | 左侧图标为badge类型，图标大小为8*8vp。 |
| NORMAL_ICON | 2 | 左侧图标为小图标类型，图标大小为16*16vp。 |
| SYSTEM_ICON | 3 | 左侧图标为系统图标类型，图标大小为24*24vp。 |
| HEAD_SCULPTURE | 4 | 左侧图标为头像类型，图标大小为40*40vp。 |
| APP_ICON | 5 | 左侧图标为应用图标类型，图标大小为64*64vp。 |
| PREVIEW | 6 | 左侧图标为预览图类型，图标大小为96*96vp。 |
| LONGITUDINAL | 7 | 左侧图标为横向特殊比例（宽比高大），保持最长边为96vp。 |
| VERTICAL | 8 | 左侧图标为竖向特殊比例（高比宽大），保持最长边为96vp。 |

#### OperateItem

列表右侧显示的元素类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| arrow | OperateIcon | 否 | 是 | 右侧元素为箭头，大小为12*24vp。 默认不设置或设置为undefined，右侧箭头不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| icon | OperateIcon | 否 | 是 | 右侧元素的第一个图标，大小为24*24vp。 默认不设置或设置为undefined，右侧图标不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| subIcon | OperateIcon | 否 | 是 | 右侧元素的第二个图标，大小为24*24vp。 默认不设置或设置为undefined，右侧第二个图标不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| button | OperateButton | 否 | 是 | 右侧元素为按钮。 默认不设置或设置为undefined，右侧按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| switch | OperateCheck | 否 | 是 | 右侧元素为开关。 默认不设置或设置为undefined，右侧开关不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| checkbox | OperateCheck | 否 | 是 | 右侧元素为多选框，大小为24*24vp。 默认不设置或设置为undefined，右侧多选框不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| radio | OperateCheck | 否 | 是 | 右侧元素为单选框，大小为24*24vp。 默认不设置或设置为undefined，右侧单选框不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| image | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧元素为图片，大小为48*48vp。 默认不设置或设置为undefined，右侧图片不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier) | 否 | 是 | 右侧元素为Symbol图标资源，大小为48*48vp。 默认不设置或设置为undefined，右侧Symbol图标不显示。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧元素为文字。  默认不设置或设置为undefined，右侧文字不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### OperateIcon

列表右侧图标元素的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 否 | 右侧图标/箭头资源。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier) | 否 | 是 | 右侧Symbol图标/箭头资源，优先级大于value。 默认不设置或设置为undefined，Symbol图标不显示。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| action | ()=>void | 否 | 是 | 右侧图标/箭头点击事件。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧图标/箭头的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。 默认值："" 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧图标/箭头的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。 默认值为“单指双击即可执行”。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 右侧图标/箭头的无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。 支持的值为： "auto"：当前组件会转换"no"。 "yes"：当前组件可被无障碍辅助服务所识别。 "no"：当前组件不可被无障碍辅助服务所识别。 "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。 默认值："auto"  元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### OperateButton

列表右侧按钮元素的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧按钮文字。 默认值："" 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。 默认值："" 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。 默认值："单指双击即可执行"。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 右侧按钮的无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。 支持的值为： "auto"：当前组件会转换"no"。 "yes"：当前组件可被无障碍辅助服务所识别。 "no"：当前组件不可被无障碍辅助服务所识别。 "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。 默认值："auto"  元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### OperateCheck

列表右侧元素为Switch、CheckBox、Radio的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isCheck | boolean | 否 | 是 | 右侧Switch/CheckBox/Radio选中状态。  isCheck默认值为false。  isCheck为true时，表示为选中。  isCheck为false时，表示为未选中。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onChange | (value: boolean)=>void | 否 | 是 | 右侧Switch/CheckBox/Radio选中状态改变时触发回调。  value为true时，表示从未选中变为选中。  value为false时，表示从选中变为未选中。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧Switch/CheckBox/Radio的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。 默认值："" 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 否 | 是 | 右侧Switch/CheckBox/Radio的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。 默认跟随基础组件Switch/CheckBox/Radio播报规则。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 右侧Switch/CheckBox/Radio的无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。 支持的值为： "auto"：当前组件会转换"no"。 "yes"：当前组件可被无障碍辅助服务所识别。 "no"：当前组件不可被无障碍辅助服务所识别。 "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。 默认值："auto"  元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### 事件

不支持[通用事件]([通用事件](../misc/通用事件.md).md)。

#### 示例

#### 示例1（设置简单列表项）

该示例实现了带有主标题、副标题、描述、右侧按钮及文本的简单列表项。

```ets
// 该示例主要演示该组件的基础功能使用，包含左侧右侧元素的情况
import { IconType, ComposeListItem } from '@kit.ArkUI';

@Entry
@Component
struct ComposeListItemExample {
  build() {
    Column() {
      List() {
        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL_ICON,
              icon: $r('sys.media.ohos_app_icon'),
              primaryText: '双行列表',
              secondaryText: '辅助文字',
              description: '描述内容文字'
            }),
            operateItem: ({
              icon: {
                value: $r('sys.media.ohos_app_icon'),
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: 'icon'
                  });
                } },
              text: '右侧文本'
            })
}
```

#### 示例2（设置右侧不同元素自定义播报）

从API version 18开始，该示例通过设置属性accessibilityText、accessibilityDescription、accessibilityLevel，实现右侧图标、按钮、单选框自定义屏幕朗读播报文本。

```ets
import { IconType, ComposeListItem } from '@kit.ArkUI';
@Entry
@Component
struct ComposeListItemExample {
  build() {
    Column() {
      List() {
        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL_ICON,
              icon: $r('sys.media.ohos_app_icon'),
              primaryText: '双行列表',
              secondaryText: '辅助文字',
              description: '描述内容文字'
            }),
            operateItem: ({
              radio: {
                accessibilityText: '单选框', // 该单选框屏幕朗读播报文本为‘单选框’
                accessibilityDescription: '未选中', // 该单选框屏幕朗读播报描述为'未选中'
                accessibilityLevel: 'yes'  // 该项可被无障碍屏幕朗读聚焦
              }
            })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL_ICON,
              icon: $r('sys.media.ohos_app_icon'),
              primaryText: '双行列表',
              secondaryText: '辅助文字',
              description: '描述内容文字'
            }),
            operateItem: ({
              button: {
                text: '确定',
                accessibilityText: '这是一个按钮',
                accessibilityDescription: '单指双击即可执行',
                accessibilityLevel: 'no'  // 该按钮不可被屏幕朗读服务识别
              }
          })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL_ICON,
              icon: $r('sys.media.ohos_app_icon'),
              primaryText: '双行列表',
              secondaryText: '辅助文字',
              description: '描述内容文字'
            }),
            operateItem: ({
              icon: {
                value: $r('sys.media.ohos_app_icon'),
                action: () => {
                this.getUIContext().getPromptAction().showToast({
                    message: 'icon'
                  });
                },
                accessibilityText: '这是一个icon', // 该icon屏幕朗读播报文本为‘这是一个icon’
                accessibilityDescription: '单指双击即可弹出', // 该icon屏幕朗读播报描述为'单指双击即可弹出'
                accessibilityLevel: 'yes'  // 该项可被无障碍屏幕朗读聚焦
              }
            })
}
```

#### 示例3（设置Symbol类型图标）

从API version 18开始，该示例通过设置ContentItem、OperateItem、OperateIcon的属性symbolStyle，展示了自定义Symbol类型图标。

```ets
import { IconType, ComposeListItem, SymbolGlyphModifier } from '@kit.ArkUI';
@Entry
@Component
struct ComposeListItemExample {
  build() {
    Column() {
      List() {
        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL_ICON,
              icon: $r('sys.symbol.house'),
              primaryText: '双行列表',
              secondaryText: '辅助文字',
              description: '描述内容文字'
            }),
            operateItem: ({
              image: $r('sys.symbol.car'),
            })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL_ICON,
              icon: $r('sys.symbol.house'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor([Color.Red]),
              primaryText: '双行列表',
              secondaryText: '辅助文字',
              description: '描述内容文字'
            }),
            operateItem: ({
              image: $r('sys.symbol.car'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor([Color.Pink]),
          })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL_ICON,
              icon: $r('sys.symbol.house'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor([Color.Blue]),
              primaryText: '双行列表',
              secondaryText: '辅助文字',
              description: '描述内容文字'
            }),
            operateItem: ({
              icon: {
                value: $r('sys.symbol.car'),
                symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor([Color.Orange]),
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: 'icon'
                  });
                }
          })
        }
```

![image](public_sys-resources/zh-cn_image_0000002522245362.webp)
