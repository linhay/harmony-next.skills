# OH_CM_Blob

```ets
typedef struct {...} OH_CM_Blob
```

**概述**

定义存放数据的结构体类型。

起始版本： 22

相关模块： [CertManagerType](CertManagerType.md)

所在头文件： [cm_native_type.h](cm_native_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t size | 数据大小。 |
| uint8_t *data | 指向数据内存的指针。 |