# @ohos.accessibility.GesturePoint (手势触摸点)

GesturePoint表示手势触摸点。

本模块用于创建辅助功能注入手势所需的手势路径的触摸点信息。

- 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { GesturePoint } from '@kit.AccessibilityKit';
```

#### GesturePoint

表示手势触摸点。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### 属性

名称类型只读可选说明positionXnumber否否触摸点X坐标。positionYnumber否否触摸点Y坐标。

#### constructor(deprecated)

constructor(positionX: number, positionY: number);

构造函数。

从API version 12开始废弃。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明positionXnumber是触摸点X坐标。positionYnumber是触摸点Y坐标。

**示例：**

```ets
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```