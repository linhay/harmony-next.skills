# OH_NativeXComponent_MouseEvent_Callback

```ets
typedef struct OH_NativeXComponent_MouseEvent_Callback {...} OH_NativeXComponent_MouseEvent_Callback
```

#### 概述

注册鼠标事件的回调。

**起始版本：** 9

**相关模块：**[OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

**所在头文件：**[native_interface_xcomponent.h](../../capi/headers/native_interface_xcomponent.h.md)

#### 汇总

#### 成员函数

名称描述[void (*DispatchMouseEvent)(OH_NativeXComponent* component, void* window)](#ZH-CN_TOPIC_0000002529445079__dispatchmouseevent)当鼠标事件被触发时调用。[void (*DispatchHoverEvent)(OH_NativeXComponent* component, bool isHover)](#ZH-CN_TOPIC_0000002529445079__dispatchhoverevent)当悬停事件被触发时调用。

#### 成员函数说明

#### DispatchMouseEvent()

```ets
void (*DispatchMouseEvent)(OH_NativeXComponent* component, void* window)
```

**描述：**

当鼠标事件被触发时调用。

**起始版本：** 9

**参数：**

参数项描述[OH_NativeXComponent](OH_NativeXComponent.md)* component表示指向[OH_NativeXComponent](OH_NativeXComponent.md)实例的指针。void* window表示NativeWindow句柄。

#### DispatchHoverEvent()

```ets
void (*DispatchHoverEvent)(OH_NativeXComponent* component, bool isHover)
```

**描述：**

当悬停事件被触发时调用。

**起始版本：** 9

**参数：**

参数项描述[OH_NativeXComponent](OH_NativeXComponent.md)* component表示指向[OH_NativeXComponent](OH_NativeXComponent.md)实例的指针。bool isHover表示鼠标或手写笔是否悬浮在组件上，进入时为true，离开时为false。