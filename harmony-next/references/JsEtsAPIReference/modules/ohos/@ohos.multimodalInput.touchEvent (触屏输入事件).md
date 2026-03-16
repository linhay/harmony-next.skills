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

名称值说明CANCEL0触屏取消。DOWN1触屏按下。MOVE2触屏移动。UP3触屏抬起。

#### ToolType

操作触屏的工具类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称值说明FINGER0手指。PEN1笔。RUBBER2橡皮擦。BRUSH3笔刷。PENCIL4铅笔。AIRBRUSH5气笔。MOUSE6鼠标。LENS7透镜。

#### SourceType

触屏来源的设备类型，当前仅支持触摸屏、触控板类型上报。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称值说明TOUCH_SCREEN0触摸屏。PEN1手写笔。TOUCH_PAD2触控板。

#### Touch

触屏点信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明idnumber否否触屏输入事件ID。pressedTimenumber否否按下时间戳，单位：μs。screenXnumber否否该触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数。screenYnumber否否该触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数。windowXnumber否否触屏所在窗口左上角为原点的相对坐标系的X坐标。当前仅支持整数。windowYnumber否否触屏所在窗口左上角为原点的相对坐标系的Y坐标。当前仅支持整数。pressurenumber否否压力值，取值范围是[0.0, 1.0]，0.0表示不支持。widthnumber否否触屏区域的宽度。当前仅支持整数。heightnumber否否触屏区域的高度。当前仅支持整数。tiltXnumber否否相对YZ平面的角度，取值的范围[-90, 90]，其中正值是向右倾斜。tiltYnumber否否相对XZ平面的角度，取值的范围[-90, 90]，其中正值是向下倾斜。toolXnumber否否工具区域的中心点以指定屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数。toolYnumber否否工具区域的中心点以指定屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数。toolWidthnumber否否工具区域宽度。当前仅支持整数。toolHeightnumber否否工具区域高度。当前仅支持整数。rawXnumber否否输入设备上的X坐标。当前仅支持整数。rawYnumber否否输入设备上的Y坐标。当前仅支持整数。toolType[ToolType](#ZH-CN_TOPIC_0000002529445535__tooltype)否否工具类型。globalX20+number否是该触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。作为出参时，由系统上报。globalY20+number否是该触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。作为出参时，由系统上报。

#### TouchEvent

触屏输入事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明action[Action](#ZH-CN_TOPIC_0000002529445535__action)否否触屏输入事件类型。touch[Touch](#ZH-CN_TOPIC_0000002529445535__touch)否否当前触屏点信息。touches[Touch](#ZH-CN_TOPIC_0000002529445535__touch)[]否否所有触屏点。sourceType[SourceType](#ZH-CN_TOPIC_0000002529445535__sourcetype)否否触屏来源的设备类型。