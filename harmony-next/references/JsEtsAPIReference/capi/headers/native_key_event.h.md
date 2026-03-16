# native_key_event.h

#### 概述

提供NativeKeyEvent相关接口定义。

**引用文件：** <arkui/native_key_event.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 14

**相关模块：**[ArkUI_NativeModule](../../topics/system-services/ArkUI_NativeModule.md)

**相关示例：**[NdkKeyEvent](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NdkKeyEvent)

#### 汇总

#### 枚举

名称typedef关键字描述[ArkUI_KeyCode](#ZH-CN_TOPIC_0000002497445100__arkui_keycode)ArkUI_KeyCode按键事件的键码。[ArkUI_KeyEventType](#ZH-CN_TOPIC_0000002497445100__arkui_keyeventtype)ArkUI_KeyEventType按键的类型。[ArkUI_KeySourceType](#ZH-CN_TOPIC_0000002497445100__arkui_keysourcetype)ArkUI_KeySourceType触发当前按键的输入设备类型。[ArkUI_KeyIntension](#ZH-CN_TOPIC_0000002497445100__arkui_keyintension)ArkUI_KeyIntension按键对应的意图。

#### 函数

名称描述[ArkUI_KeyEventType OH_ArkUI_KeyEvent_GetType(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_gettype)获取按键的类型。[int32_t OH_ArkUI_KeyEvent_GetKeyCode(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_getkeycode)获取按键的键码。[const char OH_ArkUI_KeyEvent_GetKeyText(const ArkUI_UIInputEvent event)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_getkeytext)获取按键的键值。[ArkUI_KeySourceType OH_ArkUI_KeyEvent_GetKeySource(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_getkeysource)获取当前按键的输入设备类型。[void OH_ArkUI_KeyEvent_StopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_stoppropagation)阻塞事件冒泡传递。[ArkUI_KeyIntension OH_ArkUI_KeyEvent_GetKeyIntensionCode(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_getkeyintensioncode)获取按键对应的意图。[uint32_t OH_ArkUI_KeyEvent_GetUnicode(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_getunicode)获取按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。[void OH_ArkUI_KeyEvent_SetConsumed(const ArkUI_UIInputEvent* event, bool isConsumed)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_setconsumed)在按键事件回调中，设置事件是否被该回调消费。[void OH_ArkUI_KeyEvent_Dispatch(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_dispatch)将按键事件分发到特定组件节点。[ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsNumLockOn(const ArkUI_UIInputEvent* event, bool* state)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_isnumlockon)获取按键事件发生时NumLock的状态。[ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsCapsLockOn(const ArkUI_UIInputEvent* event, bool* state)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_iscapslockon)获取按键事件发生时CapsLock的状态。[ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsScrollLockOn(const ArkUI_UIInputEvent* event, bool* state)](#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_isscrolllockon)获取按键事件发生时ScrollLock的状态。

#### 枚举类型说明

#### ArkUI_KeyCode

```ets
enum ArkUI_KeyCode
```

**描述：**

按键事件的键码。

**起始版本：** 14

枚举项描述ARKUI_KEYCODE_UNKNOWN = -1未知按键。ARKUI_KEYCODE_FN = 0功能（Fn）键。ARKUI_KEYCODE_VOLUME_UP = 16音量增加键。ARKUI_KEYCODE_VOLUME_DOWN = 17音量减小键。ARKUI_KEYCODE_POWER = 18电源键。ARKUI_KEYCODE_CAMERA = 19拍照键。ARKUI_KEYCODE_VOLUME_MUTE = 22扬声器静音键。ARKUI_KEYCODE_MUTE = 23话筒静音键。ARKUI_KEYCODE_BRIGHTNESS_UP = 40亮度调节按键，调亮。ARKUI_KEYCODE_BRIGHTNESS_DOWN = 41亮度调节按键，调暗。ARKUI_KEYCODE_0 = 2000按键'0'。ARKUI_KEYCODE_1 = 2001按键'1'。ARKUI_KEYCODE_2 = 2002按键'2'。ARKUI_KEYCODE_3 = 2003按键'3'。ARKUI_KEYCODE_4 = 2004按键'4'。ARKUI_KEYCODE_5 = 2005按键'5'。ARKUI_KEYCODE_6 = 2006按键'6'。ARKUI_KEYCODE_7 = 2007按键'7'。ARKUI_KEYCODE_8 = 2008按键'8'。ARKUI_KEYCODE_9 = 2009按键'9'。ARKUI_KEYCODE_STAR = 2010按键'*'。ARKUI_KEYCODE_POUND = 2011按键'#'。ARKUI_KEYCODE_DPAD_UP = 2012导航键，向上。ARKUI_KEYCODE_DPAD_DOWN = 2013导航键，向下。ARKUI_KEYCODE_DPAD_LEFT = 2014导航键，向左。ARKUI_KEYCODE_DPAD_RIGHT = 2015导航键，向右。ARKUI_KEYCODE_DPAD_CENTER = 2016导航键，确定键。ARKUI_KEYCODE_A = 2017按键'A'。ARKUI_KEYCODE_B = 2018按键'B'。ARKUI_KEYCODE_C = 2019按键'C'。ARKUI_KEYCODE_D = 2020按键'D'。ARKUI_KEYCODE_E = 2021按键'E'。ARKUI_KEYCODE_F = 2022按键'F'。ARKUI_KEYCODE_G = 2023按键'G'。ARKUI_KEYCODE_H = 2024按键'H'。ARKUI_KEYCODE_I = 2025按键'I'。ARKUI_KEYCODE_J = 2026按键'J'。ARKUI_KEYCODE_K = 2027按键'K'。ARKUI_KEYCODE_L = 2028按键'L'。ARKUI_KEYCODE_M = 2029按键'M'。ARKUI_KEYCODE_N = 2030按键'N'。ARKUI_KEYCODE_O = 2031按键'O'。ARKUI_KEYCODE_P = 2032按键'P'。ARKUI_KEYCODE_Q = 2033按键'Q'。ARKUI_KEYCODE_R = 2034按键'R'。ARKUI_KEYCODE_S = 2035按键'S'。ARKUI_KEYCODE_T = 2036按键'T'。ARKUI_KEYCODE_U = 2037按键'U'。ARKUI_KEYCODE_V = 2038按键'V'。ARKUI_KEYCODE_W = 2039按键'W'。ARKUI_KEYCODE_X = 2040按键'X'。ARKUI_KEYCODE_Y = 2041按键'Y'。ARKUI_KEYCODE_Z = 2042按键'Z'。ARKUI_KEYCODE_COMMA = 2043按键','。ARKUI_KEYCODE_PERIOD = 2044按键'.'。ARKUI_KEYCODE_ALT_LEFT = 2045左Alt键。ARKUI_KEYCODE_ALT_RIGHT = 2046右Alt键。ARKUI_KEYCODE_SHIFT_LEFT = 2047左Shift键。ARKUI_KEYCODE_SHIFT_RIGHT = 2048右Shift键。ARKUI_KEYCODE_TAB = 2049Tab键。ARKUI_KEYCODE_SPACE = 2050空格键。ARKUI_KEYCODE_SYM = 2051符号修改器按键。ARKUI_KEYCODE_EXPLORER = 2052浏览器功能键，此键用于启动浏览器应用程序。ARKUI_KEYCODE_ENVELOPE = 2053电子邮件功能键，此键用于启动电子邮件应用程序。ARKUI_KEYCODE_ENTER = 2054回车键。ARKUI_KEYCODE_DEL = 2055退格键。ARKUI_KEYCODE_GRAVE = 2056按键'`'。ARKUI_KEYCODE_MINUS = 2057按键'-'。ARKUI_KEYCODE_EQUALS = 2058按键'='。ARKUI_KEYCODE_LEFT_BRACKET = 2059按键'['。ARKUI_KEYCODE_RIGHT_BRACKET = 2060按键']'。ARKUI_KEYCODE_BACKSLASH = 2061按键'\'。ARKUI_KEYCODE_SEMICOLON = 2062按键';'。ARKUI_KEYCODE_APOSTROPHE = 2063按键''' (单引号)。ARKUI_KEYCODE_SLASH = 2064按键'/'。ARKUI_KEYCODE_AT = 2065按键'@'。ARKUI_KEYCODE_PLUS = 2066按键'+'。ARKUI_KEYCODE_MENU = 2067菜单键。ARKUI_KEYCODE_PAGE_UP = 2068向上翻页键。ARKUI_KEYCODE_PAGE_DOWN = 2069向下翻页键。ARKUI_KEYCODE_ESCAPE = 2070ESC键。ARKUI_KEYCODE_FORWARD_DEL = 2071删除键。ARKUI_KEYCODE_CTRL_LEFT = 2072左Ctrl键。ARKUI_KEYCODE_CTRL_RIGHT = 2073右Ctrl键。ARKUI_KEYCODE_CAPS_LOCK = 2074大写锁定键。ARKUI_KEYCODE_SCROLL_LOCK = 2075滚动锁定键。ARKUI_KEYCODE_META_LEFT = 2076左元修改器键。ARKUI_KEYCODE_META_RIGHT = 2077右元修改器键。ARKUI_KEYCODE_FUNCTION = 2078功能键。ARKUI_KEYCODE_SYSRQ = 2079系统请求/打印屏幕键。ARKUI_KEYCODE_BREAK = 2080Break/Pause键。ARKUI_KEYCODE_MOVE_HOME = 2081光标移动到开始键。ARKUI_KEYCODE_MOVE_END = 2082光标移动到末尾键。ARKUI_KEYCODE_INSERT = 2083插入键。ARKUI_KEYCODE_FORWARD = 2084前进键。ARKUI_KEYCODE_MEDIA_PLAY = 2085多媒体键，播放。ARKUI_KEYCODE_MEDIA_PAUSE = 2086多媒体键，暂停。ARKUI_KEYCODE_MEDIA_CLOSE = 2087多媒体键，关闭。ARKUI_KEYCODE_MEDIA_EJECT = 2088多媒体键，弹出。ARKUI_KEYCODE_MEDIA_RECORD = 2089多媒体键，录音。ARKUI_KEYCODE_F1 = 2090按键'F1'。ARKUI_KEYCODE_F2 = 2091按键'F2'。ARKUI_KEYCODE_F3 = 2092按键'F3'。ARKUI_KEYCODE_F4 = 2093按键'F4'。ARKUI_KEYCODE_F5 = 2094按键'F5'。ARKUI_KEYCODE_F6 = 2095按键'F6'。ARKUI_KEYCODE_F7 = 2096按键'F7'。ARKUI_KEYCODE_F8 = 2097按键'F8'。ARKUI_KEYCODE_F9 = 2098按键'F9'。ARKUI_KEYCODE_F10 = 2099按键'F10'。ARKUI_KEYCODE_F11 = 2100按键'F11'。ARKUI_KEYCODE_F12 = 2101按键'F12'。ARKUI_KEYCODE_NUM_LOCK = 2102小键盘锁。ARKUI_KEYCODE_NUMPAD_0 = 2103小键盘按键'0'。ARKUI_KEYCODE_NUMPAD_1 = 2104小键盘按键'1'。ARKUI_KEYCODE_NUMPAD_2 = 2105小键盘按键'2'。ARKUI_KEYCODE_NUMPAD_3 = 2106小键盘按键'3'。ARKUI_KEYCODE_NUMPAD_4 = 2107小键盘按键'4'。ARKUI_KEYCODE_NUMPAD_5 = 2108小键盘按键'5'。ARKUI_KEYCODE_NUMPAD_6 = 2109小键盘按键'6'。ARKUI_KEYCODE_NUMPAD_7 = 2110小键盘按键'7'。ARKUI_KEYCODE_NUMPAD_8 = 2111小键盘按键'8'。ARKUI_KEYCODE_NUMPAD_9 = 2112小键盘按键'9'。ARKUI_KEYCODE_NUMPAD_DIVIDE = 2113小键盘按键'/'。ARKUI_KEYCODE_NUMPAD_MULTIPLY = 2114小键盘按键'*'。ARKUI_KEYCODE_NUMPAD_SUBTRACT = 2115小键盘按键'-'。ARKUI_KEYCODE_NUMPAD_ADD = 2116小键盘按键'+'。ARKUI_KEYCODE_NUMPAD_DOT = 2117小键盘按键'.'。ARKUI_KEYCODE_NUMPAD_COMMA = 2118小键盘按键','。ARKUI_KEYCODE_NUMPAD_ENTER = 2119小键盘按键回车。ARKUI_KEYCODE_NUMPAD_EQUALS = 2120小键盘按键'='。ARKUI_KEYCODE_NUMPAD_LEFT_PAREN = 2121小键盘按键'('。ARKUI_KEYCODE_NUMPAD_RIGHT_PAREN = 2122小键盘按键')'。ARKUI_KEYCODE_BUTTON_A = 2301

游戏手柄按键'A'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_B = 2302

游戏手柄按键'B'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_X = 2304

游戏手柄按键'X'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_Y = 2305

游戏手柄按键'Y'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_L1 = 2307

游戏手柄按键'L1'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_R1 = 2308

游戏手柄按键'R1'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_L2 = 2309

游戏手柄按键'L2'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_R2 = 2310

游戏手柄按键'R2'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_SELECT = 2311

游戏手柄按键'Select'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_START = 2312

游戏手柄按键'Start'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_MODE = 2313

游戏手柄按键'Mode'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_THUMBL = 2314

游戏手柄按键'THUMBL'。

**起始版本：** 15

ARKUI_KEYCODE_BUTTON_THUMBR = 2315

游戏手柄按键'THUMBR'。

**起始版本：** 15

#### ArkUI_KeyEventType

```ets
enum ArkUI_KeyEventType
```

**描述：**

按键的类型。

**起始版本：** 14

枚举项描述ARKUI_KEY_EVENT_UNKNOWN = -1未知类型。ARKUI_KEY_EVENT_DOWN = 0按键按下。ARKUI_KEY_EVENT_UP = 1按键松开。ARKUI_KEY_EVENT_LONG_PRESS = 2按键长按。ARKUI_KEY_EVENT_CLICK = 3按键点击。

#### ArkUI_KeySourceType

```ets
enum ArkUI_KeySourceType
```

**描述：**

触发当前按键的输入设备类型。

**起始版本：** 14

枚举项描述ARKUI_KEY_SOURCE_UNKNOWN = 0未知类型。ARKUI_KEY_SOURCE_TYPE_MOUSE = 1鼠标。ARKUI_KEY_SOURCE_TYPE_KEYBOARD = 4键盘。ARKUI_KEY_SOURCE_TYPE_JOYSTICK = 5

游戏手柄。

**起始版本：** 15

#### ArkUI_KeyIntension

```ets
enum ArkUI_KeyIntension
```

**描述：**

按键对应的意图。

**起始版本：** 14

枚举项描述ARKUI_KEY_INTENSION_UNKNOWN = -1未知意图。ARKUI_KEY_INTENSION_UP = 1向上。ARKUI_KEY_INTENSION_DOWN = 2向下。ARKUI_KEY_INTENSION_LEFT = 3向左。ARKUI_KEY_INTENSION_RIGHT = 4向右。ARKUI_KEY_INTENSION_SELECT = 5选中。ARKUI_KEY_INTENSION_ESCAPE = 6返回。ARKUI_KEY_INTENSION_BACK = 7后退。ARKUI_KEY_INTENSION_FORWARD = 8前进。ARKUI_KEY_INTENSION_MENU = 9菜单。ARKUI_KEY_INTENSION_HOME = 10主页。ARKUI_KEY_INTENSION_PAGE_UP = 11上一页。ARKUI_KEY_INTENSION_PAGE_DOWN = 12下一页。ARKUI_KEY_INTENSION_ZOOM_OUT = 13缩小。ARKUI_KEY_INTENSION_ZOOM_IN = 14放大。ARKUI_KEY_INTENTION_MEDIA_PLAY_PAUSE = 100播放。ARKUI_KEY_INTENTION_MEDIA_FAST_FORWARD = 101快进。ARKUI_KEY_INTENTION_MEDIA_FAST_PLAYBACK = 103快速播放。ARKUI_KEY_INTENTION_MEDIA_NEXT = 104下一首。ARKUI_KEY_INTENTION_MEDIA_PREVIOUS = 105上一首。ARKUI_KEY_INTENTION_MEDIA_MUTE = 106静音。ARKUI_KEY_INTENTION_VOLUME_UP = 107音量增加。ARKUI_KEY_INTENTION_VOLUME_DOWN = 108音量降低。ARKUI_KEY_INTENTION_CALL = 200接听电话。ARKUI_KEY_INTENTION_CAMERA = 300拍照。

#### 函数说明

#### OH_ArkUI_KeyEvent_GetType()

```ets
ArkUI_KeyEventType OH_ArkUI_KeyEvent_GetType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的类型。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明[ArkUI_KeyEventType](native_key_event.h.md#ZH-CN_TOPIC_0000002497445100__arkui_keyeventtype)ArkUI_KeyEventType 按键的类型。

#### OH_ArkUI_KeyEvent_GetKeyCode()

```ets
int32_t OH_ArkUI_KeyEvent_GetKeyCode(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的键码。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明int32_t按键的键码。

#### OH_ArkUI_KeyEvent_GetKeyText()

```ets
const char *OH_ArkUI_KeyEvent_GetKeyText(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的键值。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明const char *按键的键值。

#### OH_ArkUI_KeyEvent_GetKeySource()

```ets
ArkUI_KeySourceType OH_ArkUI_KeyEvent_GetKeySource(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前按键的输入设备类型。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明[ArkUI_KeySourceType](native_key_event.h.md#ZH-CN_TOPIC_0000002497445100__arkui_keysourcetype)ArkUI_KeySourceType 当前按键的输入设备类型。

#### OH_ArkUI_KeyEvent_StopPropagation()

```ets
void OH_ArkUI_KeyEvent_StopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

**描述：**

阻塞事件冒泡传递。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。bool stopPropagation表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。

#### OH_ArkUI_KeyEvent_GetKeyIntensionCode()

```ets
ArkUI_KeyIntension OH_ArkUI_KeyEvent_GetKeyIntensionCode(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键对应的意图。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明[ArkUI_KeyIntension](native_key_event.h.md#ZH-CN_TOPIC_0000002497445100__arkui_keyintension)ArkUI_KeyIntension 按键对应的意图。

#### OH_ArkUI_KeyEvent_GetUnicode()

```ets
uint32_t OH_ArkUI_KeyEvent_GetUnicode(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明uint32_tUnicode码值。

#### OH_ArkUI_KeyEvent_SetConsumed()

```ets
void OH_ArkUI_KeyEvent_SetConsumed(const ArkUI_UIInputEvent* event, bool isConsumed)
```

**描述：**

在按键事件回调中，设置事件是否被该回调消费。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。bool isConsumed事件是否被该回调消费。true表示事件被消费，false表示事件未被消费。

#### OH_ArkUI_KeyEvent_Dispatch()

```ets
void OH_ArkUI_KeyEvent_Dispatch(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event)
```

**描述：**

将按键事件分发到特定组件节点。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_NodeHandle](../../topics/components/ArkUI_Node_.md) node指定的节点。[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

#### OH_ArkUI_KeyEvent_IsNumLockOn()

```ets
ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsNumLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

**描述：**

获取按键事件发生时NumLock的状态。

**起始版本：** 19

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。bool* state输出参数，返回NumLock的状态。true表示处于激活状态，false表示处于未激活状态。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyEvent_IsCapsLockOn()

```ets
ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsCapsLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

**描述：**

获取按键事件发生时CapsLock的状态。

**起始版本：** 19

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。bool* state输出参数，返回CapsLock的状态。true表示处于激活状态，false表示处于未激活状态。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyEvent_IsScrollLockOn()

```ets
ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsScrollLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

**描述：**

获取按键事件发生时ScrollLock的状态。

**起始版本：** 19

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。bool* state输出参数，返回ScrollLock的状态。true表示处于激活状态，false表示处于未激活状态。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。