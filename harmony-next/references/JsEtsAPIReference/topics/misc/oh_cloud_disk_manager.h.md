# oh_cloud_disk_manager.h

**概述**

云盘管理模块的接口定义。

引用文件： <filemanagement/clouddiskmanager/oh_cloud_disk_manager.h>

库： libohclouddiskmanager.so

系统能力： SystemCapability.FileManagement.CloudDiskManager

起始版本： 21

相关模块： [CloudDisk](CloudDisk.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| CloudDisk_PathInfo | CloudDisk_PathInfo/CloudDisk_FileIdInfo/CloudDisk_SyncFolderPath | CloudDisk_PathInfo：文件路径信息。  CloudDisk_FileIdInfo：定义的文件ID。  CloudDisk_SyncFolderPath：定义的同步根路径。 |
| CloudDisk_FileSyncState | CloudDisk_FileSyncState | 文件的同步状态。 |
| CloudDisk_ChangeData | CloudDisk_ChangeData | 定义了同步根路径下单个文件变更事件的数据结构。该结构包含有关文件变更的详细信息，包括唯一ID、父目录的唯一ID、相对路径、变更类型、文件大小和时间戳。 |
| CloudDisk_ChangesResult | CloudDisk_ChangesResult | 查询同步根路径中文件变更的结果。该结构体包含同步根路径中文件的变更数据，包括下一个更新序列号、结尾标志以及变更数据项数组。 |
| CloudDisk_FailedList | CloudDisk_FailedList | 同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。 |
| CloudDisk_ResultList | CloudDisk_ResultList | 表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。 |
| CloudDisk_DisplayNameInfo | CloudDisk_DisplayNameInfo | 定义同步根路径的显示名称信息。 |
| CloudDisk_SyncFolder | CloudDisk_SyncFolder | 同步根属性信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| CloudDisk_SyncState | CloudDisk_SyncState | 文件同步状态的枚举值。 |
| CloudDisk_OperationType | CloudDisk_OperationType | 文件变更类型枚举值。 |
| CloudDisk_ErrorReason | CloudDisk_ErrorReason | 文件同步失败原因的枚举值。 |
| CloudDisk_SyncFolderState | CloudDisk_SyncFolderState | 同步根路径状态的枚举值。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, void (*callback)(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_ChangeData changeDatas[], size_t bufferLength)) | 应用注册一个回调函数，用于获取同步根路径下文件的变更。 |
| CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath) | 应用取消注册同步根路径下文件变更的回调。 |
| CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, uint64_t startUsn, size_t count, CloudDisk_ChangesResult **changesResult) | 获取同步根路径下的历史操作记录。 |
| CloudDisk_ErrorCode OH_CloudDisk_SetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_FileSyncState fileSyncStates[], size_t bufferLength, CloudDisk_FailedList **failedLists, size_t *failedCount) | 应用设置同步根路径下文件的同步状态。 |
| CloudDisk_ErrorCode OH_CloudDisk_GetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo paths[], size_t bufferLength, CloudDisk_ResultList **resultLists, size_t *resultCount) | 应用查询同步根路径下文件同步状态。 |
| CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolder(const CloudDisk_SyncFolder *syncFolder) | 应用注册同步根。 |
| CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath) | 应用取消注册同步根。 |
| CloudDisk_ErrorCode OH_CloudDisk_ActiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath) | 应用激活同步根。 |
| CloudDisk_ErrorCode OH_CloudDisk_DeactiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath) | 应用取消激活同步根。 |
| CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolders(CloudDisk_SyncFolder **syncFolders, size_t *count) | 应用获取所有同步根。 |
| CloudDisk_ErrorCode OH_CloudDisk_UpdateCustomAlias(const CloudDisk_SyncFolderPath syncFolderPath, const char *customAlias, size_t customAliasLength) | 应用更新同步根别名。 |

**枚举类型说明**

**CloudDisk_SyncState**

```ets
enum CloudDisk_SyncState
```

描述

文件同步状态的枚举值。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| IDLE = 0 | 目前处于空闲状态，未执行任何同步操作。 |
| SYNCING = 1 | 文件正在同步。 |
| SYNC_SUCCEEDED = 2 | 文件同步成功。 |
| SYNC_FAILED = 3 | 文件同步失败。 |
| SYNC_CANCELED = 4 | 文件同步取消。 |
| SYNC_CONFLICTED = 5 | 文件同步冲突。 |

**CloudDisk_OperationType**

```ets
enum CloudDisk_OperationType
```

描述

文件变更类型枚举值。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| CREATE = 0 | 创建文件或目录。 |
| DELETE = 1 | 删除文件或目录。 |
| MOVE_FROM = 2 | 移动此文件或目录。 |
| MOVE_TO = 3 | 移动到此文件或目录。 |
| CLOSE_WRITE = 4 | 在写入操作后关闭文件。 |
| SYNC_FOLDER_INVALID = 5 | 同步根路径无效。 |

**CloudDisk_ErrorReason**

```ets
enum CloudDisk_ErrorReason
```

描述

文件同步失败原因的枚举值。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| INVALID_ARGUMENT = 0 | 输入的参数无效。 |
| NO_SUCH_FILE = 1 | 操作的文件或目录不存在。 |
| NO_SPACE_LEFT = 2 | 设备上的剩余空间不足。 |
| OUT_OF_RANGE = 3 | 超出有效范围。 |
| NO_SYNC_STATE = 4 | 同步状态未设置。 |

**CloudDisk_SyncFolderState**

```ets
enum CloudDisk_SyncFolderState
```

描述

同步根路径状态的枚举值。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| INACTIVE = 0 | 表示同步根路径的状态是未激活的。 |
| ACTIVE = 1 | 表示同步根路径的状态是激活的。 |

**函数说明**

**OH_CloudDisk_RegisterSyncFolderChanges()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, void (*callback)(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_ChangeData changeDatas[], size_t bufferLength))
```

描述

应用注册一个回调函数，用于获取同步根路径下文件的变更。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 表示同步根路径，参考：CloudDisk_PathInfo。 |
| callback | 注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_UnregisterSyncFolderChanges()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath)
```

描述

应用取消注册同步根路径下文件变更的回调。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 表示同步根路径，参考：CloudDisk_PathInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_GetSyncFolderChanges()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolderChanges(const CloudDisk_SyncFolderPath syncFolderPath, uint64_t startUsn, size_t count, CloudDisk_ChangesResult **changesResult)
```

描述

获取同步根路径下的历史操作记录。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 查询的同步根路径，参考：CloudDisk_PathInfo。 |
| uint64_t startUsn | 查询起始的变更序列，范围：[0, 2^64 - 1]。 |
| size_t count | 查询文件变更的数量，范围：[1, 100]。 |
| CloudDisk_ChangesResult **changesResult | 表示查询文件变更的结果。详情请参阅CloudDisk_ChangesResult。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_SetFileSyncStates()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_SetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_FileSyncState fileSyncStates[], size_t bufferLength, CloudDisk_FailedList **failedLists, size_t *failedCount)
```

描述

应用设置同步根路径下文件的同步状态。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 待设置的同步根路径，参考：CloudDisk_PathInfo。 |
| const CloudDisk_FileSyncState fileSyncStates[] | 指定文件路径及其目标同步状态的CloudDisk_FileSyncState数组。 |
| size_t bufferLength | 待设置同步状态数组的长度，范围：[1, 100]。 |
| CloudDisk_FailedList **failedLists | 输出参数。返回一个指向CloudDisk_FailedList数组的指针，该数组包含设置失败的文件。 |
| size_t *failedCount | 输出参数。设置同步状态失败的文件列表数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_GetFileSyncStates()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_GetFileSyncStates(const CloudDisk_SyncFolderPath syncFolderPath, const CloudDisk_PathInfo paths[], size_t bufferLength, CloudDisk_ResultList **resultLists, size_t *resultCount)
```

描述

应用查询同步根路径下文件同步状态。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 待查询的同步根路径，参考：CloudDisk_PathInfo。 |
| const CloudDisk_PathInfo paths[] | 待查询同步状态CloudDisk_PathInfo的数组。 |
| size_t bufferLength | 待查询同步状态的数组的长度，范围：[1, 100]。 |
| CloudDisk_ResultList **resultLists | 输出参数。返回一个查询到的文件同步操作结果，详情可参考：CloudDisk_ResultList。 |
| size_t *resultCount | 输出参数。返回失败的文件数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_RegisterSyncFolder()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_RegisterSyncFolder(const CloudDisk_SyncFolder *syncFolder)
```

描述

应用注册同步根。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolder *syncFolder | 待注册的同步根路径，参考：CloudDisk_SyncFolder。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_UnregisterSyncFolder()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_UnregisterSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

描述

应用取消注册同步根。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 需要取消注册的同步根路径，参考：CloudDisk_PathInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_ActiveSyncFolder()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_ActiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

描述

应用激活同步根。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 需要激活监听的同步根路径，参考：CloudDisk_PathInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_DeactiveSyncFolder()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_DeactiveSyncFolder(const CloudDisk_SyncFolderPath syncFolderPath)
```

描述

应用取消激活同步根。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 取消激活监听的同步根路径，参考：CloudDisk_PathInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_GetSyncFolders()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_GetSyncFolders(CloudDisk_SyncFolder **syncFolders, size_t *count)
```

描述

应用获取所有同步根。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| CloudDisk_SyncFolder **syncFolders | 输出参数。返回同步根路径数组CloudDisk_SyncFolder。 |
| size_t *count | 输出参数。当前网盘注册的所有同步根的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |

**OH_CloudDisk_UpdateCustomAlias()**

```ets
CloudDisk_ErrorCode OH_CloudDisk_UpdateCustomAlias(const CloudDisk_SyncFolderPath syncFolderPath, const char *customAlias, size_t customAliasLength)
```

描述

应用更新同步根别名。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| const CloudDisk_SyncFolderPath syncFolderPath | 待更新别名的同步根路径，参考：CloudDisk_PathInfo。 |
| const char *customAlias | 用户定义的别名，不能包含字符：\/*?<>|:"，以及不能以"."、".."和纯空格作为完整名称。 |
| size_t customAliasLength | 用户定义的别名长度，范围：[0, 255]。 |

返回：

| 类型 | 说明 |
| --- | --- |
| CloudDisk_ErrorCode | 如果接口调用成功，返回CLOUD_DISK_OK；否则返回云盘管理模块的错误码CloudDisk_ErrorCode。 |