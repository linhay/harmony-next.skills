# XComponentNode

提供XComponent节点XComponentNode，表示组件树中的[XComponent](XComponent.md)组件，用于[EGL](EGL.md)/[OpenGLES](OpenGL ES.md)和媒体数据写入，并支持动态修改节点渲染类型。

从API version 12开始废弃，建议使用[类型为XComponent的typeNode](FrameNode.md#ZH-CN_TOPIC_0000002529284787__xcomponent12)的方式实现。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

当前不支持在预览器中使用XComponentNode。

#### 导入模块

```ets
import { XComponentNode } from "@kit.ArkUI";
```

#### XComponentNode

#### constructor

constructor(uiContext: UIContext, options: RenderOptions, id: string, type: XComponentType, libraryName?: string)

XComponentNode的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明uiContext[UIContext](Class (UIContext).md)是UI上下文，获取方式可参考[UIContext获取方法](@ohos.arkui.node.md#ZH-CN_TOPIC_0000002529284763__uicontext获取方法)。options[RenderOptions](BuilderNode.md#ZH-CN_TOPIC_0000002497604794__renderoptions)是XComponentNode的构造可选参数。idstring是XComponent的唯一标识，支持最大的字符串长度128。详见[XComponent](XComponent.md)组件。type[XComponentType](枚举说明.md#ZH-CN_TOPIC_0000002529284967__xcomponenttype10)是用于指定XComponent组件类型。详见[XComponent](XComponent.md)组件。libraryNamestring否Native层编译输出动态库名称。详见[XComponent](XComponent.md)组件。

需要显式指定[RenderOptions](BuilderNode.md#ZH-CN_TOPIC_0000002497604794__renderoptions)中的selfIdealSize，否则XComponentNode内容大小为空，不显示任何内容。

#### onCreate

onCreate(event?: Object): void

XComponentNode加载完成时触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明eventObject否获取XComponent实例对象的context，context上挂载的方法由开发者在C++层定义。

#### onDestroy

onDestroy(): void

XComponentNode销毁时触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### changeRenderType

changeRenderType(type: NodeRenderType): boolean

修改XComponentNode的渲染类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明type[NodeRenderType](BuilderNode.md#ZH-CN_TOPIC_0000002497604794__noderendertype)是需要修改的渲染类型。

**返回值：**

类型说明boolean

修改渲染类型是否成功。

true：修改渲染类型成功；false：修改渲染类型失败。

#### 示例

```ets
import { NodeController, FrameNode, XComponentNode, NodeRenderType, UIContext} from '@kit.ArkUI'

class XComponentNodeController extends NodeController {
  private xComponentNode: MyXComponentNode | null = null;
  private soName: string = "tetrahedron_napi" // 该 so 由开发者通过 NAPI 编写并生成

  constructor() {
    super();
  }

  makeNode(context: UIContext): FrameNode | null {
    this.xComponentNode = new MyXComponentNode(context, {
      selfIdealSize: { width: 200, height: 200 }
    }, "xComponentId", XComponentType.SURFACE, this.soName);
    return this.xComponentNode;
  }

  changeRenderType(renderType: NodeRenderType): void {
    if (this.xComponentNode) {
      this.xComponentNode.changeRenderType(renderType);
    }
  }
}

class MyXComponentNode extends XComponentNode {
  onCreate(event: Object) {
    // do something when XComponentNode has created
  }

  onDestroy() {
    // do something when XComponentNode is destroying
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        NodeContainer(new XComponentNodeController())
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```