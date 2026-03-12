# hiappevent_event.h

#### 概述

定义所有预定义事件的事件名称。除了与特定应用关联的自定义事件之外，开发者还可以使用预定义事件进行打点。

**引用文件：** <hiappevent/hiappevent_event.h>

**库：** libhiappevent_ndk.z.so

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 8

**相关模块：**[HiAppEvent](HiAppEvent.md)

#### 汇总

#### 宏定义

名称描述[EVENT_USER_LOGIN](#ZH-CN_TOPIC_0000002529285661__event_user_login) "hiappevent.user_login"

用户登录事件。

**起始版本：** 8

[EVENT_USER_LOGOUT](#ZH-CN_TOPIC_0000002529285661__event_user_logout) "hiappevent.user_logout"

用户登出事件。

**起始版本：** 8

[EVENT_DISTRIBUTED_SERVICE_START](#ZH-CN_TOPIC_0000002529285661__event_distributed_service_start) "hiappevent.distributed_service_start"

分布式服务事件。

**起始版本：** 8

[EVENT_APP_CRASH](#ZH-CN_TOPIC_0000002529285661__event_app_crash) "APP_CRASH"

崩溃事件。

**起始版本：** 12

[EVENT_APP_FREEZE](#ZH-CN_TOPIC_0000002529285661__event_app_freeze) "APP_FREEZE"

应用冻屏事件。

**起始版本：** 12

[EVENT_APP_LAUNCH](#ZH-CN_TOPIC_0000002529285661__event_app_launch) "APP_LAUNCH"

启动耗时事件。

**起始版本：** 12

[EVENT_SCROLL_JANK](#ZH-CN_TOPIC_0000002529285661__event_scroll_jank) "SCROLL_JANK"

滑动丢帧事件。

**起始版本：** 12

[EVENT_CPU_USAGE_HIGH](#ZH-CN_TOPIC_0000002529285661__event_cpu_usage_high) "CPU_USAGE_HIGH"

CPU高负载事件。

**起始版本：** 12

[EVENT_BATTERY_USAGE](#ZH-CN_TOPIC_0000002529285661__event_battery_usage) "BATTERY_USAGE"

24h功耗器件分解统计事件。

**起始版本：** 12

[EVENT_RESOURCE_OVERLIMIT](#ZH-CN_TOPIC_0000002529285661__event_resource_overlimit) "RESOURCE_OVERLIMIT"

资源泄漏事件。

**起始版本：** 12

[EVENT_ADDRESS_SANITIZER](#ZH-CN_TOPIC_0000002529285661__event_address_sanitizer) "ADDRESS_SANITIZER"

地址越界事件。

**起始版本：** 12

[EVENT_MAIN_THREAD_JANK](#ZH-CN_TOPIC_0000002529285661__event_main_thread_jank) "MAIN_THREAD_JANK"

主线程超时事件。

**起始版本：** 12

[EVENT_APP_HICOLLIE](#ZH-CN_TOPIC_0000002529285661__event_app_hicollie) "APP_HICOLLIE"

任务执行超时事件。

**起始版本：** 18

[EVENT_APP_KILLED](#ZH-CN_TOPIC_0000002529285661__event_app_killed) "APP_KILLED"

应用终止事件。

**起始版本：** 20

[EVENT_AUDIO_JANK_FRAME](#ZH-CN_TOPIC_0000002529285661__event_audio_jank_frame) "AUDIO_JANK_FRAME"

音频卡顿事件。

**起始版本：** 21

[DOMAIN_OS](#ZH-CN_TOPIC_0000002529285661__domain_os) "OS"

OS作用域。

**起始版本：** 12

#### 宏定义说明

#### EVENT_USER_LOGIN

```ets
#define EVENT_USER_LOGIN "hiappevent.user_login"
```

**描述**

用户登录事件。

**起始版本：** 8

#### EVENT_USER_LOGOUT

```ets
#define EVENT_USER_LOGOUT "hiappevent.user_logout"
```

**描述**

用户登出事件。

**起始版本：** 8

#### EVENT_DISTRIBUTED_SERVICE_START

```ets
#define EVENT_DISTRIBUTED_SERVICE_START "hiappevent.distributed_service_start"
```

**描述**

分布式服务事件。

**起始版本：** 8

#### EVENT_APP_CRASH

```ets
#define EVENT_APP_CRASH "APP_CRASH"
```

**描述**

崩溃事件。

**起始版本：** 12

#### EVENT_APP_FREEZE

```ets
#define EVENT_APP_FREEZE "APP_FREEZE"
```

**描述**

应用冻屏事件。

**起始版本：** 12

#### EVENT_APP_LAUNCH

```ets
#define EVENT_APP_LAUNCH "APP_LAUNCH"
```

**描述**

启动耗时事件。

**起始版本：** 12

#### EVENT_SCROLL_JANK

```ets
#define EVENT_SCROLL_JANK "SCROLL_JANK"
```

**描述**

滑动丢帧事件。

**起始版本：** 12

#### EVENT_CPU_USAGE_HIGH

```ets
#define EVENT_CPU_USAGE_HIGH "CPU_USAGE_HIGH"
```

**描述**

CPU高负载事件。

**起始版本：** 12

#### EVENT_BATTERY_USAGE

```ets
#define EVENT_BATTERY_USAGE "BATTERY_USAGE"
```

**描述**

24h功耗器件分解统计事件。

**起始版本：** 12

#### EVENT_RESOURCE_OVERLIMIT

```ets
#define EVENT_RESOURCE_OVERLIMIT "RESOURCE_OVERLIMIT"
```

**描述**

资源泄漏事件。

**起始版本：** 12

#### EVENT_ADDRESS_SANITIZER

```ets
#define EVENT_ADDRESS_SANITIZER "ADDRESS_SANITIZER"
```

**描述**

地址越界事件。

**起始版本：** 12

#### EVENT_MAIN_THREAD_JANK

```ets
#define EVENT_MAIN_THREAD_JANK "MAIN_THREAD_JANK"
```

**描述**

主线程超时事件。

**起始版本：** 12

#### EVENT_APP_HICOLLIE

```ets
#define EVENT_APP_HICOLLIE "APP_HICOLLIE"
```

**描述**

任务执行超时事件。

**起始版本：** 18

#### EVENT_APP_KILLED

```ets
#define EVENT_APP_KILLED "APP_KILLED"
```

**描述**

应用终止事件。

**起始版本：** 20

#### EVENT_AUDIO_JANK_FRAME

```ets
#define EVENT_AUDIO_JANK_FRAME "AUDIO_JANK_FRAME"
```

**描述**

音频卡顿事件。

**起始版本：** 21

#### DOMAIN_OS

```ets
#define DOMAIN_OS "OS"
```

**描述**

OS作用域。

**起始版本：** 12