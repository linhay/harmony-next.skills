# fast_ads_segment_map.h

#### 概述

线段表相关数据结构及函数定义。

**库：** libfast_ads.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.0.2(22)

**相关模块：**[FAST](../../topics/misc/FAST.md)

#### 汇总

#### 类型定义

名称

描述

typedef enum [FAST_SegmentMapQueryType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f)[FAST_SegmentMapQueryType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga7be8db1fe5677bb8732d73ff6d09b6f8)

线段表支持的查询操作类型。

typedef enum [FAST_SegmentMapUpdateType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76)[FAST_SegmentMapUpdateType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga88bbda3d57a45b5bd34a2892013a694f)

线段表支持的更新操作类型。

typedef struct [FAST_SegmentMapConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e)[FAST_SegmentMapConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e)

线段表的不透明配置。

typedef void * [FAST_SegmentMapHandle](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9)

线段表的句柄。

#### 枚举

名称

描述

[FAST_SegmentMapQueryType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f) { [FAST_SEGMENTMAP_QUERY_TYPE_SUM](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gga8ef2e816f027493a63bd4e82876f233facf3afe794c5e32bf0400630eaba67e9c) = 0, [FAST_SEGMENTMAP_QUERY_TYPE_MIN](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gga8ef2e816f027493a63bd4e82876f233facbdea2922cd1bbed97dc788cb515a7b9) = 1, [FAST_SEGMENTMAP_QUERY_TYPE_MAX](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gga8ef2e816f027493a63bd4e82876f233fa4ad7364deefffe6a10c5aa8098670a83) = 2 }

线段表支持的查询操作类型。

[FAST_SegmentMapUpdateType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76) { [FAST_SEGMENTMAP_UPDATE_TYPE_SET](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gga2747e3df771507eaeff23cc28f17fc76a6b3378fd423bad1f8ac685f386fd98a1) = 0, [FAST_SEGMENTMAP_UPDATE_TYPE_ADD](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gga2747e3df771507eaeff23cc28f17fc76a815d2af4cdaa826e15a162e4dfd4fbff) = 1, [FAST_SEGMENTMAP_UPDATE_TYPE_SUB](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gga2747e3df771507eaeff23cc28f17fc76a14b3ed12f408fd2232fc78691bbf9647) = 2 }

线段表支持的更新操作类型。

#### 函数

名称

描述

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_SegmentMap_CreateConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c5e1b0e64894e3a8910c06800afe560) ([FAST_SegmentMapConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) **config)

创建线段表的不透明配置。

FAST_EXPORT void [HMS_FAST_SegmentMap_DestroyConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga54dc92174e74665cd52b96dd0dc99e45) ([FAST_SegmentMapConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) *config)

销毁线段表的不透明配置。

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_SegmentMap_SetQueryType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga14043280774888f1d2a34951f27415ae) ([FAST_SegmentMapConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) *config, [FAST_SegmentMapQueryType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f) type)

设置线段表不透明配置中的查询类型。

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_SegmentMap_SetUpdateType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga1f37b6071a0af42c8e217cc0bf2bda2a) ([FAST_SegmentMapConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) *config, [FAST_SegmentMapUpdateType](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76) type)

设置线段表不透明配置中的更新类型。

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_SegmentMap_Create](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga1e6c63ee4731e04eeac80a64246db037) ([FAST_SegmentMapHandle](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) *handle, size_t size, const int32_t *array, [FAST_SegmentMapConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) *config)

创建线段表。

FAST_EXPORT void [HMS_FAST_SegmentMap_Destroy](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gaf24e3e9e42dbf8e6fd7092762ffdf894) ([FAST_SegmentMapHandle](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) handle)

销毁线段表实例，释放内存，再次调用为未定义行为。

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_SegmentMap_Update](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gae85d6f1561a1c4bab0c9161401db07fe) ([FAST_SegmentMapHandle](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) handle, size_t left, size_t right, int32_t value)

更新线段表的区间，根据配置按照赋值、加法、减法等操作更新。

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_SegmentMap_Query](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga13129191dae4340dccb99132f54d4055) ([FAST_SegmentMapHandle](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) handle, size_t left, size_t right, int32_t *result)

查询线段表的区间，根据配置返回最大值、最小值、求和等数据。