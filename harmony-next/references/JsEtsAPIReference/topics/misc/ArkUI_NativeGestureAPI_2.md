# ArkUI_NativeGestureAPI_2

```ets
typedef struct {...} ArkUI_NativeGestureAPI_2
```

**概述**

定义手势模块接口集合。

起始版本： 18

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_gesture.h](native_gesture.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeGestureAPI_1* gestureApi1 | 指向ArkUI_NativeGestureAPI_1结构体的指针。 |

**成员函数**

| 名称 | 描述 |
| --- | --- |
| int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void* userData,ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info)) | 设置手势中断事件的回调函数。 |

**成员函数说明**

**setGestureInterrupterToNode()**

```ets
int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))
```

描述：

设置手势中断事件的回调函数。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要被设置手势打断回调的ArkUI节点指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info) | 打断回调，info返回手势打断数据。interrupter返回GESTURE_INTERRUPT_RESULT_CONTINUE，手势正常进行；返回GESTURE_INTERRUPT_RESULT_REJECT，手势打断。设置此参数为nullptr时将取消注册回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。  401 - 参数错误。 |