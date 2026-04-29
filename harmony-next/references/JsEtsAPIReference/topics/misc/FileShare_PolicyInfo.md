# FileShare_PolicyInfo

```ets
typedef struct FileShare_PolicyInfo {...} FileShare_PolicyInfo
```

**概述**

需要授予或使能权限URI的策略信息。

起始版本： 12

相关模块： [fileShare](fileShare.md)

所在头文件： [oh_file_share.h](oh_file_share.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char *uri | 需要授予或使能权限的URI。 |
| unsigned int length | URI的字节长度。 |
| unsigned int operationMode | 授予或使能权限的URI访问模式。  示例：FileShare_OperationMode.READ_MODE 、 FileShare_OperationMode.WRITE_MODE   或者 FileShare_OperationMode.READ_MODE|FileShare_OperationMode.WRITE_MODE。 |