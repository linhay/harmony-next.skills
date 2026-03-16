# fiber.h

#### 概述

纤程是一种轻量级的用户态线程，用于在用户空间内实现高效的任务调度和上下文切换，此为声明纤程的C接口。

**引用文件：** <ffrt/fiber.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 20

**相关模块：**[FFRT](../../topics/misc/FFRT.md)

#### 汇总

#### 函数

名称描述[FFRT_C_API int ffrt_fiber_init(ffrt_fiber_t* fiber, void(*func)(void*), void* arg, void* stack, size_t stack_size)](#ZH-CN_TOPIC_0000002529445521__ffrt_fiber_init)纤程初始化函数，此函数初始化纤程实例，该实例可以存储上下文。[FFRT_C_API void ffrt_fiber_switch(ffrt_fiber_t* from, ffrt_fiber_t* to)](#ZH-CN_TOPIC_0000002529445521__ffrt_fiber_switch)纤程切换函数，调用该函数的线程会暂停当前任务的执行，并将当前上下文保存到from纤程中，同时恢复to纤程中的上下文。

#### 函数说明

#### ffrt_fiber_init()

```ets
FFRT_C_API int ffrt_fiber_init(ffrt_fiber_t* fiber, void(*func)(void*), void* arg, void* stack, size_t stack_size)
```

**描述**

纤程初始化函数，此函数初始化纤程实例，该实例可以存储上下文。

**起始版本：** 20

**参数：**

参数项描述fiber指向要初始化的纤程的指针, 具体可参考[ffrt_fiber_t](../../topics/misc/ffrt_fiber_t.md)。func纤程切换后所要执行的方法。void* arg纤程切换后所要执行方法的入参。void* stack纤程堆栈内存指针。size_t stack_size纤程堆栈大小, 具体可参考[ffrt_storage_size_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_storage_size_t)。

**返回：**

类型说明FFRT_C_API int初始化成功返回ffrt_success，否则返回ffrt_error。

#### ffrt_fiber_switch()

```ets
FFRT_C_API void ffrt_fiber_switch(ffrt_fiber_t* from, ffrt_fiber_t* to)
```

**描述**

纤程切换函数，调用该函数的线程会暂停当前任务的执行，并将当前上下文保存到from纤程中，同时恢复to纤程中的上下文。

**起始版本：** 20

**参数：**

参数项描述[ffrt_fiber_t](../../topics/misc/ffrt_fiber_t.md)* from将要保存的纤程指针。[ffrt_fiber_t](../../topics/misc/ffrt_fiber_t.md)* to将要恢复的纤程指针。