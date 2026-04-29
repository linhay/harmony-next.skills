# inputmethod_types_capi.h

**概述**

提供了输入法相关的类型定义。

引用文件： <inputmethod/inputmethod_types_capi.h>

库： libohinputmethod.so

系统能力： SystemCapability.MiscServices.InputMethodFramework

起始版本： 12

相关模块： [InputMethod](InputMethod.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| InputMethod_KeyboardStatus | InputMethod_KeyboardStatus | 键盘状态。 |
| InputMethod_EnterKeyType | InputMethod_EnterKeyType | 回车键功能类型。 |
| InputMethod_Direction | InputMethod_Direction | 移动方向。 |
| InputMethod_ExtendAction | InputMethod_ExtendAction | 编辑框中文本的扩展编辑操作类型。 |
| InputMethod_TextInputType | InputMethod_TextInputType | 文本输入类型。 |
| InputMethod_CommandValueType | InputMethod_CommandValueType | 私有数据类型。 |
| InputMethod_ErrorCode | InputMethod_ErrorCode | 输入法错误码。 |
| InputMethod_RequestKeyboardReason | InputMethod_RequestKeyboardReason | 表示请求键盘输入的原因。 |

**枚举类型说明**

**InputMethod_KeyboardStatus**

```ets
enum InputMethod_KeyboardStatus
```

描述

键盘状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IME_KEYBOARD_STATUS_NONE = 0 | 键盘状态为NONE。 |
| IME_KEYBOARD_STATUS_HIDE = 1 | 键盘状态为隐藏。 |
| IME_KEYBOARD_STATUS_SHOW = 2 | 键盘状态为显示。 |

**InputMethod_EnterKeyType**

```ets
enum InputMethod_EnterKeyType
```

描述

回车键功能类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IME_ENTER_KEY_UNSPECIFIED = 0 | 未指定。 |
| IME_ENTER_KEY_NONE = 1 | 回车键功能类型为NONE。 |
| IME_ENTER_KEY_GO = 2 | 前往。 |
| IME_ENTER_KEY_SEARCH = 3 | 搜索。 |
| IME_ENTER_KEY_SEND = 4 | 发送。 |
| IME_ENTER_KEY_NEXT = 5 | 下一步。 |
| IME_ENTER_KEY_DONE = 6 | 完成。 |
| IME_ENTER_KEY_PREVIOUS = 7 | 上一步。 |
| IME_ENTER_KEY_NEWLINE = 8 | 换行。 |

**InputMethod_Direction**

```ets
enum InputMethod_Direction
```

描述

移动方向。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IME_DIRECTION_NONE = 0 | 移动方向为NONE。 |
| IME_DIRECTION_UP = 1 | 向上。 |
| IME_DIRECTION_DOWN = 2 | 向下。 |
| IME_DIRECTION_LEFT = 3 | 向左。 |
| IME_DIRECTION_RIGHT = 4 | 向右。 |

**InputMethod_ExtendAction**

```ets
enum InputMethod_ExtendAction
```

描述

编辑框中文本的扩展编辑操作类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IME_EXTEND_ACTION_SELECT_ALL = 0 | 全选。 |
| IME_EXTEND_ACTION_CUT = 3 | 剪切。 |
| IME_EXTEND_ACTION_COPY = 4 | 复制。 |
| IME_EXTEND_ACTION_PASTE = 5 | 粘贴。 |

**InputMethod_TextInputType**

```ets
enum InputMethod_TextInputType
```

描述

文本输入类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IME_TEXT_INPUT_TYPE_NONE = -1 | 文本输入类型为NONE。 |
| IME_TEXT_INPUT_TYPE_TEXT = 0 | 文本类型。 |
| IME_TEXT_INPUT_TYPE_MULTILINE = 1 | 多行类型。 |
| IME_TEXT_INPUT_TYPE_NUMBER = 2 | 数字类型。 |
| IME_TEXT_INPUT_TYPE_PHONE = 3 | 电话号码类型。 |
| IME_TEXT_INPUT_TYPE_DATETIME = 4 | 日期类型。 |
| IME_TEXT_INPUT_TYPE_EMAIL_ADDRESS = 5 | 邮箱地址类型。 |
| IME_TEXT_INPUT_TYPE_URL = 6 | 链接类型。 |
| IME_TEXT_INPUT_TYPE_VISIBLE_PASSWORD = 7 | 密码类型。 |
| IME_TEXT_INPUT_TYPE_NUMBER_PASSWORD = 8 | 数字密码类型。 |
| IME_TEXT_INPUT_TYPE_SCREEN_LOCK_PASSWORD = 9 | 锁屏密码类型。 |
| IME_TEXT_INPUT_TYPE_USER_NAME = 10 | 用户名类型。 |
| IME_TEXT_INPUT_TYPE_NEW_PASSWORD = 11 | 新密码类型。 |
| IME_TEXT_INPUT_TYPE_NUMBER_DECIMAL = 12 | 数字小数类型。 |
| IME_TEXT_INPUT_TYPE_ONE_TIME_CODE = 13 | 验证码类型。起始版本： 20 |

**InputMethod_CommandValueType**

```ets
enum InputMethod_CommandValueType
```

描述

私有数据类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IME_COMMAND_VALUE_TYPE_NONE = 0 | 私有数据类型为NONE。 |
| IME_COMMAND_VALUE_TYPE_STRING = 1 | 字符串类型。 |
| IME_COMMAND_VALUE_TYPE_BOOL = 2 | 布尔类型。 |
| IME_COMMAND_VALUE_TYPE_INT32 = 3 | 32位带符号整数类型。 |

**InputMethod_ErrorCode**

```ets
enum InputMethod_ErrorCode
```

描述

输入法错误码。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IME_ERR_OK = 0 | 成功。 |
| IME_ERR_UNDEFINED = 1 | 未定义错误。 |
| IME_ERR_PARAMCHECK = 401 | 参数检查失败。 |
| IME_ERR_PACKAGEMANAGER = 12800001 | 包管理异常。 |
| IME_ERR_IMENGINE = 12800002 | 输入法应用异常。 |
| IME_ERR_IMCLIENT = 12800003 | 输入框客户端异常。 |
| IME_ERR_CONFIG_PERSIST = 12800005 | 配置固化失败。当保存配置失败时，会报此错误码。 |
| IME_ERR_CONTROLLER = 12800006 | 输入法控制器异常。 |
| IME_ERR_SETTINGS = 12800007 | 输入法设置器异常。 |
| IME_ERR_IMMS = 12800008 | 输入法管理服务异常。 |
| IME_ERR_DETACHED = 12800009 | 输入框未绑定。 |
| IME_ERR_NULL_POINTER = 12802000 | 空指针异常。 |
| IME_ERR_QUERY_FAILED = 12802001 | 查询失败。 |

**InputMethod_RequestKeyboardReason**

```ets
enum InputMethod_RequestKeyboardReason
```

描述

表示请求键盘输入的原因。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| IME_REQUEST_REASON_NONE = 0 | 表示没有特定的原因触发键盘请求。 |
| IME_REQUEST_REASON_MOUSE = 1 | 表示键盘请求是由鼠标操作触发的。 |
| IME_REQUEST_REASON_TOUCH = 2 | 表示键盘请求是由触摸操作触发的。 |
| IME_REQUEST_REASON_OTHER = 20 | 表示键盘请求是由其他原因触发的。 |