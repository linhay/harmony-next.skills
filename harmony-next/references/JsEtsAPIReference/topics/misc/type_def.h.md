# type_def.h

**概述**

定义通用类型。

引用文件： <ffrt/type_def.h>

库： libffrt.z.so

系统能力： SystemCapability.Resourceschedule.Ffrt.Core

起始版本： 10

相关模块： [FFRT](FFRT.md)

**汇总**

**变量**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| int | ffrt_timer_t | 定时器句柄。 |
| int | ffrt_qos_t | QoS类型。 |
| using qos = int | - | QoS类型。 起始版本： 10 |

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ffrt_function_header_t | ffrt_function_header_t | 任务执行体。 |
| ffrt_dependence_t | ffrt_dependence_t | 依赖数据结构。 |
| ffrt_deps_t | ffrt_deps_t | 依赖结构定义。 |
| ffrt_task_attr_t | ffrt_task_attr_t | 并行任务属性结构。 |
| ffrt_queue_attr_t | ffrt_queue_attr_t | 串行队列属性结构。 |
| ffrt_condattr_t | ffrt_condattr_t | FFRT条件变量属性结构。 |
| ffrt_mutexattr_t | ffrt_mutexattr_t | FFRT锁属性结构。 |
| ffrt_rwlockattr_t | ffrt_rwlockattr_t | FFRT读写锁属性结构。 |
| ffrt_mutex_t | ffrt_mutex_t | FFRT互斥锁结构。 |
| ffrt_rwlock_t | ffrt_rwlock_t | FFRT读写锁结构。 |
| ffrt_cond_t | ffrt_cond_t | FFRT条件变量结构。 |
| void* | ffrt_task_handle_t | 并行任务句柄。 |
| ffrt_fiber_t | ffrt_fiber_t | 纤程结构。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ffrt_queue_priority_t | ffrt_queue_priority_t | 任务的优先级类型。 |
| ffrt_qos_default_t | ffrt_qos_default_t | 任务的QoS类型。 |
| ffrt_storage_size_t | ffrt_storage_size_t | 多种类型数据结构分配大小定义。 |
| ffrt_function_kind_t | ffrt_function_kind_t | 任务类型。 |
| ffrt_dependence_type_t | ffrt_dependence_type_t | 依赖类型。 |
| ffrt_error_t | ffrt_error_t | FFRT错误码。 |
| ffrt_mutex_type | ffrt_mutex_type | 互斥锁类型枚举。描述互斥类型，ffrt_mutex_normal是普通互斥锁；ffrt_mutex_recursive是递归互斥锁，ffrt_mutex_default是普通互斥锁。 |
| qos_default | - | 任务QoS类型枚举。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void(*ffrt_function_t)(void*) | ffrt_function_t | 任务执行函数指针类型。 |
| typedef void (*ffrt_poller_cb)(void* data, uint32_t event) | ffrt_poller_cb | poller回调函数定义。 |
| typedef void (*ffrt_timer_cb)(void* data) | ffrt_timer_cb | timer回调函数定义。 |

**枚举类型说明**

**ffrt_queue_priority_t**

```ets
enum ffrt_queue_priority_t
```

描述

任务的优先级类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt_queue_priority_immediate = 0 | immediate 优先级 |
| ffrt_queue_priority_high | high 优先级 |
| ffrt_queue_priority_low | low 优先级 |
| ffrt_queue_priority_idle | lowest 优先级 |

**ffrt_qos_default_t**

```ets
enum ffrt_qos_default_t
```

描述

任务的QoS类型。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt_qos_inherit = -1 | 继承当前任务QoS属性 |
| ffrt_qos_background | 后台任务 |
| ffrt_qos_utility | 实时工具 |
| ffrt_qos_default | 默认类型 |
| ffrt_qos_user_initiated | 用户期望 |
| ffrt_qos_deadline_request | 时限请求 起始版本： 23 |
| ffrt_qos_user_interactive | 用户交互 起始版本： 23 |
| ffrt_qos_max = ffrt_qos_user_interactive | 最高QoS等级 起始版本： 23 |

**ffrt_storage_size_t**

```ets
enum ffrt_storage_size_t
```

描述

多种类型数据结构分配大小定义。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt_task_attr_storage_size = 128 | 任务属性 |
| ffrt_auto_managed_function_storage_size = 64 + sizeof(ffrt_function_header_t) | 任务执行体 |
| ffrt_mutex_storage_size = 64 | 互斥锁 |
| ffrt_cond_storage_size = 64 | 条件变量 |
| ffrt_queue_attr_storage_size = 128 | 队列属性 |
| ffrt_rwlock_storage_size = 64 | 读写锁 起始版本： 18 |
| ffrt_fiber_storage_size | 纤程在不同平台所占大小，单位：Byte。（平台相关）aarch64架构：22字节；arm架构：64字节；x86_64架构：8字节；其他平台：不支持。 起始版本： 20 |

**ffrt_function_kind_t**

```ets
enum ffrt_function_kind_t
```

描述

任务类型。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt_function_kind_general | 通用任务类型 |
| ffrt_function_kind_queue | 队列任务类型 |

**ffrt_dependence_type_t**

```ets
enum ffrt_dependence_type_t
```

描述

依赖类型。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt_dependence_data | 数据依赖类型 |
| ffrt_dependence_task | 任务依赖类型 |

**ffrt_error_t**

```ets
enum ffrt_error_t
```

描述

FFRT错误码。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt_error = -1 | 失败 |
| ffrt_success = 0 | 成功 |
| ffrt_error_nomem = ENOMEM | 内存不足 |
| ffrt_error_timedout = ETIMEDOUT | 超时 |
| ffrt_error_busy = EBUSY | 重新尝试 |
| ffrt_error_inval = EINVAL | 值无效 |

**ffrt_mutex_type**

```ets
enum ffrt_mutex_type
```

描述

互斥锁类型枚举。描述互斥类型，ffrt_mutex_normal是普通互斥锁；ffrt_mutex_recursive是递归互斥锁，ffrt_mutex_default是普通互斥锁。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt_mutex_normal = 0 | 普通互斥锁 |
| ffrt_mutex_recursive = 2 | 递归互斥锁 |
| ffrt_mutex_default = ffrt_mutex_normal | 默认互斥锁 |

**qos_default**

```ets
enum qos_default
```

描述

任务QoS类型枚举。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| qos_inherit = ffrt_qos_inherit | 继承当前任务的QoS类型 |
| qos_background = ffrt_qos_background | 后台任务 |
| qos_utility = ffrt_qos_utility | 实时工具 |
| qos_default = ffrt_qos_default | 默认类型 |
| qos_user_initiated = ffrt_qos_user_initiated | 用户期望 |
| qos_deadline_request = ffrt_qos_deadline_request | 时限请求 起始版本： 23 |
| qos_user_interactive = ffrt_qos_user_interactive | 用户交互 起始版本： 23 |
| qos_max = ffrt_qos_user_interactive | 最高QoS等级 起始版本： 23 |

**函数说明**

**ffrt_function_t()**

```ets
typedef void(*ffrt_function_t)(void*)
```

描述

任务执行函数指针类型。

起始版本： 10

**ffrt_poller_cb()**

```ets
typedef void (*ffrt_poller_cb)(void* data, uint32_t event)
```

描述

poller回调函数定义。

起始版本： 12

**ffrt_timer_cb()**

```ets
typedef void (*ffrt_timer_cb)(void* data)
```

描述

timer回调函数定义。

起始版本： 12