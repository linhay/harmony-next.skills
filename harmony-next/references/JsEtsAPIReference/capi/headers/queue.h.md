# queue.h

#### 概述

声明队列的C接口。

**引用文件：** <ffrt/queue.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：**[FFRT](../../topics/misc/FFRT.md)

#### 汇总

#### 结构体

名称描述[ffrt_queue_t](../../topics/misc/ffrt_queue_t.md)队列句柄。

#### 枚举

名称typedef关键字描述[ffrt_queue_type_t](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_type_t)ffrt_queue_type_t队列类型。

#### 函数

名称描述[FFRT_C_API int ffrt_queue_attr_init(ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_init)初始化队列属性。[FFRT_C_API void ffrt_queue_attr_destroy(ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_destroy)销毁队列属性。[FFRT_C_API void ffrt_queue_attr_set_qos(ffrt_queue_attr_t* attr, ffrt_qos_t qos)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_set_qos)设置队列QoS属性。[FFRT_C_API ffrt_qos_t ffrt_queue_attr_get_qos(const ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_get_qos)获取队列QoS属性。[FFRT_C_API void ffrt_queue_attr_set_timeout(ffrt_queue_attr_t* attr, uint64_t timeout_us)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_set_timeout)设置串行队列timeout属性。超时时间的最小值是1ms，如果设置的值小于1ms，那么超时时间被设置为1ms。[FFRT_C_API uint64_t ffrt_queue_attr_get_timeout(const ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_get_timeout)获取串行队列任务执行的timeout时间。[FFRT_C_API void ffrt_queue_attr_set_callback(ffrt_queue_attr_t* attr, ffrt_function_header_t* f)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_set_callback)设置串行队列超时回调方法。[FFRT_C_API ffrt_function_header_t* ffrt_queue_attr_get_callback(const ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_get_callback)获取串行队列超时回调方法。[FFRT_C_API void ffrt_queue_attr_set_max_concurrency(ffrt_queue_attr_t* attr, const int max_concurrency)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_set_max_concurrency)设置并行队列最大并发度。[FFRT_C_API int ffrt_queue_attr_get_max_concurrency(const ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_get_max_concurrency)获取并行队列最大并发度。[FFRT_C_API void ffrt_queue_attr_set_thread_mode(ffrt_queue_attr_t* attr, bool mode)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_set_thread_mode)设置队列中的任务是以协程模式还是以线程模式运行。默认以协程模式运行。[FFRT_C_API bool ffrt_queue_attr_get_thread_mode(const ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_attr_get_thread_mode)获取队列中的任务是以协程模式还是以线程模式运行。[FFRT_C_API ffrt_queue_t ffrt_queue_create(ffrt_queue_type_t type, const char* name, const ffrt_queue_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_create)创建队列。[FFRT_C_API void ffrt_queue_destroy(ffrt_queue_t queue)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_destroy)销毁队列。[FFRT_C_API void ffrt_queue_submit(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_submit)提交一个任务到队列中调度执行。[FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_submit_h)提交一个任务到队列中调度执行，并返回任务句柄。[FFRT_C_API void ffrt_queue_submit_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_submit_f)提交一个任务到队列中调度执行，是ffrt_queue_submit接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt_queue_submit接口。[FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_submit_h_f)提交一个任务到队列中调度执行，并返回任务句柄，是ffrt_queue_submit_h接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt_queue_submit_h接口。[FFRT_C_API void ffrt_queue_wait(ffrt_task_handle_t handle)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_wait)等待队列中一个任务执行完成。[FFRT_C_API int ffrt_queue_cancel(ffrt_task_handle_t handle)](#ZH-CN_TOPIC_0000002529285545__ffrt_queue_cancel)取消队列中一个任务。[FFRT_C_API ffrt_queue_t ffrt_get_main_queue(void)](#ZH-CN_TOPIC_0000002529285545__ffrt_get_main_queue)获取主线程队列。[FFRT_C_API ffrt_queue_t ffrt_get_current_queue(void)](#ZH-CN_TOPIC_0000002529285545__ffrt_get_current_queue)获取应用Worker(ArkTs)线程队列。

#### 枚举类型说明

#### ffrt_queue_type_t

```ets
enum ffrt_queue_type_t
```

**描述**

队列类型。

**起始版本：** 12

枚举项描述ffrt_queue_serial串行队列ffrt_queue_concurrent并行队列ffrt_queue_max无效队列类型

#### 函数说明

#### ffrt_queue_attr_init()

```ets
FFRT_C_API int ffrt_queue_attr_init(ffrt_queue_attr_t* attr)
```

**描述**

初始化队列属性。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。

**返回：**

类型说明FFRT_C_API int

执行成功时返回0，

 执行失败时返回-1。

#### ffrt_queue_attr_destroy()

```ets
FFRT_C_API void ffrt_queue_attr_destroy(ffrt_queue_attr_t* attr)
```

**描述**

销毁队列属性。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。

#### ffrt_queue_attr_set_qos()

```ets
FFRT_C_API void ffrt_queue_attr_set_qos(ffrt_queue_attr_t* attr, ffrt_qos_t qos)
```

**描述**

设置队列QoS属性。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。[ffrt_qos_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__变量) qosQoS属性值。

#### ffrt_queue_attr_get_qos()

```ets
FFRT_C_API ffrt_qos_t ffrt_queue_attr_get_qos(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列QoS属性。

**起始版本：** 10

**参数：**

参数项描述[const ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。

**返回：**

类型说明FFRT_C_API [ffrt_qos_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__变量)返回队列的QoS属性。

#### ffrt_queue_attr_set_timeout()

```ets
FFRT_C_API void ffrt_queue_attr_set_timeout(ffrt_queue_attr_t* attr, uint64_t timeout_us)
```

**描述**

设置串行队列timeout属性。超时时间的最小值是1ms，如果设置的值小于1ms，那么超时时间被设置为1ms。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr串行队列属性指针。uint64_t timeout_us串行队列任务执行的timeout时间(微秒)。

#### ffrt_queue_attr_get_timeout()

```ets
FFRT_C_API uint64_t ffrt_queue_attr_get_timeout(const ffrt_queue_attr_t* attr)
```

**描述**

获取串行队列任务执行的timeout时间。

**起始版本：** 10

**参数：**

参数项描述[const ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr串行队列属性指针。

**返回：**

类型说明FFRT_C_API uint64_t返回串行队列任务执行的timeout时间。

#### ffrt_queue_attr_set_callback()

```ets
FFRT_C_API void ffrt_queue_attr_set_callback(ffrt_queue_attr_t* attr, ffrt_function_header_t* f)
```

**描述**

设置串行队列超时回调方法。

不建议在f中调用exit函数，可能导致未定义行为。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr串行队列属性指针。[ffrt_function_header_t](../../topics/misc/ffrt_function_header_t.md)* f超时回调方法执行体。

#### ffrt_queue_attr_get_callback()

```ets
FFRT_C_API ffrt_function_header_t* ffrt_queue_attr_get_callback(const ffrt_queue_attr_t* attr)
```

**描述**

获取串行队列超时回调方法。

**起始版本：** 10

**参数：**

参数项描述[const ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr串行队列属性指针。

**返回：**

类型说明FFRT_C_API [ffrt_function_header_t](../../topics/misc/ffrt_function_header_t.md)*返回串行队列超时回调方法。

#### ffrt_queue_attr_set_max_concurrency()

```ets
FFRT_C_API void ffrt_queue_attr_set_max_concurrency(ffrt_queue_attr_t* attr, const int max_concurrency)
```

**描述**

设置并行队列最大并发度。

**起始版本：** 12

**参数：**

参数项描述[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。const int max_concurrency最大并发度。

#### ffrt_queue_attr_get_max_concurrency()

```ets
FFRT_C_API int ffrt_queue_attr_get_max_concurrency(const ffrt_queue_attr_t* attr)
```

**描述**

获取并行队列最大并发度。

**起始版本：** 12

**参数：**

参数项描述[const ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。

**返回：**

类型说明FFRT_C_API int返回最大并发度。

#### ffrt_queue_attr_set_thread_mode()

```ets
FFRT_C_API void ffrt_queue_attr_set_thread_mode(ffrt_queue_attr_t* attr, bool mode)
```

**描述**

设置队列中的任务是以协程模式还是以线程模式运行。默认以协程模式运行。

**起始版本：** 20

**参数：**

参数项描述[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。bool mode设置队列任务运行方式。true表示以线程模式运行, false表示以协程方式运行。

#### ffrt_queue_attr_get_thread_mode()

```ets
FFRT_C_API bool ffrt_queue_attr_get_thread_mode(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列中的任务是以协程模式还是以线程模式运行。

**起始版本：** 20

**参数：**

参数项描述[const ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性指针。

**返回：**

类型说明FFRT_C_API booltrue表示以线程模式运行，false表示以协程模式运行。

#### ffrt_queue_create()

```ets
FFRT_C_API ffrt_queue_t ffrt_queue_create(ffrt_queue_type_t type, const char* name, const ffrt_queue_attr_t* attr)
```

**描述**

创建队列。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_type_t](queue.h.md#ZH-CN_TOPIC_0000002529285545__ffrt_queue_type_t) type队列类型。const char* name队列名字。[const ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)* attr队列属性。

**返回：**

类型说明FFRT_C_API [ffrt_queue_t](../../topics/misc/ffrt_queue_t.md)

创建队列成功返回非空队列句柄，

 创建队列失败返回空指针。

#### ffrt_queue_destroy()

```ets
FFRT_C_API void ffrt_queue_destroy(ffrt_queue_t queue)
```

**描述**

销毁队列。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_t](../../topics/misc/ffrt_queue_t.md) queue队列句柄。

#### ffrt_queue_submit()

```ets
FFRT_C_API void ffrt_queue_submit(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_t](../../topics/misc/ffrt_queue_t.md) queue队列句柄。[ffrt_function_header_t](../../topics/misc/ffrt_function_header_t.md)* f任务的执行体。[const ffrt_task_attr_t](../../topics/system-services/ffrt_task_attr_t.md)* attr任务属性。

#### ffrt_queue_submit_h()

```ets
FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行，并返回任务句柄。

**起始版本：** 10

**参数：**

参数项描述[ffrt_queue_t](../../topics/misc/ffrt_queue_t.md) queue队列句柄。[ffrt_function_header_t](../../topics/misc/ffrt_function_header_t.md)* f任务的执行体。[const ffrt_task_attr_t](../../topics/system-services/ffrt_task_attr_t.md)* attr任务属性。

**返回：**

类型说明FFRT_C_API [ffrt_task_handle_t](../../topics/system-services/ffrt_task_handle_t.md)

提交成功返回非空任务句柄，

 提交失败返回空指针。

#### ffrt_queue_submit_f()

```ets
FFRT_C_API void ffrt_queue_submit_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行，是ffrt_queue_submit接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt_queue_submit接口。

**起始版本：** 20

**参数：**

参数项描述[ffrt_queue_t](../../topics/misc/ffrt_queue_t.md) queue队列句柄。[ffrt_function_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_function_t) func指定的任务函数。void* arg传递给任务函数的参数。[const ffrt_task_attr_t](../../topics/system-services/ffrt_task_attr_t.md)* attr任务属性。

**参考：**

[ffrt_queue_submit](queue.h.md#ZH-CN_TOPIC_0000002529285545__ffrt_queue_submit)

#### ffrt_queue_submit_h_f()

```ets
FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行，并返回任务句柄，是ffrt_queue_submit_h接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt_queue_submit_h接口。

**起始版本：** 20

**参数：**

参数项描述[ffrt_queue_t](../../topics/misc/ffrt_queue_t.md) queue队列句柄。[ffrt_function_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_function_t) func指定的任务函数。void* arg传递给任务函数的参数。[const ffrt_task_attr_t](../../topics/system-services/ffrt_task_attr_t.md)* attr任务属性。

**返回：**

类型说明FFRT_C_API [ffrt_task_handle_t](../../topics/system-services/ffrt_task_handle_t.md)

提交成功返回非空任务句柄，

 提交失败返回空指针。

**参考：**

[ffrt_queue_submit_h](queue.h.md#ZH-CN_TOPIC_0000002529285545__ffrt_queue_submit_h)

#### ffrt_queue_wait()

```ets
FFRT_C_API void ffrt_queue_wait(ffrt_task_handle_t handle)
```

**描述**

等待队列中一个任务执行完成。

**起始版本：** 10

**参数：**

参数项描述[ffrt_task_handle_t](../../topics/system-services/ffrt_task_handle_t.md) handle任务句柄。

#### ffrt_queue_cancel()

```ets
FFRT_C_API int ffrt_queue_cancel(ffrt_task_handle_t handle)
```

**描述**

取消队列中一个任务。

**起始版本：** 10

**参数：**

参数项描述[ffrt_task_handle_t](../../topics/system-services/ffrt_task_handle_t.md) handle任务句柄。

**返回：**

类型说明FFRT_C_API int

取消任务成功返回0，

 取消任务失败返回-1。

#### ffrt_get_main_queue()

```ets
FFRT_C_API ffrt_queue_t ffrt_get_main_queue(void)
```

**描述**

获取主线程队列。

**起始版本：** 12

**返回：**

类型说明FFRT_C_API [ffrt_queue_t](../../topics/misc/ffrt_queue_t.md)返回主线程队列句柄。

#### ffrt_get_current_queue()

```ets
FFRT_C_API ffrt_queue_t ffrt_get_current_queue(void)
```

**描述**

获取应用Worker(ArkTs)线程队列。

**起始版本：** 12

**废弃版本：** 18

**返回：**

类型说明FFRT_C_API ffrt_queue_t返回当前线程队列句柄。