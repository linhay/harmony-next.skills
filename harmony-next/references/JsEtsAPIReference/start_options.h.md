# start_options.h

#### 概述

提供应用启动参数数据结构[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md)以及设置和获取相关函数。

**引用文件：** <AbilityKit/ability_runtime/start_options.h>

**库：** libability_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 17

**相关模块：**[AbilityRuntime](AbilityRuntime.md)

#### 汇总

#### 结构体

名称typedef关键字描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md)AbilityRuntime_StartOptionsStartOptions数据结构。

#### 函数

名称描述[AbilityRuntime_StartOptions* OH_AbilityRuntime_CreateStartOptions(void)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_createstartoptions)创建AbilityRuntime_StartOptions对象。[AbilityRuntime_ErrorCode OH_AbilityRuntime_DestroyStartOptions(AbilityRuntime_StartOptions **startOptions)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_destroystartoptions)销毁AbilityRuntime_StartOptions对象。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode windowMode)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionswindowmode)设置启动Ability时的窗口模式。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode &windowMode)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionswindowmode)获取启动Ability时的窗口模式。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t displayId)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsdisplayid)设置启动Ability时窗口所在的屏幕ID。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t &displayId)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsdisplayid)获取启动Ability时窗口所在的屏幕ID。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool withAnimation)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionswithanimation)设置启动Ability时是否具有动画效果。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool &withAnimation)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionswithanimation)获取启动Ability时是否具有动画效果。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t windowLeft)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionswindowleft)设置启动Ability时的窗口左侧位置，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t &windowLeft)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionswindowleft)获取启动Ability时的窗口左侧位置，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t windowTop)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionswindowtop)设置启动Ability时的窗口顶部位置，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t &windowTop)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionswindowtop)获取启动Ability时的窗口顶部位置，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t windowHeight)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionswindowheight)设置启动Ability时的窗口高度，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t &windowHeight)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionswindowheight)获取启动Ability时的窗口高度，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t windowWidth)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionswindowwidth)设置启动Ability时的窗口宽度，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t &windowWidth)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionswindowwidth)获取启动Ability时的窗口宽度，单位为px。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility startVisibility)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsstartvisibility)设置启动Ability时窗口和dock栏图标的显示模式。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility &startVisibility)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsstartvisibility)获取启动Ability时窗口和dock栏图标的显示模式。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative *startWindowIcon)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsstartwindowicon)设置启动Ability时的窗口启动图标。图片数据大小限制为600M。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative **startWindowIcon)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsstartwindowicon)获取启动Ability时的窗口启动图标。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, const char *startWindowBackgroundColor)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsstartwindowbackgroundcolor)设置启动Ability时的窗口背景颜色。如果未设置该字段，则默认采用module.json5配置文件中abilities标签的startWindowBackground字段的配置。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, char **startWindowBackgroundColor, size_t &size)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsstartwindowbackgroundcolor)获取启动Ability时的窗口背景颜色。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode *supportedWindowModes,size_t size)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionssupportedwindowmodes)设置启动Ability时的组件所支持的窗口模式。如果未配置该字段，则默认采用该UIAbility对应的module.json5配置文件中abilities标签的supportWindowMode字段取值。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode **supportedWindowModes,size_t &size)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionssupportedwindowmodes)获取启动Ability时的组件所支持的窗口模式。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t minWindowWidth)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsminwindowwidth)设置启动Ability时的窗口最小宽度，单位为vp。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowWidth)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsminwindowwidth)获取启动Ability时的窗口最小宽度，单位为vp。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowWidth)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsmaxwindowwidth)设置启动Ability时的窗口最大宽度，单位为vp。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowWidth)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsmaxwindowwidth)获取启动Ability时的窗口最大宽度，单位为vp。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t minWindowHeight)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsminwindowheight)设置启动Ability时的窗口最小高度，单位为vp。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowHeight)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsminwindowheight)获取启动Ability时的窗口最小高度，单位为vp。[AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowHeight)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_setstartoptionsmaxwindowheight)设置启动Ability时的窗口最大高度，单位为vp。[AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowHeight)](#ZH-CN_TOPIC_0000002497444682__oh_abilityruntime_getstartoptionsmaxwindowheight)获取启动Ability时的窗口最大高度，单位为vp。

#### 函数说明

#### OH_AbilityRuntime_CreateStartOptions()

```ets
AbilityRuntime_StartOptions* OH_AbilityRuntime_CreateStartOptions(void)
```

**描述**

创建[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md)对象。

**起始版本：** 17

**返回：**

类型说明[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md)*返回指针类型AbilityRuntime_StartOptions对象。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void createStartOptionsTest()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_DestroyStartOptions()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_DestroyStartOptions(AbilityRuntime_StartOptions **startOptions)
```

**描述**

销毁[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md)对象。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) **startOptions需要销毁的AbilityRuntime_StartOptions对象。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void destroyStartOptionsTest()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsWindowMode()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode windowMode)
```

**描述**

设置启动Ability时的窗口模式。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。[AbilityRuntime_WindowMode](context_constant.h.md#ZH-CN_TOPIC_0000002529284651__abilityruntime_windowmode) windowMode启动Ability时的窗口模式。取值范围参见AbilityRuntime_WindowMode。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空或者WindowMode无效。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowMode(options,
        ABILITY_RUNTIME_WINDOW_MODE_FULL_SCREEN);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsWindowMode()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode &windowMode)
```

**描述**

获取启动Ability时的窗口模式。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。[AbilityRuntime_WindowMode](context_constant.h.md#ZH-CN_TOPIC_0000002529284651__abilityruntime_windowmode) windowMode启动Ability时的窗口模式。取值范围参见AbilityRuntime_WindowMode。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_WindowMode windowMode = ABILITY_RUNTIME_WINDOW_MODE_UNDEFINED;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowMode(options, windowMode);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsDisplayId()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t displayId)
```

**描述**

设置启动Ability时窗口所在的屏幕ID。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t displayId启动Ability时窗口所在的屏幕ID。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsDisplayId(options, 1);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsDisplayId()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t &displayId)
```

**描述**

获取启动Ability时窗口所在的屏幕ID。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &displayId启动Ability时窗口所在的屏幕ID。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t displayId = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsDisplayId(options, displayId);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsWithAnimation()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool withAnimation)
```

**描述**

设置启动Ability时是否具有动画效果。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。bool withAnimation

启动Ability时是否具有动画效果。

true表示启动Ability时具有动画效果；false表示启动Ability时不具有动画效果。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWithAnimation(options, true);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsWithAnimation()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool &withAnimation)
```

**描述**

获取启动Ability时是否具有动画效果。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。bool &withAnimation

启动Ability时是否具有动画效果。

true表示启动Ability时具有动画效果；false表示启动Ability时不具有动画效果。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    bool withAnimation = false;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWithAnimation(options, withAnimation);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsWindowLeft()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t windowLeft)
```

**描述**

设置启动Ability时的窗口左侧位置，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t windowLeft启动Ability时的窗口左侧位置，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowLeft(options, 200);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsWindowLeft()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t &windowLeft)
```

**描述**

获取启动Ability时的窗口左侧位置，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &windowLeft启动Ability时的窗口左侧位置，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowLeft = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowLeft(options, windowLeft);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsWindowTop()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t windowTop)
```

**描述**

设置启动Ability时的窗口顶部位置，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t windowTop启动Ability时的窗口顶部位置，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowTop(options, 500);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsWindowTop()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t &windowTop)
```

**描述**

获取启动Ability时的窗口顶部位置，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &windowTop启动Ability时的窗口顶部位置，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowTop = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowTop(options, windowTop);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsWindowHeight()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t windowHeight)
```

**描述**

设置启动Ability时的窗口高度，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t windowHeight启动Ability时的窗口高度，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowHeight(options, 500);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsWindowHeight()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t &windowHeight)
```

**描述**

获取启动Ability时的窗口高度，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &windowHeight启动Ability时的窗口高度，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowHeight = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowHeight(options, windowHeight);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsWindowWidth()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t windowWidth)
```

**描述**

设置启动Ability时的窗口宽度，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t windowWidth启动Ability时的窗口宽度，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowWidth(options, 500);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsWindowWidth()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t &windowWidth)
```

**描述**

获取启动Ability时的窗口宽度，单位为px。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &windowWidth启动Ability时的窗口宽度，单位为px。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowWidth = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowWidth(options, windowWidth);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsStartVisibility()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility startVisibility)
```

**描述**

设置启动Ability时窗口和dock栏图标的显示模式。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsStartOptions结构体。[AbilityRuntime_StartVisibility](context_constant.h.md#ZH-CN_TOPIC_0000002529284651__abilityruntime_startvisibility) startVisibility需要设置的显示模式。取值范围参见AbilityRuntime_StartVisibility。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示设置成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空，或startVisibility取值不在枚举类AbilityRuntime_StartVisibility中。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_StartVisibility visibility = AbilityRuntime_StartVisibility::ABILITY_RUNTIME_SHOW_UPON_START;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartVisibility(options, visibility);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsStartVisibility()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility &startVisibility)
```

**描述**

获取启动Ability时窗口和dock栏图标的显示模式。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsStartOptions结构体。[bilityRuntime_StartVisibility](context_constant.h.md#ZH-CN_TOPIC_0000002529284651__abilityruntime_startvisibility) &startVisibility获取到的显示模式。取值范围参见AbilityRuntime_StartVisibility。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示获取成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空，或startVisibility未被设置。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_StartVisibility visibility;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartVisibility(options, visibility);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsStartWindowIcon()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative *startWindowIcon)
```

**描述**

设置启动Ability时的窗口启动图标。图片数据大小限制为600M。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。OH_PixelmapNative *startWindowIcon启动Ability时的窗口启动图标。图片数据大小限制为600M。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空，或者OH_PixelmapNative没有置为空指针。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    uint8_t data[96];
    size_t dataSize = 96;
    for (int i = 0; i < dataSize; i++) {
        data[i] = i + 1;
    }

    //创建参数结构体实例，并设置参数
    OH_Pixelmap_InitializationOptions *createOpts = nullptr;
    OH_PixelmapInitializationOptions_Create(&createOpts);
    OH_PixelmapInitializationOptions_SetWidth(createOpts, 6);
    OH_PixelmapInitializationOptions_SetHeight(createOpts, 4);
    OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
    OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNKNOWN);

    //创建Pixelmap实例
    OH_PixelmapNative *startWindowIcon = nullptr;
    Image_ErrorCode errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &startWindowIcon);
    if (errCode != IMAGE_SUCCESS) {
        // 记录错误日志以及其他业务处理

        // 销毁createOpts，防止内存泄漏
        OH_PixelmapInitializationOptions_Release(createOpts);
        return;
    }

    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理

        // 销毁createOpts，防止内存泄漏
        OH_PixelmapInitializationOptions_Release(createOpts);

        // 销毁startWindowIcon，防止内存泄漏
        OH_PixelmapNative_Release(startWindowIcon);
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartWindowIcon(options, startWindowIcon);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁createOpts，防止内存泄漏
    OH_PixelmapInitializationOptions_Release(createOpts);

    // 销毁startWindowIcon，防止内存泄漏
    OH_PixelmapNative_Release(startWindowIcon);

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsStartWindowIcon()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative **startWindowIcon)
```

**描述**

获取启动Ability时的窗口启动图标。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。OH_PixelmapNative **startWindowIcon启动Ability时的窗口启动图标。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions或者StartWindowBackgroundColor为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    OH_PixelmapNative *startWindowIcon = nullptr;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartWindowIcon(options, &startWindowIcon);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁startWindowIcon，防止内存泄漏
    OH_PixelmapNative_Release(startWindowIcon);

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, const char *startWindowBackgroundColor)
```

**描述**

设置启动Ability时的窗口背景颜色。启动UIAbility时，启动页所显示的背景颜色如果未设置该字段，则默认采用[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中[abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)的startWindowBackground字段的配置。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。const char *startWindowBackgroundColor启动Ability时的窗口背景颜色。固定为ARGB格式, 如：#E5FFFFFF。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空，或者StartWindowBackgroundColor没有置为空指针。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor(options, "#00000000");
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, char **startWindowBackgroundColor, size_t &size)
```

**描述**

获取启动Ability时的窗口背景颜色。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。char **startWindowBackgroundColor启动Ability时的窗口背景颜色。固定为ARGB格式, 如：#E5FFFFFF。size_t &size获取到的窗口背景颜色的大小。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions或者SupportedWindowModes为空，或者Size为0。

在返回ABILITY_RUNTIME_ERROR_CODE_INTERNAL时，表示开发者无法恢复的内部错误，比如内部调用malloc错误，或者字符串拷贝函数出错。

**示例代码：**

```ets
#include <cstdlib>

#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    char *startWindowBackgroundColor = nullptr;
    size_t size = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor(options,
        &startWindowBackgroundColor, size);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    if (startWindowBackgroundColor != nullptr) {
        // 销毁startWindowBackgroundColor，防止内存泄漏
        free(startWindowBackgroundColor);
        startWindowBackgroundColor = nullptr;
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsSupportedWindowModes()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode *supportedWindowModes,size_t size)
```

**描述**

设置启动Ability时的组件所支持的窗口模式。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。[AbilityRuntime_SupportedWindowMode](context_constant.h.md#ZH-CN_TOPIC_0000002529284651__abilityruntime_supportedwindowmode) *supportedWindowModes启动Ability时的组件所支持的窗口模式。取值范围参见AbilityRuntime_SupportedWindowMode。size_t size组件所支持的窗口模式大小。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions或者SupportedWindowModes为空，或者Size为0。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    size_t supportedWindowModesSize = 3;
    AbilityRuntime_SupportedWindowMode supportedWindowModes[3] = {
        ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_FULL_SCREEN,
        ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_SPLIT,
        ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_FLOATING,
    };
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsSupportedWindowModes(options,
        supportedWindowModes, supportedWindowModesSize);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsSupportedWindowModes()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode **supportedWindowModes,size_t &size)
```

**描述**

获取启动Ability时的组件所支持的窗口模式。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。[AbilityRuntime_SupportedWindowMode](context_constant.h.md#ZH-CN_TOPIC_0000002529284651__abilityruntime_supportedwindowmode) **supportedWindowModes启动Ability时的组件所支持的窗口模式。取值范围参见AbilityRuntime_SupportedWindowMode。size组件所支持的窗口模式大小。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空，或者SupportWindowMode没有置为空指针。

在返回ABILITY_RUNTIME_ERROR_CODE_INTERNAL时，表示开发者无法恢复的内部错误，比如内部调用malloc错误。

**示例代码：**

```ets
#include <cstdlib>

#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_SupportedWindowMode *supportedWindowModes = nullptr;
    size_t size = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsSupportedWindowModes(options,
        &supportedWindowModes, size);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    if (supportedWindowModes != nullptr) {
        // 销毁supportedWindowModes，防止内存泄漏
        free(supportedWindowModes);
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsMinWindowWidth()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t minWindowWidth)
```

**描述**

设置启动Ability时的窗口最小宽度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t minWindowWidth启动Ability时的窗口最小宽度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMinWindowWidth(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsMinWindowWidth()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowWidth)
```

**描述**

获取启动Ability时的窗口最小宽度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &minWindowWidth启动Ability时的窗口最小宽度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t minWindowWidth = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMinWindowWidth(options, minWindowWidth);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsMaxWindowWidth()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowWidth)
```

**描述**

设置启动Ability时的窗口最大宽度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t maxWindowWidth启动Ability时的窗口最大宽度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMaxWindowWidth(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsMaxWindowWidth()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowWidth)
```

**描述**

获取启动Ability时的窗口最大宽度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &maxWindowWidth启动Ability时的窗口最大宽度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t maxWindowWidth = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMaxWindowWidth(options, maxWindowWidth);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsMinWindowHeight()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t minWindowHeight)
```

**描述**

设置启动Ability时的窗口最小高度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t minWindowHeight启动Ability时的窗口最小高度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMinWindowHeight(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsMinWindowHeight()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowHeight)
```

**描述**

获取启动Ability时的窗口最小高度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &minWindowHeight启动Ability时的窗口最小高度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t minWindowHeight = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMinWindowHeight(options, minWindowHeight);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_SetStartOptionsMaxWindowHeight()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowHeight)
```

**描述**

设置启动Ability时的窗口最大高度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t maxWindowHeight启动Ability时的窗口最大高度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMaxWindowHeight(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### OH_AbilityRuntime_GetStartOptionsMaxWindowHeight()

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowHeight)
```

**描述**

获取启动Ability时的窗口最大高度，单位为vp。

**起始版本：** 17

**参数：**

参数项描述[AbilityRuntime_StartOptions](AbilityRuntime_StartOptions.md) *startOptionsAbilityRuntime_StartOptions对象。int32_t &maxWindowHeight启动Ability时的窗口最大高度，单位为vp。

**返回：**

类型说明[AbilityRuntime_ErrorCode](ability_runtime_common.h.md#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)

在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示接口调用成功。

在返回ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID时，表示StartOptions为空。

**示例代码：**

```ets
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t maxWindowHeight = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMaxWindowHeight(options, maxWindowHeight);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```