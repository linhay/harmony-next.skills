# aip_retrieval_query.h

#### 概述

提供与检索查询相关的接口。

**库：** libnative_aip_retrieval_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：**[Retrieval](Retrieval.md)

#### 汇总

#### 类型定义

名称

描述

typedef struct [OH_Retrieval_Query](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)[OH_Retrieval_Query](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)

定义检索词，当前只支持纯文本检索。

#### 函数

名称

描述

[OH_Retrieval_Query](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) * [OH_Retrieval_CreateQuery](Retrieval.md#ZH-CN_TOPIC_0000002379806489__gad5182c984d2e5d85171fd93205ea785f) ()

创建检索词，作为检索接口的入参。

int [OH_Retrieval_DestroyQuery](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga8810c6250f69bcb4ef1d5f9b6084a42b) ([OH_Retrieval_Query](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) *query)

销毁通过[OH_Retrieval_CreateQuery](Retrieval.md#ZH-CN_TOPIC_0000002379806489__gad5182c984d2e5d85171fd93205ea785f)获得的检索词。

int [OH_Retrieval_SetOriginalQuestion](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga967b4d6fd7de85f9299529598dce72e4) ([OH_Retrieval_Query](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) *query, const char *question)

设置[OH_Retrieval_Query](Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)中的检索词。