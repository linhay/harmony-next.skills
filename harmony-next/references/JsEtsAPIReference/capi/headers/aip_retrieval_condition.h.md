# aip_retrieval_condition.h

#### 概述

提供与检索条件相关的接口。

**库：** libnative_aip_retrieval_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：**[Retrieval](../../topics/misc/Retrieval.md)

#### 汇总

#### 类型定义

名称

描述

typedef struct [OH_Retrieval_Condition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)[OH_Retrieval_Condition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e)

定义检索条件，可包含多个子检索条件等。

typedef struct [OH_Retrieval_SubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)[OH_Retrieval_SubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)

定义子检索条件，可以是向量检索。

#### 函数

名称

描述

[OH_Retrieval_Condition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) * [OH_Retrieval_CreateCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf596f89029870da548ab24229ab117d8) ()

创建检索条件，作为检索接口的入参。

int [OH_Retrieval_DestroyCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga494ae3c2094d8c7d7886df7323e07a31) ([OH_Retrieval_Condition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) *condition)

销毁通过[OH_Retrieval_CreateCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gaf596f89029870da548ab24229ab117d8)获得的检索条件。

int [OH_Retrieval_DestroySubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga9801829d9219eff29dcc372301c3eec4) ([OH_Retrieval_SubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) *condition)

销毁通过[OH_Retrieval_SubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a)创建的条件。

int [OH_Retrieval_AddSubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__ga2a1a77b04c4876fb8f6836fb7c85a3fd) ([OH_Retrieval_Condition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gab273fa3774c357b746a8b1f3d223022e) *condition, [OH_Retrieval_SubCondition](../../topics/misc/Retrieval.md#ZH-CN_TOPIC_0000002379806489__gabf02dc24d39de7926dd144966984b06a) *subCondition)

在检索条件中，增加子检索条件。