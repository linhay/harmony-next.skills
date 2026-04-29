# inputmethod_controller_capi.h

**概述**

提供绑定、解绑输入法的方法。

引用文件： <inputmethod/inputmethod_controller_capi.h>

库： libohinputmethod.so

系统能力： SystemCapability.MiscServices.InputMethodFramework

起始版本： 12

相关模块： [InputMethod](InputMethod.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| InputMethod_ErrorCode OH_InputMethodController_Attach(InputMethod_TextEditorProxy *textEditorProxy,InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy) | 将应用绑定到输入法服务。 |
| InputMethod_ErrorCode OH_InputMethodController_AttachWithUIContext(ArkUI_ContextHandle context, InputMethod_TextEditorProxy *textEditorProxy, InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy) | 将应用绑定到输入法服务。 |
| InputMethod_ErrorCode OH_InputMethodController_Detach(InputMethod_InputMethodProxy *inputMethodProxy) | 将应用从输入法服务解绑。 |

**函数说明**

**OH_InputMethodController_Attach()**

```ets
InputMethod_ErrorCode OH_InputMethodController_Attach(InputMethod_TextEditorProxy *textEditorProxy,InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)
```

描述

将应用绑定到输入法服务。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 表示指向InputMethod_TextEditorProxy实例的指针。调用者需要自行管理textEditorProxy的生命周期。并且如果调用成功，调用者在下次发起绑定或解绑之前，不能将textEditorProxy释放。 |
| InputMethod_AttachOptions *options | 表示指向InputMethod_AttachOptions实例的指针。该参数用于指定附加输入法时的选项。 |
| InputMethod_InputMethodProxy **inputMethodProxy | 表示指向InputMethod_InputMethodProxy实例的指针。生命周期维持到下一次绑定或解绑的调用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_PARAMCHECK - 表示参数错误。  IME_ERR_IMCLIENT - 输入法客户端错误。  IME_ERR_IMMS - 输入法服务错误。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_InputMethodController_AttachWithUIContext()**

```ets
InputMethod_ErrorCode OH_InputMethodController_AttachWithUIContext(ArkUI_ContextHandle context, InputMethod_TextEditorProxy *textEditorProxy, InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)
```

描述

将应用绑定到输入法服务。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle context | 表示指向ArkUI_Context实例的指针。 |
| InputMethod_TextEditorProxy *textEditorProxy | 表示指向InputMethod_TextEditorProxy实例的指针。调用者需要自行管理textEditorProxy的生命周期。并且如果调用成功，调用者在下次发起绑定或解绑之前，不能将textEditorProxy释放。 |
| InputMethod_AttachOptions *options | 表示指向InputMethod_AttachOptions实例的指针。该参数用于指定附加输入法时的选项。 |
| InputMethod_InputMethodProxy **inputMethodProxy | 表示指向InputMethod_InputMethodProxy实例的指针。生命周期维持到下一次绑定或解绑的调用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_PARAMCHECK - 表示参数错误。  IME_ERR_IMCLIENT - 输入法客户端错误。  IME_ERR_IMMS - 输入法服务错误。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |

**OH_InputMethodController_Detach()**

```ets
InputMethod_ErrorCode OH_InputMethodController_Detach(InputMethod_InputMethodProxy *inputMethodProxy)
```

描述

将应用从输入法服务解绑。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_InputMethodProxy *inputMethodProxy | 表示指向InputMethod_InputMethodProxy实例的指针。inputMethodProxy由调用OH_InputMethodController_Attach获取。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_IMCLIENT - 表示输入法客户端错误。  IME_ERR_IMMS - 表示输入法服务错误。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考InputMethod_ErrorCode。 |