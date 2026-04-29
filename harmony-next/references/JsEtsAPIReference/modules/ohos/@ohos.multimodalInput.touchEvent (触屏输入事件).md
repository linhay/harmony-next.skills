# @ohos.multimodalInput.touchEvent (触屏输入事件)

设备上报的触屏输入事件，继承自[InputEvent](@ohos.multimodalInput.inputEvent (输入事件).md)。


本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Action,ToolType,SourceType,Touch,TouchEvent } from '@kit.InputKit';
```

#### Action

触屏输入事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CANCEL | 0 | 触屏取消。触屏down事件异常打断，未正常闭环，例如：手指按下后未抬起，屏幕发生旋转、折叠或有新hover等场景时触发cancel事件。 |
| DOWN | 1 | 触屏按下。 |
| MOVE | 2 | 触屏移动。 |
| UP | 3 | 触屏抬起。 |

#### ToolType

操作触屏的工具类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FINGER | 0 | 手指。 |
| PEN | 1 | 笔。 |
| RUBBER | 2 | 橡皮擦。 |
| BRUSH | 3 | 笔刷。 |
| PENCIL | 4 | 铅笔。 |
| AIRBRUSH | 5 | 气笔。 |
| MOUSE | 6 | 鼠标。 |
| LENS | 7 | 透镜。 |

#### SourceType

触屏来源的设备类型，当前仅支持触摸屏、触控板类型上报。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOUCH_SCREEN | 0 | 触摸屏。 |
| PEN | 1 | 手写笔。 |
| TOUCH_PAD | 2 | 触控板。 |

#### Touch

触屏点信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 触屏输入事件ID。 |
| pressedTime | number | 否 | 否 | 按下时间戳，单位：μs。 |
| screenX | number | 否 | 否 | 该触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数。 |
| screenY | number | 否 | 否 | 该触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数。 |
| windowX | number | 否 | 否 | 触屏所在窗口左上角为原点的相对坐标系的X坐标。当前仅支持整数。 |
| windowY | number | 否 | 否 | 触屏所在窗口左上角为原点的相对坐标系的Y坐标。当前仅支持整数。 |
| pressure | number | 否 | 否 | 压力值，取值范围是[0.0, 1.0]，0.0表示不支持。 |
| width | number | 否 | 否 | 触屏区域的宽度。当前仅支持整数。 |
| height | number | 否 | 否 | 触屏区域的高度。当前仅支持整数。 |
| tiltX | number | 否 | 否 | 相对YZ平面的角度，取值的范围[-90, 90]，其中正值是向右倾斜。 |
| tiltY | number | 否 | 否 | 相对XZ平面的角度，取值的范围[-90, 90]，其中正值是向下倾斜。 |
| toolX | number | 否 | 否 | 工具区域的中心点以指定屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数。 |
| toolY | number | 否 | 否 | 工具区域的中心点以指定屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数。 |
| toolWidth | number | 否 | 否 | 工具区域宽度。当前仅支持整数。 |
| toolHeight | number | 否 | 否 | 工具区域高度。当前仅支持整数。 |
| rawX | number | 否 | 否 | 输入设备上的X坐标。当前仅支持整数。 |
| rawY | number | 否 | 否 | 输入设备上的Y坐标。当前仅支持整数。 |
| toolType | ToolType | 否 | 否 | 工具类型。 |
| globalX20+ | number | 否 | 是 | 该触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。作为出参时，由系统上报。 |
| globalY20+ | number | 否 | 是 | 该触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。作为出参时，由系统上报。 |

#### TouchEvent

触屏输入事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | Action | 否 | 否 | 触屏输入事件类型。 |
| touch | Touch | 否 | 否 | 当前触屏点信息。 |
| touches | Touch[] | 否 | 否 | 所有触屏点。 |
| sourceType | SourceType | 否 | 否 | 触屏来源的设备类型。 |