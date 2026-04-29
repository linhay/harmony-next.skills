# ArkUI_NativeDialogAPI_2

```ets
typedef struct {...} ArkUI_NativeDialogAPI_2
```

**概述**

ArkUI提供的Native侧自定义弹窗接口集合。

起始版本： 15

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_dialog.h](native_dialog.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeDialogAPI_1 nativeDialogAPI1 | ArkUI提供的Native侧自定义弹窗接口集合，范围是ArkUI_NativeDialogAPI_1。 起始版本： 15 |

**成员函数**

| 名称 | 描述 |
| --- | --- |
| int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit) | 弹窗避让键盘后，和键盘之间距离。 |
| int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode) | 设置弹窗的显示层级。 |
| int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId) | 设置弹窗显示层级页面下的节点id。 |
| int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode) | 设置嵌入式弹窗蒙层的显示区域。 |

**成员函数说明**

**setKeyboardAvoidDistance()**

```ets
int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit)
```

描述：

弹窗避让键盘后，和键盘之间距离。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setKeyboardAvoidDistance方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| float distance | 避让键盘的距离，单位为vp。 |
| ArkUI_LengthMetricUnit unit | 避让距离的单位，参数类型ArkUI_LengthMetricUnit。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_CAPI_INIT_ERROR 接口初始化错误。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setLevelMode()**

```ets
int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode)
```

描述：

设置弹窗的显示层级。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setLevelMode方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_LevelMode levelMode | 显示层级的枚举值， 类型为ArkUI_LevelMode。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setLevelUniqueId()**

```ets
int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId)
```

描述：

设置弹窗显示层级页面下的节点id。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setLevelUniqueId方法需要在调用[setLevelMode](#ZH-CN_TOPIC_0000002522241048__setlevelmode)方法之前调用。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| int32_t uniqueId | 指定节点id，会查找该节点所在页面，并将弹窗显示在该页面下。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setImmersiveMode()**

```ets
int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode)
```

描述：

设置嵌入式弹窗蒙层的显示区域。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setImmersiveMode方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002553360975__show)方法之前调用。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_ImmersiveMode immersiveMode | 显示区域类型的枚举值， 类型为ArkUI_ImmersiveMode。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |