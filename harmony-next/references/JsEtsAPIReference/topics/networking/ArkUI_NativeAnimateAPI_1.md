# ArkUI_NativeAnimateAPI_1

```ets
typedef struct {...} ArkUI_NativeAnimateAPI_1
```

#### 概述

ArkUI提供的Native侧动画接口集合。

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](../system-services/ArkUI_NativeModule.md)

**所在头文件：**[native_animate.h](../../capi/headers/native_animate.h.md)

#### 汇总

#### 成员函数

名称描述[int32_t (*animateTo)(ArkUI_ContextHandle context, ArkUI_AnimateOption* option, ArkUI_ContextCallback* update,ArkUI_AnimateCompleteCallback* complete)](#ZH-CN_TOPIC_0000002497445114__animateto)显式动画接口。[int32_t (*keyframeAnimateTo)(ArkUI_ContextHandle context, ArkUI_KeyframeAnimateOption* option)](#ZH-CN_TOPIC_0000002497445114__keyframeanimateto)关键帧动画接口。[ArkUI_AnimatorHandle (*createAnimator)(ArkUI_ContextHandle context, ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002497445114__createanimator)创建animator动画对象。[void (*disposeAnimator)(ArkUI_AnimatorHandle animatorHandle)](#ZH-CN_TOPIC_0000002497445114__disposeanimator)销毁animator动画对象。

#### 成员函数说明

#### animateTo()

```ets
int32_t (*animateTo)(ArkUI_ContextHandle context, ArkUI_AnimateOption* option, ArkUI_ContextCallback* update,ArkUI_AnimateCompleteCallback* complete)
```

**描述：**

显式动画接口。

event闭包中要设置的组件属性，必须在其之前设置过。

**参数：**

参数项描述[ArkUI_ContextHandle](../graphics/ArkUI_Context_.md) contextUIContext实例。[ArkUI_AnimateOption](../media/ArkUI_AnimateOption.md)* option设置动画效果相关参数。[ArkUI_ContextCallback](../graphics/ArkUI_ContextCallback.md)* update指定动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。[ArkUI_AnimateCompleteCallback](../media/ArkUI_AnimateCompleteCallback.md)* complete设置动画播放完成回调参数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](../../capi/headers/native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](../../capi/headers/native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### keyframeAnimateTo()

```ets
int32_t (*keyframeAnimateTo)(ArkUI_ContextHandle context, ArkUI_KeyframeAnimateOption* option)
```

**描述：**

关键帧动画接口。

**参数：**

参数项描述[ArkUI_ContextHandle](../graphics/ArkUI_Context_.md) contextUIContext实例。[ArkUI_KeyframeAnimateOption](../components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](../../capi/headers/native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](../../capi/headers/native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### createAnimator()

```ets
ArkUI_AnimatorHandle (*createAnimator)(ArkUI_ContextHandle context, ArkUI_AnimatorOption* option)
```

**描述：**

创建animator动画对象。

**参数：**

参数项描述[ArkUI_ContextHandle](../graphics/ArkUI_Context_.md) contextUIContext实例。[ArkUI_AnimatorOption](../media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明[ArkUI_AnimatorHandle](../media/ArkUI_Animator_.md)animator动画对象指针。函数参数异常时返回NULL。

#### disposeAnimator()

```ets
void (*disposeAnimator)(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

销毁animator动画对象。

**参数：**

参数项描述[ArkUI_AnimatorHandle](../media/ArkUI_Animator_.md) animatorHandleanimator动画对象。