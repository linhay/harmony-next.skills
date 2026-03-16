# native_animate.h

#### 概述

提供ArkUI在Native侧的动画接口定义集合。

**引用文件：** <arkui/native_animate.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](../../topics/system-services/ArkUI_NativeModule.md)

**相关示例：**[AnimationNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/AnimationNDK)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkUI_ExpectedFrameRateRange](../../topics/components/ArkUI_ExpectedFrameRateRange.md)ArkUI_ExpectedFrameRateRange设置动画的期望帧率。[ArkUI_AnimateCompleteCallback](../../topics/media/ArkUI_AnimateCompleteCallback.md)ArkUI_AnimateCompleteCallback动画播放结束回调类型。[ArkUI_NativeAnimateAPI_1](../../topics/networking/ArkUI_NativeAnimateAPI_1.md)ArkUI_NativeAnimateAPI_1ArkUI提供的Native侧动画接口集合。[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)ArkUI_AnimateOption设置动画效果相关参数。[ArkUI_Curve](../../topics/media/ArkUI_Curve.md)ArkUI_Curve提供曲线的插值对象定义。[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)ArkUI_Curve*定义曲线的插值对象指针定义。[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)ArkUI_KeyframeAnimateOption定义关键帧动画参数对象。[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)ArkUI_AnimatorOption定义animator动画参数对象。[ArkUI_AnimatorHandle](../../topics/media/ArkUI_Animator_.md)ArkUI_Animator*定义animator动画对象指针。[ArkUI_AnimatorEvent](../../topics/media/ArkUI_AnimatorEvent.md)ArkUI_AnimatorEvent定义animator回调事件对象。[ArkUI_AnimatorOnFrameEvent](../../topics/components/ArkUI_AnimatorOnFrameEvent.md)ArkUI_AnimatorOnFrameEvent定义animator接收到帧时回调对象。[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)ArkUI_TransitionEffect定义transition属性配置转场参数对象。

#### 函数

名称描述[ArkUI_AnimateOption* OH_ArkUI_AnimateOption_Create()](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_create)创建动画效果参数。[void OH_ArkUI_AnimateOption_Dispose(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_dispose)销毁动画效果参数指针。[uint32_t OH_ArkUI_AnimateOption_GetDuration(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_getduration)获取动画持续时间，单位为ms（毫秒）。[float OH_ArkUI_AnimateOption_GetTempo(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_gettempo)获取动画播放速度。[ArkUI_AnimationCurve OH_ArkUI_AnimateOption_GetCurve(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_getcurve)获取动画曲线。[int32_t OH_ArkUI_AnimateOption_GetDelay(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_getdelay)获取动画延迟播放时间，单位为ms（毫秒）。[int32_t OH_ArkUI_AnimateOption_GetIterations(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_getiterations)获取动画播放次数。[ArkUI_AnimationPlayMode OH_ArkUI_AnimateOption_GetPlayMode(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_getplaymode)获取动画播放模式。[ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimateOption_GetExpectedFrameRateRange(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_getexpectedframeraterange)获取动画的期望帧率。[void OH_ArkUI_AnimateOption_SetDuration(ArkUI_AnimateOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_setduration)设置动画持续时间，单位为ms（毫秒）。[void OH_ArkUI_AnimateOption_SetTempo(ArkUI_AnimateOption* option, float value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_settempo)设置动画播放速度。[void OH_ArkUI_AnimateOption_SetCurve(ArkUI_AnimateOption* option, ArkUI_AnimationCurve value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_setcurve)设置动画曲线。[void OH_ArkUI_AnimateOption_SetDelay(ArkUI_AnimateOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_setdelay)设置动画延迟播放时间，单位为ms（毫秒）。[void OH_ArkUI_AnimateOption_SetIterations(ArkUI_AnimateOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_setiterations)设置动画播放次数。[void OH_ArkUI_AnimateOption_SetPlayMode(ArkUI_AnimateOption* option, ArkUI_AnimationPlayMode value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_setplaymode)设置动画播放模式。[void OH_ArkUI_AnimateOption_SetExpectedFrameRateRange(ArkUI_AnimateOption* option, ArkUI_ExpectedFrameRateRange* value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_setexpectedframeraterange)设置动画的期望帧率。[void OH_ArkUI_AnimateOption_SetICurve(ArkUI_AnimateOption* option, ArkUI_CurveHandle value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_seticurve)设置动画的动画曲线。[ArkUI_CurveHandle OH_ArkUI_AnimateOption_GetICurve(ArkUI_AnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_geticurve)获取动画的动画曲线。[ArkUI_KeyframeAnimateOption* OH_ArkUI_KeyframeAnimateOption_Create(int32_t size)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_create)获取关键帧动画参数。[void OH_ArkUI_KeyframeAnimateOption_Dispose(ArkUI_KeyframeAnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_dispose)销毁关键帧动画参数。[int32_t OH_ArkUI_KeyframeAnimateOption_SetDelay(ArkUI_KeyframeAnimateOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_setdelay)设置关键帧动画的整体延时时间，单位为ms（毫秒），默认不延时播放。[int32_t OH_ArkUI_KeyframeAnimateOption_SetIterations(ArkUI_KeyframeAnimateOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_setiterations)设置关键帧动画的动画播放次数。默认播放一次，设置为-1时表示无限次播放。设置为0时表示无动画效果。[int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnFinishCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*onFinish)(void* userData))](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_registeronfinishcallback)设置关键帧动画播放完成回调。当keyframe动画所有次数播放完成后调用。[int32_t OH_ArkUI_KeyframeAnimateOption_SetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option, ArkUI_ExpectedFrameRateRange* frameRate)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_setexpectedframerate)设置关键帧动画期望帧率。[int32_t OH_ArkUI_KeyframeAnimateOption_SetDuration(ArkUI_KeyframeAnimateOption* option, int32_t value, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_setduration)设置关键帧动画某段关键帧动画的持续时间，单位为ms（毫秒）。[int32_t OH_ArkUI_KeyframeAnimateOption_SetCurve(ArkUI_KeyframeAnimateOption* option, ArkUI_CurveHandle value, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_setcurve)设置关键帧动画某段关键帧使用的动画曲线。[int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnEventCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*event)(void* userData), int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_registeroneventcallback)设置关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。[int32_t OH_ArkUI_KeyframeAnimateOption_GetDelay(ArkUI_KeyframeAnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_getdelay)获取关键帧整体延时时间，单位为ms（毫秒）。[int32_t OH_ArkUI_KeyframeAnimateOption_GetIterations(ArkUI_KeyframeAnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_getiterations)获取关键帧动画播放次数。[ArkUI_ExpectedFrameRateRange* OH_ArkUI_KeyframeAnimateOption_GetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_getexpectedframerate)获取关键帧动画参数的期望帧率。[int32_t OH_ArkUI_KeyframeAnimateOption_GetDuration(ArkUI_KeyframeAnimateOption* option, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_getduration)获取关键帧动画某段状态持续时间，单位为ms（毫秒）。[ArkUI_CurveHandle OH_ArkUI_KeyframeAnimateOption_GetCurve(ArkUI_KeyframeAnimateOption* option, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_keyframeanimateoption_getcurve)获取关键帧动画某段状态动画曲线。[ArkUI_AnimatorOption* OH_ArkUI_AnimatorOption_Create(int32_t keyframeSize)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_create)创建animator动画对象参数。[void OH_ArkUI_AnimatorOption_Dispose(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_dispose)销毁animator动画对象参数。[int32_t OH_ArkUI_AnimatorOption_SetDuration(ArkUI_AnimatorOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setduration)设置animator动画播放的时长，单位为ms（毫秒）。[int32_t OH_ArkUI_AnimatorOption_SetDelay(ArkUI_AnimatorOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setdelay)设置animator动画延时播放时长，单位为ms（毫秒）。[int32_t OH_ArkUI_AnimatorOption_SetIterations(ArkUI_AnimatorOption* option, int32_t value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setiterations)设置animator动画播放次数。设置为0时不播放，设置为-1时无限次播放。[int32_t OH_ArkUI_AnimatorOption_SetFill(ArkUI_AnimatorOption* option, ArkUI_AnimationFillMode value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setfill)设置animator动画执行后是否恢复到初始状态。[int32_t OH_ArkUI_AnimatorOption_SetDirection(ArkUI_AnimatorOption* option, ArkUI_AnimationDirection value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setdirection)设置animator动画播放方向。[int32_t OH_ArkUI_AnimatorOption_SetCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setcurve)设置animator动画插值曲线。[int32_t OH_ArkUI_AnimatorOption_SetBegin(ArkUI_AnimatorOption* option, float value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setbegin)设置animator动画插值起点。[int32_t OH_ArkUI_AnimatorOption_SetEnd(ArkUI_AnimatorOption* option, float value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setend)设置animator动画插值终点。[int32_t OH_ArkUI_AnimatorOption_SetExpectedFrameRateRange(ArkUI_AnimatorOption* option, ArkUI_ExpectedFrameRateRange* value)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setexpectedframeraterange)设置animator动画期望的帧率范围。[int32_t OH_ArkUI_AnimatorOption_SetKeyframe(ArkUI_AnimatorOption* option, float time, float value, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setkeyframe)设置animator动画关键帧参数。[int32_t OH_ArkUI_AnimatorOption_SetKeyframeCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_setkeyframecurve)设置animator动画关键帧曲线类型。[int32_t OH_ArkUI_AnimatorOption_GetDuration(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getduration)获取animator动画播放的时长。[int32_t OH_ArkUI_AnimatorOption_GetDelay(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getdelay)获取animator动画延时播放时长。[int32_t OH_ArkUI_AnimatorOption_GetIterations(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getiterations)获取animator动画播放次数。[ArkUI_AnimationFillMode OH_ArkUI_AnimatorOption_GetFill(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getfill)获取animator动画执行后是否恢复到初始状态。[ArkUI_AnimationDirection OH_ArkUI_AnimatorOption_GetDirection(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getdirection)获取animator动画播放方向。[ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetCurve(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getcurve)获取animator动画插值曲线。[float OH_ArkUI_AnimatorOption_GetBegin(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getbegin)获取animator动画插值起点。[float OH_ArkUI_AnimatorOption_GetEnd(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getend)获取animator动画插值终点。[ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimatorOption_GetExpectedFrameRateRange(ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getexpectedframeraterange)获取animator动画期望的帧率范围。[float OH_ArkUI_AnimatorOption_GetKeyframeTime(ArkUI_AnimatorOption* option, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getkeyframetime)获取animator动画关键帧时间，单位为ms（毫秒）。[float OH_ArkUI_AnimatorOption_GetKeyframeValue(ArkUI_AnimatorOption* option, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getkeyframevalue)获取animator动画关键帧数值。[ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetKeyframeCurve(ArkUI_AnimatorOption* option, int32_t index)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_getkeyframecurve)获取animator动画关键帧动画插值曲线。[void* OH_ArkUI_AnimatorEvent_GetUserData(ArkUI_AnimatorEvent* event)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatorevent_getuserdata)获取动画事件对象中的用户自定义对象。[void* OH_ArkUI_AnimatorOnFrameEvent_GetUserData(ArkUI_AnimatorOnFrameEvent* event)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoronframeevent_getuserdata)获取动画事件对象中的用户自定义对象。[float OH_ArkUI_AnimatorOnFrameEvent_GetValue(ArkUI_AnimatorOnFrameEvent* event)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoronframeevent_getvalue)获取动画事件对象中的当前进度。[int32_t OH_ArkUI_AnimatorOption_RegisterOnFrameCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorOnFrameEvent* event))](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_registeronframecallback)设置animator动画接收到帧时回调。[int32_t OH_ArkUI_AnimatorOption_RegisterOnFinishCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_registeronfinishcallback)设置animator动画完成时回调。[int32_t OH_ArkUI_AnimatorOption_RegisterOnCancelCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_registeroncancelcallback)设置animator动画被取消时回调。[int32_t OH_ArkUI_AnimatorOption_RegisterOnRepeatCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animatoroption_registeronrepeatcallback)设置animator动画重复时回调。[int32_t OH_ArkUI_Animator_ResetAnimatorOption(ArkUI_AnimatorHandle animatorHandle, ArkUI_AnimatorOption* option)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animator_resetanimatoroption)更新animator动画。[int32_t OH_ArkUI_Animator_Play(ArkUI_AnimatorHandle animatorHandle)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animator_play)启动animator动画。[int32_t OH_ArkUI_Animator_Finish(ArkUI_AnimatorHandle animatorHandle)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animator_finish)结束animator动画。[int32_t OH_ArkUI_Animator_Pause(ArkUI_AnimatorHandle animatorHandle)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animator_pause)暂停animator动画。[int32_t OH_ArkUI_Animator_Cancel(ArkUI_AnimatorHandle animatorHandle)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animator_cancel)取消animator动画。[int32_t OH_ArkUI_Animator_Reverse(ArkUI_AnimatorHandle animatorHandle)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animator_reverse)以相反的顺序播放animator动画。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateCurveByType(ArkUI_AnimationCurve curve)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createcurvebytype)插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateStepsCurve(int32_t count, bool end)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createstepscurve)构造阶梯曲线对象。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createcubicbeziercurve)构造三阶贝塞尔曲线对象。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createspringcurve)构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受animation、animateTo中的duration参数控制。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createspringmotion)构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换掉前一个动画，并继承之前的速度。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createresponsivespringmotion)构造弹性跟手动画曲线对象，是springMotion的一种特例，仅默认参数不同，可与springMotion混合使用。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createinterpolatingspring)构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。[ArkUI_CurveHandle OH_ArkUI_Curve_CreateCustomCurve(void* userData, float (*interpolate)(float fraction, void* userdata))](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_createcustomcurve)构造自定义曲线对象。[void OH_ArkUI_Curve_DisposeCurve(ArkUI_CurveHandle curveHandle)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_curve_disposecurve)销毁自定义曲线对象。[ArkUI_TransitionEffect* OH_ArkUI_CreateOpacityTransitionEffect(float opacity)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_createopacitytransitioneffect)创建组件转场时的透明度效果对象。[ArkUI_TransitionEffect* OH_ArkUI_CreateTranslationTransitionEffect(ArkUI_TranslationOptions* translate)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_createtranslationtransitioneffect)创建组件转场时的平移效果对象。[ArkUI_TransitionEffect* OH_ArkUI_CreateScaleTransitionEffect(ArkUI_ScaleOptions* scale)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_createscaletransitioneffect)创建组件转场时的缩放效果对象。[ArkUI_TransitionEffect* OH_ArkUI_CreateRotationTransitionEffect(ArkUI_RotationOptions* rotate)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_createrotationtransitioneffect)创建组件转场时的旋转效果对象。[ArkUI_TransitionEffect* OH_ArkUI_CreateMovementTransitionEffect(ArkUI_TransitionEdge edge)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_createmovementtransitioneffect)创建组件平移效果对象。[ArkUI_TransitionEffect* OH_ArkUI_CreateAsymmetricTransitionEffect(ArkUI_TransitionEffect* appear, ArkUI_TransitionEffect* disappear)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_createasymmetrictransitioneffect)创建非对称的转场效果对象。[void OH_ArkUI_TransitionEffect_Dispose(ArkUI_TransitionEffect* effect)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_transitioneffect_dispose)销毁转场效果对象。[int32_t OH_ArkUI_TransitionEffect_Combine(ArkUI_TransitionEffect* firstEffect, ArkUI_TransitionEffect* secondEffect)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_transitioneffect_combine)设置转场效果链式组合，以形成包含多种转场效果的TransitionEffect。[int32_t OH_ArkUI_TransitionEffect_SetAnimation(ArkUI_TransitionEffect* effect, ArkUI_AnimateOption* animation)](#ZH-CN_TOPIC_0000002529285067__oh_arkui_transitioneffect_setanimation)设置转场效果动画参数。

#### 函数说明

#### OH_ArkUI_AnimateOption_Create()

```ets
ArkUI_AnimateOption* OH_ArkUI_AnimateOption_Create()
```

**描述：**

创建动画效果参数。

**起始版本：** 12

**返回：**

类型说明[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)*新的动画效果参数指针。

#### OH_ArkUI_AnimateOption_Dispose()

```ets
void OH_ArkUI_AnimateOption_Dispose(ArkUI_AnimateOption* option)
```

**描述：**

销毁动画效果参数指针。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

#### OH_ArkUI_AnimateOption_GetDuration()

```ets
uint32_t OH_ArkUI_AnimateOption_GetDuration(ArkUI_AnimateOption* option)
```

**描述：**

获取动画持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

**返回：**

类型说明uint32_t持续时间。

#### OH_ArkUI_AnimateOption_GetTempo()

```ets
float OH_ArkUI_AnimateOption_GetTempo(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放速度。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

**返回：**

类型说明float动画播放速度。

#### OH_ArkUI_AnimateOption_GetCurve()

```ets
ArkUI_AnimationCurve OH_ArkUI_AnimateOption_GetCurve(ArkUI_AnimateOption* option)
```

**描述：**

获取动画曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

**返回：**

类型说明[ArkUI_AnimationCurve](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationcurve)动画曲线。

#### OH_ArkUI_AnimateOption_GetDelay()

```ets
int32_t OH_ArkUI_AnimateOption_GetDelay(ArkUI_AnimateOption* option)
```

**描述：**

获取动画延迟播放时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

**返回：**

类型说明int32_t动画延迟播放时间。

#### OH_ArkUI_AnimateOption_GetIterations()

```ets
int32_t OH_ArkUI_AnimateOption_GetIterations(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放次数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

**返回：**

类型说明int32_t动画播放次数。

#### OH_ArkUI_AnimateOption_GetPlayMode()

```ets
ArkUI_AnimationPlayMode OH_ArkUI_AnimateOption_GetPlayMode(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放模式。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

**返回：**

类型说明[ArkUI_AnimationPlayMode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationplaymode)动画播放模式。

#### OH_ArkUI_AnimateOption_GetExpectedFrameRateRange()

```ets
ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimateOption_GetExpectedFrameRateRange(ArkUI_AnimateOption* option)
```

**描述：**

获取动画的期望帧率。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。

**返回：**

类型说明[ArkUI_ExpectedFrameRateRange](../../topics/components/ArkUI_ExpectedFrameRateRange.md)*动画的期望帧率，单位为帧/秒（fps）。

#### OH_ArkUI_AnimateOption_SetDuration()

```ets
void OH_ArkUI_AnimateOption_SetDuration(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。int32_t value持续时间，单位为ms（毫秒）。

#### OH_ArkUI_AnimateOption_SetTempo()

```ets
void OH_ArkUI_AnimateOption_SetTempo(ArkUI_AnimateOption* option, float value)
```

**描述：**

设置动画播放速度。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。float value动画播放速度。

#### OH_ArkUI_AnimateOption_SetCurve()

```ets
void OH_ArkUI_AnimateOption_SetCurve(ArkUI_AnimateOption* option, ArkUI_AnimationCurve value)
```

**描述：**

设置动画曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。[ArkUI_AnimationCurve](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationcurve) value动画曲线。默认值：ARKUI_CURVE_LINEAR。

#### OH_ArkUI_AnimateOption_SetDelay()

```ets
void OH_ArkUI_AnimateOption_SetDelay(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画延迟播放时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。int32_t value动画延迟播放时间，单位为ms（毫秒）。

#### OH_ArkUI_AnimateOption_SetIterations()

```ets
void OH_ArkUI_AnimateOption_SetIterations(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画播放次数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。int32_t value动画播放次数。

#### OH_ArkUI_AnimateOption_SetPlayMode()

```ets
void OH_ArkUI_AnimateOption_SetPlayMode(ArkUI_AnimateOption* option, ArkUI_AnimationPlayMode value)
```

**描述：**

设置动画播放模式。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。[ArkUI_AnimationPlayMode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationplaymode) value动画播放模式。

#### OH_ArkUI_AnimateOption_SetExpectedFrameRateRange()

```ets
void OH_ArkUI_AnimateOption_SetExpectedFrameRateRange(ArkUI_AnimateOption* option, ArkUI_ExpectedFrameRateRange* value)
```

**描述：**

设置动画的期望帧率。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* option动画效果参数。[ArkUI_ExpectedFrameRateRange](../../topics/components/ArkUI_ExpectedFrameRateRange.md)* value动画的期望帧率，单位为帧/秒（fps）。

#### OH_ArkUI_AnimateOption_SetICurve()

```ets
void OH_ArkUI_AnimateOption_SetICurve(ArkUI_AnimateOption* option, ArkUI_CurveHandle value)
```

**描述：**

设置动画的动画曲线。

此方法优先于[OH_ArkUI_AnimateOption_SetCurve](#ZH-CN_TOPIC_0000002529285067__oh_arkui_animateoption_setcurve)生效。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* optionanimator动画参数。[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md) value动画曲线参数。

#### OH_ArkUI_AnimateOption_GetICurve()

```ets
ArkUI_CurveHandle OH_ArkUI_AnimateOption_GetICurve(ArkUI_AnimateOption* option)
```

**描述：**

获取动画的动画曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* optionanimator动画参数。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)动画的动画曲线。参数option异常时返回NULL。

#### OH_ArkUI_KeyframeAnimateOption_Create()

```ets
ArkUI_KeyframeAnimateOption* OH_ArkUI_KeyframeAnimateOption_Create(int32_t size)
```

**描述：**

获取关键帧动画参数。

**起始版本：** 12

**参数：**

参数项描述int32_t size关键帧动画状态数。

**返回：**

类型说明[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)*关键帧动画参数对象。size小于0时返回NULL。

#### OH_ArkUI_KeyframeAnimateOption_Dispose()

```ets
void OH_ArkUI_KeyframeAnimateOption_Dispose(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

销毁关键帧动画参数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数对象。

#### OH_ArkUI_KeyframeAnimateOption_SetDelay()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_SetDelay(ArkUI_KeyframeAnimateOption* option, int32_t value)
```

**描述：**

设置关键帧动画的整体延时时间，单位为ms（毫秒），默认不延时播放。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。int32_t value延时时间, 单位为ms（毫秒）。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyframeAnimateOption_SetIterations()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_SetIterations(ArkUI_KeyframeAnimateOption* option, int32_t value)
```

**描述：**

设置关键帧动画的动画播放次数。默认播放一次，设置为-1时表示无限次播放。设置为0时表示无动画效果。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。int32_t value动画播放次数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyframeAnimateOption_RegisterOnFinishCallback()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnFinishCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*onFinish)(void* userData))
```

**描述：**

设置关键帧动画播放完成回调。当keyframe动画所有次数播放完成后调用。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。void* userData用户自定义对象指针。void (*onFinish)(void* userData)

回调方法。

- userData：回调函数的入参，用户自定义对象指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyframeAnimateOption_SetExpectedFrameRate()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_SetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option, ArkUI_ExpectedFrameRateRange* frameRate)
```

**描述：**

设置关键帧动画期望帧率。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。[ArkUI_ExpectedFrameRateRange](../../topics/components/ArkUI_ExpectedFrameRateRange.md)* frameRate关键帧动画的期望帧率。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyframeAnimateOption_SetDuration()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_SetDuration(ArkUI_KeyframeAnimateOption* option, int32_t value, int32_t index)
```

**描述：**

设置关键帧动画某段关键帧动画的持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。int32_t value持续时间，单位为ms（毫秒）。int32_t index状态索引值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyframeAnimateOption_SetCurve()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_SetCurve(ArkUI_KeyframeAnimateOption* option, ArkUI_CurveHandle value, int32_t index)
```

**描述：**

设置关键帧动画某段关键帧使用的动画曲线。

由于springMotion、responsiveSpringMotion、interpolatingSpring曲线时长不生效，故不支持这三种曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md) value该关键帧使用的动画曲线。默认值：EASE_IN_OUT。int32_t index状态索引值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyframeAnimateOption_RegisterOnEventCallback()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnEventCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*event)(void* userData), int32_t index)
```

**描述：**

设置关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。void* userData用户定义对象指针。void (*event)(void* userData)闭包函数。int32_t index状态索引值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_KeyframeAnimateOption_GetDelay()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_GetDelay(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧整体延时时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。

**返回：**

类型说明int32_t整体延时时间，单位为ms（毫秒）。

#### OH_ArkUI_KeyframeAnimateOption_GetIterations()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_GetIterations(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧动画播放次数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。

**返回：**

类型说明int32_t动画播放次数。

#### OH_ArkUI_KeyframeAnimateOption_GetExpectedFrameRate()

```ets
ArkUI_ExpectedFrameRateRange* OH_ArkUI_KeyframeAnimateOption_GetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧动画参数的期望帧率。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。

**返回：**

类型说明[ArkUI_ExpectedFrameRateRange](../../topics/components/ArkUI_ExpectedFrameRateRange.md)*关键帧动画参数的期望帧率。

#### OH_ArkUI_KeyframeAnimateOption_GetDuration()

```ets
int32_t OH_ArkUI_KeyframeAnimateOption_GetDuration(ArkUI_KeyframeAnimateOption* option, int32_t index)
```

**描述：**

获取关键帧动画某段状态持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。int32_t index状态索引值。

**返回：**

类型说明int32_t持续时间，单位为ms（毫秒）。

#### OH_ArkUI_KeyframeAnimateOption_GetCurve()

```ets
ArkUI_CurveHandle OH_ArkUI_KeyframeAnimateOption_GetCurve(ArkUI_KeyframeAnimateOption* option, int32_t index)
```

**描述：**

获取关键帧动画某段状态动画曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_KeyframeAnimateOption](../../topics/components/ArkUI_KeyframeAnimateOption.md)* option关键帧动画参数。int32_t index状态索引值。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)动画曲线。函数参数异常时返回NULL。

#### OH_ArkUI_AnimatorOption_Create()

```ets
ArkUI_AnimatorOption* OH_ArkUI_AnimatorOption_Create(int32_t keyframeSize)
```

**描述：**

创建animator动画对象参数。

keyframeSize大于0时，动画插值起点默认是0，动画插值终点模式值是1。不支持设置。

**起始版本：** 12

**参数：**

参数项描述int32_t keyframeSize关键帧个数。

**返回：**

类型说明ArkUI_AnimatorOption*animator动画对象参数指针。size小于0时返回NULL。

#### OH_ArkUI_AnimatorOption_Dispose()

```ets
void OH_ArkUI_AnimatorOption_Dispose(ArkUI_AnimatorOption* option)
```

**描述：**

销毁animator动画对象参数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。

#### OH_ArkUI_AnimatorOption_SetDuration()

```ets
int32_t OH_ArkUI_AnimatorOption_SetDuration(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画播放的时长，单位毫秒。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。int32_t value播放的时长，单位毫秒。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetDelay()

```ets
int32_t OH_ArkUI_AnimatorOption_SetDelay(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画延时播放时长，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。int32_t value延时播放时长，单位为ms（毫秒）。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetIterations()

```ets
int32_t OH_ArkUI_AnimatorOption_SetIterations(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画播放次数。设置为0时不播放，设置为-1时无限次播放。

设置为除-1外其他负数视为无效取值，无效取值动画默认播放1次。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。int32_t value动画播放次数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetFill()

```ets
int32_t OH_ArkUI_AnimatorOption_SetFill(ArkUI_AnimatorOption* option, ArkUI_AnimationFillMode value)
```

**描述：**

设置animator动画执行后是否恢复到初始状态。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。[ArkUI_AnimationFillMode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationfillmode) value动画执行后是否恢复到初始状态。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetDirection()

```ets
int32_t OH_ArkUI_AnimatorOption_SetDirection(ArkUI_AnimatorOption* option, ArkUI_AnimationDirection value)
```

**描述：**

设置animator动画播放方向。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。[ArkUI_AnimationDirection](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationdirection) value动画播放方向。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetCurve()

```ets
int32_t OH_ArkUI_AnimatorOption_SetCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value)
```

**描述：**

设置animator动画插值曲线。

不支持springCurve，springMotion，responsiveSpringMotion，interpolatingSpring，customCurve动画曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md) value动画插值曲线。默认值：ARKUI_CURVE_LINEAR。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetBegin()

```ets
int32_t OH_ArkUI_AnimatorOption_SetBegin(ArkUI_AnimatorOption* option, float value)
```

**描述：**

设置animator动画插值起点。

当Animator动画为keyframe动画时，此方法不生效。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。float value动画插值起点。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetEnd()

```ets
int32_t OH_ArkUI_AnimatorOption_SetEnd(ArkUI_AnimatorOption* option, float value)
```

**描述：**

设置animator动画插值终点。

当Animator动画为keyframe动画时，此方法不生效。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。float value动画插值终点。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetExpectedFrameRateRange()

```ets
int32_t OH_ArkUI_AnimatorOption_SetExpectedFrameRateRange(ArkUI_AnimatorOption* option, ArkUI_ExpectedFrameRateRange* value)
```

**描述：**

设置animator动画期望的帧率范围。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。[ArkUI_ExpectedFrameRateRange](../../topics/components/ArkUI_ExpectedFrameRateRange.md)* value期望的帧率范围对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetKeyframe()

```ets
int32_t OH_ArkUI_AnimatorOption_SetKeyframe(ArkUI_AnimatorOption* option, float time, float value, int32_t index)
```

**描述：**

设置animator动画关键帧参数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。float time关键帧时间。取值范围：[0, 1], 必须是递增。float value关键帧数值。int32_t index关键帧的索引值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_SetKeyframeCurve()

```ets
int32_t OH_ArkUI_AnimatorOption_SetKeyframeCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value, int32_t index)
```

**描述：**

设置animator动画关键帧曲线类型。

不支持springCurve，springMotion，responsiveSpringMotion，interpolatingSpring，customCurve动画曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md) value动画插值曲线。int32_t index关键帧的索引值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_GetDuration()

```ets
int32_t OH_ArkUI_AnimatorOption_GetDuration(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放的时长。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明int32_t动画播放的时长，单位毫秒。

#### OH_ArkUI_AnimatorOption_GetDelay()

```ets
int32_t OH_ArkUI_AnimatorOption_GetDelay(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画延时播放时长。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明int32_t动画延时播放时长，单位毫秒。

#### OH_ArkUI_AnimatorOption_GetIterations()

```ets
int32_t OH_ArkUI_AnimatorOption_GetIterations(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放次数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画动画参数。

**返回：**

类型说明int32_t动画播放次数。

#### OH_ArkUI_AnimatorOption_GetFill()

```ets
ArkUI_AnimationFillMode OH_ArkUI_AnimatorOption_GetFill(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画执行后是否恢复到初始状态。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明[ArkUI_AnimationFillMode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationfillmode)执行后是否恢复到初始状态。

#### OH_ArkUI_AnimatorOption_GetDirection()

```ets
ArkUI_AnimationDirection OH_ArkUI_AnimatorOption_GetDirection(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放方向。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明[ArkUI_AnimationDirection](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationdirection)动画播放方向。

#### OH_ArkUI_AnimatorOption_GetCurve()

```ets
ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetCurve(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)动画插值曲线。

#### OH_ArkUI_AnimatorOption_GetBegin()

```ets
float OH_ArkUI_AnimatorOption_GetBegin(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值起点。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明float动画插值起点。

#### OH_ArkUI_AnimatorOption_GetEnd()

```ets
float OH_ArkUI_AnimatorOption_GetEnd(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值终点。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明float动画插值终点。

#### OH_ArkUI_AnimatorOption_GetExpectedFrameRateRange()

```ets
ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimatorOption_GetExpectedFrameRateRange(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画期望的帧率范围。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明[ArkUI_ExpectedFrameRateRange](../../topics/components/ArkUI_ExpectedFrameRateRange.md)*期望的帧率范围对象指针。函数参数异常时返回NULL。

#### OH_ArkUI_AnimatorOption_GetKeyframeTime()

```ets
float OH_ArkUI_AnimatorOption_GetKeyframeTime(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。int32_t index关键帧的索引值。

**返回：**

类型说明float关键帧时间，单位为ms（毫秒）。

#### OH_ArkUI_AnimatorOption_GetKeyframeValue()

```ets
float OH_ArkUI_AnimatorOption_GetKeyframeValue(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧数值。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。int32_t index关键帧的索引值。

**返回：**

类型说明float关键帧数值。

#### OH_ArkUI_AnimatorOption_GetKeyframeCurve()

```ets
ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetKeyframeCurve(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧动画插值曲线。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画对象参数。int32_t index关键帧的索引值。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)动画插值曲线。函数参数异常时返回NULL。

#### OH_ArkUI_AnimatorEvent_GetUserData()

```ets
void* OH_ArkUI_AnimatorEvent_GetUserData(ArkUI_AnimatorEvent* event)
```

**描述：**

获取动画事件对象中的用户自定义对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorEvent](../../topics/media/ArkUI_AnimatorEvent.md)* event动画事件对象。

**返回：**

类型说明void*用户自定义对象。

#### OH_ArkUI_AnimatorOnFrameEvent_GetUserData()

```ets
void* OH_ArkUI_AnimatorOnFrameEvent_GetUserData(ArkUI_AnimatorOnFrameEvent* event)
```

**描述：**

获取动画事件对象中的用户自定义对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOnFrameEvent](../../topics/components/ArkUI_AnimatorOnFrameEvent.md)* event动画事件对象。

**返回：**

类型说明void*用户自定义对象。

#### OH_ArkUI_AnimatorOnFrameEvent_GetValue()

```ets
float OH_ArkUI_AnimatorOnFrameEvent_GetValue(ArkUI_AnimatorOnFrameEvent* event)
```

**描述：**

获取动画事件对象中的当前进度。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOnFrameEvent](../../topics/components/ArkUI_AnimatorOnFrameEvent.md)* event动画事件对象。

**返回：**

类型说明float动画进度。

#### OH_ArkUI_AnimatorOption_RegisterOnFrameCallback()

```ets
int32_t OH_ArkUI_AnimatorOption_RegisterOnFrameCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorOnFrameEvent* event))
```

**描述：**

设置animator动画接收到帧时回调。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。void* userData用户自定义参数。void (*callback)(ArkUI_AnimatorOnFrameEvent* event)

回调函数。

- event：回调函数的入参，动画事件对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_RegisterOnFinishCallback()

```ets
int32_t OH_ArkUI_AnimatorOption_RegisterOnFinishCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画完成时回调。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。void* userData用户自定义参数。void (*callback)(ArkUI_AnimatorEvent* event)

回调函数。

- event：回调函数的入参，动画事件对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_RegisterOnCancelCallback()

```ets
int32_t OH_ArkUI_AnimatorOption_RegisterOnCancelCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画被取消时回调。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。void* userData用户自定义参数。void (*callback)(ArkUI_AnimatorEvent* event)

回调函数。

- event：回调函数的入参，动画事件对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AnimatorOption_RegisterOnRepeatCallback()

```ets
int32_t OH_ArkUI_AnimatorOption_RegisterOnRepeatCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画重复时回调。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。void* userData用户自定义参数。void (*callback)(ArkUI_AnimatorEvent* event)

回调函数。

- event：回调函数的入参，动画事件对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_Animator_ResetAnimatorOption()

```ets
int32_t OH_ArkUI_Animator_ResetAnimatorOption(ArkUI_AnimatorHandle animatorHandle, ArkUI_AnimatorOption* option)
```

**描述：**

更新animator动画。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorHandle](../../topics/media/ArkUI_Animator_.md) animatorHandleanimator动画对象。[ArkUI_AnimatorOption](../../topics/media/ArkUI_AnimatorOption.md)* optionanimator动画参数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_Animator_Play()

```ets
int32_t OH_ArkUI_Animator_Play(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

启动animator动画。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorHandle](../../topics/media/ArkUI_Animator_.md) animatorHandleanimator动画对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_Animator_Finish()

```ets
int32_t OH_ArkUI_Animator_Finish(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

结束animator动画。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorHandle](../../topics/media/ArkUI_Animator_.md) animatorHandleanimator动画对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_Animator_Pause()

```ets
int32_t OH_ArkUI_Animator_Pause(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

暂停animator动画。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorHandle](../../topics/media/ArkUI_Animator_.md) animatorHandleanimator动画对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_Animator_Cancel()

```ets
int32_t OH_ArkUI_Animator_Cancel(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

取消animator动画。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorHandle](../../topics/media/ArkUI_Animator_.md) animatorHandleanimator动画对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_Animator_Reverse()

```ets
int32_t OH_ArkUI_Animator_Reverse(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

以相反的顺序播放animator动画。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimatorHandle](../../topics/media/ArkUI_Animator_.md) animatorHandleanimator动画对象。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_Curve_CreateCurveByType()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCurveByType(ArkUI_AnimationCurve curve)
```

**描述：**

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_AnimationCurve](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_animationcurve) curve曲线类型。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_CreateStepsCurve()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateStepsCurve(int32_t count, bool end)
```

**描述：**

构造阶梯曲线对象。

**起始版本：** 12

**参数：**

参数项描述int32_t count阶梯的数量，需要为正整数，取值范围：[1, +∞)。bool end在每个间隔的起点或是终点发生阶跃变化。true：在终点发生阶跃变化。false：在起点发生阶跃变化。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_CreateCubicBezierCurve()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)
```

**描述：**

构造三阶贝塞尔曲线对象。

**起始版本：** 12

**参数：**

参数项描述float x1确定贝塞尔曲线第一点横坐标，取值范围：[0, 1]。设置的值小于0时，按0处理；设置的值大于1时，按1处理。float y1确定贝塞尔曲线第一点纵坐标。float x2确定贝塞尔曲线第二点横坐标，取值范围：[0, 1]。设置的值小于0时，按0处理；设置的值大于1时，按1处理。float y2确定贝塞尔曲线第二点纵坐标。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_CreateSpringCurve()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)
```

**描述：**

构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受animation、animateTo中的duration参数控制。

**起始版本：** 12

**参数：**

参数项描述float velocity初始速度。是由外部因素对弹性动效产生的影响参数，其目的是保证对象从之前的运动状态平滑的过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。float mass质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。float stiffness刚度。是物体抵抗施加的力而形变的程度。在弹性系统中，刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度就越快。float damping阻尼。用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_CreateSpringMotion()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)
```

**描述：**

构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换掉前一个动画，并继承之前的速度。

动画时间由曲线参数决定，不受animation、animateTo中的duration参数控制。

**起始版本：** 12

**参数：**

参数项描述float response弹簧自然振动周期，决定弹簧复位的速度。float dampingFraction阻尼系数。大于0小于1的值为欠阻尼，运动过程中会超出目标值；等于1为临界阻尼；大于1为过阻尼，运动过程中逐渐趋于目标值。float overlapDuration弹性动画衔接时长。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_CreateResponsiveSpringMotion()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)
```

**描述：**

构造弹性跟手动画曲线对象，是springMotion的一种特例，仅默认参数不同，可与springMotion混合使用。

动画时间由曲线参数决定，不受animation、animateTo中的duration参数控制。

**起始版本：** 12

**参数：**

参数项描述float response弹簧自然振动周期，决定弹簧复位的速度。float dampingFraction阻尼系数。大于0小于1的值为欠阻尼，运动过程中会超出目标值；等于1为临界阻尼；大于1为过阻尼，运动过程中逐渐趋于目标值。float overlapDuration弹性动画衔接时长。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_CreateInterpolatingSpring()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)
```

**描述：**

构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。

动画时间由曲线参数决定，不受animation、animateTo中的duration参数控制。

**起始版本：** 12

**参数：**

参数项描述float velocity初始速度。外部因素对弹性动效产生的影响参数，目的是保证对象从之前的运动状态平滑地过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。float mass质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。float stiffness刚度。表示物体抵抗施加的力而形变的程度。刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度越快。float damping阻尼。用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_CreateCustomCurve()

```ets
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCustomCurve(void* userData, float (*interpolate)(float fraction, void* userdata))
```

**描述：**

构造自定义曲线对象。

**起始版本：** 12

**参数：**

参数项描述void* userData用户自定义数据。float (*interpolate)(float fraction, void* userdata)用户自定义的插值回调函数。fraction为动画开始时的插值输入x值。取值范围：[0,1]返回值为曲线的y值。取值范围：[0,1]。fraction等于0时，返回值为0对应动画起点，返回不为0，动画在起点处有跳变效果。fraction等于1时，返回值为1对应动画终点，返回值不为1将导致动画的终值不是状态变量的值，出现大于或者小于状态变量值，再跳变到状态变量值的效果。

**返回：**

类型说明[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md)曲线的插值对象指针。如果参数异常返回NULL。

#### OH_ArkUI_Curve_DisposeCurve()

```ets
void OH_ArkUI_Curve_DisposeCurve(ArkUI_CurveHandle curveHandle)
```

**描述：**

销毁自定义曲线对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_CurveHandle](../../topics/media/ArkUI_Curve_.md) curveHandle曲线的插值对象指针。

#### OH_ArkUI_CreateOpacityTransitionEffect()

```ets
ArkUI_TransitionEffect* OH_ArkUI_CreateOpacityTransitionEffect(float opacity)
```

**描述：**

创建组件转场时的透明度效果对象。

**起始版本：** 12

**参数：**

参数项描述float opacity透明度，取值范围为[0, 1]。默认值为1。设置小于0的非法值按0处理，大于1的非法值按1处理，1表示不透明，0表示完全透明。

**返回：**

类型说明[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)*组件转场时的透明度效果对象。

#### OH_ArkUI_CreateTranslationTransitionEffect()

```ets
ArkUI_TransitionEffect* OH_ArkUI_CreateTranslationTransitionEffect(ArkUI_TranslationOptions* translate)
```

**描述：**

创建组件转场时的平移效果对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_TranslationOptions](../../topics/media/ArkUI_TranslationOptions.md)* translate组件转场时的平移参数对象。

**返回：**

类型说明[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)*组件转场时的平移效果对象。如果参数异常返回NULL。

#### OH_ArkUI_CreateScaleTransitionEffect()

```ets
ArkUI_TransitionEffect* OH_ArkUI_CreateScaleTransitionEffect(ArkUI_ScaleOptions* scale)
```

**描述：**

创建组件转场时的缩放效果对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_ScaleOptions](../../topics/media/ArkUI_ScaleOptions.md)* scale组件转场时的缩放参数对象。

**返回：**

类型说明[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)*组件转场时的缩放效果对象。如果参数异常返回NULL。

#### OH_ArkUI_CreateRotationTransitionEffect()

```ets
ArkUI_TransitionEffect* OH_ArkUI_CreateRotationTransitionEffect(ArkUI_RotationOptions* rotate)
```

**描述：**

创建组件转场时的旋转效果对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_RotationOptions](../../topics/media/ArkUI_RotationOptions.md)* rotate组件转场时的旋转参数对象。

**返回：**

类型说明[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)*组件转场时的旋转效果对象。如果参数异常返回NULL。

#### OH_ArkUI_CreateMovementTransitionEffect()

```ets
ArkUI_TransitionEffect* OH_ArkUI_CreateMovementTransitionEffect(ArkUI_TransitionEdge edge)
```

**描述：**

创建组件平移效果对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_TransitionEdge](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_transitionedge) edge平移类型。

**返回：**

类型说明[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)*组件转场时的平移效果对象。如果参数异常返回NULL。

#### OH_ArkUI_CreateAsymmetricTransitionEffect()

```ets
ArkUI_TransitionEffect* OH_ArkUI_CreateAsymmetricTransitionEffect(ArkUI_TransitionEffect* appear, ArkUI_TransitionEffect* disappear)
```

**描述：**

创建非对称的转场效果对象。

如不通过asymmetric函数构造TransitionEffect，则表明该效果在组件出现和消失时均生效。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)* appear出现的转场效果。[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)* disappear消失的转场效果。

**返回：**

类型说明[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)*非对称的转场效果对象。如果参数异常返回NULL。

#### OH_ArkUI_TransitionEffect_Dispose()

```ets
void OH_ArkUI_TransitionEffect_Dispose(ArkUI_TransitionEffect* effect)
```

**描述：**

销毁转场效果对象。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)* effect转场效果对象。

#### OH_ArkUI_TransitionEffect_Combine()

```ets
int32_t OH_ArkUI_TransitionEffect_Combine(ArkUI_TransitionEffect* firstEffect, ArkUI_TransitionEffect* secondEffect)
```

**描述：**

设置转场效果链式组合，以形成包含多种转场效果的TransitionEffect。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)* firstEffect转场效果。[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)* secondEffect需要链式转场效果。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_TransitionEffect_SetAnimation()

```ets
int32_t OH_ArkUI_TransitionEffect_SetAnimation(ArkUI_TransitionEffect* effect, ArkUI_AnimateOption* animation)
```

**描述：**

设置转场效果动画参数。

如果通过combine进行转场效果的组合，前一转场效果的动画参数也可用于后一转场效果。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_TransitionEffect](../../topics/media/ArkUI_TransitionEffect.md)* effect转场效果。[ArkUI_AnimateOption](../../topics/media/ArkUI_AnimateOption.md)* animation属性显示动画效果相关参数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。