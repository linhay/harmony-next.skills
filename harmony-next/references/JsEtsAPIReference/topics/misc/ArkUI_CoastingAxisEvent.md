# ArkUI_CoastingAxisEvent

```ets
typedef struct ArkUI_CoastingAxisEvent ArkUI_CoastingAxisEvent
```

**概述**

定义惯性滚动轴事件。

当用户在触控板上用双指滑动时，系统会根据手指抬起时的速度，按照一定的衰减曲线构造滑动事件。可以监听此类事件，以便在常规轴事件之后立即处理抛滑效果。

仅当用户在触控板上双指抛滑，且指针位置下存在通过[registerNodeEvent](ArkUI_NativeNodeAPI_1.md#ZH-CN_TOPIC_0000002522081074__registernodeevent)注册了[NODE_ON_COASTING_AXIS_EVENT](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodeeventtype)事件的组件时，才能接收到此事件。

起始版本： 22

相关模块： [ArkUI_EventModule](ArkUI_EventModule.md)

所在头文件： [ui_input_event.h](ui_input_event.h.md)