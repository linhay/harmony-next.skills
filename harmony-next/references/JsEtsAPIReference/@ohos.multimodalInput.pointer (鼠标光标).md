# @ohos.multimodalInput.pointer (鼠标光标)

本模块提供鼠标光标管理能力，包括查询、设置鼠标光标属性。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { pointer } from '@kit.InputKit';
```

#### pointer.setPointerVisible

setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void

设置当前窗口的鼠标光标是否显示，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明visibleboolean是当前窗口鼠标光标是否显示。true表示显示，false表示不显示。callbackAsyncCallback<void>是回调函数。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisible(true, (error: BusinessError) => {
              if (error) {
                console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Set pointer visible success`);
            });
          } catch (error) {
            console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.setPointerVisible

setPointerVisible(visible: boolean): Promise<void>

设置当前窗口的鼠标光标是否显示，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明visibleboolean是当前窗口鼠标光标是否显示。true表示显示，false表示不显示。

**返回值**：

类型说明Promise<void>Promise对象，无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisible(false).then(() => {
              console.info(`Set pointer visible success`);
            }).catch((error: BusinessError) => {
              console.error(`Set pointer failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.setPointerVisibleSync10+

setPointerVisibleSync(visible: boolean): void

设置当前窗口鼠标光标的显示状态，使用同步方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明visibleboolean是当前窗口鼠标光标是否显示。true表示显示，false表示不显示。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisibleSync(false);
            console.info(`Set pointer visible success`);
          } catch (error) {
            console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.isPointerVisible

isPointerVisible(callback: AsyncCallback<boolean>): void

获取鼠标光标显示状态，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数，返回鼠标光标状态，true为显示，false为隐藏。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.isPointerVisible((error: BusinessError, visible: boolean) => {
              if (error) {
                console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
            });
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.isPointerVisible

isPointerVisible(): Promise<boolean>

获取鼠标光标显示状态，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**返回值**：

类型说明Promise<boolean>Promise对象，返回鼠标光标状态查询结果。true代表显示状态，false代表隐藏状态。

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.isPointerVisible().then((visible: boolean) => {
              console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get pointer failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.isPointerVisibleSync10+

isPointerVisibleSync(): boolean

获取当前窗口鼠标光标的显示状态，使用同步方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**返回值**：

类型说明boolean返回鼠标光标显示或隐藏状态。true代表显示状态，false代表隐藏状态。

**示例**：

```ets
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let visible: boolean = pointer.isPointerVisibleSync();
            console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.getPointerStyle

getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void

获取指定窗口的鼠标样式类型，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是

窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。

窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。

如果通过[setPointerStyle](#ZH-CN_TOPIC_0000002529285561__pointersetpointerstyle)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。

callbackAsyncCallback<[PointerStyle](#ZH-CN_TOPIC_0000002529285561__pointerstyle)>是回调函数，返回鼠标样式类型。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.getPointerStyle(windowId, (error: Error, style: pointer.PointerStyle) => {
                console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
              });
            } catch (error) {
              console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.getPointerStyle

getPointerStyle(windowId: number): Promise<PointerStyle>

获取鼠标样式类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是

窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。

窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。

如果通过[setPointerStyle](#ZH-CN_TOPIC_0000002529285561__pointersetpointerstyle-1)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。

**返回值**：

类型说明Promise<[PointerStyle](#ZH-CN_TOPIC_0000002529285561__pointerstyle)>Promise对象，返回鼠标样式类型。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.getPointerStyle(windowId).then((style: pointer.PointerStyle) => {
                console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
              });
            } catch (error) {
              console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.getPointerStyleSync10+

getPointerStyleSync(windowId: number): PointerStyle

查询指定窗口的鼠标样式类型，如向东箭头、向西箭头、向南箭头、向北箭头等。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是

窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。

窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。

如果通过[setPointerStyleSync](#ZH-CN_TOPIC_0000002529285561__pointersetpointerstylesync10)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。

**返回值**：

类型说明[PointerStyle](#ZH-CN_TOPIC_0000002529285561__pointerstyle)返回鼠标样式类型。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let windowId = -1;
          try {
            let style: pointer.PointerStyle = pointer.getPointerStyleSync(windowId);
            console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
          } catch (error) {
            console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.setPointerStyle

setPointerStyle(windowId: number, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void

设置指定窗口的鼠标样式类型，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是

窗口ID。取值范围为大于等于0的整数。

窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。

设置结果可通过[getPointerStyle](#ZH-CN_TOPIC_0000002529285561__pointergetpointerstyle)获取。

pointerStyle[PointerStyle](#ZH-CN_TOPIC_0000002529285561__pointerstyle)是鼠标样式。callbackAsyncCallback<void>是回调函数。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS, error => {
                console.info(`Set pointer style success`);
              });
            } catch (error) {
              console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.setPointerStyle

setPointerStyle(windowId: number, pointerStyle: PointerStyle): Promise<void>

设置指定窗口的鼠标样式类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是

窗口ID。取值范围为大于等于0的整数。

窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。

设置结果可通过[getPointerStyle](#ZH-CN_TOPIC_0000002529285561__pointergetpointerstyle-1)获取。

pointerStyle[PointerStyle](#ZH-CN_TOPIC_0000002529285561__pointerstyle)是鼠标样式。

**返回值**：

类型说明Promise<void>Promise对象，无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS).then(() => {
                console.info(`Set pointer style success`);
              });
            } catch (error) {
              console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.setPointerStyleSync10+

setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void

设置指定窗口的鼠标样式类型，使用同步方式返回结果。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是

窗口ID。取值范围为大于等于0的整数。

窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。

设置结果可通过[getPointerStyleSync](#ZH-CN_TOPIC_0000002529285561__pointergetpointerstylesync10)获取。

pointerStyle[PointerStyle](#ZH-CN_TOPIC_0000002529285561__pointerstyle)是鼠标样式。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyleSync(windowId, pointer.PointerStyle.CROSS);
              console.info(`Set pointer style success`);
            } catch (error) {
              console.error(`getPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### PrimaryButton10+

鼠标主键类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

名称值说明LEFT0鼠标左键。RIGHT1鼠标右键。

#### RightClickType10+

右键菜单的触发方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

名称值说明TOUCHPAD_RIGHT_BUTTON1按压触控板右键区域。TOUCHPAD_LEFT_BUTTON2按压触控板左键区域。TOUCHPAD_TWO_FINGER_TAP3双指轻击或双指按压触控板。TOUCHPAD_TWO_FINGER_TAP_OR_RIGHT_BUTTON20+4双指轻击或双指按压触控板、或按压触控板右键区域。TOUCHPAD_TWO_FINGER_TAP_OR_LEFT_BUTTON20+5双指轻击或双指按压触控板、或按压触控板左键区域。

#### PointerStyle

鼠标光标样式类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

名称值说明图示DEFAULT0默认EAST1向东箭头WEST2向西箭头SOUTH3向南箭头NORTH4向北箭头WEST_EAST5向西东箭头NORTH_SOUTH6向北南箭头NORTH_EAST7向东北箭头NORTH_WEST8向西北箭头SOUTH_EAST9向东南箭头SOUTH_WEST10向西南箭头NORTH_EAST_SOUTH_WEST11东北西南调整NORTH_WEST_SOUTH_EAST12西北东南调整CROSS13准确选择CURSOR_COPY14拷贝CURSOR_FORBID15不可用COLOR_SUCKER16滴管HAND_GRABBING17并拢的手HAND_OPEN18张开的手HAND_POINTING19手形指针HELP20帮助选择MOVE21移动RESIZE_LEFT_RIGHT22内部左右调整RESIZE_UP_DOWN23内部上下调整SCREENSHOT_CHOOSE24截图十字准星SCREENSHOT_CURSOR25截图TEXT_CURSOR26文本选择ZOOM_IN27放大ZOOM_OUT28缩小MIDDLE_BTN_EAST29向东滚动MIDDLE_BTN_WEST30向西滚动MIDDLE_BTN_SOUTH31向南滚动MIDDLE_BTN_NORTH32向北滚动MIDDLE_BTN_NORTH_SOUTH33向南北滚动MIDDLE_BTN_NORTH_EAST34向东北滚动MIDDLE_BTN_NORTH_WEST35向西北滚动MIDDLE_BTN_SOUTH_EAST36向东南滚动MIDDLE_BTN_SOUTH_WEST37向西南滚动MIDDLE_BTN_NORTH_SOUTH_WEST_EAST38四向锥形移动HORIZONTAL_TEXT_CURSOR10+39垂直文本选择CURSOR_CROSS10+40十字光标CURSOR_CIRCLE10+41圆形光标LOADING10+42

正在载入动画光标

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

RUNNING10+43

后台运行中动画光标

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MIDDLE_BTN_EAST_WEST18+44向东西滚动RUNNING_LEFT22+45后台运行中动画光标(拓展1)RUNNING_RIGHT22+46后台运行中动画光标(拓展2)AECH_DEVELOPER_DEFINED_ICON22+47圆形自定义光标SCREENRECORDER_CURSOR20+48录屏光标LASER_CURSOR22+49

悬浮光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

LASER_CURSOR_DOT22+50

点击光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

LASER_CURSOR_DOT_RED22+51

激光笔光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

DEVELOPER_DEFINED_ICON22+-100自定义光标，开发者可使用[setCustomCursor](#ZH-CN_TOPIC_0000002529285561__pointersetcustomcursor15)设置自定义光标，不支持使用[setPointerStyle](#ZH-CN_TOPIC_0000002529285561__pointersetpointerstyle-1)直接设置。自定义光标样式，通过接口设置。

#### pointer.setCustomCursor11+

setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>

设置指定窗口的自定义光标样式，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是窗口ID。pixelMap[image.PixelMap](Interface (PixelMap).md)是自定义光标资源。focusXnumber否自定义光标焦点x，取值范围：大于等于0，默认为0。focusYnumber否自定义光标焦点y，取值范围：大于等于0，默认为0。

**返回值**：

类型说明Promise<void>Promise对象，无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon为示例资源，请开发者根据实际需求配置资源文件。
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, pixelMap).then(() => {
                    console.info(`setCustomCursor success`);
                  });
                } catch (error) {
                  console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            });
          });
        })
    }
  }
}
```

#### CustomCursor15+

自定义光标资源。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

名称类型只读可选说明pixelMap[image.PixelMap](Interface (PixelMap).md)否否自定义光标。最小限制为资源图本身的最小限制。最大限制为256 x 256px。focusXnumber否是自定义光标焦点的水平坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的宽度最大值，该参数缺省时默认为0。focusYnumber否是自定义光标焦点的垂直坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的高度最大值，该参数缺省时默认为0。

#### CursorConfig15+

自定义光标配置。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

名称类型只读可选说明followSystemboolean否否是否根据系统设置调整光标大小。false表示使用自定义光标样式大小，true表示根据系统设置调整光标大小，可调整范围为：[光标资源图大小，256×256]。

#### pointer.setCustomCursor15+

setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>

设置指定窗口的自定义光标样式，使用Promise异步回调。

应用窗口布局改变、热区切换、页面跳转、光标移出再回到窗口、光标在窗口不同区域移动，以上场景可能导致光标切换回系统样式，需要开发者重新设置光标样式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是窗口ID。cursor[CustomCursor](@ohos.multimodalInput.pointer (鼠标光标).md#ZH-CN_TOPIC_0000002529285561__customcursor15)是自定义光标资源。config[CursorConfig](@ohos.multimodalInput.pointer (鼠标光标).md#ZH-CN_TOPIC_0000002529285561__cursorconfig15)是自定义光标配置，用于配置是否根据系统设置调整光标大小。如果CursorConfig中followSystem设置为true，则光标大小的可调整范围为：[光标资源图大小，256×256]。

**返回值**：

类型说明Promise<void>Promise对象，无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[输入设备错误码](输入设备错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Abnormal windowId parameter passed in. 2. Abnormal pixelMap parameter passed in; 3. Abnormal focusX parameter passed in.4. Abnormal focusY parameter passed in.26500001Invalid windowId. Possible causes: The window id does not belong to the current process.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon为示例资源，请开发者根据实际需求配置资源文件。
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, { pixelMap: pixelMap, focusX: 25, focusY: 25 },
                    { followSystem: false }).then(() => {
                    console.info(`setCustomCursor success`);
                  });
                } catch (error) {
                  console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            });
          });
        })
    }
  }
}
```

#### pointer.setCustomCursorSync11+

setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void

设置指定窗口的自定义光标样式，使用同步方式进行设置。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

参数名类型必填说明windowIdnumber是窗口ID。取值为大于0的整数。pixelMap[image.PixelMap](Interface (PixelMap).md)是自定义光标资源。focusXnumber否自定义光标焦点x，取值范围：大于等于0，默认为0。focusYnumber否自定义光标焦点y，取值范围：大于等于0，默认为0。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon为示例资源，请开发者根据实际需求配置资源文件。
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursorSync(windowId, pixelMap, 25, 25);
                  console.info(`setCustomCursorSync success`);
                } catch (error) {
                  console.error(`setCustomCursorSync failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            });
          });
        })
    }
  }
}
```