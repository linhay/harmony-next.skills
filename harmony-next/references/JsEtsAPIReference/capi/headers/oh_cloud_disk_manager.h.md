# oh_cloud_disk_manager.h

#### 概述

云盘管理模块的接口定义。

**引用文件：** <filemanagement/cloud_disk_manager/oh_cloud_disk_manager.h>

**库：** libohclouddiskmanager.so

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**起始版本：** 21

**相关模块：**[CloudDisk](../../topics/networking/CloudDisk.md)

#### 汇总

#### 结构体

名称typedef关键字描述[CloudDisk_PathInfo](../../topics/graphics/CloudDisk_PathInfo.md)CloudDisk_PathInfo文件路径信息。[CloudDisk_FileSyncState](../../topics/networking/CloudDisk_FileSyncState.md)CloudDisk_FileSyncState文件的同步状态。[CloudDisk_ChangeData](../../topics/networking/CloudDisk_ChangeData.md)CloudDisk_ChangeData定义了同步根路径下单个文件变更事件的数据结构。该结构包含有关文件变更的详细信息，包括唯一ID、父目录的唯一ID、相对路径、变更类型、文件大小和时间戳。[CloudDisk_ChangesResult](../../topics/networking/CloudDisk_ChangesResult.md)CloudDisk_ChangesResult查询同步根路径中文件变更的结果。该结构体包含同步根路径中文件的变更数据，包括下一个更新序列号、结尾标志以及变更数据项数组。[CloudDisk_FailedList](../../topics/components/CloudDisk_FailedList.md)CloudDisk_FailedList同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。[CloudDisk_ResultList](../../topics/components/CloudDisk_ResultList.md)CloudDisk_ResultList表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。[CloudDisk_DisplayNameInfo](../../topics/networking/CloudDisk_DisplayNameInfo.md)CloudDisk_DisplayNameInfo定义同步根路径的显示名称信息。[CloudDisk_SyncFolder](../../topics/networking/CloudDisk_SyncFolder.md)CloudDisk_SyncFolder同步根属性信息。

#### 枚举

名称typedef关键字描述[CloudDisk_SyncState](#ZH-CN_TOPIC_0000002497445290__clouddisk_syncstate)CloudDisk_SyncState文件同步状态的枚举值。[CloudDisk_OperationType](#ZH-CN_TOPIC_0000002497445290__clouddisk_operationtype)CloudDisk_OperationType文件变更类型枚举值。[CloudDisk_ErrorReason](#ZH-CN_TOPIC_0000002497445290__clouddisk_errorreason)CloudDisk_ErrorReason文件同步失败原因的枚举值。[CloudDisk_SyncFolderState](#ZH-CN_TOPIC_0000002497445290__clouddisk_syncfolderstate)CloudDisk_SyncFolderState同步根路径状态的枚举值。

#### 函数

名称描述[CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, void (*callback)(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_ChangeData changeDatas[], size_t bufferLength))](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_registersyncfolderchanges)应用注册一个回调函数，用于获取同步根路径下文件的变更。[CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_unregistersyncfolderchanges)应用取消注册同步根路径下文件变更的回调。[CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, uint64_t startUsn, size_t count, CloudDisk_ChangesResult **changesResult)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_getsyncfolderchanges)获取同步根路径下的历史操作记录。[CloudDisk_ErrorCode OH_CloudDisk_SetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_FileSyncState fileSyncStates[], size_t bufferLength, CloudDisk_FailedList **failedLists, size_t *failedCount)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_setfilesyncstates)应用设置同步根路径下文件的同步状态。[CloudDisk_ErrorCode OH_CloudDisk_GetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo paths[], size_t bufferLength, CloudDisk_ResultList **resultLists, size_t *resultCount)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_getfilesyncstates)应用查询同步根路径下文件同步状态。[CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolder(const CloudDisk_SyncFolder *syncFolder)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_registersyncfolder)应用注册同步根。[CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_unregistersyncfolder)应用取消注册同步根。[CloudDisk_ErrorCode OH_CloudDisk_ActiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_activesyncfolder)应用激活同步根。[CloudDisk_ErrorCode OH_CloudDisk_DeactiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_deactivesyncfolder)应用取消激活同步根。[CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolders(CloudDisk_SyncFolder **syncFolders, size_t *count)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_getsyncfolders)应用获取所有同步根。[CloudDisk_ErrorCode OH_CloudDisk_UpdateCustomAlias(const CloudDisk_SyncFolderPath syncFolderPath, const char *customAlias, size_t customAliasLength)](#ZH-CN_TOPIC_0000002497445290__oh_clouddisk_updatecustomalias)应用更新同步根别名。

#### 枚举类型说明

#### CloudDisk_SyncState

```ets
enum CloudDisk_SyncState
```

**描述**

文件同步状态的枚举值。

**起始版本：** 21

枚举项描述IDLE = 0目前处于空闲状态，未执行任何同步操作。SYNCING = 1文件正在同步。SYNC_SUCCEEDED = 2文件同步成功。SYNC_FAILED = 3文件同步失败。SYNC_CANCELED = 4文件同步取消。SYNC_CONFLICTED = 5文件同步冲突。

#### CloudDisk_OperationType

```ets
enum CloudDisk_OperationType
```

**描述**

文件变更类型枚举值。

**起始版本：** 21

枚举项描述CREATE = 0创建文件或目录。DELETE = 1删除文件或目录。MOVE_FROM = 2移动此文件或目录。MOVE_TO = 3移动到此文件或目录。CLOSE_WRITE = 4在写入操作后关闭文件。SYNC_FOLDER_INVALID = 5同步根路径无效。

#### CloudDisk_ErrorReason

```ets
enum CloudDisk_ErrorReason
```

**描述**

文件同步失败原因的枚举值。

**起始版本：** 21

枚举项描述INVALID_ARGUMENT = 0输入的参数无效。NO_SUCH_FILE = 1操作的文件或目录不存在。NO_SPACE_LEFT = 2设备上的剩余空间不足。OUT_OF_RANGE = 3超出有效范围。NO_SYNC_STATE = 4同步状态未设置。

#### CloudDisk_SyncFolderState

```ets
enum CloudDisk_SyncFolderState
```

**描述**

同步根路径状态的枚举值。

**起始版本：** 21

枚举项描述INACTIVE = 0表示同步根路径的状态是未激活的。ACTIVE = 1表示同步根路径的状态是激活的。

#### 函数说明

#### OH_CloudDisk_RegisterSyncFolderChanges()

```ets
CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, void (*callback)(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_ChangeData changeDatas[], size_t bufferLength))
```

**描述**

应用注册一个回调函数，用于获取同步根路径下文件的变更。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath表示同步根路径，参考：{@link CloudDisk_SyncFolderPath}。callback注册的回调函数。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_UnregisterSyncFolderChanges()

```ets
CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用取消注册同步根路径下文件变更的回调。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath表示同步根路径，参考：{@link CloudDisk_SyncFolderPath}。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_GetSyncFolderChanges()

```ets
CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, uint64_t startUsn, size_t count, CloudDisk_ChangesResult **changesResult)
```

**描述**

获取同步根路径下的历史操作记录。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath查询的同步根路径，参考：{@link CloudDisk_SyncFolderPath}。uint64_t startUsn查询起始的变更序列，范围：[0, 2^64 - 1]。size_t count查询文件变更的数量，范围：[1, 100]。[CloudDisk_ChangesResult](../../topics/networking/CloudDisk_ChangesResult.md) **changesResult表示查询文件变更的结果。详情请参阅[CloudDisk_ChangesResult](../../topics/networking/CloudDisk_ChangesResult.md)。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_SetFileSyncStates()

```ets
CloudDisk_ErrorCode OH_CloudDisk_SetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_FileSyncState fileSyncStates[], size_t bufferLength, CloudDisk_FailedList **failedLists, size_t *failedCount)
```

**描述**

应用设置同步根路径下文件的同步状态。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath待设置的同步根路径，参考：{@link CloudDisk_SyncFolderPath}。[const CloudDisk_FileSyncState](../../topics/networking/CloudDisk_FileSyncState.md) fileSyncStates[]指定文件路径及其目标同步状态的[CloudDisk_FileSyncState](../../topics/networking/CloudDisk_FileSyncState.md)数组。size_t bufferLength待设置同步状态数组的长度，范围：[1, 100]。[CloudDisk_FailedList](../../topics/components/CloudDisk_FailedList.md) **failedLists输出参数。返回一个指向[CloudDisk_FailedList](../../topics/components/CloudDisk_FailedList.md)数组的指针，该数组包含设置失败的文件。size_t *failedCount输出参数。设置同步状态失败的文件列表数组长度。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_GetFileSyncStates()

```ets
CloudDisk_ErrorCode OH_CloudDisk_GetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo paths[], size_t bufferLength, CloudDisk_ResultList **resultLists, size_t *resultCount)
```

**描述**

应用查询同步根路径下文件同步状态。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath待查询的同步根路径，参考：{@link CloudDisk_SyncFolderPath}。[const CloudDisk_PathInfo](../../topics/graphics/CloudDisk_PathInfo.md) paths[]待查询同步状态[CloudDisk_PathInfo](../../topics/graphics/CloudDisk_PathInfo.md)的数组。size_t bufferLength待查询同步状态的数组的长度，范围：[1, 100]。[CloudDisk_ResultList](../../topics/components/CloudDisk_ResultList.md) **resultLists输出参数。返回一个查询到的文件同步操作结果，详情可参考：[CloudDisk_ResultList](../../topics/components/CloudDisk_ResultList.md)。size_t *resultCount输出参数。返回失败的文件数量。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_RegisterSyncFolder()

```ets
CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolder(const CloudDisk_SyncFolder *syncFolder)
```

**描述**

应用注册同步根。

**起始版本：** 21

**参数：**

参数项描述[const CloudDisk_SyncFolder](../../topics/networking/CloudDisk_SyncFolder.md) *syncFolder待注册的同步根路径，参考：[CloudDisk_SyncFolder](../../topics/networking/CloudDisk_SyncFolder.md)。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_UnregisterSyncFolder()

```ets
CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用取消注册同步根。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath需要取消注册的同步根路径，参考：{@link CloudDisk_SyncFolderPath}。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_ActiveSyncFolder()

```ets
CloudDisk_ErrorCode OH_CloudDisk_ActiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用激活同步根。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath需要激活监听的同步根路径，参考：{@link CloudDisk_SyncFolderPath}。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_DeactiveSyncFolder()

```ets
CloudDisk_ErrorCode OH_CloudDisk_DeactiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

**描述**

应用取消激活同步根。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath取消激活监听的同步根路径，参考：{@link CloudDisk_SyncFolderPath}。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_GetSyncFolders()

```ets
CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolders(CloudDisk_SyncFolder **syncFolders, size_t *count)
```

**描述**

应用获取所有同步根。

**起始版本：** 21

**参数：**

参数项描述[CloudDisk_SyncFolder](../../topics/networking/CloudDisk_SyncFolder.md) **syncFolders输出参数。返回同步根路径数组[CloudDisk_SyncFolder](../../topics/networking/CloudDisk_SyncFolder.md)。size_t *count输出参数。当前网盘注册的所有同步根的数量。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。

#### OH_CloudDisk_UpdateCustomAlias()

```ets
CloudDisk_ErrorCode OH_CloudDisk_UpdateCustomAlias(const CloudDisk_SyncFolderPath syncFolderPath, const char *customAlias, size_t customAliasLength)
```

**描述**

应用更新同步根别名。

**起始版本：** 21

**参数：**

参数项描述const CloudDisk_SyncFolderPath syncFolderPath待更新别名的同步根路径，参考：{@link CloudDisk_SyncFolderPath}。const char *customAlias用户定义的别名，不能包含字符：\/*?<>|:"，以及不能以"."、".."和纯空格作为完整名称。size_t customAliasLength用户定义的别名长度，范围：[0, 255]。

**返回：**

类型说明[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)如果接口调用成功，返回[CLOUD_DISK_OK](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)；否则返回云盘管理模块的错误码[CloudDisk_ErrorCode](cloud_disk_error_code.h.md#ZH-CN_TOPIC_0000002529285261__clouddisk_errorcode)。