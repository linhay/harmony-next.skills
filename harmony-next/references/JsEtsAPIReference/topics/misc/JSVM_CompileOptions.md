# JSVM_CompileOptions

```ets
typedef struct {...} JSVM_CompileOptions
```

**概述**

配合[OH_JSVM_CompileScriptWithOptions](jsvm.h.md#ZH-CN_TOPIC_0000002553362535__oh_jsvm_compilescriptwithoptions)接口使用，是其参数中options数组的元素类型。

起始版本： 12

相关模块： [JSVM](JSVM.md)

所在头文件： [jsvm_types.h](jsvm_types.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| JSVM_CompileOptionId id | 编译选项对应的ID。 |
| void* ptr | void*类型。 |
| int num | int类型。 |
| bool boolean | bool类型。 |