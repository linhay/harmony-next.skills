# status.h

**概述**

提供了MindSpore Lite运行时的状态码。

引用文件： <mindspore/status.h>

库： libmindspore_lite_ndk.so

系统能力： SystemCapability.Ai.MindSpore

起始版本： 9

相关模块： [MindSpore](MindSpore.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AI_CompCode | - | MindSpore不同组件的代码。 |
| OH_AI_Status | OH_AI_Status | MindSpore的状态码。 |

**枚举类型说明**

**OH_AI_CompCode**

```ets
enum OH_AI_CompCode
```

描述

MindSpore不同组件的代码。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_COMPCODE_CORE = 0x00000000u | MindSpore Core的代码。 |
| OH_AI_COMPCODE_MD = 0x10000000u | MindSpore MindData的代码。 |
| OH_AI_COMPCODE_ME = 0x20000000u | MindSpore MindExpression的代码。 |
| OH_AI_COMPCODE_MC = 0x30000000u | MindSpore的代码。 |
| OH_AI_COMPCODE_LITE = 0xF0000000u | MindSpore Lite的代码。 |

**OH_AI_Status**

```ets
enum OH_AI_Status
```

描述

MindSpore的状态码。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_STATUS_SUCCESS = 0 | 执行成功。 |
| OH_AI_STATUS_CORE_FAILED = OH_AI_COMPCODE_CORE | 0x1 | MindSpore Core执行失败。 |
| OH_AI_STATUS_LITE_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -1) | MindSpore Lite执行异常。 |
| OH_AI_STATUS_LITE_NULLPTR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -2) | MindSpore Lite空指针异常。 |
| OH_AI_STATUS_LITE_PARAM_INVALID = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -3) | MindSpore Lite参数异常。 |
| OH_AI_STATUS_LITE_NO_CHANGE = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -4) | MindSpore Lite未改变。 |
| OH_AI_STATUS_LITE_SUCCESS_EXIT = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -5) | MindSpore Lite没有错误但是退出。 |
| OH_AI_STATUS_LITE_MEMORY_FAILED = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -6) | MindSpore Lite分配内存失败。 |
| OH_AI_STATUS_LITE_NOT_SUPPORT = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -7) | MindSpore Lite未支持的功能。 |
| OH_AI_STATUS_LITE_THREADPOOL_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -8) | MindSpore Lite线程池异常。 |
| OH_AI_STATUS_LITE_UNINITIALIZED_OBJ = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -9) | MindSpore Lite 未初始化状态码。 |
| OH_AI_STATUS_LITE_OUT_OF_TENSOR_RANGE = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -100) | 执行器相关的错误码，范围 (-200, -100]。 MindSpore Lite张量溢出错误。 |
| OH_AI_STATUS_LITE_INPUT_TENSOR_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -101) | 执行器相关的错误码，范围 (-200, -100]。 MindSpore Lite张量输入异常。 |
| OH_AI_STATUS_LITE_REENTRANT_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -102) | 执行器相关的错误码，范围 (-200, -100]。 MindSpore Lite函数重入异常。 |
| OH_AI_STATUS_LITE_GRAPH_FILE_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -200) | 图相关的错误码，范围 (-300, -200]。 MindSpore Lite图文件异常。 |
| OH_AI_STATUS_LITE_NOT_FIND_OP = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -300) | 算子相关的错误码，范围 (-400, -300]。 MindSpore Lite未找到算子。 |
| OH_AI_STATUS_LITE_INVALID_OP_NAME = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -301) | 算子相关的错误码，范围 (-400, -300]。 MindSpore Lite算子无效。 |
| OH_AI_STATUS_LITE_INVALID_OP_ATTR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -302) | 算子相关的错误码，范围 (-400, -300]。 MindSpore Lite算子超参数无效。 |
| OH_AI_STATUS_LITE_OP_EXECUTE_FAILURE = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -303) | 算子相关的错误码，范围 (-400, -300]。 MindSpore Lite算子执行失败。 |
| OH_AI_STATUS_LITE_FORMAT_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -400) | 张量相关的错误码，范围 (-500, -400]。 MindSpore Lite张量格式异常。 |
| OH_AI_STATUS_LITE_INFER_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -500) | 形状推理相关的错误码，范围 (-600, -500]。 MindSpore Lite形状推理异常。 |
| OH_AI_STATUS_LITE_INFER_INVALID = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -501) | 形状推理相关的错误码，范围 (-600, -500]。 MindSpore Lite形状推理无效。 |
| OH_AI_STATUS_LITE_INPUT_PARAM_INVALID = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -600) | 用户输入相关的错误码，范围 (-700, -600]。 用户输入的参数无效。 |
| OH_AI_STATUS_LITE_AIPP_NOT_SUPPORTED = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -700) | AIPP（AI Pre-Process，针对AI推理的输入数据进行前处理）相关的错误码，范围 (-800, -700]。  MindSpore Lite不支持AIPP。 起始版本： 23 |
| OH_AI_STATUS_LITE_AIPP_INFER_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -701) | AIPP（AI Pre-Process，针对AI推理的输入数据进行前处理）相关的错误码，范围 (-800, -700]。  MindSpore Lite使用AIPP推理失败。 起始版本： 23 |