# ArkUI_TouchTestInfo

```ets
typedef struct ArkUI_TouchTestInfo ArkUI_TouchTestInfo
```

**概述**

定义触摸测试信息。

当用户通过[registerNodeEvent](ArkUI_NativeNodeAPI_1.md#ZH-CN_TOPIC_0000002522081074__registernodeevent)注册了[NODE_ON_CHILD_TOUCH_TEST](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodeeventtype)事件时，才能接收到此事件。触摸测试信息包含触摸测试策略、命中测试过程中需要作用的子组件ID和触摸测试信息项的列表。

起始版本： 22

相关模块： [ArkUI_EventModule](ArkUI_EventModule.md)

所在头文件： [ui_input_event.h](ui_input_event.h.md)