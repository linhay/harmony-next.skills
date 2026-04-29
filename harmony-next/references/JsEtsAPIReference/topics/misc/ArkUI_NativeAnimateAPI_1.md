# ArkUI_NativeAnimateAPI_1

```ets
typedef struct {...} ArkUI_NativeAnimateAPI_1
```

**概述**

ArkUI提供的Native侧动画接口集合。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_animate.h](native_animate.h.md)

**汇总**

**成员函数**

| 名称 | 描述 |
| --- | --- |
| int32_t (*animateTo)(ArkUI_ContextHandle context, ArkUI_AnimateOption* option, ArkUI_ContextCallback* update,ArkUI_AnimateCompleteCallback* complete) | 显式动画接口。 |
| int32_t (*keyframeAnimateTo)(ArkUI_ContextHandle context, ArkUI_KeyframeAnimateOption* option) | 关键帧动画接口。 |
| ArkUI_AnimatorHandle (*createAnimator)(ArkUI_ContextHandle context, ArkUI_AnimatorOption* option) | 创建animator动画对象。 |
| void (*disposeAnimator)(ArkUI_AnimatorHandle animatorHandle) | 销毁animator动画对象。 |

**成员函数说明**

**animateTo()**

```ets
int32_t (*animateTo)(ArkUI_ContextHandle context, ArkUI_AnimateOption* option, ArkUI_ContextCallback* update,ArkUI_AnimateCompleteCallback* complete)
```

描述：

显式动画接口。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

event闭包中要设置的组件属性，必须在其之前设置过。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle context | UIContext实例。 |
| ArkUI_AnimateOption* option | 设置动画效果相关参数。 |
| ArkUI_ContextCallback* update | 指定动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |
| ArkUI_AnimateCompleteCallback* complete | 设置动画播放完成回调参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**keyframeAnimateTo()**

```ets
int32_t (*keyframeAnimateTo)(ArkUI_ContextHandle context, ArkUI_KeyframeAnimateOption* option)
```

描述：

关键帧动画接口。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle context | UIContext实例。 |
| ArkUI_KeyframeAnimateOption* option | 关键帧动画参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**createAnimator()**

```ets
ArkUI_AnimatorHandle (*createAnimator)(ArkUI_ContextHandle context, ArkUI_AnimatorOption* option)
```

描述：

创建animator动画对象。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle context | UIContext实例。 |
| ArkUI_AnimatorOption* option | animator动画参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AnimatorHandle | animator动画对象指针。函数参数异常时返回NULL。 |

**disposeAnimator()**

```ets
void (*disposeAnimator)(ArkUI_AnimatorHandle animatorHandle)
```

描述：

销毁animator动画对象。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AnimatorHandle animatorHandle | animator动画对象。 |