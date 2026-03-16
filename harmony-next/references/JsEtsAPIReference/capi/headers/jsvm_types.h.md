# jsvm_types.h

#### 概述

提供JSVM-API类型定义。通过API接口为开发者提供独立、标准、完整的JavaScript引擎能力，包括管理引擎生命周期、编译运行JS代码、实现JS/C++跨语言调用、拍摄快照等。

**引用文件：** <ark_runtime/jsvm_types.h>

**库：** libjsvm.so

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：**[JSVM](../../topics/misc/JSVM.md)

#### 汇总

#### 结构体

名称typedef关键字描述[JSVM_CallbackStruct](../../topics/misc/JSVM_CallbackStruct.md)JSVM_CallbackStruct用户提供的native回调函数的指针和数据，这些函数通过JSVM-API接口暴露给JavaScript。[JSVM_HeapStatistics](../../topics/misc/JSVM_HeapStatistics.md)JSVM_HeapStatistics用于保存有关JavaScript堆内存使用情况的统计信息。[JSVM_InitOptions](../../topics/misc/JSVM_InitOptions.md)JSVM_InitOptions初始化选项，用于初始化JavaScript虚拟机。[JSVM_CreateVMOptions](../../topics/misc/JSVM_CreateVMOptions.md)JSVM_CreateVMOptions创建JavaScript虚拟机的选项。[JSVM_VMInfo](../../topics/misc/JSVM_VMInfo.md)JSVM_VMInfoJavaScript虚拟机信息。[JSVM_PropertyDescriptor](../../topics/misc/JSVM_PropertyDescriptor.md)JSVM_PropertyDescriptor属性描述符。[JSVM_ExtendedErrorInfo](../../topics/misc/JSVM_ExtendedErrorInfo.md)JSVM_ExtendedErrorInfo扩展的异常信息。[JSVM_TypeTag](../../topics/misc/JSVM_TypeTag.md)JSVM_TypeTag类型标记，存储为两个无符号64位整数的128位值。作为一个UUID，通过它，JavaScript对象可以是"tagged"，以确保它们的类型保持不变。[JSVM_PropertyHandlerConfigurationStruct](../../topics/misc/JSVM_PropertyHandlerConfigurationStruct.md)JSVM_PropertyHandlerConfigurationStruct当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。[JSVM_ScriptOrigin](../../topics/misc/JSVM_ScriptOrigin.md)JSVM_ScriptOrigin某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。[JSVM_PropertyHandler](../../topics/misc/JSVM_PropertyHandler.md)JSVM_PropertyHandler包含将class作为函数进行调用时所触发的回调函数的函数指针和访问实例对象属性时触发的回调函数的函数指针集。[JSVM_DefineClassOptions](../../topics/misc/JSVM_DefineClassOptions.md)JSVM_DefineClassOptions定义Class的选项。[JSVM_VM__*](../../topics/misc/JSVM_VM___.md)JSVM_VM表示JavaScript虚拟机实例。[JSVM_VMScope__*](../../topics/misc/JSVM_VMScope___.md)JSVM_VMScope表示JavaScript虚拟机作用域。[JSVM_EnvScope__*](../../topics/misc/JSVM_EnvScope___.md)JSVM_EnvScope表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH_JSVM_OpenEnvScope进入该环境的JSVM_EnvScope后，该环境才对线程的虚拟机实例可用。[JSVM_Script__*](../../topics/misc/JSVM_Script___.md)JSVM_Script表示一段JavaScript代码。[JSVM_Env__*](../../topics/misc/JSVM_Env___.md)JSVM_Env表示虚拟机特定状态的上下文环境，需要在调用native函数时作为参数传递，并且传递给后续任何的JSVM-API嵌套调用。[JSVM_CpuProfiler__*](../../topics/misc/JSVM_CpuProfiler___.md)JSVM_CpuProfiler表示一个JavaScript CPU时间性能分析器。[JSVM_Value__*](../../topics/misc/JSVM_Value___.md)JSVM_Value表示JavaScript值。[JSVM_Data__*](../../topics/misc/JSVM_Data___.md)JSVM_Data表示一个 JavaScript Data。[JSVM_Ref__*](../../topics/misc/JSVM_Ref___.md)JSVM_Ref表示JavaScript值的引用。[JSVM_HandleScope__*](../../topics/misc/JSVM_HandleScope___.md)JSVM_HandleScope表示JavaScript值的作用域，用于控制和修改在特定范围内创建的对象的生命周期。通常，JSVM-API值是在JSVM_HandleScope的上下文中创建的。当从JavaScript调用native方法时，将存在默认JSVM_HandleScope。如果用户没有显式创建新的JSVM_HandleScope，将在默认JSVM_HandleScope中创建JSVM-API值。对于native方法执行之外的任何代码调用（例如，在libuv回调调用期间），模块需要在调用任何可能导致创建JavaScript值的函数之前创建一个作用域。JSVM_HandleScope是使用OH_JSVM_OpenHandleScope创建的，并使用OH_JSVM_CloseHandleScope销毁的。关闭作用域代表向GC指示在JSVM_HandleScope作用域的生命周期内创建的所有JSVM_Value将不再从当前堆的栈帧中引用。[JSVM_EscapableHandleScope__*](../../topics/misc/JSVM_EscapableHandleScope___.md)JSVM_EscapableHandleScope表示一种特殊类型的handle scope，用于将在特定handle scope内创建的值返回到父作用域。[JSVM_CallbackInfo__*](../../topics/misc/JSVM_CallbackInfo___.md)JSVM_CallbackInfo表示传递给回调函数的不透明数据类型。可用于获取调用该函数的上下文的附加信息。[JSVM_Deferred__*](../../topics/misc/JSVM_Deferred___.md)JSVM_Deferred表示Promise延迟对象。[JSVM_PropertyHandlerConfigurationStruct*](../../topics/misc/JSVM_PropertyHandlerConfigurationStruct_.md)JSVM_PropertyHandlerCfg包含属性监听回调的结构的指针类型。[JSVM_CallbackStruct*](../../topics/misc/JSVM_CallbackStruct_.md)JSVM_Callback用户提供的native函数的函数指针类型，这些函数通过JSVM-API接口暴露给JavaScript。[JSVM_CompileProfile](../../topics/misc/JSVM_CompileProfile.md)JSVM_CompileProfile与JSVM_COMPILE_COMPILE_PROFILE一起传递的编译采样文件。

#### 枚举

名称typedef关键字描述[JSVM_PropertyAttributes](#ZH-CN_TOPIC_0000002497446184__jsvm_propertyattributes)JSVM_PropertyAttributes用于控制JavaScript对象属性的行为。[JSVM_ValueType](#ZH-CN_TOPIC_0000002497446184__jsvm_valuetype)JSVM_ValueType描述JSVM_Value的类型。[JSVM_TypedarrayType](#ZH-CN_TOPIC_0000002497446184__jsvm_typedarraytype)JSVM_TypedarrayType描述TypedArray的类型。[JSVM_Status](#ZH-CN_TOPIC_0000002497446184__jsvm_status)JSVM_Status表示JSVM-API调用成功或失败的完整状态码。[JSVM_KeyCollectionMode](#ZH-CN_TOPIC_0000002497446184__jsvm_keycollectionmode)JSVM_KeyCollectionMode限制查找属性的范围。[JSVM_KeyFilter](#ZH-CN_TOPIC_0000002497446184__jsvm_keyfilter)JSVM_KeyFilter属性过滤器，可以通过使用or来构造一个复合过滤器。[JSVM_KeyConversion](#ZH-CN_TOPIC_0000002497446184__jsvm_keyconversion)JSVM_KeyConversion键转换选项。[JSVM_MemoryPressureLevel](#ZH-CN_TOPIC_0000002497446184__jsvm_memorypressurelevel)JSVM_MemoryPressureLevel内存压力水平。[JSVM_RegExpFlags](#ZH-CN_TOPIC_0000002497446184__jsvm_regexpflags)JSVM_RegExpFlags正则表达式标志位。它们可以用来启用一组标志。[JSVM_InitializedFlag](#ZH-CN_TOPIC_0000002497446184__jsvm_initializedflag)JSVM_InitializedFlag初始化方式的标志位。[JSVM_WasmOptLevel](#ZH-CN_TOPIC_0000002497446184__jsvm_wasmoptlevel)JSVM_WasmOptLevelWebAssembly 函数优化等级。[JSVM_CacheType](#ZH-CN_TOPIC_0000002497446184__jsvm_cachetype)JSVM_CacheType缓存类型。[JSVM_MicrotaskPolicy](#ZH-CN_TOPIC_0000002497446184__jsvm_microtaskpolicy)JSVM_MicrotaskPolicyJSVM 微任务执行策略。[JSVM_TraceCategory](#ZH-CN_TOPIC_0000002497446184__jsvm_tracecategory)JSVM_TraceCategoryJSVM 内部 Trace 事件的类别。[JSVM_CBTriggerTimeForGC](#ZH-CN_TOPIC_0000002497446184__jsvm_cbtriggertimeforgc)JSVM_CBTriggerTimeForGC触发回调函数的时机。[JSVM_GCType](#ZH-CN_TOPIC_0000002497446184__jsvm_gctype)JSVM_GCTypeGC类型。[JSVM_GCCallbackFlags](#ZH-CN_TOPIC_0000002497446184__jsvm_gccallbackflags)JSVM_GCCallbackFlagsGC回调函数标记。[JSVM_PromiseRejectEvent](#ZH-CN_TOPIC_0000002497446184__jsvm_promiserejectevent)JSVM_PromiseRejectEventpromise-reject事件。[JSVM_MessageErrorLevel](#ZH-CN_TOPIC_0000002497446184__jsvm_messageerrorlevel)JSVM_MessageErrorLevelmessage的报错级别。[JSVM_DefineClassOptionsId](#ZH-CN_TOPIC_0000002497446184__jsvm_defineclassoptionsid)JSVM_DefineClassOptionsId定义Class的选项ID。[JSVM_DebugOption](#ZH-CN_TOPIC_0000002497446184__jsvm_debugoption)JSVM_DebugOption调试选项。

#### 函数

名称typedef关键字描述[typedef void (JSVM_CDECL* JSVM_Finalize)(JSVM_Env env,void* finalizeData,void* finalizeHint)](#ZH-CN_TOPIC_0000002497446184__jsvm_finalize)JSVM_CDECL* JSVM_Finalize函数指针类型，当native类型对象或数据与JS对象被关联时，传入该指针。该函数将会在关联的JS对象被GC回收时被调用，用以执行native的清理动作。[typedef bool (JSVM_CDECL* JSVM_OutputStream)(const char* data,int size,void* streamData)](#ZH-CN_TOPIC_0000002497446184__jsvm_outputstream)JSVM_CDECL* JSVM_OutputStreamASCII输出流回调的函数指针类型。参数data是指输出的数据指针。参数size是指输出的数据大小。空数据指针指示流的结尾。参数streamData是指与回调一起传递给API函数的指针，该API函数向输出流生成数据。[typedef void (JSVM_CDECL* JSVM_HandlerForGC)(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void* data)](#ZH-CN_TOPIC_0000002497446184__jsvm_handlerforgc)JSVM_CDECL* JSVM_HandlerForGCGC回调的函数指针类型。[typedef void (JSVM_CDECL* JSVM_HandlerForOOMError)(const char* location,const char* detail,bool isHeapOOM)](#ZH-CN_TOPIC_0000002497446184__jsvm_handlerforoomerror)JSVM_CDECL* JSVM_HandlerForOOMErrorOOM-Error回调的函数指针类型。[typedef void (JSVM_CDECL* JSVM_HandlerForFatalError)(const char* location,const char* message)](#ZH-CN_TOPIC_0000002497446184__jsvm_handlerforfatalerror)JSVM_CDECL* JSVM_HandlerForFatalErrorFatal-Error回调的函数指针类型。[typedef void (JSVM_CDECL* JSVM_HandlerForPromiseReject)(JSVM_Env env, JSVM_PromiseRejectEvent rejectEvent, JSVM_Value rejectInfo)](#ZH-CN_TOPIC_0000002497446184__jsvm_handlerforpromisereject)JSVM_CDECL* JSVM_HandlerForPromiseRejectPromise-Reject回调的函数指针类型。

#### 变量

名称typedef关键字描述uint16_tchar16_t

为uint16_t创建一个别名——char16_t。

这段代码的核心目的是确保 char16_t 这个类型在所有目标编译环境中都可用，即使在一些不支持它的旧环境里。char16_t 是 C++11 标准中引入的一个新的基本数据类型，专门用于存储16位字符，通常用来表示UTF-16编码的字符。

如果编译器本身不认识char16_t，手动创建一个底层实现是16位无符号的整数类型。前置生效条件为：当前编译器——非C++编译器编译 || 是微软Visual C++编译器且版本早于Visual Studio 2015（不含）。

#### 枚举类型说明

#### JSVM_PropertyAttributes

```ets
enum JSVM_PropertyAttributes
```

**描述**

用于控制JavaScript对象属性的行为。

**起始版本：** 11

枚举项描述JSVM_DEFAULT = 0没有在属性上设置显式属性。JSVM_WRITABLE = 1 << 0该属性是可写的。JSVM_ENUMERABLE = 1 << 1该属性是可枚举的。JSVM_CONFIGURABLE = 1 << 2该属性是可配置的。JSVM_NO_RECEIVER_CHECK = 1 << 3用于标记本地方法的接收器无需进行检查。如果未设置 JSVM_NO_RECEIVER_CHECK，则该方法仅接受定义类的实例作为接收器，否则会向 JSVM 抛出异常“类型错误：非法调用”。JSVM_STATIC = 1 << 10该属性将被定义为类的静态属性，而不是默认的实例属性。这仅由OH_JSVM_DefineClass使用。JSVM_DEFAULT_METHOD = JSVM_WRITABLE | JSVM_CONFIGURABLE就像JS类中的方法一样，该属性是可配置和可写的，但不可枚举。JSVM_METHOD_NO_RECEIVER_CHECK = JSVM_DEFAULT_METHOD | JSVM_NO_RECEIVER_CHECK无需检查接收者的类方法。JSVM_DEFAULT_JSPROPERTY = JSVM_WRITABLE | JSVM_ENUMERABLE | JSVM_CONFIGURABLE就像JavaScript中通过赋值设置的属性一样，属性是可写、可枚举和可配置的。JSVM_JSPROPERTY_NO_RECEIVER_CHECK = JSVM_DEFAULT_JSPROPERTY | JSVM_NO_RECEIVER_CHECK无需检查接收者的对象属性。

#### JSVM_ValueType

```ets
enum JSVM_ValueType
```

**描述**

描述JSVM_Value的类型。

**起始版本：** 11

枚举项描述JSVM_UNDEFINED未定义类型。JSVM_NULLNull类型。JSVM_BOOLEAN布尔类型。JSVM_NUMBER数字类型。JSVM_STRING字符串类型。JSVM_SYMBOL符号类型。JSVM_OBJECT对象类型。JSVM_FUNCTION函数类型。JSVM_EXTERNAL外部类型。JSVM_BIGINTbigint类型。

#### JSVM_TypedarrayType

```ets
enum JSVM_TypedarrayType
```

**描述**

描述TypedArray的类型。

**起始版本：** 11

枚举项描述JSVM_INT8_ARRAYint8类型。JSVM_UINT8_ARRAYuint8类型。JSVM_UINT8_CLAMPED_ARRAYuint8固定类型。JSVM_INT16_ARRAYint16类型。JSVM_UINT16_ARRAYuint16类型。JSVM_INT32_ARRAYint32类型。JSVM_UINT32_ARRAYuint32类型。JSVM_FLOAT32_ARRAYfloat32类型。JSVM_FLOAT64_ARRAYfloat64类型。JSVM_BIGINT64_ARRAYbigint64类型。JSVM_BIGUINT64_ARRAYbiguint64类型。

#### JSVM_Status

```ets
enum JSVM_Status
```

**描述**

表示JSVM-API调用成功或失败的完整状态码。

**起始版本：** 11

枚举项描述JSVM_OK成功状态。JSVM_INVALID_ARG无效的状态。JSVM_OBJECT_EXPECTED期待传入对象类型。JSVM_STRING_EXPECTED期望传入字符串类型。JSVM_NAME_EXPECTED期望传入名字类型。JSVM_FUNCTION_EXPECTED期待传入函数类型。JSVM_NUMBER_EXPECTED期待传入数字类型。JSVM_BOOLEAN_EXPECTED期待传入布尔类型。JSVM_ARRAY_EXPECTED期待传入数组类型。JSVM_GENERIC_FAILURE泛型失败状态。JSVM_PENDING_EXCEPTION挂起异常状态。JSVM_CANCELLED取消状态。JSVM_ESCAPE_CALLED_TWICE转义调用了两次。JSVM_HANDLE_SCOPE_MISMATCH句柄作用域不匹配。JSVM_CALLBACK_SCOPE_MISMATCH回调作用域不匹配。JSVM_QUEUE_FULL队列满。JSVM_CLOSING关闭中。JSVM_BIGINT_EXPECTED期望传入Bigint类型。JSVM_DATE_EXPECTED期望传入日期类型。JSVM_ARRAYBUFFER_EXPECTED期望传入ArrayBuffer类型。JSVM_DETACHABLE_ARRAYBUFFER_EXPECTED可分离的数组缓冲区预期状态。JSVM_WOULD_DEADLOCK将死锁状态。JSVM_NO_EXTERNAL_BUFFERS_ALLOWED不允许外部缓冲区。JSVM_CANNOT_RUN_JS不能执行JS。JSVM_INVALID_TYPE

传入的参数为非法类型。

**起始版本：** 18

JSVM_JIT_MODE_EXPECTED

无 JIT 权限。

**起始版本：** 18

#### JSVM_KeyCollectionMode

```ets
enum JSVM_KeyCollectionMode
```

**描述**

限制查找属性的范围。

**起始版本：** 11

枚举项描述JSVM_KEY_INCLUDE_PROTOTYPES也包含对象原型链上的属性。JSVM_KEY_OWN_ONLY仅包含对象自身属性。

#### JSVM_KeyFilter

```ets
enum JSVM_KeyFilter
```

**描述**

属性过滤器，可以通过使用or来构造一个复合过滤器。

**起始版本：** 11

枚举项描述JSVM_KEY_ALL_PROPERTIES = 0所有属性的键。JSVM_KEY_WRITABLE = 1可写的键。JSVM_KEY_ENUMERABLE = 1 << 1可枚举的键。JSVM_KEY_CONFIGURABLE = 1 << 2可配置的键。JSVM_KEY_SKIP_STRINGS = 1 << 3排除字符串类型的键。JSVM_KEY_SKIP_SYMBOLS = 1 << 4排除符号类型的键。

#### JSVM_KeyConversion

```ets
enum JSVM_KeyConversion
```

**描述**

键转换选项。

**起始版本：** 11

枚举项描述JSVM_KEY_KEEP_NUMBERS将返回整数索引的数字。JSVM_KEY_NUMBERS_TO_STRINGS将整数索引转换为字符串。

#### JSVM_MemoryPressureLevel

```ets
enum JSVM_MemoryPressureLevel
```

**描述**

内存压力水平。

**起始版本：** 11

枚举项描述JSVM_MEMORY_PRESSURE_LEVEL_NONE无压力。JSVM_MEMORY_PRESSURE_LEVEL_MODERATE中等压力。JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL临界压力。

#### JSVM_RegExpFlags

```ets
enum JSVM_RegExpFlags
```

**描述**

正则表达式标志位。它们可以用来启用一组标志。

**起始版本：** 12

枚举项描述JSVM_REGEXP_NONE = 0None模式。JSVM_REGEXP_GLOBAL = 1 << 0Global模式。JSVM_REGEXP_IGNORE_CASE = 1 << 1Ignore Case模式。JSVM_REGEXP_MULTILINE = 1 << 2Multiline模式。JSVM_REGEXP_STICKY = 1 << 3Sticky模式。JSVM_REGEXP_UNICODE = 1 << 4Unicode模式。JSVM_REGEXP_DOT_ALL = 1 << 5dotAll模式。JSVM_REGEXP_LINEAR = 1 << 6Linear模式。JSVM_REGEXP_HAS_INDICES = 1 << 7Has Indices模式。JSVM_REGEXP_UNICODE_SETS = 1 << 8Unicode Sets模式。

#### JSVM_InitializedFlag

```ets
enum JSVM_InitializedFlag
```

**描述**

初始化方式的标志位。

**起始版本：** 12

枚举项描述JSVM_ZERO_INITIALIZED初始化为0。JSVM_UNINITIALIZED不做初始化。

#### JSVM_WasmOptLevel

```ets
enum JSVM_WasmOptLevel
```

**描述**

WebAssembly 函数优化等级。

**起始版本：** 12

枚举项描述JSVM_WASM_OPT_BASELINE = 10baseline 优化等级。JSVM_WASM_OPT_HIGH = 20高优化等级。

#### JSVM_CacheType

```ets
enum JSVM_CacheType
```

**描述**

缓存类型。

**起始版本：** 12

枚举项描述JSVM_CACHE_TYPE_JSJS 缓存, 由接口 OH_JSVM_CreateCodeCache 生成。JSVM_CACHE_TYPE_WASMWebAssembly 缓存, 由接口 OH_JSVM_CreateWasmCache 生成。

#### JSVM_MicrotaskPolicy

```ets
enum JSVM_MicrotaskPolicy
```

**描述**

JSVM 微任务执行策略。

**起始版本：** 18

枚举项描述JSVM_MICROTASK_EXPLICIT = 0调用 OH_JSVM_PerformMicrotaskCheckpoint 方法后微任务执行。JSVM_MICROTASK_AUTOJS 调用栈为 0 时自动执行微任务。默认模式。

#### JSVM_TraceCategory

```ets
enum JSVM_TraceCategory
```

**描述**

JSVM 内部 Trace 事件的类别。

**起始版本：** 18

枚举项描述JSVM_TRACE_VM采集 JSVM 主要接口调用, 例如执行 js 脚本。JSVM_TRACE_COMPILE采集编译相关的接口调用, 例如后台编译。JSVM_TRACE_EXECUTE采集与运行状态相关的接口调用, 例如中断与微任务。JSVM_TRACE_RUNTIME采集外部函数调用相关信息。JSVM_TRACE_STACK_TRACE采集 JSVM 中回栈相关信息。JSVM_TRACE_WASM采集主要的 WASM 相关接口调用, 例如编译与实例化 WASM 模块。JSVM_TRACE_WASM_DETAILED采集更多更细节的 WASM 相关接口调用，例如后台编译、跳板编译。

#### JSVM_CBTriggerTimeForGC

```ets
enum JSVM_CBTriggerTimeForGC
```

**描述**

触发回调函数的时机。

**起始版本：** 18

枚举项描述JSVM_CB_TRIGGER_BEFORE_GC在GC之前触发回调函数。JSVM_CB_TRIGGER_AFTER_GC在GC之后触发回调函数。

#### JSVM_GCType

```ets
enum JSVM_GCType
```

**描述**

GC类型。

**起始版本：** 18

枚举项描述JSVM_GC_TYPE_SCAVENGE = 1 << 0GC算法为Scavenge。JSVM_GC_TYPE_MINOR_MARK_COMPACT = 1 << 1GC算法为Minor-Mark-Compact。JSVM_GC_TYPE_MARK_SWEEP_COMPACT = 1 << 2GC算法为Mark-Sweep-Compact。JSVM_GC_TYPE_INCREMENTAL_MARKING = 1 << 3GC算法为Incremental-Marking。JSVM_GC_TYPE_PROCESS_WEAK_CALLBACKS = 1 << 4GC算法为Weak-Callbacks。JSVM_GC_TYPE_ALL = JSVM_GC_TYPE_SCAVENGE | JSVM_GC_TYPE_MINOR_MARK_COMPACT | JSVM_GC_TYPE_MARK_SWEEP_COMPACT | JSVM_GC_TYPE_INCREMENTAL_MARKING | JSVM_GC_TYPE_PROCESS_WEAK_CALLBACKS包含所有类型的GC算法。

#### JSVM_GCCallbackFlags

```ets
enum JSVM_GCCallbackFlags
```

**描述**

GC回调函数标记。

**起始版本：** 18

枚举项描述JSVM_NO_GC_CALLBACK_FLAGS无回调函数标记。JSVM_GC_CALLBACK_CONSTRUCT_RETAINED_OBJECT_INFOS垃圾回收回调中将构建保留对象信息。JSVM_GC_CALLBACK_FORCED强制执行垃圾回收回调。JSVM_GC_CALLBACK_SYNCHRONOUS_PHANTOM_CALLBACK_PROCESSING同步处理幽灵对象回调。JSVM_GC_CALLBACK_COLLECT_ALL_AVAILABLE_GARBAGE垃圾回收过程中会收集所有可用的垃圾对象。JSVM_GC_CALLBACK_COLLECT_ALL_EXTERNAL_MEMORY垃圾回收时会收集所有的外部内存。JSVM_GC_CALLBACK_SCHEDULE_IDLE_GARBAGE_COLLECTION在空闲时调度垃圾回收。

#### JSVM_PromiseRejectEvent

```ets
enum JSVM_PromiseRejectEvent
```

**描述**

promise-reject事件。

**起始版本：** 18

枚举项描述JSVM_PROMISE_REJECT_OTHER_REASONS = 0Promise被拒绝，但拒绝的原因未知或不明确。JSVM_PROMISE_REJECT_WITH_NO_HANDLER = 1Promise被拒绝但没有处理程序。JSVM_PROMISE_ADD_HANDLER_AFTER_REJECTED = 2Promise已被拒绝后，再添加处理程序。JSVM_PROMISE_REJECT_AFTER_RESOLVED = 3Promise已被解决后，再尝试拒绝该Promise。JSVM_PROMISE_RESOLVE_AFTER_RESOLVED = 4Promise已被解决后，再尝试解决该Promise。

#### JSVM_MessageErrorLevel

```ets
enum JSVM_MessageErrorLevel
```

**描述**

message的报错级别。

**起始版本：** 18

枚举项描述JSVM_MESSAGE_LOG = (1 << 0)Log级别的信息。JSVM_MESSAGE_DEBUG = (1 << 1)Debug级别的信息。JSVM_MESSAGE_INFO = (1 << 2)Info级别的信息。JSVM_MESSAGE_ERROR = (1 << 3)Error级别的信息。JSVM_MESSAGE_WARNING = (1 << 4)Warning级别的信息。JSVM_MESSAGE_ALL = JSVM_MESSAGE_LOG | JSVM_MESSAGE_DEBUG | JSVM_MESSAGE_INFO | JSVM_MESSAGE_ERROR | JSVM_MESSAGE_WARNING所有级别的信息。

#### JSVM_DefineClassOptionsId

```ets
enum JSVM_DefineClassOptionsId
```

**描述**

定义Class的选项ID。

**起始版本：** 18

枚举项描述JSVM_DEFINE_CLASS_NORMAL在常规模式下定义Class。JSVM_DEFINE_CLASS_WITH_COUNT为所创建的Class预留指定数量的interfield槽位，在这些槽位中可以存放native-data。JSVM_DEFINE_CLASS_WITH_PROPERTY_HANDLER为所创建的Class设置监听拦截属性以及设置作为函数调用时回调函数。

#### JSVM_DebugOption

```ets
enum JSVM_DebugOption
```

**描述**

调试选项。

**起始版本：** 20

枚举项描述JSVM_SCOPE_CHECKscope校验功能。

#### 函数说明

#### JSVM_Finalize()

```ets
typedef void (JSVM_CDECL* JSVM_Finalize)(JSVM_Env env,void* finalizeData,void* finalizeHint)
```

**描述**

函数指针类型，当native类型对象或数据与JS对象被关联时，传入该指针。该函数将会在关联的JS对象被GC回收时被调用，用以执行native的清理动作。

**起始版本：** 11

#### JSVM_OutputStream()

```ets
typedef bool (JSVM_CDECL* JSVM_OutputStream)(const char* data,int size,void* streamData)
```

**描述**

ASCII输出流回调的函数指针类型。参数data是指输出的数据指针。参数size是指输出的数据大小。空数据指针指示流的结尾。参数streamData是指与回调一起传递给API函数的指针，该API函数向输出流生成数据。

**起始版本：** 12

**返回：**

类型说明bool返回true表示流可以继续接受数据，返回false将中止流。

#### JSVM_HandlerForGC()

```ets
typedef void (JSVM_CDECL* JSVM_HandlerForGC)(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void* data)
```

**描述**

GC回调的函数指针类型。

**起始版本：** 18

#### JSVM_HandlerForOOMError()

```ets
typedef void (JSVM_CDECL* JSVM_HandlerForOOMError)(const char* location,const char* detail,bool isHeapOOM)
```

**描述**

OOM-Error回调的函数指针类型。

**起始版本：** 18

#### JSVM_HandlerForFatalError()

```ets
typedef void (JSVM_CDECL* JSVM_HandlerForFatalError)(const char* location,const char* message)
```

**描述**

Fatal-Error回调的函数指针类型。

**起始版本：** 18

#### JSVM_HandlerForPromiseReject()

```ets
typedef void (JSVM_CDECL* JSVM_HandlerForPromiseReject)(JSVM_Env env, JSVM_PromiseRejectEvent rejectEvent, JSVM_Value rejectInfo)
```

**描述**

Promise-Reject回调的函数指针类型。

**起始版本：** 18