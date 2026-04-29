# aip_retrieval_record.h

**概述**

提供与检索结果相关的接口。

引用文件： #include "dataaugmentation/retrieval/aip_retrieval_record.h"

库： libretrieval_ndk.so

系统能力： SystemCapability.DataAugmentation.Retrieval

起始版本： 6.0.0(20)

相关模块： [Retrieval](Retrieval.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct OH_Retrieval_Record OH_Retrieval_Record | 定义检索结果，包含检索知识库得到的字段和字段取值。 |
| typedef struct OH_Retrieval_RecordItem OH_Retrieval_RecordItem | 定义检索结果中的数据库bucket数组。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int OH_Retrieval_DestroyRecord (OH_Retrieval_Record *record) | 销毁通过检索接口OH_Retrieval_Retrieve获得的检索结果。 |
| int OH_Retrieval_GetRecordLength (const OH_Retrieval_Record *record, uint32_t *length) | 获取检索结果OH_Retrieval_Record中的数据库bucket数组长度。 |
| int OH_Retrieval_GetRecordItem (const OH_Retrieval_Record *record, uint32_t index, const OH_Retrieval_RecordItem **item) | 获取检索结果OH_Retrieval_Record中的数据库bucket数组。 |
| int OH_Retrieval_GetItemSize (const OH_Retrieval_RecordItem *items, const char *fieldName, size_t *size) | 获取数据库bucket数组OH_Retrieval_RecordItem中指定字段的值的size。size值包含结束符。 |
| int OH_Retrieval_GetItemText (const OH_Retrieval_RecordItem *items, const char *fieldName, char *value, size_t size) | 获取数据库bucket数组OH_Retrieval_RecordItem中指定字段的值。 |