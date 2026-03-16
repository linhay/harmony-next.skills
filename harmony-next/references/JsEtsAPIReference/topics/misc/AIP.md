# AIP

#### 概述

智慧化数据平台（AIP）为应用提供构建端侧智慧化解决方案，提供向量化、知识检索和知识问答的能力。

**起始版本：** 6.0.0(20)

#### 汇总

#### 文件

名称

描述

[aip_error_code.h](../../capi/headers/aip_error_code.h.md)

描述错误码信息。

#### 类型定义

名称

描述

typedef enum [OH_Aip_ErrCode](#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)[OH_Aip_ErrCode](#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417)

错误码。

#### 枚举

名称

描述

[OH_Aip_ErrCode](#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417) {

AIP_OK = 0,

AIP_E_EXEC_ERR = 1021200005,

AIP_E_OUT_OF_RANGE = 1021200006,

AIP_E_NO_SUCH_FIELD = 1021200007,

AIP_E_OVER_LIMIT = 1021200008,

AIP_E_CONDITION_OVER_LIMIT = 1021200009,

AIP_E_INVALID_ARGS = 1021200010,

AIP_E_EMBEDDING_ERR = 1021200012

}

错误码信息。

#### 类型定义说明

#### OH_Aip_ErrCode

```ets
typedef enum [OH_Aip_ErrCode](#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417) [OH_Aip_ErrCode](#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417);
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)

#### 枚举类型说明

#### OH_Aip_ErrCode

```ets
enum [OH_Aip_ErrCode](#ZH-CN_TOPIC_0000002379686713__ga1eb26b856dc8a8f5ed5c815f9a4b3417);
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)

枚举值

描述

****AIP_OK

操作成功。

****AIP_E_EXEC_ERR

执行报错。

****AIP_E_OUT_OF_RANGE

下标越界。

****AIP_E_NO_SUCH_FIELD

不存在该字段。

****AIP_E_OVER_LIMIT

数组超过最大长度512字节。

****AIP_E_CONDITION_OVER_LIMIT

条件数量超过上限1。

****AIP_E_INVALID_ARGS

无效参数。

****AIP_E_EMBEDDING_ERR

无法生成嵌入向量。