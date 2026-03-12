# inputmethod_controller_capi.h

#### 概述

提供绑定、解绑输入法的方法。

**引用文件：** <inputmethod/inputmethod_controller_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：**[InputMethod](InputMethod.md)

#### 汇总

#### 函数

名称描述[InputMethod_ErrorCode OH_InputMethodController_Attach(InputMethod_TextEditorProxy *textEditorProxy,InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)](#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)将应用绑定到输入法服务。[InputMethod_ErrorCode OH_InputMethodController_Detach(InputMethod_InputMethodProxy *inputMethodProxy)](#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_detach)将应用从输入法服务解绑。

#### 函数说明

#### OH_InputMethodController_Attach()

```ets
InputMethod_ErrorCode OH_InputMethodController_Attach(InputMethod_TextEditorProxy *textEditorProxy,InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)
```

**描述**

将应用绑定到输入法服务。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md) *textEditorProxy表示指向[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)实例的指针。调用者需要自行管理textEditorProxy的生命周期。并且如果调用成功，调用者在下次发起绑定或解绑之前，不能将textEditorProxy释放。[InputMethod_AttachOptions](InputMethod_AttachOptions.md) *options表示指向[InputMethod_AttachOptions](InputMethod_AttachOptions.md)实例的指针。该参数用于指定附加输入法时的选项。[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) **inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。生命周期维持到下一次绑定或解绑的调用。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_PARAMCHECK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示参数错误。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 输入法服务错误。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_InputMethodController_Detach()

```ets
InputMethod_ErrorCode OH_InputMethodController_Detach(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

将应用从输入法服务解绑。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md) *inputMethodProxy表示指向[InputMethod_InputMethodProxy](InputMethod_InputMethodProxy.md)实例的指针。inputMethodProxy由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002529445259__oh_inputmethodcontroller_attach)获取。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_IMCLIENT](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示输入法客户端错误。

[IME_ERR_IMMS](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示输入法服务错误。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。