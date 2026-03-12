# ohprint.h

#### 概述

声明用于发现和连接打印机、从打印机打印文件、查询已添加打印机的列表及其中的打印机信息等API。

**引用文件：** <BasicServicesKit/ohprint.h>

**库：** libohprint.so

**系统能力：** SystemCapability.Print.PrintFramework

**起始版本：** 12

**相关模块：**[OH_Print](OH_Print.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Print_Margin](Print_Margin.md)Print_Margin打印边距。[Print_PageSize](Print_PageSize.md)Print_PageSize纸张大小信息。[Print_Range](Print_Range.md)Print_Range打印范围。[Print_PrintAttributes](Print_PrintAttributes.md)Print_PrintAttributes打印属性结构体。[Print_PrintDocCallback](Print_PrintDocCallback.md)Print_PrintDocCallback打印文档任务回调结构体。

#### 枚举

名称typedef关键字描述[Print_ErrorCode](#ZH-CN_TOPIC_0000002497445554__print_errorcode)Print_ErrorCode枚举错误码。[Print_JobDocAdapterState](#ZH-CN_TOPIC_0000002497445554__print_jobdocadapterstate)Print_JobDocAdapterState打印文档任务的状态。

#### 函数

名称typedef关键字描述[typedef void(*Print_WriteResultCallback)(const char *jobId, uint32_t code)](#ZH-CN_TOPIC_0000002497445554__print_writeresultcallback)Print_WriteResultCallback文件回写回调。[typedef void(*Print_OnStartLayoutWrite)(const char *jobId, uint32_t fd, const Print_PrintAttributes *oldAttrs, const Print_PrintAttributes *newAttrs, Print_WriteResultCallback writeCallback)](#ZH-CN_TOPIC_0000002497445554__print_onstartlayoutwrite)Print_OnStartLayoutWrite文件开始回写回调函数。[typedef void(*Print_OnJobStateChanged)(const char *jobId, uint32_t state)](#ZH-CN_TOPIC_0000002497445554__print_onjobstatechanged)Print_OnJobStateChanged打印任务状态回调。[Print_ErrorCode OH_Print_StartPrintByNative(const char *printJobName, Print_PrintDocCallback printDocCallback, void *context)](#ZH-CN_TOPIC_0000002497445554__oh_print_startprintbynative)-拉起打印预览界面接口。

#### 枚举类型说明

#### Print_ErrorCode

```ets
enum Print_ErrorCode
```

**描述**

枚举错误码。

**起始版本：** 12

枚举项描述PRINT_ERROR_NONE = 0成功。PRINT_ERROR_NO_PERMISSION = 201没有权限。PRINT_ERROR_INVALID_PARAMETER = 401无效参数。PRINT_ERROR_GENERIC_FAILURE = 24300001内部错误。PRINT_ERROR_RPC_FAILURE = 24300002rpc传输错误。PRINT_ERROR_SERVER_FAILURE = 24300003打印服务错误。PRINT_ERROR_INVALID_EXTENSION = 24300004无效打印扩展。PRINT_ERROR_INVALID_PRINTER = 24300005无效打印机。PRINT_ERROR_INVALID_PRINT_JOB = 24300006无效打印任务。PRINT_ERROR_FILE_IO = 24300007文件读写错误。PRINT_ERROR_UNKNOWN = 24300255未知错误。

#### Print_JobDocAdapterState

```ets
enum Print_JobDocAdapterState
```

**描述**

打印文档任务的状态。

**起始版本：** 13

枚举项描述PRINT_DOC_ADAPTER_PREVIEW_ABILITY_DESTROY = 0打印预览界面销毁。PRINT_DOC_ADAPTER_PRINT_TASK_SUCCEED = 1打印任务执行成功。PRINT_DOC_ADAPTER_PRINT_TASK_FAIL = 2打印任务执行失败。PRINT_DOC_ADAPTER_PRINT_TASK_CANCEL = 3打印任务被取消。PRINT_DOC_ADAPTER_PRINT_TASK_BLOCK = 4打印任务阻塞。PRINT_DOC_ADAPTER_PREVIEW_ABILITY_DESTROY_FOR_CANCELED = 5预览界面点击取消按钮界面退出。PRINT_DOC_ADAPTER_PREVIEW_ABILITY_DESTROY_FOR_STARTED = 6预览界面点击打印按钮界面退出。

#### 函数说明

#### Print_WriteResultCallback()

```ets
typedef void(*Print_WriteResultCallback)(const char *jobId, uint32_t code)
```

**描述**

文件回写回调。

**起始版本：** 13

**参数：**

参数项描述const char *jobId打印任务id。uint32_t code文件回写结果。

#### Print_OnStartLayoutWrite()

```ets
typedef void(*Print_OnStartLayoutWrite)(const char *jobId, uint32_t fd, const Print_PrintAttributes *oldAttrs, const Print_PrintAttributes *newAttrs, Print_WriteResultCallback writeCallback)
```

**描述**

文件开始回写回调函数。

**起始版本：** 13

**参数：**

参数项描述const char *jobId打印任务id。uint32_t fd回写的文件句柄。[ const Print_PrintAttributes](Print_PrintAttributes.md) *oldAttrs用户设置打印参数变化前的参数。[ const Print_PrintAttributes](Print_PrintAttributes.md) *newAttrs用户设置打印参数变化后的参数。[ Print_WriteResultCallback](ohprint.h.md#ZH-CN_TOPIC_0000002497445554__print_writeresultcallback) writeCallback使用方回写完文件后调用回调函数通知打印服务。

#### Print_OnJobStateChanged()

```ets
typedef void(*Print_OnJobStateChanged)(const char *jobId, uint32_t state)
```

**描述**

打印任务状态回调。

**起始版本：** 13

**参数：**

参数项描述const char *jobId打印任务id。uint32_t state当前任务状态。

#### OH_Print_StartPrintByNative()

```ets
Print_ErrorCode OH_Print_StartPrintByNative(const char *printJobName, Print_PrintDocCallback printDocCallback, void *context)
```

**描述**

拉起打印预览界面接口。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 13

**参数：**

参数项描述const char *printJobName打印任务名称。[Print_PrintDocCallback](Print_PrintDocCallback.md) printDocCallback打印文档任务回调结构体。void *context调用接口的ability的上下文。

**返回：**

类型说明[Print_ErrorCode](ohprint.h.md#ZH-CN_TOPIC_0000002497445554__print_errorcode)

返回 [Print_ErrorCode](ohprint.h.md#ZH-CN_TOPIC_0000002497445554__print_errorcode) 执行成功。

[PRINT_ERROR_NO_PERMISSION](ohprint.h.md#ZH-CN_TOPIC_0000002497445554__print_errorcode) 需要配置 ohos.permission.PRINT 权限。

[PRINT_ERROR_RPC_FAILURE](ohprint.h.md#ZH-CN_TOPIC_0000002497445554__print_errorcode) 无法连接打印服务。