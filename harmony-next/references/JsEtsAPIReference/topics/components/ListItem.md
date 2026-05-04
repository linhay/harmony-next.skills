# [List](list.md)Item

用来展示列表具体item，必须配合[List](list.md)来使用。

- 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

- 该组件的父组件只能是[List]([List](list.md).md)或者[ListItemGroup](ListItemGroup.md)。

- 当ListItem配合[LazyForEach](LazyForEach.md)使用时，ListItem子组件在ListItem创建时创建。配合[if/else](../../guides/if-else：条件渲染.md)、[ForEach](ForEach.md)使用时，或父组件为List/ListItemGroup时，ListItem子组件在ListItem布局时创建。

#### 子组件

可以包含单个子组件。

#### 接口

#### [List](list.md)Item10+

[List](list.md)Item(value?: ListItemOptions)

创建[List](list.md)Item组件。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [List](list.md)ItemOptions | 否 | 为ListItem提供可选参数，该对象内含有ListItemStyle枚举类型的style参数。 默认值：{ style: ListItemStyle.NONE } |

#### [List](list.md)Item(deprecated)

[List](list.md)Item(value?: string)

创建[List](list.md)Item组件。


从API version 7开始支持，从API version 10开始废弃，建议使用[ListItem10+](#ZH-CN_TOPIC_0000002553200785__listitem10)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 否 | 无 |

#### 属性

除支持[通用属性]([通用属性](../misc/通用属性.md).md)外，还支持以下属性：

#### sticky(deprecated)

sticky(value: Sticky)

设置[List](list.md)Item吸顶效果。


从API version 7开始支持，从API version 9开始废弃，建议使用[sticky](List.md#ZH-CN_TOPIC_0000002522240820__sticky9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Sticky | 是 | [List](list.md)Item吸顶效果。 默认值：Sticky.None |

#### editable(deprecated)

editable(value: boolean | EditMode)

设置当前[List](list.md)Item元素是否可编辑，进入编辑模式后可删除或移动列表项。

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | EditMode | 是 | [List](list.md)Item元素是否可编辑。 默认值：false |

#### selectable8+

selectable(value: boolean)

设置当前[List](list.md)Item元素是否可以被鼠标框选。外层List容器的鼠标框选开启时，ListItem的框选才生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | [List](list.md)Item元素是否可以被鼠标框选。设置为true时可以被鼠标框选，设置为false时无法被鼠标框选。 默认值：true |

#### selected10+

selected(value: boolean)

设置当前ListItem选中状态。该属性支持[$$](../../guides/$$语法：系统组件双向同步.md)双向绑定变量。该属性需要在设置[多态样式](多态样式.md)前使用才能生效[选中态样式](多态样式.md#ZH-CN_TOPIC_0000002497604846__statestyles)。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前[List](list.md)Item选中状态。设置为true时为选中状态，设置为false时为默认状态。 默认值：false |

#### swipeAction9+

swipeAction(value: SwipeActionOptions)

用于设置[List](list.md)Item的划出组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SwipeActionOptions | 是 | [List](list.md)Item的划出组件。 |

#### Sticky(deprecated)枚举说明

[List](list.md)Item吸顶效果枚举。


从API version 7开始支持，从API version 9开始废弃，建议使用[List组件stickyStyle枚举](List.md#ZH-CN_TOPIC_0000002522240820__stickystyle9枚举说明)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | - | 无吸顶效果。 |
| Normal | - | 当前item吸顶。 |
| Opacity | - | 当前item吸顶显示透明度变化效果。 |

#### EditMode(deprecated)枚举说明

[List](list.md)Item元素编辑模式枚举。

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | - | 编辑操作不限制。 |
| Deletable | - | 可删除。 |
| Movable | - | 可移动。 |

#### SwipeEdgeEffect9+枚举说明

滑动效果枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Spring | - | [List](list.md)Item划动距离超过划出组件大小后可以继续划动。 如果设置了删除区域，ListItem划动距离超过删除阈值后可以继续划动， 松手后按照弹簧阻尼曲线回弹。 |
| None | - | [List](list.md)Item划动距离不能超过划出组件大小。 如果设置了删除区域，ListItem划动距离不能超过删除阈值， 并且在设置删除回调的情况下，达到删除阈值后松手触发删除回调。 |

#### SwipeActionOptions9+对象说明

start和end对应的@builder函数中顶层必须是单个组件，否则会引发未定义行为。如果@builder函数中顶层是if/else、ForEach等语句，那么需要保证if/else、ForEach等语句必须能生成单个组件。

滑动手势只在listItem区域上，如果子组件划出[List](list.md)Item区域外，在ListItem以外部分不会响应划动手势。所以在多列模式下，建议不要将划出组件设置太宽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | SwipeActionItem | 否 | 是 | ListItem向右划动时item左边的组件（List垂直布局时）或ListItem向下划动时item上方的组件（List水平布局时）。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| end | CustomBuilder | SwipeActionItem | 否 | 是 | [List](list.md)Item向左划动时item右边的组件（List垂直布局时）或ListItem向上划动时item下方的组件（List水平布局时）。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| edgeEffect | SwipeEdgeEffect | 否 | 是 | 滑动效果。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onOffsetChange11+ | (offset: number) => void | 否 | 是 | 当列表项向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列表方向为“水平”时）位置发生变化触发，以vp为单位。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### SwipeActionItem10+对象说明

[List](list.md)垂直布局，ListItem向右滑动时，item左边的长距离滑动删除选项。向左滑动时，item右边的长距离滑动删除选项。

[List](list.md)水平布局，ListItem向上滑动时，item下边的长距离滑动删除选项。向下滑动时，item上边的长距离滑动删除选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| actionAreaDistance | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 否 | 是 | 设置组件长距离滑动删除距离阈值。即划出组件被完全滑进视窗后，继续滑动触发删除的距离阈值。 默认值：56vp 说明： 不支持设置百分比。 删除距离阈值大于item宽度减去划出组件宽度，或删除距离阈值小于等于0就不会设置删除区域。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onAction | () => void | 否 | 是 | 组件进入长距删除区后抬手时触发。 说明： 滑动后松手的位置超过或等于设置的距离阈值，并且设置的距离阈值有效时才会触发。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onEnterActionArea | () => void | 否 | 是 | 在滑动条目进入删除区域时调用，只触发一次，当再次进入时仍触发。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onExitActionArea | () => void | 否 | 是 | 当滑动条目退出删除区域时调用，只触发一次，当再次退出时仍触发。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| builder | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | 否 | 是 | 当列表项向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列表方向为“水平”时）时显示的操作项。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| builderComponent18+ | [ComponentContent](../misc/ComponentContent.md) | 否 | 是 | 当列表项向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列表方向为“水平”时）时显示的操作项。 说明： 该参数的优先级高于参数builder。即同时设置builder和builderComponent时，以builderComponent设置的值为准。 同一个builderComponent不推荐同时给不同的start/end使用，否则会导致显示问题。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| onStateChange11+ | (state:SwipeActionState) => void | 否 | 是 | 当列表项滑动状态变化时候触发。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### [List](list.md)ItemOptions10+对象说明

[List](list.md)Item组件参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | ListItemStyle | 否 | 是 | 设置List组件卡片样式。 默认值：ListItemStyle.NONE 设置为ListItemStyle.NONE时无样式。 设置为ListItemStyle.CARD时，建议配合[ListItemGroup](ListItemGroup.md)的ListItemGroupStyle.CARD同时使用，显示默认卡片样式。 卡片样式下，ListItem默认规格：高度48vp，宽度100%，左右内边距8vp。如果需要实现ListItem高度自适应，可以把height设置为undefined。 卡片样式下，为卡片内的列表选项提供了默认的focus、hover、press、selected和disable样式。 说明： 当设置为ListItemStyle.CARD时，List的listDirection属性值须为Axis.Vertical，如果设置为Axis.Horizontal，会导致显示混乱；List属性alignListItem默认为ListItemAlign.Center，居中对齐显示。 |

#### [List](list.md)ItemStyle10+枚举说明

[List](list.md)组件卡片样式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无样式。 |
| CARD | 1 | 显示默认卡片样式。 |

#### SwipeActionState11+枚举说明

列表项滑动状态枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLLAPSED | 0 | 收起状态，当[List](list.md)Item向左或向右滑动（当列表方向为“垂直”时）， 向上或向下滑动（当列表方向为“水平”时）时操作项处于隐藏状态。 |
| EXPANDED | 1 | 展开状态，当[List](list.md)Item向左或向右滑动（当列表方向为“垂直”时）， 向上或向下滑动（当列表方向为“水平”时）时操作项处于显示状态。 说明： 需要ListItem设置向左或向右滑动（当列表方向为“垂直”时）， 向上或向下滑动（当列表方向为“水平”时）时显示的操作项。 |
| ACTIONING | 2 | 长距离状态，当[List](list.md)Item进入长距删除区后删除ListItem的状态。 说明： 滑动后松手的位置超过或等于设置的距离阈值，并且设置的距离阈值有效时才能进入该状态。 |

#### 事件

#### onSelect8+

onSelect(event: (isSelected: boolean) => void)

[List](list.md)Item元素被鼠标框选的状态改变时触发回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSelected | boolean | 是 | 进入鼠标框选范围即被选中返回true， 移出鼠标框选范围即未被选中返回false。 |

#### [List](list.md)ItemSwipeActionManager21+

[List](list.md)Item划出菜单的管理器。

#### expand21+

expand(node: [FrameNode](../misc/FrameNode.md), direction: ListItemSwipeActionDirection): void

展开指定[List](list.md)Item的划出菜单。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](../misc/FrameNode.md) | 是 | ListItem节点对象。 |
| direction | [List](list.md)ItemSwipeActionDirection | 是 | ListItem划出菜单的展开方向。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码]([自定义节点错误码](../../errors/自定义节点错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | The component type of the node is incorrect. |
| 106203 | The node not mounted to component tree. |


- 如果[List](list.md)组件cachedCount属性isShow参数设置为true，List显示区域外已预加载完成的ListItem支持展开，否则List显示区域外节点不支持展开。

#### collapse21+

collapse(node: [FrameNode](../misc/FrameNode.md)): void

收起指定[List](list.md)Item的划出菜单。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](../misc/FrameNode.md) | 是 | ListItem节点对象。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码]([自定义节点错误码](../../errors/自定义节点错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | The component type of the node is incorrect. |
| 106203 | The node not mounted to component tree. |

#### [List](list.md)ItemSwipeActionDirection21+枚举说明

[List](list.md)Item划出菜单的展开方向。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 当列表方向是垂直方向时，LTR模式下表示[List](list.md)Item的左边，RTL模式下表示ListItem的右边。当列表是水平方向时，表示ListItem的上边。 |
| END | 1 | 当列表方向是垂直方向时，LTR模式下表示[List](list.md)Item的右边，RTL模式下表示ListItem的左边。当列表是水平方向时，表示ListItem的下边。 |

#### 示例

#### 示例1（创建[List](list.md)Item）

该示例实现了创建[List](list.md)Item的基本用法。

```ets
// xxx.ets
export class ListDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
}

@Entry
@Component
struct ListItemExample {
  private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }.width('90%')
      .scrollBar(BarState.Off)
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
```

#### 示例2（设置划出组件）

该示例展示了[List](list.md)Item设置了swipeAction的横滑效果。

```ets
// xxx.ets
@Entry
@Component
struct ListItemExample2 {
  @State arr: number[] = [0, 1, 2, 3, 4];
  @State enterEndDeleteAreaString: string = 'not enterEndDeleteArea';
  @State exitEndDeleteAreaString: string = 'not exitEndDeleteArea';
  private scroller: ListScroller = new ListScroller();

  @Builder
  itemEnd() {
    Row() {
      Button('Delete').margin('4vp')
      Button('Set').margin('4vp').onClick(() => {
        this.scroller.closeAllSwipeActions();
      })
    }.padding('4vp').justifyContent(FlexAlign.SpaceEvenly)
  }

  build() {
    Column() {
      List({ space: 10, scroller: this.scroller }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('item' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
          .transition(TransitionEffect.OPACITY)
          .swipeAction({
            end: {
              builder: () => {
                this.itemEnd()
              },
              onAction: () => {
                this.getUIContext()?.animateTo({ duration: 1000 }, () => {
                  let index = this.arr.indexOf(item);
                  this.arr.splice(index, 1);
                });
              },
              actionAreaDistance: 56,
              onEnterActionArea: () => {
                this.enterEndDeleteAreaString = 'enterEndDeleteArea';
                this.exitEndDeleteAreaString = 'not exitEndDeleteArea';
              },
              onExitActionArea: () => {
                this.enterEndDeleteAreaString = 'not enterEndDeleteArea';
                this.exitEndDeleteAreaString = 'exitEndDeleteArea';
              }
          })
        }, (item: number) => item.toString())
      }
      Text(this.enterEndDeleteAreaString).fontSize(20)
      Text(this.exitEndDeleteAreaString).fontSize(20)
    }
    .padding(10)
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
}
```

#### 示例3（设置卡片样式）

该示例展示了[List](list.md)Item的卡片样式效果。

```ets
// xxx.ets
@Entry
@Component
struct ListItemExample3 {
  build() {
    Column() {
      List({ space: '4vp', initialIndex: 0 }) {
        ListItemGroup({ style: ListItemGroupStyle.CARD }) {
          ForEach([ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE], (itemStyle: number, index?: number) => {
            ListItem({ style: itemStyle }) {
              Text('' + index)
                .width('100%')
                .textAlign(TextAlign.Center)
            }
          })
        }

        ForEach([ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE], (itemStyle: number, index?: number) => {
          ListItem({ style: itemStyle }) {
            Text('' + index)
              .width('100%')
              .textAlign(TextAlign.Center)
          }
        })
      }
      .width('100%')
      .multiSelectable(true)
      .backgroundColor(0xDCDCDC)
    }
    .width('100%')
    .padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244878.webp)

#### 示例4（通过[ComponentContent](../misc/ComponentContent.md)设置划出组件）

该示例通过[ComponentContent]([ComponentContent](../misc/ComponentContent.md#ZH-CN_TOPIC_0000002497444816__componentcontent-1).md#ZH-CN_TOPIC_0000002553360669__componentcontent-1)设置ListItem中的划出组件操作时显示的操作项。

```ets
// xxx.ets
import { ComponentContent } from '@kit.ArkUI';

class BuilderParams {
  text: string | Resource;
  scroller: ListScroller;
  constructor(text: string | Resource, scroller: ListScroller) {
    this.text = text;
    this.scroller = scroller;
}

@Builder
function itemBuilder(params: BuilderParams) {
  Row() {
    Button(params.text).margin('4vp')
    Button('Set').margin('4vp').onClick(() => {
      params.scroller.closeAllSwipeActions()
    })
  }.padding('4vp').justifyContent(FlexAlign.SpaceEvenly)
}
@Component
struct MyListItem {
  scroller: ListScroller = new ListScroller();
  @State arr: number[] = [0, 1, 2, 3, 4];
  @State project ?: number = 0;
  startBuilder ?: ComponentContent<BuilderParams> = undefined;
  endBuilder ?: ComponentContent<BuilderParams> = undefined;
  builderParam = new BuilderParams('delete', this.scroller);

  aboutToAppear(): void {
    this.startBuilder = new ComponentContent(this.getUIContext(), wrapBuilder(itemBuilder), this.builderParam);
    this.endBuilder = new ComponentContent(this.getUIContext(), wrapBuilder(itemBuilder), this.builderParam);
  }
  GetStartBuilder() {
    this.startBuilder?.update(new BuilderParams('StartDelete', this.scroller));
    return this.startBuilder;
  }
  GetEndBuilder() {
    this.endBuilder?.update(new BuilderParams('EndDelete', this.scroller));
    return this.endBuilder;
  }
  build() {
    ListItem() {
      Text('item' + this.project)
        .width('100%')
        .height(100)
        .fontSize(16)
        .textAlign(TextAlign.Center)
        .borderRadius(10)
        .backgroundColor(0xFFFFFF)
    }
    .transition(TransitionEffect.OPACITY)
    .swipeAction({
      end: {
        builderComponent: this.GetEndBuilder(),
        onAction: () => {
          this.getUIContext()?.animateTo({ duration: 1000 }, () => {
            let index = this.arr.indexOf(this.project);
            this.arr.splice(index, 1);
          });
        },
        actionAreaDistance: 56
      },
      start: {
        builderComponent: this.GetStartBuilder(),
        onAction: () => {
          this.getUIContext()?.animateTo({ duration: 1000 }, () => {
            let index = this.arr.indexOf(this.project);
            this.arr.splice(index, 1);
          });
        },
        actionAreaDistance: 56
      }
    })
    .padding(5)
  }

@Entry
@Component
struct ListItemExample {
  @State arr: number[] = [0, 1, 2, 3, 4];
  private scroller: ListScroller = new ListScroller();

  build() {
    Column() {
      List({ space: 10, scroller: this.scroller }) {
        ListItemGroup() {
          ForEach(this.arr, (project: number) => {
            MyListItem({ scroller: this.scroller, project: project, arr:this.arr })
          }, (item: string) => item)
        }
    .padding(10)
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204839.webp)

#### 示例5（通过[List](list.md)ItemSwipeActionManager管理划出菜单）

从API version 21开始，该示例通过[ListItemSwipeActionManager](#ZH-CN_TOPIC_0000002553200785__listitemswipeactionmanager21)管理ListItem的划出菜单。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ListItemExample5 {
  @Builder
  itemAction(str: string) {
    Row() {
      Button(str).margin('4vp')
    }.padding('4vp').justifyContent(FlexAlign.SpaceEvenly)
  }

  build() {
    Flex({ wrap: FlexWrap.Wrap }) {
      Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.SpaceBetween }) {
        Button('expand start')
          .onClick(() => {
            try {
              let node: FrameNode | null = this.getUIContext().getAttachedFrameNodeById('listItem');
              ListItemSwipeActionManager.expand(node, ListItemSwipeActionDirection.START)
            } catch (error) {
              console.error('Error expand item:', (error as BusinessError).code, (error as BusinessError).message);
            }
          })
        Button('expand end')
          .onClick(() => {
            try {
              let node: FrameNode | null = this.getUIContext().getAttachedFrameNodeById('listItem');
              ListItemSwipeActionManager.expand(node, ListItemSwipeActionDirection.END)
            } catch (error) {
              console.error('Error expand item:', (error as BusinessError).code, (error as BusinessError).message);
            }
          })
        Button('collapse')
          .onClick(() => {
            try {
              let node: FrameNode | null = this.getUIContext().getAttachedFrameNodeById('listItem');
              ListItemSwipeActionManager.collapse(node)
            } catch (error) {
              console.error('Error collapse item:', (error as BusinessError).code, (error as BusinessError).message);
            }
          })
      }
      .margin({ bottom: 10 })

      List({ space: 10 }) {
        ListItem() {
          Text('item')
            .width('100%')
            .height(100)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }
        .id('listItem')
        .transition(TransitionEffect.OPACITY)
        .swipeAction({
          start: {
            builder: () => {
              this.itemAction('start')
          },
          end: {
            builder: () => {
              this.itemAction('end')
            },
          }
        })
      }
      .height('80%')

    }
    .padding(10)
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
  }
```
