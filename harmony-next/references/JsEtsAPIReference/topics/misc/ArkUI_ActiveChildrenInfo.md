# ArkUI_ActiveChildrenInfo

```ets
typedef struct ArkUI_ActiveChildrenInfo ArkUI_ActiveChildrenInfo
```

**概述**

定义ActiveChildrenInfo类信息。

起始版本： 14

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_type.h](native_type.h.md)

相关接口：

| 名称 | 描述 |
| --- | --- |
| OH_ArkUI_NodeUtils_GetActiveChildrenInfo | 获取某个节点所有活跃的子节点。 |
| OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex | 获取ActiveChildrenInfo结构体的下标为index的子节点。 |
| OH_ArkUI_ActiveChildrenInfo_GetCount | 获取ActiveChildrenInfo结构体内的节点数量。 |
| OH_ArkUI_ActiveChildrenInfo_Destroy | 销毁ActiveChildrenInfo实例。 |