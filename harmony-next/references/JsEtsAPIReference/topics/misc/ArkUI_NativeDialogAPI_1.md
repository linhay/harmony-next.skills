# ArkUI_NativeDialogAPI_1

```ets
typedef struct {...} ArkUI_NativeDialogAPI_1
```

**概述**

ArkUI提供的Native侧自定义弹窗接口集合。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_dialog.h](native_dialog.h.md)

**汇总**

**成员函数**

| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle (*create)() | 创建自定义弹窗并返回指向自定义弹窗的指针。 |
| void (*dispose)(ArkUI_NativeDialogHandle handle) | 销毁自定义弹窗。 |
| int32_t (*setContent)(ArkUI_NativeDialogHandle handle, ArkUI_NodeHandle content) | 挂载自定义弹窗内容。 |
| int32_t (*removeContent)(ArkUI_NativeDialogHandle handle) | 卸载自定义弹窗内容。 |
| int32_t (*setContentAlignment)(ArkUI_NativeDialogHandle handle, int32_t alignment, float offsetX, float offsetY) | 设置自定义弹窗对齐方式。 |
| int32_t (*resetContentAlignment)(ArkUI_NativeDialogHandle handle) | 重置setContentAlignment方法设置的属性，使用系统默认的对齐方式。 |
| int32_t (*setModalMode)(ArkUI_NativeDialogHandle handle, bool isModal) | 设置自定义弹窗是否开启模态样式的弹窗。 |
| int32_t (*setAutoCancel)(ArkUI_NativeDialogHandle handle, bool autoCancel) | 设置自定义弹窗是否允许通过点击遮罩层退出。 |
| int32_t (*setMask)(ArkUI_NativeDialogHandle handle, uint32_t maskColor, const ArkUI_Rect* maskRect) | 设置自定义弹窗遮罩属性。 |
| int32_t (*setBackgroundColor)(ArkUI_NativeDialogHandle handle, uint32_t backgroundColor) | 设置弹窗背景色。 |
| int32_t (*setCornerRadius)(ArkUI_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight) | 设置弹窗背板圆角半径。 |
| int32_t (*setGridColumnCount)(ArkUI_NativeDialogHandle handle, int32_t gridCount) | 设置弹窗宽度占栅格宽度的个数。 |
| int32_t (*enableCustomStyle)(ArkUI_NativeDialogHandle handle, bool enableCustomStyle) | 弹窗容器样式是否可以自定义。 |
| int32_t (*enableCustomAnimation)(ArkUI_NativeDialogHandle handle, bool enableCustomAnimation) | 弹窗容器是否使用自定义弹窗动画。 |
| int32_t (*registerOnWillDismiss)(ArkUI_NativeDialogHandle handle, ArkUI_OnWillDismissEvent eventHandler) | 当触发系统定义的返回操作、键盘ESC关闭交互操作时，如果注册了该回调函数，弹窗不会立即关闭，而是由用户决定是否关闭。 |
| int32_t (*show)(ArkUI_NativeDialogHandle handle, bool showInSubWindow) | 显示自定义弹窗。 |
| int32_t (*close)(ArkUI_NativeDialogHandle handle) | 关闭自定义弹窗，如已关闭，则不生效。 |
| int32_t (*registerOnWillDismissWithUserData)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event)) | 注册系统关闭自定义弹窗的监听事件。 |

**成员函数说明**

**create()**

```ets
ArkUI_NativeDialogHandle (*create)()
```

描述：

创建自定义弹窗并返回指向自定义弹窗的指针。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

create方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NativeDialogHandle | 返回指向自定义弹窗的指针，如果创建失败，则返回空指针。 |

**dispose()**

```ets
void (*dispose)(ArkUI_NativeDialogHandle handle)
```

描述：

销毁自定义弹窗。

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |

**setContent()**

```ets
int32_t (*setContent)(ArkUI_NativeDialogHandle handle, ArkUI_NodeHandle content)
```

描述：

挂载自定义弹窗内容。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setContent方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_NodeHandle content | 弹窗内容根节点指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**removeContent()**

```ets
int32_t (*removeContent)(ArkUI_NativeDialogHandle handle)
```

描述：

卸载自定义弹窗内容。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

removeContent方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setContentAlignment()**

```ets
int32_t (*setContentAlignment)(ArkUI_NativeDialogHandle handle, int32_t alignment, float offsetX, float offsetY)
```

描述：

设置自定义弹窗对齐方式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setContentAlignment方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| int32_t alignment | 对齐方式，参数类型ArkUI_Alignment。 |
| float offsetX | 弹窗的水平偏移量，浮点型。 |
| float offsetY | 弹窗的垂直偏移量，浮点型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**resetContentAlignment()**

```ets
int32_t (*resetContentAlignment)(ArkUI_NativeDialogHandle handle)
```

描述：

重置setContentAlignment方法设置的属性，使用系统默认的对齐方式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

resetContentAlignment方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setModalMode()**

```ets
int32_t (*setModalMode)(ArkUI_NativeDialogHandle handle, bool isModal)
```

描述：

设置自定义弹窗是否开启模态样式的弹窗。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setModalMode方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| bool isModal | 设置是否开启模态窗口，模态窗口有蒙层，非模态窗口无蒙层。为true时开启模态窗口，为false时不开启模态窗口。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setAutoCancel()**

```ets
int32_t (*setAutoCancel)(ArkUI_NativeDialogHandle handle, bool autoCancel)
```

描述：

设置自定义弹窗是否允许通过点击遮罩层退出。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setAutoCancel方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| bool autoCancel | 设置是否允许通过点击遮罩层退出，true表示关闭弹窗，false表示不关闭弹窗。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setMask()**

```ets
int32_t (*setMask)(ArkUI_NativeDialogHandle handle, uint32_t maskColor, const ArkUI_Rect* maskRect)
```

描述：

设置自定义弹窗遮罩属性。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setMask方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| uint32_t maskColor | 设置遮罩颜色，0xargb格式。 |
| const ArkUI_Rect* maskRect | 遮蔽层区域范围的指针，遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。参数类型ArkUI_Rect。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setBackgroundColor()**

```ets
int32_t (*setBackgroundColor)(ArkUI_NativeDialogHandle handle, uint32_t backgroundColor)
```

描述：

设置弹窗背景色。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setBackgroundColor方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| uint32_t backgroundColor | 设置弹窗背景颜色，0xargb格式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setCornerRadius()**

```ets
int32_t (*setCornerRadius)(ArkUI_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight)
```

描述：

设置弹窗背板圆角半径。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setCornerRadius方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| float topLeft | 设置弹窗背板左上角圆角半径。 |
| float topRight | 设置弹窗背板右上角圆角半径。 |
| float bottomLeft | 设置弹窗背板左下圆角半径。 |
| float bottomRight | 设置弹窗背板右下角圆角半径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setGridColumnCount()**

```ets
int32_t (*setGridColumnCount)(ArkUI_NativeDialogHandle handle, int32_t gridCount)
```

描述：

设置弹窗宽度占栅格宽度的个数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setGridColumnCount方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| int32_t gridCount | 默认为按照窗口大小自适应，最大栅格数为系统最大栅格数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**enableCustomStyle()**

```ets
int32_t (*enableCustomStyle)(ArkUI_NativeDialogHandle handle, bool enableCustomStyle)
```

描述：

弹窗容器样式是否可以自定义。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

enableCustomStyle方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| bool enableCustomStyle | 弹窗容器样式是否可以自定义。 默认值：false true：弹窗容器样式不能自定义，宽度自适应子节点，圆角为0，弹窗背景色透明；false：弹窗容器样式可以自定义，高度自适应子节点，宽度由栅格系统定义，圆角半径24vp，PC/2in1设备避让屏幕边缘以及窗口标题栏。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**enableCustomAnimation()**

```ets
int32_t (*enableCustomAnimation)(ArkUI_NativeDialogHandle handle, bool enableCustomAnimation)
```

描述：

弹窗容器是否使用自定义弹窗动画。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

enableCustomAnimation方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| bool enableCustomAnimation | true:使用自定义动画，关闭系统默认动画；false:使用系统默认动画。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**registerOnWillDismiss()**

```ets
int32_t (*registerOnWillDismiss)(ArkUI_NativeDialogHandle handle, ArkUI_OnWillDismissEvent eventHandler)
```

描述：

当触发系统定义的返回操作、键盘ESC关闭交互操作时，如果注册了该回调函数，弹窗不会立即关闭，而是由用户决定是否关闭。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

registerOnWillDismiss方法需要在调用[show](#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_OnWillDismissEvent eventHandler | 弹窗关闭的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**show()**

```ets
int32_t (*show)(ArkUI_NativeDialogHandle handle, bool showInSubWindow)
```

描述：

显示自定义弹窗。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| bool showInSubWindow | 是否在子窗口显示弹窗。true表示在子窗显示弹窗。false表示不在子窗显示弹窗。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**close()**

```ets
int32_t (*close)(ArkUI_NativeDialogHandle handle)
```

描述：

关闭自定义弹窗，如已关闭，则不生效。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**registerOnWillDismissWithUserData()**

```ets
int32_t (*registerOnWillDismissWithUserData)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event))
```

描述：

注册系统关闭自定义弹窗的监听事件。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| void* userData | 用户自定义数据指针。 |
| callback | 监听自定义弹窗关闭的回调事件。  - event: 回调函数的入参，捕获关闭原因。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |