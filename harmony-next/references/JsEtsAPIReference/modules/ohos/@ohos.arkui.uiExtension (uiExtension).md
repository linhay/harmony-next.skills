# @ohos.arkui.uiExtension (uiExtension)

用于[EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/embeddeduiextensionability)（或[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md#ZH-CN_TOPIC_0000002553200505__uiextensionability)）中获取宿主应用的窗口信息或对应的[EmbeddedComponent](EmbeddedComponent.md)组件的信息。


从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import { uiExtension } from '@kit.ArkUI';
```

#### WindowProxy

UIExtension宿主窗代理。

#### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties14+ | WindowProxyProperties | 否 | 否 | 组件（EmbeddedComponent或UIExtensionComponent）的信息。 约束： 由于架构约束，不建议在onSessionCreate阶段同步获取该值，建议在收到on('windowSizeChange')回调之后获取。 |

#### getWindowAvoidArea

getWindowAvoidArea(type: [window.AvoidAreaType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7)): window.AvoidArea

获取宿主应用窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与宿主窗口内容重叠时，需要宿主窗口内容避让的区域。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [window.AvoidAreaType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7) | 是 | 表示规避区类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| window.AvoidArea | 宿主窗口内容规避区域。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 获取宿主应用窗口的避让信息
    let avoidArea: window.AvoidArea | undefined = extensionWindow?.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
    console.info(`avoidArea: ${JSON.stringify(avoidArea)}`);
  }
```

#### on('avoidAreaChange')

on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void

注册系统规避区变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定为'avoidAreaChange'，即系统规避区变化事件。 |
| callback | Callback<AvoidAreaInfo> | 是 | 回调函数：入参用于接收当前规避区的信息。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注册避让区变化的监听
    extensionWindow.on('avoidAreaChange', (info: uiExtension.AvoidAreaInfo) => {
      console.info(`The avoid area of the host window is: ${JSON.stringify(info.area)}.`);
    });
  }
```

#### off('avoidAreaChange')

off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void

注销系统规避区变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销的事件类型，固定为'avoidAreaChange'，即系统规避区变化事件。 |
| callback | Callback<AvoidAreaInfo> | 否 | 回调函数：如果传入该参数，则关闭该监听。如果未传入参数，则关闭所有系统规避区变化的监听。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注销所有避让区变化的监听
    extensionWindow.off('avoidAreaChange');
  }
```

#### on('windowSizeChange')

on(type: 'windowSizeChange', callback: Callback<window.Size>): void

注册组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定为'windowSizeChange'，即组件（EmbeddedComponent或UIExtensionComponent）尺寸变化事件。 |
| callback | Callback<window.Size> | 是 | 回调函数：入参用于接收当前组件（EmbeddedComponent或UIExtensionComponent）的尺寸。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注册组件（EmbeddedComponent或UIExtensionComponent）大小变化的监听
    extensionWindow.on('windowSizeChange', (size: window.Size) => {
      console.info(`The avoid area of the host window is: ${JSON.stringify(size)}.`);
    });
  }
```

#### off('windowSizeChange')

off(type: 'windowSizeChange', callback?: Callback<window.Size>): void

注销组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销的事件类型，固定值：'windowSizeChange'，即组件（EmbeddedComponent或UIExtensionComponent）尺寸变化事件。 |
| callback | Callback<window.Size> | 否 | 回调函数。返回当前的组件（EmbeddedComponent或UIExtensionComponent）尺寸。如果传入该参数，则关闭该监听。如果未传入参数，则关闭组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注销组件（EmbeddedComponent或UIExtensionComponent）大小变化的监听
    extensionWindow.off('windowSizeChange');
  }
```

#### on('rectChange')14+

on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void

注册组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChange'，即组件（EmbeddedComponent或UIExtensionComponent）矩形变化事件。 |
| reasons | number | 是 | 触发组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的原因，具体取值可参考RectChangeReason枚举值。 |
| callback | Callback<RectChangeOptions> | 是 | 回调函数。返回当前组件（EmbeddedComponent或UIExtensionComponent）矩形变化值及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注册组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听
    extensionWindow.on('rectChange', uiExtension.RectChangeReason.HOST_WINDOW_RECT_CHANGE, (data: uiExtension.RectChangeOptions) => {
        console.info('Succeeded window rect changes. Data: ' + JSON.stringify(data));
    });
  }
```

#### off('rectChange')14+

off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void

注销组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChange'，即组件（EmbeddedComponent或UIExtensionComponent）矩形变化事件。 |
| callback | Callback<RectChangeOptions> | 否 | 回调函数。返回当前组件（EmbeddedComponent或UIExtensionComponent）矩形变化值及变化原因。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有组件（EmbeddedComponent或UIExtensionComponent）矩形变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注销组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听
    extensionWindow.off('rectChange');
  }
```

#### createSubWindowWithOptions

createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>

创建该WindowProxy实例下的子窗口，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| subWindowOptions | window.SubWindowOptions | 是 | 子窗口参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<window.Window> | Promise对象。返回当前WindowProxy下创建的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码]([窗口错误码](../../errors/窗口错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible causes: 1. The window is not created or destroyed. 2. Internal task error. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    const subWindowOpts: window.SubWindowOptions = {
      title: 'This is a subwindow',
      decorEnabled: true
    };
    // 创建子窗口
    extensionWindow.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
      .then((subWindow: window.Window) => {
        subWindow.setUIContent('pages/Index', (err, data) =>{
          if (err && err.code != 0) {
            return;
          }
          subWindow?.resize(300, 300, (err, data)=>{
            if (err && err.code != 0) {
              return;
            }
            subWindow?.moveWindowTo(100, 100, (err, data)=>{
              if (err && err.code != 0) {
                return;
              }
              subWindow?.showWindow((err, data) => {
                if (err && err.code == 0) {
                  console.info(`The subwindow has been shown!`);
                } else {
                  console.error(`Failed to show the subwindow!`);
                }
              });
      }).catch((error: BusinessError) => {
        console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
      })
  }
```

**createSubWindowWithOptions23+**

createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions, followCreatorLifecycle: boolean): Promise<window.Window>

创建该WindowProxy实例下的子窗口，可通过设置followCreatorLifecycle，决定子窗是否跟随组件（EmbeddedComponent或UIExtensionComponent）的生命周期，使用Promise异步回调。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| subWindowConfig | window.SubWindowOptions | 是 | 子窗口参数。 |
| followCreatorLifecycle | boolean | 是 | 子窗生命周期是否跟组件（EmbeddedComponent或UIExtensionComponent）保持同步。true表示该组件隐藏时，子窗隐藏，该组件显示时子窗显示，false表示子窗的显隐不跟随该组件变化。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<window.Window> | Promise对象。返回当前WindowProxy下创建的子窗口对象。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

示例：

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    const subWindowConfig: window.SubWindowOptions = {
      title: 'This is a subwindow',
      decorEnabled: true
    };
    // 创建子窗口
    extensionWindow.createSubWindowWithOptions('subWindowForHost', subWindowConfig, true)
      .then((subWindow: window.Window) => {
        subWindow.setUIContent('pages/Index', (err, data) =>{
          if (err && err.code != 0) {
            return;
          }
          subWindow?.resize(300, 300, (err, data)=>{
            if (err && err.code != 0) {
              return;
            }
            subWindow?.moveWindowTo(100, 100, (err, data)=>{
              if (err && err.code != 0) {
                return;
              }
              subWindow?.showWindow((err, data) => {
                if (err && err.code == 0) {
                  console.info(`The subwindow has been shown!`);
                } else {
                  console.error(`Failed to show the subwindow!`);
                }
        });
      }).catch((error: BusinessError) => {
        console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
      })
}
```

#### occupyEvents18+

occupyEvents(eventFlags: number): Promise<void>

设置组件（EmbeddedComponent或UIExtensionComponent）占用事件，宿主将不响应组件区域内被占用的事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventFlags | number | 是 | 占用的事件类型，具体取值可见EventFlag枚举值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 占用事件
    setTimeout(() => {
      try {
        let promise = extensionWindow.occupyEvents(uiExtension.EventFlag.EVENT_CLICK | uiExtension.EventFlag.EVENT_LONG_PRESS);
        promise.then(() => {
          console.info(`Succeeded in occupying events`);
        }).catch((err: BusinessError) => {
          console.error(`Failed to occupy events. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (e) {
        console.error(`Occupy events got exception code: ${e.code}, message: ${e.message}`);
      }
    }, 500);
  }
```

#### EventFlag18+

事件类型枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT_NONE | 0x00000000 | 无事件。 |
| EVENT_PAN_GESTURE_LEFT | 0x00000001 | 左滑事件。 |
| EVENT_PAN_GESTURE_RIGHT | 0x00000002 | 右滑事件。 |
| EVENT_PAN_GESTURE_UP | 0x00000004 | 上滑事件。 |
| EVENT_PAN_GESTURE_DOWN | 0x00000008 | 下滑事件。 |
| EVENT_CLICK | 0x00000100 | 点击事件。 |
| EVENT_LONG_PRESS | 0x00000200 | 长按事件。 |

#### AvoidAreaInfo

用于表示窗口规避区的信息。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [window.AvoidAreaType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7) | 否 | 否 | 窗口规避区类型。 |
| area | window.AvoidArea | 否 | 否 | 窗口内容规避区域。 |

#### WindowProxyProperties14+

用于表示组件的相关信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uiExtensionHostWindowProxyRect | window.Rect | 否 | 否 | 组件（EmbeddedComponent或UIExtensionComponent）的位置和宽高。 |

#### RectChangeReason14+

组件（EmbeddedComponent或UIExtensionComponent）矩形（位置及尺寸）变化的原因。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HOST_WINDOW_RECT_CHANGE | 0x0001 | 组件所在的宿主窗口矩形变化。 |

#### RectChangeOptions14+

组件（EmbeddedComponent或UIExtensionComponent）矩形（位置及尺寸）变化返回的值及变化原因。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | window.Rect | 否 | 否 | 组件矩形变化后的值。 |
| reason | RectChangeReason | 否 | 否 | 组件矩形变化的原因。 |

#### 完整示例

本示例展示文档中所有API在[EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/embeddeduiextensionability)中的基础使用方式，示例应用的bundleName为"com.example.embeddeddemo"，被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。

-

示例应用中的EntryAbility(UIAbility)加载首页文件：pages/Index.ets，其中内容如下：
```ets
// pages/Index.ets -- UIAbility启动时加载此页面
import { Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Message: ';
  private want: Want = {
    bundleName: "com.example.embeddeddemo",
    abilityName: "ExampleEmbeddedAbility",
  }

  build() {
    Row() {
      Column() {
        Text(this.message).fontSize(30)
        EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
          .width('100%')
          .height('90%')
          .onTerminated((info)=>{
            this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
          })
          .onError((error)=>{
            this.message = 'Error: code = ' + error.code;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
```

-

EmbeddedComponent拉起的EmbeddedUIExtensionAbility在ets/extensionAbility/ExampleEmbeddedAbility文件中实现，内容如下：
```ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

const TAG: string = '[ExampleEmbeddedAbility]';
export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {

  onCreate() {
    console.info(TAG, `onCreate`);
  }

  onForeground() {
    console.info(TAG, `onForeground`);
  }

  onBackground() {
    console.info(TAG, `onBackground`);
  }

  onDestroy() {
    console.info(TAG, `onDestroy`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
    let param: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(param);
    session.loadContent('pages/extension', storage);
}
```

-

EmbeddedUIExtensionAbility的入口页面文件pages/extension.ets内容如下：
```ets
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { uiExtension, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry()
@Component
struct Extension {
  @State message: string = 'EmbeddedUIExtensionAbility Index';
  private storage: LocalStorage | undefined = this.getUIContext()?.getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');
  private extensionWindow: uiExtension.WindowProxy | undefined = this.session?.getUIExtensionWindowProxy();
  private subWindow: window.Window | undefined = undefined;

  aboutToAppear(): void {
    this.extensionWindow?.on('windowSizeChange', (size: window.Size) => {
        console.info(`size = ${JSON.stringify(size)}`);
    });
    this.extensionWindow?.on('rectChange', uiExtension.RectChangeReason.HOST_WINDOW_RECT_CHANGE, (data: uiExtension.RectChangeOptions) => {
        console.info('Succeeded window rect changes. Data: ' + JSON.stringify(data));
    });
    this.extensionWindow?.on('avoidAreaChange', (info: uiExtension.AvoidAreaInfo) => {
        console.info(`type = ${JSON.stringify(info.type)}, area = ${JSON.stringify(info.area)}`);
    });
  }

  aboutToDisappear(): void {
    this.extensionWindow?.off('windowSizeChange');
    this.extensionWindow?.off('rectChange');
    this.extensionWindow?.off('avoidAreaChange');
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
      Button("获取组件大小").width('90%').margin({top: 5, bottom: 5}).fontSize(16).onClick(() => {
        let rect = this.extensionWindow?.properties.uiExtensionHostWindowProxyRect;
        console.info(`EmbeddedComponent的位置和尺寸信息: ${JSON.stringify(rect)}`);
      })
      Button("获取系统规避区信息").width('90%').margin({top: 5, bottom: 5}).fontSize(16).onClick(() => {
        let avoidArea: window.AvoidArea | undefined = this.extensionWindow?.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
        console.info(`系统规避区: ${JSON.stringify(avoidArea)}`);
      })
      Button("创建子窗口").width('90%').margin({top: 5, bottom: 5}).fontSize(16).onClick(() => {
        let subWindowOpts: window.SubWindowOptions = {
            'title': 'This is a subwindow',
            decorEnabled: true
        };
        this.extensionWindow?.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
            .then((subWindow: window.Window) => {
                this.subWindow = subWindow;
                this.subWindow.loadContent('pages/Index', this.storage, (err, data) =>{
                    if (err && err.code != 0) {
                        return;
                    }
                    this.subWindow?.resize(300, 300, (err, data)=>{
                        if (err && err.code != 0) {
                            return;
                        }
                        this.subWindow?.moveWindowTo(100, 100, (err, data)=>{
                            if (err && err.code != 0) {
                                return;
                            }
                            this.subWindow?.showWindow((err, data) => {
                                if (err && err.code == 0) {
                                    console.info(`The subwindow has been shown!`);
                                } else {
                                    console.error(`Failed to show the subwindow!`);
                                }
                            });
            }).catch((error: BusinessError) => {
                console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
            })
    }.width('100%').height('100%')
}
```

-

最后，示例应用的module.json5中的"extensionAbilities"中需要增加一项，具体内容如下：
```ets
{
  "name": "ExampleEmbeddedAbility",
  "srcEntry": "./ets/extensionAbility/ExampleEmbeddedAbility.ets",
  "type": "embeddedUI"
}
```