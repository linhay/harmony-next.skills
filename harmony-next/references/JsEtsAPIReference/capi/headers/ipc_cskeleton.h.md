# ipc_cskeleton.h

#### 概述

提供IPC框架tokenId、凭据、PID/UID、线程池配置等功能C接口。

**引用文件：** <IPCKit/ipc_cskeleton.h>

**库：** libipc_capi.so

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：**[OHIPCSkeleton](../../topics/misc/OHIPCSkeleton.md)

#### 汇总

#### 函数

名称描述[void OH_IPCSkeleton_JoinWorkThread(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_joinworkthread)当前线程加入IPC工作线程池。[void OH_IPCSkeleton_StopWorkThread(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_stopworkthread)当前线程退出IPC工作线程池。[uint64_t OH_IPCSkeleton_GetCallingTokenId(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_getcallingtokenid)获取调用方TokenId。该接口需要在IPC上下文中调用，否则返回自身TokenId。[uint64_t OH_IPCSkeleton_GetFirstTokenId(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_getfirsttokenid)获取首调者TokenId。[uint64_t OH_IPCSkeleton_GetSelfTokenId(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_getselftokenid)获取自身TokenId。[uint64_t OH_IPCSkeleton_GetCallingPid(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_getcallingpid)获取调用方进程ID。该接口需要在IPC上下文中调用，否则返回当前进程ID。[uint64_t OH_IPCSkeleton_GetCallingUid(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_getcallinguid)获取调用方用户ID。该接口需要在IPC上下文中调用，否则返回当前用户ID。[int OH_IPCSkeleton_IsLocalCalling(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_islocalcalling)判断是否正在进行本地调用。[int OH_IPCSkeleton_SetMaxWorkThreadNum(const int maxThreadNum)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_setmaxworkthreadnum)设置最大工作线程数。[int OH_IPCSkeleton_ResetCallingIdentity(char **identity, int32_t *len, OH_IPC_MemAllocator allocator)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_resetcallingidentity)重置调用方身份凭证为自身进程的身份凭证（包括tokenid、UID和PID信息），并返回调用方的凭证信息。 该信息主要用于OH_IPCSkeleton_SetCallingIdentity接口调用。[int OH_IPCSkeleton_SetCallingIdentity(const char *identity)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_setcallingidentity)恢复调用方凭证信息至IPC上下文中。[int OH_IPCSkeleton_IsHandlingTransaction(void)](#ZH-CN_TOPIC_0000002529285301__oh_ipcskeleton_ishandlingtransaction)是否正在处理IPC请求。

#### 函数说明

#### OH_IPCSkeleton_JoinWorkThread()

```ets
void OH_IPCSkeleton_JoinWorkThread(void)
```

**描述：**

当前线程加入IPC工作线程池。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

#### OH_IPCSkeleton_StopWorkThread()

```ets
void OH_IPCSkeleton_StopWorkThread(void)
```

**描述：**

当前线程退出IPC工作线程池。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

#### OH_IPCSkeleton_GetCallingTokenId()

```ets
uint64_t OH_IPCSkeleton_GetCallingTokenId(void)
```

**描述：**

获取调用方TokenId。该接口需要在IPC上下文中调用，否则返回自身TokenId。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

类型说明uint64_t返回调用方TokenId。

#### OH_IPCSkeleton_GetFirstTokenId()

```ets
uint64_t OH_IPCSkeleton_GetFirstTokenId(void)
```

**描述：**

获取首调者TokenId。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

类型说明uint64_t返回首调者TokenId。

#### OH_IPCSkeleton_GetSelfTokenId()

```ets
uint64_t OH_IPCSkeleton_GetSelfTokenId(void)
```

**描述：**

获取自身TokenId。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

类型说明uint64_t返回自身TokenId。

#### OH_IPCSkeleton_GetCallingPid()

```ets
uint64_t OH_IPCSkeleton_GetCallingPid(void)
```

**描述：**

获取调用方进程ID。该接口需要在IPC上下文中调用，否则返回当前进程ID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

类型说明uint64_t返回调用方进程ID。

#### OH_IPCSkeleton_GetCallingUid()

```ets
uint64_t OH_IPCSkeleton_GetCallingUid(void)
```

**描述：**

获取调用方用户ID。该接口需要在IPC上下文中调用，否则返回当前用户ID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

类型说明uint64_t返回调用方用户ID。

#### OH_IPCSkeleton_IsLocalCalling()

```ets
int OH_IPCSkeleton_IsLocalCalling(void)
```

**描述：**

判断是否正在进行本地调用。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

类型说明int正在进行本地调用，返回1；否则，返回0。

#### OH_IPCSkeleton_SetMaxWorkThreadNum()

```ets
int OH_IPCSkeleton_SetMaxWorkThreadNum(const int maxThreadNum)
```

**描述：**

设置最大工作线程数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

参数项描述const int maxThreadNummaxThreadNum 最大工作线程数，默认16，范围:[1, 32]。

**返回：**

类型说明int

成功返回[OH_IPC_ErrorCode#OH_IPC_SUCCESS](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)；

 参数错误返回[OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)；

 其它情况返回[OH_IPC_ErrorCode#OH_IPC_INNER_ERROR](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)。

#### OH_IPCSkeleton_ResetCallingIdentity()

```ets
int OH_IPCSkeleton_ResetCallingIdentity(char **identity, int32_t *len, OH_IPC_MemAllocator allocator)
```

**描述：**

重置调用方身份凭证为自身进程的身份凭证（包括tokenid、UID和PID信息），并返回调用方的凭证信息。 该信息主要用于OH_IPCSkeleton_SetCallingIdentity接口调用。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

参数项描述char **identityidentity 用于存储调凭证的内存地址，该内存由用户提供的分配器进行内存分配，用户使用完后需要主动释放，不能为空。int32_t *lenlen 写入identity的数据长度，不能为空。[OH_IPC_MemAllocator](ipc_cparcel.h.md#ZH-CN_TOPIC_0000002497605308__oh_ipc_memallocator) allocatorallocator 用户指定的用来分配identity的内存分配器，不能为空。

**返回：**

类型说明int

成功返回[OH_IPC_ErrorCode#OH_IPC_SUCCESS](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)；

 参数错误返回[OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)；

 内存分配失败返回[OH_IPC_ErrorCode#OH_IPC_MEM_ALLOCATOR_ERROR](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)；

 其它情况返回[OH_IPC_ErrorCode#OH_IPC_INNER_ERROR](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)。

#### OH_IPCSkeleton_SetCallingIdentity()

```ets
int OH_IPCSkeleton_SetCallingIdentity(const char *identity)
```

**描述：**

恢复调用方凭证信息至IPC上下文中。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

参数项描述const char *identityidentity 调用方凭证，不能为空。来源于OH_IPCSkeleton_ResetCallingIdentity的返回值。

**返回：**

类型说明int

成功返回[OH_IPC_ErrorCode#OH_IPC_SUCCESS](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)；

 参数错误返回[OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)；

 其它情况返回[OH_IPC_ErrorCode#OH_IPC_INNER_ERROR](ipc_error_code.h.md#ZH-CN_TOPIC_0000002529445275__oh_ipc_errorcode)。

#### OH_IPCSkeleton_IsHandlingTransaction()

```ets
int OH_IPCSkeleton_IsHandlingTransaction(void)
```

**描述：**

是否正在处理IPC请求。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

类型说明int正在处理IPC请求，返回1；否则，返回0。