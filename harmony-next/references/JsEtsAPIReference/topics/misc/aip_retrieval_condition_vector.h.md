# aip_retrieval_condition_vector.h

**概述**

提供与向量条件相关的接口。

引用文件： #include "dataaugmentation/retrieval/aip_retrieval_condition_vector.h"

库： libretrieval_ndk.so

系统能力： SystemCapability.DataAugmentation.Retrieval

起始版本： 6.0.0(20)

相关模块： [Retrieval](Retrieval.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct OH_Retrieval_SubCondition OH_Retrieval_VectorCondition | 定义向量检索条件，包含检索的字段、检索参数、过滤条件等。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Retrieval_VectorCondition * OH_Retrieval_CreateVectorCondition () | 创建向量检索条件。 |
| int OH_Retrieval_DestroyVectorCondition (OH_Retrieval_VectorCondition *condition) | 销毁通过OH_Retrieval_CreateVectorCondition获得的检索条件。 |
| int OH_Retrieval_SetVectorRecallLimit (OH_Retrieval_VectorCondition *condition, uint32_t limit) | 在检索条件中，设置向量检索结果数量上限。 |
| int OH_Retrieval_SetSimilarityThreshold (OH_Retrieval_VectorCondition *condition, double threshold) | 在检索条件中，设置向量检索的相似度阈值。 |