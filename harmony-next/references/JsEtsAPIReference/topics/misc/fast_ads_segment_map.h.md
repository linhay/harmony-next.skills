# fast_ads_segment_map.h

**概述**

线段表相关数据结构及函数定义。

引用文件： <FASTKit/fast_ads_segment_map.h>

库： libfast_ads.so

系统能力： SystemCapability.FAST.Core

起始版本： 6.0.2(22)

相关模块： [FAST](FAST.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum FAST_SegmentMapQueryType FAST_SegmentMapQueryType | 线段表支持的查询操作类型。 |
| typedef enum FAST_SegmentMapUpdateType FAST_SegmentMapUpdateType | 线段表支持的更新操作类型。 |
| typedef struct FAST_SegmentMapConfig FAST_SegmentMapConfig | 线段表的不透明配置。 |
| typedef void * FAST_SegmentMapHandle | 线段表的句柄。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| FAST_SegmentMapQueryType { FAST_SEGMENTMAP_QUERY_TYPE_SUM = 0, FAST_SEGMENTMAP_QUERY_TYPE_MIN = 1, FAST_SEGMENTMAP_QUERY_TYPE_MAX = 2 } | 线段表支持的查询操作类型。 |
| FAST_SegmentMapUpdateType { FAST_SEGMENTMAP_UPDATE_TYPE_SET = 0, FAST_SEGMENTMAP_UPDATE_TYPE_ADD = 1, FAST_SEGMENTMAP_UPDATE_TYPE_SUB = 2 } | 线段表支持的更新操作类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig (FAST_SegmentMapConfig **config) | 创建线段表的不透明配置。 |
| FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig (FAST_SegmentMapConfig *config) | 销毁线段表的不透明配置。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetQueryType (FAST_SegmentMapConfig *config, FAST_SegmentMapQueryType type) | 设置线段表不透明配置中的查询类型。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetUpdateType (FAST_SegmentMapConfig *config, FAST_SegmentMapUpdateType type) | 设置线段表不透明配置中的更新类型。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create (FAST_SegmentMapHandle *handle, size_t size, const int32_t *array, FAST_SegmentMapConfig *config) | 创建线段表。 |
| FAST_EXPORT void HMS_FAST_SegmentMap_Destroy (FAST_SegmentMapHandle handle) | 销毁线段表实例，释放内存，再次调用为未定义行为。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Update (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value) | 更新线段表的区间，根据配置按照赋值、加法、减法等操作更新。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Query (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t *result) | 查询线段表的区间，根据配置返回最大值、最小值、求和等数据。 |