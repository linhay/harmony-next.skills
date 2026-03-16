# background_process_manager.h

#### 概述

本模块提供了后台子进程管控接口。开发者可以通过本模块接口对子进程进行压制、解压制，避免子进程过多占用系统资源，导致系统使用卡顿。本模块接口仅对通过OH_Ability_StartNativeChildProcess接口创建的子进程生效。

**引用文件：** <background_process_manager/background_process_manager.h>

**库：** libbackground_process_manager.z.so

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**起始版本：** 17

**相关模块：**[BackgroundProcessManager](../../topics/system-services/BackgroundProcessManager.md)

#### 汇总

#### 枚举

名称typedef关键字描述[BackgroundProcessManager_ProcessPriority](#ZH-CN_TOPIC_0000002497445268__backgroundprocessmanager_processpriority)BackgroundProcessManager_ProcessPriority子进程压制档位。[BackgroundProcessManager_ErrorCode](#ZH-CN_TOPIC_0000002497445268__backgroundprocessmanager_errorcode)BackgroundProcessManager_ErrorCode定义后台子进程管控错误码。

#### 函数

名称描述[int OH_BackgroundProcessManager_SetProcessPriority(int pid, BackgroundProcessManager_ProcessPriority priority)](#ZH-CN_TOPIC_0000002497445268__oh_backgroundprocessmanager_setprocesspriority)设置子进程的压制档位，子进程被压制后可获得的CPU资源将会受到限制。如果主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，子进程如需继续压制，需要重新调用本接口。[int OH_BackgroundProcessManager_ResetProcessPriority(int pid)](#ZH-CN_TOPIC_0000002497445268__oh_backgroundprocessmanager_resetprocesspriority)为子进程解压制，即子进程策略恢复为主进程调度策略。若主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，等效于执行一次resetProcessPriority动作。

#### 枚举类型说明

#### BackgroundProcessManager_ProcessPriority

```ets
enum BackgroundProcessManager_ProcessPriority
```

**描述**

子进程压制档位。

**起始版本：** 17

枚举项描述PROCESS_BACKGROUND = 1该档位相较PROCESS_INACTIVE压制效果更显著，获取到的CPU资源更少。推荐执行处于后台的图文页面等用户无感知业务的后台子进程时设置该档位。PROCESS_INACTIVE = 2推荐正在执行播放音频、导航等用户可感知业务的后台子进程时设置该档位。

#### BackgroundProcessManager_ErrorCode

```ets
enum BackgroundProcessManager_ErrorCode
```

**描述**

定义后台子进程管控错误码。

**起始版本：** 17

枚举项描述ERR_BACKGROUND_PROCESS_MANAGER_SUCCESS = 0压制参数发送成功。ERR_BACKGROUND_PROCESS_MANAGER_INVALID_PARAM = 401参数检查失败。ERR_BACKGROUND_PROCESS_MANAGER_REMOTE_ERROR = 31800001客户端进程请求系统服务进程，获取系统服务操作失败。

#### 函数说明

#### OH_BackgroundProcessManager_SetProcessPriority()

```ets
int OH_BackgroundProcessManager_SetProcessPriority(int pid, BackgroundProcessManager_ProcessPriority priority)
```

**描述**

设置子进程的压制档位，子进程被压制后可获得的CPU资源将会受到限制。如果主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，子进程如需继续压制，需要重新调用本接口。

**起始版本：** 17

**参数：**

参数项描述int pid需要被压制子进程的进程号，OH_Ability_StartNativeChildProcess接口创建子进程后的pid参数，即为子进程进程号。[BackgroundProcessManager_ProcessPriority](background_process_manager.h.md#ZH-CN_TOPIC_0000002497445268__backgroundprocessmanager_processpriority) priority压制档位。

**返回：**

类型说明int

返回 [ERR_BACKGROUND_PROCESS_MANAGER_SUCCESS](background_process_manager.h.md#ZH-CN_TOPIC_0000002497445268__backgroundprocessmanager_errorcode)，表示压制参数发送成功。

 返回 [ERR_BACKGROUND_PROCESS_MANAGER_INVALID_PARAM](background_process_manager.h.md#ZH-CN_TOPIC_0000002497445268__backgroundprocessmanager_errorcode)，表示参数检查失败。

#### OH_BackgroundProcessManager_ResetProcessPriority()

```ets
int OH_BackgroundProcessManager_ResetProcessPriority(int pid)
```

**描述**

为子进程解压制，即子进程策略恢复为主进程调度策略。若主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，等效于执行一次resetProcessPriority动作。

**起始版本：** 17

**参数：**

参数项描述int pid子进程的进程号，OH_Ability_StartNativeChildProcess接口创建子进程后的pid参数，即为子进程进程号。

**返回：**

类型说明int返回 [ERR_BACKGROUND_PROCESS_MANAGER_SUCCESS](background_process_manager.h.md#ZH-CN_TOPIC_0000002497445268__backgroundprocessmanager_errorcode)，表示压制参数发送成功。