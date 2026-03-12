# hidebug.h

#### 概述

定义HiDebug模块的调试功能。

**引用文件：** <hidebug/hidebug.h>

**库：** libohhidebug.so

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 12

**相关模块：**[HiDebug](HiDebug.md)

#### 汇总

#### 函数

名称typedef关键字描述[double OH_HiDebug_GetSystemCpuUsage()](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getsystemcpuusage)-获取系统的CPU资源占用情况百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。[double OH_HiDebug_GetAppCpuUsage()](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getappcpuusage)-获取进程的CPU使用率百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。[HiDebug_ThreadCpuUsagePtr OH_HiDebug_GetAppThreadCpuUsage()](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getappthreadcpuusage)-获取应用所有线程CPU使用情况。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。[void OH_HiDebug_FreeThreadCpuUsage(HiDebug_ThreadCpuUsagePtr *threadCpuUsage)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_freethreadcpuusage)-释放线程数据结构。[void OH_HiDebug_GetSystemMemInfo(HiDebug_SystemMemInfo *systemMemInfo)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getsystemmeminfo)-获取系统内存信息。[void OH_HiDebug_GetAppNativeMemInfo(HiDebug_NativeMemInfo *nativeMemInfo)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getappnativememinfo)-获取应用程序进程的内存信息。注意：由于该接口需要读取/proc/{pid}/smaps_rollup节点信息，耗时较长，建议不要在主线程中直接调用。[void OH_HiDebug_GetAppNativeMemInfoWithCache(HiDebug_NativeMemInfo *nativeMemInfo, bool forceRefresh)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getappnativememinfowithcache)-获取应用程序进程的内存信息，该接口存在缓存机制以提高接口性能。缓存值的有效期为5分钟。注意：由于该接口需要读取/proc/{pid}/smaps_rollup节点信息，耗时较长，建议不要在主线程中直接调用。[void OH_HiDebug_GetAppMemoryLimit(HiDebug_MemoryLimit *memoryLimit)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getappmemorylimit)-获取应用程序进程的内存限制。[HiDebug_ErrorCode OH_HiDebug_StartAppTraceCapture(HiDebug_TraceFlag flag, uint64_t tags, uint32_t limitSize, char* fileName, uint32_t length)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_startapptracecapture)-启动应用trace采集。[HiDebug_ErrorCode OH_HiDebug_StopAppTraceCapture()](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_stopapptracecapture)-停止采集应用程序trace。[HiDebug_ErrorCode OH_HiDebug_GetGraphicsMemory(uint32_t *value)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getgraphicsmemory)-获取应用GPU显存大小。注意：由于该接口涉及多次跨进程通信，其耗时可能超过1秒，建议不要在主线程中直接调用该接口。[int OH_HiDebug_BacktraceFromFp(HiDebug_Backtrace_Object object, void* startFp, void** pcArray, int size)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_backtracefromfp)-根据给定的fp地址进行栈回溯，该函数异步信号安全。[typedef void (*OH_HiDebug_SymbolicAddressCallback)(void* pc, void* arg, const HiDebug_StackFrame* frame)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddresscallback)OH_HiDebug_SymbolicAddressCallback若[OH_HiDebug_SymbolicAddress](zh-cn_topic_0000002497445692.html#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddress)接口调用成功，将通过该函数将解析后的栈信息返回给调用者。注意：由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。[HiDebug_ErrorCode OH_HiDebug_SymbolicAddress(HiDebug_Backtrace_Object object, void* pc, void* arg, OH_HiDebug_SymbolicAddressCallback callback)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddress)-通过给定的pc地址获取详细的符号信息，该函数非异步信号安全。[HiDebug_Backtrace_Object OH_HiDebug_CreateBacktraceObject(void)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_createbacktraceobject)-创建一个用于栈回溯及栈解析的对象，该函数非异步信号安全。[void OH_HiDebug_DestroyBacktraceObject(HiDebug_Backtrace_Object object)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_destroybacktraceobject)-销毁由[OH_HiDebug_CreateBacktraceObject](zh-cn_topic_0000002497445692.html#ZH-CN_TOPIC_0000002497445692__oh_hidebug_createbacktraceobject)创建的对象，以释放栈回溯及栈解析过程中申请的资源，该函数非异步信号安全。[HiDebug_ErrorCode OH_HiDebug_SetMallocDispatchTable(struct HiDebug_MallocDispatch *dispatchTable)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_setmallocdispatchtable)-设置基础库C库MallocDispatch表，用于替换开发者自定义的内存操作函数（例如：malloc/free/calloc/realloc/mmap/munmap)。MallocDispatch表是基础库C库中封装malloc/calloc/realloc/free等内存操作函数的结构体。HiDebug_MallocDispatch只是MallocDispatch结构体的一部分。[HiDebug_MallocDispatch* OH_HiDebug_GetDefaultMallocDispatchTable(void)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getdefaultmallocdispatchtable)-获取基础库C库当前默认MallocDispatch表，调用[OH_HiDebug_RestoreMallocDispatchTable](zh-cn_topic_0000002497445692.html#ZH-CN_TOPIC_0000002497445692__oh_hidebug_restoremallocdispatchtable)可恢复。[void OH_HiDebug_RestoreMallocDispatchTable(void)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_restoremallocdispatchtable)-恢复基础库C库MallocDispatch表。[HiDebug_ErrorCode OH_HiDebug_GetGraphicsMemorySummary(uint32_t interval, HiDebug_GraphicsMemorySummary *summary)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_getgraphicsmemorysummary)-获取应用显存占用的详细数据。[typedef void (*OH_HiDebug_ThreadLiteSamplingCallback)(const char* stacks)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_threadlitesamplingcallback)OH_HiDebug_ThreadLiteSamplingCallback轻量级Perf采样栈内容的回调函数定义。注意：采样数据仅在该回调函数执行期间有效，若需在函数外使用，务必对采样栈内容进行深拷贝。[HiDebug_ErrorCode OH_HiDebug_RequestThreadLiteSampling(HiDebug_ProcessSamplerConfig* config, OH_HiDebug_ThreadLiteSamplingCallback stacksCallback)](#ZH-CN_TOPIC_0000002497445692__oh_hidebug_requestthreadlitesampling)-对指定的数个线程进行Perf采样，并在调用结束后返回采样栈内容。注意：调用该函数后会阻塞当前线程，直至采样过程完全结束。系统对该接口的调用次数有严格限制，频繁调用超出限额后，将返回[HIDEBUG_RESOURCE_UNAVAILABLE](zh-cn_topic_0000002529285663.html#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)错误码。

#### 函数说明

#### OH_HiDebug_GetSystemCpuUsage()

```ets
double OH_HiDebug_GetSystemCpuUsage()
```

**描述**

获取系统的CPU资源占用情况百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**返回：**

类型说明double返回系统CPU资源占用情况百分比。如果返回结果为0，可能的原因是获取失败。

#### OH_HiDebug_GetAppCpuUsage()

```ets
double OH_HiDebug_GetAppCpuUsage()
```

**描述**

获取进程的CPU使用率百分比。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**返回：**

类型说明double返回进程的CPU使用率百分比。如果返回结果为0，可能因当前应用的CPU使用率过低导致。

#### OH_HiDebug_GetAppThreadCpuUsage()

```ets
HiDebug_ThreadCpuUsagePtr OH_HiDebug_GetAppThreadCpuUsage()
```

**描述**

获取应用所有线程CPU使用情况。注意：由于该接口涉及跨进程通信，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**返回：**

类型说明[HiDebug_ThreadCpuUsagePtr](HiDebug_ThreadCpuUsage.md)

返回所有线程CPU使用情况，见[HiDebug_ThreadCpuUsagePtr](HiDebug_ThreadCpuUsage.md)。

 若返回结果为null，可能因未获取到线程相关数据所致。

#### OH_HiDebug_FreeThreadCpuUsage()

```ets
void OH_HiDebug_FreeThreadCpuUsage(HiDebug_ThreadCpuUsagePtr *threadCpuUsage)
```

**描述**

释放线程数据结构。

**起始版本：** 12

**参数：**

参数项描述[HiDebug_ThreadCpuUsagePtr](HiDebug_ThreadCpuUsage.md) *threadCpuUsage应用的所有线程可用CPU使用缓冲区指针，见[HiDebug_ThreadCpuUsagePtr](HiDebug_ThreadCpuUsage.md)。传入的参数是要由OH_HiDebug_GetAppThreadCpuUsage()得到的。

#### OH_HiDebug_GetSystemMemInfo()

```ets
void OH_HiDebug_GetSystemMemInfo(HiDebug_SystemMemInfo *systemMemInfo)
```

**描述**

获取系统内存信息。

**起始版本：** 12

**参数：**

参数项描述[HiDebug_SystemMemInfo](HiDebug_SystemMemInfo.md) *systemMemInfo表示指向[HiDebug_SystemMemInfo](HiDebug_SystemMemInfo.md)。函数调用后，若结构体数据为空，则表明调用失败。

#### OH_HiDebug_GetAppNativeMemInfo()

```ets
void OH_HiDebug_GetAppNativeMemInfo(HiDebug_NativeMemInfo *nativeMemInfo)
```

**描述**

获取应用程序进程的内存信息。注意：由于该接口需要读取/proc/{pid}/smaps_rollup节点信息，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 12

**参数：**

参数项描述[HiDebug_NativeMemInfo](HiDebug_NativeMemInfo.md) *nativeMemInfo表示指向[HiDebug_NativeMemInfo](HiDebug_NativeMemInfo.md)。函数调用后，若结构体数据为空，则表明调用失败。

#### OH_HiDebug_GetAppNativeMemInfoWithCache()

```ets
void OH_HiDebug_GetAppNativeMemInfoWithCache(HiDebug_NativeMemInfo *nativeMemInfo, bool forceRefresh)
```

**描述**

获取应用程序进程的内存信息，该接口存在缓存机制以提高接口性能。缓存值的有效期为5分钟。注意：由于该接口需要读取/proc/{pid}/smaps_rollup节点信息，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 20

**参数：**

参数项描述[HiDebug_NativeMemInfo](HiDebug_NativeMemInfo.md) *nativeMemInfo表示指向[HiDebug_NativeMemInfo](HiDebug_NativeMemInfo.md)。函数调用后，若结构体数据为空，则表明调用失败。bool forceRefresh

是否需要无视缓存有效性，强制更新缓存值。

 当为true时，直接获取当前内存数据并更新缓存值；

 当为false时，缓存有效时，直接返回缓存值，缓存失效时，获取当前内存数据并更新缓存值。

#### OH_HiDebug_GetAppMemoryLimit()

```ets
void OH_HiDebug_GetAppMemoryLimit(HiDebug_MemoryLimit *memoryLimit)
```

**描述**

获取应用程序进程的内存限制。

**起始版本：** 12

**参数：**

参数项描述[HiDebug_MemoryLimit](HiDebug_MemoryLimit.md) *memoryLimit表示指向[HiDebug_MemoryLimit](HiDebug_MemoryLimit.md)。函数调用后，若结构体数据为空，则表明调用失败。

#### OH_HiDebug_StartAppTraceCapture()

```ets
HiDebug_ErrorCode OH_HiDebug_StartAppTraceCapture(HiDebug_TraceFlag flag, uint64_t tags, uint32_t limitSize, char* fileName, uint32_t length)
```

**描述**

启动应用trace采集。

**起始版本：** 12

**参数：**

参数项描述[HiDebug_TraceFlag](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_traceflag) flag采集线程trace方式。uint64_t tags采集trace场景标签。uint32_t limitSizetrace文件的最大大小（以字节为单位），最大为 500MB。char* fileName输出trace文件名缓冲区。uint32_t length输出trace文件名缓冲区长度。

**返回：**

类型说明[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)

0 - 成功。

[HIDEBUG_INVALID_ARGUMENT](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode) 401 - fileName参数为空指针或者传入的length参数过小或者limitSize参数小于等于0。

 11400102 - 已经开启了一个trace。

 11400103 - 没有权限去开启trace。

 11400104 - 系统内部错误。

#### OH_HiDebug_StopAppTraceCapture()

```ets
HiDebug_ErrorCode OH_HiDebug_StopAppTraceCapture()
```

**描述**

停止采集应用程序trace。

**起始版本：** 12

**返回：**

类型说明[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)

0 - 成功。

 11400104 - 系统内部错误。

 11400105 - 当前没有trace正在运行

#### OH_HiDebug_GetGraphicsMemory()

```ets
HiDebug_ErrorCode OH_HiDebug_GetGraphicsMemory(uint32_t *value)
```

**描述**

获取应用GPU显存大小。注意：由于该接口涉及多次跨进程通信，其耗时可能超过1秒，建议不要在主线程中直接调用该接口。

**起始版本：** 14

**参数：**

参数项描述uint32_t *value指向用来保存接口获取到的应用显存大小（单位KB）的变量的指针。

**返回：**

类型说明[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)

0 - 接口获取成功。

 401 - 无效参数，所传递参数为空指针。

 11400104 - 系统内部错误。

#### OH_HiDebug_BacktraceFromFp()

```ets
int OH_HiDebug_BacktraceFromFp(HiDebug_Backtrace_Object object, void* startFp, void** pcArray, int size)
```

**描述**

根据给定的fp地址进行栈回溯，该函数异步信号安全。

**起始版本：** 20

**参数：**

参数项描述[HiDebug_Backtrace_Object](HiDebug_Backtrace_Object___.md) object由[OH_HiDebug_CreateBacktraceObject](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_createbacktraceobject)接口获取到的用来栈回溯的对象。void* startFp栈回溯的起始栈帧地址。void** pcArray保存栈回溯得到的pc地址的数组。int size保存栈回溯得到的pc地址的数组长度。

**返回：**

类型说明int成功回溯并写入到pcArray中的栈帧数量。如果返回结果为0，原因可能是栈回溯失败。

#### OH_HiDebug_SymbolicAddressCallback()

```ets
typedef void (*OH_HiDebug_SymbolicAddressCallback)(void* pc, void* arg, const HiDebug_StackFrame* frame)
```

**描述**

若[OH_HiDebug_SymbolicAddress](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddress)接口调用成功，将通过该函数将解析后的栈信息返回给调用者。注意：由于该接口涉及多次IO操作，耗时较长，建议不要在主线程中直接调用。

**起始版本：** 20

**参数：**

参数项描述void* pc传入[OH_HiDebug_SymbolicAddress](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddress)接口的需要解析的pc地址。void* arg传入[OH_HiDebug_SymbolicAddress](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddress)接口的arg值。[ const HiDebug_StackFrame](HiDebug_StackFrame.md)* frame由传入[OH_HiDebug_SymbolicAddress](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddress)接口的pc地址解析后的得到栈信息[HiDebug_StackFrame](HiDebug_StackFrame.md)指针，该指针指向内容仅在该函数作用域内有效。

#### OH_HiDebug_SymbolicAddress()

```ets
HiDebug_ErrorCode OH_HiDebug_SymbolicAddress(HiDebug_Backtrace_Object object, void* pc, void* arg, OH_HiDebug_SymbolicAddressCallback callback)
```

**描述**

通过给定的pc地址获取详细的符号信息，该函数非异步信号安全。

**起始版本：** 20

**参数：**

参数项描述[HiDebug_Backtrace_Object](HiDebug_Backtrace_Object___.md) object由[OH_HiDebug_CreateBacktraceObject](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_createbacktraceobject)接口创建的对象。void* pc由[OH_HiDebug_BacktraceFromFp](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_backtracefromfp)接口获取到的pc地址。void* arg保留的自定义参数，符号解析成功后系统内部会将该参数传递给回调函数[OH_HiDebug_SymbolicAddressCallback](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddresscallback)。[OH_HiDebug_SymbolicAddressCallback](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_symbolicaddresscallback) callback用于返回解析后栈信息的回调函数。

**返回：**

类型说明[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)

返回结果具体可参考[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)：

[HIDEBUG_SUCCESS](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode) 成功获取到详细的栈信息，且该函数传入的callback被调用。

[HIDEBUG_INVALID_ARGUMENT](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode) 无效参数。

[HIDEBUG_INVALID_SYMBOLIC_PC_ADDRESS](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode) 无法根据传入的pc地址找到对应的符号。

#### OH_HiDebug_CreateBacktraceObject()

```ets
HiDebug_Backtrace_Object OH_HiDebug_CreateBacktraceObject(void)
```

**描述**

创建一个用于栈回溯及栈解析的对象，该函数非异步信号安全。

**起始版本：** 20

**返回：**

类型说明[HiDebug_Backtrace_Object](HiDebug_Backtrace_Object___.md)返回创建的对象的指针，当创建失败时返回NULL。

#### OH_HiDebug_DestroyBacktraceObject()

```ets
void OH_HiDebug_DestroyBacktraceObject(HiDebug_Backtrace_Object object)
```

**描述**

销毁由[OH_HiDebug_CreateBacktraceObject](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_createbacktraceobject)创建的对象，以释放栈回溯及栈解析过程中申请的资源，该函数非异步信号安全。

**起始版本：** 20

**参数：**

参数项描述[HiDebug_Backtrace_Object](HiDebug_Backtrace_Object___.md) object需要被销毁的对象。

#### OH_HiDebug_SetMallocDispatchTable()

```ets
HiDebug_ErrorCode OH_HiDebug_SetMallocDispatchTable(struct HiDebug_MallocDispatch *dispatchTable)
```

**描述**

设置基础库C库MallocDispatch表，用于替换开发者自定义的内存操作函数（例如：malloc/free/calloc/realloc/mmap/munmap)。MallocDispatch表是基础库C库中封装malloc/calloc/realloc/free等内存操作函数的结构体。HiDebug_MallocDispatch只是MallocDispatch结构体的一部分。

**起始版本：** 20

**参数：**

参数项描述[struct HiDebug_MallocDispatch](HiDebug_MallocDispatch.md) *dispatchTable指向开发者自定义内存操作函数[HiDebug_MallocDispatch](HiDebug_MallocDispatch.md)结构体指针。

**返回：**

类型说明[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)

返回结果具体可参考[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)：

[HIDEBUG_SUCCESS](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode) 成功设置自定义内存操作函数。

[HIDEBUG_INVALID_ARGUMENT](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode) 无效参数。

#### OH_HiDebug_GetDefaultMallocDispatchTable()

```ets
HiDebug_MallocDispatch* OH_HiDebug_GetDefaultMallocDispatchTable(void)
```

**描述**

获取基础库C库当前默认MallocDispatch表，调用[OH_HiDebug_RestoreMallocDispatchTable](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_restoremallocdispatchtable)可恢复。

**起始版本：** 20

**返回：**

类型说明[HiDebug_MallocDispatch*](HiDebug_MallocDispatch.md)当前C库默认的[HiDebug_MallocDispatch](HiDebug_MallocDispatch.md)结构体指针。

#### OH_HiDebug_RestoreMallocDispatchTable()

```ets
void OH_HiDebug_RestoreMallocDispatchTable(void)
```

**描述**

恢复基础库C库MallocDispatch表。

**起始版本：** 20

#### OH_HiDebug_GetGraphicsMemorySummary()

```ets
HiDebug_ErrorCode OH_HiDebug_GetGraphicsMemorySummary(uint32_t interval, HiDebug_GraphicsMemorySummary *summary)
```

**描述**

获取应用显存占用的详细数据。

**起始版本：** 21

**参数：**

参数项描述uint32_t interval

当显存数据缓存值存在时间超过设定间隔interval（单位：秒）时，接口会获取最新的显存数据并更新缓存；否则，接口将直接返回缓存值。

 interval的取值范围为[2，3600]，若传入的interval超出取值范围时，将使用300作为默认值。

[HiDebug_GraphicsMemorySummary](HiDebug_GraphicsMemorySummary.md) *summary表示指向[HiDebug_GraphicsMemorySummary](HiDebug_GraphicsMemorySummary.md)的指针。

**返回：**

类型说明[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)

返回结果具体可参考[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)：

 HIDEBUG_SUCCESS 成功获取到应用显存数据。

 HIDEBUG_INVALID_ARGUMENT 无效参数。

 HIDEBUG_TRACE_ABNORMAL 系统内部错误。

#### OH_HiDebug_ThreadLiteSamplingCallback()

```ets
typedef void (*OH_HiDebug_ThreadLiteSamplingCallback)(const char* stacks)
```

**描述**

轻量级Perf采样栈内容的回调函数定义。注意：采样数据仅在该回调函数执行期间有效，若需在函数外使用，务必对采样栈内容进行深拷贝。

**起始版本：** 22

**参数：**

参数项描述const char* stacks采样得到的调用栈内容。

#### OH_HiDebug_RequestThreadLiteSampling()

```ets
HiDebug_ErrorCode OH_HiDebug_RequestThreadLiteSampling(HiDebug_ProcessSamplerConfig* config, OH_HiDebug_ThreadLiteSamplingCallback stacksCallback)
```

**描述**

对指定的数个线程进行Perf采样，并在调用结束后返回采样栈内容。注意：调用该函数后会阻塞当前线程，直至采样过程完全结束。系统对该接口的调用次数有严格限制，频繁调用超出限额后，将返回[HIDEBUG_RESOURCE_UNAVAILABLE](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)错误码。

**起始版本：** 22

**参数：**

参数项描述[HiDebug_ProcessSamplerConfig](HiDebug_ProcessSamplerConfig.md)* config指向Perf采样配置结构体[HiDebug_ProcessSamplerConfig](HiDebug_ProcessSamplerConfig.md)的指针。[OH_HiDebug_ThreadLiteSamplingCallback](hidebug.h.md#ZH-CN_TOPIC_0000002497445692__oh_hidebug_threadlitesamplingcallback) stacksCallback采样结束时的回调函数，用于返回采样结果。

**返回：**

类型说明[HiDebug_ErrorCode](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_errorcode)

返回结果码：

 HIDEBUG_SUCCESS：采样成功完成。

HIDEBUG_INVALID_ARGUMENT：无效参数。

 HIDEBUG_NOT_SUPPORTED：当前设备不支持Perf采样。

 HIDEBUG_UNDER_SAMPLING：已有采样任务正在执行中。

 HIDEBUG_RESOURCE_UNAVAILABLE：采样资源不足或已达调用上限。