# OH_NativeXComponent_TouchEvent

```ets
typedef struct {...} OH_NativeXComponent_TouchEvent
```

**概述**

触摸事件。

起始版本： 8

相关模块： [OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

所在头文件： [native_interface_xcomponent.h](native_interface_xcomponent.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t id | 手指的唯一标识符。 |
| float screenX | 触摸点相对于XComponent所在应用窗口左上角的x坐标。 |
| float screenY | 触摸点相对于XComponent所在应用窗口左上角的y坐标。 |
| float x | 触摸点相对于XComponent组件左边缘的x坐标。 |
| float y | 触摸点相对于XComponent组件上边缘的y坐标。 |
| OH_NativeXComponent_TouchEventType type | 触摸事件的触摸类型。 |
| double size | 指垫和屏幕之间的接触面积。 |
| float force | 当前触摸事件的压力。 |
| int64_t deviceId | 产生当前触摸事件的设备的ID。 |
| int64_t timeStamp | 当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| OH_NativeXComponent_TouchPoint touchPoints[OH_NATIVE_XCOMPONENT_MAX_TOUCH_POINTS_NUMBER] | 当前触摸点的数组。 |
| uint32_t numPoints | 当前接触点的数量，值为1时为单指触摸，大于1时为多指触摸。 |