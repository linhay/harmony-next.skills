# ability_runtime_common.h

#### 概述

声明AbilityRuntime模块的错误码。

**引用文件：** <AbilityKit/ability_runtime/ability_runtime_common.h>

**库：** libability_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 13

**相关模块：**[AbilityRuntime](AbilityRuntime.md)

#### 汇总

#### 枚举

名称typedef关键字描述[AbilityRuntime_ErrorCode](#ZH-CN_TOPIC_0000002497604658__abilityruntime_errorcode)AbilityRuntime_ErrorCodeAbilityRuntime模块的错误码的枚举。

#### 枚举类型说明

#### AbilityRuntime_ErrorCode

```ets
enum AbilityRuntime_ErrorCode
```

**描述**

AbilityRuntime模块的错误码的枚举。

**起始版本：** 13

枚举项描述ABILITY_RUNTIME_ERROR_CODE_NO_ERROR = 0操作成功。ABILITY_RUNTIME_ERROR_CODE_PERMISSION_DENIED = 201

权限校验失败。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID = 401无效参数。ABILITY_RUNTIME_ERROR_CODE_NOT_SUPPORTED = 801

设备类型不支持。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_NO_SUCH_ABILITY = 16000001

指定的Ability名称不存在。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_INCORRECT_ABILITY_TYPE = 16000002

接口调用Ability类型错误。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_CROWDTEST_EXPIRED = 16000008

众测应用到期。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_WUKONG_MODE = 16000009

Wukong模式，不允许启动/停止Ability。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST = 16000011上下文不存在。ABILITY_RUNTIME_ERROR_CODE_CONTROLLED = 16000012

应用被管控。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_EDM_CONTROLLED = 16000013

应用被EDM管控。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_CROSS_APP = 16000018

限制API 11以上版本三方应用跳转。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_INTERNAL = 16000050

内部错误。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_CODE_NOT_TOP_ABILITY = 16000053

非顶层应用。

**起始版本：** 15

ABILITY_RUNTIME_ERROR_VISIBILITY_SETTING_DISABLED = 16000067

不允许设置窗口启动可见性。

**起始版本：** 17

ABILITY_RUNTIME_ERROR_CODE_MULTI_APP_NOT_SUPPORTED = 16000072

不支持应用分身和多实例。

**起始版本：** 17

ABILITY_RUNTIME_ERROR_CODE_INVALID_APP_INSTANCE_KEY = 16000076

无效多实例。

**起始版本：** 17

ABILITY_RUNTIME_ERROR_CODE_UPPER_LIMIT_REACHED = 16000077

应用多实例已达到上限。

**起始版本：** 17

ABILITY_RUNTIME_ERROR_MULTI_INSTANCE_NOT_SUPPORTED = 16000078

不支持应用多实例。

**起始版本：** 17

ABILITY_RUNTIME_ERROR_CODE_APP_INSTANCE_KEY_NOT_SUPPORTED = 16000079

不允许设置APP_INSTANCE_KEY。

**起始版本：** 17

ABILITY_RUNTIME_ERROR_CODE_GET_APPLICATION_INFO_FAILED = 16000081

获取应用信息失败。

**起始版本：** 21

ABILITY_RUNTIME_ERROR_CODE_START_TIMEOUT = 16000133

启动UIAbility超时。

**起始版本：** 21

ABILITY_RUNTIME_ERROR_CODE_MAIN_THREAD_NOT_SUPPORTED = 16000134

接口不允许在应用主线程调用。

**起始版本：** 21