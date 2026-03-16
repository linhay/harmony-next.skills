# @ohos.accessibility.GesturePath (手势路径)

GesturePath表示手势路径信息。

本模块用于创建辅助功能注入手势所需的手势路径信息。

- 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { GesturePath } from '@kit.AccessibilityKit';
```

#### GesturePath

表示手势路径信息。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### 属性

名称类型只读可选说明pointsArray<[GesturePoint](@ohos.accessibility.GesturePoint (手势触摸点).md#ZH-CN_TOPIC_0000002497444696__gesturepoint)>否否手势触摸点。durationTimenumber否否手势总耗时，单位为毫秒。

#### constructor(deprecated)

constructor(durationTime: number);

构造函数。

从API version 12开始废弃。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明durationTimenumber是手势总耗时，单位为毫秒。

**示例：**

```ets
import { GesturePath } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
```