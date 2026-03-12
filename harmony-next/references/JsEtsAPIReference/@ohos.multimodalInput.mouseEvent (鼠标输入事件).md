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

名称值说明CANCEL0取消。MOVE1鼠标移动。BUTTON_DOWN2鼠标按键按下。BUTTON_UP3鼠标按键抬起。AXIS_BEGIN4鼠标轴事件开始。AXIS_UPDATE5鼠标轴事件更新。AXIS_END6鼠标轴事件结束。ACTION_DOWN11+7触控板按下。ACTION_UP11+8触控板抬起。

#### Button

鼠标按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称值说明LEFT0鼠标左键。MIDDLE1鼠标中键。RIGHT2鼠标右键。SIDE3鼠标侧边键。EXTRA4鼠标扩展键。FORWARD5鼠标前进键。BACK6鼠标后退键。TASK7鼠标任务键。

#### Axis

鼠标轴类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称值说明SCROLL_VERTICAL0鼠标垂直滚动轴。SCROLL_HORIZONTAL1鼠标水平滚动轴。PINCH2鼠标捏合轴。

#### AxisValue

鼠标轴类型和轴的值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明axis[Axis](#ZH-CN_TOPIC_0000002497605568__axis)否否鼠标轴类型。valuenumber否否鼠标轴的值。

#### ToolType11+

工具类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称值说明UNKNOWN0未知类型。MOUSE1鼠标。JOYSTICK2操纵杆。TOUCHPAD3触控板。

#### MouseEvent

鼠标事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明action[Action](#ZH-CN_TOPIC_0000002497605568__action)否否鼠标事件类型。screenXnumber否否该鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数。screenYnumber否否该鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数。windowXnumber否否鼠标所在窗口左上角为原点的相对坐标系的X坐标。当前仅支持整数。windowYnumber否否鼠标所在窗口左上角为原点的相对坐标系的Y坐标。当前仅支持整数。rawDeltaXnumber否否鼠标当前事件相对于上次事件的X坐标偏移值。当前仅支持整数。rawDeltaYnumber否否鼠标当前事件相对于上次事件的Y坐标偏移值。当前仅支持整数。button[Button](#ZH-CN_TOPIC_0000002497605568__button)否否鼠标按键。pressedButtons[Button](#ZH-CN_TOPIC_0000002497605568__button)[]否否当前处于按下状态的鼠标按键。axes[AxisValue](#ZH-CN_TOPIC_0000002497605568__axisvalue)[]否否鼠标轴类型和轴的值。pressedKeys[KeyCode](zh-cn_topic_0000002529285559.html#ZH-CN_TOPIC_0000002529285559__keycode)[]否否当前处于按下状态的键值列表。ctrlKeyboolean否否

当前ctrlKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

altKeyboolean否否

当前altKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

shiftKeyboolean否否

当前shiftKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

logoKeyboolean否否

当前logoKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

fnKeyboolean否否

当前fnKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

capsLockboolean否否

当前capsLock是否处于使能状态。

true表示使能状态，false表示处于未使能状态。

numLockboolean否否

当前numLock是否处于使能状态。

true表示使能状态，false表示处于未使能状态。

scrollLockboolean否否

当前scrollLock是否处于使能状态。

true表示使能状态，false表示处于未使能状态。

toolType11+[ToolType](#ZH-CN_TOPIC_0000002497605568__tooltype11)否否工具类型。globalX20+number否是该鼠标事件以主屏左上角为原点的全局坐标系的X坐标。作为出参时，由系统上报。globalY20+number否是该鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。作为出参时，由系统上报。