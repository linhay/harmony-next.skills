# hid_ddk_types.h

#### 概述

提供HID DDK中的枚举变量与结构体定义。

**引用文件：** <hid/hid_ddk_types.h>

**库：** libhid.z.so

**系统能力：** SystemCapability.Driver.HID.Extension

**起始版本：** 11

**相关模块：**[HidDdk](HidDdk.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Hid_EmitItem](Hid_EmitItem.md)Hid_EmitItem事件信息。[Hid_Device](Hid_Device.md)Hid_Device设备基本信息。[Hid_EventTypeArray](Hid_EventTypeArray.md)Hid_EventTypeArray事件类型编码数组。[Hid_KeyCodeArray](Hid_KeyCodeArray.md)Hid_KeyCodeArray键值属性数组。[Hid_AbsAxesArray](Hid_AbsAxesArray.md)Hid_AbsAxesArray绝对坐标属性数组。[Hid_RelAxesArray](Hid_RelAxesArray.md)Hid_RelAxesArray相对坐标属性数组。[Hid_MscEventArray](Hid_MscEventArray.md)Hid_MscEventArray其它特殊事件属性数组。[Hid_EventProperties](Hid_EventProperties.md)Hid_EventProperties设备关注事件属性。[Hid_RawDevInfo](Hid_RawDevInfo.md)Hid_RawDevInfo原始设备信息定义。[Hid_DeviceHandle](Hid_DeviceHandle.md)Hid_DeviceHandle不透明的USB HID设备结构。

#### 枚举

名称typedef关键字描述[Hid_DeviceProp](#ZH-CN_TOPIC_0000002529445575__hid_deviceprop)Hid_DeviceProp输入设备特性定义。[Hid_EventType](#ZH-CN_TOPIC_0000002529445575__hid_eventtype)Hid_EventType事件类型。[Hid_SynEvent](#ZH-CN_TOPIC_0000002529445575__hid_synevent)Hid_SynEvent同步事件编码。[Hid_KeyCode](#ZH-CN_TOPIC_0000002529445575__hid_keycode)Hid_KeyCode键值编码。[Hid_AbsAxes](#ZH-CN_TOPIC_0000002529445575__hid_absaxes)Hid_AbsAxes绝对坐标编码。[Hid_RelAxes](#ZH-CN_TOPIC_0000002529445575__hid_relaxes)Hid_RelAxes相对坐标编码。[Hid_MscEvent](#ZH-CN_TOPIC_0000002529445575__hid_mscevent)Hid_MscEvent不适合其它类型的输入事件编码。[Hid_DdkErrCode](#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode)Hid_DdkErrCodeHID DDK错误码定义。[Hid_ReportType](#ZH-CN_TOPIC_0000002529445575__hid_reporttype)Hid_ReportType报告（HID设备与主机之间交换的数据包）类型定义。

#### 宏定义

名称描述HID_MAX_REPORT_BUFFER_SIZE (16 * 1024 - 1)最大报告缓冲区大小。

#### 枚举类型说明

#### Hid_DeviceProp

```ets
enum Hid_DeviceProp
```

**描述**

输入设备特性定义。

**起始版本：** 11

枚举项描述HID_PROP_POINTER = 0x00指针设备HID_PROP_DIRECT = 0x01直接输入设备HID_PROP_BUTTON_PAD = 0x02底部按键触摸设备HID_PROP_SEMI_MT = 0x03全多点触控设备HID_PROP_TOP_BUTTON_PAD = 0x04顶部软按键触摸设备HID_PROP_POINTING_STICK = 0x05指点杆设备HID_PROP_ACCELEROMETER = 0x06加速度传感器设备

#### Hid_EventType

```ets
enum Hid_EventType
```

**描述**

事件类型。

**起始版本：** 11

枚举项描述HID_EV_SYN = 0x00同步事件HID_EV_KEY = 0x01按键事件HID_EV_REL = 0x02相对坐标事件HID_EV_ABS = 0x03绝对坐标事件HID_EV_MSC = 0x04特殊事件

#### Hid_SynEvent

```ets
enum Hid_SynEvent
```

**描述**

同步事件编码。

**起始版本：** 11

枚举项描述HID_SYN_REPORT = 0表示一个事件的结束HID_SYN_CONFIG = 1表示配置同步HID_SYN_MT_REPORT = 2表示多点触摸的ABS数据包结束HID_SYN_DROPPED = 3表示该事件被丢弃

#### Hid_KeyCode

```ets
enum Hid_KeyCode
```

**描述**

键值编码。

**起始版本：** 11

枚举项描述HID_KEY_A = 30键AHID_KEY_B = 48键BHID_KEY_C = 46键CHID_KEY_D = 32键DHID_KEY_E = 18键EHID_KEY_F = 33键FHID_KEY_G = 34键GHID_KEY_H = 35键HHID_KEY_I = 23键IHID_KEY_J = 36键JHID_KEY_K = 37键KHID_KEY_L = 38键LHID_KEY_M = 50键MHID_KEY_N = 49键NHID_KEY_O = 24键OHID_KEY_P = 25键PHID_KEY_Q = 16键QHID_KEY_R = 19键RHID_KEY_S = 31键SHID_KEY_T = 20键THID_KEY_U = 22键UHID_KEY_V = 47键VHID_KEY_W = 17键WHID_KEY_X = 45键XHID_KEY_Y = 21键YHID_KEY_Z = 44键ZHID_KEY_ESC = 1键ESCHID_KEY_0 = 11键0HID_KEY_1 = 2键1HID_KEY_2 = 3键2HID_KEY_3 = 4键3HID_KEY_4 = 5键4HID_KEY_5 = 6键5HID_KEY_6 = 7键6HID_KEY_7 = 8键7HID_KEY_8 = 9键8HID_KEY_9 = 10键9HID_KEY_GRAVE = 41键`HID_KEY_MINUS = 12键-HID_KEY_EQUALS = 13键=HID_KEY_BACKSPACE = 14键退格HID_KEY_LEFT_BRACKET = 26键[HID_KEY_RIGHT_BRACKET = 27键]HID_KEY_ENTER = 28键回车HID_KEY_LEFT_SHIFT = 42键左shiftHID_KEY_BACKSLASH = 43键\HID_KEY_SEMICOLON = 39键;HID_KEY_APOSTROPHE = 40键'HID_KEY_SPACE = 57键空格HID_KEY_SLASH = 53键HID_KEY_COMMA = 51键,HID_KEY_PERIOD = 52键.HID_KEY_RIGHT_SHIFT = 54键右shiftHID_KEY_NUMPAD_0 = 82数字键0HID_KEY_NUMPAD_1 = 79数字键1HID_KEY_NUMPAD_2 = 80数字键2HID_KEY_NUMPAD_3 = 81数字键3HID_KEY_NUMPAD_4 = 75数字键4HID_KEY_NUMPAD_5 = 76数字键5HID_KEY_NUMPAD_6 = 77数字键6HID_KEY_NUMPAD_7 = 71数字键7HID_KEY_NUMPAD_8 = 72数字键8HID_KEY_NUMPAD_9 = 73数字键9HID_KEY_NUMPAD_DIVIDE = 70数字键HID_KEY_NUMPAD_MULTIPLY = 55数字键HID_KEY_NUMPAD_SUBTRACT = 74数字键-HID_KEY_NUMPAD_ADD = 78数字键+HID_KEY_NUMPAD_DOT = 83数字键.HID_KEY_SYSRQ = 99键打印屏幕HID_KEY_DELETE = 111键删除HID_KEY_MUTE = 113键静音HID_KEY_VOLUME_DOWN = 114键音量-HID_KEY_VOLUME_UP = 115键音量+HID_KEY_BRIGHTNESS_DOWN = 224键亮度-HID_KEY_BRIGHTNESS_UP = 225键亮度+HID_BTN_0 = 0x100按钮0HID_BTN_1 = 0x101按钮1HID_BTN_2 = 0x102按钮2HID_BTN_3 = 0x103按钮3HID_BTN_4 = 0x104按钮4HID_BTN_5 = 0x105按钮5HID_BTN_6 = 0x106按钮6HID_BTN_7 = 0x107按钮7HID_BTN_8 = 0x108按钮8HID_BTN_9 = 0x109按钮9HID_BTN_LEFT = 0x110鼠标按键左键HID_BTN_RIGHT = 0x111鼠标按键右键HID_BTN_MIDDLE = 0x112鼠标按键中键HID_BTN_SIDE = 0x113鼠标侧面按键HID_BTN_EXTRA = 0x114鼠标附加按键HID_BTN_FORWARD = 0x115鼠标向前按键HID_BTN_BACKWARD = 0x116鼠标向后按键HID_BTN_TASK = 0x117鼠标任务按键HID_BTN_TOOL_PEN = 0x140画笔HID_BTN_TOOL_RUBBER = 0x141橡皮擦HID_BTN_TOOL_BRUSH = 0x142笔刷HID_BTN_TOOL_PENCIL = 0x143钢笔HID_BTN_TOOL_AIRBRUSH = 0x144喷枪HID_BTN_TOOL_FINGER = 0x145手指HID_BTN_TOOL_MOUSE = 0x146鼠标HID_BTN_TOOL_LENS = 0x147镜头HID_BTN_TOOL_QUINT_TAP = 0x148五指触控HID_BTN_STYLUS3 = 0x149手写笔3HID_BTN_TOUCH = 0x14a触摸HID_BTN_STYLUS = 0x14b手写笔HID_BTN_STYLUS2 = 0x14c手写笔2HID_BTN_TOOL_DOUBLE_TAP = 0x14d二指触控HID_BTN_TOOL_TRIPLE_TAP = 0x14e三指触控HID_BTN_TOOL_QUAD_TAP = 0x14f四指触控HID_BTN_WHEEL = 0x150滚轮

#### Hid_AbsAxes

```ets
enum Hid_AbsAxes
```

**描述**

绝对坐标编码。

**起始版本：** 11

枚举项描述HID_ABS_X = 0x00X轴HID_ABS_Y = 0x01Y轴HID_ABS_Z = 0x02Z轴HID_ABS_RX = 0x03右模拟摇杆的 X 轴HID_ABS_RY = 0x04右模拟摇杆的 Y 轴HID_ABS_RZ = 0x05右模拟摇杆的 Z 轴HID_ABS_THROTTLE = 0x06油门HID_ABS_RUDDER = 0x07舵HID_ABS_WHEEL = 0x08滚轮HID_ABS_GAS = 0x09气HID_ABS_BRAKE = 0x0a制动HID_ABS_HAT0X = 0x10HAT0XHID_ABS_HAT0Y = 0x11HAT0YHID_ABS_HAT1X = 0x12HAT1XHID_ABS_HAT1Y = 0x13HAT1YHID_ABS_HAT2X = 0x14HAT2XHID_ABS_HAT2Y = 0x15HAT2YHID_ABS_HAT3X = 0x16HAT3XHID_ABS_HAT3Y = 0x17HAT3YHID_ABS_PRESSURE = 0x18压力HID_ABS_DISTANCE = 0x19距离HID_ABS_TILT_X = 0x1aX轴倾斜度HID_ABS_TILT_Y = 0x1bY轴倾斜度HID_ABS_TOOL_WIDTH = 0x1c触摸工具的宽度HID_ABS_VOLUME = 0x20音量HID_ABS_MISC = 0x28其它

#### Hid_RelAxes

```ets
enum Hid_RelAxes
```

**描述**

相对坐标编码。

**起始版本：** 11

枚举项描述HID_REL_X = 0x00X轴HID_REL_Y = 0x01Y轴HID_REL_Z = 0x02Z轴HID_REL_RX = 0x03右模拟摇杆的 X 轴HID_REL_RY = 0x04右模拟摇杆的 Y 轴HID_REL_RZ = 0x05右模拟摇杆的 Z 轴HID_REL_HWHEEL = 0x06水平滚轮HID_REL_DIAL = 0x07刻度HID_REL_WHEEL = 0x08滚轮HID_REL_MISC = 0x09其它HID_REL_RESERVED = 0x0a预留HID_REL_WHEEL_HI_RES = 0x0b高分辨率滚轮HID_REL_HWHEEL_HI_RES = 0x0c高分辨率水平滚轮

#### Hid_MscEvent

```ets
enum Hid_MscEvent
```

**描述**

不适合其它类型的输入事件编码。

**起始版本：** 11

枚举项描述HID_MSC_SERIAL = 0x00序列号HID_MSC_PULSE_LED = 0x01脉冲HID_MSC_GESTURE = 0x02手势HID_MSC_RAW = 0x03开始事件HID_MSC_SCAN = 0x04扫描HID_MSC_TIMESTAMP = 0x05时间戳

#### Hid_DdkErrCode

```ets
enum Hid_DdkErrCode
```

**描述**

HID DDK错误码定义。

**起始版本：** 11

枚举项描述HID_DDK_SUCCESS = 0操作成功。HID_DDK_NO_PERM = 201没有权限，从API 16起，取值由-6变更为201。HID_DDK_INVALID_PARAMETER = 401非法参数，从API 16起，取值由-2变更为401。HID_DDK_FAILURE = 27300001操作失败，从API 16起，取值由-1变更为27300001。HID_DDK_NULL_PTR = 27300002空指针异常，从API 16起，取值由-4变更为27300002。HID_DDK_INVALID_OPERATION = 27300003非法操作，从API 16起，取值由-3变更为27300003。HID_DDK_TIMEOUT = 27300004超时，从API 16起，取值由-5变更为27300004。HID_DDK_INIT_ERROR = 27300005

初始化DDK失败或DDK未初始化。

**起始版本：** 18

HID_DDK_SERVICE_ERROR = 27300006

服务通信过程中错误。

**起始版本：** 18

HID_DDK_MEMORY_ERROR = 27300007

内存相关的错误，包括：内存数据拷贝失败、内存申请失败等。

**起始版本：** 18

HID_DDK_IO_ERROR = 27300008

I/O操作失败。

**起始版本：** 18

HID_DDK_DEVICE_NOT_FOUND = 27300009

设备未找到。

**起始版本：** 18

#### Hid_ReportType

```ets
enum Hid_ReportType
```

**描述**

报告（HID设备与主机之间交换的数据包）类型定义。

**起始版本：** 18

枚举项描述HID_INPUT_REPORT = 0输入报告HID_OUTPUT_REPORT = 1输出报告HID_FEATURE_REPORT = 2特性报告

#### HID_MAX_REPORT_BUFFER_SIZE

```ets
HID_MAX_REPORT_BUFFER_SIZE (16 * 1024 - 1)
```

**描述**

最大报告缓冲区大小。

**起始版本：** 18