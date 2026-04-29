# OH_NativeXComponent_TouchPoint

```ets
typedef struct {...} OH_NativeXComponent_TouchPoint
```

**概述**

触摸事件中触摸点的信息。

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
| int64_t timeStamp | 当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| bool isPressed | 当前点是否被按下，按下时为true，离开时为false。 |