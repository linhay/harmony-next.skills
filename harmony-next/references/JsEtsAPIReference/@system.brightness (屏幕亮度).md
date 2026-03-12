# @system.brightness (屏幕亮度)

该模块提供屏幕亮度和模式的查询、调节接口。

- 从API Version 7 开始不再维护，替代接口能力仅对系统应用开放。
- 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import brightness, { BrightnessModeResponse, BrightnessResponse } from '@system.brightness';
```

#### brightness.getValue(deprecated)

getValue(options?: GetBrightnessOptions): void

获得设备当前的屏幕亮度值。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

参数名类型必填说明options[GetBrightnessOptions](#ZH-CN_TOPIC_0000002497605520__getbrightnessoptionsdeprecated)否获取屏幕亮度的参数对象。可选，默认为空。

**示例：**

```ets
brightness.getValue({
    success: (data: BrightnessResponse) => {
      console.log('success get brightness value:' + data.value);
    },
    fail: (data: string, code: number) => {
      console.error('get brightness fail, code: ' + code + ', data: ' + data);
    }
});
```

#### brightness.setValue(deprecated)

setValue(options?: SetBrightnessOptions): void

设置设备当前的屏幕亮度值。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

参数名类型必填说明options[SetBrightnessOptions](#ZH-CN_TOPIC_0000002497605520__setbrightnessoptionsdeprecated)否设置屏幕亮度的参数对象。可选，默认为空。

**示例：**

```ets
brightness.setValue({
    value: 100,
    success: () => {
      console.log('handling set brightness success.');
    },
    fail: (data: string, code: number) => {
      console.error('handling set brightness value fail, code:' + code + ', data: ' + data);
    }
});
```

#### brightness.getMode(deprecated)

getMode(options?: GetBrightnessModeOptions): void

获得当前屏幕亮度模式。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

参数名类型必填说明options[GetBrightnessModeOptions](#ZH-CN_TOPIC_0000002497605520__getbrightnessmodeoptionsdeprecated)否获取屏幕亮度模式的参数对象。可选，默认为空。

**示例：**

```ets
brightness.getMode({
    success: (data: BrightnessModeResponse) => {
      console.log('success get mode:' + data.mode);
    },
    fail: (data: string, code: number) => {
      console.error('handling get mode fail, code:' + code + ', data: ' + data);
    }
});
```

#### brightness.setMode(deprecated)

setMode(options?: SetBrightnessModeOptions): void

设置设备当前的屏幕亮度模式。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

参数名类型必填说明options[SetBrightnessModeOptions](#ZH-CN_TOPIC_0000002497605520__setbrightnessmodeoptionsdeprecated)否设置屏幕亮度模式的参数对象。可选，默认为空。

**示例：**

```ets
brightness.setMode({
    mode: 1,
    success: () => {
      console.log('handling set mode success.');
    },
    fail: (data: string, code: number) => {
      console.error('handling set mode fail, code:' + code + ', data: ' + data);
    }
});
```

#### brightness.setKeepScreenOn(deprecated)

setKeepScreenOn(options?: SetKeepScreenOnOptions): void

从API version 7开始不再维护，建议使用[window.setWindowKeepScreenOn()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowkeepscreenon9)替代。

设置屏幕是否保持常亮状态，开启常亮模式推荐在onShow()阶段调用。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

参数名类型必填说明options[SetKeepScreenOnOptions](#ZH-CN_TOPIC_0000002497605520__setkeepscreenonoptionsdeprecated)否设置屏幕常亮的参数对象。可选，默认为空。

**示例：**

```ets
brightness.setKeepScreenOn({
    keepScreenOn: true,
    success: () => {
      console.log('handling set keep screen on success.');
    },
    fail: (data: string, code: number) => {
      console.error('handling set keep screen on fail, code:' + code + ', data: ' + data);
    }
});
```

#### GetBrightnessOptions(deprecated)

获取屏幕亮度的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

名称类型必填说明success(data: [BrightnessResponse](#ZH-CN_TOPIC_0000002497605520__brightnessresponsedeprecated)) => void否接口调用成功的回调函数。data为[BrightnessResponse](#ZH-CN_TOPIC_0000002497605520__brightnessresponsedeprecated)类型的返回值。fail(data: string, code: number) => void否接口调用失败的回调函数。data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

#### SetBrightnessOptions(deprecated)

设置屏幕亮度的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

名称类型必填说明valuenumber是

屏幕亮度，值为1-255之间的整数。

- 如果值小于等于0，系统按1处理。

- 如果值大于255，系统按255处理。

- 如果值为小数，系统将处理为整数。例如设置为8.1，系统按8处理。

success() => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

#### BrightnessResponse(deprecated)

包含屏幕亮度的对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

名称类型可读可写说明valuenumber是否屏幕亮度，范围：1到255。

#### GetBrightnessModeOptions(deprecated)

获取屏幕亮度模式的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

名称类型必填说明success(data: [BrightnessModeResponse](#ZH-CN_TOPIC_0000002497605520__brightnessmoderesponsedeprecated)) => void否接口调用成功的回调函数。data为[BrightnessModeResponse](#ZH-CN_TOPIC_0000002497605520__brightnessmoderesponsedeprecated)类型的返回值。fail(data: string, code: number) => void否接口调用失败的回调函数。data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

#### SetBrightnessModeOptions(deprecated)

设置屏幕亮度模式的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

名称类型必填说明modenumber是0表示手动调节屏幕亮度模式，1表示自动调节屏幕亮度模式。success() => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

#### BrightnessModeResponse(deprecated)

包含屏幕亮度模式的对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

名称类型可读可写说明modenumber是否0表示手动调节屏幕亮度模式，1表示自动调节屏幕亮度模式。

#### SetKeepScreenOnOptions(deprecated)

设置屏幕常亮的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

名称类型必填说明keepScreenOnboolean是true表示保持屏幕常亮，false表示取消屏幕常亮。success() => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。