# hiappevent_event.h

**概述**

定义所有预定义事件的事件名称。除了与特定应用关联的自定义事件之外，开发者还可以使用预定义事件进行打点。

引用文件： <hiappevent/hiappevent_event.h>

库： libhiappevent_ndk.z.so

系统能力： SystemCapability.HiviewDFX.HiAppEvent

起始版本： 8

相关模块： [HiAppEvent](HiAppEvent.md)

**汇总**

**宏定义**

| 名称 | 描述 |
| --- | --- |
| EVENT_USER_LOGIN "hiappevent.user_login" | 用户登录事件。 起始版本： 8 |
| EVENT_USER_LOGOUT "hiappevent.user_logout" | 用户登出事件。 起始版本： 8 |
| EVENT_DISTRIBUTED_SERVICE_START "hiappevent.distributed_service_start" | 分布式服务事件。 起始版本： 8 |
| EVENT_APP_CRASH "APP_CRASH" | 崩溃事件。 起始版本： 12 |
| EVENT_APP_FREEZE "APP_FREEZE" | 应用冻屏事件。 起始版本： 12 |
| EVENT_APP_LAUNCH "APP_LAUNCH" | 启动耗时事件。 起始版本： 12 |
| EVENT_SCROLL_JANK "SCROLL_JANK" | 滑动丢帧事件。 起始版本： 12 |
| EVENT_CPU_USAGE_HIGH "CPU_USAGE_HIGH" | CPU高负载事件。 起始版本： 12 |
| EVENT_BATTERY_USAGE "BATTERY_USAGE" | 24h功耗器件分解统计事件。 起始版本： 12 |
| EVENT_RESOURCE_OVERLIMIT "RESOURCE_OVERLIMIT" | 资源泄漏事件。 起始版本： 12 |
| EVENT_ADDRESS_SANITIZER "ADDRESS_SANITIZER" | 地址越界事件。 起始版本： 12 |
| EVENT_MAIN_THREAD_JANK "MAIN_THREAD_JANK" | 主线程超时事件。 起始版本： 12 |
| EVENT_APP_HICOLLIE "APP_HICOLLIE" | 任务执行超时事件。 起始版本： 18 |
| EVENT_APP_KILLED "APP_KILLED" | 应用终止事件。 起始版本： 20 |
| EVENT_AUDIO_JANK_FRAME "AUDIO_JANK_FRAME" | 音频卡顿事件。 起始版本： 21 |
| DOMAIN_OS "OS" | OS作用域。 起始版本： 12 |
| EVENT_MAIN_THREAD_JANK_V2 "MAIN_THREAD_JANK_V2" | 用于设置主线程超时事件配置策略。 起始版本： 22 |

**宏定义说明**

**EVENT_USER_LOGIN**

```ets
#define EVENT_USER_LOGIN "hiappevent.user_login"
```

描述

用户登录事件。

起始版本： 8

**EVENT_USER_LOGOUT**

```ets
#define EVENT_USER_LOGOUT "hiappevent.user_logout"
```

描述

用户登出事件。

起始版本： 8

**EVENT_DISTRIBUTED_SERVICE_START**

```ets
#define EVENT_DISTRIBUTED_SERVICE_START "hiappevent.distributed_service_start"
```

描述

分布式服务事件。

起始版本： 8

**EVENT_APP_CRASH**

```ets
#define EVENT_APP_CRASH "APP_CRASH"
```

描述

崩溃事件。

起始版本： 12

**EVENT_APP_FREEZE**

```ets
#define EVENT_APP_FREEZE "APP_FREEZE"
```

描述

应用冻屏事件。

起始版本： 12

**EVENT_APP_LAUNCH**

```ets
#define EVENT_APP_LAUNCH "APP_LAUNCH"
```

描述

启动耗时事件。

起始版本： 12

**EVENT_SCROLL_JANK**

```ets
#define EVENT_SCROLL_JANK "SCROLL_JANK"
```

描述

滑动丢帧事件。

起始版本： 12

**EVENT_CPU_USAGE_HIGH**

```ets
#define EVENT_CPU_USAGE_HIGH "CPU_USAGE_HIGH"
```

描述

CPU高负载事件。

起始版本： 12

**EVENT_BATTERY_USAGE**

```ets
#define EVENT_BATTERY_USAGE "BATTERY_USAGE"
```

描述

24h功耗器件分解统计事件。

起始版本： 12

**EVENT_RESOURCE_OVERLIMIT**

```ets
#define EVENT_RESOURCE_OVERLIMIT "RESOURCE_OVERLIMIT"
```

描述

资源泄漏事件。

起始版本： 12

**EVENT_ADDRESS_SANITIZER**

```ets
#define EVENT_ADDRESS_SANITIZER "ADDRESS_SANITIZER"
```

描述

地址越界事件。

起始版本： 12

**EVENT_MAIN_THREAD_JANK**

```ets
#define EVENT_MAIN_THREAD_JANK "MAIN_THREAD_JANK"
```

描述

主线程超时事件。

起始版本： 12

**EVENT_APP_HICOLLIE**

```ets
#define EVENT_APP_HICOLLIE "APP_HICOLLIE"
```

描述

任务执行超时事件。

起始版本： 18

**EVENT_APP_KILLED**

```ets
#define EVENT_APP_KILLED "APP_KILLED"
```

描述

应用终止事件。

起始版本： 20

**EVENT_AUDIO_JANK_FRAME**

```ets
#define EVENT_AUDIO_JANK_FRAME "AUDIO_JANK_FRAME"
```

描述

音频卡顿事件。

起始版本： 21

**DOMAIN_OS**

```ets
#define DOMAIN_OS "OS"
```

描述

OS作用域。

起始版本： 12

**EVENT_MAIN_THREAD_JANK_V2**

```ets
#define EVENT_MAIN_THREAD_JANK_V2 "MAIN_THREAD_JANK_V2"
```

描述

用于设置主线程超时事件配置策略。

起始版本： 22