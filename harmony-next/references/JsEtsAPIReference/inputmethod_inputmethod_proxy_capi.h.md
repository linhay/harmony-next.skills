# inputmethod_inputmethod_proxy_capi.h

#### 概述

提供使用输入法的方法，可以向输入法应用发送请求和通知。

**引用文件：** <inputmethod/inputmethod_inputmethod_proxy_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：**[InputMethod](InputMethod.md)

#### 汇总

#### 结构体

名称typedef关键字描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)InputMethod_InputMethodProxy输入法代理对象。使用此对象可以用于调用使用输入法的方法。

#### 函数

名称描述[InputMethod_ErrorCode OH_InputMethodProxy_ShowKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)](#ZH-CN_TOPIC_0000002497445316__oh_inputmethodproxy_showkeyboard)显示键盘。[InputMethod_ErrorCode OH_InputMethodProxy_ShowTextInput(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_AttachOptions *options)](#ZH-CN_TOPIC_0000002497445316__oh_inputmethodproxy_showtextinput)显示文本输入框。[InputMethod_ErrorCode OH_InputMethodProxy_HideKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)](#ZH-CN_TOPIC_0000002497445316__oh_inputmethodproxy_hidekeyboard)隐藏键盘。[InputMethod_ErrorCode OH_InputMethodProxy_NotifySelectionChange(InputMethod_InputMethodProxy *inputMethodProxy, char16_t text[], size_t length, int start, int end)](#ZH-CN_TOPIC_0000002497445316__oh_inputmethodproxy_notifyselectionchange)通知文本框选区变化。当输入框内文本内容、光标位置或选中文本发生变化时，通过此接口将信息通知给输入法应用。[InputMethod_ErrorCode OH_InputMethodProxy_NotifyConfigurationChange(InputMethod_InputMethodProxy *inputMethodProxy,InputMethod_EnterKeyType enterKey, InputMethod_TextInputType textType)](#ZH-CN_TOPIC_0000002497445316__oh_inputmethodproxy_notifyconfigurationchange)通知输入框配置变化。[InputMethod_ErrorCode OH_InputMethodProxy_NotifyCursorUpdate(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_CursorInfo *cursorInfo)](#ZH-CN_TOPIC_0000002497445316__oh_inputmethodproxy_notifycursorupdate)通知光标位置变化。[InputMethod_ErrorCode OH_InputMethodProxy_SendPrivateCommand(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_PrivateCommand *privateCommand[], size_t size)](#ZH-CN_TOPIC_0000002497445316__oh_inputmethodproxy_sendprivatecommand)发送私有数据命令。

#### 函数说明

#### OH_InputMethodProxy_ShowKeyboard()

```ets
InputMethod_ErrorCode OH_InputMethodProxy_ShowKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

显示键盘。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_DETACHED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 未绑定输入法。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_InputMethodProxy_ShowTextInput()

```ets
InputMethod_ErrorCode OH_InputMethodProxy_ShowTextInput(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_AttachOptions *options)
```

**描述**

显示文本输入框。

**起始版本：** 15

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。[InputMethod_AttachOptions](InputMethod_AttachOptions.md) *options

表示指向[InputMethod_AttachOptions](InputMethod_AttachOptions.md)实例的指针，用于获取配置选项。

此接口中只需关注[InputMethod_RequestKeyboardReason](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_requestkeyboardreason) - 表示请求键盘输入的原因。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_DETACHED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 未绑定输入法。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_InputMethodProxy_HideKeyboard()

```ets
InputMethod_ErrorCode OH_InputMethodProxy_HideKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

隐藏键盘。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_DETACHED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 未绑定输入法。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_InputMethodProxy_NotifySelectionChange()

```ets
InputMethod_ErrorCode OH_InputMethodProxy_NotifySelectionChange(InputMethod_InputMethodProxy *inputMethodProxy, char16_t text[], size_t length, int start, int end)
```

**描述**

通知文本框选区变化。当输入框内文本内容、光标位置或选中文本发生变化时，通过此接口将信息通知给输入法应用。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。text整个输入文本。size_t lengthtext参数的长度。最大长度为8K。int start所选文本的起始位置。int end所选文本的结束位置。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_PARAMCHECK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示参数错误。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_DETACHED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 未绑定输入法。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_InputMethodProxy_NotifyConfigurationChange()

```ets
InputMethod_ErrorCode OH_InputMethodProxy_NotifyConfigurationChange(InputMethod_InputMethodProxy *inputMethodProxy,InputMethod_EnterKeyType enterKey, InputMethod_TextInputType textType)
```

**描述**

通知输入框配置变化。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。[InputMethod_EnterKeyType](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_enterkeytype) enterKey回车键类型。[InputMethod_TextInputType](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_textinputtype) textType输入框类型。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_PARAMCHECK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示参数错误。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_DETACHED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 未绑定输入法。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_InputMethodProxy_NotifyCursorUpdate()

```ets
InputMethod_ErrorCode OH_InputMethodProxy_NotifyCursorUpdate(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_CursorInfo *cursorInfo)
```

**描述**

通知光标位置变化。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。[InputMethod_CursorInfo](InputMethod_CursorInfo.md) *cursorInfo指向[InputMethod_CursorInfo](InputMethod_CursorInfo.md)实例的指针。表示光标信息。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_PARAMCHECK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示参数错误。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_DETACHED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 未绑定输入法。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_InputMethodProxy_SendPrivateCommand()

```ets
InputMethod_ErrorCode OH_InputMethodProxy_SendPrivateCommand(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_PrivateCommand *privateCommand[], size_t size)
```

**描述**

发送私有数据命令。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md) *privateCommand[]私有命令, 定义在[InputMethod_PrivateCommand](InputMethod_PrivateCommand.md)，最大大小为32KB。size_t size私有命令数组的大小，最大为5。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_PARAMCHECK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示参数错误。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_DETACHED](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 未绑定输入法。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。