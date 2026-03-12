# CloudDisk_FailedList

```ets
typedef struct CloudDisk_FailedList {...} CloudDisk_FailedList
```

#### 概述

同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。

**起始版本：** 21

**相关模块：**[CloudDisk](CloudDisk.md)

**所在头文件：**[oh_cloud_disk_manager.h](oh_cloud_disk_manager.h.md)

#### 汇总

#### 成员变量

名称描述[CloudDisk_PathInfo](CloudDisk_PathInfo.md) pathInfo失败文件的绝对路径信息。[CloudDisk_ErrorReason](oh_cloud_disk_manager.h.md#ZH-CN_TOPIC_0000002497445290__clouddisk_errorreason) errorReason文件同步失败的原因。