# native_key_event.h

**概述**

提供NativeKeyEvent相关接口定义。

引用文件： <arkui/native_key_event.h>

库： libace_ndk.z.so

系统能力： SystemCapability.ArkUI.ArkUI.Full

起始版本： 14

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

相关示例： [NdkKeyEvent](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkKeyEvent)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_KeyCode | ArkUI_KeyCode | 按键事件的键码。 |
| ArkUI_KeyEventType | ArkUI_KeyEventType | 按键的类型。 |
| ArkUI_KeySourceType | ArkUI_KeySourceType | 触发当前按键的输入设备类型。 |
| ArkUI_KeyIntension | ArkUI_KeyIntension | 按键对应的意图。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| ArkUI_KeyEventType OH_ArkUI_KeyEvent_GetType(const ArkUI_UIInputEvent* event) | 获取按键的类型。 |
| int32_t OH_ArkUI_KeyEvent_GetKeyCode(const ArkUI_UIInputEvent* event) | 获取按键的键码。 |
| const char OH_ArkUI_KeyEvent_GetKeyText(const ArkUI_UIInputEvent event) | 获取按键的键值。 |
| ArkUI_KeySourceType OH_ArkUI_KeyEvent_GetKeySource(const ArkUI_UIInputEvent* event) | 获取当前按键的输入设备类型。 |
| void OH_ArkUI_KeyEvent_StopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation) | 阻塞事件冒泡传递。 |
| ArkUI_KeyIntension OH_ArkUI_KeyEvent_GetKeyIntensionCode(const ArkUI_UIInputEvent* event) | 获取按键对应的意图。 |
| uint32_t OH_ArkUI_KeyEvent_GetUnicode(const ArkUI_UIInputEvent* event) | 获取按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。 |
| void OH_ArkUI_KeyEvent_SetConsumed(const ArkUI_UIInputEvent* event, bool isConsumed) | 在按键事件回调中，设置事件是否被该回调消费。 |
| void OH_ArkUI_KeyEvent_Dispatch(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event) | 将按键事件分发到特定组件节点。 |
| ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsNumLockOn(const ArkUI_UIInputEvent* event, bool* state) | 获取按键事件发生时NumLock的状态。 |
| ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsCapsLockOn(const ArkUI_UIInputEvent* event, bool* state) | 获取按键事件发生时CapsLock的状态。 |
| ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsScrollLockOn(const ArkUI_UIInputEvent* event, bool* state) | 获取按键事件发生时ScrollLock的状态。 |

**枚举类型说明**

**ArkUI_KeyCode**

```ets
enum ArkUI_KeyCode
```

描述：

按键事件的键码。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_KEYCODE_UNKNOWN = -1 | 未知按键。 |
| ARKUI_KEYCODE_FN = 0 | 功能（Fn）键。 |
| ARKUI_KEYCODE_VOLUME_UP = 16 | 音量增加键。 |
| ARKUI_KEYCODE_VOLUME_DOWN = 17 | 音量减小键。 |
| ARKUI_KEYCODE_POWER = 18 | 电源键。 |
| ARKUI_KEYCODE_CAMERA = 19 | 拍照键。 |
| ARKUI_KEYCODE_VOLUME_MUTE = 22 | 扬声器静音键。 |
| ARKUI_KEYCODE_MUTE = 23 | 话筒静音键。 |
| ARKUI_KEYCODE_BRIGHTNESS_UP = 40 | 亮度调节按键，调亮。 |
| ARKUI_KEYCODE_BRIGHTNESS_DOWN = 41 | 亮度调节按键，调暗。 |
| ARKUI_KEYCODE_0 = 2000 | 按键'0'。 |
| ARKUI_KEYCODE_1 = 2001 | 按键'1'。 |
| ARKUI_KEYCODE_2 = 2002 | 按键'2'。 |
| ARKUI_KEYCODE_3 = 2003 | 按键'3'。 |
| ARKUI_KEYCODE_4 = 2004 | 按键'4'。 |
| ARKUI_KEYCODE_5 = 2005 | 按键'5'。 |
| ARKUI_KEYCODE_6 = 2006 | 按键'6'。 |
| ARKUI_KEYCODE_7 = 2007 | 按键'7'。 |
| ARKUI_KEYCODE_8 = 2008 | 按键'8'。 |
| ARKUI_KEYCODE_9 = 2009 | 按键'9'。 |
| ARKUI_KEYCODE_STAR = 2010 | 按键'*'。 |
| ARKUI_KEYCODE_POUND = 2011 | 按键'#'。 |
| ARKUI_KEYCODE_DPAD_UP = 2012 | 导航键，向上。 |
| ARKUI_KEYCODE_DPAD_DOWN = 2013 | 导航键，向下。 |
| ARKUI_KEYCODE_DPAD_LEFT = 2014 | 导航键，向左。 |
| ARKUI_KEYCODE_DPAD_RIGHT = 2015 | 导航键，向右。 |
| ARKUI_KEYCODE_DPAD_CENTER = 2016 | 导航键，确定键。 |
| ARKUI_KEYCODE_A = 2017 | 按键'A'。 |
| ARKUI_KEYCODE_B = 2018 | 按键'B'。 |
| ARKUI_KEYCODE_C = 2019 | 按键'C'。 |
| ARKUI_KEYCODE_D = 2020 | 按键'D'。 |
| ARKUI_KEYCODE_E = 2021 | 按键'E'。 |
| ARKUI_KEYCODE_F = 2022 | 按键'F'。 |
| ARKUI_KEYCODE_G = 2023 | 按键'G'。 |
| ARKUI_KEYCODE_H = 2024 | 按键'H'。 |
| ARKUI_KEYCODE_I = 2025 | 按键'I'。 |
| ARKUI_KEYCODE_J = 2026 | 按键'J'。 |
| ARKUI_KEYCODE_K = 2027 | 按键'K'。 |
| ARKUI_KEYCODE_L = 2028 | 按键'L'。 |
| ARKUI_KEYCODE_M = 2029 | 按键'M'。 |
| ARKUI_KEYCODE_N = 2030 | 按键'N'。 |
| ARKUI_KEYCODE_O = 2031 | 按键'O'。 |
| ARKUI_KEYCODE_P = 2032 | 按键'P'。 |
| ARKUI_KEYCODE_Q = 2033 | 按键'Q'。 |
| ARKUI_KEYCODE_R = 2034 | 按键'R'。 |
| ARKUI_KEYCODE_S = 2035 | 按键'S'。 |
| ARKUI_KEYCODE_T = 2036 | 按键'T'。 |
| ARKUI_KEYCODE_U = 2037 | 按键'U'。 |
| ARKUI_KEYCODE_V = 2038 | 按键'V'。 |
| ARKUI_KEYCODE_W = 2039 | 按键'W'。 |
| ARKUI_KEYCODE_X = 2040 | 按键'X'。 |
| ARKUI_KEYCODE_Y = 2041 | 按键'Y'。 |
| ARKUI_KEYCODE_Z = 2042 | 按键'Z'。 |
| ARKUI_KEYCODE_COMMA = 2043 | 按键','。 |
| ARKUI_KEYCODE_PERIOD = 2044 | 按键'.'。 |
| ARKUI_KEYCODE_ALT_LEFT = 2045 | 左Alt键。 |
| ARKUI_KEYCODE_ALT_RIGHT = 2046 | 右Alt键。 |
| ARKUI_KEYCODE_SHIFT_LEFT = 2047 | 左Shift键。 |
| ARKUI_KEYCODE_SHIFT_RIGHT = 2048 | 右Shift键。 |
| ARKUI_KEYCODE_TAB = 2049 | Tab键。 |
| ARKUI_KEYCODE_SPACE = 2050 | 空格键。 |
| ARKUI_KEYCODE_SYM = 2051 | 符号修改器按键。 |
| ARKUI_KEYCODE_EXPLORER = 2052 | 浏览器功能键，此键用于启动浏览器应用程序。 |
| ARKUI_KEYCODE_ENVELOPE = 2053 | 电子邮件功能键，此键用于启动电子邮件应用程序。 |
| ARKUI_KEYCODE_ENTER = 2054 | 回车键。 |
| ARKUI_KEYCODE_DEL = 2055 | 退格键。 |
| ARKUI_KEYCODE_GRAVE = 2056 | 按键'`'。 |
| ARKUI_KEYCODE_MINUS = 2057 | 按键'-'。 |
| ARKUI_KEYCODE_EQUALS = 2058 | 按键'='。 |
| ARKUI_KEYCODE_LEFT_BRACKET = 2059 | 按键'['。 |
| ARKUI_KEYCODE_RIGHT_BRACKET = 2060 | 按键']'。 |
| ARKUI_KEYCODE_BACKSLASH = 2061 | 按键'\'。 |
| ARKUI_KEYCODE_SEMICOLON = 2062 | 按键';'。 |
| ARKUI_KEYCODE_APOSTROPHE = 2063 | 按键''' (单引号)。 |
| ARKUI_KEYCODE_SLASH = 2064 | 按键'/'。 |
| ARKUI_KEYCODE_AT = 2065 | 按键'@'。 |
| ARKUI_KEYCODE_PLUS = 2066 | 按键'+'。 |
| ARKUI_KEYCODE_MENU = 2067 | 菜单键。 |
| ARKUI_KEYCODE_PAGE_UP = 2068 | 向上翻页键。 |
| ARKUI_KEYCODE_PAGE_DOWN = 2069 | 向下翻页键。 |
| ARKUI_KEYCODE_ESCAPE = 2070 | ESC键。 |
| ARKUI_KEYCODE_FORWARD_DEL = 2071 | 删除键。 |
| ARKUI_KEYCODE_CTRL_LEFT = 2072 | 左Ctrl键。 |
| ARKUI_KEYCODE_CTRL_RIGHT = 2073 | 右Ctrl键。 |
| ARKUI_KEYCODE_CAPS_LOCK = 2074 | 大写锁定键。 |
| ARKUI_KEYCODE_SCROLL_LOCK = 2075 | 滚动锁定键。 |
| ARKUI_KEYCODE_META_LEFT = 2076 | 左元修改器键。 |
| ARKUI_KEYCODE_META_RIGHT = 2077 | 右元修改器键。 |
| ARKUI_KEYCODE_FUNCTION = 2078 | 功能键。 |
| ARKUI_KEYCODE_SYSRQ = 2079 | 系统请求/打印屏幕键。 |
| ARKUI_KEYCODE_BREAK = 2080 | Break/Pause键。 |
| ARKUI_KEYCODE_MOVE_HOME = 2081 | 光标移动到开始键。 |
| ARKUI_KEYCODE_MOVE_END = 2082 | 光标移动到末尾键。 |
| ARKUI_KEYCODE_INSERT = 2083 | 插入键。 |
| ARKUI_KEYCODE_FORWARD = 2084 | 前进键。 |
| ARKUI_KEYCODE_MEDIA_PLAY = 2085 | 多媒体键，播放。 |
| ARKUI_KEYCODE_MEDIA_PAUSE = 2086 | 多媒体键，暂停。 |
| ARKUI_KEYCODE_MEDIA_CLOSE = 2087 | 多媒体键，关闭。 |
| ARKUI_KEYCODE_MEDIA_EJECT = 2088 | 多媒体键，弹出。 |
| ARKUI_KEYCODE_MEDIA_RECORD = 2089 | 多媒体键，录音。 |
| ARKUI_KEYCODE_F1 = 2090 | 按键'F1'。 |
| ARKUI_KEYCODE_F2 = 2091 | 按键'F2'。 |
| ARKUI_KEYCODE_F3 = 2092 | 按键'F3'。 |
| ARKUI_KEYCODE_F4 = 2093 | 按键'F4'。 |
| ARKUI_KEYCODE_F5 = 2094 | 按键'F5'。 |
| ARKUI_KEYCODE_F6 = 2095 | 按键'F6'。 |
| ARKUI_KEYCODE_F7 = 2096 | 按键'F7'。 |
| ARKUI_KEYCODE_F8 = 2097 | 按键'F8'。 |
| ARKUI_KEYCODE_F9 = 2098 | 按键'F9'。 |
| ARKUI_KEYCODE_F10 = 2099 | 按键'F10'。 |
| ARKUI_KEYCODE_F11 = 2100 | 按键'F11'。 |
| ARKUI_KEYCODE_F12 = 2101 | 按键'F12'。 |
| ARKUI_KEYCODE_NUM_LOCK = 2102 | 小键盘锁。 |
| ARKUI_KEYCODE_NUMPAD_0 = 2103 | 小键盘按键'0'。 |
| ARKUI_KEYCODE_NUMPAD_1 = 2104 | 小键盘按键'1'。 |
| ARKUI_KEYCODE_NUMPAD_2 = 2105 | 小键盘按键'2'。 |
| ARKUI_KEYCODE_NUMPAD_3 = 2106 | 小键盘按键'3'。 |
| ARKUI_KEYCODE_NUMPAD_4 = 2107 | 小键盘按键'4'。 |
| ARKUI_KEYCODE_NUMPAD_5 = 2108 | 小键盘按键'5'。 |
| ARKUI_KEYCODE_NUMPAD_6 = 2109 | 小键盘按键'6'。 |
| ARKUI_KEYCODE_NUMPAD_7 = 2110 | 小键盘按键'7'。 |
| ARKUI_KEYCODE_NUMPAD_8 = 2111 | 小键盘按键'8'。 |
| ARKUI_KEYCODE_NUMPAD_9 = 2112 | 小键盘按键'9'。 |
| ARKUI_KEYCODE_NUMPAD_DIVIDE = 2113 | 小键盘按键'/'。 |
| ARKUI_KEYCODE_NUMPAD_MULTIPLY = 2114 | 小键盘按键'*'。 |
| ARKUI_KEYCODE_NUMPAD_SUBTRACT = 2115 | 小键盘按键'-'。 |
| ARKUI_KEYCODE_NUMPAD_ADD = 2116 | 小键盘按键'+'。 |
| ARKUI_KEYCODE_NUMPAD_DOT = 2117 | 小键盘按键'.'。 |
| ARKUI_KEYCODE_NUMPAD_COMMA = 2118 | 小键盘按键','。 |
| ARKUI_KEYCODE_NUMPAD_ENTER = 2119 | 小键盘按键回车。 |
| ARKUI_KEYCODE_NUMPAD_EQUALS = 2120 | 小键盘按键'='。 |
| ARKUI_KEYCODE_NUMPAD_LEFT_PAREN = 2121 | 小键盘按键'('。 |
| ARKUI_KEYCODE_NUMPAD_RIGHT_PAREN = 2122 | 小键盘按键')'。 |
| ARKUI_KEYCODE_BUTTON_A = 2301 | 游戏手柄按键'A'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_B = 2302 | 游戏手柄按键'B'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_X = 2304 | 游戏手柄按键'X'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_Y = 2305 | 游戏手柄按键'Y'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_L1 = 2307 | 游戏手柄按键'L1'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_R1 = 2308 | 游戏手柄按键'R1'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_L2 = 2309 | 游戏手柄按键'L2'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_R2 = 2310 | 游戏手柄按键'R2'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_SELECT = 2311 | 游戏手柄按键'Select'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_START = 2312 | 游戏手柄按键'Start'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_MODE = 2313 | 游戏手柄按键'Mode'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_THUMBL = 2314 | 游戏手柄按键'THUMBL'。 起始版本： 15 |
| ARKUI_KEYCODE_BUTTON_THUMBR = 2315 | 游戏手柄按键'THUMBR'。 起始版本： 15 |

**ArkUI_KeyEventType**

```ets
enum ArkUI_KeyEventType
```

描述：

按键的类型。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_KEY_EVENT_UNKNOWN = -1 | 未知类型。 |
| ARKUI_KEY_EVENT_DOWN = 0 | 按键按下。 |
| ARKUI_KEY_EVENT_UP = 1 | 按键松开。 |
| ARKUI_KEY_EVENT_LONG_PRESS = 2 | 按键长按。 |
| ARKUI_KEY_EVENT_CLICK = 3 | 按键点击。 |

**ArkUI_KeySourceType**

```ets
enum ArkUI_KeySourceType
```

描述：

触发当前按键的输入设备类型。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_KEY_SOURCE_UNKNOWN = 0 | 未知类型。 |
| ARKUI_KEY_SOURCE_TYPE_MOUSE = 1 | 鼠标。 |
| ARKUI_KEY_SOURCE_TYPE_KEYBOARD = 4 | 键盘。 |
| ARKUI_KEY_SOURCE_TYPE_JOYSTICK = 5 | 游戏手柄。 起始版本： 15 |

**ArkUI_KeyIntension**

```ets
enum ArkUI_KeyIntension
```

描述：

按键对应的意图。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_KEY_INTENSION_UNKNOWN = -1 | 未知意图。 |
| ARKUI_KEY_INTENSION_UP = 1 | 向上。 |
| ARKUI_KEY_INTENSION_DOWN = 2 | 向下。 |
| ARKUI_KEY_INTENSION_LEFT = 3 | 向左。 |
| ARKUI_KEY_INTENSION_RIGHT = 4 | 向右。 |
| ARKUI_KEY_INTENSION_SELECT = 5 | 选中。 |
| ARKUI_KEY_INTENSION_ESCAPE = 6 | 返回。 |
| ARKUI_KEY_INTENSION_BACK = 7 | 后退。 |
| ARKUI_KEY_INTENSION_FORWARD = 8 | 前进。 |
| ARKUI_KEY_INTENSION_MENU = 9 | 菜单。 |
| ARKUI_KEY_INTENSION_HOME = 10 | 主页。 |
| ARKUI_KEY_INTENSION_PAGE_UP = 11 | 上一页。 |
| ARKUI_KEY_INTENSION_PAGE_DOWN = 12 | 下一页。 |
| ARKUI_KEY_INTENSION_ZOOM_OUT = 13 | 缩小。 |
| ARKUI_KEY_INTENSION_ZOOM_IN = 14 | 放大。 |
| ARKUI_KEY_INTENTION_MEDIA_PLAY_PAUSE = 100 | 播放。 |
| ARKUI_KEY_INTENTION_MEDIA_FAST_FORWARD = 101 | 快进。 |
| ARKUI_KEY_INTENTION_MEDIA_FAST_PLAYBACK = 103 | 快速播放。 |
| ARKUI_KEY_INTENTION_MEDIA_NEXT = 104 | 下一首。 |
| ARKUI_KEY_INTENTION_MEDIA_PREVIOUS = 105 | 上一首。 |
| ARKUI_KEY_INTENTION_MEDIA_MUTE = 106 | 静音。 |
| ARKUI_KEY_INTENTION_VOLUME_UP = 107 | 音量增加。 |
| ARKUI_KEY_INTENTION_VOLUME_DOWN = 108 | 音量降低。 |
| ARKUI_KEY_INTENTION_CALL = 200 | 接听电话。 |
| ARKUI_KEY_INTENTION_CAMERA = 300 | 拍照。 |

**函数说明**

**OH_ArkUI_KeyEvent_GetType()**

```ets
ArkUI_KeyEventType OH_ArkUI_KeyEvent_GetType(const ArkUI_UIInputEvent* event)
```

描述：

获取按键的类型。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_KeyEventType | ArkUI_KeyEventType 按键的类型。 |

**OH_ArkUI_KeyEvent_GetKeyCode()**

```ets
int32_t OH_ArkUI_KeyEvent_GetKeyCode(const ArkUI_UIInputEvent* event)
```

描述：

获取按键的键码。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 按键的键码。 |

**OH_ArkUI_KeyEvent_GetKeyText()**

```ets
const char *OH_ArkUI_KeyEvent_GetKeyText(const ArkUI_UIInputEvent* event)
```

描述：

获取按键的键值。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char * | 按键的键值。 |

**OH_ArkUI_KeyEvent_GetKeySource()**

```ets
ArkUI_KeySourceType OH_ArkUI_KeyEvent_GetKeySource(const ArkUI_UIInputEvent* event)
```

描述：

获取当前按键的输入设备类型。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_KeySourceType | ArkUI_KeySourceType 当前按键的输入设备类型。 |

**OH_ArkUI_KeyEvent_StopPropagation()**

```ets
void OH_ArkUI_KeyEvent_StopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

描述：

阻塞事件冒泡传递。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |
| bool stopPropagation | 表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。 |

**OH_ArkUI_KeyEvent_GetKeyIntensionCode()**

```ets
ArkUI_KeyIntension OH_ArkUI_KeyEvent_GetKeyIntensionCode(const ArkUI_UIInputEvent* event)
```

描述：

获取按键对应的意图。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_KeyIntension | ArkUI_KeyIntension 按键对应的意图。 |

**OH_ArkUI_KeyEvent_GetUnicode()**

```ets
uint32_t OH_ArkUI_KeyEvent_GetUnicode(const ArkUI_UIInputEvent* event)
```

描述：

获取按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | Unicode码值。 |

**OH_ArkUI_KeyEvent_SetConsumed()**

```ets
void OH_ArkUI_KeyEvent_SetConsumed(const ArkUI_UIInputEvent* event, bool isConsumed)
```

描述：

在按键事件回调中，设置事件是否被该回调消费。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |
| bool isConsumed | 事件是否被该回调消费。true表示事件被消费，false表示事件未被消费。 |

**OH_ArkUI_KeyEvent_Dispatch()**

```ets
void OH_ArkUI_KeyEvent_Dispatch(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event)
```

描述：

将按键事件分发到特定组件节点。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 指定的节点。 |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |

**OH_ArkUI_KeyEvent_IsNumLockOn()**

```ets
ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsNumLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

描述：

获取按键事件发生时NumLock的状态。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |
| bool* state | 输出参数，返回NumLock的状态。true表示处于激活状态，false表示处于未激活状态。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_KeyEvent_IsCapsLockOn()**

```ets
ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsCapsLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

描述：

获取按键事件发生时CapsLock的状态。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |
| bool* state | 输出参数，返回CapsLock的状态。true表示处于激活状态，false表示处于未激活状态。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_KeyEvent_IsScrollLockOn()**

```ets
ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsScrollLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

描述：

获取按键事件发生时ScrollLock的状态。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_UIInputEvent* event | ArkUI_UIInputEvent事件指针。 |
| bool* state | 输出参数，返回ScrollLock的状态。true表示处于激活状态，false表示处于未激活状态。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |