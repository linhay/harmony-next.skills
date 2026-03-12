# @arkts.lang (ArkTS语言基础能力)

本模块提供的ArkTS语言的基础类型定义。当前提供ISendable接口。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

#### 导入模块

```ets
import { lang } from '@kit.ArkTS';
```

#### lang.ISendable

是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

ISendable类型的对象是ArkTS中的Object类型的实例。

ISendable主要用在开发者自定义Sendable数据结构的场景中，ArkTS语言标准库中的容器类型隐式地继承并实现了ISendable。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**示例：**

```ets
// 构造一个用户自定义的Sendable数据结构
@Sendable
class CustomData implements lang.ISendable {
    data1: number;
    data2: string;
    constructor(data1: number, data2: string) {
        this.data1 = data1;
        this.data2 = data2;
    }
}
```