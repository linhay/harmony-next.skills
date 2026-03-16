# inputmethod_types_capi.h

#### 概述

提供了输入法相关的类型定义。

**引用文件：** <inputmethod/inputmethod_types_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：**[InputMethod](../../topics/input/InputMethod.md)

#### 汇总

#### 枚举

名称typedef关键字描述[InputMethod_KeyboardStatus](#ZH-CN_TOPIC_0000002529285289__inputmethod_keyboardstatus)InputMethod_KeyboardStatus键盘状态。[InputMethod_EnterKeyType](#ZH-CN_TOPIC_0000002529285289__inputmethod_enterkeytype)InputMethod_EnterKeyType回车键功能类型。[InputMethod_Direction](#ZH-CN_TOPIC_0000002529285289__inputmethod_direction)InputMethod_Direction移动方向。[InputMethod_ExtendAction](#ZH-CN_TOPIC_0000002529285289__inputmethod_extendaction)InputMethod_ExtendAction编辑框中文本的扩展编辑操作类型。[InputMethod_TextInputType](#ZH-CN_TOPIC_0000002529285289__inputmethod_textinputtype)InputMethod_TextInputType文本输入类型。[InputMethod_CommandValueType](#ZH-CN_TOPIC_0000002529285289__inputmethod_commandvaluetype)InputMethod_CommandValueType私有数据类型。[InputMethod_ErrorCode](#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)InputMethod_ErrorCode输入法错误码。[InputMethod_RequestKeyboardReason](#ZH-CN_TOPIC_0000002529285289__inputmethod_requestkeyboardreason)InputMethod_RequestKeyboardReason表示请求键盘输入的原因。

#### 枚举类型说明

#### InputMethod_KeyboardStatus

```ets
enum InputMethod_KeyboardStatus
```

**描述**

键盘状态。

**起始版本：** 12

枚举项描述IME_KEYBOARD_STATUS_NONE = 0键盘状态为NONE。IME_KEYBOARD_STATUS_HIDE = 1键盘状态为隐藏。IME_KEYBOARD_STATUS_SHOW = 2键盘状态为显示。

#### InputMethod_EnterKeyType

```ets
enum InputMethod_EnterKeyType
```

**描述**

回车键功能类型。

**起始版本：** 12

枚举项描述IME_ENTER_KEY_UNSPECIFIED = 0未指定。IME_ENTER_KEY_NONE = 1回车键功能类型为NONE。IME_ENTER_KEY_GO = 2前往。IME_ENTER_KEY_SEARCH = 3搜索。IME_ENTER_KEY_SEND = 4发送。IME_ENTER_KEY_NEXT = 5下一步。IME_ENTER_KEY_DONE = 6完成。IME_ENTER_KEY_PREVIOUS = 7上一步。IME_ENTER_KEY_NEWLINE = 8换行。

#### InputMethod_Direction

```ets
enum InputMethod_Direction
```

**描述**

移动方向。

**起始版本：** 12

枚举项描述IME_DIRECTION_NONE = 0移动方向为NONE。IME_DIRECTION_UP = 1向上。IME_DIRECTION_DOWN = 2向下。IME_DIRECTION_LEFT = 3向左。IME_DIRECTION_RIGHT = 4向右。

#### InputMethod_ExtendAction

```ets
enum InputMethod_ExtendAction
```

**描述**

编辑框中文本的扩展编辑操作类型。

**起始版本：** 12

枚举项描述IME_EXTEND_ACTION_SELECT_ALL = 0全选。IME_EXTEND_ACTION_CUT = 3剪切。IME_EXTEND_ACTION_COPY = 4复制。IME_EXTEND_ACTION_PASTE = 5粘贴。

#### InputMethod_TextInputType

```ets
enum InputMethod_TextInputType
```

**描述**

文本输入类型。

**起始版本：** 12

枚举项描述IME_TEXT_INPUT_TYPE_NONE = -1文本输入类型为NONE。IME_TEXT_INPUT_TYPE_TEXT = 0文本类型。IME_TEXT_INPUT_TYPE_MULTILINE = 1多行类型。IME_TEXT_INPUT_TYPE_NUMBER = 2数字类型。IME_TEXT_INPUT_TYPE_PHONE = 3电话号码类型。IME_TEXT_INPUT_TYPE_DATETIME = 4日期类型。IME_TEXT_INPUT_TYPE_EMAIL_ADDRESS = 5邮箱地址类型。IME_TEXT_INPUT_TYPE_URL = 6链接类型。IME_TEXT_INPUT_TYPE_VISIBLE_PASSWORD = 7密码类型。IME_TEXT_INPUT_TYPE_NUMBER_PASSWORD = 8数字密码类型。IME_TEXT_INPUT_TYPE_SCREEN_LOCK_PASSWORD = 9锁屏密码类型。IME_TEXT_INPUT_TYPE_USER_NAME = 10用户名类型。IME_TEXT_INPUT_TYPE_NEW_PASSWORD = 11新密码类型。IME_TEXT_INPUT_TYPE_NUMBER_DECIMAL = 12数字小数类型。IME_TEXT_INPUT_TYPE_ONE_TIME_CODE = 13验证码类型。**起始版本：** 20

#### InputMethod_CommandValueType

```ets
enum InputMethod_CommandValueType
```

**描述**

私有数据类型。

**起始版本：** 12

枚举项描述IME_COMMAND_VALUE_TYPE_NONE = 0私有数据类型为NONE。IME_COMMAND_VALUE_TYPE_STRING = 1字符串类型。IME_COMMAND_VALUE_TYPE_BOOL = 2布尔类型。IME_COMMAND_VALUE_TYPE_INT32 = 332位带符号整数类型。

#### InputMethod_ErrorCode

```ets
enum InputMethod_ErrorCode
```

**描述**

输入法错误码。

**起始版本：** 12

枚举项描述IME_ERR_OK = 0成功。IME_ERR_UNDEFINED = 1查询失败。IME_ERR_PARAMCHECK = 401参数检查失败。IME_ERR_PACKAGEMANAGER = 12800001包管理异常。IME_ERR_IMENGINE = 12800002输入法应用异常。IME_ERR_IMCLIENT = 12800003输入框客户端异常。IME_ERR_CONFIG_PERSIST = 12800005配置固化失败。当保存配置失败时，会报此错误码。IME_ERR_CONTROLLER = 12800006输入法控制器异常。IME_ERR_SETTINGS = 12800007输入法设置器异常。IME_ERR_IMMS = 12800008输入法管理服务异常。IME_ERR_DETACHED = 12800009输入框未绑定。IME_ERR_NULL_POINTER = 12802000空指针异常。IME_ERR_QUERY_FAILED = 12802001查询失败。

#### InputMethod_RequestKeyboardReason

```ets
enum InputMethod_RequestKeyboardReason
```

**描述**

表示请求键盘输入的原因。

**起始版本：** 15

枚举项描述IME_REQUEST_REASON_NONE = 0表示没有特定的原因触发键盘请求。IME_REQUEST_REASON_MOUSE = 1表示键盘请求是由鼠标操作触发的。IME_REQUEST_REASON_TOUCH = 2表示键盘请求是由触摸操作触发的。IME_REQUEST_REASON_OTHER = 20表示键盘请求是由其他原因触发的。