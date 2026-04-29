# @ohos.multimodalInput.mouseEvent (鼠标输入事件)

设备上报的鼠标事件，继承自[InputEvent](@ohos.multimodalInput.inputEvent (输入事件).md)。


本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Action, Button, Axis, AxisValue, MouseEvent } from '@kit.InputKit';
```

#### Action

鼠标事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CANCEL | 0 | 取消。鼠标down事件异常打断，未正常闭环，例如：按下鼠标按键后未抬起，窗口退后台或被异常销毁时触发cancel事件。 |
| MOVE | 1 | 鼠标移动。 |
| BUTTON_DOWN | 2 | 鼠标按键按下。 |
| BUTTON_UP | 3 | 鼠标按键抬起。 |
| AXIS_BEGIN | 4 | 鼠标轴事件开始。 |
| AXIS_UPDATE | 5 | 鼠标轴事件更新。 |
| AXIS_END | 6 | 鼠标轴事件结束。 |
| ACTION_DOWN11+ | 7 | 触控板按下。 |
| ACTION_UP11+ | 8 | 触控板抬起。 |

#### Button

鼠标按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 鼠标左键。 |
| MIDDLE | 1 | 鼠标中键。 |
| RIGHT | 2 | 鼠标右键。 |
| SIDE | 3 | 鼠标侧边键。 |
| EXTRA | 4 | 鼠标扩展键。 |
| FORWARD | 5 | 鼠标前进键。 |
| BACK | 6 | 鼠标后退键。 |
| TASK | 7 | 鼠标任务键。 |

#### Axis

鼠标轴类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCROLL_VERTICAL | 0 | 鼠标垂直滚动轴。 |
| SCROLL_HORIZONTAL | 1 | 鼠标水平滚动轴。 |
| PINCH | 2 | 鼠标捏合轴。 |

#### AxisValue

鼠标轴类型和轴的值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| axis | Axis | 否 | 否 | 鼠标轴类型。 |
| value | number | 否 | 否 | 鼠标轴的值。 |

#### ToolType11+

工具类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知类型。 |
| MOUSE | 1 | 鼠标。 |
| JOYSTICK | 2 | 操纵杆。 |
| TOUCHPAD | 3 | 触控板。 |

#### MouseEvent

鼠标事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | Action | 否 | 否 | 鼠标事件类型。 |
| screenX | number | 否 | 否 | 该鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数。 |
| screenY | number | 否 | 否 | 该鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数。 |
| windowX | number | 否 | 否 | 鼠标所在窗口左上角为原点的相对坐标系的X坐标。当前仅支持整数。 |
| windowY | number | 否 | 否 | 鼠标所在窗口左上角为原点的相对坐标系的Y坐标。当前仅支持整数。 |
| rawDeltaX | number | 否 | 否 | 鼠标当前事件相对于上次事件的X坐标偏移值。当前仅支持整数。 |
| rawDeltaY | number | 否 | 否 | 鼠标当前事件相对于上次事件的Y坐标偏移值。当前仅支持整数。 |
| button | Button | 否 | 否 | 鼠标按键。 |
| pressedButtons | Button[] | 否 | 否 | 当前处于按下状态的鼠标按键。 |
| axes | AxisValue[] | 否 | 否 | 鼠标轴类型和轴的值。 |
| pressedKeys | KeyCode[] | 否 | 否 | 当前处于按下状态的键值列表。 |
| ctrlKey | boolean | 否 | 否 | 当前ctrlKey是否处于按下状态。  true表示处于按下状态，false表示处于抬起状态。 |
| altKey | boolean | 否 | 否 | 当前altKey是否处于按下状态。  true表示处于按下状态，false表示处于抬起状态。 |
| shiftKey | boolean | 否 | 否 | 当前shiftKey是否处于按下状态。  true表示处于按下状态，false表示处于抬起状态。 |
| logoKey | boolean | 否 | 否 | 当前logoKey是否处于按下状态。  true表示处于按下状态，false表示处于抬起状态。 |
| fnKey | boolean | 否 | 否 | 当前fnKey是否处于按下状态。  true表示处于按下状态，false表示处于抬起状态。 |
| capsLock | boolean | 否 | 否 | 当前capsLock是否处于使能状态。  true表示使能状态，false表示处于未使能状态。 |
| numLock | boolean | 否 | 否 | 当前numLock是否处于使能状态。  true表示使能状态，false表示处于未使能状态。 |
| scrollLock | boolean | 否 | 否 | 当前scrollLock是否处于使能状态。  true表示使能状态，false表示处于未使能状态。 |
| toolType11+ | ToolType | 否 | 否 | 工具类型。 |
| globalX20+ | number | 否 | 是 | 该鼠标事件以主屏左上角为原点的全局坐标系的X坐标。作为出参时，由系统上报。 |
| globalY20+ | number | 否 | 是 | 该鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。作为出参时，由系统上报。 |