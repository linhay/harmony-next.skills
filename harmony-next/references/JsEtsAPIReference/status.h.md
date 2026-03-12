# status.h

#### 概述

提供了MindSpore Lite运行时的状态码。

**引用文件：** <mindspore/status.h>

**库：** libmindspore_lite_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：**[MindSpore](MindSpore.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_AI_CompCode](#ZH-CN_TOPIC_0000002529446103__oh_ai_compcode)-MindSpore不同组件的代码。[OH_AI_Status](#ZH-CN_TOPIC_0000002529446103__oh_ai_status)OH_AI_StatusMindSpore的状态码。

#### 枚举类型说明

#### OH_AI_CompCode

```ets
enum OH_AI_CompCode
```

**描述**

MindSpore不同组件的代码。

**起始版本：** 9

枚举项描述OH_AI_COMPCODE_CORE = 0x00000000uMindSpore Core的代码。OH_AI_COMPCODE_MD = 0x10000000uMindSpore MindData的代码。OH_AI_COMPCODE_ME = 0x20000000uMindSpore MindExpression的代码。OH_AI_COMPCODE_MC = 0x30000000uMindSpore的代码。OH_AI_COMPCODE_LITE = 0xF0000000uMindSpore Lite的代码。

#### OH_AI_Status

```ets
enum OH_AI_Status
```

**描述**

MindSpore的状态码。

**起始版本：** 9

枚举项描述OH_AI_STATUS_SUCCESS = 0通用的成功状态码。OH_AI_STATUS_CORE_FAILED = OH_AI_COMPCODE_CORE | 0x1MindSpore Core 失败状态码。OH_AI_STATUS_LITE_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -1)MindSpore Lite 异常状态码。OH_AI_STATUS_LITE_NULLPTR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -2)MindSpore Lite 空指针状态码。OH_AI_STATUS_LITE_PARAM_INVALID = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -3)MindSpore Lite 参数异常状态码。OH_AI_STATUS_LITE_NO_CHANGE = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -4)MindSpore Lite 未改变状态码。OH_AI_STATUS_LITE_SUCCESS_EXIT = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -5)MindSpore Lite 没有错误但是退出的状态码。OH_AI_STATUS_LITE_MEMORY_FAILED = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -6)MindSpore Lite 内存分配失败的状态码。OH_AI_STATUS_LITE_NOT_SUPPORT = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -7)MindSpore Lite 功能未支持的状态码。OH_AI_STATUS_LITE_THREADPOOL_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -8)MindSpore Lite 线程池异常状态码。OH_AI_STATUS_LITE_UNINITIALIZED_OBJ = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -9)MindSpore Lite 未初始化状态码。OH_AI_STATUS_LITE_OUT_OF_TENSOR_RANGE = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -100)MindSpore Lite 张量溢出错误的状态码。OH_AI_STATUS_LITE_INPUT_TENSOR_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -101)MindSpore Lite 输入张量异常的状态码。OH_AI_STATUS_LITE_REENTRANT_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -102)MindSpore Lite 重入异常的状态码。OH_AI_STATUS_LITE_GRAPH_FILE_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -200)MindSpore Lite 文件异常状态码。OH_AI_STATUS_LITE_NOT_FIND_OP = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -300)MindSpore Lite 未找到算子的状态码。OH_AI_STATUS_LITE_INVALID_OP_NAME = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -301)MindSpore Lite 无效算子状态码。OH_AI_STATUS_LITE_INVALID_OP_ATTR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -302)MindSpore Lite 无效算子超参数状态码。OH_AI_STATUS_LITE_OP_EXECUTE_FAILURE = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -303)MindSpore Lite 算子执行失败的状态码。OH_AI_STATUS_LITE_FORMAT_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -400)MindSpore Lite 张量格式异常状态码。OH_AI_STATUS_LITE_INFER_ERROR = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -500)MindSpore Lite 形状推理异常状态码。OH_AI_STATUS_LITE_INFER_INVALID = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -501)MindSpore Lite 无效的形状推理的状态码。OH_AI_STATUS_LITE_INPUT_PARAM_INVALID = OH_AI_COMPCODE_LITE | (0x0FFFFFFF & -600)MindSpore Lite 用户输入的参数无效状态码。