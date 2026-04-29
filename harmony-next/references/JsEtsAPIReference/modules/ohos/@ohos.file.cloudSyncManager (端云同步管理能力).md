# @ohos.file.cloudSyncManager (端云同步管理能力)

该模块向云空间应用提供端云同步管理能力：包括使能/去使能端云协同能力、修改应用同步开关，云端数据变化通知以及账号退出清理/保留云相关文件等。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { cloudSyncManager } from '@kit.CoreFileKit';
```

#### DownloadStopReason20+

降级下载停止原因的枚举，默认值为NO_STOP。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_STOP | 0 | 下载中未停止。 |
| NETWORK_UNAVAILABLE | 1 | 下载过程中，移动数据网络和WIFI均不可用。 |
| LOCAL_STORAGE_FULL | 2 | 下载过程中，当前设备空间不足。 |
| TEMPERATURE_LIMIT | 3 | 下载过程中，设备温度过高。 |
| USER_STOPPED | 4 | 下载过程中，客户端主动停止下载。 |
| APP_UNLOAD | 5 | 下载过程中，云文件所属应用被卸载。 |
| OTHER_REASON | 6 | 下载过程中，因其他原因停止下载，如：云服务器未响应等。 |

#### DownloadState20+

降级下载任务状态的枚举。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RUNNING | 0 | 下载中。 |
| COMPLETED | 1 | 下载完成。 |
| STOPPED | 2 | 下载停止。 |

#### DownloadProgress20+

降级下载任务的进度信息。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | DownloadState | 否 | 否 | 下载任务的状态。 |
| successfulCount | number | 否 | 否 | 已下载的文件个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。 |
| failedCount | number | 否 | 否 | 下载失败的文件个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。 |
| totalCount | number | 否 | 否 | 待下载文件总个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。 |
| downloadedSize | number | 否 | 否 | 已下载数据大小，取值范围[0, INT64_MAX)，单位：Byte。进度异常时返回INT64_MAX。 |
| totalSize | number | 否 | 否 | 需要下载文件的总大小，取值范围[0, INT64_MAX)，单位：Byte。进度异常时返回INT64_MAX。 |
| stopReason | DownloadStopReason | 否 | 否 | 下载停止的原因。 |

#### CloudFileInfo20+

应用本地和云端文件个数以及大小信息。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cloudFileCount | number | 否 | 否 | 本地未下载的云端文件总个数，取值范围[0, INT32_MAX]，单位：个。 |
| cloudFileTotalSize | number | 否 | 否 | 本地未下载的云端文件总大小，取值范围[0, INT64_MAX]，单位：Byte。 |
| localFileCount | number | 否 | 否 | 本地未上传云端的文件总个数，取值范围[0, INT32_MAX]，单位：个。 |
| localFileTotalSize | number | 否 | 否 | 本地未上传云端的文件总大小，取值范围[0, INT64_MAX]，单位：Byte。 |
| bothFileCount | number | 否 | 否 | 本地已上传云端的文件总个数，取值范围[0, INT32_MAX]，单位：个。 |
| bothFileTotalSize | number | 否 | 否 | 本地已上传云端的文件总大小，取值范围[0, INT64_MAX]，单位：Byte。 |