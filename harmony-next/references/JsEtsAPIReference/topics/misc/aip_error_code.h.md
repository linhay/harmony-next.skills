# aip_error_code.h

**概述**

提供与错误代码相关的接口。

引用文件： #include "dataaugmentation/aip_error_code.h"

库： libretrieval_ndk.so

系统能力： SystemCapability.DataAugmentation.Retrieval

起始版本： 6.0.0(20)

相关模块： [AIP](AIP.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum OH_Aip_ErrCode OH_Aip_ErrCode | 错误码信息。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| OH_Aip_ErrCode { AIP_OK = 0, AIP_E_EXEC_ERR = 1021200005, AIP_E_OUT_OF_RANGE = 1021200006, AIP_E_NO_SUCH_FIELD = 1021200007, AIP_E_OVER_LIMIT = 1021200008, AIP_E_CONDITION_OVER_LIMIT = 1021200009, AIP_E_INVALID_ARGS = 1021200010, AIP_E_EMBEDDING_ERR = 1021200012 } | 错误码信息。 |