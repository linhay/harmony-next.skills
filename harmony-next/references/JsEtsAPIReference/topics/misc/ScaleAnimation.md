# ScaleAnimation

#### 导入模块

```ets
import { map } from '@kit.MapKit';
```

#### ScaleAnimation

控制缩放的动画类，继承[Animation](Animation.md)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

#### constructor

constructor(fromX: number, toX: number, fromY: number, toY: number)

构造器，构造控制缩放的动画实例。

0表示缩小消失。

1表示不缩放。

小于1的值表示缩小。

大于1的值表示放大。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

fromX

number

是

指动画开始时应用的水平缩放倍数。

toX

number

是

指动画结束时应用的水平缩放倍数。

fromY

number

是

指动画开始时应用的垂直缩放倍数。

toY

number

是

指动画结束时应用的垂直缩放倍数。

**示例：**

```ets
let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
```