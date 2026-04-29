# native_audio_resource_manager.h

**概述**

声明音频资源管理相关的接口。

引用文件： <ohaudio/native_audio_resource_manager.h>

库： libohaudio.so

系统能力： SystemCapability.Multimedia.Audio.Core

起始版本： 20

相关模块： [OHAudio](OHAudio.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioResourceManager | OH_AudioResourceManager | 声明音频资源管理器。用于管理音频资源相关功能。 |
| OH_AudioWorkgroup | OH_AudioWorkgroup | 声明音频工作组。将音频关键线程进行分组管理。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_AudioCommon_Result OH_AudioManager_GetAudioResourceManager(OH_AudioResourceManager **resourceManager) | 获取音频资源管理器。  使用音频资源管理器相关功能，首先需要获取音频资源管理器实例。 |
| OH_AudioCommon_Result OH_AudioResourceManager_CreateWorkgroup(OH_AudioResourceManager *resourceManager, const char *name, OH_AudioWorkgroup **group) | 创建音频工作组。 |
| OH_AudioCommon_Result OH_AudioResourceManager_ReleaseWorkgroup(OH_AudioResourceManager *resourceManager, OH_AudioWorkgroup *group) | 释放音频工作组。 |
| OH_AudioCommon_Result OH_AudioWorkgroup_AddCurrentThread(OH_AudioWorkgroup *group, int32_t *tokenId) | 将当前线程加入group指向的音频工作组。 |
| OH_AudioCommon_Result OH_AudioWorkgroup_RemoveThread(OH_AudioWorkgroup *group, int32_t tokenId) | 将tokenId对应的线程从group音频工作组中移除。 |
| OH_AudioCommon_Result OH_AudioWorkgroup_Start(OH_AudioWorkgroup *group, uint64_t startTime, uint64_t deadlineTime) | 通知系统group指向的音频工作组开始工作，并告知系统当前工作组预期完成时间。 |
| OH_AudioCommon_Result OH_AudioWorkgroup_Stop(OH_AudioWorkgroup *group) | 通知系统group指向的音频工作组任务已完成。 |

**函数说明**

**OH_AudioManager_GetAudioResourceManager()**

```ets
OH_AudioCommon_Result OH_AudioManager_GetAudioResourceManager(OH_AudioResourceManager **resourceManager)
```

描述

获取音频资源管理器。

 使用音频资源管理器相关功能，首先需要获取音频资源管理器实例。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioResourceManager **resourceManager | 指向OH_AudioResourceManager用于接收创建的音频资源管理器实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数resourceManager为nullptr。 |

**OH_AudioResourceManager_CreateWorkgroup()**

```ets
OH_AudioCommon_Result OH_AudioResourceManager_CreateWorkgroup(OH_AudioResourceManager *resourceManager,const char *name, OH_AudioWorkgroup **group)
```

描述

创建音频工作组。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioResourceManager *resourceManager | 指向OH_AudioManager_GetAudioResourceManager创建的音频资源管理器实例OH_AudioResourceManager。 |
| const char *name | 要创建的音频工作组的名称。 |
| OH_AudioWorkgroup **group | 指向OH_AudioWorkgroup用于接收返回的音频工作组实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：  1. 参数resourceManager为nullptr;  2. 参数name为nullptr;  3. 参数group为nullptr。  AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE：创建workgroup失败，返回workgroup为nullptr。 |

**OH_AudioResourceManager_ReleaseWorkgroup()**

```ets
OH_AudioCommon_Result OH_AudioResourceManager_ReleaseWorkgroup(OH_AudioResourceManager *resourceManager,OH_AudioWorkgroup *group)
```

描述

释放音频工作组。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioResourceManager *resourceManager | 指向OH_AudioManager_GetAudioResourceManager创建的音频资源管理器实例OH_AudioResourceManager。 |
| OH_AudioWorkgroup *group | 指向OH_AudioResourceManager_CreateWorkgroup创建的音频工作组实例OH_AudioWorkgroup。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：  1. 参数resourceManager为nullptr;  2. 参数group为nullptr。  AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE：释放workgroup失败。 |

**OH_AudioWorkgroup_AddCurrentThread()**

```ets
OH_AudioCommon_Result OH_AudioWorkgroup_AddCurrentThread(OH_AudioWorkgroup *group, int32_t *tokenId)
```

描述

将当前线程加入group指向的音频工作组。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioWorkgroup *group | 指向OH_AudioResourceManager_CreateWorkgroup创建的音频工作组实例OH_AudioWorkgroup。 |
| int32_t *tokenId | 用于接收加入音频工作组的线程号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数group为nullptr。  AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE：当前线程加入分组失败。 |

**OH_AudioWorkgroup_RemoveThread()**

```ets
OH_AudioCommon_Result OH_AudioWorkgroup_RemoveThread(OH_AudioWorkgroup *group, int32_t tokenId)
```

描述

将tokenId对应的线程从group音频工作组中移除。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioWorkgroup *group | 指向OH_AudioResourceManager_CreateWorkgroup创建的音频工作组实例OH_AudioWorkgroup。 |
| int32_t tokenId | 要从音频工作组中移除的线程号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数group为nullptr。  AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE：当前线程从分组中移除失败。 |

**OH_AudioWorkgroup_Start()**

```ets
OH_AudioCommon_Result OH_AudioWorkgroup_Start(OH_AudioWorkgroup *group, uint64_t startTime, uint64_t deadlineTime)
```

描述

通知系统group指向的音频工作组开始工作，并告知系统当前工作组预期完成时间。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioWorkgroup *group | 指向OH_AudioResourceManager_CreateWorkgroup创建的音频工作组实例OH_AudioWorkgroup。 |
| uint64_t startTime | 当前音频工作组启动的时间点。 |
| uint64_t deadlineTime | 当前音频工作组预期完成的时间。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数group为nullptr。  AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE：当前工作组通知系统启动失败。 |

**OH_AudioWorkgroup_Stop()**

```ets
OH_AudioCommon_Result OH_AudioWorkgroup_Stop(OH_AudioWorkgroup *group)
```

描述

通知系统group指向的音频工作组任务已完成。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioWorkgroup *group | 指向OH_AudioResourceManager_CreateWorkgroup创建的音频工作组实例OH_AudioWorkgroup。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数group为nullptr。  AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE：当前工作组通知系统结束失败。 |