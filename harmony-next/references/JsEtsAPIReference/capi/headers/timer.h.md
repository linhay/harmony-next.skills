# timer.h

#### 概述

声明定时器的C接口。

**引用文件：** <ffrt/timer.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 12

**相关模块：**[FFRT](../../topics/misc/FFRT.md)

#### 汇总

#### 函数

名称描述[FFRT_C_API ffrt_timer_t ffrt_timer_start(ffrt_qos_t qos, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)](#ZH-CN_TOPIC_0000002529285547__ffrt_timer_start)启动计时器。[FFRT_C_API int ffrt_timer_stop(ffrt_qos_t qos, ffrt_timer_t handle)](#ZH-CN_TOPIC_0000002529285547__ffrt_timer_stop)关闭计时器。

#### 函数说明

#### ffrt_timer_start()

```ets
FFRT_C_API ffrt_timer_t ffrt_timer_start(ffrt_qos_t qos, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```

**描述**

启动计时器。

不建议在cb中调用exit函数，可能导致未定义行为。

**起始版本：** 12

**参数：**

参数项描述[ffrt_qos_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__变量) qosQoS等级。uint64_t timeout超时时间(毫秒)。void* data超时后回调函数的入参。[ffrt_timer_cb](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_timer_cb) cb超时执行的回调函数。bool repeat是否重复执行该定时器（该功能暂未支持）。

**返回：**

类型说明FFRT_C_API [ffrt_timer_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__变量)返回定时器句柄。

#### ffrt_timer_stop()

```ets
FFRT_C_API int ffrt_timer_stop(ffrt_qos_t qos, ffrt_timer_t handle)
```

**描述**

关闭计时器。

**起始版本：** 12

**参数：**

参数项描述ffrt_qos_t qosQoS等级。ffrt_timer_t handle定时器句柄。

**返回：**

类型说明FFRT_C_API int

关闭成功返回0，

 关闭失败返回-1。