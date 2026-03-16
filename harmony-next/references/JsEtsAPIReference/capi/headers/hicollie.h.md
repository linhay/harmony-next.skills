# hicollie.h

#### 概述

HiCollie模块对外提供检测业务线程卡死、卡顿，以及上报卡死事件的能力。

**引用文件：** <hicollie/hicollie.h>

**库：** libohhicollie.so

**系统能力：** SystemCapability.HiviewDFX.HiCollie

**起始版本：** 12

**相关模块：**[HiCollie](../../topics/misc/HiCollie.md)

#### 汇总

#### 结构体

名称typedef关键字描述[HiCollie_DetectionParam](../../topics/media/HiCollie_DetectionParam.md)HiCollie_DetectionParam检测业务线程卡顿的相关参数。请注意，API 12及以上支持。[HiCollie_SetTimerParam](../../topics/media/HiCollie_SetTimerParam.md)HiCollie_SetTimerParam定义OH_HiCollie_SetTimer函数的输入参数。

#### 枚举

名称typedef关键字描述[HiCollie_ErrorCode](#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)HiCollie_ErrorCode错误码定义。[HiCollie_Flag](#ZH-CN_TOPIC_0000002497605670__hicollie_flag)HiCollie_Flag定义函数执行超时时发生的动作。

#### 函数

名称typedef关键字描述[typedef void (*OH_HiCollie_Task)(void)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_task)OH_HiCollie_Task

在业务线程卡死检测中，通过实现该函数来检测业务线程是否卡住。

 HiCollie将在独立线程中每3秒调用一次该函数。

 例如：该函数可实现向业务线程发送消息，在业务线程接收到消息之后，设置一个标记，检查这个标记，确定业务线程是否卡住。

[typedef void (*OH_HiCollie_BeginFunc)(const char* eventName)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_beginfunc)OH_HiCollie_BeginFunc

卡顿检测中,函数用于记录业务线程处理事件的开始时间。

 检查处理事件的执行时间，HiCollie将检查每个事件的持续时间。如果超过预设阈值，上报jank事件。

 该函数是在每个事件处理之前插入的回调函数。

[typedef void (*OH_HiCollie_EndFunc)(const char* eventName)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_endfunc)OH_HiCollie_EndFunc

卡顿检测中, 该函数用于检测业务线程处理事件是否卡顿。

 检查处理事件的执行时间，HiCollie将检查每个事件的持续时间。如果超过预设阈值，上报jank事件。

 该函数是在每个事件处理之后插入的回调函数。

[HiCollie_ErrorCode OH_HiCollie_Init_StuckDetection(OH_HiCollie_Task task)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_init_stuckdetection)-

注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。

 默认检测时间：3s上报BUSSINESS_THREAD_BLOCK_3S告警事件，6s上报BUSSINESS_THREAD_BLOCK_6S卡死事件。

[HiCollie_ErrorCode OH_HiCollie_Init_StuckDetectionWithTimeout(OH_HiCollie_Task task, uint32_t stuckTimeout)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_init_stuckdetectionwithtimeout)-

注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。

 开发者可以设置卡死检测时间，可设置的时间范围：[3, 15]，单位：秒。

[HiCollie_ErrorCode OH_HiCollie_Init_JankDetection(OH_HiCollie_BeginFunc* beginFunc, OH_HiCollie_EndFunc* endFunc, HiCollie_DetectionParam param)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_init_jankdetection)-

注册应用业务线程卡顿检测的回调函数。

 线程卡顿监控功能需要开发者实现两个卡顿检测回调函数, 分别放在业务线程处理事件的前后。作为插桩函数，监控业务线程处理事件执行情况。

[HiCollie_ErrorCode OH_HiCollie_Report(bool* isSixSecond)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_report)-

上报应用业务线程卡死事件，生成卡死故障日志，辅助定位应用卡死问题。

 先调用OH_HiCollie_Init_StuckDetection或OH_HiCollie_Init_StuckDetectionWithTimeout接口，初始化检测的task；

 如果task任务超时，结合业务逻辑，调用OH_HiCollie_Report接口上报卡死事件。

[typedef void (*OH_HiCollie_Callback)(void*)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_callback)OH_HiCollie_Callback当用户调用[OH_HiCollie_SetTimer](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_settimer)后，未在其自定义的任务超时时间阈值内调用[OH_HiCollie_CancelTimer](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_canceltimer)，回调函数将被执行。[HiCollie_ErrorCode OH_HiCollie_SetTimer(HiCollie_SetTimerParam param, int *id)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_settimer)-

注册定时器，用于检测函数或代码块执行是否超过自定义时间。

 结合OH_HiCollie_CancelTimer接口配套使用，应在调用耗时的函数之前使用。

[void OH_HiCollie_CancelTimer(int id)](#ZH-CN_TOPIC_0000002497605670__oh_hicollie_canceltimer)-

取消定时器。

 结合OH_HiCollie_SetTimer接口配套使用，执行函数或代码块后使用，OH_HiCollie_CancelTimer通过id将该任务取消；

 若未在自定义时间内取消，则执行回调函数，在特定自定义超时动作下，生成故障日志。

#### 枚举类型说明

#### HiCollie_ErrorCode

```ets
enum HiCollie_ErrorCode
```

**描述**

错误码定义。

**起始版本：** 12

枚举项描述HICOLLIE_SUCCESS = 0成功。HICOLLIE_INVALID_ARGUMENT = 401无效参数。HICOLLIE_WRONG_THREAD_CONTEXT = 29800001调用线程错误。HICOLLIE_REMOTE_FAILED = 29800002远程调用错误。HICOLLIE_INVALID_TIMER_NAME = 29800003

无效的函数执行超时检测器名称。

**起始版本：** 18

HICOLLIE_INVALID_TIMEOUT_VALUE = 29800004

无效的函数执行超时时间阈值。

**起始版本：** 18

HICOLLIE_WRONG_PROCESS_CONTEXT = 29800005

函数执行超时检测接入进程错误。

**起始版本：** 18

HICOLLIE_WRONG_TIMER_ID_OUTPUT_PARAM = 29800006

用于保存返回的计时器id的指针不应为NULL。

**起始版本：** 18

#### HiCollie_Flag

```ets
enum HiCollie_Flag
```

**描述**

定义函数执行超时时发生的动作。

**起始版本：** 18

枚举项描述HICOLLIE_FLAG_DEFAULT = (~0)默认动作，生成日志及执行恢复动作。HICOLLIE_FLAG_NOOP = (0)仅执行回调函数。HICOLLIE_FLAG_LOG = (1 << 0)生成日志。HICOLLIE_FLAG_RECOVERY = (1 << 1)执行恢复动作。

#### 函数说明

#### OH_HiCollie_Task()

```ets
typedef void (*OH_HiCollie_Task)(void)
```

**描述**

在业务线程卡死检测中，通过实现该函数来检测业务线程是否卡住。

 HiCollie将在独立线程中每3秒调用一次该函数。

 例如：该函数可实现向业务线程发送消息，在业务线程接收到消息之后，设置一个标记，检查这个标记，确定业务线程是否卡住。

**起始版本：** 12

#### OH_HiCollie_BeginFunc()

```ets
typedef void (*OH_HiCollie_BeginFunc)(const char* eventName)
```

**描述**

卡顿检测中,函数用于记录业务线程处理事件的开始时间。

 检查处理事件的执行时间，HiCollie将检查每个事件的持续时间。如果超过预设阈值，上报jank事件。

 该函数是在每个事件处理之前插入的回调函数。

**起始版本：** 12

**参数：**

参数项描述const char* eventName业务线程处理事件的名字。

#### OH_HiCollie_EndFunc()

```ets
typedef void (*OH_HiCollie_EndFunc)(const char* eventName)
```

**描述**

卡顿检测中, 该函数用于检测业务线程处理事件是否卡顿。

 检查处理事件的执行时间，HiCollie将检查每个事件的持续时间。如果超过预设阈值，上报jank事件。

 该函数是在每个事件处理之后插入的回调函数。

**起始版本：** 12

**参数：**

参数项描述const char* eventName业务线程处理事件的名字。

#### OH_HiCollie_Init_StuckDetection()

```ets
HiCollie_ErrorCode OH_HiCollie_Init_StuckDetection(OH_HiCollie_Task task)
```

**描述**

注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。

 默认检测时间：3s上报BUSSINESS_THREAD_BLOCK_3S告警事件，6s上报BUSSINESS_THREAD_BLOCK_6S卡死事件。

**起始版本：** 12

**参数：**

参数项描述[OH_HiCollie_Task](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_task) task每3秒执行一次的周期性检测任务，用于检测业务线程是否卡住。

**返回：**

类型说明[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)

[HICOLLIE_SUCCESS](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 0 - 成功。

[HICOLLIE_WRONG_THREAD_CONTEXT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800001 - 调用线程错误。在非主线程中调用该函数。

具体可参考[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)。

#### OH_HiCollie_Init_StuckDetectionWithTimeout()

```ets
HiCollie_ErrorCode OH_HiCollie_Init_StuckDetectionWithTimeout(OH_HiCollie_Task task, uint32_t stuckTimeout)
```

**描述**

注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。

 开发者可以设置卡死检测时间，可设置的时间范围：[3, 15]，单位：秒。

**起始版本：** 18

**参数：**

参数项描述[OH_HiCollie_Task](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_task) task每stuckTimeout时间执行一次的周期性检测任务，用于检测业务线程是否卡住。uint32_t stuckTimeout

检测业务线程卡死时间。任务执行超过stuckTimeout时间上报卡死告警事件；任务超过stuckTimeout * 2时间上报卡死事件。

单位：s。规定：最大值15s，最小值3s。

**返回：**

类型说明[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)

[HICOLLIE_SUCCESS](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 0 - 成功。

[HICOLLIE_INVALID_ARGUMENT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 401 - 卡死检测时间设置错误。

[HICOLLIE_WRONG_THREAD_CONTEXT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800001 - 调用线程错误。在非主线程中调用该函数。

具体可参考[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)。

#### OH_HiCollie_Init_JankDetection()

```ets
HiCollie_ErrorCode OH_HiCollie_Init_JankDetection(OH_HiCollie_BeginFunc* beginFunc, OH_HiCollie_EndFunc* endFunc, HiCollie_DetectionParam param)
```

**描述**

注册应用业务线程卡顿检测的回调函数。

 线程卡顿监控功能需要开发者实现两个卡顿检测回调函数, 分别放在业务线程处理事件的前后。作为插桩函数，监控业务线程处理事件执行情况。

**起始版本：** 12

**参数：**

参数项描述[OH_HiCollie_BeginFunc](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_beginfunc)* beginFunc检测业务线程处理事件前的函数。[OH_HiCollie_EndFunc](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_endfunc)* endFunc检测业务线程处理事件后的函数。[HiCollie_DetectionParam](../../topics/media/HiCollie_DetectionParam.md) param扩展参数以供将来使用。

**返回：**

类型说明[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)

[HICOLLIE_SUCCESS](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 0 - 成功。

[HICOLLIE_INVALID_ARGUMENT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 401 - 开始函数和结束函数两者都必须有值或为空，否则将返回该错误值。

[HICOLLIE_WRONG_THREAD_CONTEXT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800001 - 调用线程错误。在非主线程中调用该函数。

具体可参考[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)。

#### OH_HiCollie_Report()

```ets
HiCollie_ErrorCode OH_HiCollie_Report(bool* isSixSecond)
```

**描述**

上报应用业务线程卡死事件，生成卡死故障日志，辅助定位应用卡死问题。

 先调用OH_HiCollie_Init_StuckDetection或OH_HiCollie_Init_StuckDetectionWithTimeout接口，初始化检测的task；

 如果task任务超时，结合业务逻辑，调用OH_HiCollie_Report接口上报卡死事件。

**起始版本：** 12

**参数：**

参数项描述bool* isSixSecond布尔指针。布尔指针的值。如果卡住6秒，则为真。如果卡住3秒，则为False。

**返回：**

类型说明[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)

[HICOLLIE_SUCCESS](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 0 - 成功。

[HICOLLIE_INVALID_ARGUMENT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 401 - 开始函数和结束函数两者都必须有值或为空，否则将返回该错误值。

[HICOLLIE_WRONG_THREAD_CONTEXT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800001 - 调用线程错误。在非主线程中调用该函数。

[HICOLLIE_REMOTE_FAILED](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800002 - 远程调用错误。请求IPC远程服务失败。

具体可参考[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)。

#### OH_HiCollie_Callback()

```ets
typedef void (*OH_HiCollie_Callback)(void*)
```

**描述**

当用户调用[OH_HiCollie_SetTimer](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_settimer)后，未在其自定义的任务超时时间阈值内调用[OH_HiCollie_CancelTimer](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_canceltimer)，回调函数将被执行。

**起始版本：** 18

#### OH_HiCollie_SetTimer()

```ets
HiCollie_ErrorCode OH_HiCollie_SetTimer(HiCollie_SetTimerParam param, int *id)
```

**描述**

注册定时器，用于检测函数或代码块执行是否超过自定义时间。

 结合OH_HiCollie_CancelTimer接口配套使用，应在调用耗时的函数之前使用。

**起始版本：** 18

**参数：**

参数项描述[HiCollie_SetTimerParam](../../topics/media/HiCollie_SetTimerParam.md) param定义输入参数。int *id用于保存返回的计时器id的指针，它不应为NULL。

**返回：**

类型说明[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)

[HICOLLIE_SUCCESS](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 0 - 成功。

[HICOLLIE_INVALID_TIMER_NAME](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800003 - 无效的计时器名称，不应为NULL或空字符串。

[HICOLLIE_INVALID_TIMEOUT_VALUE](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800004 - 无效的超时值。

[HICOLLIE_WRONG_PROCESS_CONTEXT](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800005 - 无效的接入检测进程上下文，appspawn与nativespawn进程中不可调用。

[HICOLLIE_WRONG_TIMER_ID_OUTPUT_PARAM](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode) 29800006 - 用于保存返回的计时器id的指针，不应该为NULL。

具体可参考[HiCollie_ErrorCode](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_errorcode)。

#### OH_HiCollie_CancelTimer()

```ets
void OH_HiCollie_CancelTimer(int id)
```

**描述**

取消定时器。

 结合OH_HiCollie_SetTimer接口配套使用，执行函数或代码块后使用，OH_HiCollie_CancelTimer通过id将该任务取消；

 若未在自定义时间内取消，则执行回调函数，在特定自定义超时动作下，生成故障日志。

**起始版本：** 18

**参数：**

参数项描述int id执行[OH_HiCollie_SetTimer](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_settimer)函数后更新的计时器id。