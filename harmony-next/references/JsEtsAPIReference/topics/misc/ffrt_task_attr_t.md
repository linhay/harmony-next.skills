# ffrt_task_attr_t

```ets
typedef struct {...} ffrt_task_attr_t
```

**概述**

并行任务属性结构。

起始版本： 10

相关模块： [FFRT](FFRT.md)

所在头文件： [type_def.h](type_def.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t storage[(ffrt_task_attr_storage_size + sizeof(uint32_t) - 1) / sizeof(uint32_t)] | 任务属性所占空间 |