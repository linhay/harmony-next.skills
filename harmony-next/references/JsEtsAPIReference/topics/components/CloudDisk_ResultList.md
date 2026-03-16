# CloudDisk_ResultList

```ets
typedef struct CloudDisk_ResultList {...} CloudDisk_ResultList
```

#### 概述

表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。

**起始版本：** 21

**相关模块：**[CloudDisk](../networking/CloudDisk.md)

**所在头文件：**[oh_cloud_disk_manager.h](../../capi/headers/oh_cloud_disk_manager.h.md)

#### 汇总

#### 成员变量

名称描述[CloudDisk_PathInfo](../graphics/CloudDisk_PathInfo.md) pathInfo文件的绝对路径信息。bool isSuccess{false}表示操作是否成功。true：表示操作成功；false：表示操作失败。默认值为false。[CloudDisk_SyncState](../../capi/headers/oh_cloud_disk_manager.h.md#ZH-CN_TOPIC_0000002497445290__clouddisk_syncstate) syncState文件的同步状态。当isSuccess为true时才生效。[CloudDisk_ErrorReason](../../capi/headers/oh_cloud_disk_manager.h.md#ZH-CN_TOPIC_0000002497445290__clouddisk_errorreason) errorReason文件同步状态获取失败的原因。当isSuccess为false时才生效。