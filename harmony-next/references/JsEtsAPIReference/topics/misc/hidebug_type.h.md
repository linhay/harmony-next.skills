# hidebug_type.h

**概述**

HiDebug模块代码结构体定义。

引用文件： <hidebug/hidebug_type.h>

库： libohhidebug.so

系统能力： SystemCapability.HiviewDFX.HiProfiler.HiDebug

起始版本： 12

相关模块： [HiDebug](HiDebug.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| HiDebug_ThreadCpuUsage | HiDebug_ThreadCpuUsage | 应用程序所有线程的CPU使用率结构体定义。 |
| HiDebug_SystemMemInfo | HiDebug_SystemMemInfo | 系统内存信息结构类型定义。 |
| HiDebug_NativeMemInfo | HiDebug_NativeMemInfo | 应用程序进程本机内存信息结构类型定义。 |
| HiDebug_MemoryLimit | HiDebug_MemoryLimit | 应用程序进程内存限制结构类型定义。 |
| HiDebug_JsStackFrame | HiDebug_JsStackFrame | js栈帧内容的定义。 |
| HiDebug_NativeStackFrame | HiDebug_NativeStackFrame | native栈帧内容的定义。 |
| HiDebug_StackFrame | HiDebug_StackFrame | 栈帧内容的定义。 |
| HiDebug_MallocDispatch | HiDebug_MallocDispatch | 应用程序进程可替换/恢复的HiDebug_MallocDispatch表结构类型定义。 |
| HiDebug_GraphicsMemorySummary | HiDebug_GraphicsMemorySummary | 应用图形显存占用详情的结构定义。 |
| HiDebug_ProcessSamplerConfig | HiDebug_ProcessSamplerConfig | 采样配置的结构定义。 |
| HiDebug_Backtrace_Object__* | HiDebug_Backtrace_Object | 用于栈回溯及栈解析的对象。 |
| HiDebug_ThreadCpuUsage* | HiDebug_ThreadCpuUsagePtr | HiDebug_ThreadCpuUsage指针定义。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| HiDebug_ErrorCode | HiDebug_ErrorCode | 错误码定义。 |
| HiDebug_TraceFlag | HiDebug_TraceFlag | 采集trace线程的类型。 |
| HiDebug_StackFrameType | HiDebug_StackFrameType | 栈帧类型的枚举值定义。 |
| HiDebug_CrashObjType | HiDebug_CrashObjType | 维测信息数据类型的枚举。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| HIDEBUG_TRACE_TAG_FFRT (1ULL << 13) | FFRT任务标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_COMMON_LIBRARY (1ULL << 16) | 公共库子系统标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_HDF (1ULL << 18) | HDF子系统标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_NET (1ULL << 23) | 网络标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_NWEB (1ULL << 24) | NWeb标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_AUDIO (1ULL << 27) | 分布式音频标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_FILE_MANAGEMENT (1ULL << 29) | 文件管理标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_OHOS (1ULL << 30) | OHOS通用标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_ABILITY_MANAGER (1ULL << 31) | Ability Manager标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_CAMERA (1ULL << 32) | 相机模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_MEDIA (1ULL << 33) | 媒体模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_IMAGE (1ULL << 34) | 图像模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_AUDIO (1ULL << 35) | 音频模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_DATA (1ULL << 36) | 分布式数据管理器模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_GRAPHICS (1ULL << 38) | 图形模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_ARKUI (1ULL << 39) | ArkUI开发框架标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_NOTIFICATION (1ULL << 40) | 通知模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_MISC (1ULL << 41) | MISC模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_MULTIMODAL_INPUT (1ULL << 42) | 多模态输入模块标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_RPC (1ULL << 46) | RPC标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_ARK (1ULL << 47) | JSVM虚拟机标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_WINDOW_MANAGER (1ULL << 48) | 窗口管理器标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_SCREEN (1ULL << 50) | 分布式屏幕标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_CAMERA (1ULL << 51) | 分布式相机标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_FRAMEWORK (1ULL << 52) | 分布式硬件框架标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_GLOBAL_RESOURCE_MANAGER (1ULL << 53) | 全局资源管理器标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_DEVICE_MANAGER (1ULL << 54) | 分布式硬件设备管理器标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_SAMGR (1ULL << 55) | SA标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_POWER_MANAGER (1ULL << 56) | 电源管理器标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_SCHEDULER (1ULL << 57) | 分布式调度程序标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_INPUT (1ULL << 59) | 分布式输入标签。 起始版本： 12 |
| HIDEBUG_TRACE_TAG_BLUETOOTH (1ULL << 60) | 蓝牙标签。 起始版本： 12 |

**枚举类型说明**

**HiDebug_ErrorCode**

```ets
enum HiDebug_ErrorCode
```

描述

错误码定义。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG_SUCCESS = 0 | 成功。 |
| HIDEBUG_INVALID_ARGUMENT = 401 | 无效参数，可能的原因： 1.参数传值问题；2.参数类型问题。 |
| HIDEBUG_TRACE_CAPTURED_ALREADY = 11400102 | 重复采集。 |
| HIDEBUG_NO_PERMISSION = 11400103 | 没有写文件的权限。 |
| HIDEBUG_TRACE_ABNORMAL = 11400104 | 系统内部错误。 |
| HIDEBUG_NO_TRACE_RUNNING = 11400105 | 当前没有trace正在运行。 |
| HIDEBUG_INVALID_SYMBOLIC_PC_ADDRESS = 11400200 | 传入符号解析函数的pc地址是无效的。 起始版本： 20。 |
| HIDEBUG_NOT_SUPPORTED = 11400300 | 当前设备不支持。 起始版本： 22 |
| HIDEBUG_UNDER_SAMPLING = 11400301 | 当前进程正在采样。 起始版本： 22 |
| HIDEBUG_RESOURCE_UNAVAILABLE = 11400302 | 采样资源不可用。 起始版本： 22 |

**HiDebug_TraceFlag**

```ets
enum HiDebug_TraceFlag
```

描述

采集trace线程的类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG_TRACE_FLAG_MAIN_THREAD = 1 | 只采集当前应用主线程。 |
| HIDEBUG_TRACE_FLAG_ALL_THREADS = 2 | 采集当前应用下所有线程。 |

**HiDebug_StackFrameType**

```ets
enum HiDebug_StackFrameType
```

描述

栈帧类型的枚举值定义。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG_STACK_FRAME_TYPE_JS = 1 | js类型栈帧。 |
| HIDEBUG_STACK_FRAME_TYPE_NATIVE = 2 | native类型栈帧。 |

**HiDebug_CrashObjType**

```ets
enum HiDebug_CrashObjType
```

描述

维测信息数据类型的枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| HIDEBUG_CRASHOBJ_STRING = 0 | 字符串 |
| HIDEBUG_CRASHOBJ_MEMORY_64B = 1 | 64字节内存块 |
| HIDEBUG_CRASHOBJ_MEMORY_256B = 2 | 256字节内存块 |
| HIDEBUG_CRASHOBJ_MEMORY_1024B = 3 | 1024字节内存块 |
| HIDEBUG_CRASHOBJ_MEMORY_2048B = 4 | 2048字节内存块 |
| HIDEBUG_CRASHOBJ_MEMORY_4096B = 5 | 4096字节内存块 |

**宏定义说明**

**HIDEBUG_TRACE_TAG_FFRT**

```ets
#define HIDEBUG_TRACE_TAG_FFRT (1ULL << 13)
```

描述

FFRT任务标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_COMMON_LIBRARY**

```ets
#define HIDEBUG_TRACE_TAG_COMMON_LIBRARY (1ULL << 16)
```

描述

公共库子系统标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_HDF**

```ets
#define HIDEBUG_TRACE_TAG_HDF (1ULL << 18)
```

描述

HDF子系统标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_NET**

```ets
#define HIDEBUG_TRACE_TAG_NET (1ULL << 23)
```

描述

网络标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_NWEB**

```ets
#define HIDEBUG_TRACE_TAG_NWEB (1ULL << 24)
```

描述

NWeb标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_AUDIO**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_AUDIO (1ULL << 27)
```

描述

分布式音频标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_FILE_MANAGEMENT**

```ets
#define HIDEBUG_TRACE_TAG_FILE_MANAGEMENT (1ULL << 29)
```

描述

文件管理标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_OHOS**

```ets
#define HIDEBUG_TRACE_TAG_OHOS (1ULL << 30)
```

描述

OHOS通用标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_ABILITY_MANAGER**

```ets
#define HIDEBUG_TRACE_TAG_ABILITY_MANAGER (1ULL << 31)
```

描述

Ability Manager标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_CAMERA**

```ets
#define HIDEBUG_TRACE_TAG_CAMERA (1ULL << 32)
```

描述

相机模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_MEDIA**

```ets
#define HIDEBUG_TRACE_TAG_MEDIA (1ULL << 33)
```

描述

媒体模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_IMAGE**

```ets
#define HIDEBUG_TRACE_TAG_IMAGE (1ULL << 34)
```

描述

图像模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_AUDIO**

```ets
#define HIDEBUG_TRACE_TAG_AUDIO (1ULL << 35)
```

描述

音频模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_DATA**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_DATA (1ULL << 36)
```

描述

分布式数据管理器模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_GRAPHICS**

```ets
#define HIDEBUG_TRACE_TAG_GRAPHICS (1ULL << 38)
```

描述

图形模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_ARKUI**

```ets
#define HIDEBUG_TRACE_TAG_ARKUI (1ULL << 39)
```

描述

ArkUI开发框架标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_NOTIFICATION**

```ets
#define HIDEBUG_TRACE_TAG_NOTIFICATION (1ULL << 40)
```

描述

通知模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_MISC**

```ets
#define HIDEBUG_TRACE_TAG_MISC (1ULL << 41)
```

描述

MISC模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_MULTIMODAL_INPUT**

```ets
#define HIDEBUG_TRACE_TAG_MULTIMODAL_INPUT (1ULL << 42)
```

描述

多模态输入模块标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_RPC**

```ets
#define HIDEBUG_TRACE_TAG_RPC (1ULL << 46)
```

描述

RPC标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_ARK**

```ets
#define HIDEBUG_TRACE_TAG_ARK (1ULL << 47)
```

描述

JSVM虚拟机标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_WINDOW_MANAGER**

```ets
#define HIDEBUG_TRACE_TAG_WINDOW_MANAGER (1ULL << 48)
```

描述

窗口管理器标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_SCREEN**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_SCREEN (1ULL << 50)
```

描述

分布式屏幕标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_CAMERA**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_CAMERA (1ULL << 51)
```

描述

分布式相机标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_FRAMEWORK**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_FRAMEWORK (1ULL << 52)
```

描述

分布式硬件框架标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_GLOBAL_RESOURCE_MANAGER**

```ets
#define HIDEBUG_TRACE_TAG_GLOBAL_RESOURCE_MANAGER (1ULL << 53)
```

描述

全局资源管理器标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_DEVICE_MANAGER**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_DEVICE_MANAGER (1ULL << 54)
```

描述

分布式硬件设备管理器标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_SAMGR**

```ets
#define HIDEBUG_TRACE_TAG_SAMGR (1ULL << 55)
```

描述

SA标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_POWER_MANAGER**

```ets
#define HIDEBUG_TRACE_TAG_POWER_MANAGER (1ULL << 56)
```

描述

电源管理器标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_SCHEDULER**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_SCHEDULER (1ULL << 57)
```

描述

分布式调度程序标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_DISTRIBUTED_INPUT**

```ets
#define HIDEBUG_TRACE_TAG_DISTRIBUTED_INPUT (1ULL << 59)
```

描述

分布式输入标签。

起始版本： 12

**HIDEBUG_TRACE_TAG_BLUETOOTH**

```ets
#define HIDEBUG_TRACE_TAG_BLUETOOTH (1ULL << 60)
```

描述

蓝牙标签。

起始版本： 12