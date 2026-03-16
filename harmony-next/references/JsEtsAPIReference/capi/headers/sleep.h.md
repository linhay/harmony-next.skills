# sleep.h

#### 概述

声明sleep和yield的C接口。

**引用文件：** <ffrt/sleep.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：**[FFRT](../../topics/misc/FFRT.md)

#### 汇总

#### 函数

名称描述[FFRT_C_API int ffrt_usleep(uint64_t usec)](#ZH-CN_TOPIC_0000002497605554__ffrt_usleep)睡眠调用线程固定的时间。[FFRT_C_API void ffrt_yield(void)](#ZH-CN_TOPIC_0000002497605554__ffrt_yield)当前任务主动放权，让其他任务有机会调度执行。

#### 函数说明

#### ffrt_usleep()

```ets
FFRT_C_API int ffrt_usleep(uint64_t usec)
```

**描述**

睡眠调用线程固定的时间。

**起始版本：** 10

**参数：**

参数项描述uint64_t usec睡眠时间，单位是微秒。

**返回：**

类型说明FFRT_C_API int

执行成功时返回ffrt_success，

 执行失败时返回ffrt_error。

#### ffrt_yield()

```ets
FFRT_C_API void ffrt_yield(void)
```

**描述**

当前任务主动放权，让其他任务有机会调度执行。

**起始版本：** 10