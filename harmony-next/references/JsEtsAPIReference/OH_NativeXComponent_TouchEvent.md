# OH_NativeXComponent_TouchEvent

```ets
typedef struct {...} OH_NativeXComponent_TouchEvent
```

#### 概述

触摸事件。

**起始版本：** 8

**相关模块：**[OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

**所在头文件：**[native_interface_xcomponent.h](native_interface_xcomponent.h.md)

#### 汇总

#### 成员变量

名称描述int32_t id手指的唯一标识符。float screenX触摸点相对于XComponent所在应用窗口左上角的x坐标。float screenY触摸点相对于XComponent所在应用窗口左上角的y坐标。float x触摸点相对于XComponent组件左边缘的x坐标。float y触摸点相对于XComponent组件上边缘的y坐标。[OH_NativeXComponent_TouchEventType](native_interface_xcomponent.h.md#ZH-CN_TOPIC_0000002497605078__oh_nativexcomponent_toucheventtype) type触摸事件的触摸类型。double size指垫和屏幕之间的接触面积。float force当前触摸事件的压力。int64_t deviceId产生当前触摸事件的设备的ID。int64_t timeStamp当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。[OH_NativeXComponent_TouchPoint](OH_NativeXComponent_TouchPoint.md) touchPoints[[OH_NATIVE_XCOMPONENT_MAX_TOUCH_POINTS_NUMBER]](native_interface_xcomponent.h.md#ZH-CN_TOPIC_0000002497605078__变量)当前触摸点的数组。uint32_t numPoints当前接触点的数量，值为1时为单指触摸，大于1时为多指触摸。