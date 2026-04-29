# hid_ddk_types.h

**概述**

提供HID DDK中的枚举变量与结构体定义。

引用文件： <hid/hid_ddk_types.h>

库： libhid.z.so

系统能力： SystemCapability.Driver.HID.Extension

起始版本： 11

相关模块： [HidDdk](HidDdk.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Hid_EmitItem | Hid_EmitItem | 事件信息。 |
| Hid_Device | Hid_Device | 设备基本信息。 |
| Hid_EventTypeArray | Hid_EventTypeArray | 事件类型编码数组。 |
| Hid_KeyCodeArray | Hid_KeyCodeArray | 键值属性数组。 |
| Hid_AbsAxesArray | Hid_AbsAxesArray | 绝对坐标属性数组。 |
| Hid_RelAxesArray | Hid_RelAxesArray | 相对坐标属性数组。 |
| Hid_MscEventArray | Hid_MscEventArray | 其它特殊事件属性数组。 |
| Hid_EventProperties | Hid_EventProperties | 设备关注事件属性。 |
| Hid_RawDevInfo | Hid_RawDevInfo | 原始设备信息定义。 |
| Hid_DeviceHandle | Hid_DeviceHandle | 不透明的USB HID设备结构。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Hid_DeviceProp | Hid_DeviceProp | 输入设备特性定义。 |
| Hid_EventType | Hid_EventType | 事件类型。 |
| Hid_SynEvent | Hid_SynEvent | 同步事件编码。 |
| Hid_KeyCode | Hid_KeyCode | 键值编码。 |
| Hid_AbsAxes | Hid_AbsAxes | 绝对坐标编码。 |
| Hid_RelAxes | Hid_RelAxes | 相对坐标编码。 |
| Hid_MscEvent | Hid_MscEvent | 不适合其它类型的输入事件编码。 |
| Hid_DdkErrCode | Hid_DdkErrCode | HID DDK错误码定义。 |
| Hid_ReportType | Hid_ReportType | 报告（HID设备与主机之间交换的数据包）类型定义。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| HID_MAX_REPORT_BUFFER_SIZE (16 * 1024 - 1) | 最大报告缓冲区大小。 |

**枚举类型说明**

**Hid_DeviceProp**

```ets
enum Hid_DeviceProp
```

描述

输入设备特性定义。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_PROP_POINTER = 0x00 | 指针设备 |
| HID_PROP_DIRECT = 0x01 | 直接输入设备 |
| HID_PROP_BUTTON_PAD = 0x02 | 底部按键触摸设备 |
| HID_PROP_SEMI_MT = 0x03 | 全多点触控设备 |
| HID_PROP_TOP_BUTTON_PAD = 0x04 | 顶部软按键触摸设备 |
| HID_PROP_POINTING_STICK = 0x05 | 指点杆设备 |
| HID_PROP_ACCELEROMETER = 0x06 | 加速度传感器设备 |

**Hid_EventType**

```ets
enum Hid_EventType
```

描述

事件类型。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_EV_SYN = 0x00 | 同步事件 |
| HID_EV_KEY = 0x01 | 按键事件 |
| HID_EV_REL = 0x02 | 相对坐标事件 |
| HID_EV_ABS = 0x03 | 绝对坐标事件 |
| HID_EV_MSC = 0x04 | 特殊事件 |

**Hid_SynEvent**

```ets
enum Hid_SynEvent
```

描述

同步事件编码。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_SYN_REPORT = 0 | 表示一个事件的结束 |
| HID_SYN_CONFIG = 1 | 表示配置同步 |
| HID_SYN_MT_REPORT = 2 | 表示多点触摸的ABS数据包结束 |
| HID_SYN_DROPPED = 3 | 表示该事件被丢弃 |

**Hid_KeyCode**

```ets
enum Hid_KeyCode
```

描述

键值编码。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_KEY_A = 30 | 键A |
| HID_KEY_B = 48 | 键B |
| HID_KEY_C = 46 | 键C |
| HID_KEY_D = 32 | 键D |
| HID_KEY_E = 18 | 键E |
| HID_KEY_F = 33 | 键F |
| HID_KEY_G = 34 | 键G |
| HID_KEY_H = 35 | 键H |
| HID_KEY_I = 23 | 键I |
| HID_KEY_J = 36 | 键J |
| HID_KEY_K = 37 | 键K |
| HID_KEY_L = 38 | 键L |
| HID_KEY_M = 50 | 键M |
| HID_KEY_N = 49 | 键N |
| HID_KEY_O = 24 | 键O |
| HID_KEY_P = 25 | 键P |
| HID_KEY_Q = 16 | 键Q |
| HID_KEY_R = 19 | 键R |
| HID_KEY_S = 31 | 键S |
| HID_KEY_T = 20 | 键T |
| HID_KEY_U = 22 | 键U |
| HID_KEY_V = 47 | 键V |
| HID_KEY_W = 17 | 键W |
| HID_KEY_X = 45 | 键X |
| HID_KEY_Y = 21 | 键Y |
| HID_KEY_Z = 44 | 键Z |
| HID_KEY_ESC = 1 | 键ESC |
| HID_KEY_0 = 11 | 键0 |
| HID_KEY_1 = 2 | 键1 |
| HID_KEY_2 = 3 | 键2 |
| HID_KEY_3 = 4 | 键3 |
| HID_KEY_4 = 5 | 键4 |
| HID_KEY_5 = 6 | 键5 |
| HID_KEY_6 = 7 | 键6 |
| HID_KEY_7 = 8 | 键7 |
| HID_KEY_8 = 9 | 键8 |
| HID_KEY_9 = 10 | 键9 |
| HID_KEY_GRAVE = 41 | 键` |
| HID_KEY_MINUS = 12 | 键- |
| HID_KEY_EQUALS = 13 | 键= |
| HID_KEY_BACKSPACE = 14 | 键退格 |
| HID_KEY_LEFT_BRACKET = 26 | 键[ |
| HID_KEY_RIGHT_BRACKET = 27 | 键] |
| HID_KEY_ENTER = 28 | 键回车 |
| HID_KEY_LEFT_SHIFT = 42 | 键左shift |
| HID_KEY_BACKSLASH = 43 | 键\ |
| HID_KEY_SEMICOLON = 39 | 键; |
| HID_KEY_APOSTROPHE = 40 | 键' |
| HID_KEY_SPACE = 57 | 键空格 |
| HID_KEY_SLASH = 53 | 键 |
| HID_KEY_COMMA = 51 | 键, |
| HID_KEY_PERIOD = 52 | 键. |
| HID_KEY_RIGHT_SHIFT = 54 | 键右shift |
| HID_KEY_NUMPAD_0 = 82 | 数字键0 |
| HID_KEY_NUMPAD_1 = 79 | 数字键1 |
| HID_KEY_NUMPAD_2 = 80 | 数字键2 |
| HID_KEY_NUMPAD_3 = 81 | 数字键3 |
| HID_KEY_NUMPAD_4 = 75 | 数字键4 |
| HID_KEY_NUMPAD_5 = 76 | 数字键5 |
| HID_KEY_NUMPAD_6 = 77 | 数字键6 |
| HID_KEY_NUMPAD_7 = 71 | 数字键7 |
| HID_KEY_NUMPAD_8 = 72 | 数字键8 |
| HID_KEY_NUMPAD_9 = 73 | 数字键9 |
| HID_KEY_NUMPAD_DIVIDE = 70 | 数字键 |
| HID_KEY_NUMPAD_MULTIPLY = 55 | 数字键 |
| HID_KEY_NUMPAD_SUBTRACT = 74 | 数字键- |
| HID_KEY_NUMPAD_ADD = 78 | 数字键+ |
| HID_KEY_NUMPAD_DOT = 83 | 数字键. |
| HID_KEY_SYSRQ = 99 | 键打印屏幕 |
| HID_KEY_DELETE = 111 | 键删除 |
| HID_KEY_MUTE = 113 | 键静音 |
| HID_KEY_VOLUME_DOWN = 114 | 键音量- |
| HID_KEY_VOLUME_UP = 115 | 键音量+ |
| HID_KEY_BRIGHTNESS_DOWN = 224 | 键亮度- |
| HID_KEY_BRIGHTNESS_UP = 225 | 键亮度+ |
| HID_BTN_0 = 0x100 | 按钮0 |
| HID_BTN_1 = 0x101 | 按钮1 |
| HID_BTN_2 = 0x102 | 按钮2 |
| HID_BTN_3 = 0x103 | 按钮3 |
| HID_BTN_4 = 0x104 | 按钮4 |
| HID_BTN_5 = 0x105 | 按钮5 |
| HID_BTN_6 = 0x106 | 按钮6 |
| HID_BTN_7 = 0x107 | 按钮7 |
| HID_BTN_8 = 0x108 | 按钮8 |
| HID_BTN_9 = 0x109 | 按钮9 |
| HID_BTN_LEFT = 0x110 | 鼠标按键左键 |
| HID_BTN_RIGHT = 0x111 | 鼠标按键右键 |
| HID_BTN_MIDDLE = 0x112 | 鼠标按键中键 |
| HID_BTN_SIDE = 0x113 | 鼠标侧面按键 |
| HID_BTN_EXTRA = 0x114 | 鼠标附加按键 |
| HID_BTN_FORWARD = 0x115 | 鼠标向前按键 |
| HID_BTN_BACKWARD = 0x116 | 鼠标向后按键 |
| HID_BTN_TASK = 0x117 | 鼠标任务按键 |
| HID_BTN_TOOL_PEN = 0x140 | 画笔 |
| HID_BTN_TOOL_RUBBER = 0x141 | 橡皮擦 |
| HID_BTN_TOOL_BRUSH = 0x142 | 笔刷 |
| HID_BTN_TOOL_PENCIL = 0x143 | 钢笔 |
| HID_BTN_TOOL_AIRBRUSH = 0x144 | 喷枪 |
| HID_BTN_TOOL_FINGER = 0x145 | 手指 |
| HID_BTN_TOOL_MOUSE = 0x146 | 鼠标 |
| HID_BTN_TOOL_LENS = 0x147 | 镜头 |
| HID_BTN_TOOL_QUINT_TAP = 0x148 | 五指触控 |
| HID_BTN_STYLUS3 = 0x149 | 手写笔3 |
| HID_BTN_TOUCH = 0x14a | 触摸 |
| HID_BTN_STYLUS = 0x14b | 手写笔 |
| HID_BTN_STYLUS2 = 0x14c | 手写笔2 |
| HID_BTN_TOOL_DOUBLE_TAP = 0x14d | 二指触控 |
| HID_BTN_TOOL_TRIPLE_TAP = 0x14e | 三指触控 |
| HID_BTN_TOOL_QUAD_TAP = 0x14f | 四指触控 |
| HID_BTN_WHEEL = 0x150 | 滚轮 |

**Hid_AbsAxes**

```ets
enum Hid_AbsAxes
```

描述

绝对坐标编码。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_ABS_X = 0x00 | X轴 |
| HID_ABS_Y = 0x01 | Y轴 |
| HID_ABS_Z = 0x02 | Z轴 |
| HID_ABS_RX = 0x03 | 右模拟摇杆的 X 轴 |
| HID_ABS_RY = 0x04 | 右模拟摇杆的 Y 轴 |
| HID_ABS_RZ = 0x05 | 右模拟摇杆的 Z 轴 |
| HID_ABS_THROTTLE = 0x06 | 油门 |
| HID_ABS_RUDDER = 0x07 | 舵 |
| HID_ABS_WHEEL = 0x08 | 滚轮 |
| HID_ABS_GAS = 0x09 | 气 |
| HID_ABS_BRAKE = 0x0a | 制动 |
| HID_ABS_HAT0X = 0x10 | HAT0X |
| HID_ABS_HAT0Y = 0x11 | HAT0Y |
| HID_ABS_HAT1X = 0x12 | HAT1X |
| HID_ABS_HAT1Y = 0x13 | HAT1Y |
| HID_ABS_HAT2X = 0x14 | HAT2X |
| HID_ABS_HAT2Y = 0x15 | HAT2Y |
| HID_ABS_HAT3X = 0x16 | HAT3X |
| HID_ABS_HAT3Y = 0x17 | HAT3Y |
| HID_ABS_PRESSURE = 0x18 | 压力 |
| HID_ABS_DISTANCE = 0x19 | 距离 |
| HID_ABS_TILT_X = 0x1a | X轴倾斜度 |
| HID_ABS_TILT_Y = 0x1b | Y轴倾斜度 |
| HID_ABS_TOOL_WIDTH = 0x1c | 触摸工具的宽度 |
| HID_ABS_VOLUME = 0x20 | 音量 |
| HID_ABS_MISC = 0x28 | 其它 |

**Hid_RelAxes**

```ets
enum Hid_RelAxes
```

描述

相对坐标编码。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_REL_X = 0x00 | X轴 |
| HID_REL_Y = 0x01 | Y轴 |
| HID_REL_Z = 0x02 | Z轴 |
| HID_REL_RX = 0x03 | 右模拟摇杆的 X 轴 |
| HID_REL_RY = 0x04 | 右模拟摇杆的 Y 轴 |
| HID_REL_RZ = 0x05 | 右模拟摇杆的 Z 轴 |
| HID_REL_HWHEEL = 0x06 | 水平滚轮 |
| HID_REL_DIAL = 0x07 | 刻度 |
| HID_REL_WHEEL = 0x08 | 滚轮 |
| HID_REL_MISC = 0x09 | 其它 |
| HID_REL_RESERVED = 0x0a | 预留 |
| HID_REL_WHEEL_HI_RES = 0x0b | 高分辨率滚轮 |
| HID_REL_HWHEEL_HI_RES = 0x0c | 高分辨率水平滚轮 |

**Hid_MscEvent**

```ets
enum Hid_MscEvent
```

描述

不适合其它类型的输入事件编码。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_MSC_SERIAL = 0x00 | 序列号 |
| HID_MSC_PULSE_LED = 0x01 | 脉冲 |
| HID_MSC_GESTURE = 0x02 | 手势 |
| HID_MSC_RAW = 0x03 | 开始事件 |
| HID_MSC_SCAN = 0x04 | 扫描 |
| HID_MSC_TIMESTAMP = 0x05 | 时间戳 |

**Hid_DdkErrCode**

```ets
enum Hid_DdkErrCode
```

描述

HID DDK错误码定义。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| HID_DDK_SUCCESS = 0 | 操作成功。 |
| HID_DDK_NO_PERM = 201 | 没有权限，从API 16起，取值由-6变更为201。 |
| HID_DDK_INVALID_PARAMETER = 401 | 非法参数，从API 16起，取值由-2变更为401。 |
| HID_DDK_FAILURE = 27300001 | 操作失败，从API 16起，取值由-1变更为27300001。 |
| HID_DDK_NULL_PTR = 27300002 | 空指针异常，从API 16起，取值由-4变更为27300002。 |
| HID_DDK_INVALID_OPERATION = 27300003 | 非法操作，从API 16起，取值由-3变更为27300003。 |
| HID_DDK_TIMEOUT = 27300004 | 超时，从API 16起，取值由-5变更为27300004。 |
| HID_DDK_INIT_ERROR = 27300005 | 初始化DDK失败或DDK未初始化。  起始版本： 18 |
| HID_DDK_SERVICE_ERROR = 27300006 | 服务通信过程中错误。  起始版本： 18 |
| HID_DDK_MEMORY_ERROR = 27300007 | 内存相关的错误，包括：内存数据拷贝失败、内存申请失败等。  起始版本： 18 |
| HID_DDK_IO_ERROR = 27300008 | I/O操作失败。  起始版本： 18 |
| HID_DDK_DEVICE_NOT_FOUND = 27300009 | 设备未找到。  起始版本： 18 |

**Hid_ReportType**

```ets
enum Hid_ReportType
```

描述

报告（HID设备与主机之间交换的数据包）类型定义。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| HID_INPUT_REPORT = 0 | 输入报告 |
| HID_OUTPUT_REPORT = 1 | 输出报告 |
| HID_FEATURE_REPORT = 2 | 特性报告 |

**HID_MAX_REPORT_BUFFER_SIZE**

```ets
HID_MAX_REPORT_BUFFER_SIZE (16 * 1024 - 1)
```

描述

最大报告缓冲区大小。

起始版本： 18