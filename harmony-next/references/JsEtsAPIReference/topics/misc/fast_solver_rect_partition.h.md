# fast_solver_rect_partition.h

**概述**

矩形划分求解器相关数据结构及函数定义。

引用文件： <FASTKit/fast_solver_rect_partition.h>

库： libfast_solver.so

系统能力： SystemCapability.FAST.Core

起始版本： 6.0.2(22)

相关模块： [FAST](FAST.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct FAST_Rect | 定义矩形的数据结构（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct FAST_Rect FAST_Rect | 定义矩形的数据结构。 |
| typedef struct FAST_RectPartitionConfig FAST_RectPartitionConfig | 矩形划分求解器的不透明配置。 |

**函数**

   ![image](public_sys-resources/zh-cn_image_0000002522085806.webp)

![image](public_sys-resources/zh-cn_image_0000002553365719.webp)![image](public_sys-resources/zh-cn_image_0000002522245796.webp)![image](public_sys-resources/zh-cn_image_0000002553205761.webp)![image](public_sys-resources/zh-cn_image_0000002522085808.webp)

| 名称 | 描述 |
| --- | --- |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_CreateConfig (FAST_RectPartitionConfig **config) | 创建矩形划分求解器的不透明配置。 |
| FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig (FAST_RectPartitionConfig *config) | 销毁矩形划分求解器的不透明配置。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_SetAlgo (FAST_RectPartitionConfig *config, const char *name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_Solve (FAST_RectPartitionConfig *config, size_t size, const FAST_Rect *origin, FAST_Rect *result, size_t *resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。 说明： 1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST_ERROR_CODE_ILLEGAL_INPUT。 2. 函数保证输出矩形的数量小于等于输入矩形的数量。 |