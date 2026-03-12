# AnimationSet

#### 导入模块

```ets
import { map } from '@kit.MapKit';
```

#### AnimationSet

动画类的集合，继承[Animation](Animation.md)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

#### constructor

constructor(shareInterpolator: boolean)

构造器，构造动画类的集合实例。

动画类集合继承[Animation](Animation.md)方法，仅shareInterpolator为true时共享插值器，其他属性不共享，不支持设置。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

shareInterpolator

boolean

是

定义是否共享插值器。

- true：共享
- false：不共享

**示例：**

```ets
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.setInterpolator(Curve.Linear);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
animation.clearAnimation();
```

#### addAnimation

addAnimation(animation: Animation): void

动画类集合增加动画。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

animation

[Animation](Animation.md)

是

动画类集合增加动画。

**示例：**

```ets
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
```

#### clearAnimation

clearAnimation(): void

清空动画类集合。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
animation.clearAnimation();
```