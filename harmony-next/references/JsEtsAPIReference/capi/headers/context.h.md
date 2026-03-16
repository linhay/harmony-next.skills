# context.h

#### 概述

提供了Context相关的接口，可以配置运行时信息，该接口是非线程安全的。

**引用文件：** <mindspore/context.h>

**库：** libmindspore_lite_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：**[MindSpore](../../topics/misc/MindSpore.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)void*MindSpore Lite的上下文信息的指针，该指针会指向Context。[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)void*MindSpore Lite的运行设备信息的指针。

#### 函数

名称描述[OH_AI_API OH_AI_ContextHandle OH_AI_ContextCreate()](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextcreate)创建一个上下文的对象。注意：此接口需跟OH_AI_ContextDestroy配套使用。[OH_AI_API void OH_AI_ContextDestroy(OH_AI_ContextHandle *context)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextdestroy)释放上下文对象。[OH_AI_API void OH_AI_ContextSetThreadNum(OH_AI_ContextHandle context, int32_t thread_num)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadnum)设置运行时的线程数量。[OH_AI_API int32_t OH_AI_ContextGetThreadNum(const OH_AI_ContextHandle context)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextgetthreadnum)获取线程数量。[OH_AI_API void OH_AI_ContextSetThreadAffinityMode(OH_AI_ContextHandle context, int mode)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitymode)设置运行时线程绑定CPU核心的策略，按照CPU物理核频率分为大、中、小三种类型的核心，并且仅需绑大核或者绑中核，不需要绑小核。[OH_AI_API int OH_AI_ContextGetThreadAffinityMode(const OH_AI_ContextHandle context)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextgetthreadaffinitymode)获取运行时线程绑定CPU核心的策略。[OH_AI_API void OH_AI_ContextSetThreadAffinityCoreList(OH_AI_ContextHandle context, const int32_t *core_list,size_t core_num)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitycorelist)

设置运行时线程绑定CPU核心的列表。

 例如：当core_list=[2,6,8]时，则线程会在CPU的第2，6，8个核心上运行。

 如果对于同一个上下文对象，调用了[OH_AI_ContextSetThreadAffinityMode](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitymode)和[OH_AI_ContextSetThreadAffinityCoreList](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitycorelist)。

 这两个函数，则仅[OH_AI_ContextSetThreadAffinityCoreList](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitycorelist)的core_list参数生效，而[OH_AI_ContextSetThreadAffinityMode](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitymode)的mode参数不生效。

[OH_AI_API const int32_t *OH_AI_ContextGetThreadAffinityCoreList(const OH_AI_ContextHandle context, size_t *core_num)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextgetthreadaffinitycorelist)获取CPU绑核列表。[OH_AI_API void OH_AI_ContextSetEnableParallel(OH_AI_ContextHandle context, bool is_parallel)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetenableparallel)设置运行时是否支持并行。此接口特性当前未开启，设置无效。[OH_AI_API bool OH_AI_ContextGetEnableParallel(const OH_AI_ContextHandle context)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextgetenableparallel)获取是否支持算子间并行。[OH_AI_API void OH_AI_ContextAddDeviceInfo(OH_AI_ContextHandle context, OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_contextadddeviceinfo)将一个用户定义的运行设备信息附加到推理上下文中。[OH_AI_API OH_AI_DeviceInfoHandle OH_AI_DeviceInfoCreate(OH_AI_DeviceType device_type)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfocreate)创建一个设备信息对象。[OH_AI_API void OH_AI_DeviceInfoDestroy(OH_AI_DeviceInfoHandle *device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfodestroy)释放设备信息实例。注意：设备信息实例被添加到context后，无须调用者手动释放。[OH_AI_API void OH_AI_DeviceInfoSetProvider(OH_AI_DeviceInfoHandle device_info, const char *provider)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfosetprovider)设置生产商的名称。[OH_AI_API const char *OH_AI_DeviceInfoGetProvider(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetprovider)获取生产商的名称。[OH_AI_API void OH_AI_DeviceInfoSetProviderDevice(OH_AI_DeviceInfoHandle device_info, const char *device)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfosetproviderdevice)设置生产商设备的名称。[OH_AI_API const char *OH_AI_DeviceInfoGetProviderDevice(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetproviderdevice)获取生产商设备的名称。[OH_AI_API OH_AI_DeviceType OH_AI_DeviceInfoGetDeviceType(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetdevicetype)获取设备的类型。[OH_AI_API void OH_AI_DeviceInfoSetEnableFP16(OH_AI_DeviceInfoHandle device_info, bool is_fp16)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfosetenablefp16)设置是否开启float16推理模式，仅CPU/GPU设备可用。[OH_AI_API bool OH_AI_DeviceInfoGetEnableFP16(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetenablefp16)获取是否开启float16推理模式，仅CPU/GPU设备可用。[OH_AI_API void OH_AI_DeviceInfoSetFrequency(OH_AI_DeviceInfoHandle device_info, int frequency)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfosetfrequency)设置NPU的频率，仅NPU设备可用。[OH_AI_API int OH_AI_DeviceInfoGetFrequency(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetfrequency)获取NPU的频率类型，仅NPU设备可用。[OH_AI_API NNRTDeviceDesc *OH_AI_GetAllNNRTDeviceDescs(size_t *num)](#ZH-CN_TOPIC_0000002529446101__oh_ai_getallnnrtdevicedescs)获取系统中所有NNRt硬件设备的描述信息。[OH_AI_API NNRTDeviceDesc *OH_AI_GetElementOfNNRTDeviceDescs(NNRTDeviceDesc *descs, size_t index)](#ZH-CN_TOPIC_0000002529446101__oh_ai_getelementofnnrtdevicedescs)获取NNRt设备描述信息数组中的元素指针。[OH_AI_API void OH_AI_DestroyAllNNRTDeviceDescs(NNRTDeviceDesc **desc)](#ZH-CN_TOPIC_0000002529446101__oh_ai_destroyallnnrtdevicedescs)销毁从[OH_AI_GetAllNNRTDeviceDescs](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_getallnnrtdevicedescs)获取的NNRt描述信息实例数组。[OH_AI_API size_t OH_AI_GetDeviceIdFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)](#ZH-CN_TOPIC_0000002529446101__oh_ai_getdeviceidfromnnrtdevicedesc)从特定的NNRt设备描述信息实例获取NNRt设备ID。注意，此ID只对NNRt有效。[OH_AI_API const char *OH_AI_GetNameFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)](#ZH-CN_TOPIC_0000002529446101__oh_ai_getnamefromnnrtdevicedesc)从特定的NNRt设备描述信息实例获取NNRt设备名称。[OH_AI_API OH_AI_NNRTDeviceType OH_AI_GetTypeFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)](#ZH-CN_TOPIC_0000002529446101__oh_ai_gettypefromnnrtdevicedesc)从特定的NNRt设备描述信息实例获取NNRt设备类型。[OH_AI_API OH_AI_DeviceInfoHandle OH_AI_CreateNNRTDeviceInfoByName(const char *name)](#ZH-CN_TOPIC_0000002529446101__oh_ai_creatennrtdeviceinfobyname)查找指定名称的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。[OH_AI_API OH_AI_DeviceInfoHandle OH_AI_CreateNNRTDeviceInfoByType(OH_AI_NNRTDeviceType type)](#ZH-CN_TOPIC_0000002529446101__oh_ai_creatennrtdeviceinfobytype)查找指定类型的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。[OH_AI_API void OH_AI_DeviceInfoSetDeviceId(OH_AI_DeviceInfoHandle device_info, size_t device_id)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfosetdeviceid)设置NNRt设备ID，仅NNRt设备可用。[OH_AI_API size_t OH_AI_DeviceInfoGetDeviceId(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetdeviceid)获取NNRt设备ID，仅NNRt设备可用。[OH_AI_API void OH_AI_DeviceInfoSetPerformanceMode(OH_AI_DeviceInfoHandle device_info, OH_AI_PerformanceMode mode)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfosetperformancemode)设置NNRt性能模式，仅NNRt设备可用。[OH_AI_API OH_AI_PerformanceMode OH_AI_DeviceInfoGetPerformanceMode(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetperformancemode)获取NNRt性能模式，仅NNRt设备可用。[OH_AI_API void OH_AI_DeviceInfoSetPriority(OH_AI_DeviceInfoHandle device_info, OH_AI_Priority priority)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfosetpriority)设置NNRt任务优先级，仅NNRt设备可用。[OH_AI_API OH_AI_Priority OH_AI_DeviceInfoGetPriority(const OH_AI_DeviceInfoHandle device_info)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfogetpriority)获取NNRt任务优先级，仅NNRt设备可用。[OH_AI_API OH_AI_Status OH_AI_DeviceInfoAddExtension(OH_AI_DeviceInfoHandle device_info, const char *name,const char *value, size_t value_size)](#ZH-CN_TOPIC_0000002529446101__oh_ai_deviceinfoaddextension)

向设备信息中添加键/值对形式的扩展配置。只对NNRt设备信息有效。

当前仅支持配置以下11种键：{"CachePath": "YourCachePath"}，{"CacheVersion": "YourCacheVersion"}，

 {"QuantBuffer": "YourQuantBuffer"}，{"ModelName": "YourModelName"}，

 {"isProfiling": "YourProfilingSwitch"}，{"opLayout": "YourOpLayout"}，

 {"InputDims": "YourInputDims"}，{"DynamicDims": "YourDynamicDims"}，

 {"QuantConfigData": "YourQuantConfigData"}，{"BandMode": "YourBandMode"}，

 {"NPU_FM_SHARED": "YourNPU_FM_SHARED"}，用户可根据使用情况配置各个键对应的值。

#### 函数说明

#### OH_AI_ContextCreate()

```ets
OH_AI_API OH_AI_ContextHandle OH_AI_ContextCreate()
```

**描述**

创建一个上下文的对象。注意：此接口需跟OH_AI_ContextDestroy配套使用。

**起始版本：** 9

**返回：**

类型说明OH_AI_API [OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)指向上下文信息的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。

#### OH_AI_ContextDestroy()

```ets
OH_AI_API void OH_AI_ContextDestroy(OH_AI_ContextHandle *context)
```

**描述**

释放上下文对象。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) *context指向[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)的二级指针，上下文销毁后会对context置为空指针。

#### OH_AI_ContextSetThreadNum()

```ets
OH_AI_API void OH_AI_ContextSetThreadNum(OH_AI_ContextHandle context, int32_t thread_num)
```

**描述**

设置运行时的线程数量。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。int32_t thread_num运行时的线程数量。长度跟随系统限制。

#### OH_AI_ContextGetThreadNum()

```ets
OH_AI_API int32_t OH_AI_ContextGetThreadNum(const OH_AI_ContextHandle context)
```

**描述**

获取线程数量。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。

**返回：**

类型说明OH_AI_API int32_t当前的线程数量。

#### OH_AI_ContextSetThreadAffinityMode()

```ets
OH_AI_API void OH_AI_ContextSetThreadAffinityMode(OH_AI_ContextHandle context, int mode)
```

**描述**

设置运行时线程绑定CPU核心的策略，按照CPU物理核频率分为大、中、小三种类型的核心，并且仅需绑大核或者绑中核，不需要绑小核。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。int mode绑核策略。一共有三种策略，0为不绑核，1为大核优先，2为中核优先。

#### OH_AI_ContextGetThreadAffinityMode()

```ets
OH_AI_API int OH_AI_ContextGetThreadAffinityMode(const OH_AI_ContextHandle context)
```

**描述**

获取运行时线程绑定CPU核心的策略。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。

**返回：**

类型说明OH_AI_API int绑核策略。一共有三种策略，0为不绑核，1为大核优先，2为中核优先。

#### OH_AI_ContextSetThreadAffinityCoreList()

```ets
OH_AI_API void OH_AI_ContextSetThreadAffinityCoreList(OH_AI_ContextHandle context, const int32_t *core_list,size_t core_num)
```

**描述**

设置运行时线程绑定CPU核心的列表。

 例如：当core_list=[2,6,8]时，则线程会在CPU的第2，6，8个核心上运行。

 如果对于同一个上下文对象，调用了[OH_AI_ContextSetThreadAffinityMode](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitymode)和[OH_AI_ContextSetThreadAffinityCoreList](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitycorelist)。

 这两个函数，则仅[OH_AI_ContextSetThreadAffinityCoreList](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitycorelist)的core_list参数生效，而[OH_AI_ContextSetThreadAffinityMode](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_contextsetthreadaffinitymode)的mode参数不生效。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。const int32_t *core_listCPU绑核的列表。size_t core_num核的数量，它就代表core_list的长度。

#### OH_AI_ContextGetThreadAffinityCoreList()

```ets
OH_AI_API const int32_t *OH_AI_ContextGetThreadAffinityCoreList(const OH_AI_ContextHandle context, size_t *core_num)
```

**描述**

获取CPU绑核列表。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。size_t *core_num该参数是输出参数，表示核的数量。

**返回：**

类型说明OH_AI_API const int32_t *CPU绑核列表。此列表对象由[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)管理，调用者无须手动释放。

#### OH_AI_ContextSetEnableParallel()

```ets
OH_AI_API void OH_AI_ContextSetEnableParallel(OH_AI_ContextHandle context, bool is_parallel)
```

**描述**

设置运行时是否支持并行。此接口特性当前未开启，设置无效。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。bool is_parallel是否支持并行。true为支持并行，false为不支持并行。

#### OH_AI_ContextGetEnableParallel()

```ets
OH_AI_API bool OH_AI_ContextGetEnableParallel(const OH_AI_ContextHandle context)
```

**描述**

获取是否支持算子间并行。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。

**返回：**

类型说明OH_AI_API bool是否支持并行。true为支持并行，false为不支持并行。

#### OH_AI_ContextAddDeviceInfo()

```ets
OH_AI_API void OH_AI_ContextAddDeviceInfo(OH_AI_ContextHandle context, OH_AI_DeviceInfoHandle device_info)
```

**描述**

将一个用户定义的运行设备信息附加到推理上下文中。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md) context指向上下文信息实例的[OH_AI_ContextHandle](../../topics/graphics/OH_AI_ContextHandle.md)。[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

#### OH_AI_DeviceInfoCreate()

```ets
OH_AI_API OH_AI_DeviceInfoHandle OH_AI_DeviceInfoCreate(OH_AI_DeviceType device_type)
```

**描述**

创建一个设备信息对象。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_DeviceType](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_devicetype) device_type设备类型，具体见[OH_AI_DeviceType](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_devicetype)。

**返回：**

类型说明OH_AI_API [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

#### OH_AI_DeviceInfoDestroy()

```ets
OH_AI_API void OH_AI_DeviceInfoDestroy(OH_AI_DeviceInfoHandle *device_info)
```

**描述**

释放设备信息实例。注意：设备信息实例被添加到context后，无须调用者手动释放。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) *device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

#### OH_AI_DeviceInfoSetProvider()

```ets
OH_AI_API void OH_AI_DeviceInfoSetProvider(OH_AI_DeviceInfoHandle device_info, const char *provider)
```

**描述**

设置生产商的名称。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。const char *provider生产商的名称。字符串长度跟随系统限制。

#### OH_AI_DeviceInfoGetProvider()

```ets
OH_AI_API const char *OH_AI_DeviceInfoGetProvider(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取生产商的名称。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API const char *生产商的名称。

#### OH_AI_DeviceInfoSetProviderDevice()

```ets
OH_AI_API void OH_AI_DeviceInfoSetProviderDevice(OH_AI_DeviceInfoHandle device_info, const char *device)
```

**描述**

设置生产商设备的名称。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。const char *device生产商设备名称。例如: CPU。字符串长度跟随系统限制。

#### OH_AI_DeviceInfoGetProviderDevice()

```ets
OH_AI_API const char *OH_AI_DeviceInfoGetProviderDevice(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取生产商设备的名称。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API const char *生产商设备的名称。

#### OH_AI_DeviceInfoGetDeviceType()

```ets
OH_AI_API OH_AI_DeviceType OH_AI_DeviceInfoGetDeviceType(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取设备的类型。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API [OH_AI_DeviceType](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_devicetype)生产商设备类型。

#### OH_AI_DeviceInfoSetEnableFP16()

```ets
OH_AI_API void OH_AI_DeviceInfoSetEnableFP16(OH_AI_DeviceInfoHandle device_info, bool is_fp16)
```

**描述**

设置是否开启float16推理模式，仅CPU/GPU设备可用。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。bool is_fp16是否开启float16推理模式。true为开启float16推理模式，false为不开启float16推理模式。

#### OH_AI_DeviceInfoGetEnableFP16()

```ets
OH_AI_API bool OH_AI_DeviceInfoGetEnableFP16(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取是否开启float16推理模式，仅CPU/GPU设备可用。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API bool是否开启float16推理模式。true为开启float16推理模式，false为不开启float16推理模式。

#### OH_AI_DeviceInfoSetFrequency()

```ets
OH_AI_API void OH_AI_DeviceInfoSetFrequency(OH_AI_DeviceInfoHandle device_info, int frequency)
```

**描述**

设置NPU的频率，仅NPU设备可用。

**起始版本：** 9

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。int frequency频率类型，取值范围为0-4，默认是3。0表示不设置，由系统调节；1表示低功耗；2表示平衡；3表示高性能；4表示超高性能。

#### OH_AI_DeviceInfoGetFrequency()

```ets
OH_AI_API int OH_AI_DeviceInfoGetFrequency(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NPU的频率类型，仅NPU设备可用。

**起始版本：** 9

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API intNPU的频率类型。取值范围为0-4，0表示不设置，由系统调节；1表示低功耗；2表示平衡；3表示高性能；4表示超高性能。

#### OH_AI_GetAllNNRTDeviceDescs()

```ets
OH_AI_API NNRTDeviceDesc *OH_AI_GetAllNNRTDeviceDescs(size_t *num)
```

**描述**

获取系统中所有NNRt硬件设备的描述信息。

**起始版本：** 10

**参数：**

参数项描述size_t *num输出参数，返回设备数量。

**返回：**

类型说明OH_AI_API [NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md) *指向NNRt设备描述信息实例数组的指针。当获取失败时，返回NULL。

#### OH_AI_GetElementOfNNRTDeviceDescs()

```ets
OH_AI_API NNRTDeviceDesc *OH_AI_GetElementOfNNRTDeviceDescs(NNRTDeviceDesc *descs, size_t index)
```

**描述**

获取NNRt设备描述信息数组中的元素指针。

**起始版本：** 10

**参数：**

参数项描述[NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md) *descsNNRt设备描述信息数组。size_t index数组元素索引。

**返回：**

类型说明OH_AI_API [NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md) *NNRt设备描述信息类型指针。

#### OH_AI_DestroyAllNNRTDeviceDescs()

```ets
OH_AI_API void OH_AI_DestroyAllNNRTDeviceDescs(NNRTDeviceDesc **desc)
```

**描述**

销毁从[OH_AI_GetAllNNRTDeviceDescs](context.h.md#ZH-CN_TOPIC_0000002529446101__oh_ai_getallnnrtdevicedescs)获取的NNRt描述信息实例数组。

**起始版本：** 10

**参数：**

参数项描述[NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md) **desc指向NNRt设备描述信息实例数组的二重指针。销毁结束，desc指向内容会被置为NULL。

#### OH_AI_GetDeviceIdFromNNRTDeviceDesc()

```ets
OH_AI_API size_t OH_AI_GetDeviceIdFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)
```

**描述**

从特定的NNRt设备描述信息实例获取NNRt设备ID。注意，此ID只对NNRt有效。

**起始版本：** 10

**参数：**

参数项描述const [NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md) *desc指向NNRt设备描述信息实例的指针。

**返回：**

类型说明OH_AI_API size_tNNRt设备ID。

#### OH_AI_GetNameFromNNRTDeviceDesc()

```ets
OH_AI_API const char *OH_AI_GetNameFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)
```

**描述**

从特定的NNRt设备描述信息实例获取NNRt设备名称。

**起始版本：** 10

**参数：**

参数项描述const [NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md) *desc指向NNRt设备描述信息实例的指针。

**返回：**

类型说明OH_AI_API const char *NNRt设备名称，指向一个常量字符串的指针，该常量字符串由desc持有，调用者无需单独释放此指针。

#### OH_AI_GetTypeFromNNRTDeviceDesc()

```ets
OH_AI_API OH_AI_NNRTDeviceType OH_AI_GetTypeFromNNRTDeviceDesc(const NNRTDeviceDesc *desc)
```

**描述**

从特定的NNRt设备描述信息实例获取NNRt设备类型。

**起始版本：** 10

**参数：**

参数项描述const [NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md) *desc指向NNRt设备描述信息实例的指针。

**返回：**

类型说明OH_AI_API [OH_AI_NNRTDeviceType](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_nnrtdevicetype)[OH_AI_NNRTDeviceType](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_nnrtdevicetype) NNRt设备类型。

#### OH_AI_CreateNNRTDeviceInfoByName()

```ets
OH_AI_API OH_AI_DeviceInfoHandle OH_AI_CreateNNRTDeviceInfoByName(const char *name)
```

**描述**

查找指定名称的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。

**起始版本：** 10

**参数：**

参数项描述const char *name目标NNRt设备名。字符串长度跟随系统限制。

**返回：**

类型说明OH_AI_API [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

#### OH_AI_CreateNNRTDeviceInfoByType()

```ets
OH_AI_API OH_AI_DeviceInfoHandle OH_AI_CreateNNRTDeviceInfoByType(OH_AI_NNRTDeviceType type)
```

**描述**

查找指定类型的NNRt设备，根据找到的第一个设备信息，创建NNRt设备信息。

**起始版本：** 10

**参数：**

参数项描述[OH_AI_NNRTDeviceType](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_nnrtdevicetype) type[OH_AI_NNRTDeviceType](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_nnrtdevicetype) 目标NNRt设备类型。

**返回：**

类型说明OH_AI_API [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

#### OH_AI_DeviceInfoSetDeviceId()

```ets
OH_AI_API void OH_AI_DeviceInfoSetDeviceId(OH_AI_DeviceInfoHandle device_info, size_t device_id)
```

**描述**

设置NNRt设备ID，仅NNRt设备可用。

**起始版本：** 10

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。size_t device_idNNRt设备ID。

#### OH_AI_DeviceInfoGetDeviceId()

```ets
OH_AI_API size_t OH_AI_DeviceInfoGetDeviceId(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NNRt设备ID，仅NNRt设备可用。

**起始版本：** 10

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API size_tNNRt设备ID。

#### OH_AI_DeviceInfoSetPerformanceMode()

```ets
OH_AI_API void OH_AI_DeviceInfoSetPerformanceMode(OH_AI_DeviceInfoHandle device_info, OH_AI_PerformanceMode mode)
```

**描述**

设置NNRt性能模式，仅NNRt设备可用。

**起始版本：** 10

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。[OH_AI_PerformanceMode](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_performancemode) mode[OH_AI_PerformanceMode](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_performancemode) NNRt性能模式。

#### OH_AI_DeviceInfoGetPerformanceMode()

```ets
OH_AI_API OH_AI_PerformanceMode OH_AI_DeviceInfoGetPerformanceMode(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NNRt性能模式，仅NNRt设备可用。

**起始版本：** 10

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API [OH_AI_PerformanceMode](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_performancemode)[OH_AI_PerformanceMode](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_performancemode) NNRt性能模式。

#### OH_AI_DeviceInfoSetPriority()

```ets
OH_AI_API void OH_AI_DeviceInfoSetPriority(OH_AI_DeviceInfoHandle device_info, OH_AI_Priority priority)
```

**描述**

设置NNRt任务优先级，仅NNRt设备可用。

**起始版本：** 10

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。[OH_AI_Priority](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_priority) priority[OH_AI_Priority](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_priority) NNRt任务优先级。

#### OH_AI_DeviceInfoGetPriority()

```ets
OH_AI_API OH_AI_Priority OH_AI_DeviceInfoGetPriority(const OH_AI_DeviceInfoHandle device_info)
```

**描述**

获取NNRt任务优先级，仅NNRt设备可用。

**起始版本：** 22

**参数：**

参数项描述const [OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。

**返回：**

类型说明OH_AI_API [OH_AI_Priority](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_priority)[OH_AI_Priority](types.h.md#ZH-CN_TOPIC_0000002497446160__oh_ai_priority) NNRt任务优先级。

#### OH_AI_DeviceInfoAddExtension()

```ets
OH_AI_API OH_AI_Status OH_AI_DeviceInfoAddExtension(OH_AI_DeviceInfoHandle device_info, const char *name,const char *value, size_t value_size)
```

**描述**

向设备信息中添加键/值对形式的扩展配置。只对NNRt设备信息有效。

当前仅支持配置以下11种键：{"CachePath": "YourCachePath"}，{"CacheVersion": "YourCacheVersion"}，

 {"QuantBuffer": "YourQuantBuffer"}，{"ModelName": "YourModelName"}，

 {"isProfiling": "YourProfilingSwitch"}，{"opLayout": "YourOpLayout"}，

 {"InputDims": "YourInputDims"}，{"DynamicDims": "YourDynamicDims"}，

 {"QuantConfigData": "YourQuantConfigData"}，{"BandMode": "YourBandMode"}，

 {"NPU_FM_SHARED": "YourNPU_FM_SHARED"}，用户可根据使用情况配置各个键对应的值。

**起始版本：** 10

**参数：**

参数项描述[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md) device_info指向设备信息实例的[OH_AI_DeviceInfoHandle](../../topics/system-services/OH_AI_DeviceInfoHandle.md)。const char *name单个扩展项的键，格式为C字符串。字符串长度限制为128。const char *value单个扩展项的值内容首地址。字符串长度跟随系统限制。size_t value_size单个扩展项的值内容长度。

**返回：**

类型说明OH_AI_API [OH_AI_Status](status.h.md#ZH-CN_TOPIC_0000002529446103__oh_ai_status)[OH_AI_Status](status.h.md#ZH-CN_TOPIC_0000002529446103__oh_ai_status) 执行状态码，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。