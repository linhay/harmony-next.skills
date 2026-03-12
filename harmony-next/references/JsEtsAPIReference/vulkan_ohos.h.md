# vulkan_ohos.h

#### 概述

定义了HarmonyOS平台扩展的Vulkan接口。

**引用文件：** <vulkan/vulkan_ohos.h>

**库：** libvulkan.so

**起始版本：** 10

**相关模块：**[Vulkan](Vulkan.md)

#### 汇总

#### 结构体

名称typedef关键字描述[VkSurfaceCreateInfoOHOS](VkSurfaceCreateInfoOHOS.md)VkSurfaceCreateInfoOHOS包含创建Vulkan Surface时必要的参数。[VkNativeBufferUsageOHOS](VkNativeBufferUsageOHOS.md)VkNativeBufferUsageOHOS提供HarmonyOS NativeBuffer用途的说明。[VkNativeBufferPropertiesOHOS](VkNativeBufferPropertiesOHOS.md)VkNativeBufferPropertiesOHOS包含了NativeBuffer的属性。[VkNativeBufferFormatPropertiesOHOS](VkNativeBufferFormatPropertiesOHOS.md)VkNativeBufferFormatPropertiesOHOS包含了NativeBuffer的一些格式属性。[VkImportNativeBufferInfoOHOS](VkImportNativeBufferInfoOHOS.md)VkImportNativeBufferInfoOHOS包含了OH_NativeBuffer结构体的指针。[VkMemoryGetNativeBufferInfoOHOS](VkMemoryGetNativeBufferInfoOHOS.md)VkMemoryGetNativeBufferInfoOHOS用于从Vulkan内存中获取OH_NativeBuffer。[VkExternalFormatOHOS](VkExternalFormatOHOS.md)VkExternalFormatOHOS表示外部定义的格式标识符。[NativeWindow](NativeWindow.md)OHNativeWindow本地窗口。[OH_NativeBuffer](OH_NativeBuffer.md)-OH_NativeBuffer结构体声明。

#### 宏定义

名称描述VK_OHOS_surface 1

HarmonyOS平台Surface扩展宏定义。

**起始版本：** 10

VK_OHOS_SURFACE_SPEC_VERSION 1

HarmonyOS平台Surface扩展版本号。

**起始版本：** 10

VK_OHOS_SURFACE_EXTENSION_NAME "VK_OHOS_surface"

HarmonyOS平台Surface扩展名。

**起始版本：** 10

VK_OHOS_external_memory 1

HarmonyOS平台external_memory扩展宏定义。

**起始版本：** 10

VK_OHOS_EXTERNAL_MEMORY_SPEC_VERSION 1

HarmonyOS平台external_memory扩展版本号。

**起始版本：** 10

VK_OHOS_EXTERNAL_MEMORY_EXTENSION_NAME "VK_OHOS_external_memory"

HarmonyOS平台external_memory扩展名。

**起始版本：** 10

#### 函数

名称typedef关键字描述[VkResult (VKAPI_PTR PFN_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)](#ZH-CN_TOPIC_0000002529446153__pfn_vkcreatesurfaceohos)PFN_vkCreateSurfaceOHOS创建Vulkan Surface的函数指针定义。[VKAPI_ATTR VkResult VKAPI_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)](#ZH-CN_TOPIC_0000002529446153__vkcreatesurfaceohos)-创建Vulkan Surface。[VkResult (VKAPI_PTR PFN_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH_NativeBuffer buffer, VkNativeBufferPropertiesOHOS* pProperties)](#ZH-CN_TOPIC_0000002529446153__pfn_vkgetnativebufferpropertiesohos)PFN_vkGetNativeBufferPropertiesOHOS获取OH_NativeBuffer属性的函数指针定义。[VkResult (VKAPI_PTR PFN_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS pInfo, struct OH_NativeBuffer** pBuffer)](#ZH-CN_TOPIC_0000002529446153__pfn_vkgetmemorynativebufferohos)PFN_vkGetMemoryNativeBufferOHOS获取OH_NativeBuffer的函数指针定义。[VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties)](#ZH-CN_TOPIC_0000002529446153__vkgetnativebufferpropertiesohos)-获取OH_NativeBuffer属性。[VKAPI_ATTR VkResult VKAPI_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer)](#ZH-CN_TOPIC_0000002529446153__vkgetmemorynativebufferohos)-获取OH_NativeBuffer。[VKAPI_ATTR VkResult VKAPI_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t* grallocUsage)](#ZH-CN_TOPIC_0000002529446153__vkgetswapchaingrallocusageohos)-根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。[VKAPI_ATTR VkResult VKAPI_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](#ZH-CN_TOPIC_0000002529446153__vkacquireimageohos)-用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。[VKAPI_ATTR VkResult VKAPI_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)](#ZH-CN_TOPIC_0000002529446153__vkqueuesignalreleaseimageohos)-当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。

#### 函数说明

#### PFN_vkCreateSurfaceOHOS()

```ets
typedef VkResult (VKAPI_PTR *PFN_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)
```

**描述**

创建Vulkan Surface的函数指针定义。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkInstance instanceVulkan实例。[const VkSurfaceCreateInfoOHOS](VkSurfaceCreateInfoOHOS.md)* pCreateInfo一个VkSurfaceCreateInfoOHOS结构体的指针，包含创建Vulkan Surface时必要的参数。const VkAllocationCallbacks* pAllocator用户自定义内存分配的回调函数，如果不需要可以传入NULL，接口会使用默认的内存分配函数。VkSurfaceKHR* pSurface出参，用于接收创建的Vulkan Surface，类型为VkSurfaceKHR。

**返回：**

类型说明VkResult返回一个VkResult类型的错误码，返回值为VK_SUCCESS表示执行成功。

#### vkCreateSurfaceOHOS()

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)
```

**描述**

创建Vulkan Surface。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkInstance instanceVulkan实例。[const VkSurfaceCreateInfoOHOS](VkSurfaceCreateInfoOHOS.md)* pCreateInfo一个VkSurfaceCreateInfoOHOS结构体的指针，包含创建Vulkan Surface时必要的参数。const VkAllocationCallbacks* pAllocator用户自定义内存分配的回调函数，如果不需要可以传入NULL，接口会使用默认的内存分配函数。VkSurfaceKHR* pSurface出参，用于接收创建的Vulkan Surface，类型为VkSurfaceKHR。

**返回：**

类型说明VkResult

返回一个VkResult类型的错误码，具体返回类型如下：

 返回VK_SUCCESS，表示执行成功。

 返回VK_ERROR_OUT_OF_HOST_MEMORY，表示分配VkSurfaceKHR内存失败。

 返回VK_ERROR_SURFACE_LOST_KHR，表示操作NativeWindow失败。

#### PFN_vkGetNativeBufferPropertiesOHOS()

```ets
typedef VkResult (VKAPI_PTR *PFN_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties)
```

**描述**

获取OH_NativeBuffer属性的函数指针定义。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkDevice deviceVkDevice对象。const [struct OH_NativeBuffer](OH_NativeBuffer.md)* bufferOH_NativeBuffer结构体指针。[VkNativeBufferPropertiesOHOS](VkNativeBufferPropertiesOHOS.md)* pProperties用于接收OH_NativeBuffer属性的结构体。

**返回：**

类型说明VkResult返回一个VkResult类型的错误码，返回值为VK_SUCCESS表示执行成功。

#### PFN_vkGetMemoryNativeBufferOHOS()

```ets
typedef VkResult (VKAPI_PTR *PFN_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer)
```

**描述**

获取OH_NativeBuffer的函数指针定义。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkDevice deviceVkDevice对象。[const VkMemoryGetNativeBufferInfoOHOS](VkMemoryGetNativeBufferInfoOHOS.md)* pInfoVkMemoryGetNativeBufferInfoOHOS结构体对象。[struct OH_NativeBuffer](OH_NativeBuffer.md)** pBuffer用于接收获取到的OH_NativeBuffer。

**返回：**

类型说明VkResult返回一个VkResult类型的错误码，返回值为VK_SUCCESS表示执行成功。

#### vkGetNativeBufferPropertiesOHOS()

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties)
```

**描述**

获取OH_NativeBuffer属性。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkDevice deviceVkDevice对象。const [struct OH_NativeBuffer](OH_NativeBuffer.md)* bufferOH_NativeBuffer结构体指针。[VkNativeBufferPropertiesOHOS](VkNativeBufferPropertiesOHOS.md)* pProperties用于接收OH_NativeBuffer属性的结构体。

**返回：**

类型说明VkResult

返回一个VkResult类型的错误码，具体返回类型如下：

 返回VK_SUCCESS，表示执行成功。

 返回VK_ERROR_INVALID_EXTERNAL_HANDLE_KHR，表示入参存在异常。

 返回VK_ERROR_OUT_OF_DEVICE_MEMORY，表示设备内存不足。

#### vkGetMemoryNativeBufferOHOS()

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer)
```

**描述**

获取OH_NativeBuffer。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkDevice deviceVkDevice对象。[const VkMemoryGetNativeBufferInfoOHOS](VkMemoryGetNativeBufferInfoOHOS.md)* pInfoVkMemoryGetNativeBufferInfoOHOS结构体对象。[struct OH_NativeBuffer](OH_NativeBuffer.md)** pBuffer用于接收获取到的OH_NativeBuffer。

**返回：**

类型说明VkResult

返回一个VkResult类型的错误码，具体返回类型如下：

 返回VK_SUCCESS，表示执行成功。

 返回VK_ERROR_OUT_OF_HOST_MEMORY，表示pInfo入参异常，或获取的pBuffer异常。

#### vkGetSwapchainGrallocUsageOHOS()

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t* grallocUsage)
```

**描述**

根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkDevice deviceVkDevice对象。VkFormat format图像格式。VkImageUsageFlags imageUsage图像使用标志。uint64_t* grallocUsage出参, 返回Gralloc(内存分配器)使用标志。

**返回：**

类型说明VkResult

返回一个VkResult类型的错误码，具体返回类型如下：

 返回VK_SUCCESS，表示执行成功。

 返回VK_ERROR_INITIALIZATION_FAILED，表示入参异常。

#### vkAcquireImageOHOS()

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

**描述**

用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkDevice deviceVkDevice对象。VkImage image要获取的Vulkan图像。int32_t nativeFenceFd原生Fence的文件描述符。VkSemaphore semaphore表示图像可用状态的Vulkan Semaphore(信号量)。VkFence fence用于在图像获取完成时进行同步的Vulkan Fence。

**返回：**

类型说明VkResult

返回一个VkResult类型的错误码，具体返回类型如下：

 返回VK_SUCCESS，表示执行成功。

 返回VK_ERROR_OUT_OF_HOST_MEMORY，表示主机内存不足。

#### vkQueueSignalReleaseImageOHOS()

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

**描述**

当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

参数项描述VkQueue queueVulkan队列的句柄。uint32_t waitSemaphoreCount等待Semaphore(信号量)的数量。const VkSemaphore* pWaitSemaphores指向等待Semaphore(信号量)数组的指针。VkImage image要释放的Vulkan图像句柄。int32_t* pNativeFenceFd指向Fence的文件描述符的指针。

**返回：**

类型说明VkResult

返回一个VkResult类型的错误码，具体返回类型如下：

 返回VK_SUCCESS，表示执行成功。

 返回VK_ERROR_DEVICE_LOST，表示Vulkan设备链接丢失。

 返回VK_ERROR_OUT_OF_HOST_MEMORY，表示主机内存不足。