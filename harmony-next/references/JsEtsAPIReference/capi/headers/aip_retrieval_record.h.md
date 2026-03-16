# aip_retrieval_record.h

#### 概述

提供与检索结果相关的接口。

**库：** libnative_aip_retrieval_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：**[Retrieval](../../topics/misc/Retrieval.md)

#### 汇总

#### 类型定义

名称

描述

typedef struct [OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)[OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)

定义检索结果，包含检索知识库得到的字段和字段取值。

typedef struct [OH_Retrieval_RecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)[OH_Retrieval_RecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)

定义检索结果中的数据库bucket数组。

#### 函数

名称

描述

int [OH_Retrieval_DestroyRecord](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga92addac70c2eeb71b2ebf370d982aa48) ([OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record)

销毁通过检索接口[OH_Retrieval_Retrieve](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9b5b65705a02d8817f65dd01955cfe77)获得的检索结果。

int [OH_Retrieval_GetRecordLength](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gae806d473b297a2d3accd5b34aca68bd9) (const [OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record, uint32_t *length)

获取检索结果[OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)中的数据库bucket数组长度。

int [OH_Retrieval_GetRecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga41b814740cf743acf9c3ee6edbc0bed4) (const [OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952) *record, uint32_t index, const [OH_Retrieval_RecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) **item)

获取检索结果[OH_Retrieval_Record](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga3d8c3ba973c81dc8f510a69bc6f3a952)中的数据库bucket数组。

int [OH_Retrieval_GetItemSize](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaa2e5538a14e0d33ef3315551314a9044) (const [OH_Retrieval_RecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) *items, const char *fieldName, size_t *size)

获取数据库bucket数组[OH_Retrieval_RecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)中指定字段的值的size。size值包含结束符。

int [OH_Retrieval_GetItemText](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga273f6ae58af8630fec0f8d9c1472c659) (const [OH_Retrieval_RecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f) *items, const char *fieldName, char *value, size_t size)

获取数据库bucket数组[OH_Retrieval_RecordItem](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab0ce809958f4e406378fe926a8a9269f)中指定字段的值。