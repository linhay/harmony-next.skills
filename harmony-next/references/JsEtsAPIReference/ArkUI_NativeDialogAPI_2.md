# ArkUI_NativeDialogAPI_2

```ets
typedef struct {...} ArkUI_NativeDialogAPI_2
```

#### 概述

ArkUI提供的Native侧自定义弹窗接口集合。

**起始版本：** 15

**相关模块：**[ArkUI_NativeModule](ArkUI_NativeModule.md)

**所在头文件：**[native_dialog.h](native_dialog.h.md)

#### 汇总

#### 成员变量

名称描述[ArkUI_NativeDialogAPI_1](ArkUI_NativeDialogAPI_1.md) nativeDialogAPI1

ArkUI提供的Native侧自定义弹窗接口集合，范围是[ArkUI_NativeDialogAPI_1](ArkUI_NativeDialogAPI_1.md)。

**起始版本：** 15

#### 成员函数

名称描述[int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit)](#ZH-CN_TOPIC_0000002497605098__setkeyboardavoiddistance)弹窗避让键盘后，和键盘之间距离。[int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode)](#ZH-CN_TOPIC_0000002497605098__setlevelmode)设置弹窗的显示层级。[int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId)](#ZH-CN_TOPIC_0000002497605098__setleveluniqueid)设置弹窗显示层级页面下的节点id。[int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode)](#ZH-CN_TOPIC_0000002497605098__setimmersivemode)设置嵌入式弹窗蒙层的显示区域。

#### 成员函数说明

#### setKeyboardAvoidDistance()

```ets
int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit)
```

**描述：**

弹窗避让键盘后，和键盘之间距离。

setKeyboardAvoidDistance方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002529445063__show)方法之前调用。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_NativeDialogHandle](ArkUI_NativeDialog_.md) handle指向自定义弹窗控制器的指针。float distance避让键盘的距离，单位为vp。[ArkUI_LengthMetricUnit](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_lengthmetricunit) unit避让距离的单位，参数类型[ArkUI_LengthMetricUnit](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_lengthmetricunit)。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### setLevelMode()

```ets
int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode)
```

**描述：**

设置弹窗的显示层级。

setLevelMode方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002529445063__show)方法之前调用。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_NativeDialogHandle](ArkUI_NativeDialog_.md) handle指向自定义弹窗控制器的指针。[ArkUI_LevelMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_levelmode) levelMode显示层级的枚举值， 类型为[ArkUI_LevelMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_levelmode)。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### setLevelUniqueId()

```ets
int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId)
```

**描述：**

设置弹窗显示层级页面下的节点id。

setLevelUniqueId方法需要在调用[setLevelMode](#ZH-CN_TOPIC_0000002497605098__setlevelmode)方法之前调用。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_NativeDialogHandle](ArkUI_NativeDialog_.md) handle指向自定义弹窗控制器的指针。int32_t uniqueId指定节点id，会查找该节点所在页面，并将弹窗显示在该页面下。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### setImmersiveMode()

```ets
int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode)
```

**描述：**

设置嵌入式弹窗蒙层的显示区域。

setImmersiveMode方法需要在调用[show](ArkUI_NativeDialogAPI_1.md#ZH-CN_TOPIC_0000002529445063__show)方法之前调用。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_NativeDialogHandle](ArkUI_NativeDialog_.md) handle指向自定义弹窗控制器的指针。[ArkUI_ImmersiveMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_immersivemode) immersiveMode显示区域类型的枚举值， 类型为[ArkUI_ImmersiveMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_immersivemode)。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。