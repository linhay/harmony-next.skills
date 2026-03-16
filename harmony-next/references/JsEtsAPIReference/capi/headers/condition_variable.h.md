# condition_variable.h

#### 概述

声明条件变量的C接口。

**引用文件：** <ffrt/condition_variable.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：**[FFRT](../../topics/misc/FFRT.md)

#### 汇总

#### 函数

名称描述[FFRT_C_API int ffrt_cond_init(ffrt_cond_t* cond, const ffrt_condattr_t* attr)](#ZH-CN_TOPIC_0000002529445517__ffrt_cond_init)初始化条件变量。[FFRT_C_API int ffrt_cond_signal(ffrt_cond_t* cond)](#ZH-CN_TOPIC_0000002529445517__ffrt_cond_signal)唤醒阻塞在条件变量上的一个任务。[FFRT_C_API int ffrt_cond_broadcast(ffrt_cond_t* cond)](#ZH-CN_TOPIC_0000002529445517__ffrt_cond_broadcast)唤醒阻塞在条件变量上的所有任务。[FFRT_C_API int ffrt_cond_wait(ffrt_cond_t* cond, ffrt_mutex_t* mutex)](#ZH-CN_TOPIC_0000002529445517__ffrt_cond_wait)条件变量等待函数，条件变量不满足时阻塞当前任务。[FFRT_C_API int ffrt_cond_timedwait(ffrt_cond_t* cond, ffrt_mutex_t* mutex, const struct timespec* time_point)](#ZH-CN_TOPIC_0000002529445517__ffrt_cond_timedwait)条件变量超时等待函数，条件变量不满足时阻塞当前任务，超时等待返回。如果达到最大等待时间点时没有调用ffrt_cond_signal或ffrt_cond_broadcast函数解除线程阻塞，则线程会被自动解除阻塞。[FFRT_C_API int ffrt_cond_destroy(ffrt_cond_t* cond)](#ZH-CN_TOPIC_0000002529445517__ffrt_cond_destroy)销毁条件变量。

#### 函数说明

#### ffrt_cond_init()

```ets
FFRT_C_API int ffrt_cond_init(ffrt_cond_t* cond, const ffrt_condattr_t* attr)
```

**描述**

初始化条件变量。

**起始版本：** 10

**参数：**

参数项描述[ffrt_cond_t](../../topics/misc/ffrt_cond_t.md)* cond条件变量指针。[const ffrt_condattr_t](../../topics/misc/ffrt_condattr_t.md)* attr条件变量属性指针。

**返回：**

类型说明FFRT_C_API int

初始化条件变量成功返回ffrt_success，

 初始化条件变量失败返回ffrt_error_inval。

#### ffrt_cond_signal()

```ets
FFRT_C_API int ffrt_cond_signal(ffrt_cond_t* cond)
```

**描述**

唤醒阻塞在条件变量上的一个任务。

**起始版本：** 10

**参数：**

参数项描述[ffrt_cond_t](../../topics/misc/ffrt_cond_t.md)* cond条件变量指针。

**返回：**

类型说明FFRT_C_API int

唤醒成功返回ffrt_success，

 唤醒失败返回ffrt_error_inval。

#### ffrt_cond_broadcast()

```ets
FFRT_C_API int ffrt_cond_broadcast(ffrt_cond_t* cond)
```

**描述**

唤醒阻塞在条件变量上的所有任务。

**起始版本：** 10

**参数：**

参数项描述[ffrt_cond_t](../../topics/misc/ffrt_cond_t.md)* cond条件变量指针。

**返回：**

类型说明FFRT_C_API int

唤醒成功返回ffrt_success，

 唤醒失败返回ffrt_error_inval。

#### ffrt_cond_wait()

```ets
FFRT_C_API int ffrt_cond_wait(ffrt_cond_t* cond, ffrt_mutex_t* mutex)
```

**描述**

条件变量等待函数，条件变量不满足时阻塞当前任务。

**起始版本：** 10

**参数：**

参数项描述[ffrt_cond_t](../../topics/misc/ffrt_cond_t.md)* cond条件变量指针。[ffrt_mutex_t](../../topics/misc/ffrt_mutex_t.md)* mutexmutex指针。

**返回：**

类型说明FFRT_C_API int

等待后被成功唤醒返回ffrt_success，

 等待失败返回ffrt_error_inval。

#### ffrt_cond_timedwait()

```ets
FFRT_C_API int ffrt_cond_timedwait(ffrt_cond_t* cond, ffrt_mutex_t* mutex, const struct timespec* time_point)
```

**描述**

条件变量超时等待函数，条件变量不满足时阻塞当前任务，超时等待返回。如果达到最大等待时间点时没有调用ffrt_cond_signal或ffrt_cond_broadcast函数解除线程阻塞，则线程会被自动解除阻塞。

**起始版本：** 10

**参数：**

参数项描述[ffrt_cond_t](../../topics/misc/ffrt_cond_t.md)* cond条件变量指针。[ffrt_mutex_t](../../topics/misc/ffrt_mutex_t.md)* mutexmutex指针。const struct timespec* time_point最大等待到的时间点，超过这个时间点等待返回。

**返回：**

类型说明FFRT_C_API int

等待后被成功唤醒返回ffrt_success，

 等待超时返回ffrt_error_timedout，

 等待失败ffrt_error_inval。

#### ffrt_cond_destroy()

```ets
FFRT_C_API int ffrt_cond_destroy(ffrt_cond_t* cond)
```

**描述**

销毁条件变量。

**起始版本：** 10

**参数：**

参数项描述[ffrt_cond_t](../../topics/misc/ffrt_cond_t.md)* cond条件变量指针。

**返回：**

类型说明FFRT_C_API int

销毁条件变量成功返回ffrt_success，

销毁条件变量失败返回ffrt_error_inval。