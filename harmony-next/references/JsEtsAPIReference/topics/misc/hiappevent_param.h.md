# hiappevent_param.h

**概述**

定义所有预定义事件的参数名称。除了与特定应用关联的自定义事件之外，开发者还可以使用预定义事件进行打点。

引用文件： <hiappevent/hiappevent_param.h>

库： libhiappevent_ndk.z.so

系统能力： SystemCapability.HiviewDFX.HiAppEvent

起始版本： 8

相关模块： [HiAppEvent](HiAppEvent.md)

**汇总**

**宏定义**

| 名称 | 描述 |
| --- | --- |
| PARAM_USER_ID "user_id" | 用户ID。 起始版本： 8 |
| PARAM_DISTRIBUTED_SERVICE_NAME "ds_name" | 分布式服务名称。 起始版本： 8 |
| PARAM_DISTRIBUTED_SERVICE_INSTANCE_ID "ds_instance_id" | 分布式服务实例ID。 起始版本： 8 |
| MAIN_THREAD_JANK_PARAM_LOG_TYPE "log_type" | 用于MAIN_THREAD_JANK_V2事件，主线程超时检测采集日志的类型。 起始版本： 22 |
| MAIN_THREAD_JANK_PARAM_SAMPLE_INTERVAL "sample_interval" | 用于MAIN_THREAD_JANK_V2事件，主线程超时检测间隔和采样间隔。 起始版本： 22 |
| MAIN_THREAD_JANK_PARAM_IGNORE_STARTUP_TIME "ignore_startup_time" | 用于MAIN_THREAD_JANK_V2事件，应用启动期间忽略主线程超时检测的时间。 起始版本： 22 |
| MAIN_THREAD_JANK_PARAM_SAMPLE_COUNT "sample_count" | 用于MAIN_THREAD_JANK_V2事件，主线程超时检测的采样栈的次数。 起始版本： 22 |
| MAIN_THREAD_JANK_PARAM_REPORT_TIMES_PER_APP "report_times_per_app" | 用于MAIN_THREAD_JANK_V2事件，每个应用PID一个生命周期内，主线程超时采样上报的次数，一个生命周期内只能设置一次。 起始版本： 22 |
| MAIN_THREAD_JANK_PARAM_AUTO_STOP_SAMPLING "auto_stop_sampling" | 用于MAIN_THREAD_JANK_V2事件，主线程超时结束时，是否停止采样主线程堆栈。 起始版本： 22 |

**宏定义说明**

**PARAM_USER_ID**

```ets
#define PARAM_USER_ID "user_id"
```

描述

用户ID。

起始版本： 8

**PARAM_DISTRIBUTED_SERVICE_NAME**

```ets
#define PARAM_DISTRIBUTED_SERVICE_NAME "ds_name"
```

描述

分布式服务名称。

起始版本： 8

**PARAM_DISTRIBUTED_SERVICE_INSTANCE_ID**

```ets
#define PARAM_DISTRIBUTED_SERVICE_INSTANCE_ID "ds_instance_id"
```

描述

分布式服务实例ID。

起始版本： 8

**MAIN_THREAD_JANK_PARAM_LOG_TYPE**

```ets
#define MAIN_THREAD_JANK_PARAM_LOG_TYPE "log_type"
```

描述

用于MAIN_THREAD_JANK_V2事件，主线程超时检测采集日志的类型。

起始版本： 22

**MAIN_THREAD_JANK_PARAM_SAMPLE_INTERVAL**

```ets
#define MAIN_THREAD_JANK_PARAM_SAMPLE_INTERVAL "sample_interval"
```

描述

用于MAIN_THREAD_JANK_V2事件，主线程超时检测间隔和采样间隔。

起始版本： 22

**MAIN_THREAD_JANK_PARAM_IGNORE_STARTUP_TIME**

```ets
#define MAIN_THREAD_JANK_PARAM_IGNORE_STARTUP_TIME "ignore_startup_time"
```

描述

用于MAIN_THREAD_JANK_V2事件，应用启动期间忽略主线程超时检测的时间。

起始版本： 22

**MAIN_THREAD_JANK_PARAM_SAMPLE_COUNT**

```ets
#define MAIN_THREAD_JANK_PARAM_SAMPLE_COUNT "sample_count"
```

描述

用于MAIN_THREAD_JANK_V2事件，主线程超时检测的采样栈的次数。

起始版本： 22

**MAIN_THREAD_JANK_PARAM_REPORT_TIMES_PER_APP**

```ets
#define MAIN_THREAD_JANK_PARAM_REPORT_TIMES_PER_APP "report_times_per_app"
```

描述

用于MAIN_THREAD_JANK_V2事件，每个应用PID一个生命周期内，主线程超时采样上报的次数，一个生命周期内只能设置一次。

起始版本： 22

**MAIN_THREAD_JANK_PARAM_AUTO_STOP_SAMPLING**

```ets
#define MAIN_THREAD_JANK_PARAM_AUTO_STOP_SAMPLING "auto_stop_sampling"
```

描述

用于MAIN_THREAD_JANK_V2事件，是否停止采样主线程堆栈。

起始版本： 22