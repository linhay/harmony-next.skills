# CloudDisk_FailedList

```ets
typedef struct CloudDisk_FailedList {...} CloudDisk_FailedList
```

**概述**

同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。

起始版本： 21

相关模块： [CloudDisk](CloudDisk.md)

所在头文件： [oh_cloud_disk_manager.h](oh_cloud_disk_manager.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| CloudDisk_PathInfo pathInfo | 失败文件的绝对路径信息。 |
| CloudDisk_ErrorReason errorReason | 文件同步失败的原因。 |