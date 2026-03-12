# FlowItem

[瀑布流组件](WaterFlow.md)的子组件，用来展示瀑布流具体item。

- 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 仅支持作为[WaterFlow](WaterFlow.md)组件的子组件使用。
- 在滑动场景中，由于FlowItem及其子组件的频繁创建与销毁，建议将FlowItem中的组件封装为自定义组件，并使用@Reusable装饰器进行修饰，以增强组件的复用能力，从而减少ArkUI框架内部重复创建和销毁节点的开销。最佳实践请参考[优化瀑布流加载慢丢帧问题-组件复用](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-waterflow-performance-optimization#section189041489339)。

#### 子组件

支持单个子组件。

#### 接口

FlowItem()

使用该接口来创建瀑布流子组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

无

#### 示例

详见[瀑布流组件示例](WaterFlow.md#ZH-CN_TOPIC_0000002497604876__示例)。