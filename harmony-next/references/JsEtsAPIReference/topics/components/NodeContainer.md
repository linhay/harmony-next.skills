# NodeContainer

基础组件，用于挂载自定义节点（如[FrameNode](FrameNode.md)或[BuilderNode](BuilderNode.md)），并通过[NodeController](NodeController.md)动态控制节点的上树和下树。组件不支持尾随添加子节点，接受一个[NodeController](NodeController.md)实例接口，需与NodeController组合使用。

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件下仅支持挂载自定义节点[FrameNode](FrameNode.md)或者是[BuilderNode](BuilderNode.md)中获取的根节点FrameNode。

不支持挂载查询获得的系统组件[代理节点](FrameNode.md#ZH-CN_TOPIC_0000002529284787__ismodifiable12)。

当前不支持使用[动态属性设置](../misc/动态属性设置.md)。

该组件下的节点树构建中会使用UI实例[UIContext](../../types/classes/Class (UIContext).md)，当实例切换时可能会因为实例不匹配而出现问题，因此该组件当前不支持跨实例的节点复用。

该组件未销毁时，不会主动触发挂载节点的下树。

#### 子组件

不支持子组件。

#### 接口

#### NodeContainer

NodeContainer(controller: NodeController)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明controller[NodeController](NodeController.md)是NodeController用于控制NodeContainer中的节点的上树和下树，反映NodeContainer容器的生命周期。

#### 属性

支持[通用属性](../misc/通用属性.md)。

#### 事件

支持[通用事件](../misc/通用事件.md)。

#### 示例

通过NodeController挂载BuilderNode节点。

```ets
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

declare class Params {
  text: string
}

@Builder
function buttonBuilder(params: Params) {
  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {
    Text(params.text)
      .fontSize(12)
    Button(`This is a Button`, { type: ButtonType.Normal, stateEffect: true })
      .fontSize(12)
      .borderRadius(8)
      .backgroundColor(0x317aff)
  }
  .height(100)
  .width(200)
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<[Params]> | null = null;
  private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.rootNode === null) {
      this.rootNode = new BuilderNode(uiContext);
      this.rootNode.build(this.wrapBuilder, { text: "This is a Text" })
    }
    return this.rootNode.getFrameNode();
  }
}

@Entry
@Component
struct Index {
  private baseNode: MyNodeController = new MyNodeController()

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceEvenly }) {
      Text("This is a NodeContainer contains a text and a button ")
        .fontSize(9)
        .fontColor(0xCCCCCC)
      NodeContainer(this.baseNode)
        .borderWidth(1)
        .onClick(() => {
          console.info("click event");
        })
    }
    .padding({ left: 35, right: 35, top: 35 })
    .height(200)
    .width(300)
  }
}
```