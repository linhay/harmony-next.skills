# OH_NativeXComponent_MouseEvent

```ets
typedef struct {...} OH_NativeXComponent_MouseEvent
```

#### 概述

鼠标事件。

**起始版本：** 9

**相关模块：**[OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

**所在头文件：**[native_interface_xcomponent.h](../../capi/headers/native_interface_xcomponent.h.md)

#### 汇总

#### 成员变量

名称描述float x点击触点相对于当前组件左上角的x轴坐标。float y点击触点相对于当前组件左上角的y轴坐标。float screenX点击触点相对于XComponent所在应用屏幕左上角的x轴坐标。float screenY点击触点相对于XComponent所在应用屏幕左上角的y轴坐标。int64_t timestamp当前鼠标事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。[OH_NativeXComponent_MouseEventAction](../../capi/headers/native_interface_xcomponent.h.md#ZH-CN_TOPIC_0000002497605078__oh_nativexcomponent_mouseeventaction) action当前鼠标事件动作。[OH_NativeXComponent_MouseEventButton](../../capi/headers/native_interface_xcomponent.h.md#ZH-CN_TOPIC_0000002497605078__oh_nativexcomponent_mouseeventbutton) button鼠标事件按键。