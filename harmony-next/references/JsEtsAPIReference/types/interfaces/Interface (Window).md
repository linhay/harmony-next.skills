# Interface (Window)

当前窗口实例，窗口管理器管理的基本单元。

下列API示例中都需先使用[getLastWindow()](Functions.md#ZH-CN_TOPIC_0000002553200715__windowgetlastwindow9)、[createWindow()](Functions.md#ZH-CN_TOPIC_0000002553200715__windowcreatewindow9)、[findWindow()](Functions.md#ZH-CN_TOPIC_0000002553200715__windowfindwindow9)中的任一方法获取到Window实例（windowClass），再通过此实例调用对应方法。


-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](SysCap (系统能力).md#ZH-CN_TOPIC_0000002553202569__caniuse)接口判断当前设备是否支持此syscap及对应接口。

#### 导入模块

```ets
import { window } from '@kit.ArkUI';
```

#### showWindow9+

showWindow(callback: AsyncCallback<void>): void

显示当前窗口，使用callback异步回调，支持系统窗口、应用子窗口、模态窗和全局悬浮窗，或将已显示的应用主窗口层级提升至顶部。


调用该接口前，建议先通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法或者[setUIContent](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setuicontent9-1)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会一直显示启动界面；如果系统窗口、应用子窗口、模态窗和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码]([窗口错误码](../../errors/窗口错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      try {
        // 创建子窗
        windowStage.createSubWindow("testSubWindow").then((subWindow) => {
          if (subWindow == null) {
            console.error('Failed to create the subWindow. Cause: The data is empty');
            return;
          }
          subWindow.setUIContent('pages/Index', (err) => {
            if (err.code) {
              console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
              return;
            }
            console.info('Succeeded in loading the subWindow content.');
            try {
              subWindow.showWindow((err: BusinessError) => {
                const errCode: number = err.code;
                if (errCode) {
                  console.error(`Failed to show the window. Error code: ${err.code}, message: ${err.message}`);
                  return;
                }
                console.info('Succeeded in showing the window.');
              });
            } catch (exception) {
              console.error(`Failed to show the window. Cause code: ${exception.code}, message: ${exception.message}`);
            }
          })
        });
      } catch (exception) {
        console.error(`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}`);
      }
  });
  }
```

#### showWindow9+

showWindow(): Promise<void>

显示当前窗口，使用Promise异步回调，支持系统窗口、应用子窗口、模态窗和全局悬浮窗，或将已显示的应用主窗口层级提升至顶部。


调用该接口前，建议优先通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法或者[setUIContent](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setuicontent9-1)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会一直显示启动界面；如果系统窗口、应用子窗口、模态窗和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
// EntryAbility.ets

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      try {
        // 创建子窗
        windowStage.createSubWindow("testSubWindow").then((subWindow) => {
          if (subWindow == null) {
            console.error('Failed to create the subWindow. Cause: The data is empty');
            return;
          }
          subWindow.setUIContent('pages/Index', (err) => {
            if (err.code) {
              console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
              return;
            }
            console.info('Succeeded in loading the subWindow content.');
            try {
              let promise = subWindow.showWindow();
              promise.then(() => {
                console.info('Succeeded in showing the window.');
              }).catch((err: BusinessError) => {
                console.error(`Failed to show the window. Error code: ${err.code}, message: ${err.message}`);
              });
            } catch (exception) {
              console.error(`Failed to show window. Cause code: ${exception.code}, message: ${exception.message}`);
            }
          });
      } catch (exception) {
        console.error(`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### showWindow20+

showWindow(options: ShowWindowOptions): Promise<void>

显示当前窗口或将已显示的应用主窗口的层级提升至顶部，支持传入参数来控制窗口显示的行为，使用Promise异步回调。

仅支持除TYPE_DIALOG类型的窗口和模态子窗口（即使用setSubWindowModal启用了子窗的模态属性）之外的应用子窗口、应用主窗、全局悬浮窗以及系统窗口。


调用该接口前，建议优先通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法或者[setUIContent](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setuicontent9-1)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会一直显示启动界面；如果系统窗口、应用子窗口和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShowWindowOptions | 是 | 显示子窗口或系统窗口时的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function showWindow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Modal subwindow and dialog window can not set focusOnShow. |
| 1300016 | Parameter validation error. Possible cause: 1. The value of the parameter is out of the allowed range; 2. The length of the parameter exceeds the allowed length; 3. The parameter format is incorrect. |

**示例：**

```ets
// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      // 创建子窗
      try {
        windowStage.createSubWindow('subWindow').then((data) => {
          if (data == null) {
            console.error('Failed to create the subWindow. Cause: The data is empty');
            return;
          }
          data.setUIContent('pages/Index', (err) => {
            if (err.code) {
              console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
              return;
            }
            console.info('Succeeded in loading the subWindow content.');
            let options: window.ShowWindowOptions = {
              focusOnShow: false
            };
            try {
              data.showWindow(options).then(() => {
                console.info('Succeeded in showing window');
              }).catch((err: BusinessError) => {
                console.error(`Failed to show window. Error code: ${err.code}, message: ${err.message}`);
              });
            } catch (exception) {
              console.error(`Failed to show window. Cause code: ${exception.code}, message: ${exception.message}`);
            }
          });
      } catch (exception) {
        console.error(`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
}
```

#### destroyWindow9+

destroyWindow(callback: AsyncCallback<void>): void

销毁当前窗口，使用callback异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.destroyWindow((err) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in destroying the window.');
});
```

#### destroyWindow9+

destroyWindow(): Promise<void>

销毁当前窗口，使用Promise异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.destroyWindow();
promise.then(() => {
  console.info('Succeeded in destroying the window.');
}).catch((err: BusinessError) => {
  console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### moveWindowTo9+

moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void

移动窗口位置，使用callback异步回调。调用成功即返回，但返回后无法立即获取最终生效结果。如需立即获取，请使用[moveWindowToAsync()](#ZH-CN_TOPIC_0000002522080752__movewindowtoasync12)。


-

不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）外的其他窗口模式下使用。

-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口相对于屏幕移动；在非自由窗口状态下，窗口相对于父窗口移动。

-

若需在非自由窗口状态下实现相对于屏幕的移动，请使用[moveWindowToGlobal()](#ZH-CN_TOPIC_0000002522080752__movewindowtoglobal15)。

-

该方法对非自由窗口状态下的主窗口无效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在y轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in moving the window.');
  });
} catch (exception) {
  console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### moveWindowTo9+

moveWindowTo(x: number, y: number): Promise<void>

移动窗口位置，使用Promise异步回调。调用成功即返回，但返回后无法立即获取最终生效结果。如需立即获取，请使用[moveWindowToAsync()](#ZH-CN_TOPIC_0000002522080752__movewindowtoasync12)。


-

不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）外的其他窗口模式下使用。

-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口相对于屏幕移动；在非自由窗口状态下，窗口相对于父窗口移动。

-

若需在非自由窗口状态下实现相对于屏幕的移动，请使用[moveWindowToGlobal()](#ZH-CN_TOPIC_0000002522080752__movewindowtoglobal15)。

-

该方法对非自由窗口状态下的主窗口无效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在y轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowTo(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### moveWindowToAsync12+

moveWindowToAsync(x: number, y: number): Promise<void>

移动窗口位置，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](#ZH-CN_TOPIC_0000002522080752__getwindowproperties9)（见示例）立即获取最终生效结果。


-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300010。

-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口相对于屏幕移动；在非自由窗口状态下，窗口相对于主窗口移动。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在y轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowToAsync(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(`Get window rect: ` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### moveWindowToAsync15+

moveWindowToAsync(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>

移动窗口位置，支持配置moveConfiguration参数指定窗口移动的目标屏幕ID，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](#ZH-CN_TOPIC_0000002522080752__getwindowproperties9)（见示例）立即获取最终生效结果。


-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300010。

-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口相对于屏幕移动；在非自由窗口状态下，窗口相对于主窗口移动。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动的值，值为正表示右移，单位为px，该参数应该为整数，非整数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动的值，值为正表示下移，单位为px，该参数应该为整数，非整数输入将向下取整。 |
| moveConfiguration | MoveConfiguration | 否 | 窗口移动选项，未设置将默认保持为当前屏幕。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let moveConfiguration: window.MoveConfiguration = {
    displayId: 0
  };
  let promise = windowClass.moveWindowToAsync(300, 300, moveConfiguration);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(`Get window rect: ` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### moveWindowToGlobal13+

moveWindowToGlobal(x: number, y: number): Promise<void>

基于屏幕坐标移动窗口位置，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](#ZH-CN_TOPIC_0000002522080752__getwindowproperties9)（见示例）立即获取最终生效结果。


-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300010。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 表示以屏幕左上角为起点，窗口在x轴方向移动的值，单位为px。值为正表示右移，值为负表示左移。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 表示以屏幕左上角为起点，窗口在y轴方向移动的值，单位为px。值为正表示下移，值为负表示上移。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowToGlobal(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(`Get window rect: ` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### moveWindowToGlobal15+

moveWindowToGlobal(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>

基于屏幕坐标移动窗口位置，支持配置moveConfiguration参数指定窗口移动的目标屏幕ID，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](#ZH-CN_TOPIC_0000002522080752__getwindowproperties9)（见示例）立即获取最终生效结果。


-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300010。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 表示以目标屏幕左上角为起点，窗口在x轴方向移动的值，单位为px。值为正表示右移，值为负表示左移。该参数应该为整数，非整数输入将向下取整。 |
| y | number | 是 | 表示以目标屏幕左上角为起点，窗口在y轴方向移动的值，单位为px。值为正表示下移，值为负表示上移。该参数应该为整数，非整数输入将向下取整。 |
| moveConfiguration | MoveConfiguration | 否 | 窗口移动选项，未设置将默认保持为当前屏幕。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let moveConfiguration: window.MoveConfiguration = {
    displayId: 0
  };
  let promise = windowClass.moveWindowToGlobal(300, 300, moveConfiguration);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(`Get window rect: ` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### moveWindowToGlobalDisplay20+

moveWindowToGlobalDisplay(x: number, y: number): Promise<void>

基于[全局坐标系](../../guides/窗口开发术语.md#全局坐标系)移动窗口位置，使用Promise异步回调。


-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300010。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 表示以主屏幕左上角为起点，窗口在x轴方向移动的值，单位为px。值为正表示右移，值为负表示左移。该参数应该为整数，非整数输入将向下取整。 |
| y | number | 是 | 表示以主屏幕左上角为起点，窗口在y轴方向移动的值，单位为px。值为正表示下移，值为负表示上移。该参数应该为整数，非整数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowToGlobalDisplay(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window in global display.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move the window in global display. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to move the window in global display. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### clientToGlobalDisplay20+

clientToGlobalDisplay(winX: number, winY: number): Position

将相对于当前窗口左上角的坐标转换为相对于主屏幕左上角的全局坐标。

不支持在经过显示缩放的窗口中调用，例如手机或平板设备在非自由多窗模式下的悬浮窗场景。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| winX | number | 是 | 表示以当前窗口左上角为原点的x轴方向偏移量，单位为px。值为正表示在原点右侧，值为负表示在原点左侧。该参数应为整数，非整数输入将向下取整。 |
| winY | number | 是 | 表示以当前窗口左上角为原点的y轴方向偏移量，单位为px。值为正表示在原点下方，值为负表示在原点上方。该参数应为整数，非整数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Position | 返回转换后的坐标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300010 | The operation in the current window status is invalid. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```ets
try {
  let position = windowClass.clientToGlobalDisplay(100, 100);
  console.info(`Succeeded in converting the position in the current window to the position in global display. Position: ` + JSON.stringify(position));
} catch (exception) {
  console.error(`Failed to convert the position. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### globalDisplayToClient20+

globalDisplayToClient(globalDisplayX: number, globalDisplayY: number): Position

将相对于主屏幕左上角的全局坐标转换为相对于当前窗口左上角的坐标。

不支持在经过显示缩放的窗口中调用，例如手机或平板设备在非自由多窗模式下的悬浮窗场景。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| globalDisplayX | number | 是 | 表示以当前窗口左上角为原点的x轴方向偏移量，单位为px。值为正表示在原点右侧，值为负表示在原点左侧。该参数应为整数，非整数输入将向下取整。 |
| globalDisplayY | number | 是 | 表示以当前窗口左上角为原点的y轴方向偏移量，单位为px。值为正表示在原点下方，值为负表示在原点上方。该参数应为整数，非整数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Position | 返回转换后的坐标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300010 | The operation in the current window status is invalid. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```ets
try {
  let position = windowClass.globalDisplayToClient(100, 100);
  console.info(`Succeeded in converting in the position in global display to the position in the current window. Position: ` + JSON.stringify(position));
} catch (exception) {
  console.error(`Failed to convert the position. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### resize9+

resize(width: number, height: number, callback: AsyncCallback<void>): void

基于窗口左上角顶点改变当前窗口大小，使用callback异步回调。

调用成功即返回，该接口返回后无法立即获取最终生效结果，如需立即获取，建议使用接口[resizeAsync()](#ZH-CN_TOPIC_0000002522080752__resizeasync12)。

窗口存在大小限制[WindowLimits](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__windowlimits11)，具体尺寸限制范围可以通过[getWindowLimits](#ZH-CN_TOPIC_0000002522080752__getwindowlimits11)接口进行查询。

调用该接口设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300002。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.resize(500, 1000, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in changing the window size.');
  });
} catch (exception) {
  console.error(`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### resize9+

resize(width: number, height: number): Promise<void>

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。

调用成功即返回，该接口返回后无法立即获取最终生效结果，如需立即获取，建议使用接口[resizeAsync()](#ZH-CN_TOPIC_0000002522080752__resizeasync12)。

窗口存在大小限制[WindowLimits](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__windowlimits11)，具体尺寸限制范围可以通过[getWindowLimits](#ZH-CN_TOPIC_0000002522080752__getwindowlimits11)接口进行查询。

调用该接口设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300002。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.resize(500, 1000);
  promise.then(() => {
    console.info('Succeeded in changing the window size.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### resizeAsync12+

resizeAsync(width: number, height: number): Promise<void>

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。

调用生效后返回，回调中可使用[getWindowProperties()](#ZH-CN_TOPIC_0000002522080752__getwindowproperties9)（见示例）立即获取最终生效结果。

窗口存在大小限制[WindowLimits](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__windowlimits11)，具体尺寸限制范围可以通过[getWindowLimits](#ZH-CN_TOPIC_0000002522080752__getwindowlimits11)接口进行查询。

调用该接口设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

-

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](#ZH-CN_TOPIC_0000002522080752__getwindowstatus12)获取）时调用生效，否则抛出错误码1300010。

-

在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: Invalid parameter range. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.resizeAsync(500, 1000);
  promise.then(() => {
    console.info('Succeeded in changing the window size.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(`Get window rect: ` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindowProperties9+

getWindowProperties(): WindowProperties

获取当前窗口的属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WindowProperties | 当前窗口属性。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
try {
  let properties = windowClass.getWindowProperties();
} catch (exception) {
  console.error(`Failed to obtain the window properties. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindowDensityInfo15+

getWindowDensityInfo(): WindowDensityInfo

获取当前窗口所在屏幕的系统显示大小缩放系数、系统默认显示大小缩放系数和自定义显示大小缩放系数信息。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WindowDensityInfo | 当前窗口的显示大小缩放系数信息。当返回值为[-1, -1, -1]时，表示当前设备不支持使用该接口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
try {
  let densityInfo = windowClass.getWindowDensityInfo();
} catch (exception) {
  console.error(`Failed to obtain the window densityInfo. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowContainerColor20+

setWindowContainerColor(activeColor: string, inactiveColor: string): void

设置主窗口容器在焦点态和非焦点态时的背景色。在Stage模型下，该接口需在调用[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)后使用。

窗口容器背景色覆盖整个窗口区域，包括标题栏和内容区域。当同时使用该接口和[setWindowBackgroundColor()](#ZH-CN_TOPIC_0000002522080752__setwindowbackgroundcolor9)设置背景色时，内容区域显示窗口背景色，标题栏显示窗口容器背景色。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码；从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**需要权限：** ohos.permission.SET_WINDOW_TRANSPARENT

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activeColor | string | 是 | 窗口容器处于焦点态时的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 |
| inactiveColor | string | 是 | 窗口容器处于非焦点态时的背景色，为十六进制RGB颜色或ARGB颜色（透明度固定为'FF'），不区分大小写，例如'#00FF00'或'#FF00FF00'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in loading the content.');
      // 获取应用主窗口。
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        let activeColor: string = '#00000000';
        let inactiveColor: string = '#FF000000';
        try {
          windowClass.setWindowContainerColor(activeColor, inactiveColor);
          console.info('Succeeded in setting window container color.');
        } catch (exception) {
          console.error(`Failed to set the window container color. Cause code: ${exception.code}, message: ${exception.message}`);
        };
      });
}
```

#### getGlobalRect13+

getGlobalRect(): Rect

获取窗口在其所在物理屏幕上的真实显示区域，同步接口。

在某些设备上，窗口显示时可能经过了缩放，此接口可以获取缩放后窗口在屏幕上的真实位置和大小。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Rect | 四元组分别表示距离屏幕左上角的x坐标、距离屏幕左上角的y坐标、缩放后的窗口宽度和缩放后的窗口高度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Failed to convert result into JS value object. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  let rect = windowClass.getGlobalRect();
  console.info(`Succeeded in getting window rect: ` + JSON.stringify(rect));
} catch (exception) {
  console.error(`Failed to get window rect. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindowAvoidArea9+

getWindowAvoidArea(type: [AvoidAreaType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7)): AvoidArea

获取当前窗口避让区域。

主窗口/子窗口：

- [自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下，仅存在固定态软键盘（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_KEYBOARD）类型的避让区域。

- 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_SYSTEM）类型的避让区域。

- 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

- 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

- 仅在调用[setSystemAvoidAreaEnabled](#ZH-CN_TOPIC_0000002522080752__setsystemavoidareaenabled18)方法使能后，才能通过此接口获取避让区域，否则获取的避让区域为空。

该接口一般适用于两种场景：

- 在[onWindowStageCreate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onwindowstagecreate)方法中，获取应用启动时的初始布局避让区域时可调用该接口。

- 当应用内子窗需要临时显示，对显示内容做布局避让时可调用该接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7) | 是 | 表示避让区域类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AvoidArea | 窗口内容避让区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Convert avoid area failed. |

**示例：**

```ets
let type = window.AvoidAreaType.TYPE_SYSTEM;
try {
  let avoidArea = windowClass.getWindowAvoidArea(type);
} catch (exception) {
  console.error(`Failed to obtain the area. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindowAvoidAreaIgnoringVisibility22+

getWindowAvoidAreaIgnoringVisibility(type: [AvoidAreaType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7)): AvoidArea

获取当前应用窗口的避让区域，即使避让区域当前处于不可见状态。

主窗口/子窗口：

- 主窗口在非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下，仅存在系统栏（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_SYSTEM）类型的避让区域。

- 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

- 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

- 仅在调用[setSystemAvoidAreaEnabled](#ZH-CN_TOPIC_0000002522080752__setsystemavoidareaenabled18)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7) | 是 | 表示避让区域类型。不支持获取软键盘类型的避让区域，传入TYPE_KEYBOARD时，返回1300016错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AvoidArea | 窗口内容避让区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Convert avoid area failed. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. |

**示例：**

```ets
let type = window.AvoidAreaType.TYPE_SYSTEM;
try {
  let avoidArea = windowClass.getWindowAvoidAreaIgnoringVisibility(type);
} catch (exception) {
  console.error(`Failed to obtain the area. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setSystemAvoidAreaEnabled18+

setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>

创建全局悬浮窗、模态窗或WindowType窗口类型为系统窗口时，调用该接口使能后才可以通过[getWindowAvoidArea()](#ZH-CN_TOPIC_0000002522080752__getwindowavoidarea9)获取窗口避让区信息或通过[on('avoidAreaChange')](#ZH-CN_TOPIC_0000002522080752__onavoidareachange9)监听窗口避让区变化。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否可以获取到避让区。 true表示可以获取避让区；false表示不可以获取避让区。默认值是false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only global floating windows, dialog windows, or Window Type as system windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      let windowClass: window.Window | undefined = undefined;
      let config: window.Configuration = {
        name: "test",
        windowType: window.WindowType.TYPE_DIALOG,
        decorEnabled: true,
        ctx: this.context
      };
      try {
        window.createWindow(config, (err: BusinessError, data) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}`);
            return;
          }
          windowClass = data;
          windowClass.setUIContent("pages/Test");
          let enabled = true;
          let promise = windowClass.setSystemAvoidAreaEnabled(enabled);
          promise.then(() => {
            let type = window.AvoidAreaType.TYPE_SYSTEM;
            let avoidArea = windowClass?.getWindowAvoidArea(type);
          }).catch((err: BusinessError) => {
            console.error(`Failed to obtain the system window avoid area. Cause code: ${err.code}, message: ${err.message}`);
          });
      } catch (exception) {
        console.error(`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### isSystemAvoidAreaEnabled18+

isSystemAvoidAreaEnabled(): boolean

获取悬浮窗、模态窗或WindowType为系统类型的窗口是否可以获取窗口内容的避让区[AvoidArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__avoidarea7)。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否可以获取窗口内容的避让区。 true表示可以获取避让区；false表示不可以获取避让区。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Create js value failed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let config: window.Configuration = {
  name: "test",
  windowType: window.WindowType.TYPE_DIALOG,
  decorEnabled: true,
  ctx: this.context
};
try {
  window.createWindow(config, (err: BusinessError, data) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    windowClass = data;
    windowClass.setUIContent("pages/Test");
    let enabled = true;
    let promise = windowClass.setSystemAvoidAreaEnabled(enabled);
    promise.then(() => {
      let enable = windowClass?.isSystemAvoidAreaEnabled();
    }).catch((err: BusinessError) => {
      console.error(`Failed to obtain whether the system window can get avoid area. Cause code: ${err.code}, message: ${err.message}`);
    });
} catch (exception) {
  console.error(`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setTitleAndDockHoverShown14+

setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>

设置主窗口进入全屏模式时鼠标Hover到热区上是否显示窗口标题栏和dock栏，使用Promise异步回调。

**系统能力**：SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTitleHoverShown | boolean | 否 | 是否显示窗口标题栏。 true表示显示窗口标题栏；false表示不显示窗口标题栏。默认值是true。 |
| isDockHoverShown | boolean | 否 | 是否显示dock栏。 true表示显示dock栏；false表示不显示dock栏。默认值是true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // 加载主窗口对应的页面。
    windowStage.loadContent('pages/Index', (err) => {
      let mainWindow: window.Window | undefined = undefined;
      // 获取应用主窗口。
      windowStage.getMainWindow().then(
        data => {
          if (!data) {
            console.error('Failed to get main window. Cause: The data is undefined.');
            return;
          }
          mainWindow = data;
          console.info(`Succeeded in obtaining the main window. Data: ${JSON.stringify(data)}`);
          // 调用maximize接口，设置窗口进入全屏模式。
          mainWindow.maximize(window.MaximizePresentation.ENTER_IMMERSIVE);
          // 调用setTitleAndDockHoverShown接口，隐藏标题栏和dock栏。
          mainWindow.setTitleAndDockHoverShown(false, false);
        }
      ).catch((err: BusinessError) => {
          if(err.code){
            console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
          }
      });
}
```

#### setWindowLayoutFullScreen9+

setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>

设置应用主窗口或应用子窗口的布局是否为沉浸式布局，使用Promise异步回调。其余窗口调用不生效也不报错。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.2之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.2开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错，切换到非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态时生效；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局状态栏、底部导航区域仍然显示）。true表示沉浸式布局；false表示非沉浸式布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen = true;
      try {
        let promise = windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
        promise.then(() => {
          console.info('Succeeded in setting the window layout to full-screen mode.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setImmersiveModeEnabledState12+

setImmersiveModeEnabledState(enabled: boolean): void

设置当前窗口是否开启沉浸式布局，该调用不会改变窗口模式和窗口大小。仅主窗口和子窗口可调用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.2之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.2开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启沉浸式布局。 true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and subwindows are supported. |

**示例：**

```ets
try {
  let enabled = false;
  windowClass.setImmersiveModeEnabledState(enabled);
} catch (exception) {
  console.error(`Failed to set the window immersive mode enabled status. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getImmersiveModeEnabledState12+

getImmersiveModeEnabledState(): boolean

查询当前窗口是否开启沉浸式布局。

仅支持主窗和子窗调用。

返回值与[setImmersiveModeEnabledState()](#ZH-CN_TOPIC_0000002522080752__setimmersivemodeenabledstate12)以及[setWindowLayoutFullScreen()](#ZH-CN_TOPIC_0000002522080752__setwindowlayoutfullscreen9)设置结果一致，若未调用上述两个接口则默认返回false。

**系统能力**：SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否设置开启沉浸式布局。 true表示开启沉浸式布局，false表示关闭沉浸式布局。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and subwindows are supported. |

**示例：**

```ets
try {
  let isEnabled = windowClass.getImmersiveModeEnabledState();
} catch (exception) {
  console.error(`Failed to get the window immersive mode enabled status. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### isImmersiveLayout20+

isImmersiveLayout(): boolean

查询当前窗口是否处于沉浸式布局状态。

**系统能力**：SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否处于沉浸式布局状态。true表示处于沉浸式布局状态，false表示不处于沉浸式布局状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
try {
  let isEnabled = windowClass.isImmersiveLayout();
} catch (exception) {
  console.error(`Failed to check if the window layout is in immersive mode. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowDelayRaiseOnDrag19+

setWindowDelayRaiseOnDrag(isEnabled: boolean): void

设置窗口是否使能延迟抬升，仅主窗和子窗可设置。

不调用此接口或传入false，主窗和子窗在鼠标左键按下时，默认立即抬升。

调用此接口使能延迟抬升后，在跨窗拖拽场景，可拖拽组件所在窗口在鼠标左键按下时不会立即抬升，直到鼠标左键抬起。

**系统能力**：SystemCapability.Window.SessionManager

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用； 在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否使能延迟抬升。 true表示使能窗口延迟抬升；false表示不使能窗口延迟抬升。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setWindowDelayRaiseOnDrag can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
try {
  windowClass.setWindowDelayRaiseOnDrag(true);
} catch (exception) {
  console.error(`Failed to set window delay raise. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setDragKeyFramePolicy20+

setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>

设置主窗口拖拽的关键帧策略，并使用Promise处理异步回调。

非主窗口调用时，返回1300004错误码。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备可正常调用，在其他设备中返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyFramePolicy | KeyFramePolicy | 是 | 用于设置拖拽的关键帧策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KeyFramePolicy> | Promise对象，返回实际生效的关键帧策略。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range; 2. The parameter format is incorrect. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let keyFramePolicy: window.KeyFramePolicy = {
        enable: true
      }
      try {
        let promise = windowClass.setDragKeyFramePolicy(keyFramePolicy);
        promise.then((ret: window.KeyFramePolicy) => {
          console.info(`Succeeded in setting key frame: ${JSON.stringify(ret)}`);
        }).catch((err: BusinessError) => {
          console.error(`Failed to set key frame. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set key frame. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setWindowSystemBarEnable9+

setWindowSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用Promise异步回调。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**设备行为差异：**

在HarmonyOS 5.0.0之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.0开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏/最大化模式时状态栏、底部导航区域是否显示。 例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// 此处以状态栏等均不显示为例
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = [];
      try {
        let promise = windowClass.setWindowSystemBarEnable(names);
        promise.then(() => {
          console.info('Succeeded in setting the system bar to be invisible.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### set[SpecificSystemBar](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604804__specificsystembar11)Enabled11+

set[SpecificSystemBar](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604804__specificsystembar11)Enabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>

设置主窗口状态栏、底部导航区域的显示或隐藏，使用Promise异步回调。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.0之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.0开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | [SpecificSystemBar](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604804__specificsystembar11) | 是 | 设置窗口全屏模式时，显示或隐藏的系统栏类型。 |
| enable | boolean | 是 | 设置窗口全屏模式时状态栏或底部导航区域是否显示，true表示显示， false表示隐藏。 |
| enableAnimation12+ | boolean | 否 | 设置状态栏或底部导航区域显示状态变化时是否使用动画，true表示使用， false表示不使用，默认值为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// 此处以隐藏状态栏为例
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        let promise = windowClass.setSpecificSystemBarEnabled('status', false);
        promise.then(() => {
          console.info('Succeeded in setting the system bar to be invisible.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setWindowSystemBarProperties9+

setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>

设置主窗口状态栏的属性，使用Promise异步回调。

子窗口调用后不生效。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | SystemBarProperties | 是 | 状态栏的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        //以下两个属性从API Version8开始支持
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      try {
        let promise = windowClass.setWindowSystemBarProperties(SystemBarProperties);
        promise.then(() => {
          console.info('Succeeded in setting the system bar properties.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### getWindowSystemBarProperties12+

getWindowSystemBarProperties(): SystemBarProperties

获取主窗口状态栏的属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SystemBarProperties | 当前状态栏属性。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Create js object failed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        let systemBarProperty = windowClass.getWindowSystemBarProperties();
        console.info('Success in obtaining system bar properties. Property: ' + JSON.stringify(systemBarProperty));
      } catch (err) {
        console.error(`Failed to get system bar properties. Code: ${err.code}, message: ${err.message}`);
      }
    });
  }
};
```

#### setStatusBarColor18+

setStatusBarColor(color: [ColorMetrics](../../topics/misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)): Promise<void>

设置主窗口状态栏的文字颜色，使用Promise异步回调。

子窗口不支持设置状态栏文字颜色，调用无效果。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ColorMetrics](../../topics/misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12) | 是 | 要设置的状态栏颜色值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported on this device. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics, window } from '@kit.ArkUI';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        let promise = windowClass.setStatusBarColor(ColorMetrics.numeric(0x112233));
        promise.then(() => {
          console.info('Succeeded in setting the status bar color.');
        }).catch((err: BusinessError) => {
          console.error(`Set the status bar color failed. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the status bar color. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### getStatusBarProperty18+

getStatusBarProperty(): StatusBarProperty

获取主窗口状态栏的属性，如状态栏文字颜色。

子窗口不支持查询，调用会返回错误码1300004。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| StatusBarProperty | 当前状态栏属性，如状态栏颜色。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        let statusBarProperty = windowClass.getStatusBarProperty();
        console.info('Succeeded in obtaining system bar properties. Property: ' + JSON.stringify(statusBarProperty));
      } catch (err) {
        console.error(`Failed to get system bar properties. Code: ${err.code}, message: ${err.message}`);
      }
    });
  }
};
```

#### setPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)9+

setPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)(orientation: Orientation, callback: AsyncCallback<void>): void

设置窗口的显示方向属性，使用callback异步回调。相关横竖屏开发实践查询[横竖屏切换](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-landscape-and-portrait-development)。

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，仅支持主窗口调用且生效，其他窗口类型调用后不生效。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，支持主窗口和WindowType为TYPE_WALLET_SWIPE_CARD的系统窗口调用且生效，其他窗口类型调用后不生效。当系统窗口调用setPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)接口时，若存在层级更高的窗口设置了显示方向，那么本次调用不会立即生效。此时，设置的显示方向会被记录，当不存在有更高层级且设置了显示方向的窗口时，将还原最后一次的方向请求。当WindowType为TYPE_WALLET_SWIPE_CARD的系统窗口设置显示方向且生效时，会将前台应用退至后台。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

设备行为差异： 该接口在支持sensor旋转且不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在支持sensor旋转，支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在支持sensor旋转，支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错，切换到非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下生效；在其他情况的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9) | 是 | 窗口显示方向的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。该回调函数返回调用结果是否成功，非应用旋转动效结束。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: Invalid parameter value range. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let orientation = window.Orientation.AUTO_ROTATION;
      try {
        windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to set window orientation. Cause code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('Succeeded in setting window orientation.');
        });
      } catch (exception) {
        console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)9+

setPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)(orientation: Orientation): Promise<void>

设置主窗口的显示方向属性，使用Promise异步回调。子窗口调用后不生效。

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，仅支持主窗口调用且生效，其他窗口类型调用后不生效。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，支持主窗口和WindowType为TYPE_WALLET_SWIPE_CARD的系统窗口调用且生效，其他窗口类型调用后不生效。当系统窗口调用setPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)接口时，若存在层级更高的窗口设置了显示方向，那么本次调用不会立即生效。此时，设置的显示方向会被记录，当不存在有更高层级且设置了显示方向的窗口时，将还原最后一次的方向请求。当WindowType为TYPE_WALLET_SWIPE_CARD的系统窗口设置显示方向且生效时，会将前台应用退至后台。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

设备行为差异： 该接口在支持sensor旋转且不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在支持sensor旋转，支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在支持sensor旋转，支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错，切换到非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下生效；在其他情况的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9) | 是 | 窗口显示方向的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: Invalid parameter value range. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let orientation = window.Orientation.AUTO_ROTATION;
      try {
        let promise = windowClass.setPreferredOrientation(orientation);
        promise.then(() => {
          console.info('Succeeded in setting the window orientation.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the window orientation. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### getPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)12+

getPreferred[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)(): Orientation

获取窗口的显示方向属性。未指定方向时，返回window.[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9).UNSPECIFIED。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9) | 窗口显示方向的属性。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        let orientation = windowClass.getPreferredOrientation();
      } catch (exception) {
        console.error(`Failed to get window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
};
```

#### getUIContext10+

getUIContext(): UIContext

获取UIContext实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIContext | 返回UIContext实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window, UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 为主窗口加载对应的目标页面。
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in loading the content.');
      // 获取应用主窗口。
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
        // 获取UIContext实例。
        let uiContext: UIContext | null = null;
        uiContext = windowClass.getUIContext();
      });
  }
};
```

#### setUIContent9+

setUIContent(path: string, callback: AsyncCallback<void>): void

根据当前工程中指定的某个页面路径为窗口加载具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.setUIContent('pages/page2/page3', (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in loading the content.');
  });
} catch (exception) {
  console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setUIContent9+

setUIContent(path: string): Promise<void>

根据当前工程中指定的某个页面路径为窗口加载具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.setUIContent('pages/page2/page3');
  promise.then(() => {
    console.info('Succeeded in loading the content.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### loadContent9+

loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

根据当前工程中指定的页面路径为窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用callback异步回调。建议在UIAbility启动过程中使用该接口，重复调用将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，该路径需添加到工程的main_pages.json文件中。 |
| storage | LocalStorage | 是 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
windowClass.loadContent('pages/page2', storage, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in loading the content.');
});
```

#### loadContent9+

loadContent(path: string, storage: LocalStorage): Promise<void>

根据当前工程中指定的页面路径为窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用Promise异步回调。建议在UIAbility启动过程中使用该接口，重复调用将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，该路径需添加到工程的main_pages.json文件中。 |
| storage | LocalStorage | 是 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
let promise = windowClass.loadContent('pages/page2', storage);
promise.then(() => {
  console.info('Succeeded in loading the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### loadContentByName11+

loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void

根据指定路由页面名称为当前窗口加载[命名路由](../classes/Class (Router).md)页面，通过LocalStorage传递状态属性至加载页面，使用callback异步回调。建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| storage | LocalStorage | 是 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets

import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import * as Index from '../pages/Index'; // 导入命名路由页面

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let storage: LocalStorage = new LocalStorage();
    let newValue: Number = 121;
    storage.setOrCreate('storageSimpleProp', newValue);
    try {
      let windowClass: window.Window = windowStage.getMainWindowSync();
      if (!windowClass) {
        console.error('Failed to get main window.');
        return;
      }
      windowClass.loadContentByName(Index.entryName, storage, (err: BusinessError) => {
        const errCode: number = err?.code;
        if (errCode) {
          console.error(`Failed to load the content. Cause code: ${err?.code}, message: ${err?.message}`);
          return;
        }
        console.info('Succeeded in loading the content.');
      });
    } catch (exception) {
      console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

```ets
// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName, useSharedStorage: true})
@Component
export struct Index {
  @State message: string = 'Hello World'
  @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### loadContentByName11+

loadContentByName(name: string, callback: AsyncCallback<void>): void

根据指定路由页面名称为当前窗口加载[命名路由](../classes/Class (Router).md)页面，使用callback异步回调。建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import * as Index from '../pages/Index'; // 导入命名路由页面

try {
  (windowClass as window.Window).loadContentByName(Index.entryName, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in loading the content.');
  });
} catch (exception) {
  console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

```ets
// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName})
@Component
export struct Index {
  @State message: string = 'Hello World'
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### loadContentByName11+

loadContentByName(name: string, storage?: LocalStorage): Promise<void>

根据指定路由页面名称为当前窗口加载[命名路由](../classes/Class (Router).md)页面，通过LocalStorage传递状态属性至加载页面，使用Promise异步回调。建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| storage | LocalStorage | 否 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import * as Index from '../pages/Index'; // 导入命名路由页面

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
try {
  let promise = (windowClass as window.Window).loadContentByName(Index.entryName, storage);
  promise.then(() => {
    console.info('Succeeded in loading the content.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

```ets
// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName, useSharedStorage: true})
@Component
export struct Index {
  @State message: string = 'Hello World'
  @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### isWindowShowing9+

isWindowShowing(): boolean

判断当前窗口是否已显示。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否已显示。true表示当前窗口已显示，false则表示当前窗口未显示。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
try {
  let data = windowClass.isWindowShowing();
  console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
} catch (exception) {
  console.error(`Failed to check whether the window is showing. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('windowSizeChange')7+

on(type: 'windowSizeChange', callback: Callback<Size>): void

开启窗口尺寸变化的监听。仅在主线程调用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowSizeChange'，即窗口尺寸变化事件。 |
| callback | Callback<Size> | 是 | 回调函数。返回当前的窗口尺寸。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
try {
  windowClass.on('windowSizeChange', (data) => {
    console.info('Succeeded in enabling the listener for window size changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(`Failed to enable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('windowSizeChange')7+

off(type: 'windowSizeChange', callback?: Callback<Size>): void

关闭窗口尺寸变化的监听。仅在主线程调用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowSizeChange'，即窗口尺寸变化事件。 |
| callback | Callback<Size> | 否 | 回调函数。返回当前的窗口尺寸。如果传入参数，则关闭该监听。如果未传入参数，则关闭窗口尺寸变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ets
const callback = (size: window.Size) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('windowSizeChange', callback);
  // 关闭指定callback的监听
  windowClass.off('windowSizeChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('windowSizeChange');
} catch (exception) {
  console.error(`Failed to disable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('avoidAreaChange')9+

on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void

开启当前应用窗口系统规避区变化的监听。

主窗口/子窗口：

- [自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下触发回调时，仅存在固定态软键盘（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_KEYBOARD）类型的避让区域。

- 主窗口在非自由窗口状态的自由悬浮窗口模式下触发回调时，仅存在系统栏（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_SYSTEM）类型的避让区域。

- 主窗口在其余场景下触发回调时，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能返回计算后的避让区域，否则直接返回空的避让区域。

- 子窗口在非自由窗口状态或非自由悬浮窗口模式下触发回调时，仅当子窗口的位置和大小与主窗口一致时，才能返回计算后的子窗口避让区域，否则直接返回空的避让区域。

全局悬浮窗、模态窗或系统窗口：

- 仅在调用[setSystemAvoidAreaEnabled](#ZH-CN_TOPIC_0000002522080752__setsystemavoidareaenabled18)方法使能后，触发回调时才能返回计算后的避让区域，否则直接返回空的避让区域。

常见的触发避让区回调的场景如下：应用窗口在全屏模式、悬浮模式、分屏模式之间的切换；应用窗口旋转；多折叠设备在屏幕折叠态和展开态之间的切换；应用窗口在多设备之间的流转。实现沉浸式布局可参考[开发应用沉浸式效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'avoidAreaChange'，即系统规避区变化事件。 |
| callback | Callback<AvoidAreaOptions> | 是 | 回调函数。返回当前规避区以及规避区类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
try {
  windowClass.on('avoidAreaChange', (data) => {
    console.info('Succeeded in enabling the listener for system avoid area changes. type:' +
    JSON.stringify(data.type) + ', area: ' + JSON.stringify(data.area));
  });
} catch (exception) {
  console.error(`Failed to enable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('avoidAreaChange')9+

off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void

关闭当前窗口系统规避区变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'avoidAreaChange'，即系统规避区变化事件。 |
| callback | Callback<AvoidAreaOptions> | 否 | 回调函数。返回当前规避区以及规避区类型。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有系统规避区变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ets
interface Param {
  type: window.AvoidAreaType,
  area: window.AvoidArea
}
const callback = (data: Param) => {
  // ...
}
try {
  windowClass.on('avoidAreaChange', callback);

  windowClass.off('avoidAreaChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('avoidAreaChange');
} catch (exception) {
  console.error(`Failed to enable or disable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('keyboardHeightChange')7+

on(type: 'keyboardHeightChange', callback: Callback<number>): void

开启固定态软键盘高度变化的监听。当软键盘从本窗口唤出且与窗口有重叠区域时，通知键盘高度变化。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardHeightChange'，即键盘高度变化事件。 |
| callback | Callback<number> | 是 | 回调函数。返回当前的键盘高度。返回值为整数，单位为px。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.on('keyboardHeightChange', (data) => {
    console.info('Succeeded in enabling the listener for keyboard height changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(`Failed to enable the listener for keyboard height changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('keyboardHeightChange')7+

off(type: 'keyboardHeightChange', callback?: Callback<number>): void

关闭固定态软键盘高度变化的监听，使应用程序不再接收键盘高度变化的通知。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardHeightChange'，即键盘高度变化事件。 |
| callback | Callback<number> | 否 | 回调函数。返回当前的键盘高度，返回值为整数，单位为px。若传入参数，则关闭该监听；未传入参数，则关闭所有固定态软键盘高度变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const callback = (height: number) => {
  // ...
}
try {
  windowClass.on('keyboardHeightChange', callback);

  windowClass.off('keyboardHeightChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('keyboardHeightChange');
} catch (exception) {
  console.error(`Failed to disable the listener for keyboard height changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('keyboardWillShow')20+

on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void

开启固定态软键盘即将开始显示的监听。此监听在固定态软键盘即将开始显示或软键盘由悬浮态切换为固定态时触发。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillShow'，即固定态软键盘即将开始显示的事件。 |
| callback | Callback<KeyboardInfo> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(`Keyboard will show animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillShow', callback);
  console.info(`Register keyboard will show animation success`);
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('keyboardWillShow')20+

off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘即将开始显示的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillShow'，即固定态软键盘即将开始显示的事件。 |
| callback | Callback<KeyboardInfo> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘即将开始显示的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(`Keyboard will show animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillShow', callback);
  windowClass.off('keyboardWillShow', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('keyboardWillShow');
  console.info(`Unregister keyboard will show animation success`);
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('keyboardWillHide')20+

on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void

开启固定态软键盘即将开始隐藏的监听。此监听在固定态软键盘即将开始隐藏或软键盘由固定态切换为悬浮态时触发。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillHide'，即固定态软键盘即将开始隐藏的事件。 |
| callback | Callback<KeyboardInfo> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(`Keyboard will hide animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillHide', callback);
  console.info(`Register keyboard will hide animation success`);
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('keyboardWillHide')20+

off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘即将开始隐藏的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillHide'，即固定态软键盘即将开始隐藏的事件。 |
| callback | Callback<KeyboardInfo> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘即将开始隐藏的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(`Keyboard will hide animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillHide', callback);
  windowClass.off('keyboardWillHide', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('keyboardWillHide');
  console.info(`Unregister keyboard will hide animation success`);
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('keyboardDidShow')18+

on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void

开启固定态软键盘显示动画完成的监听。此监听在固定态软键盘显示动画完成或软键盘由悬浮态切换至固定态时触发。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidShow'，即固定态软键盘显示动画完成事件。 |
| callback | Callback<KeyboardInfo> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.on('keyboardDidShow', (keyboardInfo) => {
    console.info('keyboard show animation completion. keyboardInfo: ' + JSON.stringify(keyboardInfo));
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('keyboardDidShow')18+

off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘显示动画完成的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidShow'，即固定态软键盘显示动画完成事件。 |
| callback | Callback<KeyboardInfo> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘显示动画完成的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  // ...
}
try {
  windowClass.on('keyboardDidShow', callback);
  windowClass.off('keyboardDidShow', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('keyboardDidShow');
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('keyboardDidHide')18+

on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void

开启固定态软键盘隐藏动画完成的监听。此监听在固定态软键盘隐藏动画完成或软键盘由固定态切换至悬浮态时触发。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidHide'，即固定态软键盘隐藏动画完成事件。 |
| callback | Callback<KeyboardInfo> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.on('keyboardDidHide', (keyboardInfo) => {
    console.info('keyboard hide animation completion. keyboardInfo: ' + JSON.stringify(keyboardInfo));
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('keyboardDidHide')18+

off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘隐藏动画完成的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见[输入法服务](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidHide'，即固定态软键盘隐藏动画完成事件。 |
| callback | Callback<KeyboardInfo> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘隐藏动画完成的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  // ...
}
try {
  windowClass.on('keyboardDidHide', callback);
  windowClass.off('keyboardDidHide', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('keyboardDidHide');
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('touchOutside')11+

on(type: 'touchOutside', callback: Callback<void>): void

开启本窗口区域范围外的点击事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'touchOutside'，即本窗口范围外的点击事件。 |
| callback | Callback<void> | 是 | 回调函数。当点击事件发生在本窗口范围之外的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
try {
  windowClass.on('touchOutside', () => {
    console.info('touch outside');
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('touchOutside')11+

off(type: 'touchOutside', callback?: Callback<void>): void

关闭本窗口区域范围外的点击事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'touchOutside'，即本窗口范围外的点击事件。 |
| callback | Callback<void> | 否 | 回调函数。当点击事件发生在本窗口范围之外的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口区域范围外的点击事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ets
const callback = () => {
  // ...
}
try {
  windowClass.on('touchOutside', callback);
  windowClass.off('touchOutside', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('touchOutside');
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('screenshot')9+

on(type: 'screenshot', callback: Callback<void>): void

开启截屏事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshot'，即截屏事件，对控制中心截屏、hdc命令截屏、整屏截屏接口生效。 |
| callback | Callback<void> | 是 | 回调函数。发生截屏事件时的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
try {
  windowClass.on('screenshot', () => {
    console.info('screenshot happened');
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('screenshot')9+

off(type: 'screenshot', callback?: Callback<void>): void

关闭截屏事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshot'，即截屏事件。 |
| callback | Callback<void> | 否 | 回调函数。发生截屏事件时的回调。若传入参数，则关闭该监听。若未传入参数，则关闭所有截屏事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ets
let callback = () => {
  console.info('screenshot happened');
};
try {
  windowClass.on('screenshot', callback);
  windowClass.off('screenshot', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('screenshot');
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('screenshotAppEvent')20+

on(type: 'screenshotAppEvent', callback: Callback<[ScreenshotEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__screenshoteventtype20)>): void

开启屏幕截屏事件类型的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshotAppEvent'，即屏幕截屏的事件类型，对控制中心截屏、快捷键截屏以及滚动截屏生效。 |
| callback | Callback<[ScreenshotEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__screenshoteventtype20)> | 是 | 回调函数。返回触发的截屏事件类型。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (eventType: window.ScreenshotEventType) => {
  console.info(`screenshotAppEvent happened. Event: ${eventType}`);
}
try {
  windowClass.on('screenshotAppEvent', callback);
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('screenshotAppEvent')20+

off(type: 'screenshotAppEvent', callback?: Callback<[ScreenshotEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__screenshoteventtype20)>): void

关闭屏幕截屏事件类型的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshotAppEvent'，即屏幕截屏的事件类型。 |
| callback | Callback<[ScreenshotEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__screenshoteventtype20)> | 否 | 回调函数。返回触发的截屏事件类型。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口截图事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (eventType: window.ScreenshotEventType) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('screenshotAppEvent', callback);
  // 关闭指定callback的监听
  windowClass.off('screenshotAppEvent', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('screenshotAppEvent');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('dialogTargetTouch')10+

on(type: 'dialogTargetTouch', callback: Callback<void>): void

开启模态窗口所遮盖窗口的点击或触摸事件的监听，除模态窗口以外其他窗口调用此接口不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'dialogTargetTouch'，即模态窗口所遮盖窗口的点击或触摸事件。 |
| callback | Callback<void> | 是 | 回调函数。当点击或触摸事件发生在模态窗口所遮盖窗口的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
try {
  windowClass.on('dialogTargetTouch', () => {
    console.info('touch dialog target');
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('dialogTargetTouch')10+

off(type: 'dialogTargetTouch', callback?: Callback<void>): void

关闭模态窗口目标窗口的点击事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'dialogTargetTouch'，即模态窗口目标窗口的点击事件。 |
| callback | Callback<void> | 否 | 回调函数。当点击事件发生在模态窗口目标窗口的回调。若传入参数，则关闭该监听。若未传入参数，则关闭所有模态窗口目标窗口的点击事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ets
const callback = () => {
  // ...
}
try {
  windowClass.on('dialogTargetTouch', callback);
  windowClass.off('dialogTargetTouch', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('dialogTargetTouch');
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('windowEvent')10+

on(type: 'windowEvent', callback: Callback<[WindowEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windoweventtype10)>): void

开启窗口生命周期变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowEvent'，即窗口生命周期变化事件。 |
| callback | Callback<[WindowEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windoweventtype10)> | 是 | 回调函数。返回当前的窗口生命周期状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
try {
  windowClass.on('windowEvent', (data) => {
    console.info('Window event happened. Event:' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('windowEvent')10+

off(type: 'windowEvent', callback?: Callback<[WindowEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windoweventtype10)>): void

关闭窗口生命周期变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowEvent'，即窗口生命周期变化事件。 |
| callback | Callback<[WindowEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windoweventtype10)> | 否 | 回调函数。返回当前的窗口生命周期状态。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口生命周期变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ets
const callback = (windowEventType: window.WindowEventType) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('windowEvent', callback);
  // 关闭指定callback的监听
  windowClass.off('windowEvent', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('windowEvent');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('displayIdChange')14+

on(type: 'displayIdChange', callback: Callback<number>): void

开启本窗口所处屏幕变化事件的监听。比如，当前窗口移动到其他屏幕时，可以从此接口监听到这个行为。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'displayIdChange'，即本窗口所处屏幕变化的事件。 |
| callback | Callback<number> | 是 | 回调函数。当本窗口所处屏幕发生变化后的回调。回调函数返回number类型参数，表示窗口所处屏幕的displayId。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
try {
  windowClass.on('displayIdChange', (data) => {
    console.info('Window displayId changed, displayId=' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('displayIdChange')14+

off(type: 'displayIdChange', callback?: Callback<number>): void

关闭本窗口所处屏幕变化事件的监听。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'displayIdChange'，即本窗口所处屏幕变化的事件。 |
| callback | Callback<number> | 否 | 回调函数。当本窗口所处屏幕发生变化时的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口所处屏幕变化事件的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
const callback = (displayId: number) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('displayIdChange', callback);
  // 关闭指定callback的监听
  windowClass.off('displayIdChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('displayIdChange');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('windowVisibilityChange')11+

on(type: 'windowVisibilityChange', callback: Callback<boolean>): void

开启本窗口可见状态变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景：

- 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setwindowshadowenabled20)和[setWindowShadowRadius](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setwindowshadowradius17)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是完全可见，但实际返回的是部分可见。

- 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。

- 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowVisibilityChange'，即本窗口可见状态变化的事件。 |
| callback | Callback<boolean> | 是 | 回调函数。当本窗口可见状态发生变化后的回调。回调函数返回boolean类型参数，当返回参数为true时表示窗口可见，否则表示窗口不可见。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  windowClass.on('windowVisibilityChange', (boolean) => {
    console.info('Window visibility changed, isVisible=' + boolean);
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('windowVisibilityChange')11+

off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void

关闭本窗口可见状态变化事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowVisibilityChange'，即本窗口可见状态变化的事件。 |
| callback | Callback<boolean> | 否 | 回调函数。当本窗口可见状态发生变化时的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口可见状态变化事件的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (bool: boolean) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('windowVisibilityChange', callback);
  // 关闭指定callback的监听
  windowClass.off('windowVisibilityChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('windowVisibilityChange');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('occlusionStateChanged')22+

on(type: 'occlusionStateChanged', callback: Callback<[OcclusionState](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__occlusionstate22)>): void

开启窗口[可见性状态](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__occlusionstate22)变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景：

- 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setwindowshadowenabled20)和[setWindowShadowRadius](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setwindowshadowradius17)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是完全可见，但实际返回的是部分可见。

- 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。

- 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'occlusionStateChanged'，即窗口可见性变化事件。 |
| callback | Callback<[OcclusionState](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__occlusionstate22)> | 是 | 窗口可见性变化时的回调函数。详情见可见性状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  let callback: Callback<window.OcclusionState> = (data: window.OcclusionState) => {
    console.info(`Window occlusion state changed: ${data}`);
  };
  windowClass.on('occlusionStateChanged', callback);
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('occlusionStateChanged')22+

off(type: 'occlusionStateChanged', callback?: Callback<[OcclusionState](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__occlusionstate22)>): void

关闭窗口[可见性状态](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__occlusionstate22)变化事件的监听。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'occlusionStateChanged'，即窗口可见性变化事件。 |
| callback | Callback<[OcclusionState](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__occlusionstate22)> | 否 | 若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口可见性变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  let callback: Callback<window.OcclusionState> = (data: window.OcclusionState) => {
    console.info(`Window occlusion state changed: ${data}`);
  };
  // 通过on接口开启监听
  windowClass.on('occlusionStateChanged', callback);
  // 关闭指定callback的监听
  windowClass.off('occlusionStateChanged', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('occlusionStateChanged');
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('frameMetricsMeasured')22+

on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void

开启窗口帧率指标变化事件的监听。该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

应用注册帧率变化监听后，只有当客户端UI内容发生重绘时（如页面切换、和可响应组件交互、设置背景色和透明度等），才会触发注册的回调。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'frameMetricsMeasured'，即窗口帧率指标变化事件。 |
| callback | Callback<FrameMetrics> | 是 | 窗口帧率指标变化时的回调函数。详情见帧率指标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
try {
  let callback: Callback<window.FrameMetrics> = (data: window.FrameMetrics) => {
    console.info(`Window frame metrics changed: ${JSON.stringify(data)}`);
  };
  windowClass.on('frameMetricsMeasured', callback);
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('frameMetricsMeasured')22+

off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void

关闭窗口帧率指标变化事件的监听。该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'frameMetricsMeasured'，即窗口帧率指标变化事件。 |
| callback | Callback<FrameMetrics> | 否 | 若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口帧率指标变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
try {
  let callback: Callback<window.FrameMetrics> = (data: window.FrameMetrics) => {
    console.info(`Window frame metrics changed: ${JSON.stringify(data)}`);
  };
  // 通过on接口开启监听
  windowClass.on('frameMetricsMeasured', callback);
  // 关闭指定callback的监听
  windowClass.off('frameMetricsMeasured', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('frameMetricsMeasured');
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('systemDensityChange')15+

on(type: 'systemDensityChange', callback: Callback<number>): void

开启本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。比如，当调整窗口所处屏幕的显示大小缩放系数时，可以从此接口监听到这个行为。

在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp * density = px。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemDensityChange'，即本窗口所处屏幕的系统显示大小缩放系数变化的事件。 |
| callback | Callback<number> | 是 | 回调函数。当本窗口所处屏幕的系统显示大小缩放系数发生变化后的回调。回调函数返回number类型参数，表示当前窗口所处屏幕的系统显示大小缩放系数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
const callback = (density: number) => {
  console.info('System density changed, density=' + JSON.stringify(density));
  // 通过回调返回值计算px
  let vp = 100;
  let px = vp * density;
}
try {
  windowClass.on('systemDensityChange', callback);
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('systemDensityChange')15+

off(type: 'systemDensityChange', callback?: Callback<number>): void

关闭本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。

在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp * density = px。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemDensityChange'，即本窗口所处屏幕的系统显示大小缩放系数变化的事件。 |
| callback | Callback<number> | 否 | 回调函数。当本窗口所处屏幕的系统显示大小缩放系数发生变化后的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口所处屏幕的系统显示大小缩放系数变化事件的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
const callback = (density: number) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('systemDensityChange', callback);
  // 关闭指定callback的监听
  windowClass.off('systemDensityChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('systemDensityChange');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('noInteractionDetected')12+

on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void

开启本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'noInteractionDetected'，即本窗口在指定超时时间内无交互的事件。 |
| timeout | number | 是 | 指定本窗口在多长时间内无交互即回调，单位为秒(s)。该参数仅支持整数输入，负数和小数为非法参数。 |
| callback | Callback<void> | 是 | 回调函数。当本窗口在指定超时时间内无交互事件时的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  windowClass.on('noInteractionDetected', 60, () => {
    console.info('no interaction in 60s');
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('noInteractionDetected')12+

off(type: 'noInteractionDetected', callback?: Callback<void>): void

关闭本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'noInteractionDetected'，即本窗口在指定超时时间内无交互的事件。 |
| callback | Callback<void> | 否 | 回调函数，当本窗口在指定超时时间内无交互事件时的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口在指定超时时间内无交互事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = () => {
  // ...
}
try {
  windowClass.on('noInteractionDetected', 60, callback);
  windowClass.off('noInteractionDetected', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('noInteractionDetected');
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('windowStatusChange')11+

on(type: 'windowStatusChange', callback: Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)>): void

开启窗口模式变化的监听，当窗口windowStatus发生变化时进行通知（此时窗口属性可能还没有更新，如果需要在收到windowStatus变化通知时能够立即获取到变化后的窗口大小、位置，建议使用[on('windowStatusDidChange')](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__onwindowstatusdidchange20)）。

使用当前接口开启监听后，在调用maximize、recover方法时会收到多次回调，如需获取去重后的回调，可使用[on('windowStatusDidChange')](#ZH-CN_TOPIC_0000002522080752__onwindowstatusdidchange20)。


在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，应用的[targetAPIVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#配置文件标签)设置小于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::FULL_SCREEN。应用的[targetAPIVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#配置文件标签)设置大于等于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::MAXIMIZE。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusChange'，即窗口模式变化事件。 |
| callback | Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)> | 是 | 回调函数。返回当前的窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
try {
    windowClass.on('windowStatusChange', (WindowStatusType) => {
        console.info('Succeeded in enabling the listener for window status changes. Data: ' + JSON.stringify(WindowStatusType));
    });
} catch (exception) {
    console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('windowStatusChange')11+

off(type: 'windowStatusChange', callback?: Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)>): void

关闭窗口模式变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusChange'，即窗口模式变化事件。 |
| callback | Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)> | 否 | 回调函数。返回当前的窗口模式。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有窗口模式变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
const callback = (windowStatusType: window.WindowStatusType) => {
    // ...
}
try {
    windowClass.on('windowStatusChange', callback);
    windowClass.off('windowStatusChange', callback);
    // 如果通过on开启多个callback进行监听，同时关闭所有监听：
    windowClass.off('windowStatusChange');
} catch (exception) {
    console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('windowStatusDidChange')20+

on(type: 'windowStatusDidChange', callback: Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)>): void

开启窗口模式变化的监听，当窗口windowStatus发生变化后进行通知（此时窗口[Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__rect7)属性已经完成更新）。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusDidChange'，即窗口模式变化完成事件。 |
| callback | Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)> | 是 | 回调函数。返回当前的窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
try {
    windowClass.on('windowStatusDidChange', (WindowStatusType) => {
        console.info(`Succeeded in enabling the listener for window status changes. Data: ${JSON.stringify(WindowStatusType)}`);
    });
} catch (exception) {
    console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('windowStatusDidChange')20+

off(type: 'windowStatusDidChange', callback?: Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)>): void

关闭窗口模式变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusDidChange'，即窗口模式变化完成事件。 |
| callback | Callback<[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)> | 否 | 回调函数。返回当前的窗口模式。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有窗口模式变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
const callback = (windowStatusType: window.WindowStatusType) => {
    // ...
}
try {
    windowClass.on('windowStatusDidChange', callback);
    windowClass.off('windowStatusDidChange', callback);
    // 如果通过on开启多个callback进行监听，同时关闭所有监听：
    windowClass.off('windowStatusDidChange');
} catch (exception) {
    console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowGrayScale12+

setWindowGrayScale(grayScale: number): Promise<void>

设置窗口灰阶，使用Promise异步回调。该接口需要在调用[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)使窗口加载页面内容后调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| grayScale | number | 是 | 窗口灰阶。该参数为浮点数，取值范围为[0.0, 1.0]。0.0表示窗口图像无变化，1.0表示窗口图像完全转为灰度图像，0.0至1.0之间时效果呈线性变化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass?.setUIContent('pages/Index', (error: BusinessError) => {
  if (error.code) {
    console.error(`Failed to set the content. Cause code: ${error.code}`);
    return;
  }
  console.info('Succeeded in setting the content.');
  let grayScale: number = 0.5;
  try {
    if (canIUse("SystemCapability.Window.SessionManager")) {
      let promise = windowClass?.setWindowGrayScale(grayScale);
      promise?.then(() => {
        console.info('Succeeded in setting the grayScale.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the grayScale. Cause code: ${err.code}, message: ${err.message}`);
      });
    }
  } catch (exception) {
    console.error(`Failed to set the grayScale. Cause code: ${exception.code}, message: ${exception.message}`);
  }
});
```

#### on('windowTitleButtonRectChange')11+

on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void

开启窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowTitleButtonRectChange'，即标题栏上的最小化、最大化、关闭按钮矩形区域变化事件。 |
| callback | Callback<TitleButtonRect> | 是 | 回调函数。返回当前标题栏上的最小化、最大化、关闭按钮矩形区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
windowClass.setUIContent('pages/WindowPage').then(() => {
  try {
    windowClass?.on('windowTitleButtonRectChange', (titleButtonRect) => {
      console.info('Succeeded in enabling the listener for window title buttons area changes. Data: ' + JSON.stringify(titleButtonRect));
    });
  } catch (exception) {
    console.error(`Failed to enable the listener for window title buttons area changes. Cause code: ${exception.code}, message: ${exception.message}`);
  }
})
```

#### off('windowTitleButtonRectChange')11+

off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void

关闭窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowTitleButtonRectChange'，即标题栏上的最小化、最大化、关闭按钮矩形区域变化事件。 |
| callback | Callback<TitleButtonRect> | 否 | 回调函数。返回当前标题栏上的最小化、最大化、关闭按钮矩形区域。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
windowClass.setUIContent('pages/WindowPage').then(() => {
    const callback = (titleButtonRect: window.TitleButtonRect) => {
        // ...
    }
  try {
    // 通过on接口开启监听
    windowClass?.on('windowTitleButtonRectChange', callback);
    // 关闭指定callback的监听
    windowClass?.off('windowTitleButtonRectChange', callback);
    // 如果通过on开启多个callback进行监听，同时关闭所有监听：
    windowClass?.off('windowTitleButtonRectChange');
  } catch (exception) {
    console.error(`Failed to disable the listener for window title buttons area changes. Cause code: ${exception.code}, message: ${exception.message}`);
  }
})
```

#### on('windowRectChange')12+

on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void

开启窗口矩形（窗口位置及窗口大小）变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowRectChange'，即窗口矩形变化事件。 |
| callback | Callback<RectChangeOptions> | 是 | 回调函数。返回当前窗口矩形变化值及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  windowClass.on('windowRectChange', (data: window.RectChangeOptions) => {
      console.info(`Succeeded in enabling the listener for window rect changes. Data: ${JSON.stringify(data)}`);
  });
} catch (exception) {
  console.error(`Failed to disable the listener for window rect changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('windowRectChange')12+

off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void

关闭窗口矩形（窗口位置及窗口大小）变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowRectChange'，即窗口矩形变化事件。 |
| callback | Callback<RectChangeOptions> | 否 | 回调函数。返回当前的窗口矩形及变化原因。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有窗口矩形变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (rectChangeOptions: window.RectChangeOptions) => {
  // ...
}

try {
  windowClass.on('windowRectChange', callback);
  windowClass.off('windowRectChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('windowRectChange');
} catch (exception) {
  console.error(`Failed to disable the listener for window rect changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('rectChangeInGlobalDisplay')20+

on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void

开启[全局坐标系](../../guides/窗口开发术语.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChangeInGlobalDisplay'，即全局坐标系下窗口矩形变化事件。 |
| callback | Callback<RectChangeOptions> | 是 | 回调函数。返回当前窗口矩形变化值及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (rectChangeOptions: window.RectChangeOptions) => {
  console.info(`Succeeded in enabling the listener for window rect changes in global display. Data: ` + JSON.stringify(rectChangeOptions));
}

try {
  windowClass.on('rectChangeInGlobalDisplay', callback);
} catch (exception) {
  console.error(`Failed to enable the listener for window rect changes in global display. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('rectChangeInGlobalDisplay')20+

off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void

关闭[全局坐标系](../../guides/窗口开发术语.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChangeInGlobalDisplay'，即全局坐标系下窗口矩形变化事件。 |
| callback | Callback<RectChangeOptions> | 否 | 回调函数。返回当前的窗口矩形及变化原因。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有全局坐标系下窗口矩形变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (rectChangeOptions: window.RectChangeOptions) => {
  // ...
}

try {
  windowClass.on('rectChangeInGlobalDisplay', callback);
  windowClass.off('rectChangeInGlobalDisplay', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('rectChangeInGlobalDisplay');
} catch (exception) {
  console.error(`Failed to disable the listener for window rect changes in global display. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('subWindowClose')12+

on(type: 'subWindowClose', callback: Callback<void>): void

开启子窗口关闭事件的监听。此监听仅在点击系统提供的右上角关闭按钮关闭子窗时触发，其余关闭方式不触发回调。

当重复注册窗口关闭事件的监听时，最后一次注册成功的监听事件生效。

该接口触发的窗口关闭事件监听回调函数是同步执行，子窗口的异步关闭事件监听参考[on('windowWillClose')](#ZH-CN_TOPIC_0000002522080752__onwindowwillclose15)方法。

如果存在[on('windowWillClose')](#ZH-CN_TOPIC_0000002522080752__onwindowwillclose15)监听事件，只响应[on('windowWillClose')](#ZH-CN_TOPIC_0000002522080752__onwindowwillclose15)接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'subWindowClose'，即子窗口关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。当点击子窗口右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑的返回值决定当前子窗是否继续关闭，如果返回boolean类型的true表示不关闭子窗，返回false或者其他非boolean类型表示关闭子窗。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
const callback = () => {
  // ...
  return true;
}
try {
  windowClass.on('subWindowClose', callback);
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('subWindowClose')12+

off(type: 'subWindowClose', callback?: Callback<void>): void

关闭子窗口关闭事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'subWindowClose'，即子窗口关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。当点击子窗口右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑的返回值决定当前子窗是否继续关闭，如果返回boolean类型的true表示不关闭子窗，返回false或者其他非boolean类型表示关闭子窗。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有子窗口关闭的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
const callback = () => {
  // ...
  return true;
}
try {
  windowClass.on('subWindowClose', callback);
  windowClass.off('subWindowClose', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('subWindowClose');
} catch (exception) {
  console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('windowWillClose')15+

on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void

开启主窗口或子窗口关闭事件的监听。此监听仅能通过系统提供的窗口标题栏关闭按键触发，其余关闭窗口的方式不触发回调。

该接口触发的回调函数是异步执行。子窗口的同步关闭事件监听参考[on('subWindowClose')](#ZH-CN_TOPIC_0000002522080752__onsubwindowclose12)方法。主窗口的同步关闭事件监听参考[on('windowStageClose')](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__onwindowstageclose14)方法。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowWillClose'，即窗口关闭事件。 |
| callback | Callback<void, Promise<boolean>> | 是 | 回调函数。当点击窗口系统提供的右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑需要有Promise<boolean>类型的返回值。在返回的Promise函数里，执行resolve(true) 方法表示不关闭当前窗口，执行resolve(false) 方法或者reject方法均表示关闭当前窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    const callback = () => {
      // ...
      return new Promise<boolean>((resolve, reject) => {
        // 是否关闭该窗口
        let result: boolean = true;
        resolve(result);
      });
    }
    try {
      let windowClass = windowStage.getMainWindowSync();
      windowClass.on('windowWillClose', callback);
    } catch (exception) {
      console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### off('windowWillClose')15+

off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void

用于关闭主窗口或子窗口关闭事件的监听。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowWillClose'，即窗口关闭事件。 |
| callback | Callback<void, Promise<boolean>> | 否 | 回调函数。当点击窗口系统提供的右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑需要有Promise<boolean>类型的返回值。在返回的Promise函数里，执行resolve(true) 方法表示不关闭当前窗口，执行resolve(false) 方法或者reject方法均表示关闭当前窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      const callback = () => {
        // ...
        return new Promise<boolean>((resolve, reject) => {
          // 是否关闭该窗口
          let result: boolean = true;
          resolve(result);
        });
      }
      let windowClass = windowStage.getMainWindowSync();
      windowClass.on('windowWillClose', callback);
      windowClass.off('windowWillClose', callback);
      // 如果通过on开启多个callback进行监听，同时关闭所有监听：
      windowClass.off('windowWillClose');
    } catch (exception) {
      console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### on('windowHighlightChange')15+

on(type: 'windowHighlightChange', callback: Callback<boolean>): void

开启窗口激活态变化事件的监听。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowHighlightChange'，即窗口激活态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。当本窗口的激活态发生变化时的回调。回调函数返回boolean类型参数。当返回参数为true表示激活态；false表示非激活态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  windowClass.on('windowHighlightChange', (data: boolean) => {
    console.info(`Window highlight Change: ${data}`);
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('windowHighlightChange')15+

off(type: 'windowHighlightChange', callback?: Callback<boolean>): void

关闭窗口激活态变化事件的监听。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowHighlightChange'，即窗口激活态变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数。当本窗口的激活态发生变化时的回调。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口激活态变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (data: boolean) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('windowHighlightChange', callback);
  // 关闭指定callback的监听
  windowClass.off('windowHighlightChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('windowHighlightChange');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('rotationChange')19+

on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void

开启窗口旋转变化的监听。[RotationChangeInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__rotationchangeinfo19)中窗口旋转事件类型为窗口即将旋转时，必须返回[RotationChangeResult](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__rotationchangeresult19)。窗口旋转事件类型为窗口旋转结束时返回[RotationChangeResult](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__rotationchangeresult19)不生效。

该函数只允许在主线程注册。同一个窗口多次注册同类型回调函数，只生效最新注册的同类型回调函数返回值。系统提供了超时保护机制，若20ms内窗口未返回[RotationChangeResult](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__rotationchangeresult19)，系统不处理该返回值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 该接口在2in1设备上调用会返回801错误码，在非2in1且支持sensor旋转但不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在非2in1且支持sensor旋转，支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在非2in1且支持sensor旋转，支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错，切换到非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下生效；在其他情况的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rotationChange'，即窗口旋转变化事件。 |
| callback | RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void> | 是 | 回调函数。返回窗口旋转信息RotationChangeInfo，应用返回当前窗口变化结果RotationChangeResult。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
function calculateRect(info: window.RotationChangeInfo): window.Rect {
    // calculate result with info
    let rect : window.Rect = {
      left: 0,
      top: 0,
      width: 500,
      height: 600,
    }
    return rect;
}

const callback = (info: window.RotationChangeInfo): window.RotationChangeResult | void => {
  let result: window.RotationChangeResult = {
    rectType: window.RectType.RELATIVE_TO_SCREEN,
    windowRect: {
      left: 0,
      top: 0,
      width: 0,
      height: 0,
    }
  };
  if (info.type === window.RotationChangeType.WINDOW_WILL_ROTATE) {
      result.rectType = window.RectType.RELATIVE_TO_SCREEN;
      result.windowRect = calculateRect(info);
      return result;
  } else {
      // do something after rotate
      return;
  }

try {
  windowClass.on('rotationChange', callback);
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('rotationChange')19+

off(type: 'rotationChange', callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void

关闭窗口旋转变化的监听。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 该接口在2in1设备上调用会返回801错误码，在非2in1且支持sensor旋转但不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在非2in1且支持sensor旋转，支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用且立即生效；在非2in1且支持sensor旋转，支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错，切换到非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下生效；在其他情况的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rotationChange'，即窗口旋转变化事件。 |
| callback | RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void> | 否 | 回调函数。如果传入参数，则关闭该监听。如果未传入参数，则关闭该窗口的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (info: window.RotationChangeInfo): window.RotationChangeResult | void => {
  // ...
  return;
}
try {
  windowClass.off('rotationChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听。
  windowClass.off('rotationChange');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('uiExtensionSecureLimitChange')20+

on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void

开启窗口内uiExtension安全限制变化事件的监听, 建议在窗口创建后立即监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'uiExtensionSecureLimitChange'，即窗口内uiExtension安全限制变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。当窗口内uiExtension安全限制变化时触发回调。当返回参数为true表示窗口内uiExtension开启了隐藏不安全窗口；当返回参数为false表示窗口内uiExtension关闭了隐藏不安全窗口。若窗口内存在多个uiExtension，当返回参数为true表示窗口内至少一个uiExtension开启了隐藏不安全窗口；当返回参数为false表示窗口内所有uiExtension关闭了隐藏不安全窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.Function on('uiExtensionSecureLimitChange') can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  windowClass.on('uiExtensionSecureLimitChange', (data: boolean) => {
    console.info(`Window secure limit Change: ${data}`);
  });
} catch (exception) {
  console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('uiExtensionSecureLimitChange')20+

off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void

关闭窗口内uiextension安全限制变化事件的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'uiExtensionSecureLimitChange'，即窗口内uiExtension安全限制变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口安全限制变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.Function off('uiExtensionSecureLimitChange') can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (data: boolean) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('uiExtensionSecureLimitChange', callback);
  // 关闭指定callback的监听
  windowClass.off('uiExtensionSecureLimitChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  windowClass.off('uiExtensionSecureLimitChange');
} catch (exception) {
  console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### isWindowSupportWideGamut9+

isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void

判断当前窗口是否支持广色域模式，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.isWindowSupportWideGamut((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in checking whether the window support WideGamut Data: ${data}`);
});
```

#### isWindowSupportWideGamut9+

isWindowSupportWideGamut(): Promise<boolean>

判断当前窗口是否支持广色域模式，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.isWindowSupportWideGamut();
promise.then((data) => {
  console.info(`Succeeded in checking whether the window support WideGamut. Data: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setWindow[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)9+

setWindow[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(colorSpace:ColorSpace, callback: AsyncCallback<void>): void

设置当前窗口为广色域模式或默认色域模式，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8) | 是 | 设置色域模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.setWindowColorSpace(window.ColorSpace.WIDE_GAMUT, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in setting window colorspace.');
  });
} catch (exception) {
  console.error(`Failed to set window colorspace. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindow[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)9+

setWindow[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(colorSpace:ColorSpace): Promise<void>

设置当前窗口为广色域模式或默认色域模式，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8) | 是 | 设置色域模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.setWindowColorSpace(window.ColorSpace.WIDE_GAMUT);
  promise.then(() => {
    console.info('Succeeded in setting window colorspace.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set window colorspace. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindow[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)9+

getWindow[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(): ColorSpace

获取当前窗口色域模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8) | 当前色域模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let colorSpace = windowClass.getWindowColorSpace();
  console.info(`Succeeded in getting the window color space. ColorSpace: ${colorSpace}`);
} catch (exception) {
  console.error(`Failed to get the window color space. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowBackgroundColor9+

setWindowBackgroundColor(color: string | [ColorMetrics](../../topics/misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)): void

设置窗口的背景色。

未调用该接口时，窗口在浅色模式默认背景色为'#FFF0F0F0'，在深色模式默认背景色为'#FF1A1A1A'。

Stage模型下，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | string | [ColorMetrics](../../topics/misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)18+ | 是 | 需要设置的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 从API version 18开始，此参数支持ColorMetrics类型。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics } from '@kit.ArkUI';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in loading the content.');
  let color1: string = '#00FF33';
  let color2: ColorMetrics = ColorMetrics.numeric(0xff112233);
  try {
    windowClass?.setWindowBackgroundColor(color1);
    windowClass?.setWindowBackgroundColor(color2);
  } catch (exception) {
    console.error(`Failed to set the background color. Cause code: ${exception.code}, message: ${exception.message}`);
  };
});
```

#### setWindowShadowEnabled20+

setWindowShadowEnabled(enable: boolean): Promise<void>

设置主窗口是否显示阴影，使用Promise异步回调。未调用该接口时，主窗口默认显示阴影。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码；从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在2in1和Tablet设备中可正常调用，在Tablet设备时仅在开启[自由多窗模式](../../guides/窗口开发术语.md#自由多窗模式)下生效，在其他设备中返回801错误码。

**需要权限：** ohos.permission.SET_WINDOW_TRANSPARENT

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置主窗口是否显示阴影。true表示显示阴影，false表示不显示阴影。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in loading the content.');
      // 获取应用主窗口。
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        let enable = true;
        let promise = windowClass.setWindowShadowEnabled(enable);
        promise.then(() => {
          console.info('Succeeded in setting window shadow.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the window shadow. Cause code: ${err.code}, message: ${err.message}`);
        });
}
```

#### setWindowBrightness9+

setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void

主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。使用callback异步回调。

窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。

当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。

当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议连续调用或窗口退至后台时调用此接口，否则可能产生时序问题。


- 针对非2in1设备：

  - 在HarmonyOS开发套件（基于API 23）配套的系统版本之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。

  - 从HarmonyOS开发套件（基于API 23）配套的系统版本开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。

- 针对2in1设备：

  - 在HarmonyOS5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。
  - 从HarmonyOS5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
      if (loadError.code) {
        console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
        return;
      }
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let brightness: number = 1.0;
      try {
        windowClass.setWindowBrightness(brightness, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('Succeeded in setting the brightness.');
        });
      } catch (exception) {
        console.error(`Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setWindowBrightness9+

setWindowBrightness(brightness: number): Promise<void>

主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。使用Promise异步回调。

窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。

当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。

当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议连续调用或窗口退至后台时调用此接口，否则可能产生时序问题。


- 针对非2in1设备：

  - 在HarmonyOS开发套件（基于API 23）配套的系统版本之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。

  - 从HarmonyOS开发套件（基于API 23）配套的系统版本开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。

- 针对2in1设备：

  - 在HarmonyOS5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。
  - 从HarmonyOS5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
      if (loadError.code) {
        console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
        return;
      }
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let brightness: number = 1.0;
      try {
        let promise = windowClass.setWindowBrightness(brightness);
        promise.then(() => {
          console.info('Succeeded in setting the brightness.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setWindowFocusable9+

setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void

设置窗口是否具有获得焦点的能力，使用callback异步回调。

从API version 22开始，调用[createVirtualScreen](@ohos.display (屏幕属性).md#ZH-CN_TOPIC_0000002522240754__displaycreatevirtualscreen16)接口创建虚拟屏，并设置supportsFocus配置项为false时，位于该虚拟屏的窗口无法调用该接口修改窗口的可获焦能力，如果调用，会抛出1300002错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 窗口是否可获焦。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考不可获焦窗口中输入框与输入法交互指南。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
try {
  windowClass.setWindowFocusable(isFocusable, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in setting the window to be focusable.');
  });
} catch (exception) {
  console.error(`Failed to set the window to be focusable. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowFocusable9+

setWindowFocusable(isFocusable: boolean): Promise<void>

设置窗口是否具有获得焦点的能力，使用Promise异步回调。

从API version 22开始，调用[createVirtualScreen](@ohos.display (屏幕属性).md#ZH-CN_TOPIC_0000002522240754__displaycreatevirtualscreen16)接口创建虚拟屏，并设置supportsFocus配置项为false时，位于该虚拟屏的窗口无法调用该接口修改窗口的可获焦能力，如果调用，会抛出1300002错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 窗口是否可获焦。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考不可获焦窗口中输入框与输入法交互指南。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
try {
  let promise = windowClass.setWindowFocusable(isFocusable);
  promise.then(() => {
    console.info('Succeeded in setting the window to be focusable.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the window to be focusable. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowKeepScreenOn9+

setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void

设置屏幕是否为常亮状态，使用callback异步回调。

规范使用该接口：仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
try {
  windowClass.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in setting the screen to be always on.');
  });
} catch (exception) {
  console.error(`Failed to set the screen to be always on. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowKeepScreenOn9+

setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

设置屏幕是否为常亮状态，使用Promise异步回调。

规范使用该接口：仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
try {
  let promise = windowClass.setWindowKeepScreenOn(isKeepScreenOn);
  promise.then(() => {
    console.info('Succeeded in setting the screen to be always on.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the screen to be always on. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowPrivacyMode9+

setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

设置窗口是否为隐私模式，使用callback异步回调。

设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。

隐私模式窗口退后台后在多任务卡片中显示为白色蒙层或隐私蒙层。

未调用此接口时，窗口默认不开启隐私模式，可以被截屏或录屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.PRIVACY_WINDOW

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示为隐私模式，false表示为非隐私模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Possible cause: Need ohos.permission.PRIVACY_WINDOW permission. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
try {
  windowClass.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in setting the window to privacy mode.');
  });
} catch (exception) {
  console.error(`Failed to set the window to privacy mode. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowPrivacyMode9+

setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>

设置窗口是否为隐私模式，使用Promise异步回调。

设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。

隐私模式窗口退后台后在多任务卡片中显示为白色蒙层或隐私蒙层。

未调用此接口时，窗口默认不开启隐私模式，可以被截屏或录屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.PRIVACY_WINDOW

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示为隐私模式，false表示为非隐私模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Possible cause: Need ohos.permission.PRIVACY_WINDOW permission. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
try {
  let promise = windowClass.setWindowPrivacyMode(isPrivacyMode);
  promise.then(() => {
    console.info('Succeeded in setting the window to privacy mode.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the window to privacy mode. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowTouchable9+

setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void

设置窗口是否为可触状态，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可触状态。true表示可触；false表示不可触。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable = true;
try {
  windowClass.setWindowTouchable(isTouchable, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in setting the window to be touchable.');
  });
} catch (exception) {
  console.error(`Failed to set the window to be touchable. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowTouchable9+

setWindowTouchable(isTouchable: boolean): Promise<void>

设置窗口是否为可触状态，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可触状态。true表示可触；false表示不可触。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable: boolean = true;
try {
  let promise = windowClass.setWindowTouchable(isTouchable);
  promise.then(() => {
    console.info('Succeeded in setting the window to be touchable.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the window to be touchable. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### snapshot9+

snapshot(callback: AsyncCallback<image.PixelMap>): void

获取窗口截图，使用callback异步回调。若当前窗口设置为隐私模式（可通过[setWindowPrivacyMode](#ZH-CN_TOPIC_0000002522080752__setwindowprivacymode9)接口设置），截图结果为白屏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<image.PixelMap> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Get pixelMap failed; 3. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

windowClass.snapshot((err: BusinessError, pixelMap: image.PixelMap) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
  pixelMap.release(); // PixelMap使用完后及时释放内存
});
```

#### snapshot9+

snapshot(): Promise<image.PixelMap>

获取当前窗口截图。若当前窗口设置为隐私模式（可通过[setWindowPrivacyMode](#ZH-CN_TOPIC_0000002522080752__setwindowprivacymode9)接口设置），截图结果为白屏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | Promise对象。返回当前窗口截图。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Get pixelMap failed; 3. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let promise = windowClass.snapshot();
promise.then((pixelMap: image.PixelMap) => {
  console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
  pixelMap.release(); // PixelMap使用完后及时释放内存
}).catch((err: BusinessError) => {
  console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### snapshotSync20+

snapshotSync(): image.PixelMap

获取当前窗口截图，此接口为同步接口。若当前窗口设置为隐私模式（[setWindowPrivacyMode](#ZH-CN_TOPIC_0000002522080752__setwindowprivacymode9)接口设置），截图结果为白屏。

Stage模型下，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | 返回当前窗口截图。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Create pixelMap failed. |
| 1300018 | Timeout. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

try {
  let pixelMap = windowClass.snapshotSync();
  console.info(`Succeeded in snapshotting window`);
  pixelMap.release(); // PixelMap使用完后及时释放内存
} catch (exception) {
  console.error(`Failed to snapshot window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### snapshotIgnorePrivacy18+

snapshotIgnorePrivacy(): Promise<image.PixelMap>

获取当前窗口截图。即使当前窗口设置为隐私模式（可通过[setWindowPrivacyMode](#ZH-CN_TOPIC_0000002522080752__setwindowprivacymode9)接口设置），仍可调用本接口返回当前窗口截图。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | Promise对象。返回当前窗口截图。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function snapshotIgnorePrivacy can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Create pixelMap failed; 3. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let promise = windowClass.snapshotIgnorePrivacy();
promise.then((pixelMap: image.PixelMap) => {
  console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
  pixelMap.release(); // PixelMap使用完后及时释放内存
}).catch((err: BusinessError) => {
  console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setAspectRatio10+

setAspectRatio(ratio: number): Promise<void>

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用Promise异步回调。

-

通过其他接口如[resize](#ZH-CN_TOPIC_0000002522080752__resize9)、[resizeAsync](#ZH-CN_TOPIC_0000002522080752__resizeasync12)设置窗口大小时，不受ratio约束。

-

仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).FLOATING）下生效。此比例参数将持久化保存，关闭应用或重启设备后，切换到自由悬浮窗口模式时，设置的比例仍然生效。

-

当同一应用的某个主窗口调用此接口设置宽高比生效后，后续打开的主窗口均会沿用该宽高比。若需为单个主窗口单独设置宽高比，请使用[setContentAspectRatio](#ZH-CN_TOPIC_0000002522080752__setcontentaspectratio21)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | number | 是 | 窗口内容布局（不含边框和标题栏等装饰）的宽高比。该参数为浮点数，受窗口最大最小尺寸限制，比例值下限为最小宽度/最大高度，上限为最大宽度/最小高度。窗口最大最小尺寸由WindowLimits和系统限制的交集决定，系统限制优先级高于WindowLimits。ratio的有效范围会随WindowLimits变化而变化。如果先设置了WindowLimits，后设置的ratio与其冲突，会返回错误码；如果先设置了ratio，后设置的WindowLimits与其冲突，窗口的宽高比可能会不跟随设置的宽高比（ratio）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: Invalid parameter range. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
    if (!windowClass) {
      console.info('windowClass is null');
    }
    try {
      let ratio = 1.0;
      let promise = windowClass.setAspectRatio(ratio);
      promise.then(() => {
        console.info('Succeeded in setting aspect ratio of window.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setAspectRatio10+

setAspectRatio(ratio: number, callback: AsyncCallback<void>): void

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用callback异步回调。

-

通过其他接口如[resize](#ZH-CN_TOPIC_0000002522080752__resize9)、[resizeAsync](#ZH-CN_TOPIC_0000002522080752__resizeasync12)设置窗口大小时，不受ratio约束。

-

仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).FLOATING）下生效。此比例参数将持久化保存，关闭应用或重启设备后，切换到自由悬浮窗口模式时，设置的比例仍然生效。

-

当同一应用的某个主窗口调用此接口设置宽高比生效后，后续打开的主窗口均会沿用该宽高比。若需为单个主窗口单独设置宽高比，请使用[setContentAspectRatio](#ZH-CN_TOPIC_0000002522080752__setcontentaspectratio21)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | number | 是 | 窗口内容布局（不含边框和标题栏等装饰）的宽高比。该参数为浮点数，受窗口最大最小尺寸限制，比例值下限为最小宽度/最大高度，上限为最大宽度/最小高度。窗口最大最小尺寸由WindowLimits和系统限制的交集决定，系统限制优先级高于WindowLimits。ratio的有效范围会随WindowLimits变化而变化。如果先设置了WindowLimits，后设置的ratio与其冲突，会返回错误码；如果先设置了ratio，后设置的WindowLimits与其冲突，窗口的宽高比可能会不跟随设置的宽高比（ratio）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: Invalid parameter range. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
    if (!windowClass) {
      console.info('Failed to load the content. Cause: windowClass is null');
    }
    try {
      let ratio = 1.0;
      windowClass.setAspectRatio(ratio, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in setting the aspect ratio of window.');
      });
    } catch (exception) {
      console.error(`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setContentAspectRatio21+

setContentAspectRatio(ratio: number, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用Promise异步回调。

-

根据相同的ratio参数调整窗口宽高时，窗口宽高会跟随窗口边框装饰尺寸或可见性变化而调整。

-

通过[setWindowDecorVisible](#ZH-CN_TOPIC_0000002522080752__setwindowdecorvisible11)将窗口标题栏设置为不可见时，窗口内容区域将占据原本标题栏的高度空间。

-

通过其他接口如[resize](#ZH-CN_TOPIC_0000002522080752__resize9)、[resizeAsync](#ZH-CN_TOPIC_0000002522080752__resizeasync12)设置窗口大小时，不受ratio约束。

-

仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).FLOATING）下生效。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | number | 是 | 窗口内容布局（不含边框和标题栏等装饰）的宽高比。该参数为浮点数，受窗口最大最小尺寸限制，比例值下限为最小宽度/最大高度，上限为最大宽度/最小高度。窗口最大最小尺寸由WindowLimits和系统限制的交集决定，系统限制优先级高于WindowLimits。ratio的有效范围会随WindowLimits变化而变化。如果先设置了WindowLimits，后设置的ratio与其冲突，会返回错误码；如果先设置了ratio，后设置的WindowLimits与其冲突，窗口的宽高比可能会不跟随设置的宽高比（ratio）。 |
| isPersistent | boolean | 否 | 是否持久化保存该比例参数。 如为true，比例参数会持久化保存，销毁窗口、关闭应用或重启设备后，当再次切换到自由悬浮窗口模式时仍然生效。可通过resetAspectRatio清除持久化保存的比例参数。 如为false，比例参数仅对当前窗口生效，窗口销毁后清除该数据。 默认值为true。 |
| needUpdateRect | boolean | 否 | 是否立即根据当前比例更新窗口大小。 如为true，立即根据当前比例更新窗口大小。 如为false，窗口将在拖拽缩放时根据当前比例更新，也可以使用resize或resizeAsync进行主动更新。 默认值为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. 2. Invalid parameter length. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      let windowClass = windowStage.getMainWindowSync();
      let ratio = 1.0;
      let promise = windowClass.setContentAspectRatio(ratio, true, true);
      promise.then(() => {
        console.info('Succeeded in setting aspect ratio of window.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### resetAspectRatio10+

resetAspectRatio(): Promise<void>

取消设置窗口内容布局的比例，使用Promise异步回调。

仅主窗可设置，调用后将清除持久化储存的比例信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
    if (!windowClass) {
      console.info('Failed to load the content. Cause: windowClass is null');
    }
    try {
      let promise = windowClass.resetAspectRatio();
      promise.then(() => {
        console.info('Succeeded in resetting aspect ratio of window.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to reset the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to reset the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### resetAspectRatio10+

resetAspectRatio(callback: AsyncCallback<void>): void

取消设置窗口内容布局的比例，使用callback异步回调。

仅主窗可设置，调用后将清除持久化储存的比例信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
    if (!windowClass) {
      console.info('Failed to load the content. Cause: windowClass is null');
    }
    try {
      windowClass.resetAspectRatio((err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to reset the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in resetting aspect ratio of window.');
      });
    } catch (exception) {
      console.error(`Failed to reset the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### minimize11+

minimize(callback: AsyncCallback<void>): void

此接口根据调用对象不同，实现不同的功能：

-

当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原，2in1 设备上可以使用[restore()](#ZH-CN_TOPIC_0000002522080752__restore14)进行还原。

-

当调用对象为子窗口或全局悬浮窗时，实现隐藏功能，不可在Dock栏中还原，可以使用[showWindow()](#ZH-CN_TOPIC_0000002522080752__showwindow9)进行还原。

该接口仅支持主窗口、子窗口或全局悬浮窗，其它窗口调用返回1300002错误码，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error; 3.Invalid window type. Only main windows, subwindows, and float windows are supported. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.minimize((err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to minimize the window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in minimizing the window.');
});
```

#### minimize11+

minimize(): Promise<void>

此接口根据调用对象不同，实现不同的功能：

-

当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原，2in1 设备上可以使用[restore()](#ZH-CN_TOPIC_0000002522080752__restore14)进行还原。

-

当调用对象为子窗口或全局悬浮窗时，实现隐藏功能，不可在Dock栏中还原，可以使用[showWindow()](#ZH-CN_TOPIC_0000002522080752__showwindow9)进行还原。

该接口仅支持主窗口、子窗口或全局悬浮窗，其它窗口调用返回1300002错误码，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error; 3.Invalid window type. Only main windows, subwindows, and float windows are supported. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.minimize();
promise.then(() => {
  console.info('Succeeded in minimizing the window.');
}).catch((err: BusinessError) => {
  console.error(`Failed to minimize the window. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### maximize12+

maximize(presentation?: [MaximizePresentation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__maximizepresentation12)): Promise<void>

实现最大化功能。主窗口可调用此接口实现最大化功能；子窗口需在创建时设置子窗口参数maximizeSupported为true，再调用此接口可实现最大化功能。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| presentation | [MaximizePresentation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__maximizepresentation12) | 否 | 主窗口或子窗口最大化时的布局枚举。默认值window.MaximizePresentation.ENTER_IMMERSIVE，即默认最大化时进入全屏模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function maximize can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and maximizable subwindows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let promise = windowClass.maximize();
      // let promise = windowClass.maximize(window.MaximizePresentation.ENTER_IMMERSIVE);
      promise.then(() => {
        console.info('Succeeded in maximizing the window.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}`);
      });
  }
};
```

#### maximize22+

maximize(presentation?: [MaximizePresentation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__maximizepresentation12), acrossDisplay?: boolean): Promise<void>

实现最大化功能。主窗口可调用此接口实现最大化功能；子窗口需在创建时设置子窗口参数maximizeSupported为true，再调用此接口可实现最大化功能。在具备折叠功能的2in1设备上，支持控制悬停态（参考[折叠屏悬停态最佳实践](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-folded-hover)）下主窗口的瀑布流模式行为，即窗口在悬停态下最大化时是否跨上下两个半屏显示。使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| presentation | [MaximizePresentation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__maximizepresentation12) | 否 | 主窗口或子窗口最大化时的布局枚举。默认值window.MaximizePresentation.ENTER_IMMERSIVE，即默认最大化时进入全屏模式。 |
| acrossDisplay | boolean | 否 | 控制悬停态下主窗口在最大化时的瀑布流模式行为。仅主窗口可设置此参数，非主窗口调用时返回错误码1300004。 取值为true时： - 悬停态下，窗口将直接进入瀑布流模式； - 展开态下，窗口进入最大化，并在悬停态下保持瀑布流模式。 取值为false时： - 悬停态下，窗口将退出瀑布流模式，进入单面最大化（即窗口最大化时只在上半屏或下半屏显示）； - 展开态下，窗口进入最大化，并在悬停态下退出瀑布流模式。 取值为undefined或不传值时，不修改窗口瀑布流模式行为： - 悬停态下，窗口进入单面最大化； - 展开态下，窗口进入最大化，并在悬停态下默认保持瀑布流模式。 设备行为差异： 仅在具备折叠功能的2in1设备可正常调用；在其他设备上调用不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function maximize can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and maximizable subwindows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      let mainWindow = windowStage.getMainWindowSync();
      mainWindow.maximize(window.MaximizePresentation.ENTER_IMMERSIVE, true)
        .then(() => {
          console.info('Window maximized successfully.');
        })
        .catch((err: BusinessError) => {
          console.error(`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}`);
        });
  }
};
```

#### setResizeByDragEnabled14+

setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void

禁止/使能通过拖拽方式缩放主窗口或启用装饰的子窗口的功能。使用callback异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置窗口是否使能通过拖拽进行缩放，true表示使能，false表示禁止。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  let enabled = false;
  windowClass.setResizeByDragEnabled(enabled, (err) => {
    if (err.code) {
      console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in setting the function of disabling the resize by drag window.`);
  });
} catch (exception) {
  console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setResizeByDragEnabled14+

setResizeByDragEnabled(enable: boolean): Promise<void>

禁止/使能通过拖拽方式缩放主窗口或启用装饰的子窗口的功能。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置窗口是否使能通过拖拽进行缩放，true表示使能，false表示禁止。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let enabled = false;
  let promise = windowClass.setResizeByDragEnabled(enabled);
  promise.then(() => {
    console.info(`Succeeded in setting the function of disabling the resize by drag window.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### recover11+

recover(): Promise<void>

将主窗口从全屏、最大化、分屏模式下还原为自由悬浮窗口模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).FLOATING），并恢复到进入该模式之前的大小和位置，已经是自由悬浮窗口模式不可再还原。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let windowClass = windowStage.getMainWindowSync();
      if (!windowClass) {
        console.error('Failed to get main window.');
        return;
      }
      let promise = windowClass.recover();
      promise.then(() => {
        console.info('Succeeded in recovering the window.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to recover the window. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to recover the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### restore14+

restore(): Promise<void>

主窗口为最小化状态且UIAbility生命周期为onForeground时，将主窗口从最小化状态，恢复到前台显示，并恢复到进入最小化状态之前的大小和位置。主窗口为前台状态时，仅抬升主窗口层级。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      let windowClass = windowStage.getMainWindowSync();
      // 调用minimize, 使主窗最小化
      windowClass.minimize();
      //设置延时函数延时5秒钟后对主窗进行恢复。
      setTimeout(()=>{
        //调用restore()函数对主窗进行恢复。
        let promise = windowClass.restore();
        promise.then(() => {
          console.info('Succeeded in restoring the window.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to restore the window. Cause code: ${err.code}, message: ${err.message}`);
        });
      }, 5000);
    } catch (exception) {
      console.error(`Failed to restore the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

**restoreMainWindow23+**

restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>

将当前窗口的主窗口恢复到前台显示，如果主窗口已处于前台，则会抬升主窗层级。此接口仅适用于类型为[TYPE_FLOAT](Enums.md#ZH-CN_TOPIC_0000002553200717__windowtype7)的窗口，并且需在窗口触发过[DOWN](枚举说明.md#ZH-CN_TOPIC_0000002553200889__touchtype)事件后才能调用。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Window.SessionManager

设备行为差异： 该接口在Phone设备、Tablet设备和2in1设备上可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParameters | Record<string, Object> | 否 | 拉起窗口时会给主窗传递的自定义参数，主窗会在触发onNewWant回调时收到。默认值为空，代表不向主窗传入任何自定义参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: 1. The window is not float window. 2. The window is not at foreground or has never been clicked. 3. The window cannot find main window. |
| 1300007 | Restore parent main window failed. Possible cause: 1. The main window is at PAUSED lifecycle state. 2. The main window is in background during recent. |

示例：

```ets
// Float.ets
import { window } from '@kit.ArkUI'
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';

@Entry
@Component
struct Float {
  build() {
    Button('CreateFloatWindow').onClick(() => {
      this.createFloatWindow();
    })
  }

  private createFloatWindow() {
    let windowClass: window.Window | undefined = undefined;
    let config: window.Configuration = {
      name: 'testFloatWindow',
      title: 'floatWindow',
      windowType: window.WindowType.TYPE_FLOAT,
      ctx: this.getUIContext()?.getHostContext(),
      decorEnabled: true,
    };
    try {
      window.createWindow(config, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        console.info(`succedded in creating the window. Data: ${JSON.stringify(data)}`);
        windowClass.resize(500, 1600).then(() => {
          console.info('Succeeded in changing the window size.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
        });
        windowClass.setUIContent("pages/FloatWindowInfo").then(() => {
          console.info('Succeeded in loading the content.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
        });
        windowClass.showWindow().then(() => {
          console.info("showWindow success");
        }).catch((err: BusinessError) => {
          console.error(`showWindow err: ${JSON.stringify(err)}`);
        });
        windowClass.moveWindowToAsync(20, 200).then(() => {
          console.info('Succeeded in moving the window.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
        });
    } catch (exception) {
      console.error(`failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

```ets
// FloatWindowInfo.ets
import { window } from '@kit.ArkUI'
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct FloatWindowInfo {
  @State subWindow: window.Window | undefined = undefined;
  @State windowId: number = -1;
  async aboutToAppear(): Promise<void> {
    this.subWindow = window.findWindow('testFloatWindow');
    this.windowId = this.subWindow?.getWindowProperties()?.id;
  }

  build() {
    Column() {
      Text('Hello')
    }
    .width('100%')
    .height('100%')
    .onTouch((event: TouchEvent) => {
      // 保证有Down事件产生，实际调用时机可由开发者决定
      if (event.type === TouchType.Down) {
        let param: Record<string, Object> = {
          "info": "helloworld",
        };
        try {
          let promise = this.subWindow?.restoreMainWindow(param);
          promise?.then(() => {
            console.info('Succeeded in restoring the main window.');
          }).catch((err: BusinessError) => {
            console.error(`Failed to restore the main window. Cause code: ${err.code}, message: ${err.message}`);
          });
        } catch (exception) {
          console.error(`Failed to restore the main window. Cause code: ${exception.code}, message: ${exception.message}`);
        }
    })
}
```

#### getWindowLimits11+

getWindowLimits(): WindowLimits

获取当前应用窗口的尺寸限制，单位为物理像素px。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WindowLimits | 当前窗口尺寸限制。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
try {
  let windowLimits = windowClass.getWindowLimits();
} catch (exception) {
  console.error(`Failed to obtain the window limits of window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindowLimitsVP22+

getWindowLimitsVP(): WindowLimits

获取当前应用窗口的尺寸限制，单位为虚拟像素vp。

对于系统窗口和全局悬浮窗，默认窗口宽高的系统限制最小值为1px，通过此接口获取到的1vp，是计算取整后的值。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WindowLimits | 当前窗口尺寸限制。 |

**错误码：**

错误码详情请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
try {
  let windowLimits: window.WindowLimits = windowClass.getWindowLimitsVP();
} catch (exception) {
  console.error(`Failed to obtain the window limits. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowLimits11+

setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>

设置当前窗口的尺寸限制，使用Promise异步回调。

默认存在一个系统尺寸限制，系统尺寸限制由产品配置决定，不可修改。

未调用setWindowLimits配置过WindowLimits时，使用[getWindowLimits](#ZH-CN_TOPIC_0000002522080752__getwindowlimits11)或[getWindowLimitsVP](#ZH-CN_TOPIC_0000002522080752__getwindowlimitsvp22)可获取系统限制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowLimits | WindowLimits | 是 | 目标窗口的尺寸限制，单位为px或vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<WindowLimits> | Promise对象。返回设置后的尺寸限制，为入参与系统尺寸限制的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let windowLimits: window.WindowLimits = {
    maxWidth: 1500,
    maxHeight: 1000,
    minWidth: 500,
    minHeight: 400
  };
  let promise = windowClass.setWindowLimits(windowLimits);
    promise.then((data) => {
    console.info('Succeeded in changing the window limits. Cause:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to change the window limits. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to change the window limits. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowLimits15+

setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>

设置当前窗口的尺寸限制，使用Promise异步回调。

默认存在一个系统尺寸限制，系统尺寸限制由产品配置决定，不可修改。

未调用setWindowLimits配置过WindowLimits时，使用[getWindowLimits](#ZH-CN_TOPIC_0000002522080752__getwindowlimits11)或[getWindowLimitsVP](#ZH-CN_TOPIC_0000002522080752__getwindowlimitsvp22)可获取系统限制。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 5.1.1之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.1开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备调用返回801错误码。主窗在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowLimits | WindowLimits | 是 | 目标窗口的尺寸限制，单位为px或vp。 |
| isForcible | boolean | 是 | 是否强制设置窗口的尺寸限制。 入参windowLimits的单位为vp时：无论设置true还是false，都按照false处理，窗口宽高的最小值和最大值都取决于系统限制。 入参windowLimits的单位为px时：设置为true，表示窗口宽高最小值以系统限制值和40vp两者中的低数值为准，窗口宽高的最大值仍取决于系统限制；设置为false，表示窗口宽高的最小值和最大值都取决于系统限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<WindowLimits> | Promise对象。返回设置后的窗口尺寸限制。 入参windowLimits的单位为vp时，返回入参与系统默认窗口尺寸限制的交集。 入参windowLimits的单位为px时，isForcible为false则返回入参与系统默认窗口尺寸限制的交集；isForcible为true则返回入参与[系统限制的最小值与40vp两者中的低数值，系统限制的最大值]的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let windowLimits: window.WindowLimits = {
    maxWidth: 1500,
    maxHeight: 1000,
    minWidth: 100,
    minHeight: 100
  };
  let promise = windowClass.setWindowLimits(windowLimits, true);
  promise.then((data) => {
    console.info(`Succeeded in changing the window limits. Cause: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to change the window limits. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to change the window limits. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowMask12+

setWindowMask(windowMask: Array<Array<number>>): Promise<void>;

设置异形窗口的掩码，使用Promise异步回调。异形窗口为非常规形状的窗口，掩码用于描述异形窗口的形状。此接口仅限子窗和全局悬浮窗可用。

当异形窗口大小发生变化时，实际的显示内容为掩码大小和窗口大小的交集部分。

该接口只在多个线程操作同一个窗口时可能返回错误码1300002。窗口被销毁场景下错误码返回[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowMask | Array<Array<number>> | 是 | 异形窗口的掩码，该参数仅支持宽高为窗口宽高、取值为整数0和整数1的二维数组输入，整数0代表所在像素透明，整数1代表所在像素不透明，宽高不符合的二维数组或二维数组取值不为整数0和整数1的二维数组为非法参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and float windows are supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let maskWidth = windowClass.getWindowProperties().windowRect.width;
  let maskHeight = windowClass.getWindowProperties().windowRect.height;
  let windowMask = Array<Array<number>>(maskHeight).fill([]).map((_, row) => {
    let array = Array<number>(maskWidth);
    for (let i = 0 ; i < maskWidth; i++) {
      array[i] = (i + row) > (maskWidth + maskHeight) / 2 ? 1 : 0;
    }
    return array;
  });
  let promise = windowClass.setWindowMask(windowMask);
    promise.then(() => {
    console.info('Succeeded in setting the window mask.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window mask. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the window mask. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### keepKeyboardOnFocus11+

keepKeyboardOnFocus(keepKeyboardFlag: boolean): void

窗口获焦时是否保留由其他窗口创建的软键盘，仅支持系统窗口与应用子窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keepKeyboardFlag | boolean | 是 | 是否保留其他窗口创建的软键盘。true表示保留；false表示不保留。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
try {
  windowClass.keepKeyboardOnFocus(true);
} catch (exception) {
  console.error(`Failed to keep keyboard onFocus. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowDecorVisible11+

setWindowDecorVisible(isVisible: boolean): void

设置窗口标题栏是否可见，对存在标题栏和三键区的窗口形态生效。Stage模型下，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

设置窗口标题栏不可见后，当主窗口进入全屏沉浸状态时，此时鼠标Hover到上方窗口标题栏热区上会显示悬浮标题栏。若想禁用悬浮标题栏显示，请使用[setTitleAndDockHoverShown()](#ZH-CN_TOPIC_0000002522080752__settitleanddockhovershown14)接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isVisible | boolean | 是 | 设置标题栏是否可见，true为可见，false为隐藏。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in loading the content.');
  let isVisible = false;
  // 调用setWindowDecorVisible接口
  try {
      windowClass?.setWindowDecorVisible(isVisible);
  } catch (exception) {
      console.error(`Failed to set the visibility of window decor. Cause code: ${exception.code}, message: ${exception.message}`);
  }
});
```

#### getWindowDecorVisible18+

getWindowDecorVisible(): boolean

查询窗口标题栏是否可见。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不报错，返回false。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前窗口标题栏是否可见，true表示可见，false表示不可见。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
let isVisible: boolean | undefined = undefined;
windowClass.setUIContent('pages/WindowPage').then(() => {
  try {
    isVisible = windowClass?.getWindowDecorVisible();
  } catch (exception) {
    console.error(`Failed to get the window decor visibility. Cause code: ${exception.code}, message: ${exception.message}`);
  }
})
```

#### setWindowTitle15+

setWindowTitle(titleName: string): Promise<void>

设置窗口标题，使用Promise异步回调。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回1300002或801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| titleName | string | 是 | 窗口标题。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let title = "title";
  windowClass.setWindowTitle(title).then(() => {
    console.info('Succeeded in setting the window title.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window title. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the window title. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowTitleMoveEnabled14+

setWindowTitleMoveEnabled(enabled: boolean): void

禁止/使能主窗或子窗标题栏默认移动窗口和双击最大化的功能，当禁用标题栏默认移动窗口和双击最大化的功能时，可使用[startMoving()](#ZH-CN_TOPIC_0000002522080752__startmoving14)在应用热区中发起拖拽移动，使用[maximize()](#ZH-CN_TOPIC_0000002522080752__maximize12)实现最大化功能。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否使能标题栏默认移动窗口和双击最大化功能，true表示使能，false表示不使能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      windowStage.loadContent("pages/Index").then(() =>{
        let windowClass = windowStage.getMainWindowSync();
        let enabled = false;
        windowClass.setWindowTitleMoveEnabled(enabled);
        console.info(`Succeeded in setting the the window title move enabled: ${enabled}`);
      });
    } catch (exception) {
      console.error(`Failed to set the window title move enabled. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setSubWindowModal12+

setSubWindowModal(isModal: boolean): Promise<void>

设置子窗的模态属性是否启用，使用Promise异步回调。

子窗口调用该接口时，设置子窗口模态属性是否启用。启用子窗口模态属性后，其父级窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态属性被禁用。

子窗口之外的窗口调用该接口时，会报错。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isModal | boolean | 是 | 设置子窗口模态属性是否启用，true为启用，false为不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    // 创建子窗
    try {
      let subWindow = windowStage.createSubWindow("testSubWindow");
      subWindow.then((data) => {
        if (data == null) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        windowClass = data;
        let promise = windowClass.setSubWindowModal(true);
        promise.then(() => {
          console.info('Succeeded in setting subwindow modal');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set subwindow modal. Cause code: ${err.code}, message: ${err.message}`);
        });
    } catch (exception) {
      console.error(`Failed to create the subWindow. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setSubWindowModal14+

setSubWindowModal(isModal: boolean, modalityType: [ModalityType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__modalitytype14)): Promise<void>

设置子窗的模态类型，使用Promise异步回调。

当子窗口模态类型为模窗口子窗时，其父级窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态类型被禁用。

当子窗口模态类型为模应用子窗时，其父级窗口与该应用其他实例的窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态类型被禁用。

此接口仅支持设置子窗口模态类型，当需要禁用子窗口模态属性时，建议使用[setSubWindowModal12+](#ZH-CN_TOPIC_0000002522080752__setsubwindowmodal12)。

子窗口之外的窗口调用该接口时，会报错。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isModal | boolean | 是 | 设置子窗口模态属性是否启用，true为启用，false为不启用。当前仅支持设置为true。 |
| modalityType | [ModalityType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__modalitytype14) | 是 | 子窗口模态类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    // 创建子窗
    try {
      let subWindow = windowStage.createSubWindow("testSubWindow");
      subWindow.then((data) => {
        if (!data) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        windowClass = data;
        let promise = windowClass.setSubWindowModal(true, window.ModalityType.WINDOW_MODALITY);
        promise.then(() => {
          console.info('Succeeded in setting subwindow modal');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set subwindow modal. Cause code: ${err.code}, message: ${err.message}`);
        });
    } catch (exception) {
      console.error(`Failed to create the subWindow. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setWindowDecorHeight11+

setWindowDecorHeight(height: number): void

设置窗口的标题栏高度，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

针对Tablet设备，非[自由多窗模式](../../guides/窗口开发术语.md#自由多窗模式)下调用此接口后，当设备切换到自由多窗模式时生效；在自由多窗模式下调用此接口后，立刻生效。

当主窗口进入全屏沉浸状态时，此时鼠标Hover到窗口标题栏热区时，会显示悬浮标题栏，悬浮标题栏高度固定为37vp。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | number | 是 | 设置的窗口标题栏高度，仅支持具有窗口标题栏的窗口。该参数为整数，浮点数输入将向下取整，取值范围为[37,112]，范围外为非法参数，单位为vp。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: Invalid parameter range. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
windowClass.setUIContent('pages/WindowPage').then(() => {
  let height: number = 50;
  try {
    windowClass?.setWindowDecorHeight(height);
    console.info(`Succeeded in setting the height of window decor: ${height}`);
  } catch (exception) {
    console.error(`Failed to set the height of window decor. Cause code: ${exception.code}, message: ${exception.message}`);
  }
})
```

#### setDecorButtonStyle14+

setDecorButtonStyle(dectorStyle: DecorButtonStyle): void

设置装饰栏按钮样式，仅对主窗和子窗生效。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 5.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.0开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dectorStyle | DecorButtonStyle | 是 | 要设置的装饰栏按钮样式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and subwindows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { ConfigurationConstant } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      windowStage.loadContent("pages/Index").then(() =>{
        let windowClass = windowStage.getMainWindowSync();
        let colorMode : ConfigurationConstant.ColorMode = ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT;
        let style: window.DecorButtonStyle = {
          colorMode: colorMode,
          buttonBackgroundSize: 28,
          spacingBetweenButtons: 12,
          closeButtonRightMargin: 20,
          buttonIconSize: 20,
          buttonBackgroundCornerRadius: 4
        };
        windowClass.setDecorButtonStyle(style);
        console.info(`Succeeded in setting the style of button. Data: ${JSON.stringify(style)}`);
      });
    } catch (exception) {
      console.error(`Failed to set the style of button. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### getDecorButtonStyle14+

getDecorButtonStyle(): DecorButtonStyle

获取装饰栏按钮样式，仅对主窗和子窗生效。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 5.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.0开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在各设备均可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DecorButtonStyle | 返回当前窗口装饰栏上的按钮样式，窗口装饰按钮区域位于窗口的右上角。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
try {
  let decorButtonStyle = windowClass.getDecorButtonStyle();
  console.info(`Succeeded in getting the style of button. Data: ${JSON.stringify(decorButtonStyle)}`);
} catch (exception) {
  console.error(`Failed to get the style of button. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindowDecorHeight11+

getWindowDecorHeight(): number

对存在标题栏和三键区的窗口形态生效，用于获取窗口的标题栏高度。如果使用Stage模型，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回的窗口标题栏高度。该参数为整数，取值范围为[37,112]，单位为vp。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
windowClass.setUIContent('pages/WindowPage').then(() => {
  try {
    let height = windowClass?.getWindowDecorHeight();
    console.info(`Succeeded in getting the height of window decor: ${height}`);
  } catch (exception) {
    console.error(`Failed to get the height of window decor. Cause code: ${exception.code}, message: ${exception.message}`);
  }
})
```

#### getTitleButtonRect11+

getTitleButtonRect(): TitleButtonRect

获取主窗口或启用装饰的子窗口的标题栏上的最小化、最大化、关闭按钮矩形区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TitleButtonRect | 标题栏上的最小化、最大化、关闭按钮矩形区域，该区域位置坐标相对窗口右上角。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        let titleButtonArea = windowClass.getTitleButtonRect();
        console.info('Succeeded in obtaining the area of title buttons. Data: ' + JSON.stringify(titleButtonArea));
      } catch (exception) {
        console.error(`Failed to get the area of title buttons. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### getWindowStatus12+

getWindowStatus(): [WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)

获取当前应用窗口的模式。

在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，应用的[targetAPIVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#配置文件标签)设置小于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::FULL_SCREEN。应用的[targetAPIVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#配置文件标签)设置大于等于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::MAXIMIZE。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11) | 当前窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
try {
  let windowStatusType = windowClass.getWindowStatus();
} catch (exception) {
  console.error(`Failed to obtain the window status of window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### isFocused12+

isFocused(): boolean

判断当前窗口是否已获焦。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否已获焦。true表示当前窗口已获焦，false则表示当前窗口未获焦。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
try {
  let focus = windowClass.isFocused();
  console.info(`Succeeded in checking whether the window is focused. Data: ${focus}`);
} catch (exception) {
  console.error(`Failed to check whether the window is focused. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### createSubWindowWithOptions12+

createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>

创建主窗口、子窗口或悬浮窗下的子窗口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回undefined。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| options | SubWindowOptions | 是 | 子窗口参数。decorEnabled为true时，子窗口为非沉浸式布局；decorEnabled为false时，子窗口为沉浸式布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Window> | Promise对象。返回当前Window下创建的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error; 3. The subWindow has been created and can not be created again. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows, subwindows, and floating windows are supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let options : window.SubWindowOptions = {
    title: 'title',
    decorEnabled: true,
    isModal: true
  };
  let promise = windowClass.createSubWindowWithOptions('mySubWindow', options);
  promise.then((data) => {
    console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setParentWindow19+

setParentWindow(windowId: number): Promise<void>

更改子窗口的父窗口，该父窗口仅支持同进程下的主窗口、子窗口或悬浮窗，使用Promise异步回调。

如果该子窗口处于获焦状态，且新的父窗口处于前台，则会抬升父窗口的层级。

如果该子窗口处于获焦状态，且新的父窗口的子窗口存在层级更高的模态子窗口，则焦点会转移给该模态子窗口。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 父窗口id，该参数应为整数。推荐使用getWindowProperties()方法获取父窗口id属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let windowClass: window.Window = window.findWindow("subWindow");
  let newParentWindow: window.Window = window.findWindow("newParentWindow");
  let newParentWindowId: number = newParentWindow.getWindowProperties().id;
  let promise = windowClass.setParentWindow(newParentWindowId);
  promise.then(() => {
    console.info('Succeeded in setting the new parent window.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the new parent window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the new parent window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getParentWindow19+

getParentWindow(): Window

获取子窗口的父窗口。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在各设备均可正常调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Window | 子窗口的父窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```ets
try {
  let windowClass: window.Window = window.findWindow("subWindow");
  let parentWindow: window.Window = windowClass.getParentWindow();
  let properties = parentWindow.getWindowProperties();
  console.info(`Succeeded in obtaining parent window properties. Property: ${JSON.stringify(properties)}`);
} catch (exception) {
  console.error(`Failed to get the parent window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowTitleButtonVisible14+

setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void

设置主窗标题栏上的最大化、最小化、关闭按钮是否可见。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isMaximizeButtonVisible | boolean | 是 | 设置最大化按钮是否可见，true为可见，false为隐藏。如果最大化按钮隐藏，那么在最大化场景下，也隐藏对应的还原按钮。 |
| isMinimizeButtonVisible | boolean | 是 | 设置最小化按钮是否可见，true为可见，false为隐藏。 |
| isCloseButtonVisible | boolean | 否 | 设置关闭按钮是否可见，true为可见，false为隐藏，默认值true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // 加载主窗口对应的页面
    windowStage.loadContent('pages/Index', (err) => {
      let mainWindow: window.Window | undefined = undefined;
      // 获取应用主窗口。
      windowStage.getMainWindow().then(
        data => {
          if (!data) {
            console.error('Failed to get main window. Cause: The data is undefined.');
            return;
          }
          mainWindow = data;
          console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
          // 调用setWindowTitleButtonVisible接口，隐藏主窗标题栏最大化、最小化、关闭按钮。
          mainWindow.setWindowTitleButtonVisible(false, false, false);
        }
      ).catch((err: BusinessError) => {
          if(err.code){
            console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
          }
      });
}
```

#### setWindowTopmost14+

setWindowTopmost(isWindowTopmost: boolean): Promise<void>

应用主窗口调用，用于实现将窗口置于其他应用窗口之上不被遮挡，使用Promise异步回调。

应用可通过自定义快捷键实现主窗口的置顶和取消置顶。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**需要权限：** ohos.permission.WINDOW_TOPMOST

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isWindowTopmost | boolean | 是 | 设置主窗口置顶，true为置顶，false为取消置顶。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```ets
// ets/pages/Index.ets
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined;
let keyUpEventAry: string[] = [];

@Entry
@Component
struct Index {
  private context = (this.getUIContext()?.getHostContext() as common.UIAbilityContext);
  private windowStage = this.context.windowStage;

  build() {
    RelativeContainer() {
      Button("窗口置顶")
        .onClick(() => {
          try {
            windowClass = this.windowStage.getMainWindowSync();
            //  true:窗口置顶，false:取消窗口置顶
            let isWindowTopmost: boolean = true;
            let promiseTopmost = windowClass.setWindowTopmost(isWindowTopmost);
            promiseTopmost.then(() => {
              console.info('Succeeded in setting the main window to be topmost.');
            }).catch((err: BusinessError) => {
              console.error(`Failed to set the main window to be topmost. Cause code: ${err.code}, message: ${err.message}`);
            });
          } catch (exception) {
            console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`)
          }
        })
    }
    .height('100%')
    .width('100%')
    .onKeyEvent((event) => {
      if(event) {
        if(event.type === KeyType.Down) {
          keyUpEventAry = [];
        }
        if(event.type === KeyType.Up) {
          keyUpEventAry.push(event.keyText);
          // 自定义快捷键 ctrl+T 执行主窗口置顶、取消置顶的操作
          if(windowClass && keyUpEventAry.includes('KEYCODE_CTRL_LEFT') && keyUpEventAry.includes('KEYCODE_T')) {
            let isWindowTopmost: boolean = false;
            windowClass.setWindowTopmost(isWindowTopmost);
          }
    })
}
```

#### raiseToAppTop14+

raiseToAppTop(): Promise<void>

应用子窗口调用，提升应用子窗口到顶层，只在当前应用同一个父窗口下的相同类型子窗范围内生效，对于自定义了zLevel属性的子窗口，只在当前应用同一个父窗口下相同zLevel值的子窗范围内生效。使用Promise异步回调。

使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](#ZH-CN_TOPIC_0000002522080752__showwindow9)并执行完毕。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```ets
// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    // 创建子窗
    windowStage.createSubWindow('testSubWindow').then((subWindow) => {
      if (subWindow == null) {
        console.error('Failed to create the subWindow. Cause: The data is empty');
        return;
      }
      subWindow.showWindow().then(() => {
        subWindow.raiseToAppTop().then(() => {
          console.info('Succeeded in raising window to app top');
        }).catch((err: BusinessError)=>{
          console.error(`Failed to raise window to app top. Cause code: ${err.code}, message: ${err.message}`);
        });
}
```

#### setRaiseByClickEnabled14+

setRaiseByClickEnabled(enable: boolean): Promise<void>

禁止/使能子窗点击抬升功能。使用Promise异步回调。

通常来说，点击一个子窗口，会将该子窗口显示抬升到应用内同一个父窗口下同类型子窗口的最上方，如果设置为false，那么点击子窗口的时候，不会将该子窗口进行抬升，而是保持不变。

使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](#ZH-CN_TOPIC_0000002522080752__showwindow9)并执行完毕。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置子窗口点击抬升功能是否使能，true表示使能，false表示禁止。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```ets
// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    // 创建子窗
    windowStage.createSubWindow("testSubWindow").then((subWindow) => {
      if (subWindow == null) {
        console.error('Failed to create the subWindow. Cause: The data is empty');
        return;
      }
      subWindow.showWindow().then(() => {
        try {
          let enabled = false;
          subWindow.setRaiseByClickEnabled(enabled).then(() => {
            console.info('Succeeded in disabling the raise-by-click function.');
          }).catch((err: BusinessError) => {
            console.error(`Failed to disable the raise-by-click function. Cause code: ${err.code}, message: ${err.message}`);
          });
        } catch (err) {
          console.error(`Failed to disable the raise-by-click function. Cause code: ${err.code}, message: ${err.message}`);
        }
      });
}
```

#### enableLandscapeMultiWindow12+

enableLandscapeMultiWindow(): Promise<void>

应用部分界面支持横向布局时，在进入该界面时使能，使能后可支持进入横向多窗。不建议竖向布局界面使用。

此接口只对应用主窗口生效，且需要在module.json5配置文件中[abilities](../../guides/module.json5配置文件.md#abilities标签)标签中配置preferMultiWindowOrientation属性为"landscape_auto"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let promise = windowClass.enableLandscapeMultiWindow();
      promise.then(() => {
        console.info('Succeeded in making multi-window become landscape.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to make multi-window become landscape. Cause code: ${err.code}, message: ${err.message}`);
      });
}
```

#### disableLandscapeMultiWindow12+

disableLandscapeMultiWindow(): Promise<void>

应用部分界面支持横向布局时，在退出该界面时去使能，去使能后不支持进入横向多窗。

此接口只对应用主窗口生效，且需要在module.json5配置文件中[abilities](../../guides/module.json5配置文件.md#abilities标签)标签中配置preferMultiWindowOrientation属性为"landscape_auto"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let promise = windowClass.disableLandscapeMultiWindow();
      promise.then(() => {
        console.info('Succeeded in making multi-window become not landscape.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to make multi-window become not landscape. Cause code: ${err.code}, message: ${err.message}`);
      });
}
```

#### setDialogBackGestureEnabled12+

setDialogBackGestureEnabled(enabled: boolean): Promise<void>

设置模态窗口是否响应手势返回事件，非模态窗口调用返回错误码。

**系统能力**：SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否响应手势返回事件。 true表示响应手势返回事件，触发onBackPress回调；false表示不响应手势返回事件，不触发onBackPress回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    let config: window.Configuration = {
      name: "test",
      windowType: window.WindowType.TYPE_DIALOG,
      ctx: this.context
    };
    try {
      window.createWindow(config, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        windowClass.setUIContent("pages/Index");
        let enabled = true;
        let promise = windowClass.setDialogBackGestureEnabled(enabled);
        promise.then(() => {
          console.info('Succeeded in setting dialog window to respond back gesture.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set dialog window to respond back gesture. Cause code: ${err.code}, message: ${err.message}`);
        });
    } catch (exception) {
      console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

```ets
// ets/pages/Index.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World'
  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .height('100%')
    .width('100%')
  }

  onBackPress(): boolean | void {
    console.info('Succeeded in setting dialog window to respond back gesture.');
    return true;
  }
```

#### enableDrag20+

enableDrag(enable: boolean): Promise<void>

使能/禁止拖拽窗口，仅对系统窗口、应用子窗口、全局悬浮窗和模态窗口生效。使用Promise异步回调。

使能后，将允许通过鼠标操作或触摸对窗口进行拉伸操作。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在Phone设备、Tablet设备和2in1设备上可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否允许拖拽。 true表示允许，false表示不允许。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.enableDrag(true).then(() => {
    console.info('succeeded in setting window draggable');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set window draggable. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set window draggable. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### startMoving14+

startMoving(): Promise<void>

[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，对系统窗口、应用主窗口、应用子窗口、全局悬浮窗和模态窗口生效。非自由窗口状态下，仅对系统窗口、应用子窗口、全局悬浮窗和模态窗口生效。用于开始移动窗口，使用Promise异步回调。

仅在[onTouch](触摸事件.md#ZH-CN_TOPIC_0000002553200725__touchevent对象说明)事件（其中，事件类型必须为TouchType.Down）的回调方法中调用此接口才会有移动效果，成功调用此接口后，窗口将跟随鼠标或触摸点移动。

在点击拖拽场景下，若不期望在按下时触发拖拽事件，则可以在事件类型为[TouchType.Move](枚举说明.md#ZH-CN_TOPIC_0000002553200889__touchtype)（需要保证当前行为已经触发TouchType.Down事件）时调用此接口，触发移动效果。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在Phone设备、2in1设备和Tablet设备上可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// Index.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private isTouchDown: boolean = false;
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Red)
          .onTouch((event: TouchEvent) => {
            if(event.type == TouchType.Down){
              this.isTouchDown = true;
            } else if (event.type === TouchType.Move && this.isTouchDown) {
              try {
                let context = this.getUIContext()?.getHostContext();
                if (!context) {
                  console.error('Failed to get host context.');
                  return;
                }
                window.getLastWindow(context).then((data)=>{
                  if (!data) {
                    console.error('Failed to get last window.');
                    return;
                  }
                  let windowClass: window.Window = data;
                  windowClass.startMoving().then(() => {
                    console.info('Succeeded in starting moving window.')
                  }).catch((err: BusinessError) => {
                    console.error(`Failed to start moving. Cause code: ${err.code}, message: ${err.message}`);
                  });
              } catch (exception) {
                console.error(`Failed to start moving window. Cause code: ${exception.code}, message: ${exception.message}`);
              }
            } else {
              this.isTouchDown = false;
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
```

#### startMoving15+

startMoving(offsetX: number, offsetY: number): Promise<void>

指定鼠标在窗口内的位置并移动窗口，使用Promise异步回调。

在同应用内窗口分合后，且鼠标保持按下状态直接移动新窗口，如果此时鼠标快速移动，窗口移动时鼠标可能会在窗口外。可以使用本接口指定窗口移动时鼠标在窗口内的位置，先移动窗口到鼠标位置，再开始移动窗口。

仅在[onTouch](触摸事件.md#ZH-CN_TOPIC_0000002553200725__touchevent对象说明)事件（其中，事件类型必须为TouchType.Down）的回调方法中调用此接口才会有移动效果，成功调用此接口后，窗口将跟随鼠标移动。

在点击拖拽场景下，若不期望在按下时触发拖拽事件，则可以在事件类型为[TouchType.Move](枚举说明.md#ZH-CN_TOPIC_0000002553200889__touchtype)（需要保证当前行为已经触发TouchType.Down事件）时调用此接口，触发移动效果。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offsetX | number | 是 | 窗口移动时预期鼠标位置相对窗口左上角的x轴偏移量，单位为px，该参数仅支持整数输入，浮点数向下取整。负值为非法参数，大于窗口宽度为非法参数，窗口宽度可以在窗口属性WindowProperties中获取。 |
| offsetY | number | 是 | 窗口移动时预期鼠标位置相对窗口左上角的y轴偏移量，单位为px，该参数仅支持整数输入，浮点数向下取整。负值为非法参数，大于窗口高度为非法参数，窗口高度可以在窗口属性WindowProperties中获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// Index.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private isTouchDown: boolean = false;
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Red)
          .onTouch((event: TouchEvent) => {
            if(event.type == TouchType.Down){
              this.isTouchDown = true;
            } else if (event.type === TouchType.Move && this.isTouchDown) {
              try {
                let context = this.getUIContext()?.getHostContext();
                if (!context) {
                  console.error('Failed to get host context.');
                  return;
                }
                window.getLastWindow(context).then((data)=>{
                  let windowClass: window.Window = data;
                  windowClass.startMoving(100, 50).then(() => {
                    console.info('Succeeded in starting moving window.')
                  }).catch((err: BusinessError) => {
                    console.error(`Failed to start moving. Cause code: ${err.code}, message: ${err.message}`);
                  });
              } catch (exception) {
                console.error(`Failed to start moving window. Cause code: ${exception.code}, message: ${exception.message}`);
              }
            } else {
              this.isTouchDown = false;
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
```

#### stopMoving15+

stopMoving(): Promise<void>

在窗口拖拽移动过程中，通过此接口来停止窗口移动，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {

  onWindowStageCreate(windowStage: window.WindowStage) {
    try {
      let windowClass = windowStage.getMainWindowSync();
      windowClass.on('windowRectChange', (data: window.RectChangeOptions) => {
        if (data.reason === window.RectChangeReason.MOVE) {
          windowClass.stopMoving().then(() => {
            console.info('Succeeded in stopping moving window.')
          }).catch((err: BusinessError) => {
            console.error(`Failed to stop moving. Cause code: ${err.code}, message: ${err.message}`);
          });
        }
      });
    } catch (exception) {
      console.error(`Failed to stop moving window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setGestureBackEnabled13+

setGestureBackEnabled(enabled: boolean): Promise<void>

设置当前窗口是否启用手势侧滑返回功能，仅主窗可以调用成功，其他类型的窗口调用返回1300004错误码。

开启此功能后，仅当窗口处于全屏模式且位于前台获焦状态下才会生效。

禁用此功能后，当前应用会禁用手势热区，侧滑返回功能失效；切换到其他应用或者回到桌面后，手势热区恢复，侧滑返回功能正常。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备上调用会返回801错误码，在其他设备上可正常调用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | true时开启返回手势功能，false时禁用返回手势功能。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;

      // 设置当前窗口禁用返回手势功能
      try {
        let gestureBackEnabled: boolean = false;
        let promise = windowClass.setGestureBackEnabled(gestureBackEnabled);
        promise.then(() => {
          console.info(`Succeeded in setting gesture back disabled`);
        }).catch((err: BusinessError) => {
          console.error(`Failed to set gesture back disabled, Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch(exception) {
        console.error(`Failed to set gesture back disabled, Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### isGestureBackEnabled13+

isGestureBackEnabled(): boolean

获取当前窗口是否启用返回手势功能，仅主窗可以调用成功，其他类型的窗口调用返回1300004错误码。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 该接口在2in1设备上调用会返回801错误码，在其他设备上可正常调用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否已经启用返回手势。true表示已启用返回手势功能，false表示已禁用返回手势功能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;

      // 获取当前窗口是否禁用返回手势功能
      try {
        let gestureBackEnabled: boolean = windowClass.isGestureBackEnabled();
        console.info(`Succeeded in obtaining gesture back enabled status: ${gestureBackEnabled}`);
      } catch (exception) {
        console.error(`Failed to get gesture back enabled status. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

**setSeparati[onTouch](../../topics/components/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)Enabled23+**

setSeparati[onTouch](../../topics/components/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)Enabled(enabled: boolean): Promise<void>

设置当前窗口是否支持事件分离状态，使用Promise异步回调。默认场景下为true，支持事件分离状态。

当enable为true，支持事件分离状态下：

- 所有手指点击产生的事件均会发送给其手指命中的窗口。

当enable为false，不支持事件分离状态下：

-

当第一根手指点击持续命中该窗口未抬起时，后续其他手指无论是否点击命中该窗口，其产生的事件均会分发给该窗口。

-

当第一根手指点击未保持持续命中该窗口时，后续其他手指即使点击命中该窗口，其产生的事件也不会分发给该窗口，该事件会被系统丢弃。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Window.SessionManager

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 窗口是否支持事件分离状态。true表示支持；false表示不支持。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let enabled = false;
try {
  let promise = windowClass.setSeparationTouchEnabled(enabled);
  promise.then(() => {
    console.info('Succeeded in setting the window to be separationTouchEnabled.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window to be separationTouchEnabled. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the separationTouchEnabled. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

**isSeparati[onTouch](../../topics/components/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)Enabled23+**

isSeparati[onTouch](../../topics/components/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)Enabled():boolean

获取当前窗口是否支持事件分离的状态。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Window.SessionManager

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否支持事件分离。 true表示支持窗口事件分离，false表示不支持窗口事件分离。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSeparationTouchEnabled = windowClass.isSeparationTouchEnabled();
  console.info(`Succeeded in getting the window separationTouchEnabled status: ${isSeparationTouchEnabled}`);
} catch (exception) {
  console.error(`Failed to get the window separationTouchEnabled status.. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

**setReceiveDragEventEnabled23+**

setReceiveDragEventEnabled(enabled: boolean): Promise<void>

设置当前窗口是否能接收[拖拽事件](拖拽事件.md#ZH-CN_TOPIC_0000002553200729__dragevent7)，使用Promise异步回调。

默认场景下为true，能够接收拖拽事件。

当enable为false，当前窗口不能接收拖拽事件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Window.SessionManager

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 窗口是否能接收拖拽事件。true表示能够接收拖拽事件；false表示不能接收拖拽事件。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let enabled = false;
try {
  let promise = windowClass.setReceiveDragEventEnabled(enabled);
  promise.then(() => {
    console.info('Succeeded in setting the window to be WindowReceiveDragEventEnabled.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window to be the window ReceiveDragEventEnabled. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the window ReceiveDragEventEnabled. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

**isReceiveDragEventEnabled23+**

isReceiveDragEventEnabled():boolean

获取当前窗口是否能接收[拖拽事件](拖拽事件.md#ZH-CN_TOPIC_0000002553200729__dragevent7)的状态。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Window.SessionManager

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否能接收拖拽事件的状态。 true表示能接收拖拽事件的状态，false表示不能接收拖拽事件的状态。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isReceiveDragEventEnabled = windowClass.isReceiveDragEventEnabled();
  console.info(`Succeeded in getting the window receiveDragEvent status: ${isReceiveDragEventEnabled}`);
} catch (exception) {
  console.error(`Failed to get the window receiveDragEvent status. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowShadowRadius17+

setWindowShadowRadius(radius: number): void

设置子窗或悬浮窗窗口边缘阴影的模糊半径。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS 5.1.0之前，该接口在2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.0开始，该接口在Phone设备、Tablet设备和2in1设备中可正常调用，在其他设备中返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 表示窗口边缘阴影的模糊半径。该参数为浮点数，单位为px，取值范围为[0.0, +∞)，取值为0.0时表示关闭窗口边缘阴影。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: The shadow radius is less than zero. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and float windows are supported. |

**示例：**

```ets
try {
  windowClass.setWindowShadowRadius(4.0);
} catch (exception) {
  console.error(`Failed to set shadow. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowCornerRadius17+

setWindowCornerRadius(cornerRadius: number): Promise<void>

设置子窗或悬浮窗的圆角半径值，使用Promise异步回调。

圆角半径值过大将会导致三键（最大化、最小化、关闭按钮）位置被裁切，且会导致热区不易识别，请根据窗口大小设置合适的圆角半径值。

在调用此接口之前调用[getWindowCornerRadius()](#ZH-CN_TOPIC_0000002522080752__getwindowcornerradius17)接口可以获得窗口默认圆角半径值。

**系统能力**：SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.0.0之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.0.0开始，该接口在Phone设备、Tablet设备和2in1设备下可正常调用，在其他设备中返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cornerRadius | number | 是 | 表示窗口圆角的半径值。该参数为浮点数，单位为vp，取值范围为[0.0, +∞)，取值为0.0时表示没有窗口圆角。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: The corner radius is less than zero. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.setWindowCornerRadius(1.0);
  promise.then(() => {
    console.info('Succeeded in setting window corner radius.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set window corner radius. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set corner radius. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getWindowCornerRadius17+

getWindowCornerRadius(): number

该接口用于获取子窗或悬浮窗的圆角半径值，在未调用[setWindowCornerRadius()](#ZH-CN_TOPIC_0000002522080752__setwindowcornerradius17)接口设置窗口圆角半径值时，调用此接口可获取窗口默认圆角半径值。

**系统能力**：SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在Phone、Tablet、PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前子窗或悬浮窗的圆角半径值，单位为vp。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and float windows are supported. |

**示例：**

```ets
try {
  let cornerRadius = windowClass.getWindowCornerRadius();
} catch (exception) {
  console.error(`Failed to get corner radius. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setExclusivelyHighlighted15+

setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>

设置窗口独占激活态属性。独占激活态表示窗口获焦时，会导致当前父子窗口链中处于激活态的其他窗口失去激活态。使用Promise异步回调。

此接口对主窗、模态窗不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusivelyHighlighted | boolean | 是 | 窗口是否独占激活态。true表示独占激活态；false表示不独占激活态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let exclusivelyHighlighted: boolean = true;
try {
  let promise = windowClass.setExclusivelyHighlighted(exclusivelyHighlighted);
  promise.then(() => {
    console.info('Succeeded in setting the window to be exclusively highlight.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the window to be exclusively highlight. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the window to be exclusively highlight. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### isWindowHighlighted18+

isWindowHighlighted(): boolean

获取当前窗口是否为激活态。为准确获取激活态，需要在[WindowEventType](Enums.md#ZH-CN_TOPIC_0000002553200717__windoweventtype10)生命周期处于WINDOW_ACTIVE之后调用。

可使用[on('windowHighlightChange')](#ZH-CN_TOPIC_0000002522080752__onwindowhighlightchange15)监听对应状态变更，再执行对应具体业务。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否为激活态。true表示当前窗口为激活态，false表示当前窗口非激活态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal Possible cause: The window is not created or destroyed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isHighlighted = windowClass.isWindowHighlighted();
  console.info(`Succeeded in getting the window highlight status: ${isHighlighted}`);
} catch (exception) {
  console.error(`Failed to get the window highlight status.. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setFollowParentMultiScreenPolicy17+

setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>

设置子窗口在其父窗口处于拖拽移动或拖拽缩放过程时，该子窗口是否支持跨多个屏幕同时显示。使用Promise异步回调。

通过监听父窗口大小位置变化，对子窗口调用[moveWindowTo()](#ZH-CN_TOPIC_0000002522080752__movewindowto9)等接口实现子窗口跟随父窗口布局时，此时子窗口默认不支持跨多个屏幕同时显示。

对子窗口调用此接口后可以使能子窗口在跟随父窗口布局过程中跨多个屏幕同时显示。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备调用返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置子窗口在其父窗口处于拖拽移动或拖拽缩放过程时，该子窗口是否支持跨多个屏幕同时显示。true表示支持；false表示不支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported.Function setFollowParentMultiScreenPolicy can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let windowClass: window.Window = window.findWindow("subWindow");
  let enabled: boolean = true;
  let promise = windowClass?.setFollowParentMultiScreenPolicy(enabled);
  promise.then(() => {
    console.info('Succeeded in setting the sub window supports multi-screen simultaneous display')
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the sub window supports multi-screen simultaneous display. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the sub window supports multi-screen simultaneous display. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setFollowParentWindowLayoutEnabled17+

setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>

设置子窗或模态窗口（即WindowType为TYPE_DIALOG的窗口）的布局信息（position和size）是否跟随主窗，使用Promise异步回调。

1、只支持主窗的一级子窗或模态窗口使用该接口。

2、当子窗或模态窗口调用该接口后，立即使其布局信息与主窗完全一致并保持，除非传入false再次调用该接口，否则效果将持续。

3、当子窗或模态窗口调用该接口后，再调用moveTo、resize等修改布局信息的接口将不生效。

4、当子窗或模态窗口不再使用该功能后，不保证子窗或模态窗口的布局信息（position和size）为确定的值，需要应用重新进行设置。

该接口调用生效后，[setRelativePositionToParentWindowEnabled()](#ZH-CN_TOPIC_0000002522080752__setrelativepositiontoparentwindowenabled20)接口调用不生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用跟随主窗布局。true表示启用，false表示不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. 3. The subwindow level is more than one. 4. The subwindow is following its parent window's position. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and dialog windows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (loadError) => {
      if (loadError.code) {
        console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
        return;
      }
      console.info("Succeeded in loading the content.");
      windowStage.createSubWindow("subWindow").then((subWindow: window.Window) => {
        if (subWindow == null) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        subWindow.setFollowParentWindowLayoutEnabled(true).then(() => {
          console.info("after set follow parent window layout")
        }).catch((error: BusinessError) => {
          console.error(`setFollowParentWindowLayoutEnabled failed. ${error.code} ${error.message}`);
        })
      }).catch((error: BusinessError) => {
        console.error(`createSubWindow failed. ${error.code} ${error.message}`);
      })
    });
  }
```

#### setRelativePositionToParentWindowEnabled20+

setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: [WindowAnchor](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowanchor20), offsetX?: number, offsetY?: number): Promise<void>

该接口仅在[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下生效，用于设置一级子窗是否支持与主窗保持相对位置不变。使用Promise异步回调。

该相对位置通过一级子窗与主窗之间锚点的偏移量表示，子窗和主窗使用的窗口锚点相同。

1、只支持非最大化一级子窗使用该接口。

2、当子窗调用该接口后，立即使其显示位置跟随主窗并保持相对位置不变，除非传入false再次调用该接口，否则效果将持续。

3、当子窗调用该接口后，再调用[moveWindowTo()](#ZH-CN_TOPIC_0000002522080752__movewindowto9)、[maximize()](#ZH-CN_TOPIC_0000002522080752__maximize12)修改窗口位置或大小的接口将不生效。

该接口调用生效后，[setFollowParentWindowLayoutEnabled()](#ZH-CN_TOPIC_0000002522080752__setfollowparentwindowlayoutenabled17)接口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 一级子窗是否支持与主窗保持相对位置不变。true表示支持；false表示不支持。 |
| anchor | [WindowAnchor](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowanchor20) | 否 | 一级子窗与主窗保持相对位置不变时的窗口锚点枚举。该参数仅在enabled为true时生效，默认值为window.WindowAnchor.TopStart，即默认锚点为窗口左上角。 |
| offsetX | number | 否 | 一级子窗锚点与主窗锚点位置的x轴偏移量，单位为px。该参数仅在enabled为true时生效，仅支持整数输入，浮点数向下取整，默认值为0。 |
| offsetY | number | 否 | 一级子窗锚点与主窗锚点位置的y轴偏移量，单位为px。该参数仅在enabled为true时生效，仅支持整数输入，浮点数向下取整，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.Function setRelativePositionToParentWindowEnabled can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows are supported. |

**示例：**

```ets
// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
      if (loadError.code) {
        console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
        return;
      }
      console.info("Succeeded in loading the content.");
      windowStage.createSubWindow("subWindow").then((subWindow: window.Window) => {
        if (subWindow == null) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        subWindow.setRelativePositionToParentWindowEnabled(true).then(() => {
          console.info("after set relative position to parent window enabled");
        }).catch((error: BusinessError) => {
          console.error(`setRelativePositionToParentWindowEnabled failed. ${error.code} ${error.message}`);
        })
      }).catch((error: BusinessError) => {
        console.error(`createSubWindow failed. ${error.code} ${error.message}`);
      })
    });
  }
```

#### setWindowTransitionAnimation20+

setWindowTransitionAnimation(transitionType: [WindowTransitionType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowtransitiontype20), animation: TransitionAnimation): Promise<void>

给特定场景下的窗口增加转场动画。

当前只支持在应用主窗下使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用，在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transitionType | [WindowTransitionType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowtransitiontype20) | 是 | 本次转场动画场景。当前只支持销毁场景。 |
| animation | TransitionAnimation | 是 | 本次转场动画配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range; 2. Invalid parameter length. |

**示例：**

```ets
// EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        const animationConfig: window.WindowAnimationConfig = {
          duration: 1000,
          curve: window.WindowAnimationCurve.LINEAR,
        };
        const transitionAnimation: window.TransitionAnimation = {
          opacity: 0.5,
          config: animationConfig
        };
        let promise = windowClass.setWindowTransitionAnimation(window.WindowTransitionType.DESTROY, transitionAnimation);
        promise.then((data) => {
          console.info('Succeeded in setting window transition animation. Cause:' + JSON.stringify(data));
        }).catch((err: BusinessError) => {
          console.error(`Failed to set window transition animation. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to obtain the window status of window. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    })
  }
```

#### getWindowTransitionAnimation20+

getWindowTransitionAnimation(transitionType: [WindowTransitionType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowtransitiontype20)): TransitionAnimation | undefined

获取特定场景下的窗口转场动画配置。

当前只支持在应用主窗下使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用，在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transitionType | [WindowTransitionType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowtransitiontype20) | 是 | 本次转场动画场景。当前只支持销毁场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TransitionAnimation | undefined | 对应场景下的转场动画配置。当未使用过setWindowTransitionAnimation接口时，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```ets
// EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        let transitionAnimationResult = windowClass.getWindowTransitionAnimation(window.WindowTransitionType.DESTROY);
        console.info('Succeeded in getting window transition animation: ' + JSON.stringify(transitionAnimationResult));
      } catch (exception) {
        console.error(`Failed to obtain the window transition animation. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    })
  }
```

#### setSubWindowZLevel18+

setSubWindowZLevel(zLevel: number): Promise<void>

设置当前子窗口层级级别，设置了模态属性的子窗不支持。使用Promise异步回调。

通过该接口改变子窗口的显示层级时，不会发生焦点切换。推荐使用[shiftAppWindowFocus()](Functions.md#ZH-CN_TOPIC_0000002553200715__windowshiftappwindowfocus11)进行焦点切换。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

设备行为差异： 该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zLevel | number | 是 | 子窗口层级级别。默认值为0，取值范围为[-10000, 10000]，该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Function setSubWindowZLevel can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only sub windows are supported. |
| 1300009 | The parent window is invalid. |

**示例：**

```ets
// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let zLevel: number = 1;
    // 创建子窗
    try {
      windowStage.createSubWindow('testSubWindow').then((subWindow) => {
        if (subWindow == null) {
          console.error('Failed to create the sub window. Cause: The sub window is null');
          return;
        }
        subWindow.setSubWindowZLevel(zLevel).then(() => {
          console.info('Succeeded in setting sub window zLevel.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set sub window zLevel. Cause code: ${err.code}, message: ${err.message}`);
        });
    } catch (err) {
      console.error(`Failed to create the sub window or set zLevel. Cause code: ${err.code}, message: ${err.message}`);
}
```

#### getSubWindowZLevel18+

getSubWindowZLevel(): number

获取当前子窗口层级级别。不支持主窗、系统窗调用。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

设备行为差异： 该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前子窗口层级级别。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function getSubWindowZLevel can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```ets
// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let subWindowZLevel = -1;
    // 创建子窗
    windowStage.createSubWindow('testSubWindow').then((subWindow) => {
      if (subWindow == null) {
        console.error('Failed to create the sub window. Cause: The sub window is null');
        return;
      }
      try {
        subWindowZLevel = subWindow.getSubWindowZLevel();
        console.info(`Succeeded in obtaining sub window zLevel: ${subWindowZLevel}`);
      } catch (err) {
        console.error(`Failed to obtain the sub window zLevel. Cause code: ${err.code}, message: ${err.message}`);
      }
    });
  }
```

#### isInFreeWindowMode22+

isInFreeWindowMode(): boolean

查询当前窗口是否为[自由窗口](../../guides/窗口开发术语.md#自由窗口)模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示在自由窗口模式，false表示非自由窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
let isInFreeWindowMode: boolean = windowClass.isInFreeWindowMode();
console.info(`isInFreeWindowMode: ${isInFreeWindowMode}`);
```

#### on('freeWindowModeChange')22+

on(type: 'freeWindowModeChange', callback: Callback<boolean>): void

开启自由窗口模式变化事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'freeWindowModeChange'，即自由窗口模式变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。返回当前窗口是否在自由窗口模式，true表示是自由窗口模式，false表示非自由窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
try {
  windowClass.on('freeWindowModeChange', (data) => {
    console.info('Succeeded in enabling the listener for free window mode changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(`Failed to enable the listener for free window mode changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('freeWindowModeChange')22+

off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void

关闭自由窗口模式变化事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'freeWindowModeChange'，即自由窗口模式变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数。返回当前窗口是否在自由窗口模式。如果传入参数，则关闭该监听。如果未传入参数，则关闭自由窗口模式变化事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
const callback = (isInFreeWindowMode: boolean) => {
  // ...
}
try {
  // 通过on接口开启监听
  windowClass.on('freeWindowModeChange', callback);
  // 关闭指定callback的监听
  windowClass.off('freeWindowModeChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听
  windowClass.off('freeWindowModeChange');
} catch (exception) {
  console.error(`Failed to disable the listener for free window mode change. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

**convert[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)AndRotation23+**

convert[Orientation](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__orientation9)AndRotation(from: RotationInfoType, to: RotationInfoType, value: number): number

提供窗口方向、屏幕方向和屏幕角度互相转换的能力。

窗口方向指窗口所在屏幕的方向，以窗口模块对横竖屏的定义方式表示，窗口的方向分别用0、1、2和3表示竖屏、反向横屏、反向竖屏和横屏四个方向，其对横竖屏的定义与[RotationChangeInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__rotationchangeinfo19)和枚举类[Orientation](Enums.md#ZH-CN_TOPIC_0000002553200717__orientation9)中对横竖屏的定义一致，如Orientation设置为LANDSCAPE时，窗口方向为横屏。

系统能力： SystemCapability.Window.SessionManager

设备行为差异： 该接口在Phone和Tablet设备可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | RotationInfoType | 是 | 待转换的值的类型。 |
| to | RotationInfoType | 是 | 目标值的类型。 |
| value | number | 是 | 待转换的值。该参数为整数，浮点数输入将向下取整，取值范围为[0, 3]，范围外为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回目标类型的转换值。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

示例：

```ets
try {
  let originalValue: number = 0;
  let fromType: window.RotationInfoType = window.RotationInfoType.WINDOW_ORIENTATION;
  let toType: window.RotationInfoType = window.RotationInfoType.DISPLAY_ORIENTATION;
  let convertedValue: number = windowClass.convertOrientationAndRotation(fromType, toType, originalValue);
  console.info(`Convert ${originalValue} of type: ${fromType} to ${convertedValue} of type: ${toType}`);
} catch (exception) {
  console.error(`Failed to convert orientation and rotation between window and display. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### setWindowSystemBarProperties(deprecated)

setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void

设置主窗口状态栏的属性，使用callback异步回调，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).SPLIT_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

子窗口调用后不生效。


从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的[setWindowSystemBarProperties()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | SystemBarProperties | 是 | 状态栏的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        //以下两个属性从API Version8开始支持
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      try {
        windowClass.setWindowSystemBarProperties(SystemBarProperties, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('Succeeded in setting the system bar properties.');
        });
      } catch (exception) {
        console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setWindowSystemBarEnable(deprecated)

setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用callback异步回调。

从API version 12开始，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).SPLIT_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。


从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的[setWindowSystemBarEnable()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarenable9)替代。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏模式时状态栏和底部导航区域是否显示。 例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |
callbackAsyncCallback<void>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// 此处以状态栏等均不显示为例
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = [];
      try {
        windowClass.setWindowSystemBarEnable(names, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('Succeeded in setting the system bar to be invisible.');
        });
      } catch (exception) {
        console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### setWindowLayoutFullScreen(deprecated)

setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void

设置主窗口或子窗口的布局是否为沉浸式布局，使用callback异步回调。系统窗口调用不生效。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。


从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的[setWindowLayoutFullScreen()](#ZH-CN_TOPIC_0000002522080752__setwindowlayoutfullscreen9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.2之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.2开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局状态栏、底部导航区域仍然显示）。true表示沉浸式布局；false表示非沉浸式布局。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen = true;
      try {
        windowClass.setWindowLayoutFullScreen(isLayoutFullScreen, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('Succeeded in setting the window layout to full-screen mode.');
        });
      } catch (exception) {
        console.error(`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
```

#### show(deprecated)

show(callback: AsyncCallback<void>): void

显示当前窗口，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[showWindow()](#ZH-CN_TOPIC_0000002522080752__showwindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.show((err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to show the window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the window.');
});
```

#### show(deprecated)

show(): Promise<void>

显示当前窗口，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[showWindow()](#ZH-CN_TOPIC_0000002522080752__showwindow9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.show();
promise.then(() => {
  console.info('Succeeded in showing the window.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show the window. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### destroy(deprecated)

destroy(callback: AsyncCallback<void>): void

销毁当前窗口，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[destroyWindow()](#ZH-CN_TOPIC_0000002522080752__destroywindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.destroy((err: BusinessError) => {
  const errCode: number = err.code;
  if (err.code) {
    console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in destroying the window.');
});
```

#### destroy(deprecated)

destroy(): Promise<void>

销毁当前窗口，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[destroyWindow()](#ZH-CN_TOPIC_0000002522080752__destroywindow9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.destroy();
promise.then(() => {
  console.info('Succeeded in destroying the window.');
}).catch((err: BusinessError) => {
  console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### moveTo(deprecated)

moveTo(x: number, y: number, callback: AsyncCallback<void>): void

移动窗口位置，使用callback异步回调。

全屏模式窗口不支持该操作。


从API version 7开始支持，从API version 9开始废弃，建议使用[moveWindowTo()](#ZH-CN_TOPIC_0000002522080752__movewindowto9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.moveTo(300, 300, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in moving the window.');
});
```

#### moveTo(deprecated)

moveTo(x: number, y: number): Promise<void>

移动窗口位置，使用Promise异步回调。

全屏模式窗口不支持该操作。


从API version 7开始支持，从API version 9开始废弃，建议使用[moveWindowTo()](#ZH-CN_TOPIC_0000002522080752__movewindowto9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在y轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.moveTo(300, 300);
promise.then(() => {
  console.info('Succeeded in moving the window.');
}).catch((err: BusinessError) => {
  console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### resetSize(deprecated)

resetSize(width: number, height: number, callback: AsyncCallback<void>): void

基于窗口左上角顶点改变当前窗口大小，使用callback异步回调。

应用主窗口与子窗口存在大小限制，默认宽度范围：[320, 1920]，默认高度范围：[240, 1920]，单位为vp。

应用主窗口与子窗口的最小宽度与最小高度可由产品端进行配置，配置后的最小宽度与最小高度以产品段配置值为准，具体尺寸限制范围可以通过[getWindowLimits](#ZH-CN_TOPIC_0000002522080752__getwindowlimits11)接口进行查询。

系统窗口存在大小限制，宽度范围：(0, 1920]，高度范围：(0, 1920]，单位为vp。

设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

全屏模式窗口不支持该操作。


从API version 7开始支持，从API version 9开始废弃，建议使用[resize()](#ZH-CN_TOPIC_0000002522080752__resize9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.resetSize(500, 1000, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in changing the window size.');
});
```

#### resetSize(deprecated)

resetSize(width: number, height: number): Promise<void>

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。

应用主窗口与子窗口存在大小限制，默认宽度范围：[320, 1920]，默认高度范围：[240, 1920]，单位为vp。

应用主窗口与子窗口的最小宽度与最小高度可由产品端进行配置，配置后的最小宽度与最小高度以产品段配置值为准，具体尺寸限制范围可以通过[getWindowLimits](#ZH-CN_TOPIC_0000002522080752__getwindowlimits11)接口进行查询。

系统窗口存在大小限制，宽度范围：(0, 1920]，高度范围：(0, 1920]，单位为vp。

设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

全屏模式窗口不支持该操作。


从API version 7开始支持，从API version 9开始废弃，建议使用[resize()](#ZH-CN_TOPIC_0000002522080752__resize9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](../../errors/通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.resetSize(500, 1000);
promise.then(() => {
  console.info('Succeeded in changing the window size.');
}).catch((err: BusinessError) => {
  console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### getProperties(deprecated)

getProperties(callback: AsyncCallback<WindowProperties>): void

获取当前窗口的属性，使用callback异步回调，返回WindowProperties。


从API version 6开始支持，从API version 9开始废弃，建议使用[getWindowProperties()](#ZH-CN_TOPIC_0000002522080752__getwindowproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<WindowProperties> | 是 | 回调函数。返回当前窗口属性。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.getProperties((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to obtain the window properties. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in obtaining the window properties. Data: ' + JSON.stringify(data));
});
```

#### getProperties(deprecated)

getProperties(): Promise<WindowProperties>

获取当前窗口的属性，使用Promise异步回调，返回WindowProperties。


从API version 6开始支持，从API version 9开始废弃，建议使用[getWindowProperties()](#ZH-CN_TOPIC_0000002522080752__getwindowproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<WindowProperties> | Promise对象。返回当前窗口属性。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.getProperties();
promise.then((data) => {
  console.info('Succeeded in obtaining the window properties. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the window properties. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### getAvoidArea(deprecated)

getAvoidArea(type: [AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7), callback: AsyncCallback<[AvoidArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__avoidarea7)>): void

获取当前窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。

主窗口/子窗口：

- [自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下，仅存在固定态软键盘（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_KEYBOARD）类型的避让区域。

- 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_SYSTEM）类型的避让区域。

- 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

- 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

- 仅在调用[setSystemAvoidAreaEnabled](#ZH-CN_TOPIC_0000002522080752__setsystemavoidareaenabled18)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。


从API version 7开始支持，从API version 9开始废弃，建议使用[getWindowAvoidArea()](#ZH-CN_TOPIC_0000002522080752__getwindowavoidarea9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7) | 是 | 表示规避区类型。 |
| callback | AsyncCallback<AvoidArea> | 是 | 回调函数。返回窗口内容规避区域。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let type = window.AvoidAreaType.TYPE_SYSTEM;
windowClass.getAvoidArea(type, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to obtain the area. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in obtaining the area. Data:' + JSON.stringify(data));
});
```

#### getAvoidArea(deprecated)

getAvoidArea(type: [AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)): Promise<[AvoidArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__avoidarea7)>

获取当前窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。

主窗口/子窗口：

- [自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下，仅存在固定态软键盘（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_KEYBOARD）类型的避让区域。

- 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](Enums.md#ZH-CN_TOPIC_0000002553200717__avoidareatype7)为TYPE_SYSTEM）类型的避让区域。

- 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

- 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

- 仅在调用[setSystemAvoidAreaEnabled](#ZH-CN_TOPIC_0000002522080752__setsystemavoidareaenabled18)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。


从API version 7开始支持，从API version 9开始废弃，建议使用[getWindowAvoidArea()](#ZH-CN_TOPIC_0000002522080752__getwindowavoidarea9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__avoidareatype7) | 是 | 表示规避区类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AvoidArea> | Promise对象。返回窗口内容规避区域。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let type = window.AvoidAreaType.TYPE_SYSTEM;
let promise = windowClass.getAvoidArea(type);
promise.then((data) => {
  console.info('Succeeded in obtaining the area. Data:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the area. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setFullScreen(deprecated)

setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void

设置主窗口或子窗口的布局是否为全屏布局，使用callback异步回调。

全屏布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非全屏布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。


从API version 6开始支持，从API version 9开始废弃，建议联合使用[setWindowSystemBarEnable()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarenable9)和[setWindowLayoutFullScreen()](#ZH-CN_TOPIC_0000002522080752__setwindowlayoutfullscreen9)替代实现全屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFullScreen | boolean | 是 | 是否设为全屏布局（该全屏布局影响状态栏、底部导航区域显示）。true表示全屏；false表示非全屏。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let isFullScreen: boolean = true;
      windowClass.setFullScreen(isFullScreen, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to enable the full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in enabling the full-screen mode.');
      });
}
```

#### setFullScreen(deprecated)

setFullScreen(isFullScreen: boolean): Promise<void>

设置主窗口或子窗口的布局是否为全屏布局，使用Promise异步回调。

全屏布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非全屏布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。


从API version 6开始支持，从API version 9开始废弃，建议联合使用[setWindowSystemBarEnable()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarenable9)和[setWindowLayoutFullScreen()](#ZH-CN_TOPIC_0000002522080752__setwindowlayoutfullscreen9)替代实现全屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFullScreen | boolean | 是 | 是否设为全屏布局（该全屏布局影响状态栏、底部导航区域显示）。true表示全屏；false表示非全屏。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let isFullScreen: boolean = true;
      let promise = windowClass.setFullScreen(isFullScreen);
      promise.then(() => {
        console.info('Succeeded in enabling the full-screen mode.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to enable the full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
      });
}
```

#### setLayoutFullScreen(deprecated)

setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void

设置主窗口或子窗口的布局是否为沉浸式布局，使用callback异步回调。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowLayoutFullScreen()](#ZH-CN_TOPIC_0000002522080752__setwindowlayoutfullscreen9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局不影响状态栏、底部导航区域显示）。true表示沉浸式布局；false表示非沉浸式布局。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen: boolean = true;
      windowClass.setLayoutFullScreen(isLayoutFullScreen, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in setting the window layout to full-screen mode.');
      });
}
```

#### setLayoutFullScreen(deprecated)

setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>

设置主窗口或子窗口的布局是否为沉浸式布局，使用Promise异步回调。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowLayoutFullScreen()](#ZH-CN_TOPIC_0000002522080752__setwindowlayoutfullscreen9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局不影响状态栏、底部导航区域显示）。true表示沉浸式布局；false表示非沉浸式布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen: boolean = true;
      let promise = windowClass.setLayoutFullScreen(isLayoutFullScreen);
      promise.then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
      });
}
```

#### setSystemBarEnable(deprecated)

setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用callback异步回调。

从API version 12开始，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).SPLIT_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarEnable()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarenable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏模式时状态栏和底部导航区域是否显示。 例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |
callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
// 此处以状态栏等均不显示为例
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = [];
      windowClass.setSystemBarEnable(names, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in setting the system bar to be invisible.');
      });
}
```

#### setSystemBarEnable(deprecated)

setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用Promise异步回调。

从API version 12开始，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).SPLIT_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarEnable()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarenable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏模式时状态栏和底部导航区域是否显示。 例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
// 此处以状态栏等均不显示为例
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = [];
      let promise = windowClass.setSystemBarEnable(names);
      promise.then(() => {
        console.info('Succeeded in setting the system bar to be invisible.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
      });
}
```

#### setSystemBarProperties(deprecated)

setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void

设置主窗口状态栏的属性，使用callback异步回调，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).SPLIT_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarProperties()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | SystemBarProperties | 是 | 状态栏的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        //以下两个属性从API Version8开始支持
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      windowClass.setSystemBarProperties(SystemBarProperties, (err) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in setting the system bar properties.');
      });
}
```

#### setSystemBarProperties(deprecated)

setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>

设置主窗口状态栏的属性，使用Promise异步回调，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.[WindowStatusType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11).SPLIT_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

子窗口调用后不生效。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarProperties()](#ZH-CN_TOPIC_0000002522080752__setwindowsystembarproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | SystemBarProperties | 是 | 状态栏的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        //以下两个属性从API Version8开始支持
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      let promise = windowClass.setSystemBarProperties(SystemBarProperties);
      promise.then(() => {
        console.info('Succeeded in setting the system bar properties.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
      });
}
```

#### loadContent(deprecated)

loadContent(path: string, callback: AsyncCallback<void>): void

为当前窗口加载具体页面内容，使用callback异步回调。建议在UIAbility启动过程中使用该接口，多次调用该接口会先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。


从API version 7开始支持，从API version 9开始废弃，建议使用[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.loadContent('pages/page2/page3', (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in loading the content.');
});
```

#### loadContent(deprecated)

loadContent(path: string): Promise<void>

为当前窗口加载具体页面内容，使用Promise异步回调。建议在UIAbility启动过程中使用该接口，多次调用该接口会先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。


从API version 7开始支持，从API version 9开始废弃，建议使用[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.loadContent('pages/page2/page3');
promise.then(() => {
  console.info('Succeeded in loading the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### isShowing(deprecated)

isShowing(callback: AsyncCallback<boolean>): void

判断当前窗口是否已显示，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[isWindowShowing()](#ZH-CN_TOPIC_0000002522080752__iswindowshowing9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前窗口已显示，返回false表示当前窗口未显示。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.isShowing((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to check whether the window is showing. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
});
```

#### isShowing(deprecated)

isShowing(): Promise<boolean>

判断当前窗口是否已显示，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[isWindowShowing()](#ZH-CN_TOPIC_0000002522080752__iswindowshowing9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前窗口已显示，返回false表示当前窗口未显示。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.isShowing();
promise.then((data) => {
  console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether the window is showing. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### on('systemAvoidAreaChange')(deprecated)

on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void

开启当前窗口系统规避区变化的监听。


从API version 7开始支持，从API version 9开始废弃，建议使用[on('avoidAreaChange')](#ZH-CN_TOPIC_0000002522080752__onavoidareachange9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemAvoidAreaChange'，即系统规避区变化事件。 |
| callback | Callback<AvoidArea> | 是 | 回调函数。返回当前规避区。 |

**示例：**

```ets
windowClass.on('systemAvoidAreaChange', (data) => {
  console.info('Succeeded in enabling the listener for system avoid area changes. Data: ' + JSON.stringify(data));
});
```

#### off('systemAvoidAreaChange')(deprecated)

off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void

关闭当前窗口系统规避区变化的监听。


从API version 7开始支持，从API version 9开始废弃，建议使用[off('avoidAreaChange')](#ZH-CN_TOPIC_0000002522080752__offavoidareachange9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemAvoidAreaChange'，即系统规避区变化事件。 |
| callback | Callback<AvoidArea> | 否 | 回调函数。返回当前规避区。若传入参数，则关闭该监听。若未传入参数，则关闭所有系统规避区变化的监听。 |

**示例：**

```ets
const callback = (avoidArea: window.AvoidArea) => {
  // ...
}
windowClass.on('systemAvoidAreaChange', callback);
windowClass.off('systemAvoidAreaChange', callback);
// 如果通过on开启多个callback进行监听，同时关闭所有监听：
windowClass.off('systemAvoidAreaChange');
```

#### isSupportWideGamut(deprecated)

isSupportWideGamut(callback: AsyncCallback<boolean>): void

判断当前窗口是否支持广色域模式，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃，建议使用[isWindowSupportWideGamut()](#ZH-CN_TOPIC_0000002522080752__iswindowsupportwidegamut9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.isSupportWideGamut((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in checking whether the window support WideGamut Data: ' + JSON.stringify(data));
});
```

#### isSupportWideGamut(deprecated)

isSupportWideGamut(): Promise<boolean>

判断当前窗口是否支持广色域模式，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃，建议使用[isWindowSupportWideGamut()](#ZH-CN_TOPIC_0000002522080752__iswindowsupportwidegamut9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.isSupportWideGamut();
promise.then((data) => {
  console.info('Succeeded in checking whether the window support WideGamut. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### set[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(deprecated)

set[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(colorSpace:ColorSpace, callback: AsyncCallback<void>): void

设置当前窗口为广色域模式或默认色域模式，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃，建议使用[setWindowColorSpace()](#ZH-CN_TOPIC_0000002522080752__setwindowcolorspace9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8) | 是 | 设置色域模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.setColorSpace(window.ColorSpace.WIDE_GAMUT, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting window colorspace.');
});
```

#### set[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(deprecated)

set[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(colorSpace:ColorSpace): Promise<void>

设置当前窗口为广色域模式或默认色域模式，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃，建议使用[setWindowColorSpace()](#ZH-CN_TOPIC_0000002522080752__setwindowcolorspace9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8) | 是 | 设置色域模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.setColorSpace(window.ColorSpace.WIDE_GAMUT);
promise.then(() => {
  console.info('Succeeded in setting window colorspace.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### get[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(deprecated)

get[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(callback: AsyncCallback<ColorSpace>): void

获取当前窗口色域模式，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃，建议使用[getWindowColorSpace()](#ZH-CN_TOPIC_0000002522080752__getwindowcolorspace9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)> | 是 | 回调函数。当获取成功，err为undefined，data为当前色域模式。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.getColorSpace((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to get window colorspace. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting window colorspace. Cause:' + JSON.stringify(data));
});
```

#### get[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(deprecated)

get[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)(): Promise<ColorSpace>

获取当前窗口色域模式，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃，建议使用[getWindowColorSpace()](#ZH-CN_TOPIC_0000002522080752__getwindowcolorspace9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ColorSpace](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__colorspace8)> | Promise对象。返回当前色域模式。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.getColorSpace();
promise.then((data) => {
  console.info('Succeeded in getting window color space. Cause:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to get window colorspace. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setBackgroundColor(deprecated)

setBackgroundColor(color: string, callback: AsyncCallback<void>): void

设置窗口的背景色，使用callback异步回调。Stage模型下，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBackgroundColor()](#ZH-CN_TOPIC_0000002522080752__setwindowbackgroundcolor9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | string | 是 | 需要设置的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let color: string = '#00ff33';
windowClass.setBackgroundColor(color, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the background color. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the background color.');
});
```

#### setBackgroundColor(deprecated)

setBackgroundColor(color: string): Promise<void>

设置窗口的背景色，使用Promise异步回调。Stage模型下，该接口需要在[loadContent()](#ZH-CN_TOPIC_0000002522080752__loadcontent9)或[setUIContent()](#ZH-CN_TOPIC_0000002522080752__setuicontent9)调用生效后使用。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBackgroundColor()](#ZH-CN_TOPIC_0000002522080752__setwindowbackgroundcolor9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | string | 是 | 需要设置的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let color: string = '#00ff33';
let promise = windowClass.setBackgroundColor(color);
promise.then(() => {
  console.info('Succeeded in setting the background color.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the background color. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setBrightness(deprecated)

setBrightness(brightness: number, callback: AsyncCallback<void>): void

允许应用窗口设置屏幕亮度值，使用callback异步回调。

当前屏幕亮度规格：窗口设置屏幕亮度生效时，控制中心不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心可以调整系统屏幕亮度。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBrightness()](#ZH-CN_TOPIC_0000002522080752__setwindowbrightness9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let brightness: number = 1;
windowClass.setBrightness(brightness, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the brightness.');
});
```

#### setBrightness(deprecated)

setBrightness(brightness: number): Promise<void>

允许应用窗口设置屏幕亮度值，使用Promise异步回调。

当前屏幕亮度规格：窗口设置屏幕亮度生效时，控制中心不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心可以调整系统屏幕亮度。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBrightness()](#ZH-CN_TOPIC_0000002522080752__setwindowbrightness9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let brightness: number = 1;
let promise = windowClass.setBrightness(brightness);
promise.then(() => {
  console.info('Succeeded in setting the brightness.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setDimBehind(deprecated)

setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void

窗口叠加时，设备有子窗口的情况下设置靠后的窗口的暗度值，使用callback异步回调。

该接口不支持使用。从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dimBehindValue | number | 是 | 表示靠后的窗口的暗度值，取值范围为[0.0, 1.0]，取1.0时表示最暗。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.setDimBehind(0.5, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the dimness. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the dimness.');
});
```

#### setDimBehind(deprecated)

setDimBehind(dimBehindValue: number): Promise<void>

窗口叠加时，设备有子窗口的情况下设置靠后的窗口的暗度值，使用Promise异步回调。

该接口不支持使用。从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dimBehindValue | number | 是 | 表示靠后的窗口的暗度值，取值范围为0-1，1表示最暗。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.setDimBehind(0.5);
promise.then(() => {
  console.info('Succeeded in setting the dimness.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the dimness. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setFocusable(deprecated)

setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void

设置使用点击或其他方式使该窗口获焦的场景时，该窗口是否支持窗口焦点从操作前的获焦窗口切换到该窗口，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowFocusable()](#ZH-CN_TOPIC_0000002522080752__setwindowfocusable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 点击时是否支持切换焦点窗口。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考不可获焦窗口中输入框与输入法交互指南。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
windowClass.setFocusable(isFocusable, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the window to be focusable.');
});
```

#### setFocusable(deprecated)

setFocusable(isFocusable: boolean): Promise<void>

设置使用点击或其他方式使该窗口获焦的场景时，该窗口是否支持窗口焦点从点击前的获焦窗口切换到该窗口，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowFocusable()](#ZH-CN_TOPIC_0000002522080752__setwindowfocusable9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 点击时是否支持切换焦点窗口。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考不可获焦窗口中输入框与输入法交互指南。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
let promise = windowClass.setFocusable(isFocusable);
promise.then(() => {
  console.info('Succeeded in setting the window to be focusable.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setKeepScreenOn(deprecated)

setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void

设置屏幕是否为常亮状态，使用callback异步回调。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowKeepScreenOn()](#ZH-CN_TOPIC_0000002522080752__setwindowkeepscreenon9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
windowClass.setKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the screen to be always on.');
});
```

#### setKeepScreenOn(deprecated)

setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

设置屏幕是否为常亮状态，使用Promise异步回调。


从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowKeepScreenOn()](#ZH-CN_TOPIC_0000002522080752__setwindowkeepscreenon9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
let promise = windowClass.setKeepScreenOn(isKeepScreenOn);
promise.then(() => {
  console.info('Succeeded in setting the screen to be always on.');
}).catch((err: BusinessError) => {
  console.info(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setOutsideTouchable(deprecated)

setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void

设置是否允许可点击子窗口之外的区域，使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。

从API version 9开始，系统默认允许点击子窗口之外的区域，此接口不再支持使用，也不再提供替代接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| touchable | boolean | 是 | 设置是否可点击。true表示可点击；false表示不可点击。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

windowClass.setOutsideTouchable(true, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the area to be touchable. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the area to be touchable.');
});
```

#### setOutsideTouchable(deprecated)

setOutsideTouchable(touchable: boolean): Promise<void>

设置是否允许可点击子窗口之外的区域，使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。

从API version 9开始，系统默认允许点击子窗口之外的区域，此接口不再支持使用，也不再提供替代接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| touchable | boolean | 是 | 设置是否可点击。true表示可点击；false表示不可点击。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.setOutsideTouchable(true);
promise.then(() => {
  console.info('Succeeded in setting the area to be touchable.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the area to be touchable. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setPrivacyMode(deprecated)

setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowPrivacyMode()](#ZH-CN_TOPIC_0000002522080752__setwindowprivacymode9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示模式开启；false表示模式关闭。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
windowClass.setPrivacyMode(isPrivacyMode, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the window to privacy mode.');
});
```

#### setPrivacyMode(deprecated)

setPrivacyMode(isPrivacyMode: boolean): Promise<void>

设置窗口是否为隐私模式，使用Promise异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowPrivacyMode()](#ZH-CN_TOPIC_0000002522080752__setwindowprivacymode9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示模式开启；false表示模式关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
let promise = windowClass.setPrivacyMode(isPrivacyMode);
promise.then(() => {
  console.info('Succeeded in setting the window to privacy mode.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
});
```

#### setTouchable(deprecated)

setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void

设置窗口是否为可触状态，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowTouchable()](#ZH-CN_TOPIC_0000002522080752__setwindowtouchable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可触状态。true表示可触；false表示不可触。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable = true;
windowClass.setTouchable(isTouchable, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the window to be touchable.');
});
```

#### setTouchable(deprecated)

setTouchable(isTouchable: boolean): Promise<void>

设置窗口是否为可触状态，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowTouchable()](#ZH-CN_TOPIC_0000002522080752__setwindowtouchable9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可触状态。true表示可触；false表示不可触。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable = true;
let promise = windowClass.setTouchable(isTouchable);
promise.then(() => {
  console.info('Succeeded in setting the window to be touchable.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
});
```