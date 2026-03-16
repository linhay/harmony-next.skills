# Input_InterceptorEventCallback

```ets
typedef struct Input_InterceptorEventCallback {...} Input_InterceptorEventCallback
```

#### 概述

拦截回调事件结构体，拦截鼠标事件、触屏输入事件和轴事件。

**起始版本：** 12

**相关模块：**[input](input.md)

**所在头文件：**[oh_input_manager.h](../../capi/headers/oh_input_manager.h.md)

#### 汇总

#### 成员变量

名称描述Input_MouseEventCallback mouseCallback

鼠标事件的回调函数。

**起始版本：** 12。

Input_TouchEventCallback touchCallback

触屏输入事件的回调函数。

**起始版本：** 12。

Input_AxisEventCallback axisCallback

轴事件的回调函数。

**起始版本：** 12。

#### 成员函数

名称typedef关键字描述[typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445541__input_keyeventcallback)Input_KeyEventCallback()

按键事件的回调函数，keyEvent的生命周期为回调函数内。

**起始版本：** 12。

[typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445541__input_mouseeventcallback)Input_MouseEventCallback()

鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。

**起始版本：** 12。

[typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445541__input_toucheventcallback)Input_TouchEventCallback()

触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。

**起始版本：** 12。

[typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)](#ZH-CN_TOPIC_0000002529445541__input_axiseventcallback)Input_AxisEventCallback()

轴事件的回调函数，axisEvent的生命周期为回调函数内。

**起始版本：** 12。

[typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)](#ZH-CN_TOPIC_0000002529445541__input_deviceaddedcallback)Input_DeviceAddedCallback()

回调函数，用于回调输入设备的热插事件。

**起始版本：** 13。

[typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)](#ZH-CN_TOPIC_0000002529445541__input_deviceremovedcallback)Input_DeviceRemovedCallback()

回调函数，用于回调输入设备的热拔事件。

**起始版本：** 13。

#### 成员函数说明

#### Input_KeyEventCallback()

```ets
typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)
```

**描述**

按键事件的回调函数，keyEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_KeyEvent](Input_KeyEvent.md)* keyEvent按键事件对象。

#### Input_MouseEventCallback()

```ets
typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)
```

**描述**

鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_MouseEvent](Input_MouseEvent.md)* mouseEvent鼠标事件对象。

#### Input_TouchEventCallback()

```ets
typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)
```

**描述**

触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_TouchEvent](Input_TouchEvent.md)* touchEvent触屏输入事件对象。

#### Input_AxisEventCallback()

```ets
typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)
```

**描述**

轴事件的回调函数，axisEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](Input_AxisEvent.md)* axisEvent轴事件对象。

#### Input_DeviceAddedCallback()

```ets
typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热插事件。

**起始版本：** 13

**参数：**

参数项描述int32_t deviceId输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

#### Input_DeviceRemovedCallback()

```ets
typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热拔事件。

**起始版本：** 13

**参数：**

参数项描述int32_t deviceId输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。