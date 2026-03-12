# Animation

#### 导入模块

```ets
import { map } from '@kit.MapKit';
```

#### Animation

动画抽象类。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
let animation = new map.RotateAnimation(0, 270);
// 动画执行时间
animation.setDuration(2000);

// 动画结束状态
animation.setFillMode(map.AnimationFillMode.BACKWARDS);

// 动画重复模式
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

// 动画重复次数
animation.setRepeatCount(100);

// 根据开发需要设置动画监听
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
```

#### setDuration

setDuration(duration: number): void

设置动画持续时间。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

duration

number

是

动画持续时间，单位：ms，默认值为250，取值范围：大于等于0。

**示例：**

```ets
animation.setDuration(3000);
```

#### setFillMode

setFillMode(fillMode: AnimationFillMode): void

设置动画执行完成后的状态。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

fillMode

[AnimationFillMode](AnimationFillMode.md)

是

动画执行完成后的状态，默认值为[AnimationFillMode](AnimationFillMode.md).FORWARDS。

**示例：**

```ets
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
```

#### setInterpolator

setInterpolator(curve: Curves.Curve): void

设置动画插值器。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

curve

[Curves.Curve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curve)

是

动画插值器，默认值为[Curve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curve).Linear。

**示例：**

```ets
animation.setInterpolator(Curve.Linear);
```

#### setRepeatCount

setRepeatCount(repeatCount: number): void

设置动画重复执行的次数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

repeatCount

number

是

动画重复执行的次数，默认值为0。

- 正数：根据值重复执行
- 0：动画不重复执行
- -1：执行次数是无限
- 小于-1：使用默认值0
- 异常值按默认值处理

**示例：**

```ets
animation.setRepeatCount(100);
```

#### setRepeatMode

setRepeatMode(repeatMode: AnimationRepeatMode): void

设置重复执行的模式，默认从前往后执行。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

repeatMode

[AnimationRepeatMode](AnimationRepeatMode.md)

是

重复执行的模式，默认值为[AnimationRepeatMode](AnimationRepeatMode.md).RESTART。

**示例：**

```ets
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
```

#### on('start')

on(type: 'start', callback: Callback<void>): void

监听动画开始事件。使用callback异步回调。

建议使用[animation.on(type: 'animationStart')](#section1282619121137)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'start'：动画开始事件。

callback

Callback<void>

是

回调函数。无返回结果的回调函数。

**示例：**

```ets
animation.on("start", () => {
  console.info(`start alphaAnimation`);
});
```

#### off('start')

off(type: 'start', callback: Callback<void>): void

取消监听动画开始事件。使用callback异步回调。

建议使用[animation.off(type: 'animationStart')](#section983316121834)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'start'：动画开始事件。

callback

Callback<void>

是

回调函数。无返回结果的回调函数。

**示例：**

```ets
animation.off("start", () => {
  console.info(`start alphaAnimation`);
});
```

#### on('end')

on(type: 'end', callback: Callback<void>): void

监听动画结束事件。使用callback异步回调。

建议使用[animation.on(type: 'animationEnd')](#section1184051219311)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'end'：动画结束事件。

callback

Callback<void>

是

回调函数。无返回结果的回调函数。

**示例：**

```ets
animation.on("end", () => {
  console.info(`end alphaAnimation`);
});
```

#### off('end')

off(type: 'end', callback: Callback<void>): void

取消监听动画结束事件。使用callback异步回调。

建议使用[animation.off(type: 'animationEnd')](#section984616121137)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'end'：动画结束事件。

callback

Callback<void>

是

回调函数。无返回结果的回调函数。

**示例：**

```ets
animation.off("end", () => {
  console.info(`end alphaAnimation`);
});
```

#### on('animationStart')

on(type: 'animationStart', callback: Callback<void>): void

监听动画开始事件。支持传递多个callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'animationStart'：监听动画开始事件。

callback

Callback<void>

是

回调函数。无返回结果的回调函数。监听动画开始事件。

**示例：**

```ets
let callback1 = () => {
  console.info("animationStart", `callback1`);
};
let callback2 = () => {
  console.info("animationStart", `callback2`);
};
let callback3 = () => {
  console.info("animationStart", `callback3`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);
```

#### off('animationStart')

off(type: 'animationStart', callback?: Callback<void>): void

取消监听动画开始事件。支持传递多个callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'animationStart'：监听动画开始事件。

callback

Callback<void>

否

回调函数。无返回结果的回调函数。取消监听动画开始事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = () => {
  console.info("animationStart", `callback1`);
};
let callback2 = () => {
  console.info("animationStart", `callback2`);
};
let callback3 = () => {
  console.info("animationStart", `callback3`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);

// 只取消callback1对象的事件响应，当animationStart事件发生时，callback2和callback3会正常被调用
animation.off('animationStart', callback1);
// 取消全部animationStart事件响应
animation.off('animationStart');
```

#### on('animationEnd')

on(type: 'animationEnd', callback: Callback<void>): void

监听动画结束事件。支持传递多个callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'animationEnd'：动画结束事件。

callback

Callback<void>

是

回调函数。无返回结果的回调函数。监听动画结束事件。

**示例：**

```ets
let callback1 = () => {
  console.info("animationEnd", `callback1`);
};
let callback2 = () => {
  console.info("animationEnd", `callback2`);
};
let callback3 = () => {
  console.info("animationEnd", `callback3`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);
```

#### off('animationEnd')

off(type: 'animationEnd', callback?: Callback<void>): void

取消监听动画结束事件。支持传递多个callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'animationEnd'：监听动画结束事件。

callback

Callback<void>

否

回调函数。无返回结果的回调函数。取消监听动画结束事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = () => {
  console.info("animationEnd", `callback1`);
};
let callback2 = () => {
  console.info("animationEnd", `callback2`);
};
let callback3 = () => {
  console.info("animationEnd", `callback3`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);

// 只取消callback1对象的事件响应，当animationEnd事件发生时，callback2和callback3会正常被调用
animation.off('animationEnd', callback1);
// 取消全部animationEnd事件响应
animation.off('animationEnd');
```