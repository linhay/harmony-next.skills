# BasePriorityOverlay

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### BasePriorityOverlay

具有优先级控制的覆盖物基础类，继承[BaseOverlay](BaseOverlay.md)。[PointAnnotation](PointAnnotation.md)和[Bubble](Bubble.md)继承该基础类。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

#### getMaxZoom

getMaxZoom(): number

获取覆盖物的最大展示层级。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

覆盖物的最大展示层级。

**示例：**

```ets
// 以pointAnnotation为例
let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
  position: {
    latitude: 32.120750,
    longitude: 118.788765
  },
  titles: [{
    content: "南京夫子庙"
  }],
  // 图标需存放在resources/rawfile目录下
  icon: 'icon.png'
};
let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
let maxZoom: number = pointAnnotation.getMaxZoom();
```

#### getMinZoom

getMinZoom(): number

获取覆盖物的最小展示层级。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

覆盖物的最小展示层级。

**示例：**

```ets
// 以pointAnnotation为例
let minZoom: number = pointAnnotation.getMinZoom();
```

#### setPriority

setPriority(priority: number): void

设置覆盖物碰撞优先级，值越大优先级越低。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

priority

number

是

设置覆盖物的碰撞优先级。

**示例：**

```ets
// 以pointAnnotation为例
pointAnnotation.setPriority(100);
```

#### setZoom

setZoom(minZoom: number, maxZoom: number): void

设置覆盖物的显示层级。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

minZoom

number

是

覆盖物的最小显示层级，取值范围：[2, 20]。

传入的值高于20，最小缩放级别会取20。

传入的值小于2，最小缩放级别会取2。

 说明：

minZoom大于maxZoom，方法不生效。

maxZoom

number

是

覆盖物的最大显示层级，取值范围：[2, 20]。

传入的值高于20，最大缩放级别会取20。

传入的值小于2，最大缩放级别会取2。

**示例：**

```ets
// 以pointAnnotation为例
pointAnnotation.setZoom(3, 10);
```

#### setAnimation

setAnimation(animation: Animation): void

设置覆盖物的动画。仅支持[AlphaAnimation](AlphaAnimation.md)、[ScaleAnimation](ScaleAnimation.md)和[AnimationSet](AnimationSet.md)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

animation

[Animation](Animation.md)

是

动画。

**示例：**

```ets
let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

pointAnnotation.setAnimation(animation);
```

#### startAnimation

startAnimation(): void

启动覆盖物的动画。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

pointAnnotation.setAnimation(animation);
pointAnnotation.startAnimation();
```

#### clearAnimation

clearAnimation(): void

清除覆盖物的动画。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
pointAnnotation.clearAnimation();
```