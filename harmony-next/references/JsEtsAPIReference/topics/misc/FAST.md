# FAST

#### 概述

提供FAST算法加速能力相关接口，实现应用启动、加载、响应时延等指标的优化。

**起始版本：**6.0.2(22)

#### 汇总

概述FAST Kit中文件、结构体、宏定义、类型定义、枚举和函数等信息。

#### 文件

| 名称 | 描述 |
| --- | --- |
| [fast_ads_segment_map.h](fast_ads_segment_map.h.md) | 线段表相关数据结构及函数定义。 |
| [fast_common_def.h](fast_common_def.h.md) | FAST Kit错误码等类型的公共定义。 |
| [fast_solver_rect_partition.h](fast_solver_rect_partition.h.md) | 矩形划分求解器相关数据结构及函数定义。 |

#### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [FAST_Rect](FAST_Rect.md) | 定义矩形的数据结构。 |

#### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f) [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga7be8db1fe5677bb8732d73ff6d09b6f8) | 线段表支持的查询操作类型。 |
| typedef enum [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76) [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga88bbda3d57a45b5bd34a2892013a694f) | 线段表支持的更新操作类型。 |
| typedef struct [FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) FAST_SegmentMapConfig | 线段表的不透明配置（Opaque Configuration）。 |
| typedef void * [FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) | 线段表的句柄。 |
| typedef enum [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__gac7fc20f8b5755a79929abf218a853078) | FAST Kit的错误码。 |
| typedef struct [FAST_Rect]([FAST_Rect](FAST.md#ZH-CN_TOPIC_0000002517901103__gacb1549fff44eb0707913f3d5f92712b3).md) FAST_Rect | 定义矩形的数据结构。 |
| typedef struct [FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) FAST_RectPartitionConfig | 矩形划分求解器的不透明配置。 |

#### 枚举

| 名称 | 描述 |
| --- | --- |
| [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f) { FAST_SEGMENTMAP_QUERY_TYPE_SUM = 0, FAST_SEGMENTMAP_QUERY_TYPE_MIN = 1, FAST_SEGMENTMAP_QUERY_TYPE_MAX = 2 } | 线段表支持的查询操作类型。 |
| [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76) { FAST_SEGMENTMAP_UPDATE_TYPE_SET = 0, FAST_SEGMENTMAP_UPDATE_TYPE_ADD = 1, FAST_SEGMENTMAP_UPDATE_TYPE_SUB = 2 } | 线段表支持的更新操作类型。 |
| [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) { FAST_ERROR_CODE_SUCCESS = 1023100000, FAST_ERROR_CODE_FAIL = 1023100001, FAST_ERROR_CODE_ILLEGAL_INPUT = 1023100002, FAST_ERROR_CODE_INVALID_PTR = 1023100003, FAST_ERROR_CODE_OOM = 1023199001 } | FAST Kit的错误码。 |

#### 函数

   ![image](public_sys-resources/zh-cn_image_0000002522245792.webp)

![image](public_sys-resources/zh-cn_image_0000002553205757.webp)![image](public_sys-resources/zh-cn_image_0000002522085804.webp)![image](public_sys-resources/zh-cn_image_0000002553365717.webp)![image](public_sys-resources/zh-cn_image_0000002522245794.webp)

| 名称 | 描述 |
| --- | --- |
| FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) [HMS_FAST_SegmentMap_CreateConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c5e1b0e64894e3a8910c06800afe560) ([FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) **config) | 创建线段表不透明配置实例。 |
| FAST_EXPORT void [HMS_FAST_SegmentMap_DestroyConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga54dc92174e74665cd52b96dd0dc99e45) (FAST_SegmentMapConfig *config) | 销毁线段表的不透明配置实例并释放内存。 |
| FAST_EXPORT FAST_ErrorCode [HMS_FAST_SegmentMap_SetQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga14043280774888f1d2a34951f27415ae) (FAST_SegmentMapConfig *config, [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f) type) | 设置线段表不透明配置中的查询类型。 |
| FAST_EXPORT FAST_ErrorCode [HMS_FAST_SegmentMap_SetUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga1f37b6071a0af42c8e217cc0bf2bda2a) (FAST_SegmentMapConfig *config, [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76) type) | 设置线段表不透明配置中的更新类型。 |
| FAST_EXPORT FAST_ErrorCode [HMS_FAST_SegmentMap_Create](FAST.md#ZH-CN_TOPIC_0000002517901103__ga1e6c63ee4731e04eeac80a64246db037) ([FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) *handle, size_t size, const int32_t *array, FAST_SegmentMapConfig *config) | 创建线段表。 |
| FAST_EXPORT void [HMS_FAST_SegmentMap_Destroy](FAST.md#ZH-CN_TOPIC_0000002517901103__gaf24e3e9e42dbf8e6fd7092762ffdf894) (FAST_SegmentMapHandle handle) | 销毁线段表实例。 |
| FAST_EXPORT FAST_ErrorCode [HMS_FAST_SegmentMap_Update](FAST.md#ZH-CN_TOPIC_0000002517901103__gae85d6f1561a1c4bab0c9161401db07fe) (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value) | 更新线段表的区间。 |
| FAST_EXPORT FAST_ErrorCode [HMS_FAST_SegmentMap_Query](FAST.md#ZH-CN_TOPIC_0000002517901103__ga13129191dae4340dccb99132f54d4055) (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t *result) | 查询线段表的区间。 |
| FAST_EXPORT FAST_ErrorCode [HMS_[FAST_Rect](FAST_Rect.md)Partition_CreateConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga051634633006a8f12665a412dc96687e) ([FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) **config) | 创建矩形划分求解器的不透明配置。 |
| FAST_EXPORT void [HMS_FAST_RectPartition_DestroyConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gae515ef39072676065cef8b9af446f2ac) (FAST_RectPartitionConfig *config) | 销毁矩形划分求解器的不透明配置。 |
| FAST_EXPORT FAST_ErrorCode [HMS_FAST_RectPartition_SetAlgo](FAST.md#ZH-CN_TOPIC_0000002517901103__gaec5519d0974e98f6fe99ab2fa50411cc) (FAST_RectPartitionConfig *config, const char *name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST_EXPORT FAST_ErrorCode [HMS_FAST_RectPartition_Solve](FAST.md#ZH-CN_TOPIC_0000002517901103__ga9329484302723a20438eadc9e4b71609) (FAST_RectPartitionConfig *config, size_t size, const FAST_Rect *origin, FAST_Rect *result, size_t *resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。 说明： 1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST_ERROR_CODE_ILLEGAL_INPUT。 2. 函数能保证输出矩形的数量小于等于输入矩形的数量。 |

#### 类型定义说明

#### [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)

```ets
typedef enum [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：**6.0.2(22)

#### [FAST_Rect](FAST_Rect.md)

```ets
typedef struct [FAST_Rect](FAST_Rect.md) FAST_Rect
```

**描述**

定义矩形的数据结构。

**起始版本：**6.0.2(22)

#### [FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e)

```ets
typedef struct [FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) FAST_RectPartitionConfig
```

**描述**

矩形划分求解器的不透明配置（Opaque Configuration），如果未在配置中设置算法，默认的算法是扫描线算法“SweepLineAlgo”。

**起始版本：**6.0.2(22)

#### [FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e)

```ets
typedef struct [FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) FAST_SegmentMapConfig
```

**描述**

线段表的不透明配置（Opaque Configuration）。

**起始版本：**6.0.2(22)

#### [FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9)

```ets
typedef void* [FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9)
```

**描述**

线段表的句柄。

**起始版本：**6.0.2(22)

#### [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f)

```ets
typedef enum [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f) FAST_SegmentMapQueryType
```

**描述**

线段表数据结构支持的区间查询操作类型。

**起始版本：**6.0.2(22)

#### [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76)

```ets
typedef enum [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76) FAST_SegmentMapUpdateType
```

描述

线段表数据结构支持的区间更新操作类型。

起始版本： 6.0.2(22)

**枚举类型说明**

**[FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)**

```ets
enum [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)
```

描述

FAST Kit的错误码。

起始版本： 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| FAST_ERROR_CODE_SUCCESS = 1023100000 | 成功。 |
| FAST_ERROR_CODE_FAIL = 1023100001 | 失败。 |
| [FAST_ERROR_CODE_ILLEGAL_INPUT](FAST.md) = 1023100002 | 非法输入。 |
| FAST_ERROR_CODE_INVALID_PTR = 1023100003 | 无效指针（例如 NULL)。 |
| FAST_ERROR_CODE_OOM = 1023199001 | 内存溢出。 |

**[FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f)**

```ets
enum [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f)
```

描述

线段表支持的查询操作类型。

该枚举定义了线段表数据结构能够处理的各种区间查询操作。

起始版本： 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| [FAST_SEGMENTMAP_QUERY_TYPE_SUM](FAST.md#ZH-CN_TOPIC_0000002517901103__gga8ef2e816f027493a63bd4e82876f233facf3afe794c5e32bf0400630eaba67e9c) | 区间求和查询。 |
| FAST_SEGMENTMAP_QUERY_TYPE_MIN | 区间最小值查询。 |
| FAST_SEGMENTMAP_QUERY_TYPE_MAX | 区间最大值查询。 |

**[FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76)**

```ets
enum [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76)
```

**描述**

线段表支持的更新操作类型。

该枚举定义了线段表数据结构能够处理的各种区间更新操作。

**起始版本：**6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| [FAST_SEGMENTMAP_UPDATE_TYPE_SET](FAST.md#ZH-CN_TOPIC_0000002517901103__gga2747e3df771507eaeff23cc28f17fc76a6b3378fd423bad1f8ac685f386fd98a1) | 赋值更新，区间内的每一个元素赋同一个值。 |
| FAST_SEGMENTMAP_UPDATE_TYPE_ADD | 加法更新，区间内的每一个元素加同一个值。 |
| FAST_SEGMENTMAP_UPDATE_TYPE_SUB | 减法更新，区间内的每一个元素减同一个值。 |

#### 函数说明

#### [HMS_FAST_RectPartition_CreateConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga051634633006a8f12665a412dc96687e)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_RectPartition_CreateConfig ([FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) ** config)
```

**描述**

创建矩形划分求解器的不透明配置。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 指向矩形划分求解器不透明配置[FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e)的指针。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

#### [HMS_FAST_RectPartition_DestroyConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gae515ef39072676065cef8b9af446f2ac)()

```ets
FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig ([FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) * config)
```

**描述**

销毁矩形划分求解器的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待销毁的矩形划分求解器的不透明配置[FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e)。 |

#### [HMS_FAST_RectPartition_SetAlgo](FAST.md#ZH-CN_TOPIC_0000002517901103__gaec5519d0974e98f6fe99ab2fa50411cc)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_RectPartition_SetAlgo ([FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) * config, const char * name )
```

**描述**

设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为O(N logN)。

**起始版本：**6.0.2(22)

**参数：**

   ![image](public_sys-resources/zh-cn_image_0000002553205759.webp)
| 名称 | 描述 |
| --- | --- |
| config | 待设置的矩形划分求解器的不透明配置[FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e)。 |
| name | 矩形求解器使用的算法名称。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当config或name为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当算法不支持时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

#### [HMS_FAST_RectPartition_Solve](FAST.md#ZH-CN_TOPIC_0000002517901103__ga9329484302723a20438eadc9e4b71609)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_[FAST_Rect](FAST_Rect.md)Partition_Solve ([FAST_RectPartitionConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) * config, size_t size, const FAST_Rect * origin, FAST_Rect * result, size_t * resultSize )
```

**描述**

在指定不透明配置下求解矩形划分问题。在调用函数之前需要先初始化参数中的结果数组result。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 矩形划分求解器的不透明配置。如果参数config中未设置算法，默认的算法是扫描线算法“SweepLineAlgo”。 |
| size | 待划分的矩形[FAST_Rect](FAST_Rect.md)数量。 |
| origin | 待划分的矩形[FAST_Rect](FAST_Rect.md)源数组。 |
| result | 由矩形划分求解器得到的[FAST_Rect](FAST_Rect.md)结果，在调用函数之前需要初始化该结果数组，大小需要和源数组相等，否则可能导致溢出。 |
| resultSize | 划分之后的[FAST_Rect](FAST_Rect.md)数量。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当入参指针为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当输入非法时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)，如矩形存在相交。

当算法求解失败时，返回[FAST_ERROR_CODE_FAIL](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

**注解：**

1. 当选择“SweepLineAlgo”时，不应该返回[FAST_ERROR_CODE_FAIL](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)，此处仅作为预防性设置。

#### [HMS_FAST_SegmentMap_Create](FAST.md#ZH-CN_TOPIC_0000002517901103__ga1e6c63ee4731e04eeac80a64246db037)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_SegmentMap_Create ([FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) * handle, size_t size, const int32_t * array, [FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) * config )
```

**描述**

创建线段表。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 指向线段表句柄[FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9)的指针。 |
| size | 底层数组的大小（元素数量）。 |
| array | 可选；用于初始化线段表的底层数组。如果为NULL，则线段表中的元素均初始化为0，否则数组大小必须与参数size保持一致。 |
| config | 线段表的不透明配置FAST_SegmentMapConfig，若该参数为NULL或未配置，默认查询类型为[FAST_SEGMENTMAP_QUERY_TYPE_SUM](FAST.md#ZH-CN_TOPIC_0000002517901103__gga8ef2e816f027493a63bd4e82876f233facf3afe794c5e32bf0400630eaba67e9c)、更新类型为[FAST_SEGMENTMAP_UPDATE_TYPE_SET](FAST.md#ZH-CN_TOPIC_0000002517901103__gga2747e3df771507eaeff23cc28f17fc76a6b3378fd423bad1f8ac685f386fd98a1)。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当config或handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

#### [HMS_FAST_SegmentMap_CreateConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c5e1b0e64894e3a8910c06800afe560)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_SegmentMap_CreateConfig ([FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) ** config)
```

**描述**

创建线段表的不透明配置。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 指向线段表不透明配置[FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e)的指针。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

#### [HMS_FAST_SegmentMap_Destroy](FAST.md#ZH-CN_TOPIC_0000002517901103__gaf24e3e9e42dbf8e6fd7092762ffdf894)()

```ets
FAST_EXPORT void HMS_FAST_SegmentMap_Destroy ([FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) handle)
```

**描述**

销毁线段表实例。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 待销毁线段表句柄[FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9)。 |

#### [HMS_FAST_SegmentMap_DestroyConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga54dc92174e74665cd52b96dd0dc99e45)()

```ets
FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig ([FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) * config)
```

**描述**

销毁线段表的不透明配置。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待销毁线段表不透明配置[FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e)。 |

#### [HMS_FAST_SegmentMap_Query](FAST.md#ZH-CN_TOPIC_0000002517901103__ga13129191dae4340dccb99132f54d4055)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_SegmentMap_Query ([FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) handle, size_t left, size_t right, int32_t * result )
```

**描述**

查询线段表的区间。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间左闭右开。 |
| right | 区间右端点 （不包含），区间左闭右开。 |
| result | 根据区间查询的结果。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当输入非法时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)，如左端点大于等于右端点。

#### [HMS_FAST_SegmentMap_SetQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga14043280774888f1d2a34951f27415ae)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_SegmentMap_SetQueryType ([FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) * config, [FAST_SegmentMapQueryType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga8ef2e816f027493a63bd4e82876f233f) type )
```

**描述**

设置线段表不透明配置中的查询类型。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待修改的线段表不透明配置。 |
| type | 查询类型。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

#### [HMS_FAST_SegmentMap_SetUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga1f37b6071a0af42c8e217cc0bf2bda2a)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_SegmentMap_SetUpdateType ([FAST_SegmentMapConfig](FAST.md#ZH-CN_TOPIC_0000002517901103__ga752c7dc05b0f2d87f8cb4bd8bb04b34e) * config, [FAST_SegmentMapUpdateType](FAST.md#ZH-CN_TOPIC_0000002517901103__ga2747e3df771507eaeff23cc28f17fc76) type )
```

**描述**

设置线段表不透明配置中的更新类型。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待修改的线段表不透明配置。 |
| type | 更新类型。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

#### [HMS_FAST_SegmentMap_Update](FAST.md#ZH-CN_TOPIC_0000002517901103__gae85d6f1561a1c4bab0c9161401db07fe)()

```ets
FAST_EXPORT [FAST_ErrorCode](FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed) HMS_FAST_SegmentMap_Update ([FAST_SegmentMapHandle](FAST.md#ZH-CN_TOPIC_0000002517901103__ga3c42403e7c9306245dd1340f166993d9) handle, size_t left, size_t right, int32_t value )
```

**描述**

更新线段表的区间。

**起始版本：**6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间为左闭右开。 |
| right | 区间右端点 （不包含），区间为左闭右开。 |
| value | 待更新的值。 |

**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)。

当输入非法时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#ZH-CN_TOPIC_0000002553361567__fast_errorcode-1)，如左端点大于等于右端点。
