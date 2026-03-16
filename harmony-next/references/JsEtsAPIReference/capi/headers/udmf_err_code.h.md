# udmf_err_code.h

#### 概述

声明统一数据管理框架错误码信息。

**引用文件：** <database/udmf/udmf_err_code.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：**[UDMF](../../topics/misc/UDMF.md)

#### 汇总

#### 枚举

名称typedef关键字描述[Udmf_ErrCode](#ZH-CN_TOPIC_0000002529284699__udmf_errcode)Udmf_ErrCode错误码信息。[Udmf_ListenerStatus](#ZH-CN_TOPIC_0000002529284699__udmf_listenerstatus)Udmf_ListenerStatus异步获取数据时的状态码枚举。

#### 枚举类型说明

#### Udmf_ErrCode

```ets
enum Udmf_ErrCode
```

**描述**

错误码信息。

**起始版本：** 12

枚举项描述UDMF_E_OK = 0执行成功。UDMF_ERR = 20400000通用错误码。UDMF_E_INVALID_PARAM = (UDMF_ERR + 1)非法参数。

#### Udmf_ListenerStatus

```ets
enum Udmf_ListenerStatus
```

**描述**

异步获取数据时的状态码枚举。

**起始版本：** 15

枚举项描述UDMF_FINISHED = 0表示获取数据成功。UDMF_PROCESSING表示正在处理中。UDMF_CANCELED表示本次任务已被取消。UDMF_INNER_ERROR = 200表示有内部错误发生。UDMF_INVALID_PARAMETERS表示包含无效参数。UDMF_DATA_NOT_FOUND表示没有获取到数据。UDMF_SYNC_FAILED表示同步数据过程中出现错误。UDMF_COPY_FILE_FAILED表示文件拷贝过程中出现错误。