# Retrieval

#### 概述

智慧化数据平台（AIP）为应用提供构建端侧智慧化解决方案，提供向量化、知识检索和知识问答的能力。

该能力依赖[知识加工](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-knowledge-processing)依据Schema生成的产物。当有schema中knowledgeSource字段配置了多个知识加工数据源时，仅支持检索第一个数据源加工产物。

**起始版本：** 6.0.0(20)

#### 汇总

#### 文件

名称

描述

[aip_retrieval.h](aip_retrieval.h.md)

提供知识检索相关的接口。

[aip_retrieval_condition.h](aip_retrieval_condition.h.md)

提供与检索条件相关的接口。

[aip_retrieval_condition_vector.h](aip_retrieval_condition_vector.h.md)

提供与向量条件相关的接口。

[aip_retrieval_query.h](aip_retrieval_query.h.md)

提供与检索查询相关的接口。

[aip_retrieval_record.h](aip_retrieval_record.h.md)

提供与检索结果相关的接口。

#### 类型定义

名称

描述

typedef struct [OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)[OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)

定义检索器类型，检索器是进行检索的句柄。

typedef struct [OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)

定义检索器配置。

typedef struct [OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)

定义一个用于打开数据库存储的数据库配置。

typedef enum [Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205)[Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205)

定义数据索引类型，目前仅包括向量索引数据。

typedef void(* [OH_Retrieval_Callback](#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6)) (void *context, [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record, int errCode)

检索结果记录的回调函数。

typedef struct [OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)

定义检索条件，可包含多个子检索条件等。

typedef struct [OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)[OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)

定义子检索条件，可以是向量检索。

typedef struct [OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)

定义向量检索条件，包含检索的字段、检索参数、过滤条件等。

typedef struct [OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)

定义检索词，当前只支持纯文本检索。

typedef struct [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)

定义检索结果，包含检索知识库得到的字段和字段取值。

typedef struct [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)

定义检索结果中的数据库bucket数组。

#### 枚举

名称

描述

[Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205) { Retrieval_TYPE_VECTOR = 1 }

定义数据索引类型，目前仅包括向量索引数据。

#### 函数

名称

描述

int [OH_Retrieval_CreateRetriever](#ZH-CN_TOPIC_0000002379806489__gac6d2c1dd3039a0ac1a6996435600a81b) (const [OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) *config, [OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) **retriever)

获取检索器。

int [OH_Retrieval_DestroyRetriever](#ZH-CN_TOPIC_0000002379806489__ga1dc6c697ce9b8ff2a5901e154a7aae16) ([OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) *retriever)

销毁通过[OH_Retrieval_CreateRetriever](#ZH-CN_TOPIC_0000002379806489__gac6d2c1dd3039a0ac1a6996435600a81b)获得的检索器。

[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) * [OH_Retrieval_CreateConfig](#ZH-CN_TOPIC_0000002379806489__ga2174e9883347dee95b57863a47b60f98) ()

获取检索器配置。

int [OH_Retrieval_DestroyConfig](#ZH-CN_TOPIC_0000002379806489__gaf7646a7caa380dcfaff025669c8336b9) ([OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) *config)

销毁通过[OH_Retrieval_CreateConfig](#ZH-CN_TOPIC_0000002379806489__ga2174e9883347dee95b57863a47b60f98)获得的检索配置。

[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) * [OH_Retrieval_CreateDbConfig](#ZH-CN_TOPIC_0000002379806489__ga238499e6ca79658b59080658ad59e717) ()

创建一个配置项以打开数据库。

int [OH_Retrieval_DestroyDbConfig](#ZH-CN_TOPIC_0000002379806489__ga08500cc36d88c15fc0e45e98a2534681) ([OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) *dbConfig)

销毁[OH_Retrieval_CreateDbConfig](#ZH-CN_TOPIC_0000002379806489__ga238499e6ca79658b59080658ad59e717)创建的[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)。

int [OH_Retrieval_SetDbConfig](#ZH-CN_TOPIC_0000002379806489__gab69fc668e86d62c8e2f1cfdfc29de12e) ([OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) *dbConfig, [OH_Rdb_ConfigV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-configv2) *rdbConfig)

设置[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)中的数据库配置。

int [OH_Retrieval_AddConfig](#ZH-CN_TOPIC_0000002379806489__ga217ef10e651eb8ed7e85fd5099c21939) ([OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) *config, [Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205) channelType, [OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) *dbConfig)

设置[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)中的数据库配置。

int [OH_Retrieval_Retrieve](#ZH-CN_TOPIC_0000002379806489__ga9b5b65705a02d8817f65dd01955cfe77) (const [OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) *retriever, const [OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) *query, const [OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) *condition, void *context, const [OH_Retrieval_Callback](#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6) *callback)

执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。

[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) * [OH_Retrieval_CreateCondition](#ZH-CN_TOPIC_0000002379806489__gaf596f89029870da548ab24229ab117d8) ()

创建检索条件，作为检索接口的入参。

int [OH_Retrieval_DestroyCondition](#ZH-CN_TOPIC_0000002379806489__ga494ae3c2094d8c7d7886df7323e07a31) ([OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) *condition)

销毁通过[OH_Retrieval_CreateCondition](#ZH-CN_TOPIC_0000002379806489__gaf596f89029870da548ab24229ab117d8)获得的检索条件。

int [OH_Retrieval_DestroySubCondition](#ZH-CN_TOPIC_0000002379806489__ga9801829d9219eff29dcc372301c3eec4) ([OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) *condition)

销毁[OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)对象。

int [OH_Retrieval_AddSubCondition](#ZH-CN_TOPIC_0000002379806489__ga2a1a77b04c4876fb8f6836fb7c85a3fd) ([OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) *condition, [OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) *subCondition)

在检索条件中，增加子检索条件。

[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) * [OH_Retrieval_CreateVectorCondition](#ZH-CN_TOPIC_0000002379806489__ga9ba9d25126a97b67197b3f7b6fa90bfc) ()

创建向量检索条件。

int [OH_Retrieval_DestroyVectorCondition](#ZH-CN_TOPIC_0000002379806489__ga94ffaaedc2262aeeb5a98cc53d309b89) ([OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) *condition)

销毁通过[OH_Retrieval_CreateVectorCondition](#ZH-CN_TOPIC_0000002379806489__ga9ba9d25126a97b67197b3f7b6fa90bfc)获得的检索条件。

int [OH_Retrieval_SetVectorRecallLimit](#ZH-CN_TOPIC_0000002379806489__ga3add0883ce112a17432b44733a965b60) ([OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) *condition, uint32_t limit)

在检索条件中，设置向量检索结果数量上限1000。

int [OH_Retrieval_SetSimilarityThreshold](#ZH-CN_TOPIC_0000002379806489__gad92af7e32a48d8429bf06a587501e244) ([OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) *condition, double threshold)

在检索条件中，设置向量检索的相似度阈值。

[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) * [OH_Retrieval_CreateQuery](#ZH-CN_TOPIC_0000002379806489__gad5182c984d2e5d85171fd93205ea785f) ()

创建检索词，作为检索接口的入参。

int [OH_Retrieval_DestroyQuery](#ZH-CN_TOPIC_0000002379806489__ga8810c6250f69bcb4ef1d5f9b6084a42b) ([OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) *query)

销毁通过[OH_Retrieval_CreateQuery](#ZH-CN_TOPIC_0000002379806489__gad5182c984d2e5d85171fd93205ea785f)获得的检索词。

int [OH_Retrieval_SetOriginalQuestion](#ZH-CN_TOPIC_0000002379806489__ga967b4d6fd7de85f9299529598dce72e4) ([OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) *query, const char *question)

设置[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)中的检索词。

int [OH_Retrieval_DestroyRecord](#ZH-CN_TOPIC_0000002379806489__ga92addac70c2eeb71b2ebf370d982aa48) ([OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record)

销毁通过检索接口[OH_Retrieval_Retrieve](#ZH-CN_TOPIC_0000002379806489__ga9b5b65705a02d8817f65dd01955cfe77)获得的检索结果。

int [OH_Retrieval_GetRecordLength](#ZH-CN_TOPIC_0000002379806489__gae806d473b297a2d3accd5b34aca68bd9) (const [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record, uint32_t *length)

获取检索结果[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)中的数据库bucket数组长度。

int [OH_Retrieval_GetRecordItem](#ZH-CN_TOPIC_0000002379806489__ga41b814740cf743acf9c3ee6edbc0bed4) (const [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record, uint32_t index, const [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) **item)

获取检索结果[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)中的数据库bucket数组。

int [OH_Retrieval_GetItemSize](#ZH-CN_TOPIC_0000002379806489__gaa2e5538a14e0d33ef3315551314a9044) (const [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) *items, const char *fieldName, size_t *size)

获取数据库bucket数组[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)中指定字段的值的size。size值包含结束符。

int [OH_Retrieval_GetItemText](#ZH-CN_TOPIC_0000002379806489__ga273f6ae58af8630fec0f8d9c1472c659) (const [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) *items, const char *fieldName, char *value, size_t size)

获取数据库bucket数组[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)中指定字段的值。

#### 类型定义说明

#### OH_Retrieval_Callback

```ets
typedef void(* [OH_Retrieval_Callback](#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6)) (void *context, [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record, int errCode)
```

**描述**

检索结果记录的回调函数。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

context

表示用户提供的上下文数据。

record

表示指向 [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) 实例的指针。

errCode

表示返回的错误码。

#### OH_Retrieval_Condition

```ets
typedef struct [OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) [OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)
```

**描述**

定义检索条件，可包含多个子检索条件。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_Config

```ets
typedef struct [OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) [OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)
```

**描述**

定义检索器配置，包括数据库路径、数据库名称、包名等。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_DbConfig

```ets
typedef struct [OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) [OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)
```

**描述**

定义一个用于打开数据库存储的数据库配置。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_Query

```ets
typedef struct [OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) [OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)
```

**描述**

定义检索词，当前只支持纯文本检索，不支持图片、视频等。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_Record

```ets
typedef struct [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)
```

**描述**

定义检索结果，包含检索知识库得到的字段和字段取值。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_RecordItem

```ets
typedef struct [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)
```

**描述**

定义检索结果中的数据库bucket数组。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_Retriever

```ets
typedef struct [OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) [OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)
```

**描述**

定义检索器类型，检索器是进行检索的句柄。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_SubCondition

```ets
typedef struct [OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) [OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)
```

**描述**

定义子检索条件，目前支持向量检索。

**起始版本：** 6.0.0(20)

#### OH_Retrieval_VectorCondition

```ets
typedef struct [OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) [OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)
```

**描述**

定义向量检索条件，包含检索的字段、检索参数、过滤条件等。

**起始版本：** 6.0.0(20)

#### Retrieval_Channel_Type

```ets
typedef enum [Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205) [Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205)
```

**描述**

定义数据索引类型，目前仅包括向量索引数据。

**起始版本：** 6.0.0(20)

#### 枚举类型说明

#### Retrieval_Channel_Type

```ets
enum [Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205)
```

**描述**

定义数据索引类型，目前仅包括向量索引数据。

**起始版本：** 6.0.0(20)

枚举值

描述

****Retrieval_TYPE_VECTOR

表示向量索引。

#### 函数说明

#### OH_Retrieval_AddConfig()

```ets
int OH_Retrieval_AddConfig ([OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) * config, [Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205) channelType, [OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) * dbConfig )
```

**描述**

设置[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)中的数据库配置。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

config

指向检索配置 [OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) 实例的指针。

channelType

表示一种数据索引类型，目前仅支持向量查询。

dbConfig

指向数据库配置实例的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)、[Retrieval_Channel_Type](#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205)、[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_AddSubCondition()

```ets
int OH_Retrieval_AddSubCondition ([OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) * condition, [OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) * subCondition )
```

**描述**

在检索条件中，增加子检索条件。当前仅支持增加一个子检索条件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

condition

指向检索条件[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)实例的指针。

subCondition

指向子检索条件实例的指针，可以是向量检索条件[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

AIP_E_CONDITION_OVER_LIMIT - 条件数量超过上限。

**参见：**

[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)、[OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)、[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_CreateCondition()

```ets
[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)* OH_Retrieval_CreateCondition ()
```

**描述**

创建检索条件，作为检索接口的入参。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向检索条件[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)

#### OH_Retrieval_CreateConfig()

```ets
[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)* OH_Retrieval_CreateConfig ()
```

**描述**

获取检索器配置。用于初始化检索器。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向检索器配置[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_CreateDbConfig()

```ets
[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)* OH_Retrieval_CreateDbConfig ()
```

**描述**

创建一个数据库相关配置项。

**起始版本：** 6.0.0(20)

**返回：**

返回指向[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_CreateQuery()

```ets
[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)* OH_Retrieval_CreateQuery ()
```

**描述**

创建检索词，作为检索接口的入参。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)

#### OH_Retrieval_CreateRetriever()

```ets
int OH_Retrieval_CreateRetriever (const [OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) * config, [OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) ** retriever )
```

**描述**

读取检索配置，初始化检索器。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

config

创建检索器时，需要输入检索器的配置项[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)。

retriever

返回指向检索器[OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)实例的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)、[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_CreateVectorCondition()

```ets
[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)* OH_Retrieval_CreateVectorCondition ()
```

**描述**

创建向量检索条件。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向检索条件[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)

#### OH_Retrieval_DestroyCondition()

```ets
int OH_Retrieval_DestroyCondition ([OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) * condition)
```

**描述**

销毁通过[OH_Retrieval_CreateCondition](#ZH-CN_TOPIC_0000002379806489__gaf596f89029870da548ab24229ab117d8)获得的检索条件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

condition

指向检索条件[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)、[OH_Retrieval_CreateCondition](#ZH-CN_TOPIC_0000002379806489__gaf596f89029870da548ab24229ab117d8)

#### OH_Retrieval_DestroyConfig()

```ets
int OH_Retrieval_DestroyConfig ([OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) * config)
```

**描述**

销毁通过[OH_Retrieval_CreateConfig()](#ZH-CN_TOPIC_0000002379806489__ga2174e9883347dee95b57863a47b60f98)获得的检索配置。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

config

指向检索配置[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Config](#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)、[OH_Retrieval_CreateConfig](#ZH-CN_TOPIC_0000002379806489__ga2174e9883347dee95b57863a47b60f98)

#### OH_Retrieval_DestroyDbConfig()

```ets
int OH_Retrieval_DestroyDbConfig ([OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) * dbConfig)
```

**描述**

销毁[OH_Retrieval_CreateDbConfig](#ZH-CN_TOPIC_0000002379806489__ga238499e6ca79658b59080658ad59e717)创建的[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

dbConfig

表示指向[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)实例的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)、[OH_Retrieval_CreateDbConfig](#ZH-CN_TOPIC_0000002379806489__ga238499e6ca79658b59080658ad59e717)

#### OH_Retrieval_DestroyQuery()

```ets
int OH_Retrieval_DestroyQuery ([OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) * query)
```

**描述**

销毁通过[OH_Retrieval_CreateQuery](#ZH-CN_TOPIC_0000002379806489__gad5182c984d2e5d85171fd93205ea785f)获得的检索词。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

query

指向检索词[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)、[OH_Retrieval_CreateQuery](#ZH-CN_TOPIC_0000002379806489__gad5182c984d2e5d85171fd93205ea785f)

#### OH_Retrieval_DestroyRecord()

```ets
int OH_Retrieval_DestroyRecord ([OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) * record)
```

**描述**

销毁通过检索接口[OH_Retrieval_Retrieve](#ZH-CN_TOPIC_0000002379806489__ga9b5b65705a02d8817f65dd01955cfe77)获得的检索结果。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

record

指向检索结果[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)、[OH_Retrieval_Retrieve](#ZH-CN_TOPIC_0000002379806489__ga9b5b65705a02d8817f65dd01955cfe77)

#### OH_Retrieval_DestroyRetriever()

```ets
int OH_Retrieval_DestroyRetriever ([OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) * retriever)
```

**描述**

销毁通过[OH_Retrieval_CreateRetriever](#ZH-CN_TOPIC_0000002379806489__gac6d2c1dd3039a0ac1a6996435600a81b)获得的检索器。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

retriever

指向检索器[OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)、[OH_Retrieval_CreateRetriever](#ZH-CN_TOPIC_0000002379806489__gac6d2c1dd3039a0ac1a6996435600a81b)

#### OH_Retrieval_DestroySubCondition()

```ets
int OH_Retrieval_DestroySubCondition ([OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) * condition)
```

**描述**

销毁condition指针。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

condition

指向检索条件[OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_SubCondition](#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_DestroyVectorCondition()

```ets
int OH_Retrieval_DestroyVectorCondition ([OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) * condition)
```

**描述**

销毁通过[OH_Retrieval_CreateVectorCondition](#ZH-CN_TOPIC_0000002379806489__ga9ba9d25126a97b67197b3f7b6fa90bfc)获得的检索条件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

condition

指向向量检索条件[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)、[OH_Retrieval_CreateVectorCondition](#ZH-CN_TOPIC_0000002379806489__ga9ba9d25126a97b67197b3f7b6fa90bfc)

#### OH_Retrieval_GetItemSize()

```ets
int OH_Retrieval_GetItemSize (const [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) * items, const char * fieldName, size_t * size )
```

**描述**

获取数据库bucket数组[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)中指定字段的值的size。size值包含结束符。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

items

指向数据库bucket数组[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)实例的指针。

fieldName

数据库bucket的字段名。

size

数据库bucket相应字段的值的大小。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

AIP_E_NO_SUCH_FIELD - 不存在该字段。

**参见：**

[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_GetItemText()

```ets
int OH_Retrieval_GetItemText (const [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) * items, const char * fieldName, char * value, size_t size )
```

**描述**

获取数据库bucket数组[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)中指定字段的值。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

items

指向数据库bucket数组[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)实例的指针。

fieldName

数据库bucket的字段名。

value

数据库bucket相应字段的值。

size

数据库bucket相应字段的值的大小。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

AIP_E_NO_SUCH_FIELD - 不存在该字段。

AIP_E_IS_NULL - 数据库存储的是NULL。

**参见：**

[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_GetRecordItem()

```ets
int OH_Retrieval_GetRecordItem (const [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) * record, uint32_t index, const [OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) ** item )
```

**描述**

获取检索结果[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)中的数据库bucket数组。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

record

指向检索结果[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)实例的指针。

index

record数组的索引值。最大值为999。

item

指向record数组中单个元素[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

AIP_E_OUT_OF_RANGE - 下标越界。

**参见：**

[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)、[OH_Retrieval_RecordItem](#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_GetRecordLength()

```ets
int OH_Retrieval_GetRecordLength (const [OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) * record, uint32_t * length )
```

**描述**

获取检索结果[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)中的数据库bucket数组。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

record

指向检索结果[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)实例的指针。

length

数据库bucket数组的长度。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_Record](#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_Retrieve()

```ets
int OH_Retrieval_Retrieve (const [OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) * retriever, const [OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) * query, const [OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) * condition, void * context, const [OH_Retrieval_Callback](#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6) * callback )
```

**描述**

执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。接口执行时，会在“/data/storage/el2/base/cache”路径下生成临时存储缓存文件。当设备类型为phone、tablet时，该接口仅支持倒排，不支持向量。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

retriever

检索器句柄，指向[OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)实例的指针。

query

检索的查询词，指向[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)实例的指针。

condition

检索条件，指向[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)实例的指针。

context

表示用户提供的上下文数据，这些数据将在后续调用函数时传递回函数中。

callback

表示指向[OH_Retrieval_Callback](#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6)实例的指针。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_EXEC_ERR - 执行报错。

AIP_E_OUT_OF_RANGE - 下标越界。

AIP_E_NO_SUCH_FIELD - 不存在该字段。

AIP_E_OVER_LIMIT - 数组超过最大长度。

AIP_E_CONDITION_OVER_LIMIT - 条件数量超过上限。

AIP_E_INVALID_ARGS - 无效参数。

AIP_E_EMBEDDING_ERR - 无法生成嵌入向量。

**参见：**

[OH_Retrieval_Retriever](#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)、[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)、[OH_Retrieval_Condition](#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)、[OH_Retrieval_Callback](#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_SetDbConfig()

```ets
int OH_Retrieval_SetDbConfig ([OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) * dbConfig, [OH_Rdb_ConfigV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-configv2) * rdbConfig )
```

**描述**

在[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)中设置数据库配置。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

dbConfig

表示指向[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)实例的指针。

rdbConfig

表示指向数据库配置实例的指针，可能是[OH_Rdb_ConfigV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-configv2)实例。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_DbConfig](#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)、[OH_Rdb_ConfigV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-configv2)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_SetOriginalQuestion()

```ets
int OH_Retrieval_SetOriginalQuestion ([OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) * query, const char * question )
```

**描述**

设置[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)中的检索词。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

query

指向检索词[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)实例的指针。

question

纯文本的问题。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

AIP_E_OVER_LIMIT - 数组超过最大长度。

**参见：**

[OH_Retrieval_Query](#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_SetSimilarityThreshold()

```ets
int OH_Retrieval_SetSimilarityThreshold ([OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) * condition, double threshold )
```

**描述**

在检索条件中，设置向量检索的相似度阈值。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

condition

指向检索条件[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)实例的指针。

threshold

向量检索的余弦相似度阈值，取值范围[0, 1]。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### OH_Retrieval_SetVectorRecallLimit()

```ets
int OH_Retrieval_SetVectorRecallLimit ([OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10) * condition, uint32_t limit )
```

**描述**

在检索条件中，设置向量检索结果数量上限。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

condition

指向检索条件[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)实例的指针。

limit

向量检索结果的数量上限，最大值1000。

**返回：**

返回函数的执行状态。执行成功返回AIP_OK。

AIP_OK - 操作成功。

AIP_E_INVALID_ARGS - 无效参数。

**参见：**

[OH_Retrieval_VectorCondition](#ZH-CN_TOPIC_0000002379806489__ga7d0df66cb913d5948c58223864774b10)、[OH_Aip_ErrCode](zh-cn_topic_0000002379686713.html#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)