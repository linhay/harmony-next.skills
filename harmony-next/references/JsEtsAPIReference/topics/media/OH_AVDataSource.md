# OH_AVDataSource

```ets
typedef struct OH_AVDataSource {...} OH_AVDataSource
```

**概述**

用户自定义数据源。

起始版本： 12

相关模块： [CodecBase](CodecBase.md)

所在头文件： [native_avcodec_base.h](native_avcodec_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int64_t size | 数据源的总大小。 |
| OH_AVDataSourceReadAt readAt | 数据源的数据回调。 |