# task.h

**概述**

声明任务的C接口。

引用文件： <ffrt/task.h>

库： libffrt.z.so

系统能力： SystemCapability.Resourceschedule.Ffrt.Core

起始版本： 10

相关模块： [FFRT](FFRT.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| FFRT_C_API int ffrt_task_attr_init(ffrt_task_attr_t* attr) | 初始化任务属性。 |
| FFRT_C_API void ffrt_task_attr_set_name(ffrt_task_attr_t* attr, const char* name) | 设置任务名字。 |
| FFRT_C_API const char* ffrt_task_attr_get_name(const ffrt_task_attr_t* attr) | 获取任务名字。 |
| FFRT_C_API void ffrt_task_attr_destroy(ffrt_task_attr_t* attr) | 销毁任务属性。 |
| FFRT_C_API void ffrt_task_attr_set_qos(ffrt_task_attr_t* attr, ffrt_qos_t qos) | 设置任务QoS。 |
| FFRT_C_API ffrt_qos_t ffrt_task_attr_get_qos(const ffrt_task_attr_t* attr) | 获取任务QoS。 |
| FFRT_C_API void ffrt_task_attr_set_delay(ffrt_task_attr_t* attr, uint64_t delay_us) | 设置任务延迟时间。  设置任务的调度延迟后，任务的输入输出依赖关系不再生效。 |
| FFRT_C_API uint64_t ffrt_task_attr_get_delay(const ffrt_task_attr_t* attr) | 获取任务延迟时间。 |
| FFRT_C_API void ffrt_task_attr_set_queue_priority(ffrt_task_attr_t* attr, ffrt_queue_priority_t priority) | 设置并行队列任务优先级。 |
| FFRT_C_API ffrt_queue_priority_t ffrt_task_attr_get_queue_priority(const ffrt_task_attr_t* attr) | 获取并行队列任务优先级。 |
| FFRT_C_API void ffrt_task_attr_set_stack_size(ffrt_task_attr_t* attr, uint64_t size) | 设置任务栈大小。 |
| FFRT_C_API uint64_t ffrt_task_attr_get_stack_size(const ffrt_task_attr_t* attr) | 获取任务栈大小。 |
| FFRT_C_API int ffrt_this_task_update_qos(ffrt_qos_t qos) | 更新任务QoS。 |
| FFRT_C_API ffrt_qos_t ffrt_this_task_get_qos(void) | 获取任务QoS。 |
| FFRT_C_API uint64_t ffrt_this_task_get_id(void) | 获取任务id。 |
| FFRT_C_API void *ffrt_alloc_auto_managed_function_storage_base(ffrt_function_kind_t kind) | 申请函数执行结构的内存。 |
| FFRT_C_API void ffrt_submit_base(ffrt_function_header_t* f, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr) | 提交任务调度执行。 |
| FFRT_C_API ffrt_task_handle_t ffrt_submit_h_base(ffrt_function_header_t* f, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr) | 提交任务调度执行并返回任务句柄。 |
| FFRT_C_API void ffrt_submit_f(ffrt_function_t func, void* arg, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr) | 提交任务调度执行，是ffrt_submit_base接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为通用任务结构，并将封装后的任务结构和其他参数传递给ffrt_submit_base接口。 |
| FFRT_C_API ffrt_task_handle_t ffrt_submit_h_f(ffrt_function_t func, void* arg, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr) | 提交任务调度执行并返回任务句柄，是ffrt_submit_h_base接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为通用任务结构，并将封装后的任务结构和其他参数传递给ffrt_submit_h_base接口。 |
| FFRT_C_API uint32_t ffrt_task_handle_inc_ref(ffrt_task_handle_t handle) | 增加任务句柄的引用数。 |
| FFRT_C_API uint32_t ffrt_task_handle_dec_ref(ffrt_task_handle_t handle) | 减少任务句柄的引用计数。 |
| FFRT_C_API void ffrt_task_handle_destroy(ffrt_task_handle_t handle) | 销毁任务句柄。 |
| FFRT_C_API void ffrt_wait_deps(const ffrt_deps_t* deps) | 等待依赖的任务完成，当前任务开始执行。 |
| FFRT_C_API void ffrt_wait(void) | 等待之前所有提交任务完成，当前任务开始执行。 |

**函数说明**

**ffrt_task_attr_init()**

```ets
FFRT_C_API int ffrt_task_attr_init(ffrt_task_attr_t* attr)
```

描述

初始化任务属性。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_attr_t* attr | 任务属性指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 初始化任务属性成功返回0，  初始化任务属性失败返回-1。 |

**ffrt_task_attr_set_name()**

```ets
FFRT_C_API void ffrt_task_attr_set_name(ffrt_task_attr_t* attr, const char* name)
```

描述

设置任务名字。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_attr_t* attr | 任务属性指针。 |
| const char* name | 任务名字。 |

**ffrt_task_attr_get_name()**

```ets
FFRT_C_API const char* ffrt_task_attr_get_name(const ffrt_task_attr_t* attr)
```

描述

获取任务名字。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| const ffrt_task_attr_t* attr | 任务属性指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API const char* | 获取任务名字成功返回非空指针，  获取任务名字失败返回空指针。 |

**ffrt_task_attr_destroy()**

```ets
FFRT_C_API void ffrt_task_attr_destroy(ffrt_task_attr_t* attr)
```

描述

销毁任务属性。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_attr_t* attr | 任务属性指针。 |

**ffrt_task_attr_set_qos()**

```ets
FFRT_C_API void ffrt_task_attr_set_qos(ffrt_task_attr_t* attr, ffrt_qos_t qos)
```

描述

设置任务QoS。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_attr_t* attr | 任务属性指针。 |
| ffrt_qos_t qos | 任务QoS。 |

**ffrt_task_attr_get_qos()**

```ets
FFRT_C_API ffrt_qos_t ffrt_task_attr_get_qos(const ffrt_task_attr_t* attr)
```

描述

获取任务QoS。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| const ffrt_task_attr_t* attr | 任务属性指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_qos_t | 返回任务的QoS，默认返回ffrt_qos_default。 |

**ffrt_task_attr_set_delay()**

```ets
FFRT_C_API void ffrt_task_attr_set_delay(ffrt_task_attr_t* attr, uint64_t delay_us)
```

描述

设置任务延迟时间。

设置任务的调度延迟后，任务的输入输出依赖关系不再生效。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_attr_t* attr | 任务属性指针。 |
| uint64_t delay_us | 任务延迟时间，单位微秒。 |

**ffrt_task_attr_get_delay()**

```ets
FFRT_C_API uint64_t ffrt_task_attr_get_delay(const ffrt_task_attr_t* attr)
```

描述

获取任务延迟时间。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| const ffrt_task_attr_t* attr | 任务属性指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API uint64_t | 返回任务的延迟时间。 |

**ffrt_task_attr_set_queue_priority()**

```ets
FFRT_C_API void ffrt_task_attr_set_queue_priority(ffrt_task_attr_t* attr, ffrt_queue_priority_t priority)
```

描述

设置并行队列任务优先级。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_attr_t* attr | 任务属性指针。 |
| ffrt_queue_priority_t priority | 任务优先级。 |

**ffrt_task_attr_get_queue_priority()**

```ets
FFRT_C_API ffrt_queue_priority_t ffrt_task_attr_get_queue_priority(const ffrt_task_attr_t* attr)
```

描述

获取并行队列任务优先级。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ffrt_task_attr_t* attr | 任务属性指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_queue_priority_t | 返回任务优先级。 |

**ffrt_task_attr_set_stack_size()**

```ets
FFRT_C_API void ffrt_task_attr_set_stack_size(ffrt_task_attr_t* attr, uint64_t size)
```

描述

设置任务栈大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_attr_t* attr | 任务属性指针。 |
| uint64_t size | 任务栈大小，单位是字节。 |

**ffrt_task_attr_get_stack_size()**

```ets
FFRT_C_API uint64_t ffrt_task_attr_get_stack_size(const ffrt_task_attr_t* attr)
```

描述

获取任务栈大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ffrt_task_attr_t* attr | 任务属性指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API uint64_t | 返回任务栈大小，单位是字节。 |

**ffrt_this_task_update_qos()**

```ets
FFRT_C_API int ffrt_this_task_update_qos(ffrt_qos_t qos)
```

描述

更新任务QoS。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_qos_t qos | 当前任务待更新的QoS。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 更新任务QoS成功返回0，  更新任务QoS失败返回-1。 |

**ffrt_this_task_get_qos()**

```ets
FFRT_C_API ffrt_qos_t ffrt_this_task_get_qos(void)
```

描述

获取任务QoS。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_qos_t | 返回任务QoS。 |

**ffrt_this_task_get_id()**

```ets
FFRT_C_API uint64_t ffrt_this_task_get_id(void)
```

描述

获取任务id。

起始版本： 10

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API uint64_t | 返回当前任务的id。 |

**ffrt_alloc_auto_managed_function_storage_base()**

```ets
FFRT_C_API void *ffrt_alloc_auto_managed_function_storage_base(ffrt_function_kind_t kind)
```

描述

申请函数执行结构的内存。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_function_kind_t kind | 函数执行结构类型，支持通用和队列函数执行结构类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API void * | 申请函数执行结构成功返回非空指针，  申请函数执行结构失败返回空指针。 |

**ffrt_submit_base()**

```ets
FFRT_C_API void ffrt_submit_base(ffrt_function_header_t* f, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr)
```

描述

提交任务调度执行。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_function_header_t* f | 任务执行体封装的指针。 |
| const ffrt_deps_t* in_deps | 输入依赖指针。 |
| const ffrt_deps_t* out_deps | 输出依赖指针。 |
| const ffrt_task_attr_t* attr | 任务属性。 |

**ffrt_submit_h_base()**

```ets
FFRT_C_API ffrt_task_handle_t ffrt_submit_h_base(ffrt_function_header_t* f, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr)
```

描述

提交任务调度执行并返回任务句柄。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_function_header_t* f | 任务执行体封装的指针。 |
| const ffrt_deps_t* in_deps | 输入依赖指针。 |
| const ffrt_deps_t* out_deps | 输出依赖指针。 |
| const ffrt_task_attr_t* attr | 任务属性。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_task_handle_t | 提交任务成功返回非空任务句柄，  提交任务失败返回空指针。 |

**ffrt_submit_f()**

```ets
FFRT_C_API void ffrt_submit_f(ffrt_function_t func, void* arg, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr)
```

描述

提交任务调度执行，是ffrt_submit_base接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为通用任务结构，并将封装后的任务结构和其他参数传递给ffrt_submit_base接口。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_function_t func | 指定的任务函数。 |
| void* arg | 传递给任务函数的参数。 |
| const ffrt_deps_t* in_deps | 输入依赖指针。 |
| const ffrt_deps_t* out_deps | 输出依赖指针。 |
| const ffrt_task_attr_t* attr | 任务属性。 |

参考：

[ffrt_submit_base](task.h.md#ZH-CN_TOPIC_0000002522081656__ffrt_submit_base)

**ffrt_submit_h_f()**

```ets
FFRT_C_API ffrt_task_handle_t ffrt_submit_h_f(ffrt_function_t func, void* arg, const ffrt_deps_t* in_deps, const ffrt_deps_t* out_deps, const ffrt_task_attr_t* attr)
```

描述

提交任务调度执行并返回任务句柄，是ffrt_submit_h_base接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为通用任务结构，并将封装后的任务结构和其他参数传递给ffrt_submit_h_base接口。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_function_t func | 指定的任务函数。 |
| void* arg | 传递给任务函数的参数。 |
| const ffrt_deps_t* in_deps | 输入依赖指针。 |
| const ffrt_deps_t* out_deps | 输出依赖指针。 |
| const ffrt_task_attr_t* attr | 任务属性。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_task_handle_t | 提交任务成功返回非空任务句柄，  提交任务失败返回空指针。 |

参考：

[ffrt_submit_h_base](task.h.md#ZH-CN_TOPIC_0000002522081656__ffrt_submit_h_base)

**ffrt_task_handle_inc_ref()**

```ets
FFRT_C_API uint32_t ffrt_task_handle_inc_ref(ffrt_task_handle_t handle)
```

描述

增加任务句柄的引用数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_handle_t handle | 任务句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API uint32_t | 返回任务句柄原始引用计数。 |

**ffrt_task_handle_dec_ref()**

```ets
FFRT_C_API uint32_t ffrt_task_handle_dec_ref(ffrt_task_handle_t handle)
```

描述

减少任务句柄的引用计数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_handle_t handle | 任务句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FFRT_C_API uint32_t | 返回任务句柄原始引用计数。 |

**ffrt_task_handle_destroy()**

```ets
FFRT_C_API void ffrt_task_handle_destroy(ffrt_task_handle_t handle)
```

描述

销毁任务句柄。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| ffrt_task_handle_t handle | 任务句柄。 |

**ffrt_wait_deps()**

```ets
FFRT_C_API void ffrt_wait_deps(const ffrt_deps_t* deps)
```

描述

等待依赖的任务完成，当前任务开始执行。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| const ffrt_deps_t* deps | 依赖的指针。 |

**ffrt_wait()**

```ets
FFRT_C_API void ffrt_wait(void)
```

描述

等待之前所有提交任务完成，当前任务开始执行。

起始版本： 10