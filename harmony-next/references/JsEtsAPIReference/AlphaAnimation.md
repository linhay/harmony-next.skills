# AlphaAnimation

#### 导入模块

```ets
import { map } from '@kit.MapKit';
```

#### AlphaAnimation

控制透明度的动画类，继承[Animation](Animation.md)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

#### constructor

constructor(fromAlpha: number, toAlpha: number)

构造器，构造控制透明度的动画实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

fromAlpha

number

是

起始透明度。透明度范围为[0, 1]，1为不透明，0为完全透明。

toAlpha

number

是

目标透明度。透明度范围为[0, 1]，1为不透明，0为完全透明。

**示例：**

```ets
let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
```