# HdsListItem

该组件可设置ListItem的横滑动效，可以承载HdsListItemCard组件。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { HdsListItem } from '@kit.UIDesignKit';
```

#### 接口

HdsListItem({customItemBuilder?: CustomBuilder, hdsListItemCard?: HdsListItemCardOptions, swipeActionOptions?: HdsSwipeActionOptions | SwipeActionOptions, listItemModifier?: ListItemModifier})

提供了一个列表组件。

**装饰器类型：**@Component

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**设备行为异常：**该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：**6.0.0(20)

参数名

类型

必填

装饰器类型

说明

customItemBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

否

@BuilderParam

自定义列表卡片项内容，全局自定义函数需要使用Function.bind(this)的方式传入（Function为自定义函数）。

hdsListItemCard

[HdsListItemCardOptions](HdsListItemCard.md#section6323195713321)

否

-

列表卡片项内容。

swipeActionOptions

[HdsSwipeActionOptions](#section10384044394) | [SwipeActionOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#swipeactionoptions9对象说明)

否

-

动效横滑内容展示。

HdsSwipeActionOptions是HdsListItem封装后的横滑动效类型，SwipeActionOptions支持用户自定义使用ListItem的横滑动效类型。

listItemModifier

[ListItemModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

-

ListItem属性样式修改器。

**起始版本：**6.0.1(21)

该接口中customItemBuilder优先级高于hdsListItemCard。当同时设置customItemBuilder和hdsListItemCard时，customItemBuilder生效。

#### HdsSwipeActionOptions

设置横滑按钮的样式。

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

icons

Array<[SwipeIconConfigurations](#section113942388296)>

否

是

配置除删除按钮之外其他三个按钮样式。

deleteIconOptions

[DeleteIconOptions](#section17257185014306)

否

是

配置删除按钮样式。

fullDeleteOptions

[FullDeleteOptions](#section184131316173219)

否

是

配置滑动距离超过划出组件大小后的行为。

#### IconOptions

设置图标的可用性和无障碍等属性。

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

enable

boolean

否

是

图标是否被启用。

true：图标被启用。

false：图标被禁用。

默认值：true。

accessibilityText

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

图标的无障碍文本属性。

当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。

默认值：""。

accessibilityDescription

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

图标的无障碍描述。

此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值：“单指双击即可执行”。

accessibilityLevel

string

否

是

图标的无障碍重要性，用于控制当前项是否可被无障碍辅助服务所识别。

支持的值为：

"auto"：当前组件会转换"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

#### SwipeIconConfigurations

设置除删除图标外的横滑图标样式和功能。

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

icon

[SwipeIconType](#section2930111714251)

否

否

图标资源，可支持symbol或image类型。

iconOptions

[IconOptions](#section1486115401)

否

是

图标的能力选项。

backgroundColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

图标背景色。

onAction

[SwipeActionCallback](#section812564671318)

否

是

点击回调。

#### DeleteIconOptions

设置删除图标属性。

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

backgroundColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

删除按钮图标背景色。

iconColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

删除按钮图标颜色。

iconOptions

[IconOptions](#section1486115401)

否

是

删除按钮图标的能力选项。

onAction

[SwipeActionCallback](#section812564671318)

否

是

点击回调。

#### FullDeleteOptions

设置横滑之后再次滑动是否删除整个列表项及列表项删除的回调。

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

isFullDelete

boolean

否

是

横滑之后再次滑动是否删除整个列表项。

- true：横滑之后再次滑动删除该列表项。
- false：横滑之后再次滑动不删除该列表项。

默认值：false。

onFullDeleteAction

[SwipeActionCallback](#section812564671318)

否

是

列表项删除的回调。

#### SwipeIconType

type SwipeIconType = SymbolGlyphModifier | ImageOptions

横滑图标资源类型。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**返回值**:

类型

说明

[SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

symbol资源类型。

[ImageOptions](HdsListItemCard.md#section3582112115362)

image资源类型。

#### SwipeActionCallback

type SwipeActionCallback = () => void

列表滑动事件触发的回调函数。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

#### 示例

设置一个带横滑效果的列表：

```ets
import { promptAction, SymbolGlyphModifier, TextModifier } from '@kit.ArkUI';
import { HdsListItem } from '@kit.UIDesignKit';

@Entry
@Component
struct HdsListItemExample {
  @State dataSource: LazyDataSource<Item> = new LazyDataSource();
  @State dataArr: Array<Item> = [];
  @State EndOffset: number = 0;
  private scroller: Scroller = new Scroller();

  build() {
    Column() {
      List({ space: 10, scroller: this.scroller }) {
        LazyForEach(this.dataSource, (item: Item) => {
          HdsListItem({
            hdsListItemCard: {
              textItem: {
                primaryText: {
                  text: 'Primary Text',
                  modifier: new TextModifier().fontColor(Color.Orange).fontSize(16),
                }
              }
            },
            swipeActionOptions: {
              icons: [
                {
                  icon: new SymbolGlyphModifier($r('sys.symbol.share')).fontColor([Color.Red]).fontSize(16),
                  backgroundColor: Color.Green,
                  onAction: () => {
                    promptAction.openToast({ message: '点击share按钮', duration: 100 });
                  },
                },
                {
                  icon: new SymbolGlyphModifier($r('sys.symbol.plus_square_on_square')),
                  backgroundColor: Color.Orange,
                  onAction: () => {
                    promptAction.openToast({ message: '点击copy按钮', duration: 100 });
                  },
                },
                {
                  icon: new SymbolGlyphModifier($r('sys.symbol.plus_square_dashed_on_square'))
                          .symbolEffect(new BounceSymbolEffect(), true),
                  onAction: () => {
                    promptAction.openToast({ message: '点击paste按钮', duration: 100 });
                  },
                },
              ],
              deleteIconOptions: {
                backgroundColor: Color.Red, //  ---修改背景色
                iconColor: Color.Gray, //  ---- 修改垃圾桶的颜色
                onAction: () => {
                  promptAction.openToast({ message: '点击删除按钮', duration: 100 });
                }, //   --点击回调
              },
              fullDeleteOptions: {
                isFullDelete: true, // --- 划动距离超过划出组件大小后自动触发删除，默认是false
                onFullDeleteAction: () => {
                  promptAction.openToast({ message: '触发自动删除', duration: 100 });
                  this.getUIContext()?.animateTo({
                    duration: 350,
                  }, () => {
                    this.dataSource.deleteItem(item)
                  });
                }, //   -- 触发删除时的回调
              },
            }
          })
        }, (item: Item) => item.data)
      }
      .scrollBar(BarState.Off)
      .onDidScroll((scrollOffset: number) => {
        this.EndOffset = scrollOffset
      })
      .margin(10)
      .width('100%')
      .height('100%')
    }
    .backgroundColor('#0D182431')
    .width('100%')
    .height('100%')
  }

  aboutToAppear() {
    for (let i = 0; i < 2; i++) {
      this.dataSource.pushItem(new Item(i + ''));
      this.dataArr.push(new Item(i + ''));
    }
  }
}

class Item {
  constructor(data: string) {
    this.data = data;
  }

  public data: string = '';
}

export class LazyDataSource<T> implements IDataSource {
  private elements: T[];
  private listeners: Set<DataChangeListener>;

  constructor(elements: T[] = []) {
    this.elements = elements;
    this.listeners = new Set();
  }

  public totalCount(): number {
    return this.elements.length;
  }

  public getData(index: number): T {
    return this.elements[index];
  }

  public indexOf(item: T): number {
    return this.elements.indexOf(item);
  }

  public pinItem(item: T, index: number): void {
    this.elements.splice(index, 1);
    this.elements.unshift(item);
    this.listeners.forEach(listener => listener.onDataReloaded());
  }

  public pushItem(item: T) {
    this.elements.push(item);
    this.listeners.forEach(listener => listener.onDataAdd(this.elements.length - 1));
  }

  public deleteItem(item: T): void {
    const index = this.elements.indexOf(item);
    if (index < 0) {
      return;
    }
    this.elements.splice(index, 1);
    this.listeners.forEach(listener => listener.onDataDelete(index));
  }

  public deleteItemByIndex(index: number): void {
    this.elements.splice(index, 1);
    this.listeners.forEach(listener => listener.onDataDelete(index));
  }

  public registerDataChangeListener(listener: DataChangeListener): void {
    this.listeners.add(listener);
  }

  public unregisterDataChangeListener(listener: DataChangeListener): void {
    this.listeners.delete(listener);
  }
}
```

效果图：