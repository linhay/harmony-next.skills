# GridItem

网格容器中单项内容容器。

- 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 仅支持作为[Grid](Grid.md)组件的子组件使用。
- 当GridItem配合[LazyForEach](LazyForEach.md)使用时，GridItem子组件在GridItem创建时创建。配合[if/else](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)、[ForEach](ForEach.md)使用时，或父组件为Grid时，GridItem子组件在GridItem布局时创建。

- 当Grid中存在大量GridItem时，使用[columnStart](#ZH-CN_TOPIC_0000002522080826__columnstart)/[columnEnd](#ZH-CN_TOPIC_0000002522080826__columnend)、[rowStart](#ZH-CN_TOPIC_0000002522080826__rowstart)/[rowEnd](#ZH-CN_TOPIC_0000002522080826__rowend)设置GridItem大小会导致在使用scrollToIndex滑动到指定Index时，依次遍历GridItem节点，耗时较长。建议使用[GridLayoutOptions](Grid.md#ZH-CN_TOPIC_0000002553200787__gridlayoutoptions10对象说明)布局，以提高查找GridItem位置的效率。最佳实践请参考[优化Grid组件加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve_grid_performance)。

#### 子组件

可以包含单个子组件。

#### 接口

GridItem(value?: GridItemOptions)

创建网格容器中单项内容容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value11+ | GridItemOptions | 否 | 为GridItem提供可选参数，该对象内含有GridItemStyle枚举类型的style参数。 |

#### 属性

#### rowStart

rowStart(value: number)

设置当前元素起始行号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素起始行号。 需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](Grid.md#ZH-CN_TOPIC_0000002529444839__gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](Grid.md#ZH-CN_TOPIC_0000002529444839__示例1固定行列grid)和[Grid的示例3](Grid.md#ZH-CN_TOPIC_0000002529444839__示例3可滚动grid设置跨行跨列节点)。 取值范围：[0, 总行数-1] |

#### rowEnd

rowEnd(value: number)

设置当前元素终点行号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素终点行号。 需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](Grid.md#ZH-CN_TOPIC_0000002529444839__gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](Grid.md#ZH-CN_TOPIC_0000002529444839__示例1固定行列grid)和[Grid的示例3](Grid.md#ZH-CN_TOPIC_0000002529444839__示例3可滚动grid设置跨行跨列节点)。 取值范围：[0, 总行数-1] |

#### columnStart

columnStart(value: number)

设置当前元素起始列号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素起始列号。 需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](Grid.md#ZH-CN_TOPIC_0000002529444839__gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](Grid.md#ZH-CN_TOPIC_0000002529444839__示例1固定行列grid)和[Grid的示例3](Grid.md#ZH-CN_TOPIC_0000002529444839__示例3可滚动grid设置跨行跨列节点)。 取值范围：[0, 总列数-1] |

#### columnEnd

columnEnd(value: number)

设置当前元素终点列号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素终点列号。 需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](Grid.md#ZH-CN_TOPIC_0000002529444839__gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](Grid.md#ZH-CN_TOPIC_0000002529444839__示例1固定行列grid)和[Grid的示例3](Grid.md#ZH-CN_TOPIC_0000002529444839__示例3可滚动grid设置跨行跨列节点)。 取值范围：[0, 总列数-1] |

需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](Grid.md#ZH-CN_TOPIC_0000002553200787__gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](Grid.md#ZH-CN_TOPIC_0000002553200787__示例1固定行列grid)和[Grid的示例3](Grid.md#ZH-CN_TOPIC_0000002553200787__示例3可滚动grid设置跨行跨列节点)。

起始行号、终点行号、起始列号、终点列号生效规则如下：

-

rowStart/rowEnd合理取值范围为0~总行数-1，columnStart/columnEnd合理取值范围为0~总列数-1。

-

如果设置了rowStart/rowEnd/columnStart/columnEnd，GridItem会占据指定的行数(rowEnd-rowStart+1)或列数(columnEnd-columnStart+1)。

-

只有在设置columnsTemplate和rowsTemplate的Grid中，设置合理的rowStart/rowEnd/columnStart/columnEnd四个属性的GridItem才能按照指定的行列号布局。

-

在设置columnsTemplate和rowsTemplate的Grid中，单独设置行号rowStart/rowEnd或列号columnStart/columnEnd的GridItem会按照一行一列进行布局。

-

在只设置columnsTemplate的Grid中设置列号columnStart/columnEnd的GridItem按照列数布局。在该区域位置存在GridItem布局，则直接换行进行放置。

-

在只设置rowsTemplate的Grid中设置行号rowStart/rowEnd的GridItem按照行数布局。在该区域位置存在GridItem布局，则直接换列进行放置。

-

columnsTemplate和rowsTemplate都不设置的Grid中GridItem的行列号属性无效。

以下是GridItem行列号异常值的处理规则：

| 属性设置情况 | 异常类型 | 修正后布局规则 |
| --- | --- | --- |
| 仅设置columnsTemplate | 任意行列异常 | 按一行一列布局。 |
| 仅设置rowsTemplate | 任意行列异常 | 按一行一列布局。 |
| 同时设置rows/columnsTemplate | rowStart < rowEnd | 行跨度 = min(rowEnd-rowStart+1, 总行数)。 |
| 同时设置rows/columnsTemplate | rowStart > rowEnd | 按一行一列布局。 |
| 同时设置rows/columnsTemplate | columnStart < columnEnd | 列跨度 = min(columnEnd-columnStart+1, 总列数)。 |
| 同时设置rows/columnsTemplate | columnStart > columnEnd | 按一行一列布局。 |

#### forceRebuild(deprecated)

forceRebuild(value: boolean)

设置在触发组件build时是否重新创建此节点。

从API version 7开始支持，从API version 9开始废弃。GridItem会根据自身属性和子组件变化自行决定是否需要重新创建，无需设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 在触发组件build时是否重新创建此节点。 默认值：false |

#### selectable8+

selectable(value: boolean)

设置当前GridItem元素是否可以被鼠标框选。外层Grid容器的鼠标框选开启时，GridItem的框选才生效。

该属性需要在设置[多态样式](多态样式.md)前使用才能生效[选中态样式](多态样式.md#ZH-CN_TOPIC_0000002497604846__statestyles)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前GridItem元素是否可以被鼠标框选。设置为true时可以被鼠标框选，设置为false时无法被鼠标框选。 默认值：true |

#### selected10+

selected(value: boolean)

设置当前GridItem选中状态。该属性支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

该属性需要在设置[多态样式](多态样式.md)前使用才能生效[选中态样式](多态样式.md#ZH-CN_TOPIC_0000002497604846__statestyles)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前GridItem选中状态。设置为true时为选中状态，设置为false时为默认状态。 默认值：false |

#### GridItemOptions11+对象说明

GridItem样式对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | GridItemStyle | 否 | 是 | 设置GridItem样式。 默认值：GridItemStyle.NONE 设置为GridItemStyle.NONE时无样式。 设置为GridItemStyle.PLAIN时，显示Hover、Press态样式。 |

#### GridItemStyle11+枚举说明

GridItem样式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无样式。 |
| PLAIN | 1 | 显示Hover、Press态样式。 |


GridItem焦点态样式设置：Grid组件需要设置4vp规格以上的内边距，用于显示GridItem的焦点框。

#### 事件

#### onSelect8+

onSelect(event: (isSelected: boolean) => void)

GridItem元素被鼠标框选的状态改变时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSelected | boolean | 是 | 进入鼠标框选范围即被选中返回true， 移出鼠标框选范围即未被选中返回false。 |

#### 示例

#### 示例1（GridItem设置自身位置）

GridItem通过设置合理的ColumnStart、ColumnEnd、RowStart、RowEnd属性来设置自身位置。需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](Grid.md#ZH-CN_TOPIC_0000002553200787__gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](Grid.md#ZH-CN_TOPIC_0000002553200787__示例1固定行列grid)和[Grid的示例3](Grid.md#ZH-CN_TOPIC_0000002553200787__示例3可滚动grid设置跨行跨列节点)。

```ets
// xxx.ets
@Entry
@Component
struct GridItemExample {
  @State numbers: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'];

  build() {
    Column() {
      Grid() {
        GridItem() {
          Text('4')
            .fontSize(16)
            .backgroundColor(0xFAEEE0)
            .width('100%')
            .height('100%')
            .textAlign(TextAlign.Center)
        }.rowStart(1).rowEnd(2).columnStart(1).columnEnd(2) // 同时设置合理的行列号

        ForEach(this.numbers, (item: string) => {
          GridItem() {
            Text(item)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center)
          }
        }, (item: string) => item)

        GridItem() {
          Text('5')
            .fontSize(16)
            .backgroundColor(0xDBD0C0)
            .width('100%')
            .height('100%')
            .textAlign(TextAlign.Center)
        }.columnStart(1).columnEnd(4) // 只设置列号，不会从第1列开始布局
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
      .width('90%').height(300)
    }.width('100%').margin({ top: 5 })
  }
```

#### 示例2（设置GridItem样式）

使用GridItemOptions设置GridItem样式。

```ets
// xxx.ets
@Entry
@Component
struct GridItemExample {
  @State numbers: String[] = ['0', '1', '2'];

  build() {
    Column({ space: 5 }) {
      Grid() {
        ForEach(this.numbers, (day: string) => {
            GridItem({style:GridItemStyle.NONE}) {
              Text(day)
                .fontSize(16)
                .width('100%')
                .height('100%')
                .textAlign(TextAlign.Center)
                .focusable(true)
            }
            .backgroundColor(0xF9CF93)
        }, (day: string) => day)
      }
      .columnsTemplate('1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr')
      .columnsGap(4)
      .rowsGap(4)
      .width('60%')
      .backgroundColor(0xFAEEE0)
      .height(150)
      .padding('4vp')

      Grid() {
        ForEach(this.numbers, (day: string) => {
            GridItem({style:GridItemStyle.PLAIN}) {
              Text(day)
                .fontSize(16)
                .width('100%')
                .height('100%')
                .textAlign(TextAlign.Center)
                .focusable(true)
            }
            .backgroundColor(0xF9CF93)
        }, (day: string) => day)
      }
      .columnsTemplate('1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr')
      .columnsGap(4)
      .rowsGap(4)
      .width('60%')
      .backgroundColor(0xFAEEE0)
      .height(150)
      .padding('4vp')
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364817.webp)
