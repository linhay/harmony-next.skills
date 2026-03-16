# @ohos.graphics.displaySync (可变帧率)

可变帧率支持让开发者以指定帧率来运行UI业务，一般用于开发者自绘制UI，并且对于帧率有特定诉求的场景。

本模块首批接口和数据定义从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { displaySync } from '@kit.ArkGraphics2D';
```

#### displaySync.create

create(): DisplaySync

创建DisplaySync对象，通过此对象设置UI自绘制内容帧率。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[DisplaySync](#ZH-CN_TOPIC_0000002497605974__displaysync)返回当前创建的DisplaySync对象实例。

**示例：**

```ets
let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```

#### IntervalInfo

开发者可以从订阅函数中获取帧绘制的时间戳信息，包含当前帧到达的时间timestamp和下一帧预期到达的时间targetTimestamp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明timestampnumber否否当前帧到达的时间（单位：纳秒）。targetTimestampnumber否否下一帧预期到达的时间（单位：纳秒）。

#### DisplaySync

 帧率和回调函数设置实例。用于帧率设置和回调函数的注册，以及启动和停止回调函数的调用。

 下列API示例中都需先使用[displaySync.create()](#ZH-CN_TOPIC_0000002497605974__displaysynccreate)方法获取到DisplaySync实例，再通过此实例调用对应方法。

#### setExpectedFrameRateRange

setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void

设置期望的帧率范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明rateRange[ExpectedFrameRateRange](../../topics/misc/显式动画 (animateTo).md#ZH-CN_TOPIC_0000002497444950__expectedframeraterange11)是设置DisplaySync期望的帧率。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.Incorrect parameters types. 3. Parameter verification failed. or check ExpectedFrameRateRange if valid.

**示例：**

```ets
let range : ExpectedFrameRateRange = {
  expected: 10,
  min:0,
  max:120
};

// 设置DisplaySync期望的帧率
backDisplaySync?.setExpectedFrameRateRange(range)
```

#### on('frame')

on(type: 'frame', callback: Callback<IntervalInfo>): void

订阅每一帧的变化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明type'frame'是设置注册回调的类型（只能是'frame'类型）。callbackCallback<[IntervalInfo](#ZH-CN_TOPIC_0000002497605974__intervalinfo)>是订阅函数。

**示例：**

```ets
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// 注册订阅函数
backDisplaySync?.on("frame", callback)
```

#### off('frame')

off(type: 'frame', callback?: Callback<IntervalInfo>): void

取消订阅每一帧的变化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明type'frame'是设置注册回调的类型（只能是'frame'类型）。callbackCallback<[IntervalInfo](#ZH-CN_TOPIC_0000002497605974__intervalinfo)>否订阅函数，参数不填时，默认取消全部订阅函数。

**示例：**

```ets
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

backDisplaySync?.on("frame", callback)

// 取消订阅函数
backDisplaySync?.off("frame", callback)
```

#### start

start(): void

开始每帧回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
let range : ExpectedFrameRateRange = {
  expected: 10,
  min:0,
  max:120
};

backDisplaySync?.setExpectedFrameRateRange(range)

let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

backDisplaySync?.on("frame", callback)

// 开始每帧回调
backDisplaySync?.start()
```

start接口是将DisplaySync关联到UI实例和窗口，若在非UI页面中或者一些异步回调中进行start操作，可能无法跟踪到当前UI的上下文，导致start接口失败，会进一步导致订阅函数无法执行。

因此可以使用UIContext的[runScopedTask](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__runscopedtask)接口来指定start函数执行的UI上下文。

**示例：**

```ets
import { displaySync } from '@kit.ArkGraphics2D';
import { UIContext } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  // 创建DisplaySync实例
  backDisplaySync: displaySync.DisplaySync = displaySync.create();

  aboutToAppear() {
    // 获取UIContext实例
    let uiContext: UIContext = this.getUIContext();
    // 在当前UI上下文中执行DisplaySync的start接口
    uiContext?.runScopedTask(() => {
      this.backDisplaySync?.start();
    })
  }

  build() {
    // ...
  }
}
```

#### stop

stop(): void

停止每帧回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
let range : ExpectedFrameRateRange = {
  expected: 10,
  min:0,
  max:120
};

backDisplaySync?.setExpectedFrameRateRange(range)

let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

backDisplaySync?.on("frame", callback)

backDisplaySync?.start()

// ...

// 停止每帧回调
backDisplaySync?.stop()
```