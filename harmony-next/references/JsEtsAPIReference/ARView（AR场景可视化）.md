# ARView（AR场景可视化）

用于承载ARViewContext，实现AR场景可视化呈现。

需要与[arViewController](arViewController（AR场景管理能力）.md)配合一起使用，完成AR场景的可视化呈现。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

#### 导入模块

```ets
import { ARView, arViewController } from '@kit.AREngine';
```

#### ARView

该类为AR场景可视化呈现组件。

**装饰器类型：**@Component

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

名称

类型

必填

装饰器类型

说明

context

[arViewController](arViewController（AR场景管理能力）.md).[ARViewContext](arViewController（AR场景管理能力）.md#section12681656121519)

是

@Require

@State

ARView上下文、AR会话和场景的状态管理。

#### build

build(): void

用于创建ARView对象的构造函数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**示例**：

```ets
import { ARView, arViewController } from '@kit.AREngine';

let arContext: arViewController.ARViewContext = new arViewController.ARViewContext();

@Entry
@Component
struct ARWorld {
  // context配置及初始化
  build() {
    RelativeContainer() {
      if (arContext) {
        ARView({ context: arContext })
          .height('100%')
          .width('100%')
      }
    }
  }
}
```