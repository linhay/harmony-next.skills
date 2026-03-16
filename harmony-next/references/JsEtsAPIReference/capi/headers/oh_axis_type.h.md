# oh_axis_type.h

#### 概述

输入设备的轴事件结构和枚举。

**引用文件：** <multimodalinput/oh_axis_type.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**相关模块：**[input](../../topics/input/input.md)

#### 汇总

#### 枚举

名称typedef关键字描述[InputEvent_AxisType](#ZH-CN_TOPIC_0000002529285565__inputevent_axistype)InputEvent_AxisType输入设备的轴类型。[InputEvent_AxisEventType](#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)InputEvent_AxisEventType输入设备的轴事件类型。[InputEvent_AxisAction](#ZH-CN_TOPIC_0000002529285565__inputevent_axisaction)InputEvent_AxisAction轴事件动作。

#### 枚举类型说明

#### InputEvent_AxisType

```ets
enum InputEvent_AxisType
```

**描述**

输入设备的轴类型。

**起始版本：** 12

枚举项描述AXIS_TYPE_UNKNOWN未知轴类型，通常作为初始值。AXIS_TYPE_SCROLL_VERTICAL垂直滚动轴，当您滚动鼠标滚轮或在触控板上进行单指或双指滑动时，垂直滚动轴的状态改变。AXIS_TYPE_SCROLL_HORIZONTAL水平滚动轴，当您滚动鼠标滚轮或在触控板上进行双指滑动时，水平滚动轴的状态发生变化。AXIS_TYPE_PINCH捏合轴，用于描述触控板上的双指捏合手势。AXIS_TYPE_ROTATE旋转轴，用于描述触控板上的双指旋转手势。

#### InputEvent_AxisEventType

```ets
enum InputEvent_AxisEventType
```

**描述**

输入设备的轴事件类型。

**起始版本：** 12

枚举项描述AXIS_EVENT_TYPE_PINCH = 1

双指捏合事件，包含AXIS_TYPE_PINCH和AXIS_TYPE_ROTATE两种轴类型。

**起始版本：** 12。

AXIS_EVENT_TYPE_SCROLL = 2

滚轴事件，包含AXIS_TYPE_SCROLL_VERTICAL和AXIS_TYPE_SCROLL_HORIZONTAL两种轴类型，其中鼠标滚轮事件仅包含AXIS_TYPE_SCROLL_VERTICAL一种轴类型。

**起始版本：** 12。

#### InputEvent_AxisAction

```ets
enum InputEvent_AxisAction
```

**描述**

轴事件动作。

**起始版本：** 12

枚举项描述AXIS_ACTION_CANCEL = 0取消轴输入事件。AXIS_ACTION_BEGIN开始轴输入事件。AXIS_ACTION_UPDATE轴输入事件中。AXIS_ACTION_END结束轴输入事件。