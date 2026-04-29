# aip_retrieval_condition.h

**概述**

提供与检索条件相关的接口。

引用文件： #include "dataaugmentation/retrieval/aip_retrieval_condition.h"

库： libretrieval_ndk.so

系统能力： SystemCapability.DataAugmentation.Retrieval

起始版本： 6.0.0(20)

相关模块： [Retrieval](Retrieval.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct OH_Retrieval_Condition OH_Retrieval_Condition | 定义检索条件，可包含多个子检索条件等。 |
| typedef struct OH_Retrieval_SubCondition OH_Retrieval_SubCondition | 定义子检索条件，可以是向量检索。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Retrieval_Condition * OH_Retrieval_CreateCondition () | 创建检索条件，作为检索接口的入参。 |
| int OH_Retrieval_DestroyCondition (OH_Retrieval_Condition *condition) | 销毁通过OH_Retrieval_CreateCondition获得的检索条件。 |
| int OH_Retrieval_DestroySubCondition (OH_Retrieval_SubCondition *condition) | 销毁通过OH_Retrieval_SubCondition创建的条件。 |
| int OH_Retrieval_AddSubCondition (OH_Retrieval_Condition *condition, OH_Retrieval_SubCondition *subCondition) | 在检索条件中，增加子检索条件。 |