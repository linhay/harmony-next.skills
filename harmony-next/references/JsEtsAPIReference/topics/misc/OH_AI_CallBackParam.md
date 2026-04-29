# OH_AI_CallBackParam

```ets
typedef struct OH_AI_CallBackParam {...} OH_AI_CallBackParam
```

**概述**

回调函数中传入的算子信息。

起始版本： 9

相关模块： [MindSpore](MindSpore.md)

所在头文件： [model.h](model.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char* node_name | 算子名称。 |
| char* node_type | 算子类型。 |