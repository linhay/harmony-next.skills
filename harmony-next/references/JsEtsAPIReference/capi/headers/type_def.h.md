# type_def.h

#### 概述

定义通用类型。

**引用文件：** <ffrt/type_def.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：**[FFRT](../../topics/misc/FFRT.md)

#### 汇总

#### 变量

名称typedef关键字描述intffrt_timer_t定时器句柄。intffrt_qos_tQoS类型。using qos = int-

QoS类型。

**起始版本：** 10

#### 结构体

名称typedef关键字描述[ffrt_function_header_t](../../topics/misc/ffrt_function_header_t.md)ffrt_function_header_t任务执行体。[ffrt_dependence_t](../../topics/misc/ffrt_dependence_t.md)ffrt_dependence_t依赖数据结构。[ffrt_deps_t](../../topics/misc/ffrt_deps_t.md)ffrt_deps_t依赖结构定义。[ffrt_task_attr_t](../../topics/system-services/ffrt_task_attr_t.md)ffrt_task_attr_t并行任务属性结构。[ffrt_queue_attr_t](../../topics/misc/ffrt_queue_attr_t.md)ffrt_queue_attr_t串行队列属性结构。[ffrt_condattr_t](../../topics/misc/ffrt_condattr_t.md)ffrt_condattr_tFFRT条件变量属性结构。[ffrt_mutexattr_t](../../topics/misc/ffrt_mutexattr_t.md)ffrt_mutexattr_tFFRT锁属性结构。[ffrt_rwlockattr_t](../../topics/misc/ffrt_rwlockattr_t.md)ffrt_rwlockattr_tFFRT读写锁属性结构。[ffrt_mutex_t](../../topics/misc/ffrt_mutex_t.md)ffrt_mutex_tFFRT互斥锁结构。[ffrt_rwlock_t](../../topics/misc/ffrt_rwlock_t.md)ffrt_rwlock_tFFRT读写锁结构。[ffrt_cond_t](../../topics/misc/ffrt_cond_t.md)ffrt_cond_tFFRT条件变量结构。void*[ffrt_task_handle_t](../../topics/system-services/ffrt_task_handle_t.md)并行任务句柄。[ffrt_fiber_t](../../topics/misc/ffrt_fiber_t.md)ffrt_fiber_t纤程结构。

#### 枚举

名称typedef关键字描述[ffrt_queue_priority_t](#ZH-CN_TOPIC_0000002497605556__ffrt_queue_priority_t)ffrt_queue_priority_t任务的优先级类型。[ffrt_qos_default_t](#ZH-CN_TOPIC_0000002497605556__ffrt_qos_default_t)ffrt_qos_default_t任务的QoS类型。[ffrt_storage_size_t](#ZH-CN_TOPIC_0000002497605556__ffrt_storage_size_t)ffrt_storage_size_t多种类型数据结构分配大小定义。[ffrt_function_kind_t](#ZH-CN_TOPIC_0000002497605556__ffrt_function_kind_t)ffrt_function_kind_t任务类型。[ffrt_dependence_type_t](#ZH-CN_TOPIC_0000002497605556__ffrt_dependence_type_t)ffrt_dependence_type_t依赖类型。[ffrt_error_t](#ZH-CN_TOPIC_0000002497605556__ffrt_error_t)ffrt_error_tFFRT错误码。[ffrt_mutex_type](#ZH-CN_TOPIC_0000002497605556__ffrt_mutex_type)ffrt_mutex_type互斥锁类型枚举。描述互斥类型，ffrt_mutex_normal是普通互斥锁；ffrt_mutex_recursive是递归互斥锁，ffrt_mutex_default是普通互斥锁。[qos_default](#ZH-CN_TOPIC_0000002497605556__qos_default)-任务QoS类型枚举。

#### 函数

名称typedef关键字描述[typedef void(*ffrt_function_t)(void*)](#ZH-CN_TOPIC_0000002497605556__ffrt_function_t)ffrt_function_t任务执行函数指针类型。[typedef void (*ffrt_poller_cb)(void* data, uint32_t event)](#ZH-CN_TOPIC_0000002497605556__ffrt_poller_cb)ffrt_poller_cbpoller回调函数定义。[typedef void (*ffrt_timer_cb)(void* data)](#ZH-CN_TOPIC_0000002497605556__ffrt_timer_cb)ffrt_timer_cbtimer回调函数定义。

#### 枚举类型说明

#### ffrt_queue_priority_t

```ets
enum ffrt_queue_priority_t
```

**描述**

任务的优先级类型。

**起始版本：** 12

枚举项描述ffrt_queue_priority_immediate = 0immediate 优先级ffrt_queue_priority_highhigh 优先级ffrt_queue_priority_lowlow 优先级ffrt_queue_priority_idlelowest 优先级

#### ffrt_qos_default_t

```ets
enum ffrt_qos_default_t
```

**描述**

任务的QoS类型。

**起始版本：** 10

枚举项描述ffrt_qos_inherit = -1继承当前任务QoS属性ffrt_qos_background后台任务ffrt_qos_utility实时工具ffrt_qos_default默认类型ffrt_qos_user_initiated用户期望

#### ffrt_storage_size_t

```ets
enum ffrt_storage_size_t
```

**描述**

多种类型数据结构分配大小定义。

**起始版本：** 10

枚举项描述ffrt_task_attr_storage_size = 128任务属性ffrt_auto_managed_function_storage_size = 64 + sizeof(ffrt_function_header_t)任务执行体ffrt_mutex_storage_size = 64互斥锁ffrt_cond_storage_size = 64条件变量ffrt_queue_attr_storage_size = 128队列属性ffrt_rwlock_storage_size = 64

读写锁

**起始版本：** 18

ffrt_fiber_storage_size

纤程在不同平台所占大小，单位：Byte。（平台相关）aarch64架构：22字节；arm架构：64字节；x86_64架构：8字节；其他平台：不支持。

**起始版本：** 20

#### ffrt_function_kind_t

```ets
enum ffrt_function_kind_t
```

**描述**

任务类型。

**起始版本：** 10

枚举项描述ffrt_function_kind_general通用任务类型ffrt_function_kind_queue队列任务类型

#### ffrt_dependence_type_t

```ets
enum ffrt_dependence_type_t
```

**描述**

依赖类型。

**起始版本：** 10

枚举项描述ffrt_dependence_data数据依赖类型ffrt_dependence_task任务依赖类型

#### ffrt_error_t

```ets
enum ffrt_error_t
```

**描述**

FFRT错误码。

**起始版本：** 10

枚举项描述ffrt_error = -1失败ffrt_success = 0成功ffrt_error_nomem = ENOMEM内存不足ffrt_error_timedout = ETIMEDOUT超时ffrt_error_busy = EBUSY重新尝试ffrt_error_inval = EINVAL值无效

#### ffrt_mutex_type

```ets
enum ffrt_mutex_type
```

**描述**

互斥锁类型枚举。描述互斥类型，ffrt_mutex_normal是普通互斥锁；ffrt_mutex_recursive是递归互斥锁，ffrt_mutex_default是普通互斥锁。

**起始版本：** 12

枚举项描述ffrt_mutex_normal = 0普通互斥锁ffrt_mutex_recursive = 2递归互斥锁ffrt_mutex_default = ffrt_mutex_normal默认互斥锁

#### qos_default

```ets
enum qos_default
```

**描述**

任务QoS类型枚举。

**起始版本：** 10

枚举项描述qos_inherit = ffrt_qos_inherit继承当前任务的QoS类型qos_background = ffrt_qos_background后台任务qos_utility = ffrt_qos_utility实时工具qos_default = ffrt_qos_default默认类型qos_user_initiated = ffrt_qos_user_initiated用户期望

#### 函数说明

#### ffrt_function_t()

```ets
typedef void(*ffrt_function_t)(void*)
```

**描述**

任务执行函数指针类型。

**起始版本：** 10

#### ffrt_poller_cb()

```ets
typedef void (*ffrt_poller_cb)(void* data, uint32_t event)
```

**描述**

poller回调函数定义。

**起始版本：** 12

#### ffrt_timer_cb()

```ets
typedef void (*ffrt_timer_cb)(void* data)
```

**描述**

timer回调函数定义。

**起始版本：** 12