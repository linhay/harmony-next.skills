# application_context.h

**概述**

提供应用级别上下文相关的接口。

引用文件： <AbilityKit/ability_runtime/application_context.h>

库： libability_runtime.so

系统能力： SystemCapability.Ability.AbilityRuntime.Core

起始版本： 13

相关模块： [AbilityRuntime](AbilityRuntime.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetCacheDir(char* buffer, int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的缓存目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetAreaMode(AbilityRuntime_AreaMode* areaMode) | 获取本应用的应用级的文件数据加密等级。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetBundleName(char* buffer, int32_t bufferSize, int32_t* writeLength) | 获取应用包名。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetTempDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的临时文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetFilesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的通用文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetDatabaseDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的数据库文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetPreferencesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的首选项文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetBundleCodeDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的安装文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetDistributedFilesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的分布式文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetCloudFileDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的云文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLogFileDir(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用的应用级的日志文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetResourceDir(const char* moduleName, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取应用级别的资源目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbility(AbilityBase_Want *want) | 启动当前应用的UIAbility。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbilityWithStartOptions(AbilityBase_Want *want,AbilityRuntime_StartOptions *options) | 通过StartOptions启动当前应用的UIAbility。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetVersionCode(int64_t* versionCode) | 获取应用版本号。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbilityWithPidResult(AbilityBase_Want *want, AbilityRuntime_StartOptions *options, int32_t *targetPid) | 通过StartOptions启动当前应用的UIAbility，并获取目标UIAbility的进程号。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLaunchParameter(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用首次启动UIAbility的WantParams参数。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLatestParameter(char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取本应用最近一次启动UIAbility的WantParams参数。 |

**函数说明**

**OH_AbilityRuntime_ApplicationContextGetCacheDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetCacheDir(char* buffer, int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的缓存目录。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收本应用的应用级的缓存目录。 |
| int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetAreaMode()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetAreaMode(AbilityRuntime_AreaMode* areaMode)
```

描述

获取本应用的应用级的文件数据加密等级。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_AreaMode* areaMode | 指向接收数据加密等级的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetBundleName()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetBundleName(char* buffer, int32_t bufferSize, int32_t* writeLength)
```

描述

获取应用包名。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetTempDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetTempDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的临时文件目录。

起始版本： 16

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetFilesDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetFilesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的通用文件目录。

起始版本： 16

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetDatabaseDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetDatabaseDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的数据库文件目录。

起始版本： 16

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetPreferencesDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetPreferencesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的首选项文件目录。

起始版本： 16

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetBundleCodeDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetBundleCodeDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的安装文件目录。

起始版本： 16

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetDistributedFilesDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetDistributedFilesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的分布式文件目录。

起始版本： 16

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetCloudFileDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetCloudFileDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的云文件目录。

起始版本： 16

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetLogFileDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLogFileDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的日志文件目录。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收日志文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_ApplicationContextGetResourceDir()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetResourceDir(const char* moduleName, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用的应用级的资源目录。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| char* moduleName | 模块名。 |
| char* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

**OH_AbilityRuntime_StartSelfUIAbility()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbility(AbilityBase_Want *want)
```

描述

启动当前应用的UIAbility。

需要权限： ohos.permission.NDK_START_SELF_UI_ABILITY

起始版本： 15

设备行为差异：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回ABILITY_RUNTIME_ERROR_CODE_NOT_SUPPORTED错误码。

参数：

| 参数项 | 描述 |
| --- | --- |
| AbilityBase_Want *want | 启动当前应用UIAbility时需要的Want信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 接口调用成功。 ABILITY_RUNTIME_ERROR_CODE_PERMISSION_DENIED - 调用方权限校验失败。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 调用方入参校验失败。 ABILITY_RUNTIME_ERROR_CODE_NOT_SUPPORTED - 设备类型不支持。 ABILITY_RUNTIME_ERROR_CODE_NO_SUCH_ABILITY - 指定的Ability名称不存在。 ABILITY_RUNTIME_ERROR_CODE_INCORRECT_ABILITY_TYPE - 接口调用Ability类型错误。 ABILITY_RUNTIME_ERROR_CODE_CROWDTEST_EXPIRED - 众测应用到期。 ABILITY_RUNTIME_ERROR_CODE_WUKONG_MODE - Wukong模式，不允许启动/停止Ability。 ABILITY_RUNTIME_ERROR_CODE_CONTROLLED - 应用被管控。 ABILITY_RUNTIME_ERROR_CODE_EDM_CONTROLLED - 应用被EDM管控。 ABILITY_RUNTIME_ERROR_CODE_CROSS_APP - 限制API 11以上版本三方应用跳转。 ABILITY_RUNTIME_ERROR_CODE_INTERNAL - 内部错误。 ABILITY_RUNTIME_ERROR_CODE_NOT_TOP_ABILITY - 非顶层应用。 ABILITY_RUNTIME_ERROR_CODE_UPPER_LIMIT_REACHED - 应用多实例已达到上限（从API17开始）。 ABILITY_RUNTIME_ERROR_CODE_APP_INSTANCE_KEY_NOT_SUPPORTED - 不允许设置APP_INSTANCE_KEY（从API17开始）。 详细内容参考AbilityRuntime_ErrorCode。 |

示例代码：

```ets
#include <AbilityKit/ability_base/want.h>
#include <AbilityKit/ability_runtime/application_context.h>

void startSelfUIAbilityTest()
{
    AbilityBase_Element element;
    element.abilityName = const_cast<char*>("EntryAbility");
    element.bundleName = const_cast<char*>("com.example.myapplication");
    element.moduleName = const_cast<char*>("entry");
    AbilityBase_Want* want = OH_AbilityBase_CreateWant(element);

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_StartSelfUIAbility(want);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
        return;
    }
    // 销毁want，防止内存泄漏
    OH_AbilityBase_DestroyWant(want);
}
```

**OH_AbilityRuntime_StartSelfUIAbilityWithStartOptions()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbilityWithStartOptions(AbilityBase_Want *want,AbilityRuntime_StartOptions *options)
```

描述

通过StartOptions启动当前应用的UIAbility。

需要权限： ohos.permission.NDK_START_SELF_UI_ABILITY

起始版本： 17

设备行为差异：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回ABILITY_RUNTIME_ERROR_CODE_NOT_SUPPORTED错误码。

参数：

| 参数项 | 描述 |
| --- | --- |
| AbilityBase_Want *want | 启动当前应用UIAbility时需要的Want信息。 |
| AbilityRuntime_StartOptions *options | 启动当前应用UIAbility时需要的StartOptions信息。如果该参数中startVisibility属性的值不为空，必须确保当前应用已添加到状态栏，否则会返回ABILITY_RUNTIME_ERROR_VISIBILITY_SETTING_DISABLED错误码。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 接口调用成功。 ABILITY_RUNTIME_ERROR_CODE_PERMISSION_DENIED - 调用方权限校验失败。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 调用方入参校验失败。 ABILITY_RUNTIME_ERROR_CODE_NOT_SUPPORTED - 设备类型不支持。 ABILITY_RUNTIME_ERROR_CODE_NO_SUCH_ABILITY - 指定的Ability名称不存在。 ABILITY_RUNTIME_ERROR_CODE_INCORRECT_ABILITY_TYPE - 接口调用Ability类型错误。 ABILITY_RUNTIME_ERROR_CODE_CROWDTEST_EXPIRED - 众测应用到期。 ABILITY_RUNTIME_ERROR_CODE_WUKONG_MODE - Wukong模式，不允许启动/停止Ability。 ABILITY_RUNTIME_ERROR_CODE_CONTROLLED - 应用被管控。 ABILITY_RUNTIME_ERROR_CODE_EDM_CONTROLLED - 应用被EDM管控。 ABILITY_RUNTIME_ERROR_CODE_CROSS_APP - 限制API 11以上版本三方应用跳转。 ABILITY_RUNTIME_ERROR_CODE_INTERNAL - 内部错误。 ABILITY_RUNTIME_ERROR_CODE_NOT_TOP_ABILITY - 非顶层应用。 ABILITY_RUNTIME_ERROR_VISIBILITY_SETTING_DISABLED - 不允许设置窗口启动可见性。 ABILITY_RUNTIME_ERROR_CODE_MULTI_APP_NOT_SUPPORTED - 不支持应用分身和多实例。 ABILITY_RUNTIME_ERROR_CODE_INVALID_APP_INSTANCE_KEY - 无效多实例。  ABILITY_RUNTIME_ERROR_CODE_UPPER_LIMIT_REACHED - 应用多实例已达到上限。 ABILITY_RUNTIME_ERROR_MULTI_INSTANCE_NOT_SUPPORTED - 不支持应用多实例。 ABILITY_RUNTIME_ERROR_CODE_APP_INSTANCE_KEY_NOT_SUPPORTED - 不允许设置APP_INSTANCE_KEY。 详细内容参考AbilityRuntime_ErrorCode。 |

示例代码：

```ets
#include <AbilityKit/ability_base/want.h>
#include <AbilityKit/ability_runtime/application_context.h>

void demo()
{
    AbilityBase_Element element;
    element.abilityName = const_cast<char*>("EntryAbility");
    element.bundleName = const_cast<char*>("com.example.myapplication");
    element.moduleName = const_cast<char*>("entry");
    AbilityBase_Want* want = OH_AbilityBase_CreateWant(element);
    if (want == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理

        // 销毁want，防止内存泄漏
        OH_AbilityBase_DestroyWant(want);
        return;
    }
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_StartSelfUIAbilityWithStartOptions(want, options);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁want，防止内存泄漏
    OH_AbilityBase_DestroyWant(want);

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

**OH_AbilityRuntime_ApplicationContextGetVersionCode()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetVersionCode(int64_t* versionCode)
```

描述

获取应用版本号。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| int64_t* versionCode | 指向应用包版本号的指针，对应bundleInfo中的versionCode字段。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参versionCode为空。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 ABILITY_RUNTIME_ERROR_CODE_GET_APPLICATION_INFO_FAILED - 获取应用信息失败。 |

**OH_AbilityRuntime_StartSelfUIAbilityWithPidResult()**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbilityWithPidResult(AbilityBase_Want *want, AbilityRuntime_StartOptions *options, int32_t *targetPid)
```

描述

通过StartOptions启动当前应用的UIAbility，并获取目标UIAbility的进程号。

接口不能在应用主线程调用，但可以在应用创建的[子进程](ChildProcess.md)的主线程中调用。

如果在应用的主线程中调用，会返回ABILITY_RUNTIME_ERROR_CODE_MAIN_THREAD_NOT_SUPPORTED错误码。

需要权限： ohos.permission.NDK_START_SELF_UI_ABILITY

起始版本： 21

设备行为差异：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回ABILITY_RUNTIME_ERROR_CODE_NOT_SUPPORTED错误码。

参数：

| 参数项 | 描述 |
| --- | --- |
| AbilityBase_Want *want | 启动当前应用UIAbility时需要的Want信息。 |
| AbilityRuntime_StartOptions *options | 启动当前应用UIAbility时需要的StartOptions信息。如果该参数中startVisibility属性的值不为空，必须确保当前应用已添加到状态栏，否则会返回ABILITY_RUNTIME_ERROR_VISIBILITY_SETTING_DISABLED错误码。 |
| int32_t *targetPid | 目标UIAbility所在的进程号，作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 接口调用成功。 ABILITY_RUNTIME_ERROR_CODE_PERMISSION_DENIED - 调用方权限校验失败。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 调用方入参校验失败。 ABILITY_RUNTIME_ERROR_CODE_NOT_SUPPORTED - 设备类型不支持。 ABILITY_RUNTIME_ERROR_CODE_NO_SUCH_ABILITY - 指定的Ability名称不存在。 ABILITY_RUNTIME_ERROR_CODE_INCORRECT_ABILITY_TYPE - 接口调用Ability类型错误。 ABILITY_RUNTIME_ERROR_CODE_CROWDTEST_EXPIRED - 众测应用到期。 ABILITY_RUNTIME_ERROR_CODE_WUKONG_MODE - Wukong模式，不允许启动/停止Ability。 ABILITY_RUNTIME_ERROR_CODE_CONTROLLED - 应用被管控。 ABILITY_RUNTIME_ERROR_CODE_EDM_CONTROLLED - 应用被EDM管控。 ABILITY_RUNTIME_ERROR_CODE_CROSS_APP - 限制API 11以上版本三方应用跳转。 ABILITY_RUNTIME_ERROR_CODE_INTERNAL - 内部错误。 ABILITY_RUNTIME_ERROR_CODE_NOT_TOP_ABILITY - 非顶层应用。 ABILITY_RUNTIME_ERROR_VISIBILITY_SETTING_DISABLED - 不允许设置窗口启动可见性。 ABILITY_RUNTIME_ERROR_CODE_MULTI_APP_NOT_SUPPORTED - 不支持应用分身和多实例。 ABILITY_RUNTIME_ERROR_CODE_INVALID_APP_INSTANCE_KEY - 无效多实例。  ABILITY_RUNTIME_ERROR_CODE_UPPER_LIMIT_REACHED - 应用多实例已达到上限。 ABILITY_RUNTIME_ERROR_MULTI_INSTANCE_NOT_SUPPORTED - 不支持应用多实例。 ABILITY_RUNTIME_ERROR_CODE_APP_INSTANCE_KEY_NOT_SUPPORTED - 不允许设置APP_INSTANCE_KEY。 ABILITY_RUNTIME_ERROR_CODE_START_TIMEOUT - 启动UIAbility超时。 ABILITY_RUNTIME_ERROR_CODE_MAIN_THREAD_NOT_SUPPORTED - 接口不允许在应用主线程被调用。 |

示例代码：

```ets
#include <AbilityKit/ability_base/want.h>
#include <AbilityKit/ability_runtime/application_context.h>

void demo()
{
    AbilityBase_Element element;
    element.abilityName = const_cast<char*>("EntryAbility");
    element.bundleName = const_cast<char*>("com.example.myapplication");
    element.moduleName = const_cast<char*>("entry");
    AbilityBase_Want* want = OH_AbilityBase_CreateWant(element);
    if (want == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理

        // 销毁want，防止内存泄漏
        OH_AbilityBase_DestroyWant(want);
        return;
    }
    int32_t pid = -1;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_StartSelfUIAbilityWithPidResult(want, options, &pid);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁want，防止内存泄漏
    OH_AbilityBase_DestroyWant(want);

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

**OH_AbilityRuntime_ApplicationContextGetLaunchParameter**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLaunchParameter(
    char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用首次启动UIAbility时的WantParams参数，WantParams可参考[Want中的parameters参数](Want.md)。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收WantParams参数。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入缓冲区的字符串长度（单位：字节）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

示例：

```ets
#include "napi/native_api.h"
#include "AbilityKit/ability_runtime/application_context.h"

static napi_value GetLaunchParameter(napi_env env, napi_callback_info info)
{
    const int32_t bufferSize = 2048; // 根据实际需要调整缓冲区大小
    char buffer[bufferSize] = {0};
    int32_t writeLength = 0;
    int32_t ret = OH_AbilityRuntime_ApplicationContextGetLaunchParameter(buffer, bufferSize, &writeLength);

    if (ret != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 失败处理
    }
    // 创建 JS 字符串返回WantParams
    napi_value result;
    napi_create_string_utf8(env, buffer, writeLength, &result);
    return result;
}
```

**OH_AbilityRuntime_ApplicationContextGetLatestParameter**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLatestParameter(
    char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

描述

获取本应用最近一次启动UIAbility时的WantParams参数，WantParams可参考[Want中的parameters参数](Want.md)。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| char* buffer | 指向缓冲区的指针，用于接收WantParams参数。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入缓冲区的字符串长度（单位：字节）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 查询成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 应用上下文不存在，如在应用创建的子进程中应用级别上下文不存在。 |

示例：

```ets
#include "napi/native_api.h"
#include "AbilityKit/ability_runtime/application_context.h"

static napi_value GetLatestParameter(napi_env env, napi_callback_info info)
{
    const int32_t bufferSize = 2048; // 根据实际需要调整缓冲区大小
    char buffer[bufferSize] = {0};
    int32_t writeLength = 0;
    int32_t ret = OH_AbilityRuntime_ApplicationContextGetLatestParameter(buffer, bufferSize, &writeLength);

    if (ret != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 失败处理
    }
    // 创建 JS 字符串返回WantParams
    napi_value result;
    napi_create_string_utf8(env, buffer, writeLength, &result);
    return result;
}
```

**OH_AbilityRuntime_ApplicationContextNotifyPageChanged**

```ets
AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextNotifyPageChanged(
    const char* targetPageName, int32_t targetPageNameLength, int32_t windowId)
```

描述

该接口仅支持三方框架调用。三方框架每次切换页面时，将目标页面信息（包含目标页面路径、目标页面路径长度、目标页面对应的窗口ID）通知给系统。系统可按产品策略调整/恢复页面。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* targetPageName | 目标页面路径。 |
| int32_t targetPageNameLength | 目标页面路径长度。 |
| int32_t windowId | 目标页面对应的窗口ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参targetPageName为空或者windowId无效。 ABILITY_RUNTIME_ERROR_CODE_INTERNAL - 内部错误。 |

示例：

```ets
#include "napi/native_api.h"
#include "AbilityKit/ability_runtime/application_context.h"

static bool NotifyPageChanged(napi_env env, napi_callback_info info)
{
    const char* testPageName = "https://home.taobao.com/homepage";
    int32_t testPageNameLen = 32;
    int32_t testWindowId = 12; // 示例数值仅供参考，实际开发需使用有效的窗口ID。
    int32_t ret = OH_AbilityRuntime_ApplicationContextNotifyPageChanged(testPageName, testPageNameLen, testWindowId);

    if (ret != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 失败处理
        return false;
    }
    return true;
}
```