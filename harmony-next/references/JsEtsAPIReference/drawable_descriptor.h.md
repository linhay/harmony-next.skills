# drawable_descriptor.h

#### 概述

提供NativeDrawableDescriptor接口的类型定义。

**引用文件：** <arkui/drawable_descriptor.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](ArkUI_NativeModule.md)

**相关示例：**[DrawableDescriptorSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/DrawableDescriptorSample)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)ArkUI_DrawableDescriptor定义DrawableDescriptor对象。[OH_PixelmapNative*](OH_PixelmapNative_.md)OH_PixelmapNativeHandle定义OH_PixelmapNative对象指针类型。[ArkUI_Node*](ArkUI_Node_.md)ArkUI_NodeHandle定义ArkUI native组件实例对象指针定义。[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)ArkUI_DrawableDescriptor_AnimationController定义DrawableDescriptor动图控制器对象。

#### 枚举

名称typedef关键字描述[DrawableDescriptor_AnimationStatus](#ZH-CN_TOPIC_0000002497445096__drawabledescriptor_animationstatus)DrawableDescriptor_AnimationStatus定义DrawableDescriptor动图的播放状态。

#### 函数

名称描述[ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromPixelMap(OH_PixelmapNativeHandle pixelMap)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_createfrompixelmap)使用PixelMap创建DrawableDescriptor对象。[ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromAnimatedPixelMap(OH_PixelmapNativeHandle* array, int32_t size)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_createfromanimatedpixelmap)使用PixelMap图片数组创建DrawableDescriptor对象。[void OH_ArkUI_DrawableDescriptor_Dispose(ArkUI_DrawableDescriptor* drawableDescriptor)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_dispose)销毁DrawableDescriptor对象指针。[OH_PixelmapNativeHandle OH_ArkUI_DrawableDescriptor_GetStaticPixelMap(ArkUI_DrawableDescriptor* drawableDescriptor)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getstaticpixelmap)获取PixelMap图片对象指针。[OH_PixelmapNativeHandle* OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArray(ArkUI_DrawableDescriptor* drawableDescriptor)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getanimatedpixelmaparray)获取用于播放动画的PixelMap图片数组数据。[int32_t OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArraySize(ArkUI_DrawableDescriptor* drawableDescriptor)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getanimatedpixelmaparraysize)获取用于播放动画的PixelMap图片数组数据。[void OH_ArkUI_DrawableDescriptor_SetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t duration)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_setanimationduration)设置PixelMap图片数组播放总时长。[int32_t OH_ArkUI_DrawableDescriptor_GetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getanimationduration)获取PixelMap图片数组播放总时长。[void OH_ArkUI_DrawableDescriptor_SetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t iteration)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_setanimationiteration)设置PixelMap图片数组播放次数。[int32_t OH_ArkUI_DrawableDescriptor_GetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getanimationiteration)获取PixelMap图片数组播放次数。[int32_t OH_ArkUI_DrawableDescriptor_SetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t size)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_setanimationframedurations)设置动图中的单帧播放时间。[int32_t OH_ArkUI_DrawableDescriptor_GetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t* size)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getanimationframedurations)获取动图中的单帧播放时间。[int32_t OH_ArkUI_DrawableDescriptor_SetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t autoPlay)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_setanimationautoplay)设置动图是否自动播放。[int32_t OH_ArkUI_DrawableDescriptor_GetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* autoPlay)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getanimationautoplay)获取动图是否自动播放。[int32_t OH_ArkUI_DrawableDescriptor_CreateAnimationController(ArkUI_DrawableDescriptor* drawableDescriptor, ArkUI_NodeHandle node, ArkUI_DrawableDescriptor_AnimationController** controller)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_createanimationcontroller)创建动图控制器。[void OH_ArkUI_DrawableDescriptor_DisposeAnimationController( ArkUI_DrawableDescriptor_AnimationController* controller)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_disposeanimationcontroller)销毁动图控制器。[int32_t OH_ArkUI_DrawableDescriptor_StartAnimation(ArkUI_DrawableDescriptor_AnimationController* controller)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_startanimation)从首帧开始播放。[int32_t OH_ArkUI_DrawableDescriptor_StopAnimation(ArkUI_DrawableDescriptor_AnimationController* controller)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_stopanimation)停止动图播放并回到首帧。[int32_t OH_ArkUI_DrawableDescriptor_ResumeAnimation(ArkUI_DrawableDescriptor_AnimationController* controller)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_resumeanimation)从当前帧恢复动图播放。[int32_t OH_ArkUI_DrawableDescriptor_PauseAnimation(ArkUI_DrawableDescriptor_AnimationController* controller)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_pauseanimation)暂停动图的播放，保持在当前帧。[int32_t OH_ArkUI_DrawableDescriptor_GetAnimationStatus(ArkUI_DrawableDescriptor_AnimationController* controller, DrawableDescriptor_AnimationStatus* status)](#ZH-CN_TOPIC_0000002497445096__oh_arkui_drawabledescriptor_getanimationstatus)获取动图的播放状态。

#### 枚举类型说明

#### DrawableDescriptor_AnimationStatus

```ets
enum DrawableDescriptor_AnimationStatus
```

**描述：**

定义DrawableDescriptor动图的播放状态。

**起始版本：** 22

枚举项描述DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_INITIAL = 0动画初始状态。DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_RUNNING = 1动画处于播放状态。DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_PAUSED = 2动画处于暂停状态。DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_STOPPED = 3动画处于停止状态。

#### 函数说明

#### OH_ArkUI_DrawableDescriptor_CreateFromPixelMap()

```ets
ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromPixelMap(OH_PixelmapNativeHandle pixelMap)
```

**描述：**

使用PixelMap创建DrawableDescriptor对象。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNativeHandle](OH_PixelmapNative_.md) pixelMapPixelMap对象指针。

**返回：**

类型说明[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)*返回DrawableDescriptor对象指针。

#### OH_ArkUI_DrawableDescriptor_CreateFromAnimatedPixelMap()

```ets
ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromAnimatedPixelMap(OH_PixelmapNativeHandle* array, int32_t size)
```

**描述：**

使用PixelMap图片数组创建DrawableDescriptor对象。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNativeHandle](OH_PixelmapNative_.md)* arrayPixelMap图片数组对象指针。int32_t sizePixelMap图片数组大小。

**返回：**

类型说明[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)*返回DrawableDescriptor对象指针。

#### OH_ArkUI_DrawableDescriptor_Dispose()

```ets
void OH_ArkUI_DrawableDescriptor_Dispose(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

销毁DrawableDescriptor对象指针。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。

#### OH_ArkUI_DrawableDescriptor_GetStaticPixelMap()

```ets
OH_PixelmapNativeHandle OH_ArkUI_DrawableDescriptor_GetStaticPixelMap(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片对象指针。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。

**返回：**

类型说明[OH_PixelmapNativeHandle](OH_PixelmapNative_.md)PixelMap对象指针。

#### OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArray()

```ets
OH_PixelmapNativeHandle* OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArray(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取用于播放动画的PixelMap图片数组数据。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。

**返回：**

类型说明[OH_PixelmapNativeHandle](OH_PixelmapNative_.md)*PixelMap图片数组指针。

#### OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArraySize()

```ets
int32_t OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArraySize(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取用于播放动画的PixelMap图片数组数据。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。

**返回：**

类型说明int32_tPixelMap图片数组大小。

#### OH_ArkUI_DrawableDescriptor_SetAnimationDuration()

```ets
void OH_ArkUI_DrawableDescriptor_SetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t duration)
```

**描述：**

设置PixelMap图片数组播放总时长。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。int32_t duration播放总时长，单位毫秒。

#### OH_ArkUI_DrawableDescriptor_GetAnimationDuration()

```ets
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片数组播放总时长。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。

**返回：**

类型说明int32_t播放总时长，单位毫秒。

#### OH_ArkUI_DrawableDescriptor_SetAnimationIteration()

```ets
void OH_ArkUI_DrawableDescriptor_SetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t iteration)
```

**描述：**

设置PixelMap图片数组播放次数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。int32_t iteration播放次数。

#### OH_ArkUI_DrawableDescriptor_GetAnimationIteration()

```ets
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片数组播放次数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。

**返回：**

类型说明int32_t播放次数。

#### OH_ArkUI_DrawableDescriptor_SetAnimationFrameDurations()

```ets
int32_t OH_ArkUI_DrawableDescriptor_SetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t size)
```

**描述：**

设置动图中的单帧播放时间。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。uint32_t* durations

动图中的单帧播放时间数组，单位毫秒。

不设置则按照总时间播放。设置的优先级高于duration，即同时设置了duration和frameDurations时，duration不生效。

数组大小必须与PixelMap图片数组大小相同。

每帧播放时间取值范围：[0, +∞)。

size_t size数组大小。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_GetAnimationFrameDurations()

```ets
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t* size)
```

**描述：**

获取动图中的单帧播放时间。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。uint32_t* durations动图中的单帧播放时间数组。size_t* size数组大小。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_SetAnimationAutoPlay()

```ets
int32_t OH_ArkUI_DrawableDescriptor_SetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t autoPlay)
```

**描述：**

设置动图是否自动播放。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。uint32_t autoPlay

是否自动播放。

1表示自动播放，0表示不自动播放。

默认值为1。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_GetAnimationAutoPlay()

```ets
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* autoPlay)
```

**描述：**

获取动图是否自动播放。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。uint32_t* autoPlay是否自动播放。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_CreateAnimationController()

```ets
int32_t OH_ArkUI_DrawableDescriptor_CreateAnimationController(ArkUI_DrawableDescriptor* drawableDescriptor, ArkUI_NodeHandle node, ArkUI_DrawableDescriptor_AnimationController** controller)
```

**描述：**

创建动图控制器。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md)* drawableDescriptorDrawableDescriptor对象指针。[ArkUI_NodeHandle](ArkUI_Node_.md) node组件节点指针。[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)** controllerDrawableDescriptor动图控制器对象指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_DisposeAnimationController()

```ets
void OH_ArkUI_DrawableDescriptor_DisposeAnimationController(ArkUI_DrawableDescriptor_AnimationController* controller)
```

**描述：**

销毁动图控制器。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)* controllerDrawableDescriptor动图控制器对象指针。

#### OH_ArkUI_DrawableDescriptor_StartAnimation()

```ets
int32_t OH_ArkUI_DrawableDescriptor_StartAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

从首帧开始播放。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)* controllerDrawableDescriptor动图控制器对象指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_StopAnimation()

```ets
int32_t OH_ArkUI_DrawableDescriptor_StopAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

停止动图播放并回到首帧。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)* controllerDrawableDescriptor动图控制器对象指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_ResumeAnimation()

```ets
int32_t OH_ArkUI_DrawableDescriptor_ResumeAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

从当前帧恢复动图播放。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)* controllerDrawableDescriptor动图控制器对象指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_PauseAnimation()

```ets
int32_t OH_ArkUI_DrawableDescriptor_PauseAnimation(ArkUI_DrawableDescriptor_AnimationController* controller);
```

**描述：**

暂停动图的播放，保持在当前帧。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)* controllerDrawableDescriptor动图控制器对象指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。

#### OH_ArkUI_DrawableDescriptor_GetAnimationStatus()

```ets
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationStatus(ArkUI_DrawableDescriptor_AnimationController* controller, DrawableDescriptor_AnimationStatus* status);
```

**描述：**

获取动图的播放状态。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_DrawableDescriptor_AnimationController](ArkUI_DrawableDescriptor_AnimationController.md)* controllerDrawableDescriptor动图控制器对象指针。[DrawableDescriptor_AnimationStatus](#ZH-CN_TOPIC_0000002497445096__drawabledescriptor_animationstatus)* statusDrawableDescriptor动图的播放状态。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_INVALID_PARAM](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 输入参数错误。