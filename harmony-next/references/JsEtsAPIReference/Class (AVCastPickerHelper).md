# Class (AVCastPickerHelper)

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Class首批接口从API version 14开始支持。

投播半模态对象，可拉起半模态窗口，选择投播设备。在使用前，需要创建AVCastPickerHelper实例。

#### 导入模块

```ets
import { avSession } from '@kit.AVSessionKit';
```

#### constructor14+

constructor(context: Context)

创建AVCastPickerHelper对象，获取context参考[getHostContext](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__gethostcontext12)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明contextContext是应用上下文（仅支持[UIAbilityContext](UIAbilityContext.md)）。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as Context;
            let avCastPicker = new avSession.AVCastPickerHelper(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### select14+

select(options?: AVCastPickerOptions): Promise<void>

通过选择模式拉起AVCastPicker界面，用户可以选择投播设备。接口采用Promise异步返回形式，传入可选参数AVCastPickerOptions对象，无返回值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明options[AVCastPickerOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcastpickeroptions14)否AVCastPicker选择选项。无此参数时，以AVCastPickerOptions默认值拉起。

**返回值：**

类型说明Promise<void>Promise对象。当命令发送成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

async function avCastPicker(context: common.Context) {
  let avCastPickerOptions : avSession.AVCastPickerOptions = {
    sessionType : 'video',
  }
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.select(avCastPickerOptions).then(() => {
    console.info('select successfully');
  }).catch((err: BusinessError) => {
    console.error(`AVCastPicker.select failed with err: ${err.code}, ${err.message}`);
  });
}
```

#### resetCommunicationDevice21+

resetCommunicationDevice(): Promise<void>

将应用通话设备恢复至默认设备。比如在语音通话场景下，手机设备的通话装置将恢复成听筒。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { avSession } from '@kit.AVSessionKit';

async function avCastPicker(context: common.Context) {
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.resetCommunicationDevice().then(() => {
    console.info('resetCommunicationDevice successfully');
  });
}
```

#### on('pickerStateChange')14+

on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void

设置半模态窗口变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'pickerStateChange'：当半模态窗口变化时，触发该事件。callbackCallback<[AVCastPickerState](@ohos.multimedia.avCastPickerParam (投播组件参数).md#ZH-CN_TOPIC_0000002497445786__avcastpickerstate)>是回调函数，参数state是变化后的半模态窗口状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { AVCastPickerState } from '@kit.AVSessionKit';
import { avSession } from '@kit.AVSessionKit';

async function onPickerStateChange(context: common.Context) {
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.on('pickerStateChange', (state: AVCastPickerState) => {
    console.info(`picker state change : ${state}`);
  });
}
```

#### off('pickerStateChange')14+

off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void

取消半模态窗口变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'pickerStateChange'。callbackCallback<[AVCastPickerState](@ohos.multimedia.avCastPickerParam (投播组件参数).md#ZH-CN_TOPIC_0000002497445786__avcastpickerstate)>否

回调函数，参数state是变化后的半模态窗口状态。

当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { avSession } from '@kit.AVSessionKit';

async function onPickerStateChange(context: common.Context) {
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.off('pickerStateChange');
}
```