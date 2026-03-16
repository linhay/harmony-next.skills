# aip_retrieval_condition_vector.h

#### 概述

提供与向量条件相关的接口。

**库：** libnative_aip_retrieval_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：**[Retrieval](../../topics/misc/Retrieval.md)

#### 汇总

#### 类型定义

名称

描述

typedef struct [OH_Retrieval_SubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)[OH_Retrieval_VectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)

定义向量检索条件，包含检索的字段、检索参数、过滤条件等。

#### 函数

名称

描述

[OH_Retrieval_VectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) * [OH_Retrieval_CreateVectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9ba9d25126a97b67197b3f7b6fa90bfc) ()

创建向量检索条件。

int [OH_Retrieval_DestroyVectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga94ffaaedc2262aeeb5a98cc53d309b89) ([OH_Retrieval_VectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) *condition)

销毁通过[OH_Retrieval_CreateVectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9ba9d25126a97b67197b3f7b6fa90bfc)获得的检索条件。

int [OH_Retrieval_SetVectorRecallLimit](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3add0883ce112a17432b44733a965b60) ([OH_Retrieval_VectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) *condition, uint32_t limit)

在检索条件中，设置向量检索结果数量上限。

int [OH_Retrieval_SetSimilarityThreshold](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gad92af7e32a48d8429bf06a587501e244) ([OH_Retrieval_VectorCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) *condition, double threshold)

在检索条件中，设置向量检索的相似度阈值。