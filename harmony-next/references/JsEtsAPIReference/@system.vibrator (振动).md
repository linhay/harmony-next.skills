# @system.vibrator (振动)

vibrator模块提供控制马达振动的能力，主要包含灯的列表查询、打开灯、关闭灯等接口，振动器的列表查询、振动效果查询、触发/关闭等接口。

控制类小器件指的是设备上的LED灯和振动器。其中，LED灯主要用作指示（如充电状态）、闪烁功能（如三色灯）等；振动器主要用于闹钟、开关机振动、来电振动等场景。

- 模块维护策略：

  - 对于Lite Wearable设备类型，该模块长期维护，正常使用。
  - 对于支持该模块的其他设备类型，该模块从API version 8开始不再维护，推荐使用新接口[@ohos.vibrator](@ohos.vibrator (振动).md)。

- 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 该功能使用需要对应硬件支持，仅支持真机调试。

#### 导入模块

```ets
import { Vibrator } from '@kit.SensorServiceKit';
```

#### Vibrator.vibrate

 vibrate(options?: VibrateOptions): void

触发设备振动。

除Lite Wearable外，从API Version8开始，推荐使用[vibrator.startVibration()](@ohos.vibrator (振动).md#ZH-CN_TOPIC_0000002529445607__vibratorstartvibration9)。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice.Lite

**参数**：

参数名类型必填说明options[VibrateOptions](#ZH-CN_TOPIC_0000002497445664__vibrateoptions)否振动模式。

**示例**：

```ets
import { Vibrator, VibrateOptions } from '@kit.SensorServiceKit';

let vibrateOptions: VibrateOptions = {
  mode: 'short',
  success: () => {
    console.info('Succeed in vibrating');
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to vibrate. Data: ${data}, code: ${code}`);
  },
  complete: () => {
    console.info('completed in vibrating');
  }
};
Vibrator.vibrate(vibrateOptions);
```

#### VibrateOptions

振动模式。

**需要权限**：ohos.permission.VIBRATE

**系统能力**：SystemCapability.Sensors.MiscDevice.Lite

名称类型必填说明modestring否振动的模式，其中long表示长振动，short表示短振动，默认值为long。successFunction否感应到振动数据变化后的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。