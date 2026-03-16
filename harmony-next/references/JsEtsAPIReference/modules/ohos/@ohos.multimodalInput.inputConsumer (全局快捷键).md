# @ohos.multimodalInput.inputConsumer (全局快捷键)

全局快捷键订阅模块，用于处理组合按键的订阅，本模块也支持音量键拦截监听能力。

-

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

全局快捷键指由系统或应用定义的组合按键，系统快捷键指由系统定义的全局快捷键，应用快捷键指由应用定义的全局快捷键。

#### 导入模块

```ets
import { inputConsumer, KeyEvent } from '@kit.InputKit';
```

#### HotkeyOptions

快捷键选项。

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

名称类型只读可选说明preKeysArray<number>否否

修饰键（包括 Ctrl、Shift 和 Alt）集合，数量范围[1, 2]，无顺序要求。

例如，Ctrl+Shift+Esc中，Ctrl+Shift称为修饰键。

finalKeynumber否否

被修饰键，除修饰键和Meta键以外的按键，详细按键介绍请参见[键值](@ohos.multimodalInput.keyCode (键值).md)。

例如，Ctrl+Shift+Esc中，Esc称为被修饰键。

isRepeatboolean否是是否上报重复的按键事件。true表示上报，false表示不上报，默认值为true。

#### KeyPressedConfig16+

按键事件消费设置。

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**设备行为差异**：该接口仅在Phone和Tablet设备上生效，在其他设备上返回801错误码。

名称类型只读可选说明keynumber否否

按键键值。

**说明：** 从API version 21开始，支持[KEYCODE_VOLUME_UP](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)键、[KEYCODE_VOLUME_DOWN](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)键、[KEYCODE_MEDIA_PLAY_PAUSE](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)键、[KEYCODE_MEDIA_NEXT](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)键和[KEYCODE_MEDIA_PREVIOUS](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)键。

对于API version 20及之前的版本，仅支持[KEYCODE_VOLUME_UP](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)键和[KEYCODE_VOLUME_DOWN](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)键。

actionnumber否否

订阅指定的按键事件。

**说明：** 从API version 21开始，支持取值为1和2，取值为1表示订阅按键按下事件，取值为2表示同时订阅按键按下事件和按键抬起事件。

对于API version 20及之前的版本，仅支持取值为1，表示订阅按键按下事件。

isRepeatboolean否否是否上报重复的按键事件。true表示上报，false表示不上报，默认值为true。

#### inputConsumer.getAllSystemHotkeys

getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>

获取所有系统快捷键，使用Promise异步回调。

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**返回值：**

类型说明Promise<Array<HotkeyOptions>>Promise对象，返回所有系统快捷键的列表。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { inputConsumer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputConsumer.getAllSystemHotkeys().then((data: Array<inputConsumer.HotkeyOptions>) => {
            console.info(`List of system hotkeys : ${JSON.stringify(data)}`);
          }).catch((error: BusinessError) => {
            console.error(`Get all system hotkeys failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          })
        })
    }
  }
}
```

#### inputConsumer.on('hotkeyChange')

on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void

订阅应用快捷键。获取满足条件的组合按键输入事件，使用Callback异步回调。

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**参数：**

参数名类型必填说明typestring是事件类型，固定取值为'hotkeyChange'。hotkeyOptions[HotkeyOptions](#ZH-CN_TOPIC_0000002497445592__hotkeyoptions)是快捷键选项。callbackCallback<HotkeyOptions>是回调函数，获取满足条件的组合按键输入事件。

**错误码**：

以下错误码的详细介绍请参见[全局快捷键管理错误码](../../errors/全局快捷键管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported.4200002The hotkey has been used by the system.4200003The hotkey has been subscribed to by another.

**示例：**

```ets
import { inputConsumer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let leftCtrlKey = 2072;
          let zKey = 2042;
          let hotkeyOptions: inputConsumer.HotkeyOptions = {
            preKeys: [leftCtrlKey],
            finalKey: zKey,
            isRepeat: true
          };
          let hotkeyCallback = (hotkeyOptions: inputConsumer.HotkeyOptions) => {
            console.info(`hotkeyOptions: ${JSON.stringify(hotkeyOptions)}`);
          }
          try {
            inputConsumer.on("hotkeyChange", hotkeyOptions, hotkeyCallback);
          } catch (error) {
            console.error(`Subscribe failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputConsumer.off('hotkeyChange')

off(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback?: Callback<HotkeyOptions>): void

取消订阅应用快捷键。

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**参数：**

参数名类型必填说明typestring是事件类型，固定取值为'hotkeyChange'。hotkeyOptions[HotkeyOptions](#ZH-CN_TOPIC_0000002497445592__hotkeyoptions)是快捷键选项。callbackCallback<HotkeyOptions>否需要取消订阅的回调函数。若缺省，则取消当前应用快捷键选项已订阅的所有回调函数。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { inputConsumer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let leftCtrlKey = 2072;
          let zKey = 2042;
          // 取消订阅单个应用快捷键回调函数
          let hotkeyCallback = (hotkeyOptions: inputConsumer.HotkeyOptions) => {
            console.info(`hotkeyOptions: ${JSON.stringify(hotkeyOptions)}`);
          }
          let hotkeyOption: inputConsumer.HotkeyOptions = { preKeys: [leftCtrlKey], finalKey: zKey, isRepeat: true };
          try {
            inputConsumer.on("hotkeyChange", hotkeyOption, hotkeyCallback);
            inputConsumer.off("hotkeyChange", hotkeyOption, hotkeyCallback);
            console.info(`Unsubscribe success`);
          } catch (error) {
            console.error(`Execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```ets
import { inputConsumer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let leftCtrlKey = 2072;
          let zKey = 2042;
          // 取消订阅所有应用快捷键回调函数
          let hotkeyCallback = (hotkeyOptions: inputConsumer.HotkeyOptions) => {
            console.info(`hotkeyOptions: ${JSON.stringify(hotkeyOptions)}`);
          }
          let hotkeyOption: inputConsumer.HotkeyOptions = { preKeys: [leftCtrlKey], finalKey: zKey, isRepeat: true };
          try {
            inputConsumer.on("hotkeyChange", hotkeyOption, hotkeyCallback);
            inputConsumer.off("hotkeyChange", hotkeyOption);
            console.info(`Unsubscribe success`);
          } catch (error) {
            console.error(`Execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputConsumer.on('keyPressed')16+

on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void

订阅按键按下事件，使用callback异步回调。若当前应用窗口为前台焦点窗口，用户按下指定按键，会触发回调。

订阅成功后，该按键事件的系统默认行为将被屏蔽，即不会再触发系统级的响应，如音量调节。要恢复系统响应，请使用[off](#ZH-CN_TOPIC_0000002497445592__inputconsumeroffkeypressed16)方法取消订阅。

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**设备行为差异**：该接口仅在Phone和Tablet设备中可正常调用，在其他设备上返回801错误码。

**参数：**

参数名类型必填说明typestring是事件类型，固定取值为'keyPressed'。options[KeyPressedConfig](#ZH-CN_TOPIC_0000002497445592__keypressedconfig16)是按键事件消费设置。callbackCallback<[KeyEvent](@ohos.multimodalInput.keyEvent (按键输入事件).md#ZH-CN_TOPIC_0000002529445533__keyevent)>是回调函数，用于返回按键事件。订阅不同的按键事件需要使用不同的callback，否则订阅不生效。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { inputConsumer, KeyEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let options: inputConsumer.KeyPressedConfig = {
              key: 16,
              action: 1,
              isRepeat: false,
            }
            inputConsumer.on('keyPressed', options, (event: KeyEvent) => {
              console.info(`Subscribe success ${JSON.stringify(event)}`);
            });
          } catch (error) {
            console.error(`Subscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputConsumer.off('keyPressed')16+

off(type: 'keyPressed', callback?: Callback<KeyEvent>): void

取消对'keyPressed'事件的订阅，使用callback异步回调。调用该方法后，被屏蔽的系统按键默认行为将恢复，即系统对音量调节等默认响应将恢复。

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**设备行为差异**：该接口仅在Phone和Tablet设备中可正常调用，在其他设备上返回801错误码。

**参数：**

参数名类型必填说明typestring是事件类型，固定取值为'keyPressed'。callbackCallback<[KeyEvent](@ohos.multimodalInput.keyEvent (按键输入事件).md#ZH-CN_TOPIC_0000002529445533__keyevent)>否需要取消订阅的回调函数。若缺省，则取消当前已订阅的所有回调函数。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { inputConsumer, KeyEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 取消指定回调函数
            inputConsumer.off('keyPressed', (event: KeyEvent) => {
              console.info(`Unsubscribe success ${JSON.stringify(event)}`);
            });
            // 取消当前已订阅的所有回调函数
            inputConsumer.off("keyPressed");
          } catch (error) {
            console.error(`Unsubscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```