# loop.h

#### 概述

声明循环的C接口。

**引用文件：** <ffrt/loop.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 12

**相关模块：**[FFRT](../../topics/misc/FFRT.md)

#### 汇总

#### 结构体

名称描述[ffrt_loop_t](../../topics/misc/ffrt_loop_t.md)loop句柄。

#### 函数

名称描述[FFRT_C_API ffrt_loop_t ffrt_loop_create(ffrt_queue_t queue)](#ZH-CN_TOPIC_0000002497605552__ffrt_loop_create)创建loop对象。[FFRT_C_API int ffrt_loop_destroy(ffrt_loop_t loop)](#ZH-CN_TOPIC_0000002497605552__ffrt_loop_destroy)销毁loop对象。[FFRT_C_API int ffrt_loop_run(ffrt_loop_t loop)](#ZH-CN_TOPIC_0000002497605552__ffrt_loop_run)开启loop循环。[FFRT_C_API void ffrt_loop_stop(ffrt_loop_t loop)](#ZH-CN_TOPIC_0000002497605552__ffrt_loop_stop)停止loop循环。[FFRT_C_API int ffrt_loop_epoll_ctl(ffrt_loop_t loop, int op, int fd, uint32_t events, void *data, ffrt_poller_cb cb)](#ZH-CN_TOPIC_0000002497605552__ffrt_loop_epoll_ctl)管理loop上的监听事件。[FFRT_C_API ffrt_timer_t ffrt_loop_timer_start(ffrt_loop_t loop, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)](#ZH-CN_TOPIC_0000002497605552__ffrt_loop_timer_start)在ffrt loop上启动定时器。[FFRT_C_API int ffrt_loop_timer_stop(ffrt_loop_t loop, ffrt_timer_t handle)](#ZH-CN_TOPIC_0000002497605552__ffrt_loop_timer_stop)停止ffrt loop定时器。

#### 函数说明

#### ffrt_loop_create()

```ets
FFRT_C_API ffrt_loop_t ffrt_loop_create(ffrt_queue_t queue)
```

**描述**

创建loop对象。

**起始版本：** 12

**参数：**

参数项描述[ffrt_queue_t](../../topics/misc/ffrt_queue_t.md) queue并发队列。

**返回：**

类型说明FFRT_C_API [ffrt_loop_t](../../topics/misc/ffrt_loop_t.md)

创建成功返回ffrt_loop_t对象，

 创建失败返回空指针。

#### ffrt_loop_destroy()

```ets
FFRT_C_API int ffrt_loop_destroy(ffrt_loop_t loop)
```

**描述**

销毁loop对象。

**起始版本：** 12

**参数：**

参数项描述[ffrt_loop_t](../../topics/misc/ffrt_loop_t.md) looploop对象。

**返回：**

类型说明FFRT_C_API int

销毁成功返回0，

 销毁失败返回-1。

#### ffrt_loop_run()

```ets
FFRT_C_API int ffrt_loop_run(ffrt_loop_t loop)
```

**描述**

开启loop循环。

**起始版本：** 12

**参数：**

参数项描述[ffrt_loop_t](../../topics/misc/ffrt_loop_t.md) looploop对象。

**返回：**

类型说明FFRT_C_API int

loop循环失败返回-1，

 loop循环成功返回0。

#### ffrt_loop_stop()

```ets
FFRT_C_API void ffrt_loop_stop(ffrt_loop_t loop)
```

**描述**

停止loop循环。

**起始版本：** 12

**参数：**

参数项描述[ffrt_loop_t](../../topics/misc/ffrt_loop_t.md) looploop对象。

#### ffrt_loop_epoll_ctl()

```ets
FFRT_C_API int ffrt_loop_epoll_ctl(ffrt_loop_t loop, int op, int fd, uint32_t events, void *data, ffrt_poller_cb cb)
```

**描述**

管理loop上的监听事件。

不建议在cb中调用exit函数，可能导致未定义行为。

**起始版本：** 12

**参数：**

参数项描述[ffrt_loop_t](../../topics/misc/ffrt_loop_t.md) looploop对象。int opfd操作符。int fd事件描述符。uint32_t events事件。void *data事件变化时触发的回调函数的入参。[ffrt_poller_cb](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_poller_cb) cb事件变化时触发的回调函数。

**返回：**

类型说明FFRT_C_API int

成功返回0，

 失败返回-1。

#### ffrt_loop_timer_start()

```ets
FFRT_C_API ffrt_timer_t ffrt_loop_timer_start(ffrt_loop_t loop, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```

**描述**

在ffrt loop上启动定时器。

不建议在cb中调用exit函数，可能导致未定义行为。

**起始版本：** 12

**参数：**

参数项描述[ffrt_loop_t](../../topics/misc/ffrt_loop_t.md) looploop对象。uint64_t timeout超时时间(毫秒)。void* data事件变化时触发的回调函数的入参。[ffrt_timer_cb](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_timer_cb) cb事件变化时触发的回调函数。bool repeat是否重复执行该定时器。

**返回：**

类型说明FFRT_C_API [ffrt_timer_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__变量)返回定时器句柄。

#### ffrt_loop_timer_stop()

```ets
FFRT_C_API int ffrt_loop_timer_stop(ffrt_loop_t loop, ffrt_timer_t handle)
```

**描述**

停止ffrt loop定时器。

**起始版本：** 12

**参数：**

参数项描述ffrt_loop_t looploop对象。ffrt_timer_t handletimer对象。

**返回：**

类型说明FFRT_C_API int

成功返回0，

失败返回-1。