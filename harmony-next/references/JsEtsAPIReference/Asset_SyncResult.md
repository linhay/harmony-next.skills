# Asset_SyncResult

```ets
typedef struct {...} Asset_SyncResult
```

#### 概述

关键资产同步结果。

**起始版本：** 20

**相关模块：**[AssetType](AssetType.md)

**所在头文件：**[asset_type.h](asset_type.h.md)

#### 汇总

#### 成员变量

名称描述int32_t resultCode关键资产同步的结果码。uint32_t totalCount触发同步的关键资产总数。uint32_t failedCount关键资产同步失败的数量。