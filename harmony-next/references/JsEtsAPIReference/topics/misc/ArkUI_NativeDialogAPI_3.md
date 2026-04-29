# ArkUI_NativeDialogAPI_3

```ets
typedef struct {...} ArkUI_NativeDialogAPI_3
```

**概述**

ArkUI提供的Native侧自定义弹窗接口集合。

起始版本： 19

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_dialog.h](native_dialog.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeDialogAPI_1 nativeDialogAPI1 | ArkUI提供的Native侧自定义弹窗接口集合，范围是ArkUI_NativeDialogAPI_1。 起始版本： 19 |
| ArkUI_NativeDialogAPI_2 nativeDialogAPI2 | ArkUI提供的Native侧自定义弹窗接口集合，范围是ArkUI_NativeDialogAPI_2。 起始版本： 19 |

**成员函数**

| 名称 | 描述 |
| --- | --- |
| int32_t (*setLevelOrder)(ArkUI_NativeDialogHandle handle, double levelOrder) | 设置自定义弹窗显示的顺序。 |
| int32_t (*registerOnWillAppear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData)) | 注册自定义弹窗显示之前的回调函数。 |
| int32_t (*registerOnDidAppear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData)) | 注册自定义弹窗显示之后的回调函数。 |
| int32_t (*registerOnWillDisappear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData)) | 注册自定义弹窗关闭之前的回调函数。 |
| int32_t (*registerOnDidDisappear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData)) | 注册自定义弹窗关闭之后的回调函数。 |
| int32_t (*setBorderWidth)(ArkUI_NativeDialogHandle handle, float top, float right, float bottom, float left, ArkUI_LengthMetricUnit unit) | 设置自定义弹窗的边框宽度。 |
| int32_t (*setBorderColor)(ArkUI_NativeDialogHandle handle, uint32_t top, uint32_t right, uint32_t bottom, uint32_t left) | 设置自定义弹窗的边框颜色。 |
| int32_t (*setBorderStyle)(ArkUI_NativeDialogHandle handle, int32_t top, int32_t right, int32_t bottom, int32_t left) | 设置自定义弹窗的边框样式。 |
| int32_t (*setWidth)(ArkUI_NativeDialogHandle handle, float width, ArkUI_LengthMetricUnit unit) | 设置自定义弹窗的背板宽度。 |
| int32_t (*setHeight)(ArkUI_NativeDialogHandle handle, float height, ArkUI_LengthMetricUnit unit) | 设置自定义弹窗的背板高度。 |
| int32_t (*setShadow)(ArkUI_NativeDialogHandle handle, ArkUI_ShadowStyle shadow) | 设置自定义弹窗的背板阴影。 |
| int32_t (*setCustomShadow)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* customShadow) | 设置自定义弹窗的背板阴影。 |
| int32_t (*setBackgroundBlurStyle)(ArkUI_NativeDialogHandle handle, ArkUI_BlurStyle blurStyle) | 设置自定义弹窗的背板模糊材质。 |
| int32_t (*setKeyboardAvoidMode)(ArkUI_NativeDialogHandle handle, ArkUI_KeyboardAvoidMode keyboardAvoidMode) | 设置自定义弹窗避让键盘模式。 |
| int32_t (*enableHoverMode)(ArkUI_NativeDialogHandle handle, bool enableHoverMode) | 设置自定义弹窗是否响应悬停态。 |
| int32_t (*setHoverModeArea)(ArkUI_NativeDialogHandle handle, ArkUI_HoverModeAreaType hoverModeAreaType) | 设置悬停态下自定义弹窗默认展示区域。 |
| int32_t (*setFocusable)(ArkUI_NativeDialogHandle handle, bool focusable) | 设置自定义弹窗是否获取焦点。 |
| int32_t (*setBackgroundBlurStyleOptions)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* backgroundBlurStyleOptions) | 设置自定义弹窗的背景模糊效果。 |
| int32_t (*setBackgroundEffect)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* backgroundEffect) | 设置自定义弹窗的背景效果参数。 |

**成员函数说明**

**setLevelOrder()**

```ets
int32_t (*setLevelOrder)(ArkUI_NativeDialogHandle handle, double levelOrder)
```

描述：

设置自定义弹窗显示的顺序。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setLevelOrder方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| double levelOrder | 自定义弹窗显示的顺序。默认值：0，取值范围：[-100000.0, 100000.0]。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**registerOnWillAppear()**

```ets
int32_t (*registerOnWillAppear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

描述：

注册自定义弹窗显示之前的回调函数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

registerOnWillAppear方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| void* userData | 用户自定义数据。 |
| callback | 自定义弹窗显示之前的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**registerOnDidAppear()**

```ets
int32_t (*registerOnDidAppear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

描述：

注册自定义弹窗显示之后的回调函数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

registerOnDidAppear方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| void* userData | 用户自定义数据。 |
| callback | 自定义弹窗显示之后的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**registerOnWillDisappear()**

```ets
int32_t (*registerOnWillDisappear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

描述：

注册自定义弹窗关闭之前的回调函数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

registerOnWillDisappear方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| void* userData | 用户自定义数据。 |
| callback | 自定义弹窗关闭之前的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**registerOnDidDisappear()**

```ets
int32_t (*registerOnDidDisappear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

描述：

注册自定义弹窗关闭之后的回调函数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

registerOnDidDisappear方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| void* userData | 用户自定义数据。 |
| callback | 自定义弹窗关闭之后的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setBorderWidth()**

```ets
int32_t (*setBorderWidth)(ArkUI_NativeDialogHandle handle, float top, float right, float bottom, float left, ArkUI_LengthMetricUnit unit)
```

描述：

设置自定义弹窗的边框宽度。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setBorderWidth方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| float top | 上边框的宽度。 |
| float right | 右边框的宽度。 |
| float bottom | 下边框的宽度。 |
| float left | 左边框的宽度。 |
| ArkUI_LengthMetricUnit unit | 指定宽度单位，默认为vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setBorderColor()**

```ets
int32_t (*setBorderColor)(ArkUI_NativeDialogHandle handle, uint32_t top, uint32_t right, uint32_t bottom, uint32_t left)
```

描述：

设置自定义弹窗的边框颜色。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setBorderColor方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| uint32_t top | 上边框的颜色。 |
| uint32_t right | 右边框的颜色。 |
| uint32_t bottom | 下边框的颜色。 |
| uint32_t left | 左边框的颜色。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setBorderStyle()**

```ets
int32_t (*setBorderStyle)(ArkUI_NativeDialogHandle handle, int32_t top, int32_t right, int32_t bottom, int32_t left)
```

描述：

设置自定义弹窗的边框样式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setBorderStyle方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| int32_t top | 上边框的样式。 |
| int32_t right | 右边框的样式。 |
| int32_t bottom | 下边框的样式。 |
| int32_t left | 左边框的样式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setWidth()**

```ets
int32_t (*setWidth)(ArkUI_NativeDialogHandle handle, float width, ArkUI_LengthMetricUnit unit)
```

描述：

设置自定义弹窗的背板宽度。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setWidth方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| float width | 背板宽度。 |
| ArkUI_LengthMetricUnit unit | 指定宽度的单位，默认为vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setHeight()**

```ets
int32_t (*setHeight)(ArkUI_NativeDialogHandle handle, float height, ArkUI_LengthMetricUnit unit)
```

描述：

设置自定义弹窗的背板高度。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setHeight方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| float height | 背板高度。 |
| ArkUI_LengthMetricUnit unit | 指定高度的单位，默认为vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setShadow()**

```ets
int32_t (*setShadow)(ArkUI_NativeDialogHandle handle, ArkUI_ShadowStyle shadow)
```

描述：

设置自定义弹窗的背板阴影。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setShadow方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_ShadowStyle shadow | 背板阴影样式，枚举值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setCustomShadow()**

```ets
int32_t (*setCustomShadow)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* customShadow)
```

描述：

设置自定义弹窗的背板阴影。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setCustomShadow方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| const ArkUI_AttributeItem* customShadow | 自定义阴影参数，格式与ArkUI_NodeAttributeType中的NODE_SHADOW属性一致。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setBackgroundBlurStyle()**

```ets
int32_t (*setBackgroundBlurStyle)(ArkUI_NativeDialogHandle handle, ArkUI_BlurStyle blurStyle)
```

描述：

设置自定义弹窗的背板模糊材质。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setBackgroundBlurStyle方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_BlurStyle blurStyle | 背板模糊材质，枚举值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setKeyboardAvoidMode()**

```ets
int32_t (*setKeyboardAvoidMode)(ArkUI_NativeDialogHandle handle, ArkUI_KeyboardAvoidMode keyboardAvoidMode)
```

描述：

设置自定义弹窗避让键盘模式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setKeyboardAvoidMode方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_KeyboardAvoidMode keyboardAvoidMode | 避让键盘模式，枚举值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**enableHoverMode()**

```ets
int32_t (*enableHoverMode)(ArkUI_NativeDialogHandle handle, bool enableHoverMode)
```

描述：

设置自定义弹窗是否响应悬停态。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

enableHoverMode方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| bool enableHoverMode | 是否响应悬停态，默认false。true表示响应悬停态，false表示不响应悬停态。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setHoverModeArea()**

```ets
int32_t (*setHoverModeArea)(ArkUI_NativeDialogHandle handle, ArkUI_HoverModeAreaType hoverModeAreaType)
```

描述：

设置悬停态下自定义弹窗默认展示区域。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setHoverModeArea方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_HoverModeAreaType hoverModeAreaType | 悬停态区域，枚举值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setFocusable()**

```ets
int32_t (*setFocusable)(ArkUI_NativeDialogHandle handle, bool focusable)
```

描述：

设置自定义弹窗是否获取焦点。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setFocusable方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| bool focusable | 自定义弹窗是否获取焦点。true表示自动获取焦点，false表示不自动获取焦点。默认值：true |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setBackgroundBlurStyleOptions()**

```ets
int32_t (*setBackgroundBlurStyleOptions)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* backgroundBlurStyleOptions)
```

描述：

设置自定义弹窗的背景模糊效果。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setBackgroundBlurStyleOptions方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| const ArkUI_AttributeItem* backgroundBlurStyleOptions | 背景模糊效果。参数ArkUI_AttributeItem格式：  .value[0].i32 表示深浅色模式，取ArkUI_ColorMode枚举值。  .value[1]?.i32 表示取色模式，取ArkUI_AdaptiveColor枚举值。  .value[2]?.f32 表示模糊效果程度，取[0.0,1.0]范围内的值。  .value[3]?.u32 表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]。  .value[4]?.u32 表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]。  .value[5]?.i32 表示模糊激活策略，取ArkUI_BlurStyleActivePolicy枚举值。  .value[6]?.u32 表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setBackgroundEffect()**

```ets
int32_t (*setBackgroundEffect)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* backgroundEffect)
```

描述：

设置自定义弹窗的背景效果参数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setBackgroundEffect方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)之前调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| const ArkUI_AttributeItem* backgroundEffect | 背景效果参数。参数ArkUI_AttributeItem格式：  .value[0].f32 表示模糊半径，单位为vp。  .value[1]?.f32 表示饱和度。  .value[2]?.f32 表示亮度。  .value[3]?.u32 表示颜色，0xargb类型。  .value[4]?.i32 表示取色模式，取ArkUI_AdaptiveColor枚举值。  .value[5]?.u32 表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]。  .value[6]?.u32 表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]。  .value[7]?.i32 表示模糊激活策略，取ArkUI_BlurStyleActivePolicy枚举值。  .value[8]?.u32 表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |