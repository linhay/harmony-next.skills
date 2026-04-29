# aip_retrieval.h

**概述**

提供知识检索相关的接口。

引用文件： #include "dataaugmentation/retrieval/aip_retrieval.h"

库： libretrieval_ndk.so

系统能力： SystemCapability.DataAugmentation.Retrieval

起始版本： 6.0.0(20)

相关模块： [Retrieval](Retrieval.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct OH_Retrieval_Retriever OH_Retrieval_Retriever | 定义检索器类型，检索器是进行检索的句柄。 |
| typedef struct OH_Retrieval_Config OH_Retrieval_Config | 定义检索器配置。 |
| typedef struct OH_Retrieval_DbConfig OH_Retrieval_DbConfig | 定义一个用于打开数据库存储的数据库配置。 |
| typedef enum Retrieval_Channel_Type Retrieval_Channel_Type | 定义数据索引类型，目前仅包含向量索引数据。 |
| typedef void(* OH_Retrieval_Callback) (void *context, OH_Retrieval_Record *record, int errCode) | 检索结果记录的回调函数。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| Retrieval_Channel_Type { RETRIEVAL_TYPE_VECTOR = 1 } | 定义数据索引类型，目前仅包含向量索引数据。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int OH_Retrieval_CreateRetriever (const OH_Retrieval_Config *config, OH_Retrieval_Retriever **retriever) | 读取检索配置，初始化检索器。 |
| int OH_Retrieval_DestroyRetriever (OH_Retrieval_Retriever *retriever) | 销毁通过OH_Retrieval_CreateRetriever获得的检索器。 |
| OH_Retrieval_Config * OH_Retrieval_CreateConfig () | 获取检索器配置。用于初始化检索器。 |
| int OH_Retrieval_DestroyConfig (OH_Retrieval_Config *config) | 销毁通过OH_Retrieval_CreateConfig获得的检索配置。 |
| OH_Retrieval_DbConfig * OH_Retrieval_CreateDbConfig () | 创建一个配置项以打开数据库。 |
| int OH_Retrieval_DestroyDbConfig (OH_Retrieval_DbConfig *dbConfig) | 销毁OH_Retrieval_CreateDbConfig创建的OH_Retrieval_DbConfig。 |
| int OH_Retrieval_SetDbConfig (OH_Retrieval_DbConfig *dbConfig, OH_Rdb_ConfigV2 *rdbConfig) | 在OH_Retrieval_DbConfig中设置数据库配置。 |
| int OH_Retrieval_AddConfig (OH_Retrieval_Config *config, Retrieval_Channel_Type channelType, OH_Retrieval_DbConfig *dbConfig) | 设置OH_Retrieval_Config中的数据库配置。 |
| int OH_Retrieval_Retrieve (const OH_Retrieval_Retriever *retriever, const OH_Retrieval_Query *query, const OH_Retrieval_Condition *condition, void *context, const OH_Retrieval_Callback *callback) | 执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。 |