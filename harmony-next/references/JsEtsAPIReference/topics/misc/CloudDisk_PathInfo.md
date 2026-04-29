# CloudDisk_PathInfo

```ets
typedef struct CloudDisk_PathInfo {...} CloudDisk_PathInfo
typedef struct CloudDisk_PathInfo CloudDisk_FieldInfo
typedef struct CloudDisk_PathInfo CloudDisk_SyncFolderPath
```

**概述**

文件路径信息。

起始版本： 21

相关模块： [CloudDisk](CloudDisk.md)

所在头文件： [oh_cloud_disk_manager.h](oh_cloud_disk_manager.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char *value | 文件的路径，以'\0'字符结尾。 |
| size_t length | 文件路径的长度，不包括结尾的'\0'字符。 |