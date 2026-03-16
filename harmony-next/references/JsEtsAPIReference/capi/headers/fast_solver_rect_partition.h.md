# fast_solver_rect_partition.h

#### 概述

矩形划分求解器相关数据结构及函数定义。

**库：** libfast_solver.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.0.2(22)

**相关模块：**[FAST](../../topics/misc/FAST.md)

#### 汇总

#### 结构体

名称

描述

struct [FAST_Rect](../../topics/misc/FAST_Rect.md)

定义矩形的数据结构。

#### 类型定义

名称

描述

typedef struct [FAST_Rect](../../topics/misc/FAST_Rect.md)[FAST_Rect](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gacb1549fff44eb0707913f3d5f92712b3)

定义矩形的数据结构。

typedef struct [FAST_RectPartitionConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e)[FAST_RectPartitionConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e)

矩形划分求解器的不透明配置。

#### 函数

名称

描述

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_RectPartition_CreateConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga051634633006a8f12665a412dc96687e) ([FAST_RectPartitionConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) **config)

创建矩形划分求解器的不透明配置。

FAST_EXPORT void [HMS_FAST_RectPartition_DestroyConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gae515ef39072676065cef8b9af446f2ac) ([FAST_RectPartitionConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) *config)

销毁矩形划分求解器的不透明配置。

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_RectPartition_SetAlgo](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gaec5519d0974e98f6fe99ab2fa50411cc) ([FAST_RectPartitionConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) *config, const char *name)

设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo“，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。

FAST_EXPORT [FAST_ErrorCode](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga0766cadc400f678a061813aedc6938ed)[HMS_FAST_RectPartition_Solve](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__ga9329484302723a20438eadc9e4b71609) ([FAST_RectPartitionConfig](../../topics/misc/FAST.md#ZH-CN_TOPIC_0000002517901103__gabd3bea5600684d0638b6221f3d0eb23e) *config, size_t size, const [FAST_Rect](../../topics/misc/FAST_Rect.md) *origin, [FAST_Rect](../../topics/misc/FAST_Rect.md) *result, size_t *resultSize)

在指定不透明配置下解决矩形区域划分问题。函数接收若干个彼此不相交的矩形区域作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形区域数量尽可能少。

**说明**：

1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST_ERROR_CODE_ILLEGAL_INPUT。

2. 函数能保证输出矩形的数量小于等于输入矩形的数量。