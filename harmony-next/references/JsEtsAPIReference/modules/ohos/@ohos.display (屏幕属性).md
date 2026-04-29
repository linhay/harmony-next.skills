# @ohos.display (屏幕属性)

屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { display } from '@kit.ArkUI';
```

#### DisplayState

显示设备的状态枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_UNKNOWN | 0 | 表示显示设备状态未知。 |
| STATE_OFF | 1 | 表示显示设备状态为关闭。 |
| STATE_ON | 2 | 表示显示设备状态为开启。 |
| STATE_DOZE | 3 | 表示显示设备为低电耗模式。 |
| STATE_DOZE_SUSPEND | 4 | 表示显示设备为睡眠模式，CPU为挂起状态。 |
| STATE_VR | 5 | 表示显示设备为VR模式。 |
| STATE_ON_SUSPEND | 6 | 表示显示设备为开启状态，CPU为挂起状态。 |

#### Orientation10+

显示设备当前显示的方向枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PORTRAIT | 0 | 表示设备当前以竖屏方式显示。 |
| LANDSCAPE | 1 | 表示设备当前以横屏方式显示。 |
| PORTRAIT_INVERTED | 2 | 表示设备当前以反向竖屏方式显示。 |
| LANDSCAPE_INVERTED | 3 | 表示设备当前以反向横屏方式显示。 |

#### DisplaySourceMode19+

屏幕显示内容的显示模式枚举。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示设备当前未使用。 |
| MAIN | 1 | 表示设备当前为主屏。 |
| MIRROR | 2 | 表示设备当前为镜像显示模式。 |
| EXTEND | 3 | 表示设备当前为扩展显示模式。 |
| ALONE | 4 | 表示设备当前为异源显示模式。 |

#### FoldStatus10+

当前可折叠设备的折叠状态枚举。如果是双折轴设备，则在充电口朝下的状态下，从右到左分别是折轴一和折轴二。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLD_STATUS_UNKNOWN | 0 | 表示设备当前折叠状态无法确定或设备本身不可折叠。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_EXPANDED | 1 | 表示设备当前折叠状态为完全展开。如果是双折轴设备，则表示折轴一折叠状态为完全展开，折轴二折叠状态为折叠。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_FOLDED | 2 | 表示设备当前折叠状态为折叠。如果是双折轴设备，则表示折轴一和折轴二的折叠状态均为折叠。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_HALF_FOLDED | 3 | 表示设备当前折叠状态为半折叠。半折叠指完全展开和折叠之间的状态。如果是双折轴设备，则表示折轴一折叠状态为半折叠，折轴二折叠状态为折叠。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_EXPANDED_WITH_SECOND_EXPANDED15+ | 11 | 表示双折轴设备折轴一和折轴二的折叠状态均为完全展开。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED15+ | 21 | 表示双折轴设备折轴一折叠状态为完全展开，折轴二折叠状态为半折叠。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED15+ | 12 | 表示双折轴设备折轴一折叠状态为折叠，折轴二折叠状态为完全展开。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_FOLDED_WITH_SECOND_HALF_FOLDED15+ | 22 | 表示双折轴设备折轴一折叠状态为折叠，折轴二折叠状态为半折叠。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_HALF_FOLDED_WITH_SECOND_EXPANDED15+ | 13 | 表示双折轴设备折轴一折叠状态为半折叠，折轴二折叠状态为完全展开。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| FOLD_STATUS_HALF_FOLDED_WITH_SECOND_HALF_FOLDED15+ | 23 | 表示双折轴设备折轴一和折轴二的折叠状态均为半折叠。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |


只有一个折轴的产品包含FOLD_STATUS_EXPANDED、FOLD_STATUS_FOLDED、FOLD_STATUS_HALF_FOLDED三种折叠状态。

具有两个折轴的产品包含上表除FOLD_STATUS_UNKNOWN以外的九种折叠状态。

FOLD_STATUS_UNKNOWN是一种不可用的折叠状态。

#### FoldDisplayMode10+

可折叠设备的显示模式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLD_DISPLAY_MODE_UNKNOWN | 0 | 表示设备当前折叠显示模式未知。 |
| FOLD_DISPLAY_MODE_FULL | 1 | 表示设备当前全屏显示。 |
| FOLD_DISPLAY_MODE_MAIN | 2 | 表示设备当前主屏幕显示。 |
| FOLD_DISPLAY_MODE_SUB | 3 | 表示设备当前子屏幕显示。 |
| FOLD_DISPLAY_MODE_COORDINATION | 4 | 表示设备当前双屏协同显示。 |


• 对于内外屏均可作为主屏幕使用的折叠产品，例如大折叠、阔折叠，内屏显示状态为FOLD_DISPLAY_MODE_FULL，外屏显示状态为FOLD_DISPLAY_MODE_MAIN。

• 对于外屏只有简单的辅助显示作用的折叠产品，例如小折叠，内屏显示状态为FOLD_DISPLAY_MODE_MAIN，外屏显示状态为FOLD_DISPLAY_MODE_SUB。

**CornerType23+**

屏幕圆角类型枚举。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP_LEFT | 0 | 屏幕左上方的圆角。 |
| TOP_RIGHT | 1 | 屏幕右上方的圆角。 |
| BOTTOM_RIGHT | 2 | 屏幕右下方的圆角。 |
| BOTTOM_LEFT | 3 | 屏幕左下方的圆角。 |

**RoundedCorner23+**

屏幕圆角定义。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | CornerType | 是 | 否 | 圆角类型。 |
| position | Position | 是 | 否 | 圆角圆心的坐标点。 |
| radius | number | 是 | 否 | 圆角半径，单位为px。 |

#### FoldCreaseRegion10+

折叠折痕区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| displayId | number | 是 | 否 | 屏幕ID，用于识别折痕所在的屏幕。 |
| creaseRects | Array<Rect> | 是 | 否 | 折痕区域。 |

#### Rect9+

矩形区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 矩形区域的左边界，单位为px，该参数为整数。 |
| top | number | 否 | 否 | 矩形区域的上边界，单位为px，该参数为整数。 |
| width | number | 否 | 否 | 矩形区域的宽度，单位为px，该参数为整数。 |
| height | number | 否 | 否 | 矩形区域的高度，单位为px，该参数为整数。 |

#### WaterfallDisplayAreaRects9+

瀑布屏曲面部分显示区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | Rect | 是 | 否 | 瀑布曲面区域的左侧矩形区域。 |
| top | Rect | 是 | 否 | 瀑布曲面区域的顶部矩形区域。 |
| right | Rect | 是 | 否 | 瀑布曲面区域的右侧矩形区域。 |
| bottom | Rect | 是 | 否 | 瀑布曲面区域的底部矩形区域。 |

#### CutoutInfo9+

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| boundingRects | Array<Rect> | 是 | 否 | 挖孔、刘海等区域的边界矩形。如果没有挖孔、刘海等区域，数组返回为空。 |
| waterfallDisplayAreaRects | WaterfallDisplayAreaRects | 是 | 否 | 瀑布屏曲面部分显示区域。 |

#### DisplayPhysicalResolution12+

设备的显示模式以及对应的物理屏幕分辨率信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| foldDisplayMode | FoldDisplayMode | 是 | 否 | 设备的显示模式，非折叠设备时值为0。 |
| physicalWidth | number | 是 | 否 | 设备的宽度，单位为px，该参数为大于0的整数。 |
| physicalHeight | number | 是 | 否 | 设备的高度，单位为px，该参数为大于0的整数。 |

#### BrightnessInfo22+

屏幕亮度信息。此类型中的信息均来自底层屏幕信息数据。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentHeadroom | number | 是 | 否 | 当前亮度动态余量，该参数为大于0的浮点数。默认值为1.0。 |
| maxHeadroom | number | 是 | 否 | 当前最大亮度余量，该参数为大于0的浮点数。默认值为1.0。 |
| sdrNits | number | 是 | 否 | 屏幕的亮度，该参数为大于0的浮点数。默认值为500.0。 |

#### BrightnessCallback22+

type BrightnessCallback<T1, T2> = (data1: T1, data2: T2) => void

监听屏幕亮度信息时使用的回调函数类型。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data1 | T1 | 是 | 表示displayId，类型为number。 |
| data2 | T2 | 是 | 表示brightnessInfo，类型为BrightnessInfo。 |

#### ScreenShape18+

显示设备的屏幕形状枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RECTANGLE | 0 | 表示设备屏幕形状为矩形。 |
| ROUND | 1 | 表示设备屏幕形状为圆形。 |

#### VirtualScreenConfig16+

创建虚拟屏幕的参数。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 指定虚拟屏幕的名称，用户可自行定义。 |
| width | number | 否 | 否 | 指定虚拟屏幕的宽度，单位为px，该参数应为正整数。 |
| height | number | 否 | 否 | 指定虚拟屏幕的高度，单位为px，该参数应为正整数。 |
| density | number | 否 | 否 | 指定虚拟屏幕的密度，单位为px，该参数为浮点数。 |
| surfaceId | string | 否 | 否 | 指定虚拟屏幕的surfaceId，用户可自行定义，该参数最大长度为4096个字节，超出最大长度时则取前4096个字节。 |
| supportsFocus22+ | boolean | 否 | 是 | 指定虚拟屏幕是否可获得焦点。true表示可获焦，false表示不可获焦，默认值为true。 |

#### Position20+

坐标位置：在全局坐标系中，以主屏左上角为原点。在相对坐标系中，以指定屏幕左上角为原点。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 相对原点的横坐标，单位为px，该参数应为32位有符号整数，输入浮点数时向下取整。 |
| y | number | 否 | 否 | 相对原点的纵坐标，单位为px，该参数应为32位有符号整数，输入浮点数时向下取整。 |

#### RelativePosition20+

相对坐标系下的坐标位置，以displayId对应的屏幕左上角为原点。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| displayId | number | 否 | 否 | 相对坐标所对应的屏幕ID，仅支持整数输入，且需大于等于0。 |
| position | Position | 否 | 否 | 以displayId所指定屏幕左上角为原点的坐标值。 |

#### display.getDisplayByIdSync12+

getDisplayByIdSync(displayId: number): Display

根据displayId获取对应的Display对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 屏幕ID。该参数仅支持整数输入，该参数大于等于0。需要确保displayId准确才能成功获取到对应结果。可以通过WindowProperties的displayId属性获取到准确的displayId作为入参。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Display | 返回displayId对应的Display对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[屏幕错误码]([屏幕错误码](../../errors/屏幕错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types. 3. Parameter verification failed. |
| 1400003 | This display manager service works abnormally. Possible causes: Display is null, display id corresponding display does not exist. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;

try {
  // 可以通过WindowProperties的displayId属性获取到准确的displayId作为入参
  let displayId = 0;
  displayClass = display.getDisplayByIdSync(displayId);
} catch (exception) {
  console.error(`Failed to get display. Code: ${exception.code}, message: ${exception.message}`);
}
```

#### display.getBrightnessInfo22+

getBrightnessInfo(displayId: number): [BrightnessInfo](#ZH-CN_TOPIC_0000002522240754__brightnessinfo22)

获取指定displayId对应屏幕的亮度信息。如果屏幕不支持HDR，返回的[BrightnessInfo](#ZH-CN_TOPIC_0000002522240754__brightnessinfo22)对象中的currentHeadroom和maxHeadroom为默认值。虚拟屏的BrightnessInfo对象中sdrNits为默认值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 屏幕ID。该参数仅支持整数输入，该参数大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| BrightnessInfo | 返回displayId对应屏幕的亮度信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

try {
  let brightNessInfo = display.getBrightnessInfo(0);
  console.info(`brightness info: ${JSON.stringify(brightNessInfo)}`);
} catch (error) {
  console.error(`Failed to getDisplayBrightness. Code: ${error.code}, message: ${error.message}`);
}
```

#### display.getAllDisplayPhysicalResolution12+

getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>

获取当前设备支持的所有显示模式及其对应的物理屏幕分辨率信息对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<DisplayPhysicalResolution>> | Promise对象。返回当前所有的DisplayPhysicalResolution对象。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let promise = display.getAllDisplayPhysicalResolution();
promise.then((resolutionObjects) => {
  console.info('Obtaining physical resolution length: ' + resolutionObjects.length);
  for (let i = 0; i < resolutionObjects.length; i++) {
     console.info(`resolutionObjects[${i}].foldDisplayMode: ${resolutionObjects[i].foldDisplayMode}`);
     console.info(`resolutionObjects[${i}].physicalWidth: ${resolutionObjects[i].physicalWidth}`);
     console.info(`resolutionObjects[${i}].physicalHeight: ${resolutionObjects[i].physicalHeight}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain physical resolution. Code: ${err.code}, message: ${err.message}`);
});
```

#### display.getDefaultDisplaySync9+

getDefaultDisplaySync(): Display

返回应用所在屏幕的Display对象。若应用内多个Ability在不同屏幕，返回主屏的Display对象，若应用内多个Ability在同一屏幕，返回所在屏幕的Display对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Display | 返回默认的Display对象。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400001 | Invalid display or screen. Possible cause: Display is not created or destroyed. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
} catch (exception) {
  console.error(`Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
}
```

#### display.getPrimaryDisplaySync14+

getPrimaryDisplaySync(): Display

获取主屏信息。除2in1之外的设备获取的是设备自带屏幕的Display对象；2in1设备外接屏幕时获取的是当前主屏幕的Display对象；2in1设备没有外接屏幕时获取的是自带屏幕的Display对象。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Display | 当前设备主屏幕的Display对象。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400001 | Invalid display or screen. Possible cause: Invalid display id. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;

displayClass = display.getPrimaryDisplaySync();
```

#### display.getAllDisplays9+

getAllDisplays(callback: AsyncCallback<Array<Display>>): void

获取当前所有的Display对象，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<Display>> | 是 | 回调函数。返回当前所有的Display对象。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400001 | Invalid display or screen. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: Array<display.Display> = [];
display.getAllDisplays((err: BusinessError, data: Array<display.Display>) => {
  displayClass = data;
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining all the display objects. Data: ${JSON.stringify(data)}`);
});
```

#### display.getAllDisplays9+

getAllDisplays(): Promise<Array<Display>>

获取当前所有的Display对象，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Display>> | Promise对象。返回当前所有的Display对象。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400001 | Invalid display or screen. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: Array<display.Display> =[];
let promise: Promise<Array<display.Display>> = display.getAllDisplays();
promise.then((data: Array<display.Display>) => {
  displayClass = data;
  console.info(`Succeeded in obtaining all the display objects. Data:  ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
});
```

#### display.on('add'|'remove'|'change')

on(type: 'add'|'remove'|'change', callback: Callback<number>): void

开启显示设备变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件。 - type为"add"，表示增加显示设备事件。例如：插入显示器。 - type为"remove"，表示移除显示设备事件。例如：移除显示器。 - type为"change"，表示改变显示设备事件。例如：显示器方向改变。 |
callbackCallback<number>是回调函数。返回监听到的屏幕ID，该参数为整数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<number> = (data: number) => {
  console.info(`Listening enabled. Data: ${data}`);
};

display.on("add", callback);
```

#### display.off('add'|'remove'|'change')

off(type: 'add'|'remove'|'change', callback?: Callback<number>): void

关闭显示设备变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件。 - type为"add"，表示增加显示设备事件。例如：插入显示器。 - type为"remove"，表示移除显示设备事件。例如：移除显示器。 - type为"change"，表示改变显示设备事件。例如：显示器方向改变。 |
callbackCallback<number>否需要取消注册的回调函数。返回监听到的屏幕ID，该参数为整数。若无此参数，则取消注册当前type类型事件监听的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```ets

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off("remove");

let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for display remove. Data: ${data}`)
};
// 关闭传入的callback监听
display.off('remove', callback);
```

**display.onChangeWithAttribute23+**

onChangeWithAttribute(displayAttributeOption: Array<string>, callback: Callback<number>): void

开启显示设备指定属性变化的监听。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Window.SessionManager

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayAttributeOption | Array<string> | 是 | 指定需要监听的屏幕属性名称，且仅限于display属性中包含的属性。 |
| callback | Callback<number> | 是 | 回调函数。返回监听到的屏幕ID，该参数为整数。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function onChangeWithAttribute can not work correctly due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. Possible causes: Internal IPC error. |

示例：

```ets
import { Callback } from '@kit.BasicServicesKit';

let attributesChangeCallback: Callback<number> = (data: number) => {
  console.info(`Listening enabled. Data: ${data}`);
};
let attributes: Array<string> = ["rotation", "width"];
display.onChangeWithAttribute(attributes, attributesChangeCallback);
```

#### display.isFoldable10+

isFoldable(): boolean

判断设备是否可折叠。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | boolean对象，返回当前设备是否可折叠的结果。false表示不可折叠，true表示可折叠。对于外屏只有简单辅助显示作用的小折叠设备，应用无法自定义外屏界面，故其返回值为false。其他可折叠设备的返回值均为true。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let ret: boolean = false;
ret = display.isFoldable();
```

#### display.getFoldStatus10+

getFoldStatus(): FoldStatus

获取可折叠设备当前的折叠状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FoldStatus | FoldStatus对象，返回当前可折叠设备的折叠状态。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let data: display.FoldStatus = display.getFoldStatus();
console.info(`Succeeded in obtaining fold status. Data: ${data}`);
```

#### display.getFoldDisplayMode10+

getFoldDisplayMode(): FoldDisplayMode

获取可折叠设备当前的显示模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备、非折叠设备中返回0，在其他设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FoldDisplayMode | FoldDisplayMode对象，返回可折叠设备当前的显示模式。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let data: display.FoldDisplayMode = display.getFoldDisplayMode();
console.info(`Succeeded in obtaining fold display mode. Data: ${data}`);
```

#### display.getCurrentFoldCreaseRegion10+

getCurrentFoldCreaseRegion(): FoldCreaseRegion

在当前显示模式下获取折叠折痕区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在折叠设备中可正常调用，在其他设备中返回undefined。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FoldCreaseRegion | FoldCreaseRegion对象，返回设备在当前显示模式下的折叠折痕区域。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let data: display.FoldCreaseRegion = display.getCurrentFoldCreaseRegion();
console.info(`Succeeded in obtaining current fold crease region. Data: ${JSON.stringify(data)}`);
```

#### display.on('foldStatusChange')10+

on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void

开启折叠设备折叠状态变化的监听。

本接口监听设备物理折叠状态的变化，如果要监听屏幕显示模式的变化，需要使用[display.on('foldDisplayModeChange')](#ZH-CN_TOPIC_0000002522240754__displayonfolddisplaymodechange10)接口。

两者存在差异，时序上物理折叠状态变化在前，底层会根据物理折叠状态匹配屏幕显示模式状态。

若需监听当前显示内容是显示在折叠设备的内屏还是外屏，请使用[display.on('foldDisplayModeChange')](#ZH-CN_TOPIC_0000002522240754__displayonfolddisplaymodechange10)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldStatusChange'，表示折叠设备折叠状态发生变化。 |
| callback | Callback<FoldStatus> | 是 | 回调函数。表示折叠设备折叠状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

/**
 * 注册监听的callback参数要采用对象传递。
 * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
*/
let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  console.info(`Listening enabled. Data: ${data}`);
};
display.on('foldStatusChange', callback);
```

#### display.off('foldStatusChange')10+

off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void

关闭折叠设备折叠状态变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldStatusChange'，表示折叠设备折叠状态发生变化。 |
| callback | Callback<FoldStatus> | 否 | 需要取消注册的回调函数。表示折叠设备折叠状态。若无此参数，则取消注册折叠状态变化监听的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('foldStatusChange');

let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  console.info(`unregistering FoldStatus changes callback. Data: ${data}`);
};
// 关闭传入的callback监听
display.off('foldStatusChange', callback);
```

#### display.on('brightnessInfoChange')22+

on(type: 'brightnessInfoChange', callback: BrightnessCallback<number, BrightnessInfo>): void

开启所有屏幕亮度信息变化的监听。如果屏幕不支持HDR，监听到的[BrightnessInfo](#ZH-CN_TOPIC_0000002522240754__brightnessinfo22)对象中的currentHeadroom和maxHeadroom为默认值。虚拟屏的BrightnessInfo对象中sdrNits为默认值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'brightnessInfoChange'，表示屏幕亮度信息状态发生变化。 |
| callback | BrightnessCallback<number, BrightnessInfo> | 是 | 回调函数。返回屏幕亮度信息改变的displayId(参数1)及对应的屏幕亮度信息(参数2)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**示例：**

```ets
let callback: display.BrightnessCallback<number, display.BrightnessInfo> = (id: number, data: display.BrightnessInfo) => {
  console.info(`Listening enabled ${id}. Data: ${JSON.stringify(data)}`);
};
try {
  display.on("brightnessInfoChange", callback);
} catch (error) {
  console.error(`brightnessInfoChange error. Code ${error.code}, message: ${error.message}`);
}
```

#### display.off('brightnessInfoChange')22+

off(type: 'brightnessInfoChange', callback?: BrightnessCallback<number, BrightnessInfo>): void

关闭所有屏幕亮度信息状态变化的监听。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'brightnessInfoChange'，表示屏幕亮度信息状态发生变化。 |
| callback | BrightnessCallback<number, BrightnessInfo> | 否 | 需要取消注册的回调函数。表示brightnessInfo状态发生改变。若无此参数，则取消所有注册brightnessInfo状态发生改变的回调函数。参数1为displayId，参数2为屏幕亮度信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**示例：**

```ets
let callback: display.BrightnessCallback<number, display.BrightnessInfo> = (id: number, data: display.BrightnessInfo) => {
  console.info(`Listening enabled ${id}. Data: ${JSON.stringify(data)}`);
};
try {
  display.off("brightnessInfoChange", callback);
} catch (error) {
  console.error(`brightnessInfoChange error. Code ${error.code}, message: ${error.message}`);
}
```

#### display.on('foldAngleChange')12+

on(type: 'foldAngleChange', callback: Callback<Array<number>>): void

开启折叠设备折叠角度变化的监听。如果是双折轴设备，则有两个角度值；在充电口朝下的状态下，从右到左分别是折轴一和折轴二。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldAngleChange'，表示折叠设备折叠角度发生变化。 |
| callback | Callback<Array<number>> | 是 | 回调函数。表示折叠设备屏幕折叠角度值（0度~180度）。如果是双折轴设备，则数组返回两个角度值，第一个值是折轴一的折叠角度值，第二个值是折轴二的折叠角度值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<Array<number>> = (angles: Array<number>) => {
  console.info('Listening fold angles length: ' + angles.length);
};
display.on('foldAngleChange', callback);
```

#### display.off('foldAngleChange')12+

off(type: 'foldAngleChange', callback?: Callback<Array<number>>): void

关闭折叠设备折叠角度变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldAngleChange'表示折叠设备折叠角度发生变化。 |
| callback | Callback<Array<number>> | 否 | 需要取消注册的回调函数。表示折叠设备屏幕折叠角度值（0度~180度）。若无此参数，则取消注册折叠角度变化监听的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('foldAngleChange');

let callback: Callback<Array<number>> = (angles: Array<number>) => {
  console.info('Listening fold angles length: ' + angles.length);
};
// 关闭传入的callback监听
display.off('foldAngleChange', callback);
```

#### display.on('captureStatusChange')12+

on(type: 'captureStatusChange', callback: Callback<boolean>): void

开启设备的屏幕显示信息是否被获取的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStatusChange'表示设备的屏幕显示信息被获取的状态发生变化。 |
| callback | Callback<boolean> | 是 | 回调函数。表示设备的屏幕显示信息是否被获取。true表示设备的屏幕显示信息开始被获取，包括处于截屏、投屏、录屏状态，或创建了虚拟屏幕(虚拟屏幕可能被应用获取屏幕图像)，截屏仅返回一次true；false表示获取结束。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<boolean> = (captureStatus: boolean) => {
  console.info('Listening capture status: ' + captureStatus);
};
display.on('captureStatusChange', callback);
```

#### display.off('captureStatusChange')12+

off(type: 'captureStatusChange', callback?: Callback<boolean>): void

关闭设备的屏幕显示信息是否被获取的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStatusChange'表示设备的屏幕显示信息被获取的状态发生变化。 |
| callback | Callback<boolean> | 否 | 需要取消注册的回调函数。表示设备的屏幕显示信息是否被获取。true表示设备的屏幕显示信息开始被获取，包括处于截屏、投屏、录屏状态，或创建了虚拟屏幕(虚拟屏幕可能被应用获取屏幕图像)，截屏仅返回一次true；false表示获取结束。若无此参数，则取消注册设备的屏幕显示信息是否存在被获取监听的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('captureStatusChange');

let callback: Callback<boolean> = (captureStatus: boolean) => {
  console.info('Listening capture status: ' + captureStatus);
};
// 关闭传入的callback监听
display.off('captureStatusChange', callback);
```

#### display.isCaptured12+

isCaptured(): boolean

检查设备的屏幕显示信息是否被获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | boolean值，返回设备的屏幕显示信息是否存在被获取的情况。返回true表示设备的屏幕信息存在被获取的情况，可能为：设备正处于截屏、投屏、录屏状态，或已创建虚拟屏幕(虚拟屏幕可能被应用获取屏幕图像)；返回false则表示设备的屏幕信息不存在被获取的情况。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let ret: boolean = false;
ret = display.isCaptured();
```

#### display.on('foldDisplayModeChange')10+

on(type: 'foldDisplayModeChange', callback: Callback<FoldDisplayMode>): void

开启折叠设备屏幕显示模式变化的监听。

本接口监听设备屏幕显示模式的变化，如果要监听设备物理折叠状态的变化，需要使用[display.on('foldStatusChange')](#ZH-CN_TOPIC_0000002522240754__displayonfoldstatuschange10)接口。

两者存在差异，时序上物理折叠状态变化在前，底层会根据物理折叠状态匹配屏幕显示模式状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备、非折叠设备中不生效也不报错，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldDisplayModeChange'，表示折叠设备屏幕显示模式发生变化。 |
| callback | Callback<FoldDisplayMode> | 是 | 回调函数。表示折叠设备屏幕显示模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

/**
 * 注册监听的callback参数要采用对象传递。
 * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
*/
let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
  console.info(`Listening enabled. Data: ${data}`);
};
display.on('foldDisplayModeChange', callback);
```

#### display.off('foldDisplayModeChange')10+

off(type: 'foldDisplayModeChange', callback?: Callback<FoldDisplayMode>): void

关闭折叠设备屏幕显示模式变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备、非折叠设备中不生效也不报错，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldDisplayModeChange'，表示折叠设备屏幕显示模式发生变化。 |
| callback | Callback<FoldDisplayMode> | 否 | 需要取消注册的回调函数。表示折叠设备屏幕显示模式。若无此参数，则取消注册屏幕显示模式变化监听的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('foldDisplayModeChange');

let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
  console.info(`unregistering FoldDisplayMode changes callback. Data: ${data}`);
};
// 关闭传入的callback监听
display.off('foldDisplayModeChange', callback);
```

#### display.createVirtualScreen16+

createVirtualScreen(config:VirtualScreenConfig): Promise<number>

创建虚拟屏幕，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**需要权限**：ohos.permission.ACCESS_VIRTUAL_SCREEN

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | VirtualScreenConfig | 是 | 用于创建虚拟屏幕的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回创建的虚拟屏幕的ScreenId。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported.function createVirtualScreen can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class VirtualScreenConfig {
  name : string = '';
  width : number = 0;
  height : number = 0;
  density : number = 0;
  surfaceId : string = '';
  supportsFocus ?: boolean = true;
}

let config : VirtualScreenConfig = {
  name: 'screen01',
  width: 1080,
  height: 2340,
  density: 2,
  surfaceId: '',
  supportsFocus: false
};

display.createVirtualScreen(config).then((screenId: number) => {
  console.info(`Succeeded in creating the virtual screen.ScreenId : ${screenId}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create the virtual screen. Code:${err.code},message is ${err.message}`);
});
```

#### display.destroyVirtualScreen16+

destroyVirtualScreen(screenId:number): Promise<void>

销毁虚拟屏幕，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**需要权限**：ohos.permission.ACCESS_VIRTUAL_SCREEN

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| screenId | number | 是 | 屏幕ID，与创建的虚拟屏幕ID保持一致，即使用createVirtualScreen()接口成功创建对应虚拟屏幕时的返回值，该参数仅支持整数输入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported.function destroyVirtualScreen can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 1;
display.destroyVirtualScreen(screenId).then(() => {
  console.info('Succeeded in destroying the virtual screen.');
}).catch((err: BusinessError) => {
  console.error(`Failed to destroy the virtual screen.Code:${err.code},message is ${err.message}`);
});
```

#### display.setVirtualScreenSurface16+

setVirtualScreenSurface(screenId:number, surfaceId: string): Promise<void>

设置虚拟屏幕的surfaceId，surfaceId用于标识一个surface，表示当前虚拟屏用于显示对应surface中的内容。使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**需要权限**：ohos.permission.ACCESS_VIRTUAL_SCREEN

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| screenId | number | 是 | 屏幕ID，与创建的虚拟屏幕ID保持一致，即使用createVirtualScreen()接口成功创建对应虚拟屏幕时的返回值，该参数仅支持整数输入。 |
| surfaceId | string | 是 | 代表虚拟屏幕绑定的surfaceId，由用户指定某一实际存在的surface对应的surfaceId，该参数最大长度为4096个字节，超出最大长度时则取前4096个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported.function setVirtualScreenSurface can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
//Index.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  xComponentController: XComponentController = new XComponentController();

  setVirtualScreenSurface = () => {
    let screenId: number = 1;
    let surfaceId = this.xComponentController.getXComponentSurfaceId();
    display.setVirtualScreenSurface(screenId, surfaceId).then(() => {
      console.info('Succeeded in setting the surface for the virtual screen.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set the surface for the virtual screen. Code:${err.code},message is ${err.message}`);
    });
  }
  build() {
    RelativeContainer() {
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentController
      })
      Button('setSurface')
        .onClick((event: ClickEvent) => {
          this.setVirtualScreenSurface();
      }).width('100%')
      .height(20)
    }
    .width('100%')
    .height('100%')
  }
```

#### display.makeUnique16+

makeUnique(screenId:number): Promise<void>

将屏幕设置为异源模式，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**需要权限**：ohos.permission.ACCESS_VIRTUAL_SCREEN

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| screenId | number | 是 | 要设置成异源模式的屏幕ID。其中id应为大于0的整数，否则返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported.function makeUnique can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 0;
display.makeUnique(screenId).then(() => {
  console.info('Succeeded in making unique screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to make unique screens. Code:${err.code},message is ${err.message}`);
});
```

#### display.convertRelativeToGlobalCoordinate20+

convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position

将指定屏幕左上角为原点的相对坐标转换成主屏左上角为原点的全局坐标，仅支持主屏和扩展屏的坐标转换。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| relativePosition | RelativePosition | 是 | 需要转化为全局坐标的相对坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Position | 返回相对于主屏左上角的全局坐标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let relativePosition: display.RelativePosition = {
  displayId: 0,
  position: {
    x: 100,
    y: 200
  }
};

try {
  let position: display.Position = display.convertRelativeToGlobalCoordinate(relativePosition);
  console.info(`The global coordinate is ${position.x}, ${position.y}`)
} catch (exception) {
  console.error(`Failed to convert the relative coordinate to the global coordinate. Code: ${exception.code}, message: ${exception.message}`);
}
```

#### display.convertGlobalToRelativeCoordinate20+

convertGlobalToRelativeCoordinate(position: Position, displayId?: number): RelativePosition

将主屏左上角为原点的全局坐标转换成displayId指定屏幕左上角为原点的相对坐标。若未传入displayId，默认转换为全局坐标所在屏幕的相对坐标系。若全局坐标不在任何屏幕上，默认转换成主屏的相对坐标。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | Position | 是 | 需要转化为相对坐标的全局坐标。 |
| displayId | number | 否 | 相对坐标系原点所在的屏幕ID，传递该参数表示以指定屏幕左上角为原点转换相对坐标。不指定则不传参，默认转换成全局坐标所在屏幕的相对坐标，若全局坐标不在任何屏幕上，则默认转换成主屏的相对坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RelativePosition | 返回对应屏幕的相对坐标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let position: display.Position = {
    x: 100,
    y: 200
};

try {
  let relPos: display.RelativePosition = display.convertGlobalToRelativeCoordinate(position, 0);
  console.info(`The relative coordinate is ${relPos.displayId}, ${relPos.position.x}, ${relPos.position.y}`)
} catch (exception) {
  console.error(`Failed to convert the global coordinate to the relative coordinate. Code: ${exception.code}, message: ${exception.message}`);
}
```

#### display.getDefaultDisplay(deprecated)

getDefaultDisplay(callback: AsyncCallback<Display>): void

获取当前默认的Display对象，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[getDefaultDisplaySync()](#ZH-CN_TOPIC_0000002522240754__displaygetdefaultdisplaysync9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Display> | 是 | 回调函数。返回当前默认的Display对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
display.getDefaultDisplay((err: BusinessError, data: display.Display) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to obtain the default display object. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the default display object. Data: ${JSON.stringify(data)}`);
  displayClass = data;
});
```

#### display.getDefaultDisplay(deprecated)

getDefaultDisplay(): Promise<Display>

获取当前默认的Display对象，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[getDefaultDisplaySync()](#ZH-CN_TOPIC_0000002522240754__displaygetdefaultdisplaysync9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Display> | Promise对象。返回当前默认的Display对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
let promise: Promise<display.Display> = display.getDefaultDisplay();
promise.then((data: display.Display) => {
  displayClass = data;
  console.info(`Succeeded in obtaining the default display object. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the default display object. Code: ${err.code}, message: ${err.message}`);
});
```

#### display.getAllDisplay(deprecated)

getAllDisplay(callback: AsyncCallback<Array<Display>>): void

获取当前所有的Display对象，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[getAllDisplays()](#ZH-CN_TOPIC_0000002522240754__displaygetalldisplays9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<Display>> | 是 | 回调函数。返回当前所有的Display对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

display.getAllDisplay((err: BusinessError, data: Array<display.Display>) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the default display objects. Data: ${JSON.stringify(data)}`);
});
```

#### display.getAllDisplay(deprecated)

getAllDisplay(): Promise<Array<Display>>

获取当前所有的Display对象，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃，建议使用[getAllDisplays()](#ZH-CN_TOPIC_0000002522240754__displaygetalldisplays9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Display>> | Promise对象。返回当前所有的Display对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise: Promise<Array<display.Display>> = display.getAllDisplay();
promise.then((data: Array<display.Display>) => {
  console.info(`Succeeded in obtaining the default display objects. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
});
```

#### Display

屏幕实例。描述Display对象的属性和方法。

下列API示例中都需先使用[getAllDisplays()](#ZH-CN_TOPIC_0000002522240754__displaygetalldisplays9)、[getDefaultDisplaySync()](#ZH-CN_TOPIC_0000002522240754__displaygetdefaultdisplaysync9)中的任一方法获取到Display实例，再通过此实例调用对应方法。

#### 属性

![image](public_sys-resources/zh-cn_image_0000002522244724.webp)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 显示设备的屏幕ID，该参数为大于等于0的整数。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| name | string | 是 | 否 | 显示设备的名称。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| alive | boolean | 是 | 否 | 显示设备的启用状态，表示设备是否处于正常运行状态。true表示已启用，处于正常运行状态；false表示未启用，未处于正常运行状态。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| state | DisplayState | 是 | 否 | 显示设备的状态。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| refreshRate | number | 是 | 否 | 显示设备当前采用的刷新率，该参数为整数，单位为Hz。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| rotation | number | 是 | 否 | 显示设备的屏幕顺时针旋转角度。 值为0时，表示显示设备屏幕顺时针旋转为0°，表示显示设备的标准显示方向； 值为1时，表示显示设备屏幕顺时针旋转为90°； 值为2时，表示显示设备屏幕顺时针旋转为180°； 值为3时，表示显示设备屏幕顺时针旋转为270°。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| width | number | 是 | 否 | 显示设备的屏幕宽度，单位为px，该参数为整数。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| height | number | 是 | 否 | 显示设备的屏幕高度，单位为px，该参数为整数。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| densityDPI | number | 是 | 否 | 显示设备的物理像素密度，表示每英寸上的像素点数。该参数为浮点数，单位为px。一般取值160.0、480.0等，实际能取到的值取决于不同设备设置里提供的可选值。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| orientation10+ | Orientation | 是 | 否 | 表示显示设备当前显示的方向。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| densityPixels | number | 是 | 否 | 显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数，计算方式为： 该参数为浮点数，受densityDPI范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的densityDPI。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| scaledDensity | number | 是 | 否 | 显示设备上的字体的缩放因子。该参数为浮点数，通常与densityPixels相同。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| xDPI | number | 是 | 否 | x轴方向中每英寸屏幕的确切物理像素值，该参数为浮点数。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| yDPI | number | 是 | 否 | y轴方向中每英寸屏幕的确切物理像素值，该参数为浮点数。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| colorSpaces11+ | Array<colorSpaceManager.ColorSpace> | 是 | 否 | 显示设备支持的所有色域类型。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| hdrFormats11+ | Array<hdrCapability.HDRFormat> | 是 | 否 | 显示设备支持的所有HDR格式。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| availableWidth12+ | number | 是 | 否 | 显示设备的可用区域宽度，单位为px，该参数为大于0的整数。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。  设备行为差异： 该接口在2in1设备、Tablet设备中可正常调用；在其他设备中不可用，请通过width属性获取当前设备屏幕的可用区域宽度。 |
| availableHeight12+ | number | 是 | 否 | 显示设备的可用区域高度，单位为px，该参数为大于0的整数。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 12开始，该接口支持在元服务中使用。  设备行为差异： 该接口在2in1设备、Tablet设备中可正常调用；在其他设备中不可用，请通过height属性获取当前设备屏幕的可用区域高度。 |
| screenShape18+ | ScreenShape | 是 | 是 | 显示设备的屏幕形状，默认值为RECTANGLE。 系统能力： SystemCapability.WindowManager.WindowManager.Core 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| sourceMode19+ | DisplaySourceMode | 是 | 是 | 显示设备的显示模式枚举，默认值为DisplaySourceMode.NONE。 系统能力： SystemCapability.Window.SessionManager  元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| x19+ | number | 是 | 是 | 显示设备左上角相对于原点的x轴坐标，原点为主屏左上角，单位为px，该参数为整数，默认值为0。仅DisplaySourceMode为MAIN和EXTEND时返回实际值，其余默认返回默认值0。 系统能力： SystemCapability.Window.SessionManager 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| y19+ | number | 是 | 是 | 显示设备左上角相对于原点的y轴坐标，原点为主屏左上角，单位为px，该参数为整数，默认值为0。仅DisplaySourceMode为MAIN和EXTEND时返回实际值，其余默认返回默认值0。 系统能力： SystemCapability.Window.SessionManager 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| supportedRefreshRates20+ | Array<number> | 是 | 是 | 显示设备支持的所有刷新率，从小到大排序。刷新率值为正整数，单位为Hz。默认为空。 系统能力： SystemCapability.Window.SessionManager 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

**getRoundedCorner23+**

getRoundedCorner(): Array<RoundedCorner>

获取屏幕的圆角信息。屏幕圆角信息由产品配置决定，只有配置了屏幕圆角半径的物理屏幕才能返回圆角信息，否则返回空数组，虚拟屏同样返回空数组。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<RoundedCorner> | 返回当前屏幕的圆角信息。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let data = displayClass.getRoundedCorner();
  console.info(`Succeeded in getting rounded corner. Data: ${JSON.stringify(data)}`);
} catch (error) {
  console.error(`Failed to getRoundedCorner. Code: ${error.code}, message: ${error.message}`);
}
```

#### getCutoutInfo9+

getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void

获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。使用callback异步回调。建议应用布局规避该区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<CutoutInfo> | 是 | 回调函数。返回不可用屏幕区域对象。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400001 | Invalid display or screen. Possible cause: 1. This display is abnormal. 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();

displayClass.getCutoutInfo((err: BusinessError, data: display.CutoutInfo) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to get cutoutInfo. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting cutoutInfo. Data: ${JSON.stringify(data)}`);
});
```

#### getCutoutInfo9+

getCutoutInfo(): Promise<CutoutInfo>

获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。使用Promise异步回调。建议应用布局规避该区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<CutoutInfo> | Promise对象。返回描述不可用屏幕区域的CutoutInfo对象。 |

**错误码：**

以下错误码的详细介绍请参见[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1400001 | Invalid display or screen. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();
let promise: Promise<display.CutoutInfo> = displayClass.getCutoutInfo();
promise.then((data: display.CutoutInfo) => {
  console.info(`Succeeded in getting cutoutInfo. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
});
```

#### getAvailableArea12+

getAvailableArea(): Promise<Rect>

获取当前设备屏幕的可用区域，使用Promise异步回调。

可用区域是扣除系统UI（如状态栏、Dock栏）后，可供应用程序自由使用的区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 该接口在2in1设备、Tablet设备中可正常调用；在其他设备中不可用，请通过[Display属性](#ZH-CN_TOPIC_0000002522240754__属性)中的width、height属性获取当前设备屏幕的可用区域。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Rect> | Promise对象。返回当前屏幕可用矩形区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400001 | Invalid display or screen. Possible cause: 1. This display is abnormal. 2. Internal task error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let promise = displayClass.getAvailableArea();
  promise.then((data) => {
    console.info(`Succeeded get the available area in this display. data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get the available area in this display. Code: ${err.code}, message: ${err.message}`);
  })
} catch (exception) {
  console.error(`Failed to obtain the default display object. Code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('availableAreaChange')12+

on(type: 'availableAreaChange', callback: Callback<Rect>): void

开启当前设备屏幕可用区域的监听。当屏幕旋转、进入/退出自由多窗模式、设置Dock栏/状态栏等系统控件可见性变化时，触发回调函数，返回可用区域信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备、Tablet设备中可正常调用，在其他设备中不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件。固定为'availableAreaChange'，表示屏幕可用区域变更。 |
| callback | Callback<Rect> | 是 | 回调函数。返回改变后的可用区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(`Listening enabled. Data: ${JSON.stringify(data)}`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.on("availableAreaChange", callback);
} catch (exception) {
  console.error(`Failed to register callback. Code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('availableAreaChange')12+

off(type: 'availableAreaChange', callback?: Callback<Rect>): void

关闭当前设备屏幕可用区域变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备、Tablet设备中可正常调用，在其他设备中不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'availableAreaChange'，表示屏幕可用区域变更。 |
| callback | Callback<Rect> | 否 | 需要取消注册的回调函数。返回改变后的可用区域。若无此参数，则取消注册屏幕可用区域变化监听的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(`Listening enabled. Data: ${JSON.stringify(data)}`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.off("availableAreaChange", callback);
} catch (exception) {
  console.error(`Failed to unregister callback. Code: ${exception.code}, message: ${exception.message}`);
}
```

#### getLiveCreaseRegion20+

getLiveCreaseRegion(): FoldCreaseRegion

获取当前显示模式下的实时折痕区域。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FoldCreaseRegion | 返回设备在当前显示模式下的折叠折痕区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[屏幕错误码](屏幕错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ets
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let data: display.FoldCreaseRegion = displayClass.getLiveCreaseRegion();
  console.info(`Succeeded in getting the live crease region. Data: ${JSON.stringify(data)}`);
} catch (exception) {
  console.error(`Failed to get the live crease region. Code: ${exception.code}, message: ${exception.message}`);
}
```