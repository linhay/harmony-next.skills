# ArkUI_NativeGestureAPI_2

```ets
typedef struct {...} ArkUI_NativeGestureAPI_2
```

#### 概述

定义手势模块接口集合。

**起始版本：** 18

**相关模块：**[ArkUI_NativeModule](../system-services/ArkUI_NativeModule.md)

**所在头文件：**[native_gesture.h](../../capi/headers/native_gesture.h.md)

#### 汇总

#### 成员变量

名称描述[ArkUI_NativeGestureAPI_1](ArkUI_NativeGestureAPI_1.md)* gestureApi1指向ArkUI_NativeGestureAPI_1结构体的指针。

#### 成员函数

名称描述[int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void* userData,ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))](#ZH-CN_TOPIC_0000002497445122__setgestureinterruptertonode)设置手势中断事件的回调函数。

#### 成员函数说明

#### setGestureInterrupterToNode()

```ets
int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void* userData,ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))
```

**描述：**

设置手势中断事件的回调函数。

**参数：**

参数项描述[ArkUI_NodeHandle](../components/ArkUI_Node_.md) node需要被设置手势打断回调的ArkUI节点。void* userData用户自定义数据。interrupter打断回调，info返回手势打断数据。interrupter 返回 GESTURE_INTERRUPT_RESULT_CONTINUE，手势正常进行； 返回 GESTURE_INTERRUPT_RESULT_REJECT 手势打断。

**返回：**

类型说明int32_t

0 - 成功。

 401 - 参数错误。