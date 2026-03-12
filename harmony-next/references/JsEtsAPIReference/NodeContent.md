# NodeContent

NodeContent是ArkUI提供的[ContentSlot](ContentSlot.md)的管理器。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { NodeContent } from '@kit.ArkUI';
```

#### NodeContent

NodeContent是节点内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor

constructor()

节点内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
import { nativeNode } from 'libNativeNode.so'; // 开发者自己实现的so
import { NodeContent } from '@kit.ArkUI';

@Component
struct Parent {
  private nodeContent: Content = new NodeContent();

  aboutToAppear() {
    // 通过C-API创建节点，并添加到管理器nodeContent上
    nativeNode.createNativeNode(this.nodeContent);
  }

  build() {
    Column() {
      // 显示nodeContent管理器里存放的Native侧的组件
      ContentSlot(this.nodeContent)
    }
  }
}
```

#### addFrameNode12+

addFrameNode(node: FrameNode): void

根据参数将FrameNode添加到NodeContent中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明node[FrameNode](FrameNode.md)是需要添加的FrameNode。

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](自定义节点错误码.md)。

错误码ID错误信息100025The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted."

#### removeFrameNode12+

removeFrameNode(node: FrameNode): void

根据参数将FrameNode从NodeContent中删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明node[FrameNode](FrameNode.md)是需要删除的FrameNode。

**示例：**

添加删除NodeContent中的FrameNode节点。

```ets
// xxx.ets
import { NodeContent, typeNode } from '@kit.ArkUI';

class NodeContentCtrl {
  content: NodeContent;
  textNode: Array<typeNode.Text> = new Array();
  uiContext: UIContext;
  width: number;

  constructor(uiContext: UIContext) {
    this.content = new NodeContent();
    this.uiContext = uiContext;
    this.width = Infinity;
  }

  AddNode() {
    let node = typeNode.createNode(this.uiContext, "Text");
    node.initialize("ContentText:" + this.textNode.length).fontSize(20);
    this.textNode.push(node);
    this.content.addFrameNode(node);
  }

  RemoveNode() {
    let node = this.textNode.pop();
    this.content.removeFrameNode(node);
  }

  RemoveFront() {
    let node = this.textNode.shift();
    this.content.removeFrameNode(node);
  }

  GetContent(): NodeContent {
    return this.content;
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  controller = new NodeContentCtrl(this.getUIContext());

  build() {
    Row() {
      Column() {
        ContentSlot(this.controller.GetContent())
        Button("AddToSlot")
          .onClick(() => {
            this.controller.AddNode();
          })
        Button("RemoveBack")
          .onClick(() => {
            this.controller.RemoveNode();
          })
        Button("RemoveFront")
          .onClick(() => {
            this.controller.RemoveFront();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```