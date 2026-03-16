[]()[]()

# Functions

-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](../misc/SysCap (系统能力).md#ZH-CN_TOPIC_0000002529286149__caniuse)接口判断当前设备是否支持此syscap及对应接口。

[]()[]()

#### 导入模块

```ets
import { window } from '@kit.ArkUI';
```

[]()[]()

#### window.createWindow9+

createWindow(config: Configuration, callback: AsyncCallback<Window>): void

创建子窗口或者系统窗口，使用callback异步回调。

非[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态下，子窗口创建后默认是[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)。

自由窗口状态下，子窗口参数[decorEnabled](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。

**需要权限：** ohos.permission.SYSTEM_FLOAT_WINDOW（仅当创建窗口类型为window.WindowType.TYPE_FLOAT时需要申请）

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明config[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)是创建窗口时的参数。callbackAsyncCallback<[Window](../../types/interfaces/Interface (Window).md)>是回调函数。返回当前创建的窗口对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported. createWindow can not work correctly due to limited device capabilities.1300001Repeated operation.1300002This window state is abnormal.1300004Unauthorized operation.1300006This window context is abnormal.1300009The parent window is invalid.

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
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
        console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
        windowClass.resize(500, 1000);
      });
    } catch (exception) {
      console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```

[]()[]()

#### window.createWindow9+

createWindow(config: Configuration): Promise<Window>

创建子窗口或者系统窗口，使用Promise异步回调。

非[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态下，子窗口创建后默认是[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)。

自由窗口状态下，子窗口参数[decorEnabled](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。

**需要权限：** ohos.permission.SYSTEM_FLOAT_WINDOW（仅当创建窗口类型为window.WindowType.TYPE_FLOAT时需要申请）

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明config[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)是创建窗口时的参数。

**返回值：**

类型说明Promise<[Window](../../types/interfaces/Interface (Window).md)>Promise对象。返回当前创建的窗口对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported. createWindow can not work correctly due to limited device capabilities.1300001Repeated operation.1300002This window state is abnormal.1300004Unauthorized operation.1300006This window context is abnormal.1300009The parent window is invalid.

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let config: window.Configuration = {
      name: "test",
      windowType: window.WindowType.TYPE_DIALOG,
      ctx: this.context
    };
    try {
      window.createWindow(config).then((value:window.Window) => {
        console.info('Succeeded in creating the window. Data: ' + JSON.stringify(value));
        value.resize(500, 1000);
      }).catch((err:BusinessError)=> {
        console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```

[]()[]()

#### window.findWindow9+

findWindow(name: string): Window

查找指定名称对应的窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明namestring是窗口名称。查找子窗口或系统窗口时使用[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)中的窗口名称；查找主窗口时使用[getWindowName](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getwindowname12)获取当前实例的窗口名称。

**返回值：**

类型说明[Window](../../types/interfaces/Interface (Window).md)当前查找的窗口对象。如果查找指定名称对应的窗口不存在，则返回对象为空。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.1300002This window state is abnormal.

**示例：**

```ets
let windowClass: window.Window | undefined = undefined;
try {
  windowClass = window.findWindow('test');
} catch (exception) {
  console.error(`Failed to find the Window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

[]()[]()

#### window.getLastWindow9+

getLastWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void

获取当前应用内层级最高的子窗口，使用callback异步回调。

若无应用子窗口或子窗口未调用[showWindow()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__showwindow9)进行显示，则返回应用主窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明ctx[BaseContext](../graphics/BaseContext.md)是当前应用上下文信息。callbackAsyncCallback<[Window](../../types/interfaces/Interface (Window).md)>是回调函数。返回当前应用内层级最高的窗口对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.1300002This window state is abnormal. Top window or main window is null or destroyed.1300006This window context is abnormal.

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      if (err.code) {
        console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
      }
      windowStage.createSubWindow('TestSubWindow').then((subWindow) => {
        let storage: LocalStorage = new LocalStorage();
        subWindow.loadContent('pages/Index', storage, (err: BusinessError) => {
          if (err.code) {
            console.error(`Failed to load content for sub window. Cause code: ${err.code}, message: ${err.message}`);
          }
          subWindow.showWindow().then(() => {
            try {
              window.getLastWindow(this.context, (err: BusinessError, data) => {
                const errCode: number = err.code;
                if (errCode) {
                  console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
                  return;
                }
                windowClass = data;
                console.info(`Succeeded in obtaining the top window. Window id: ${windowClass.getWindowProperties().id}`);
              });
            } catch (exception) {
              console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
            }
          });
        });
      });
    });
  }
  //...
}
```

[]()[]()

#### window.getLastWindow9+

getLastWindow(ctx: BaseContext): Promise<Window>

获取当前应用内层级最高的子窗口，使用Promise异步回调。

若无应用子窗口或子窗口未调用[showWindow()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__showwindow9)进行显示，则返回应用主窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明ctx[BaseContext](../graphics/BaseContext.md)是当前应用上下文信息。

**返回值：**

类型说明Promise<[Window](../../types/interfaces/Interface (Window).md)>Promise对象。返回当前应用内层级最高的窗口对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.1300002This window state is abnormal. Top window or main window is null or destroyed.1300006This window context is abnormal.

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      if (err.code) {
        console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
      }
      windowStage.createSubWindow('TestSubWindow').then((subWindow) => {
        let storage: LocalStorage = new LocalStorage();
        subWindow.loadContent('pages/Index', storage, (err: BusinessError) => {
          if (err.code) {
            console.error(`Failed to load content for sub window. Cause code: ${err.code}, message: ${err.message}`);
          }
          subWindow.showWindow().then(() => {
            try {
              window.getLastWindow(this.context).then((topWindow) => {
                windowClass = topWindow;
                console.info(`Succeeded in obtaining the top window. Window id: ${topWindow.getWindowProperties().id}`);
              }).catch((err: BusinessError) => {
                console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
              });
            } catch (exception) {
              console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
            }
          });
        });
      });
    });
  }
  //...
}
```

[]()[]()

#### window.shiftAppWindowFocus11+

shiftAppWindowFocus(sourceWindowId: number, targetWindowId: number): Promise<void>

在同应用内将窗口焦点从源窗口转移到目标窗口，仅支持应用主窗、子窗范围内的焦点转移。使用Promise异步回调。

目标窗口需确保具有获得焦点的能力（可通过[setWindowFocusable()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowfocusable9)设置），并确保调用[showWindow()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__showwindow9)成功且执行完毕。

在调用shiftAppWindowFocus()前，建议确保目标窗口已调用[loadContent()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__loadcontent9)或[setUIContent()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setuicontent9)并生效，否则可能会导致不可见窗口获取焦点，造成功能异常或影响用户体验。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

参数名类型必填说明sourceWindowIdnumber是源窗口id，必须是获焦状态。推荐使用[getWindowProperties()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)方法获取窗口id属性。targetWindowIdnumber是目标窗口id。推荐使用[getWindowProperties()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)方法获取窗口id属性。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported. Failed to call the API due to limited device capabilities.1300002This window state is abnormal.1300003This window manager service works abnormally.1300004Unauthorized operation.

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // ...
    console.info('onWindowStageCreate');
    let mainWindow: window.Window | undefined = undefined;
    let subWindow: window.Window | undefined = undefined;
    let mainWindowId: number = -1;
    let subWindowId: number = -1;

    try {
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
        }
        // 获取应用主窗及ID
        windowStage.getMainWindow().then((data) => {
          if (data == null) {
            console.error('Failed to obtain the main window. Cause: The data is empty');
            return;
          }
          mainWindow = data;
          mainWindowId = mainWindow.getWindowProperties().id;
          console.info('Succeeded in obtaining the main window');
        }).catch((err: BusinessError) => {
          console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        });

        // 创建或获取子窗及ID，此时子窗口获焦
        windowStage.createSubWindow('testSubWindow').then((data) => {
          if (data == null) {
            console.error('Failed to obtain the sub window. Cause: The data is empty');
            return;
          }
          subWindow = data;
          subWindowId = subWindow.getWindowProperties().id;
          subWindow.resize(500, 500);
          subWindow.setUIContent('pages/Index');
          subWindow.showWindow();

          // 监听Window状态，确保已经就绪
          subWindow.on("windowEvent", (windowEvent) => {
            if (windowEvent == window.WindowEventType.WINDOW_ACTIVE) {
              // 切换焦点
              window.shiftAppWindowFocus(subWindowId, mainWindowId).then(() => {
                console.info('Succeeded in shifting app window focus');
              }).catch((err: BusinessError) => {
                console.error(`Failed to shift app window focus. Cause code: ${err.code}, message: ${err.message}`);
              });
            }
          });
        });
      });
    } catch (exception) {
      console.error(`Failed to shift app focus. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```

[]()[]()

#### window.shiftAppWindowPointerEvent15+

shiftAppWindowPointerEvent(sourceWindowId: number, targetWindowId: number): Promise<void>

主窗口和子窗口可正常调用，用于将鼠标输入事件从源窗口转移到目标窗口。使用Promise异步回调。

源窗口仅在[onTouch](../misc/触摸事件.md#ZH-CN_TOPIC_0000002529444777__ontouch)事件（事件类型必须为TouchType.Down）的回调方法中调用此接口才会有鼠标输入事件转移效果，成功调用此接口后，系统会向源窗口补发鼠标按键抬起（TouchType.Up）事件，并且向目标窗口补发鼠标按键按下（TouchType.Down）事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态的设备及不支持[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态的设备上调用返回801错误码。

**参数：**

参数名类型必填说明sourceWindowIdnumber是源窗口id。推荐使用[getWindowProperties()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)方法获取窗口id属性。targetWindowIdnumber是目标窗口id。推荐使用[getWindowProperties()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)方法获取窗口id属性。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported. Failed to call the API due to limited device capabilities.1300002This window state is abnormal.1300003This window manager service works abnormally.1300004Unauthorized operation.

**示例：**

```ets
// ets/pages/Index.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Blue)
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              try {
                let sourceWindowId = 1;
                let targetWindowId = 2;
                let promise = window.shiftAppWindowPointerEvent(sourceWindowId, targetWindowId);
                promise.then(() => {
                  console.info('Succeeded in shifting app window pointer event');
                }).catch((err: BusinessError) => {
                  console.error(`Failed to shift app window pointer event. Cause code: ${err.code}, message: ${err.message}`);
                });
              } catch (exception) {
                console.error(`Failed to shift app pointer event. Cause code: ${exception.code}, message: ${exception.message}`);
              }
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
}
```

[]()[]()

#### window.shiftAppWindowTouchEvent20+

shiftAppWindowTouchEvent(sourceWindowId: number, targetWindowId: number, fingerId: number): Promise<void>

主窗口和子窗口可正常调用，用于将触屏输入事件从源窗口转移到目标窗口。使用Promise异步回调。

源窗口仅在[onTouch](../misc/触摸事件.md#ZH-CN_TOPIC_0000002529444777__ontouch)事件（事件类型必须为TouchType.Down）的回调方法中调用此接口才会有触屏输入事件转移效果，成功调用此接口后，系统会向源窗口补发触屏抬起（TouchType.Up）事件，并且向目标窗口补发触屏按下（TouchType.Down）事件。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态的设备及不支持[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态的设备上调用返回801错误码。

**参数：**

参数名类型必填说明sourceWindowIdnumber是源窗口id。推荐使用[getWindowProperties()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)方法获取窗口id属性。该参数应为大于0的整数，小于等于0时会返回错误码1300016。targetWindowIdnumber是目标窗口id。推荐使用[getWindowProperties()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)方法获取窗口id属性。该参数应为大于0的整数，小于等于0时会返回错误码1300016。fingerIdnumber是触屏事件的手指唯一标识符。推荐使用[TouchEvent](../misc/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)对象中touches属性获取id。该参数应为大于等于0的整数，小于0时会返回错误码1300016。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息801Capability not supported. Function shiftAppWindowTouchEvent can not work correctly due to limited device capabilities.1300002This window state is abnormal.1300003This window manager service works abnormally.1300004Unauthorized operation.1300016Parameter error. Possible cause: 1. Invalid parameter range.

**示例：**

```ets
// ets/pages/Index.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Blue)
          .onTouch((event: TouchEvent) => {
            // 源窗口触屏事件类型必须为TouchType.Down
            if (event.type === TouchType.Down) {
              try {
                let sourceWindowId = 1;
                let targetWindowId = 2;
                let promise = window.shiftAppWindowTouchEvent(sourceWindowId, targetWindowId, event.touches[0].id);
                promise.then(() => {
                  console.info(`Succeeded in shifting app window touch event`);
                }).catch((err: BusinessError) => {
                  console.error(`Failed to shift app window touch event. Cause code: ${err.code}, message: ${err.message}`);
                });
              } catch (exception) {
                console.error(`Failed to shift app touch event. Cause code: ${exception.code}, message: ${exception.message}`);
              }
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
}
```

[]()[]()

#### window.getWindowsByCoordinate14+

getWindowsByCoordinate(displayId: number, windowNumber?: number, x?: number, y?: number): Promise<Array<Window>>

查询本应用指定坐标下的可见窗口数组，按当前窗口层级排列，层级最高的窗口对应数组下标为0，使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

参数名类型必填说明displayIdnumber是查询窗口所在的displayId，该参数应为整数，传入非整数会忽略掉小数部分，可以在窗口属性[WindowProperties](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowproperties)中获取。windowNumbernumber否查询的窗口数量，该参数应为大于0的整数，传入非整数会忽略掉小数部分，未设置或小于等于0返回所有满足条件的窗口。xnumber否查询的x坐标，以屏幕左上角为原点，该参数应为非负整数，传入非整数会忽略掉小数部分，未设置或小于0返回所有可见窗口。ynumber否查询的y坐标，以屏幕左上角为原点，该参数应为非负整数，传入非整数会忽略掉小数部分，未设置或小于0返回所有可见窗口。

**返回值：**

类型说明Promise<Array<[Window](../../types/interfaces/Interface (Window).md)>>Promise对象。返回获取到的窗口对象数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: Incorrect parameter types.801Capability not supported. Failed to call the API due to limited device capabilities.1300003This window manager service works abnormally.

```ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  window.getWindowsByCoordinate(displayId).then((data) => {
    console.info(`Succeeded in getting windows. Data: ${data}`);
    for (let window of data) {
      // do something with window
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get window from point. Cause code: ${err.code}, message: ${err.message}`);
  });
  window.getWindowsByCoordinate(displayId, 2, 500, 500).then((data) => {
    console.info(`Succeeded in getting windows. Data: ${data}`);
    for (let window of data) {
      // do something with window
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get window from point. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get window from point. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

[]()[]()

#### window.getAllWindowLayoutInfo15+

getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>

获取指定屏幕上可见的窗口布局信息数组，按当前窗口层级排列，层级最高的对应数组index为0，使用Promise异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

参数名类型必填说明displayIdnumber是需要获取窗口布局信息的displayId，该参数应为整数，且为当前实际存在屏幕的displayId，可以通过窗口属性[WindowProperties](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowproperties)获取。

**返回值：**

类型说明Promise<Array<[WindowLayoutInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowlayoutinfo15)>>Promise对象。返回获取到的窗口布局信息对象数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported. function getAllWindowLayoutInfo can not work correctly due to limited device capabilities.1300003This window manager service works abnormally.

```ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  let promise = window.getAllWindowLayoutInfo(displayId);
  promise.then((data) => {
    console.info('Succeeded in obtaining all window layout info. Data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to obtain all window layout info. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to obtain all window layout info. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

[]()[]()

#### window.getVisibleWindowInfo18+

getVisibleWindowInfo(): Promise<Array<WindowInfo>>

获取当前屏幕的可见主窗口（未退至后台的主窗口）信息。使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**需要权限：** ohos.permission.VISIBLE_WINDOW_INFO

**返回值：**

类型说明Promise<Array<[WindowInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowinfo18)>>Promise对象，返回当前可见窗口的相关信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Function getVisibleWindowInfo can not work correctly due to limited device capabilities.1300003This window manager service works abnormally.

**示例：**

```ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = window.getVisibleWindowInfo();
  promise.then((data) => {
    data.forEach(windowInfo=>{
      console.info(`left:${windowInfo.rect.left}`);
      console.info(`top:${windowInfo.rect.top}`);
      console.info(`width:${windowInfo.rect.width}`);
      console.info(`height:${windowInfo.rect.height}`);
      console.info(`windowId:${windowInfo.windowId}`);
      console.info(`windowStatusType:${windowInfo.windowStatusType}`);
      console.info(`abilityName:${windowInfo.abilityName}`);
      console.info(`bundleName:${windowInfo.bundleName}`);
      console.info(`isFocused:${windowInfo.isFocused}`);
    })
  }).catch((err: BusinessError) => {
    console.error('Failed to getWindowInfo. Cause: ' + JSON.stringify(err));
  });
} catch (exception) {
  console.error(`Failed to get visible window info. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

[]()[]()

#### window.getGlobalWindowMode20+

getGlobalWindowMode(displayId?: number): Promise<number>

获取指定屏幕上生命周期位于前台的窗口对应的窗口模式，使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

参数名类型必填说明displayIdnumber否可选的屏幕ID，用于获取对应屏幕上的窗口模式信息。该参数应为大于等于0的整数，小于0时会返回错误码1300016，不传或传值为null以及undefined则代表查询所有屏幕，传入非整数会忽略掉小数部分。如果指定的屏幕不存在，返回值为0，推荐使用[getWindowProperties()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)方法获取窗口所在屏幕ID属性。

**返回值：**

类型说明Promise<number>Promise对象。返回获取到的窗口模式。每一个二进制位代表一种窗口模式，当前支持的窗口模式见[GlobalWindowMode](Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__globalwindowmode20)，返回值为对应窗口模式值按位进行或运算的结果。比如，当前屏幕上存在全屏窗口、悬浮窗和画中画三种窗口，则返回值为0b1|0b100|0b1000 = 13。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息801Capability not supported. function getGlobalWindowMode can not work correctly due to limited device capabilities.1300003This window manager service works abnormally.1300016Parameter error. Possible cause: 1. Invalid parameter range.

**示例：**

```ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  let promise = window.getGlobalWindowMode(displayId);
  promise.then((data) => {
    console.info(`Succeeded in obtaining global window mode. Data: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to obtain global window mode. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to obtain global window mode. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

[]()[]()

#### window.setWatermarkImageForAppWindows21+

setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>

设置或取消本应用进程下窗口的水印图片，使用Promise异步回调。该接口需要在[loadContent()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__loadcontent9)或[setUIContent()](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

参数名类型必填说明pixelMap[image.PixelMap](../../types/interfaces/Interface (PixelMap).md) | undefined是

传入image.PixelMap表示设置水印图片，传入undefined表示取消水印显示。

如果图片尺寸的宽和高同时超过窗口尺寸以及屏幕尺寸的宽和高，返回错误码1300016。

如果图片尺寸的宽或高超过窗口尺寸的宽或高，超出窗口宽或高的部分会被裁剪。

如果图片尺寸的宽或高小于窗口尺寸的宽或高，小于的部分会自动重复补充。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码 ID错误信息801Capability not supported. Function setWatermarkImageForAppWindows can not to work correctly due to limited device capabilities.1300003This window manager service works abnormally.1300016Parameter error. Possible cause: 1. Invalid parameter range.

**示例：**

```ets
import { image } from "@kit.ImageKit";
import { BusinessError } from "@kit.BasicServicesKit";

let color: ArrayBuffer = new ArrayBuffer(96);
let initializationOptions: image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.RGBA_8888,
  size: {
    height: 4,
    width: 6,
  },
};
image.createPixelMap(color, initializationOptions).then((pixelMap: image.PixelMap) => {
  console.info("Succeeded in creating pixelmap.");
  try {
    let promise = window.setWatermarkImageForAppWindows(pixelMap);
    promise.then(() => {
        console.info("Succeeded in setting watermark image.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to set watermark image. Cause code: ${err.code}, message: ${err.message}`);
    });
  } catch (exception) {
    console.error(`Failed to set watermark image. Exception code: ${exception.code}, message: ${exception.message}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to create PixelMap. Cause code: ${err.code}, message: ${err.message}`);
});
```

[]()[]()

#### window.setStartWindowBackgroundColor20+

setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>

设置同一应用包名下指定moduleName、abilityName对应UIAbility的启动页背景色，使用Promise异步回调。

该接口对同一应用包名下的所有进程生效，例如多实例或应用分身场景。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

参数名类型必填说明moduleNamestring是需要设置的UIAbility所属模块名，moduleName的长度范围为0-200字节，仅支持设置当前同一应用包名内的模块。模块名由开发者在[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#配置文件标签)中的name字段指定。abilityNamestring是需要设置的UIAbility名字，abilityName的长度范围为0-200字节，仅支持设置当前同一应用包名内的abilityName。UIAbility名由开发者在[module.json5配置文件abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)的name字段指定。color[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)是设置的启动页背景色。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息801Capability not supported.function setStartWindowBackgroundColor can not to work correctly due to limited device capabilities.1300003This window manager service works abnormally.1300016Parameter error. Possible cause: 1. Invalid parameter range.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics, window } from '@kit.ArkUI';

try {
  let promise = window.setStartWindowBackgroundColor("entry", "EntryAbility", ColorMetrics.numeric(0xff000000));
  promise.then(() => {
    console.info('Succeeded in setting the starting window color.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the starting window color. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the starting window color. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

[]()[]()

#### window.getAllMainWindowInfo21+

getAllMainWindowInfo(): Promise<Array<MainWindowInfo>>

获取全部主窗口信息，使用Promise异步回调。

**需要权限：** ohos.permission.CUSTOM_SCREEN_CAPTURE

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

类型说明Promise<Array<[MainWindowInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__mainwindowinfo21)>>Promise对象。返回主窗口信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息201Permission verification failed.801Capability not supported. Failed to call the API due to limited device capabilities.1300003This window manager service works abnormally.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, UIAbility, common, Permissions } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error(`Failed to load the content. Cause: ${JSON.stringify(err)}`);
      }
      reqPermissionsFromUser(permissions, this.context);
      console.info('Succeeded in loading the content');
    });
    try {
      let windowInfoPromise = window.getAllMainWindowInfo();
      windowInfoPromise.then((list: Array<window.MainWindowInfo>) => {
        console.info('Get all main window info success.');
      }).catch((err: BusinessError) => {
        console.error(`Get all main window info failed. Error info: ${JSON.stringify(err)}`);
      });
    } catch (err) {
      console.error(`Get all main window info failed. Cause info: ${JSON.stringify(err)}`);
    }
  }
}

const permissions: Array<Permissions> = ['ohos.permission.CUSTOM_SCREEN_CAPTURE'];
function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions).then((data) => {
    console.info('requestPermissionsFromUser');
    let grantStatus: Array<number> = data.authResults;
    let length: number = grantStatus.length;
    for (let i = 0; i < length; i++) {
      if (grantStatus[i] === 0) {
        // 用户授权
      } else {
        // 用户拒绝授权
        return;
      }
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to request permission from user. Code is ${err.code}, message is ${err.message}`);
  })
}
```

[]()[]()

#### window.getMainWindowSnapshot21+

getMainWindowSnapshot(windowId: Array<number>, config: WindowSnapshotConfiguration): Promise<Array<image.PixelMap | undefined>>

获取一个或多个指定windowId的主窗口截图，使用Promise异步回调。

**需要权限：** ohos.permission.CUSTOM_SCREEN_CAPTURE

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

参数名类型必填说明windowIdArray<number>是需要获取截图的主窗口ID列表。可通过[window.getAllMainWindowInfo()](#ZH-CN_TOPIC_0000002529444767__windowgetallmainwindowinfo21)获取到主窗口windowId。当windowId为null、undefined、小于0、存在重复值或数量超过512个时，返回错误码401；当windowId大于0但不存在对应窗口时，返回undefined。config[WindowSnapshotConfiguration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowsnapshotconfiguration21)是获取窗口截图时的配置信息。

**返回值：**

类型说明Promise<Array<[image.PixelMap](../../types/interfaces/Interface (PixelMap).md) | undefined>>Promise对象。截图的PixelMap列表，按传入的窗口ID数组的顺序排列。当窗口ID合法但无法找到对应的主窗口时，返回undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[窗口错误码](../../errors/窗口错误码.md)。

错误码ID错误信息201Permission verification failed.801Capability not supported. Failed to call the API due to limited device capabilities.1300003This window manager service works abnormally.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, UIAbility, common, Permissions } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error(`Failed to load the content. Cause: JSON.stringify(err)`);
      }
      reqPermissionsFromUser(permissions, this.context);
      console.info('Success in loading the content');
    });
    try {
      let windowIds: number[] = [];
      let configs: window.WindowSnapshotConfiguration = {
        useCache: false
      }
      let windowInfoPromise = window.getAllMainWindowInfo();
      windowInfoPromise.then((mainWindowInfoList: Array<window.MainWindowInfo>) => {
        for (let i = 0; i < mainWindowInfoList.length; i++) {
          windowIds[i] = mainWindowInfoList[i].windowId;
        }
        let promise = window.getMainWindowSnapshot(windowIds, configs);
        promise.then((list: Array<image.PixelMap | undefined>) => {
          for (let i = 0; i < list.length; i++) {
            console.info(`Get main window snapshot, getBytesNumberPerRow: ${list[i]?.getBytesNumberPerRow()}`);
          }
        }).catch((err: BusinessError) => {
          console.error(`Get main window snapshot failed. Error info: ${JSON.stringify(err)}`);
        });
      }).catch((err: BusinessError) => {
        console.error(`Get all main window info failed. Error info: ${JSON.stringify(err)}`);
      });
    } catch (err) {
      console.error(`Get all main window info failed. Cause info: ${JSON.stringify(err)}`);
    }
  }
}

const permissions: Array<Permissions> = ['ohos.permission.CUSTOM_SCREEN_CAPTURE'];
function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions).then((data) => {
    console.info('requestPermissionsFromUser');
    let grantStatus: Array<number> = data.authResults;
    let length: number = grantStatus.length;
    for (let i = 0; i < length; i++) {
      if (grantStatus[i] === 0) {
        // 用户授权
      } else {
        // 用户拒绝授权
        return;
      }
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to request permission from user. Code is ${err.code}, message is ${err.message}`);
  })
}
```

[]()[]()

#### window.create(deprecated)

create(id: string, type: WindowType, callback: AsyncCallback<Window>): void

创建子窗口，使用callback异步回调。

子窗口创建后默认是[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)。

从API version 7开始支持，从API version 9开始废弃，推荐使用[createWindow()](#ZH-CN_TOPIC_0000002529444767__windowcreatewindow9)。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明idstring是窗口名字，即[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)中的name。type[WindowType](Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowtype7)是窗口类型。callbackAsyncCallback<[Window](../../types/interfaces/Interface (Window).md)>是回调函数。返回当前创建的子窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.create('test', window.WindowType.TYPE_APP, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
});
```

[]()[]()

#### window.create(deprecated)

create(id: string, type: WindowType): Promise<Window>

创建子窗口，使用Promise异步回调。

子窗口创建后默认是[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)。

从API version 7开始支持，从API version 9开始废弃，推荐使用[createWindow()](#ZH-CN_TOPIC_0000002529444767__windowcreatewindow9-1)。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明idstring是窗口名字，即[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)中的name。type[WindowType](Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowtype7)是窗口类型。

**返回值：**

类型说明Promise<[Window](../../types/interfaces/Interface (Window).md)>Promise对象。返回当前创建的子窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.create('test', window.WindowType.TYPE_APP);
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}`);
});
```

[]()[]()

#### window.create(deprecated)

create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void

创建系统窗口，使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃，推荐使用[createWindow()](#ZH-CN_TOPIC_0000002529444767__windowcreatewindow9)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明ctx[BaseContext](../graphics/BaseContext.md)是当前应用上下文信息。idstring是窗口名字，即[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)中的name。type[WindowType](Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowtype7)是窗口类型。callbackAsyncCallback<[Window](../../types/interfaces/Interface (Window).md)>是回调函数。返回当前创建的子窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.create(globalThis.getContext(), 'test', window.WindowType.TYPE_SYSTEM_ALERT, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
  windowClass.resetSize(500, 1000);
});
```

[]()[]()

#### window.create(deprecated)

create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>

创建系统窗口，使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃，推荐使用[createWindow()](#ZH-CN_TOPIC_0000002529444767__windowcreatewindow9-1)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明ctx[BaseContext](../graphics/BaseContext.md)是当前应用上下文信息。idstring是窗口名字，即[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)中的name。type[WindowType](Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowtype7)是窗口类型。

**返回值：**

类型说明Promise<[Window](../../types/interfaces/Interface (Window).md)>Promise对象。返回当前创建的子窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.create(globalThis.getContext(), 'test', window.WindowType.TYPE_SYSTEM_ALERT);
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to create the Window. Cause code: ${err.code}, message: ${err.message}`);
});
```

[]()[]()

#### window.find(deprecated)

find(id: string, callback: AsyncCallback<Window>): void

查找id所对应的窗口，使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃，推荐使用[findWindow()](#ZH-CN_TOPIC_0000002529444767__windowfindwindow9)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明idstring是窗口名字，即[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)中的name。callbackAsyncCallback<[Window](../../types/interfaces/Interface (Window).md)>是回调函数。返回当前查找到的窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.find('test', (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
});
```

[]()[]()

#### window.find(deprecated)

find(id: string): Promise<Window>

查找id所对应的窗口，使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃，推荐使用[findWindow()](#ZH-CN_TOPIC_0000002529444767__windowfindwindow9)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明idstring是窗口名字，即[Configuration](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__configuration9)中的name。

**返回值：**

类型说明Promise<[Window](../../types/interfaces/Interface (Window).md)>Promise对象。返回当前查找的窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.find('test');
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}`);
});
```

[]()[]()

#### window.getTopWindow(deprecated)

getTopWindow(callback: AsyncCallback<Window>): void

获取当前应用内最后显示的窗口，使用callback异步回调。

从API version 6开始支持，从API version 9开始废弃，推荐使用[getLastWindow()](#ZH-CN_TOPIC_0000002529444767__windowgetlastwindow9)。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[Window](../../types/interfaces/Interface (Window).md)>是回调函数。返回当前应用内最后显示的窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.getTopWindow((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
});
```

[]()[]()

#### window.getTopWindow(deprecated)

getTopWindow(): Promise<Window>

获取当前应用内最后显示的窗口，使用Promise异步回调。

从API version 6开始支持，从API version 9开始废弃，推荐使用[getLastWindow()](#ZH-CN_TOPIC_0000002529444767__windowgetlastwindow9-1)。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

类型说明Promise<[Window](../../types/interfaces/Interface (Window).md)>Promise对象。返回当前应用内最后显示的窗口对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.getTopWindow();
promise.then((data)=> {
    windowClass = data;
    console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError)=>{
    console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
});
```

[]()[]()

#### window.getTopWindow(deprecated)

getTopWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void

获取当前应用内最后显示的窗口，使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃，推荐使用[getLastWindow()](#ZH-CN_TOPIC_0000002529444767__windowgetlastwindow9)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明ctx[BaseContext](../graphics/BaseContext.md)是当前应用上下文信息。callbackAsyncCallback<[Window](../../types/interfaces/Interface (Window).md)>是回调函数。返回当前应用内最后显示的窗口对象。

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage:window.WindowStage){
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    try {
      window.getTopWindow(this.context, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if(errCode){
          console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
          return ;
        }
        windowClass = data;
        console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
      });
    } catch(error){
      console.error(`Failed to obtain the top window. Cause code: ${error.code}, message: ${error.message}`);
    }
  }
}
```

[]()[]()

#### window.getTopWindow(deprecated)

getTopWindow(ctx: BaseContext): Promise<Window>

获取当前应用内最后显示的窗口，使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，推荐使用[getLastWindow()](#ZH-CN_TOPIC_0000002529444767__windowgetlastwindow9-1)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

参数名类型必填说明ctx[BaseContext](../graphics/BaseContext.md)是当前应用上下文信息。

**返回值：**

类型说明Promise<[Window](../../types/interfaces/Interface (Window).md)>Promise对象。返回当前应用内最后显示的窗口对象。

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage:window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    let promise = window.getTopWindow(this.context);
    promise.then((data) => {
      windowClass = data;
      console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
    }).catch((error: BusinessError) => {
      console.error(`Failed to obtain the top window. Cause code: ${error.code}, message: ${error.message}`);
    });
  }
}
```