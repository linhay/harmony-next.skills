# aip_retrieval.h

#### 概述

提供知识检索相关的接口。

**库：** libnative_aip_retrieval_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：**[Retrieval](../../topics/misc/Retrieval.md)

#### 汇总

#### 类型定义

名称

描述

typedef struct [OH_Retrieval_Retriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)[OH_Retrieval_Retriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91)

定义检索器类型，检索器是进行检索的句柄。

typedef struct [OH_Retrieval_Config](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)[OH_Retrieval_Config](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)

定义检索器配置。

typedef struct [OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)[OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)

定义一个用于打开数据库存储的数据库配置。

typedef enum [Retrieval_Channel_Type](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205)[Retrieval_Channel_Type](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205)

定义数据索引类型，目前仅包含向量索引数据。

typedef void(* [OH_Retrieval_Callback](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6)) (void *context, [OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record, int errCode)

检索结果记录的回调函数。

#### 枚举

名称

描述

[Retrieval_Channel_Type](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205) { RETRIEVAL_TYPE_VECTOR = 1 }

定义数据索引类型，目前仅包含向量索引数据。

#### 函数

名称

描述

int [OH_Retrieval_CreateRetriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gac6d2c1dd3039a0ac1a6996435600a81b) (const [OH_Retrieval_Config](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) *config, [OH_Retrieval_Retriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) **retriever)

读取检索配置，初始化检索器。

int [OH_Retrieval_DestroyRetriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga1dc6c697ce9b8ff2a5901e154a7aae16) ([OH_Retrieval_Retriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) *retriever)

销毁通过[OH_Retrieval_CreateRetriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gac6d2c1dd3039a0ac1a6996435600a81b)获得的检索器。

[OH_Retrieval_Config](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) * [OH_Retrieval_CreateConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga2174e9883347dee95b57863a47b60f98) ()

获取检索器配置。用于初始化检索器。

int [OH_Retrieval_DestroyConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf7646a7caa380dcfaff025669c8336b9) ([OH_Retrieval_Config](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) *config)

销毁通过[OH_Retrieval_CreateConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga2174e9883347dee95b57863a47b60f98)获得的检索配置。

[OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) * [OH_Retrieval_CreateDbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga238499e6ca79658b59080658ad59e717) ()

创建一个配置项以打开数据库。

int [OH_Retrieval_DestroyDbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga08500cc36d88c15fc0e45e98a2534681) ([OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) *dbConfig)

销毁[OH_Retrieval_CreateDbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga238499e6ca79658b59080658ad59e717)创建的[OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)。

int [OH_Retrieval_SetDbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab69fc668e86d62c8e2f1cfdfc29de12e) ([OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) *dbConfig, [OH_Rdb_ConfigV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-configv2) *rdbConfig)

在[OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe)中设置数据库配置。

int [OH_Retrieval_AddConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga217ef10e651eb8ed7e85fd5099c21939) ([OH_Retrieval_Config](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61) *config, [Retrieval_Channel_Type](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaa9bd8706c16355372cb1eb39d7148205) channelType, [OH_Retrieval_DbConfig](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9e93c397a65a6e6438cee50e3166f0fe) *dbConfig)

设置[OH_Retrieval_Config](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf53480d04ebd0697af001a3a00f26b61)中的数据库配置。

int [OH_Retrieval_Retrieve](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9b5b65705a02d8817f65dd01955cfe77) (const [OH_Retrieval_Retriever](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gadd0ee87ef07f39395b03ff4db042aa91) *retriever, const [OH_Retrieval_Query](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga754a8a9b14076a9cfd7be8dacbcae38e) *query, const [OH_Retrieval_Condition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) *condition, void *context, const [OH_Retrieval_Callback](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf0f9144574f545243e2a035c0805b7d6) *callback)

执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。