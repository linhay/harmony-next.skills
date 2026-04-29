# vulkan_ohos.h

**概述**

定义了HarmonyOS平台扩展的Vulkan接口。

引用文件： <vulkan/vulkan_ohos.h>

库： libvulkan.so

起始版本： 10

相关模块： [Vulkan](Vulkan.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| VkSurfaceCreateInfoOHOS | VkSurfaceCreateInfoOHOS | 包含创建Vulkan Surface时必要的参数。 |
| VkNativeBufferOHOS | VkNativeBufferOHOS | 包含本地显存的参数。 |
| VkSwapchainImageCreateInfoOHOS | VkSwapchainImageCreateInfoOHOS | 包含创建Image时必要的参数。 |
| VkPhysicalDevicePresentationPropertiesOHOS | VkPhysicalDevicePresentationPropertiesOHOS | 包含设备的显示属性的参数。 |
| VkNativeBufferUsageOHOS | VkNativeBufferUsageOHOS | 提供HarmonyOS NativeBuffer用途的说明。 |
| VkNativeBufferPropertiesOHOS | VkNativeBufferPropertiesOHOS | 包含了NativeBuffer的属性。 |
| VkNativeBufferFormatPropertiesOHOS | VkNativeBufferFormatPropertiesOHOS | 包含了NativeBuffer的一些格式属性。 |
| VkImportNativeBufferInfoOHOS | VkImportNativeBufferInfoOHOS | 包含了OH_NativeBuffer结构体的指针。 |
| VkMemoryGetNativeBufferInfoOHOS | VkMemoryGetNativeBufferInfoOHOS | 用于从Vulkan内存中获取OH_NativeBuffer。 |
| VkExternalFormatOHOS | VkExternalFormatOHOS | 表示外部定义的格式标识符。 |
| NativeWindow | OHNativeWindow | 本地窗口。 |
| OHBufferHandle | - | 缓冲区句柄，用于对缓冲区的信息传递和获取。 |
| OH_NativeBuffer | - | OH_NativeBuffer结构体声明。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| VkSwapchainImageUsageFlagBitsOHOS | VkSwapchainImageUsageFlagBitsOHOS | 图像使用标志位。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| VK_OHOS_surface 1 | HarmonyOS平台Surface扩展宏定义。 起始版本： 10 |
| VK_OHOS_SURFACE_SPEC_VERSION 1 | HarmonyOS平台Surface扩展版本号。 起始版本： 10 |
| VK_OHOS_SURFACE_EXTENSION_NAME "VK_OHOS_surface" | HarmonyOS平台Surface扩展名。 起始版本： 10 |
| VK_OHOS_native_buffer 1 | native_buffer扩展宏定义。 起始版本： 10 |
| VK_OHOS_NATIVE_BUFFER_SPEC_VERSION 1 | native_buffer扩展版本号。 起始版本： 10 |
| VK_OHOS_NATIVE_BUFFER_EXTENSION_NAME "VK_OHOS_native_buffer" | native_buffer扩展名。 起始版本： 10 |
| VK_OHOS_external_memory 1 | HarmonyOS平台external_memory扩展宏定义。 起始版本： 10 |
| VK_OHOS_EXTERNAL_MEMORY_SPEC_VERSION 1 | HarmonyOS平台external_memory扩展版本号。 起始版本： 10 |
| VK_OHOS_EXTERNAL_MEMORY_EXTENSION_NAME "VK_OHOS_external_memory" | HarmonyOS平台external_memory扩展名。 起始版本： 10 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| VkResult (VKAPI_PTR PFN_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface) | PFN_vkCreateSurfaceOHOS | 创建Vulkan Surface的函数指针定义。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface) | - | 创建Vulkan Surface。 |
| VkResult (VKAPI_PTR PFN_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH_NativeBuffer buffer, VkNativeBufferPropertiesOHOS* pProperties) | PFN_vkGetNativeBufferPropertiesOHOS | 获取OH_NativeBuffer属性的函数指针定义。 |
| VkResult (VKAPI_PTR PFN_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS pInfo, struct OH_NativeBuffer** pBuffer) | PFN_vkGetMemoryNativeBufferOHOS | 获取OH_NativeBuffer的函数指针定义。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties) | - | 获取OH_NativeBuffer属性。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer) | - | 获取OH_NativeBuffer。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t* grallocUsage) | - | 根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence) | - | 用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd) | - | 当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。 |
| VkResult (VKAPI_PTR *PFN_vkSetNativeFenceFdOpenHarmony)(VkDevice device, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence) | VKAPI_PTR *PFN_vkSetNativeFenceFdOpenHarmony | 该接口已废弃。 |
| typedef VkResult (VKAPI_PTR PFN_vkGetNativeFenceFdOpenHarmony)(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd) | VKAPI_PTR *PFN_vkGetNativeFenceFdOpenHarmony | 该接口已废弃。 |
| VkResult (VKAPI_PTR PFN_vkGetSwapchainGrallocUsageOHOS)(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t grallocUsage) | VKAPI_PTR *PFN_vkGetSwapchainGrallocUsageOHOS | 根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。应用开发者无需使用该接口。 |
| VkResult (VKAPI_PTR *PFN_vkAcquireImageOHOS)(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence) | VKAPI_PTR *PFN_vkAcquireImageOHOS | 用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。应用开发者无需使用该接口。 |
| typedef VkResult (VKAPI_PTR PFN_vkQueueSignalReleaseImageOHOS)(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd) | VKAPI_PTR *PFN_vkQueueSignalReleaseImageOHOS | 当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。应用开发者无需使用该接口。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkSetNativeFenceFdOpenHarmony(VkDevice device, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence) | - | 该接口已废弃。 |
| VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeFenceFdOpenHarmony(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd) | - | 该接口已废弃。 |

**枚举类型说明**

**VkSwapchainImageUsageFlagBitsOHOS**

```ets
enum VkSwapchainImageUsageFlagBitsOHOS
```

描述

图像使用标志位。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| VK_SWAPCHAIN_IMAGE_USAGE_SHARED_BIT_OHOS = 0x00000001 | 共享类型图像标志位。 |
| VK_SWAPCHAIN_IMAGE_USAGE_FLAG_BITS_MAX_ENUM_OHOS = 0x7FFFFFFF | 最大值。 |

**函数说明**

**PFN_vkCreateSurfaceOHOS()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)
```

描述

创建Vulkan Surface的函数指针定义。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| VkInstance instance | Vulkan实例。 |
| const VkSurfaceCreateInfoOHOS* pCreateInfo | 一个VkSurfaceCreateInfoOHOS结构体的指针，包含创建Vulkan Surface时必要的参数。 |
| const VkAllocationCallbacks* pAllocator | 用户自定义内存分配的回调函数，如果不需要可以传入NULL，接口会使用默认的内存分配函数。 |
| VkSurfaceKHR* pSurface | 出参，用于接收创建的Vulkan Surface，类型为VkSurfaceKHR。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，返回值为VK_SUCCESS表示执行成功。 |

**vkCreateSurfaceOHOS()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)
```

描述

创建Vulkan Surface。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| VkInstance instance | Vulkan实例。 |
| const VkSurfaceCreateInfoOHOS* pCreateInfo | 一个VkSurfaceCreateInfoOHOS结构体的指针，包含创建Vulkan Surface时必要的参数。 |
| const VkAllocationCallbacks* pAllocator | 用户自定义内存分配的回调函数，如果不需要可以传入NULL，接口会使用默认的内存分配函数。 |
| VkSurfaceKHR* pSurface | 出参，用于接收创建的Vulkan Surface，类型为VkSurfaceKHR。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK_SUCCESS，表示执行成功。  返回VK_ERROR_OUT_OF_HOST_MEMORY，表示分配VkSurfaceKHR内存失败。  返回VK_ERROR_SURFACE_LOST_KHR，表示操作NativeWindow失败。 |

**PFN_vkGetNativeBufferPropertiesOHOS()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties)
```

描述

获取OH_NativeBuffer属性的函数指针定义。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| const struct OH_NativeBuffer* buffer | OH_NativeBuffer结构体指针。 |
| VkNativeBufferPropertiesOHOS* pProperties | 用于接收OH_NativeBuffer属性的结构体。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，返回值为VK_SUCCESS表示执行成功。 |

**PFN_vkGetMemoryNativeBufferOHOS()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer)
```

描述

获取OH_NativeBuffer的函数指针定义。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| const VkMemoryGetNativeBufferInfoOHOS* pInfo | VkMemoryGetNativeBufferInfoOHOS结构体对象。 |
| struct OH_NativeBuffer** pBuffer | 用于接收获取到的OH_NativeBuffer。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，返回值为VK_SUCCESS表示执行成功。 |

**vkGetNativeBufferPropertiesOHOS()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties)
```

描述

获取OH_NativeBuffer属性。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| const struct OH_NativeBuffer* buffer | OH_NativeBuffer结构体指针。 |
| VkNativeBufferPropertiesOHOS* pProperties | 用于接收OH_NativeBuffer属性的结构体。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK_SUCCESS，表示执行成功。  返回VK_ERROR_INVALID_EXTERNAL_HANDLE_KHR，表示入参存在异常。  返回VK_ERROR_OUT_OF_DEVICE_MEMORY，表示设备内存不足。 |

**vkGetMemoryNativeBufferOHOS()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer)
```

描述

获取OH_NativeBuffer。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| const VkMemoryGetNativeBufferInfoOHOS* pInfo | VkMemoryGetNativeBufferInfoOHOS结构体对象。 |
| struct OH_NativeBuffer** pBuffer | 用于接收获取到的OH_NativeBuffer。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK_SUCCESS，表示执行成功。  返回VK_ERROR_OUT_OF_HOST_MEMORY，表示pInfo入参异常，或获取的pBuffer异常。 |

**vkGetSwapchainGrallocUsageOHOS()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t* grallocUsage)
```

描述

根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。应用开发者无需使用该接口。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

废弃版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkFormat format | 图像格式。 |
| VkImageUsageFlags imageUsage | 图像使用标志。 |
| uint64_t* grallocUsage | 出参, 返回Gralloc(内存分配器)使用标志。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK_SUCCESS，表示执行成功。  返回VK_ERROR_INITIALIZATION_FAILED，表示入参异常。 |

**VKAPI_PTR *PFN_vkGetSwapchainGrallocUsageOHOS()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkGetSwapchainGrallocUsageOHOS)(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t* grallocUsage)
```

描述

根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。应用开发者无需使用该接口。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

废弃版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkFormat format | 图像格式。 |
| VkImageUsageFlags imageUsage | 图像使用标志。 |
| uint64_t* grallocUsage | 出参, 返回Gralloc(内存分配器)使用标志。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下： 返回VK_SUCCESS，表示执行成功。 返回VK_ERROR_INITIALIZATION_FAILED，表示入参异常。 |

**vkAcquireImageOHOS()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

描述

用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。应用开发者无需使用该接口。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

废弃版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkImage image | 要获取的Vulkan图像。 |
| int32_t nativeFenceFd | 原生Fence的文件描述符。 |
| VkSemaphore semaphore | 表示图像可用状态的Vulkan Semaphore(信号量)。 |
| VkFence fence | 用于在图像获取完成时进行同步的Vulkan Fence。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK_SUCCESS，表示执行成功。  返回VK_ERROR_OUT_OF_HOST_MEMORY，表示主机内存不足。 |

**VKAPI_PTR *PFN_vkAcquireImageOHOS()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkAcquireImageOHOS)(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

描述

用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。应用开发者无需使用该接口。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

废弃版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkImage image | 要获取的Vulkan图像。 |
| int32_t nativeFenceFd | 原生Fence的文件描述符。 |
| VkSemaphore semaphore | 表示图像可用状态的Vulkan Semaphore(信号量)。 |
| VkFence fence | 用于在图像获取完成时进行同步的Vulkan Fence。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下： 返回VK_SUCCESS，表示执行成功。 返回VK_ERROR_OUT_OF_HOST_MEMORY，表示主机内存不足。 |

**vkQueueSignalReleaseImageOHOS()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

描述

当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。应用开发者无需使用该接口。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

废弃版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| VkQueue queue | Vulkan队列的句柄。 |
| uint32_t waitSemaphoreCount | 等待Semaphore(信号量)的数量。 |
| const VkSemaphore* pWaitSemaphores | 指向等待Semaphore(信号量)数组的指针。 |
| VkImage image | 要释放的Vulkan图像句柄。 |
| int32_t* pNativeFenceFd | 指向Fence的文件描述符的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK_SUCCESS，表示执行成功。  返回VK_ERROR_DEVICE_LOST，表示Vulkan设备链接丢失。  返回VK_ERROR_OUT_OF_HOST_MEMORY，表示主机内存不足。 |

**VKAPI_PTR *PFN_vkQueueSignalReleaseImageOHOS()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkQueueSignalReleaseImageOHOS)(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

描述

当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。应用开发者无需使用该接口。

系统能力： SystemCapability.Graphic.Vulkan

起始版本： 10

废弃版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| VkQueue queue | Vulkan队列的句柄。 |
| uint32_t waitSemaphoreCount | 等待Semaphore(信号量)的数量。 |
| const VkSemaphore* pWaitSemaphores | 指向等待Semaphore(信号量)数组的指针。 |
| images | 要释放的Vulkan图像句柄。 |
| int32_t* pNativeFenceFd | 指向Fence的文件描述符的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下： 返回VK_SUCCESS，表示执行成功。 返回VK_ERROR_DEVICE_LOST，表示Vulkan设备链接丢失。 返回VK_ERROR_OUT_OF_HOST_MEMORY，表示主机内存不足。 |

**VKAPI_PTR *PFN_vkSetNativeFenceFdOpenHarmony()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkSetNativeFenceFdOpenHarmony)(VkDevice device, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

描述

该接口已废弃。

起始版本： 10

废弃版本： 10

替代接口： [PFN_vkAcquireImageOHOS](#ZH-CN_TOPIC_0000002522242638__vkapi_ptr-pfn_vkacquireimageohos)

**VKAPI_PTR *PFN_vkGetNativeFenceFdOpenHarmony()**

```ets
typedef VkResult (VKAPI_PTR *PFN_vkGetNativeFenceFdOpenHarmony)(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

描述

该接口已废弃。

起始版本： 10

废弃版本： 10

替代接口： [PFN_vkQueueSignalReleaseImageOHOS](#ZH-CN_TOPIC_0000002522242638__vkapi_ptr-pfn_vkqueuesignalreleaseimageohos)

**vkSetNativeFenceFdOpenHarmony()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkSetNativeFenceFdOpenHarmony(VkDevice device, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

描述

该接口已废弃。

起始版本： 10

废弃版本： 10

替代接口： [vkAcquireImageOHOS](vulkan_ohos.h.md#ZH-CN_TOPIC_0000002522242638__vkacquireimageohos)

**vkGetNativeFenceFdOpenHarmony()**

```ets
VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeFenceFdOpenHarmony(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

描述

该接口已废弃。

起始版本： 10

废弃版本： 10

替代接口： [vkQueueSignalReleaseImageOHOS](vulkan_ohos.h.md#ZH-CN_TOPIC_0000002522242638__vkqueuesignalreleaseimageohos)