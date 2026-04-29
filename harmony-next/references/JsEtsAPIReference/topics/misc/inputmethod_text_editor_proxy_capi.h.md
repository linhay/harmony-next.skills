# inputmethod_text_editor_proxy_capi.h

**概述**

提供一套方法支持应用开发的自绘输入框获取来自输入法应用的通知和请求。

引用文件： <inputmethod/inputmethod_text_editor_proxy_capi.h>

库： libohinputmethod.so

系统能力： SystemCapability.MiscServices.InputMethodFramework

起始版本： 12

相关模块： [InputMethod](InputMethod.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| InputMethod_TextEditorProxy | InputMethod_TextEditorProxy | 输入框代理。提供了获取来自输入法应用的通知和请求的方法。当输入法向编辑器发送请求或通知时，这些方法将被调用。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_TextEditorProxy_GetTextConfigFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_TextConfig *config) | OH_TextEditorProxy_GetTextConfigFunc | 输入法获取输入框配置时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetGetTextConfigFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_InsertTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t *text, size_t length) | OH_TextEditorProxy_InsertTextFunc | 输入法应用插入文本时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetInsertTextFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_DeleteForwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length) | OH_TextEditorProxy_DeleteForwardFunc | 输入法删除光标右侧文本时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetDeleteForwardFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_DeleteBackwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length) | OH_TextEditorProxy_DeleteBackwardFunc | 输入法删除光标左侧文本时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetDeleteBackwardFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_SendKeyboardStatusFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_KeyboardStatus keyboardStatus) | OH_TextEditorProxy_SendKeyboardStatusFunc | 输入法通知键盘状态时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetSendKeyboardStatusFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_SendEnterKeyFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_EnterKeyType enterKeyType) | OH_TextEditorProxy_SendEnterKeyFunc | 输入法发送回车键时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetSendEnterKeyFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_MoveCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_Direction direction) | OH_TextEditorProxy_MoveCursorFunc | 输入法移动光标时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetMoveCursorFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_HandleSetSelectionFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t start, int32_t end) | OH_TextEditorProxy_HandleSetSelectionFunc | 输入法请求选中文本时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetHandleSetSelectionFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_HandleExtendActionFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_ExtendAction action) | OH_TextEditorProxy_HandleExtendActionFunc | 输入法发送扩展编辑操作时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetHandleExtendActionFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_GetLeftTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length) | OH_TextEditorProxy_GetLeftTextOfCursorFunc | 输入法获取光标左侧文本时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetGetLeftTextOfCursorFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_GetRightTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length) | OH_TextEditorProxy_GetRightTextOfCursorFunc | 输入法获取光标右侧文本时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetGetRightTextOfCursorFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef int32_t (*OH_TextEditorProxy_GetTextIndexAtCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy) | OH_TextEditorProxy_GetTextIndexAtCursorFunc | 输入法获取光标所在输入框文本索引时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetGetTextIndexAtCursorFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef int32_t (*OH_TextEditorProxy_ReceivePrivateCommandFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_PrivateCommand *privateCommand[], size_t size) | OH_TextEditorProxy_ReceivePrivateCommandFunc | 输入法应用发送私有数据命令时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetReceivePrivateCommandFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef int32_t (*OH_TextEditorProxy_SetPreviewTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t text[], size_t length, int32_t start, int32_t end) | OH_TextEditorProxy_SetPreviewTextFunc | 输入法设置预上屏文本时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetSetPreviewTextFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| typedef void (*OH_TextEditorProxy_FinishTextPreviewFunc)(InputMethod_TextEditorProxy *textEditorProxy) | OH_TextEditorProxy_FinishTextPreviewFunc | 输入法结束预上屏时触发的函数。您需要实现此函数，通过 OH_TextEditorProxy_SetFinishTextPreviewFunc 将它设置到InputMethod_TextEditorProxy中， 并通过OH_InputMethodController_Attach完成注册。 |
| InputMethod_TextEditorProxy *OH_TextEditorProxy_Create(void) | - | 创建一个新的InputMethod_TextEditorProxy实例。 |
| void OH_TextEditorProxy_Destroy(InputMethod_TextEditorProxy *proxy) | - | 销毁一个InputMethod_TextEditorProxy实例。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc getTextConfigFunc) | - | 将函数OH_TextEditorProxy_GetTextConfigFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc insertTextFunc) | - | 将函数OH_TextEditorProxy_InsertTextFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc deleteForwardFunc) | - | 将函数OH_TextEditorProxy_DeleteForwardFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc deleteBackwardFunc) | - | 将函数OH_TextEditorProxy_DeleteBackwardFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc sendKeyboardStatusFunc) | - | 将函数OH_TextEditorProxy_SendKeyboardStatusFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc sendEnterKeyFunc) | - | 将函数OH_TextEditorProxy_SetSendEnterKeyFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc moveCursorFunc) | - | 将函数OH_TextEditorProxy_SetMoveCursorFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc handleSetSelectionFunc) | - | 将函数OH_TextEditorProxy_HandleSetSelectionFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc handleExtendActionFunc) | - | 将函数OH_TextEditorProxy_HandleExtendActionFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc) | - | 将函数OH_TextEditorProxy_GetLeftTextOfCursorFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc getRightTextOfCursorFunc) | - | 将函数OH_TextEditorProxy_GetRightTextOfCursorFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc) | - | 将函数OH_TextEditorProxy_GetTextIndexAtCursorFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc receivePrivateCommandFunc) | - | 将函数OH_TextEditorProxy_ReceivePrivateCommandFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc setPreviewTextFunc) | - | 将函数OH_TextEditorProxy_SetPreviewTextFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_SetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc finishTextPreviewFunc) | - | 将函数OH_TextEditorProxy_FinishTextPreviewFunc设置到InputMethod_TextEditorProxy中。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc *getTextConfigFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_GetTextConfigFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc *insertTextFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_InsertTextFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc *deleteForwardFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_DeleteForwardFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc *deleteBackwardFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_DeleteBackwardFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc *sendKeyboardStatusFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_SendKeyboardStatusFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc *sendEnterKeyFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_SendEnterKeyFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc *moveCursorFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_MoveCursorFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc *handleSetSelectionFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_HandleSetSelectionFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc *handleExtendActionFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_HandleExtendActionFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc *getLeftTextOfCursorFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_GetLeftTextOfCursorFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc *getRightTextOfCursorFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_GetRightTextOfCursorFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc *getTextIndexAtCursorFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_GetTextIndexAtCursorFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc *receivePrivateCommandFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_ReceivePrivateCommandFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc *setPreviewTextFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_SetPreviewTextFunc函数。 |
| InputMethod_ErrorCode OH_TextEditorProxy_GetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc *finishTextPreviewFunc) | - | 从InputMethod_TextEditorProxy中获取OH_TextEditorProxy_FinishTextPreviewFunc函数。 |

**函数说明**

**OH_TextEditorProxy_GetTextConfigFunc()**

```ets
typedef void (*OH_TextEditorProxy_GetTextConfigFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_TextConfig *config)
```

描述

输入法获取输入框配置时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetGetTextConfigFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setgettextconfigfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| InputMethod_TextConfig *config | 表示指向InputMethod_TextConfig实例的指针。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |

**OH_TextEditorProxy_InsertTextFunc()**

```ets
typedef void (*OH_TextEditorProxy_InsertTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t *text, size_t length)
```

描述

输入法应用插入文本时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetInsertTextFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setinserttextfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。in. |
| const char16_t *text | 插入的字符。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size_t length | 插入字符的长度。 |

**OH_TextEditorProxy_DeleteForwardFunc()**

```ets
typedef void (*OH_TextEditorProxy_DeleteForwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
```

描述

输入法删除光标右侧文本时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetDeleteForwardFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setdeleteforwardfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。in. |
| int32_t length | 要删除字符的长度。 |

**OH_TextEditorProxy_DeleteBackwardFunc()**

```ets
typedef void (*OH_TextEditorProxy_DeleteBackwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
```

描述

输入法删除光标左侧文本时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetDeleteBackwardFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setdeletebackwardfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。in. |
| int32_t length | 要删除字符的长度。 |

**OH_TextEditorProxy_SendKeyboardStatusFunc()**

```ets
typedef void (*OH_TextEditorProxy_SendKeyboardStatusFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_KeyboardStatus keyboardStatus)
```

描述

输入法通知键盘状态时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetSendKeyboardStatusFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setsendkeyboardstatusfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| InputMethod_KeyboardStatus keyboardStatus | 键盘状态，具体定义详见InputMethod_KeyboardStatus。 |

**OH_TextEditorProxy_SendEnterKeyFunc()**

```ets
typedef void (*OH_TextEditorProxy_SendEnterKeyFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_EnterKeyType enterKeyType)
```

描述

输入法发送回车键时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetSendEnterKeyFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setsendenterkeyfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| InputMethod_EnterKeyType enterKeyType | 回车键类型，具体定义详见InputMethod_EnterKeyType. |

**OH_TextEditorProxy_MoveCursorFunc()**

```ets
typedef void (*OH_TextEditorProxy_MoveCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_Direction direction)
```

描述

输入法移动光标时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetMoveCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setmovecursorfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| InputMethod_Direction direction | 光标移动方向，具体定义详见InputMethod_Direction. |

**OH_TextEditorProxy_HandleSetSelectionFunc()**

```ets
typedef void (*OH_TextEditorProxy_HandleSetSelectionFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t start, int32_t end)
```

描述

输入法请求选中文本时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetHandleSetSelectionFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_sethandlesetselectionfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| int32_t start | 表示选中文本的起始位置。 |
| int32_t end | 表示选中文本的结束位置。 |

**OH_TextEditorProxy_HandleExtendActionFunc()**

```ets
typedef void (*OH_TextEditorProxy_HandleExtendActionFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_ExtendAction action)
```

描述

输入法发送扩展编辑操作时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetHandleExtendActionFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_sethandleextendactionfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| InputMethod_ExtendAction action | 扩展编辑操作，具体定义详见InputMethod_ExtendAction. |

**OH_TextEditorProxy_GetLeftTextOfCursorFunc()**

```ets
typedef void (*OH_TextEditorProxy_GetLeftTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length)
```

描述

输入法获取光标左侧文本时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetGetLeftTextOfCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setgetlefttextofcursorfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| int32_t number | 目标获取文本的长度。 |
| char16_t text[] | 光标左侧指定长度的文本内容，需要在函数实现中对它赋值。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size_t *length | 表示游标左侧文本的长度，您需要传递此参数。 |

**OH_TextEditorProxy_GetRightTextOfCursorFunc()**

```ets
typedef void (*OH_TextEditorProxy_GetRightTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length)
```

描述

输入法获取光标右侧文本时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetGetRightTextOfCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setgetrighttextofcursorfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| int32_t number | 目标获取文本的长度。 |
| char16_t text[] | 光标右侧指定长度的文本内容，需要在函数实现中对它赋值。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size_t *length | 表示游标右侧文本的长度，您需要传递此参数。 |

**OH_TextEditorProxy_GetTextIndexAtCursorFunc()**

```ets
typedef int32_t (*OH_TextEditorProxy_GetTextIndexAtCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy)
```

描述

输入法获取光标所在输入框文本索引时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetGetTextIndexAtCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setgettextindexatcursorfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回光标所在输入框文本索引。 |

**OH_TextEditorProxy_ReceivePrivateCommandFunc()**

```ets
typedef int32_t (*OH_TextEditorProxy_ReceivePrivateCommandFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_PrivateCommand *privateCommand[], size_t size)
```

描述

输入法应用发送私有数据命令时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetReceivePrivateCommandFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setreceiveprivatecommandfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| InputMethod_PrivateCommand *privateCommand[] | 私有数据命令。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size_t size | 私有数据的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回对私有数据命令处理的处理结果。 |

**OH_TextEditorProxy_SetPreviewTextFunc()**

```ets
typedef int32_t (*OH_TextEditorProxy_SetPreviewTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t text[], size_t length, int32_t start, int32_t end)
```

描述

输入法设置预上屏文本时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetSetPreviewTextFunc](#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setsetpreviewtextfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| const char16_t text[] | 请求设置为预上屏样式的文本内容。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size_t length | 预上屏文本长度。 |
| int32_t start | 预上屏文本起始光标位置。 |
| int32_t end | 预上屏文本结束光标位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回设置预上屏文本的处理结果。 |

**OH_TextEditorProxy_FinishTextPreviewFunc()**

```ets
typedef void (*OH_TextEditorProxy_FinishTextPreviewFunc)(InputMethod_TextEditorProxy *textEditorProxy)
```

描述

输入法结束预上屏时触发的函数。您需要实现此函数，通过 [OH_TextEditorProxy_SetFinishTextPreviewFunc](#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setfinishtextpreviewfunc) 将它设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中， 并通过[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)完成注册。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *textEditorProxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |

**OH_TextEditorProxy_Create()**

```ets
InputMethod_TextEditorProxy *OH_TextEditorProxy_Create(void)
```

描述

创建一个新的[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)实例。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_TextEditorProxy * | 如果创建成功，返回一个指向新创建的InputMethod_TextEditorProxy实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

**OH_TextEditorProxy_Destroy()**

```ets
void OH_TextEditorProxy_Destroy(InputMethod_TextEditorProxy *proxy)
```

描述

销毁一个[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 表示指向即将被销毁的InputMethod_TextEditorProxy实例的指针。 |

**OH_TextEditorProxy_SetGetTextConfigFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc getTextConfigFunc)
```

描述

将函数[OH_TextEditorProxy_GetTextConfigFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_gettextconfigfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetTextConfigFunc getTextConfigFunc | 表示被设置到proxy的函数OH_TextEditorProxy_GetTextConfigFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetInsertTextFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc insertTextFunc)
```

描述

将函数[OH_TextEditorProxy_InsertTextFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_inserttextfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_InsertTextFunc insertTextFunc | 表示被设置到proxy的函数OH_TextEditorProxy_InsertTextFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetDeleteForwardFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc deleteForwardFunc)
```

描述

将函数[OH_TextEditorProxy_DeleteForwardFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_deleteforwardfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_DeleteForwardFunc deleteForwardFunc | 表示被设置到proxy的函数OH_TextEditorProxy_DeleteForwardFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetDeleteBackwardFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc deleteBackwardFunc)
```

描述

将函数[OH_TextEditorProxy_DeleteBackwardFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_deletebackwardfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_DeleteBackwardFunc deleteBackwardFunc | 表示被设置到proxy的函数OH_TextEditorProxy_DeleteBackwardFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetSendKeyboardStatusFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc sendKeyboardStatusFunc)
```

描述

将函数[OH_TextEditorProxy_SendKeyboardStatusFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_sendkeyboardstatusfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_SendKeyboardStatusFunc sendKeyboardStatusFunc | 表示被设置到proxy的函数OH_TextEditorProxy_SendKeyboardStatusFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetSendEnterKeyFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc sendEnterKeyFunc)
```

描述

将函数[OH_TextEditorProxy_SetSendEnterKeyFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setsendenterkeyfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_SendEnterKeyFunc sendEnterKeyFunc | 表示被设置到proxy的函数OH_TextEditorProxy_SendEnterKeyFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetMoveCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc moveCursorFunc)
```

描述

将函数[OH_TextEditorProxy_SetMoveCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setmovecursorfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_MoveCursorFunc moveCursorFunc | 表示被设置到proxy的函数OH_TextEditorProxy_MoveCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetHandleSetSelectionFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc handleSetSelectionFunc)
```

描述

将函数[OH_TextEditorProxy_HandleSetSelectionFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_handlesetselectionfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_HandleSetSelectionFunc handleSetSelectionFunc | 表示被设置到proxy的函数OH_TextEditorProxy_HandleSetSelectionFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetHandleExtendActionFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc handleExtendActionFunc)
```

描述

将函数[OH_TextEditorProxy_HandleExtendActionFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_handleextendactionfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_HandleExtendActionFunc handleExtendActionFunc | 表示被设置到proxy的函数OH_TextEditorProxy_HandleExtendActionFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetGetLeftTextOfCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc)
```

描述

将函数[OH_TextEditorProxy_GetLeftTextOfCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_getlefttextofcursorfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc | 表示被设置到proxy的函数OH_TextEditorProxy_GetLeftTextOfCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetGetRightTextOfCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc getRightTextOfCursorFunc)
```

描述

将函数[OH_TextEditorProxy_GetRightTextOfCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_getrighttextofcursorfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetRightTextOfCursorFunc getRightTextOfCursorFunc | 表示被设置到proxy的函数OH_TextEditorProxy_GetRightTextOfCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetGetTextIndexAtCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc)
```

描述

将函数[OH_TextEditorProxy_GetTextIndexAtCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_gettextindexatcursorfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc | 表示被设置到proxy的函数OH_TextEditorProxy_GetTextIndexAtCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetReceivePrivateCommandFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc receivePrivateCommandFunc)
```

描述

将函数[OH_TextEditorProxy_ReceivePrivateCommandFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_receiveprivatecommandfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_ReceivePrivateCommandFunc receivePrivateCommandFunc | 表示被设置到proxy的函数OH_TextEditorProxy_ReceivePrivateCommandFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetSetPreviewTextFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc setPreviewTextFunc)
```

描述

将函数[OH_TextEditorProxy_SetPreviewTextFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setpreviewtextfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_SetPreviewTextFunc setPreviewTextFunc | 表示被设置到proxy的函数OH_TextEditorProxy_SetPreviewTextFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetFinishTextPreviewFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc finishTextPreviewFunc)
```

描述

将函数[OH_TextEditorProxy_FinishTextPreviewFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_finishtextpreviewfunc)设置到[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向即将被设置的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_FinishTextPreviewFunc finishTextPreviewFunc | 表示被设置到proxy的函数OH_TextEditorProxy_FinishTextPreviewFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetGetTextConfigFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc *getTextConfigFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_GetTextConfigFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_gettextconfigfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetTextConfigFunc *getTextConfigFunc | 表示从proxy获取到的函数OH_TextEditorProxy_GetTextConfigFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetInsertTextFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc *insertTextFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_InsertTextFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_inserttextfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_InsertTextFunc *insertTextFunc | 表示从proxy获取到的函数OH_TextEditorProxy_InsertTextFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetDeleteForwardFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc *deleteForwardFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_DeleteForwardFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_deleteforwardfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_DeleteForwardFunc *deleteForwardFunc | 表示从proxy获取到的函数OH_TextEditorProxy_DeleteForwardFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetDeleteBackwardFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc *deleteBackwardFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_DeleteBackwardFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_deletebackwardfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_DeleteBackwardFunc *deleteBackwardFunc | 表示从proxy获取到的函数OH_TextEditorProxy_DeleteBackwardFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetSendKeyboardStatusFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc *sendKeyboardStatusFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_SendKeyboardStatusFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_sendkeyboardstatusfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_SendKeyboardStatusFunc *sendKeyboardStatusFunc | 表示从proxy获取到的函数OH_TextEditorProxy_SendKeyboardStatusFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetSendEnterKeyFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc *sendEnterKeyFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_SendEnterKeyFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_sendenterkeyfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_SendEnterKeyFunc *sendEnterKeyFunc | 表示从proxy获取到的函数OH_TextEditorProxy_SendEnterKeyFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetMoveCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc *moveCursorFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_MoveCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_movecursorfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_MoveCursorFunc *moveCursorFunc | 表示从proxy获取到的函数OH_TextEditorProxy_MoveCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetHandleSetSelectionFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc *handleSetSelectionFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_HandleSetSelectionFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_handlesetselectionfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_HandleSetSelectionFunc *handleSetSelectionFunc | 表示从proxy获取到的函数OH_TextEditorProxy_HandleSetSelectionFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetHandleExtendActionFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc *handleExtendActionFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_HandleExtendActionFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_handleextendactionfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_HandleExtendActionFunc *handleExtendActionFunc | 表示从proxy获取到的函数OH_TextEditorProxy_HandleExtendActionFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetGetLeftTextOfCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc *getLeftTextOfCursorFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_GetLeftTextOfCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_getlefttextofcursorfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetLeftTextOfCursorFunc *getLeftTextOfCursorFunc | 表示从proxy获取到的函数OH_TextEditorProxy_GetLeftTextOfCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetGetRightTextOfCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc *getRightTextOfCursorFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_GetRightTextOfCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_getrighttextofcursorfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetRightTextOfCursorFunc *getRightTextOfCursorFunc | 表示从proxy获取到的函数OH_TextEditorProxy_GetRightTextOfCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetGetTextIndexAtCursorFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc *getTextIndexAtCursorFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_GetTextIndexAtCursorFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_gettextindexatcursorfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_GetTextIndexAtCursorFunc *getTextIndexAtCursorFunc | 表示从proxy获取到的函数OH_TextEditorProxy_GetTextIndexAtCursorFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetReceivePrivateCommandFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc *receivePrivateCommandFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_ReceivePrivateCommandFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_receiveprivatecommandfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_ReceivePrivateCommandFunc *receivePrivateCommandFunc | 表示从proxy获取到的函数OH_TextEditorProxy_ReceivePrivateCommandFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetSetPreviewTextFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc *setPreviewTextFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_SetPreviewTextFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_setpreviewtextfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_SetPreviewTextFunc *setPreviewTextFunc | 表示从proxy获取到的函数OH_TextEditorProxy_SetPreviewTextFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_GetFinishTextPreviewFunc()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_GetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc *finishTextPreviewFunc)
```

描述

从[InputMethod_TextEditorProxy](InputMethod_TextEditorProxy.md)中获取[OH_TextEditorProxy_FinishTextPreviewFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_finishtextpreviewfunc)函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向被读取的InputMethod_TextEditorProxy实例的指针。 |
| OH_TextEditorProxy_FinishTextPreviewFunc *finishTextPreviewFunc | 表示从proxy获取到的函数OH_TextEditorProxy_FinishTextPreviewFunc。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 返回一个特定的错误码。  IME_ERR_OK - 表示成功。  IME_ERR_NULL_POINTER - 非预期的空指针。  具体错误码可以参考 InputMethod_ErrorCode。 |

**OH_TextEditorProxy_SetCallbackInMainThread()**

```ets
InputMethod_ErrorCode OH_TextEditorProxy_SetCallbackInMainThread(InputMethod_TextEditorProxy *proxy, bool isCallbackInMainThread)
```

描述

为InputMethod_TextEditorProxy的回调函数配置执行线程（主线程/IPC线程）。本接口仅控制InputMethod_TextEditorProxy中除[OH_TextEditorProxy_GetTextConfigFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_gettextconfigfunc)之外的所有回调函数。[OH_TextEditorProxy_GetTextConfigFunc](inputmethod_text_editor_proxy_capi.h.md#ZH-CN_TOPIC_0000002553361193__oh_texteditorproxy_gettextconfigfunc)的执行线程由调用[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)的线程决定，不受本接口影响，若需该回调也在主线程执行，需确保[OH_InputMethodController_Attach](inputmethod_controller_capi.h.md#ZH-CN_TOPIC_0000002553201231__oh_inputmethodcontroller_attach)在主线程调用。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| InputMethod_TextEditorProxy *proxy | 指向目标InputMethod_TextEditorProxy实例的指针。 |
| bool isCallbackInMainThread | 线程执行策略。- true：回调函数切换至主线程执行（用于避免多线程并发问题）。避免在回调内执行耗时操作，防止主线程阻塞。- false：回调函数在IPC线程执行（可能存在多线程并发情况）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| InputMethod_ErrorCode | 执行结果。  IME_ERR_OK - 配置成功。  IME_ERR_NULL_POINTER - 当proxy为NULL时返回。 |