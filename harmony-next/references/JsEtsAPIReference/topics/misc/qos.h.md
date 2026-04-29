# qos.h

**概述**

声明QoS提供的C接口。

引用文件： <qos/qos.h>

系统能力： SystemCapability.Resourceschedule.QoS.Core

库： libqos.so

起始版本： 12

相关模块： [QoS](QoS.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| OH_QoS_GewuCreateSessionResult | 格物创建会话的返回结果 |
| OH_QoS_GewuSubmitRequestResult | 格物提交请求的返回结果 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| QoS_Level | QoS_Level | 描述QoS等级。 |
| OH_QoS_GewuErrorCode | OH_QoS_GewuErrorCode | 格物错误码。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| OH_QOS_GEWU_INVALID_SESSION_ID (static_cast<OH_QoS_GewuSession>(0xffffffffU)) | 无效会话句柄，用于错误返回。 起始版本： 20 |
| OH_QOS_GEWU_INVALID_REQUEST_ID (static_cast<OH_QoS_GewuRequest>(0xffffffffU)) | 无效请求句柄，用于错误返回。 起始版本： 20 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| int OH_QoS_SetThreadQoS(QoS_Level level) | - | 为当前线程设置QoS等级。 |
| int OH_QoS_ResetThreadQoS() | - | 取消当前线程的QoS等级。 |
| int OH_QoS_GetThreadQoS(QoS_Level *level) | - | 获得当前线程的QoS等级。 |
| typedef void (*OH_QoS_GewuOnResponse)(void* context, const char* response) | OH_QoS_GewuOnResponse | 用于接收回复的回调。 |
| OH_QoS_GewuCreateSessionResult OH_QoS_GewuCreateSession(const char* attributes) | - | 创建格物会话。会话对象的生命周期从CreateSession函数返回开始，到调用DestroySession为止。会话属性的json字符串。该json字符串支持以下字段：- model: string. 表示会话使用的模型的路径。attributes json字符串例子： {  "model": "/data/storage/el2/base/files/qwen2/"  } |
| OH_QoS_GewuErrorCode OH_QoS_GewuDestroySession(OH_QoS_GewuSession session) | - | 销毁格物会话。建议用户应当等待至所有请求都已完成或中止，然后再调用该接口来销毁会话。如果调用该接口时还有正在进行的请求，那些请求将会被中止，且用户不会再收到回复。注意，在调用完该接口后，会话对象无法再被使用。 |
| OH_QoS_GewuErrorCode OH_QoS_GewuAbortRequest(OH_QoS_GewuSession session, OH_QoS_GewuRequest request) | - | 停止指定的请求。成功调用该函数后，client不会再收到该请求的回复，且该请求句柄无法再被使用。 |
| OH_QoS_GewuSubmitRequestResult OH_QoS_GewuSubmitRequest(OH_QoS_GewuSession session, const char* request, OH_QoS_GewuOnResponse callback, void* context) | - | 提交请求。请求的json字符串，支持以下字段：- messages: array. 表示消息的数组其中每个元素支持以下字段：- role: string. 消息的角色类型。- "developer": 开发者或系统提供的指示。- "user":用户输入。- "assistant": 模型生成结果。- content: string. 消息内容。- stream: boolean or null; 可选。是否使能流式推理，默认为非流式。json字符串例子： {  "messages": [  {  "role": "developer",  "content": "You are a helpful assistant."  },  {  "role": "user",  "content": "What is HarmonyOS"  }  ],  "stream": true } |

**变量**

| 名称 | 描述 |
| --- | --- |
| OH_QoS_GewuSession | 会话句柄。 起始版本： 20 |
| OH_QoS_GewuRequest | 请求句柄。 起始版本： 20 |

**枚举类型说明**

**QoS_Level**

```ets
enum QoS_Level
```

描述

描述QoS等级。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| QOS_BACKGROUND = 0 | 表示QoS等级为用户不可见任务。 |
| QOS_UTILITY | 表示QoS等级为后台重要任务。 |
| QOS_DEFAULT | 表示QoS等级为默认。 |
| QOS_USER_INITIATED | 表示QoS等级为用户触发任务。 |
| QOS_DEADLINE_REQUEST | 表示QoS等级为限时任务。 |
| QOS_USER_INTERACTIVE | 表示QoS等级为用户交互任务。 |

**OH_QoS_GewuErrorCode**

```ets
enum OH_QoS_GewuErrorCode
```

描述

格物错误码。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| OH_QOS_GEWU_OK = 0 | 成功 |
| OH_QOS_GEWU_NOPERM = 201 | 权限错误 |
| OH_QOS_GEWU_NOMEM = 203 | 内存错误 |
| OH_QOS_GEWU_INVAL = 401 | 参数错误 |
| OH_QOS_GEWU_EXIST = 501 | 已存在句柄 |
| OH_QOS_GEWU_NOENT = 502 | 找不到句柄 |
| OH_QOS_GEWU_NOSYS = 801 | 找不到符号 |
| OH_QOS_GEWU_FAULT = 901 | 其它错误 |

**函数说明**

**OH_QoS_SetThreadQoS()**

```ets
int OH_QoS_SetThreadQoS(QoS_Level level)
```

描述

为当前线程设置QoS等级。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| QoS_Level level | 表示设置的QoS等级，详细信息可以查看QoS_Level。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，失败返回负值。 |

参考：

[QoS_Level](qos.h.md#ZH-CN_TOPIC_0000002522241696__qos_level)

**OH_QoS_ResetThreadQoS()**

```ets
int OH_QoS_ResetThreadQoS()
```

描述

取消当前线程的QoS等级。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，失败返回负值。 |

参考：

[QoS_Level](qos.h.md#ZH-CN_TOPIC_0000002522241696__qos_level)

**OH_QoS_GetThreadQoS()**

```ets
int OH_QoS_GetThreadQoS(QoS_Level *level)
```

描述

获得当前线程的QoS等级。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| QoS_Level *level | 参数是输出参数，线程的QoS等级会以QoS_Level形式写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回0，失败返回负值。 |

参考：

[QoS_Level](qos.h.md#ZH-CN_TOPIC_0000002522241696__qos_level)

**OH_QoS_GewuOnResponse()**

```ets
typedef void (*OH_QoS_GewuOnResponse)(void* context, const char* response)
```

描述

用于接收回复的回调。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| void* context | 提交请求时指定的用户上下文句柄。 |
| const char* response | 回复的json字符串，包含以下参数： - message: 包含下列字段的消息。  - role: string. 消息的角色类型，应为"assistant".  - content: string。消息内容。 - finish_reason: string or null. 停止原因，可能的值如下：  - null: 表示没有停止。流式推理中会有多次回复，只有最后一次回复有非空的"finish_reason"。而非流式推理只有一次回复，且"finish_reason"非空。  - "stop": 正常停止。  - "abort": 用户主动提前中止。  - "length": token数超过限制。 |

**OH_QoS_GewuCreateSession()**

```ets
OH_QoS_GewuCreateSessionResult OH_QoS_GewuCreateSession(const char* attributes)
```

描述

创建格物会话。会话对象的生命周期从CreateSession函数返回开始，到调用DestroySession为止。会话属性的json字符串。该json字符串支持以下字段：- model: string. 表示会话使用的模型的路径。attributes json字符串例子：

{

 "model": "/data/storage/el2/base/files/qwen2/"

 }

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* attributes | 会话attributes的json字符串。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_QoS_GewuCreateSessionResult | 创建会话的结果。 |

**OH_QoS_GewuDestroySession()**

```ets
OH_QoS_GewuErrorCode OH_QoS_GewuDestroySession(OH_QoS_GewuSession session)
```

描述

销毁格物会话。建议用户应当等待至所有请求都已完成或中止，然后再调用该接口来销毁会话。如果调用该接口时还有正在进行的请求，那些请求将会被中止，且用户不会再收到回复。注意，在调用完该接口后，会话对象无法再被使用。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_QoS_GewuSession session | 要销毁的会话的句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_QoS_GewuErrorCode | 错误码  - 会话销毁成功，返回值为OH_QOS_GEWU_OK。  - 找不到会话返回OH_QOS_GEWU_NOENT。 |

**OH_QoS_GewuAbortRequest()**

```ets
OH_QoS_GewuErrorCode OH_QoS_GewuAbortRequest(OH_QoS_GewuSession session, OH_QoS_GewuRequest request)
```

描述

停止指定的请求。成功调用该函数后，client不会再收到该请求的回复，且该请求句柄无法再被使用。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_QoS_GewuSession session | 请求提交到的会话句柄。 |
| OH_QoS_GewuRequest request | 请求的句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_QoS_GewuErrorCode | 错误码。  - 成功停止请求返回OH_QOS_GEWU_OK。  - 找不到请求返回OH_QOS_GEWU_NOENT。 |

**OH_QoS_GewuSubmitRequest()**

```ets
OH_QoS_GewuSubmitRequestResult OH_QoS_GewuSubmitRequest(OH_QoS_GewuSession session, const char* request, OH_QoS_GewuOnResponse callback, void* context)
```

描述

提交请求。请求的json字符串，支持以下字段：- messages: array. 表示消息的数组其中每个元素支持以下字段：- role: string. 消息的角色类型。- "developer": 开发者或系统提供的指示。- "user":用户输入。- "assistant": 模型生成结果。- content: string. 消息内容。- stream: boolean or null; 可选。是否使能流式推理，默认为非流式。json字符串例子：

{

 "messages": [

 {

 "role": "developer",

 "content": "You are a helpful assistant."

 },

 {

 "role": "user",

 "content": "What is HarmonyOS"

 }

 ],

 "stream": true

}

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_QoS_GewuSession session | 会话句柄，表示请求要提交到哪个会话。 |
| const char* request | 请求的json字符串。 |
| OH_QoS_GewuOnResponse callback | 接受回复的回调。 |
| void* context | 要传给回调的用户上下文指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_QoS_GewuSubmitRequestResult | 格物提交请求结果。  - 提交请求成功，返回值OH_QoS_GewuSubmitRequestResult里的error为OH_QOS_GEWU_OK，request为请求句柄。  - 提交请求失败，返回值OH_QoS_GewuSubmitRequestResult里的error为错误原因，其中OH_QOS_GEWU_NOMEM表示没有足够的内存处理该请求。 |