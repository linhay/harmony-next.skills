# OH_NativeBundle_ModuleMetadata

```ets
typedef struct OH_NativeBundle_ModuleMetadata {...} OH_NativeBundle_ModuleMetadata
```

**概述**

模块元数据的信息。

起始版本： 20

相关模块： [Native_Bundle](Native_Bundle.md)

所在头文件： [native_interface_bundle.h](native_interface_bundle.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char* moduleName | 模块名称。 |
| OH_NativeBundle_Metadata* metadataArray | 模块的元数据数组。 |
| size_t metadataArraySize | 模块的元数据数组大小。 |