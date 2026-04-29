# Asset_ResultSet

```ets
typedef struct {...} Asset_ResultSet
```

**概述**

关键资产查询结果集合，用于定义多条关键资产。

起始版本： 11

相关模块： [AssetType](AssetType.md)

所在头文件： [asset_type.h](asset_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t count | 关键资产的条数。 |
| Asset_Result *results | 指向关键资产数组的指针。 |