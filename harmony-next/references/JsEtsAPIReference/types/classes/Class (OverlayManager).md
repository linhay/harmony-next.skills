# Class (OverlayManager)

提供绘制浮层的能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 12开始支持。

-

以下API需先使用UIContext中的[getOverlayManager()](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getoverlaymanager12)方法获取到OverlayManager对象，再通过该对象调用对应方法。

-

OverlayManager上节点的层级在Page页面层级之上，在Dialog、Popup、Menu、BindSheet、BindContentCover和Toast等之下。

-

OverlayManager上节点安全区域内外的绘制方式与Page一致，键盘避让方式与Page一致。

-

与OverlayManager相关的属性推荐采用AppStorage来进行应用全局存储，以免切换页面后属性值发生变化从而导致业务错误。

#### add[ComponentContent](../../topics/misc/ComponentContent.md)12+

add[ComponentContent](../../topics/misc/ComponentContent.md)(content: ComponentContent, index?: number): void

在OverlayManager上新增指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](../../topics/misc/ComponentContent.md) | 是 | 在OverlayManager的指定节点上添加此content。  说明：   新增的节点默认处于页面居中，按层级堆叠。 |
| index | number | 否 | 新增节点在OverlayManager上的层级位置。 说明：   当index ≥ 0时，越大，[ComponentContent](../../topics/misc/ComponentContent.md)的层级越高；若多个ComponentContent的index相同，ComponentContent添加的时间越晚层级越高。  当index < 0、index = null或index = undefined时，ComponentContent默认添加至最高层。 当同一个ComponentContent被添加多次时，只保留最后一次添加的ComponentContent。 |

**示例：**

```ets
import { ComponentContent, OverlayManager } from '@kit.ArkUI';

class Params {
  text: string = "";
  offset: Position;

  constructor(text: string, offset: Position) {
    this.text = text;
    this.offset = offset;
}

@Builder
function builderText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
  }.offset(params.offset)
}

@Entry
@Component
struct OverlayExample {
  @State message: string = 'ComponentContent';
  private uiContext: UIContext = this.getUIContext();
  private overlayNode: OverlayManager = this.uiContext.getOverlayManager();
  @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
  @StorageLink('componentContentIndex') componentContentIndex: number = 0;
  @StorageLink('arrayIndex') arrayIndex: number = 0;
  @StorageLink("componentOffset") componentOffset: Position = { x: 0, y: 110 };

  build() {
    Column({ space: 5 }) {
      Button("++componentContentIndex: " + this.componentContentIndex).onClick(() => {
        ++this.componentContentIndex;
      })
      Button("--componentContentIndex: " + this.componentContentIndex).onClick(() => {
        --this.componentContentIndex;
      })
      Button("增加ComponentContent" + this.contentArray.length).onClick(() => {
        let componentContent = new ComponentContent(
          this.uiContext, wrapBuilder<[Params]>(builderText),
          new Params(this.message + (this.contentArray.length), this.componentOffset)
        );
        this.contentArray.push(componentContent);
        this.overlayNode.addComponentContent(componentContent, this.componentContentIndex);
      })
      Button("++arrayIndex: " + this.arrayIndex).onClick(() => {
        ++this.arrayIndex;
      })
      Button("--arrayIndex: " + this.arrayIndex).onClick(() => {
        --this.arrayIndex;
      })
      Button("删除ComponentContent" + this.arrayIndex).onClick(() => {
        if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
          let componentContent = this.contentArray.splice(this.arrayIndex, 1);
          this.overlayNode.removeComponentContent(componentContent.pop());
        } else {
          console.info("arrayIndex有误");
        }
      })
      Button("显示ComponentContent" + this.arrayIndex).onClick(() => {
        if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
          let componentContent = this.contentArray[this.arrayIndex];
          this.overlayNode.showComponentContent(componentContent);
        } else {
          console.info("arrayIndex有误");
        }
      })
      Button("隐藏ComponentContent" + this.arrayIndex).onClick(() => {
        if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
          let componentContent = this.contentArray[this.arrayIndex];
          this.overlayNode.hideComponentContent(componentContent);
        } else {
          console.info("arrayIndex有误");
        }
      })
      Button("显示所有ComponentContent").onClick(() => {
        this.overlayNode.showAllComponentContents();
      })
      Button("隐藏所有ComponentContent").onClick(() => {
        this.overlayNode.hideAllComponentContents();
      })
    }
    .width('100%')
    .height('100%')
}
```

#### add[ComponentContent](../../topics/misc/ComponentContent.md)WithOrder18+

add[ComponentContent](../../topics/misc/ComponentContent.md)WithOrder(content: ComponentContent, levelOrder?: LevelOrder): void

创建浮层节点时，指定显示顺序。

支持在浮层节点创建时指定显示的顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](../../topics/misc/ComponentContent.md) | 是 | 在OverlayManager的指定节点上添加此content。  说明：   新增的节点默认处于页面居中位置，按层级堆叠。 |
| levelOrder | LevelOrder | 否 | 新增浮层节点的显示顺序。 说明： - 默认值：LevelOrder.clamp(0) |

**示例：**

该示例通过调用add[ComponentContent](../../topics/misc/ComponentContent.md)WithOrder接口，实现了按照指定显示顺序创建浮层节点的功能。

```ets
import { ComponentContent, PromptAction, LevelOrder, UIContext, OverlayManager } from '@kit.ArkUI';

class Params {
  text: string = "";
  offset: Position;
  constructor(text: string, offset: Position) {
    this.text = text;
    this.offset = offset;
}
@Builder
function builderText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
  }.offset(params.offset)
}

@Entry
@Component
struct Index {
  @State message: string = '弹窗';
  private ctx: UIContext = this.getUIContext();
  private promptAction: PromptAction = this.ctx.getPromptAction();
  private overlayNode: OverlayManager = this.ctx.getOverlayManager();
  @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
  @StorageLink('componentContentIndex') componentContentIndex: number = 0;
  @StorageLink('arrayIndex') arrayIndex: number = 0;
  @StorageLink("componentOffset") componentOffset: Position = { x: 0, y: 80 };

  build() {
    Row() {
      Column({ space: 10 }) {
        Button('OverlayManager下面弹窗')
          .fontSize(20)
          .onClick(() => {
            let componentContent = new ComponentContent(
              this.ctx, wrapBuilder<[Params]>(builderText),
              new Params(this.message + (this.contentArray.length), this.componentOffset)
            );
            this.contentArray.push(componentContent);
            this.overlayNode.addComponentContentWithOrder(componentContent, LevelOrder.clamp(100.1));
            let topOrder: LevelOrder = this.promptAction.getTopOrder();
            if (topOrder !== undefined) {
              console.error('topOrder: ' + topOrder.getOrder());
            }
            let bottomOrder: LevelOrder = this.promptAction.getBottomOrder();
            if (bottomOrder !== undefined) {
              console.error('bottomOrder: ' + bottomOrder.getOrder());
            }
          })
        Button('OverlayManager上面弹窗')
          .fontSize(20)
          .onClick(() => {
            let componentContent = new ComponentContent(
              this.ctx, wrapBuilder<[Params]>(builderText),
              new Params(this.message + (this.contentArray.length), this.componentOffset)
            );
            this.contentArray.push(componentContent);
            this.overlayNode.addComponentContentWithOrder(componentContent, LevelOrder.clamp(100.2));
            let topOrder: LevelOrder = this.promptAction.getTopOrder();
            if (topOrder !== undefined) {
              console.error('topOrder: ' + topOrder.getOrder());
            }
            let bottomOrder: LevelOrder = this.promptAction.getBottomOrder();
            if (bottomOrder !== undefined) {
              console.error('bottomOrder: ' + bottomOrder.getOrder());
            }
          })
      }.width('100%')
    }.height('100%')
  }
```

#### remove[ComponentContent](../../topics/misc/ComponentContent.md)12+

remove[ComponentContent](../../topics/misc/ComponentContent.md)(content: ComponentContent): void

删除overlay上的指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](../../topics/misc/ComponentContent.md) | 是 | 在OverlayManager上删除此content。 |

**示例：**

请参考[addComponentContent示例](#ZH-CN_TOPIC_0000002553360655__addcomponentcontent12)。

#### show[ComponentContent](../../topics/misc/ComponentContent.md)12+

show[ComponentContent](../../topics/misc/ComponentContent.md)(content: ComponentContent): void

在OverlayManager上显示指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](../../topics/misc/ComponentContent.md) | 是 | 在OverlayManager上显示此content。 |

**示例：**

请参考[addComponentContent示例](#ZH-CN_TOPIC_0000002553360655__addcomponentcontent12)。

#### hide[ComponentContent](../../topics/misc/ComponentContent.md)12+

hide[ComponentContent](../../topics/misc/ComponentContent.md)(content: ComponentContent): void

隐藏OverlayManager上的指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](../../topics/misc/ComponentContent.md) | 是 | 在OverlayManager上隐藏此content。 |

**示例：**

请参考[addComponentContent示例](#ZH-CN_TOPIC_0000002553360655__addcomponentcontent12)。

#### showAll[ComponentContent](../../topics/misc/ComponentContent.md)s12+

showAll[ComponentContent](../../topics/misc/ComponentContent.md)s(): void

显示OverlayManager上所有的[ComponentContent](../../topics/misc/ComponentContent.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[addComponentContent示例](#ZH-CN_TOPIC_0000002553360655__addcomponentcontent12)。

#### hideAll[ComponentContent](../../topics/misc/ComponentContent.md)s12+

hideAll[ComponentContent](../../topics/misc/ComponentContent.md)s(): void

隐藏OverlayManager上的所有[ComponentContent](../../topics/misc/ComponentContent.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[addComponentContent示例](#ZH-CN_TOPIC_0000002553360655__addcomponentcontent12)。