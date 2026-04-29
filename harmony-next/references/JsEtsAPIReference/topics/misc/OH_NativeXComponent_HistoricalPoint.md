# OH_NativeXComponent_HistoricalPoint

```ets
typedef struct {...} OH_NativeXComponent_HistoricalPoint
```

**概述**

历史接触点

起始版本： 10

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
| float titlX | 平面X-Y上的投影与当前触摸事件的Z轴之间的角度。 |
| float titlY | 当前触摸事件在平面Y-Z和轴Z上的投影之间的角度。 |
| OH_NativeXComponent_TouchEvent_SourceTool sourceTool | 当前触摸事件的源工具。 |