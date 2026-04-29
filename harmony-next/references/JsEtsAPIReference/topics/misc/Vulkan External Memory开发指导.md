# Vulkan External Memory开发指导

**场景介绍**

VK_OHOS_external_memory 扩展用于在GPU Vulkan环境下与HarmonyOS的本机缓冲区（OHNativeBuffer）之间做零拷贝的内存共享。

该扩展允许：把由HarmonyOS或其他组件（Camera、RenderService、视频解码器、OHNativeWindow等）创建的OHNativeBuffer导入为Vulkan内存（并绑定到VkImage/VkBuffer）。

这可以实现视频帧、相机输出、图像解码器等在生产端与Vulkan渲染/计算端的高效共享，避免额外拷贝或像素转换。

所以，本指导将介绍实现视频解码器与渲染器零拷贝：将解码器输出OHNativeBuffer，直接导入Vulkan。

**接口说明**

**结构体**

| 名称 | 描述 |
| --- | --- |
| VkNativeBufferPropertiesOHOS | 包含了NativeBuffer的属性。 |
| VkNativeBufferFormatPropertiesOHOS | 包含了NativeBuffer的一些格式属性。 |
| VkImportNativeBufferInfoOHOS | 包含了OH_NativeBuffer结构体的指针。 |
| VkMemoryGetNativeBufferInfoOHOS | 用于从Vulkan内存中获取OH_NativeBuffer。 |
| VkExternalFormatOHOS | 表示外部定义的格式标识符。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeBufferPropertiesOHOS (VkDevice device, const struct OH_NativeBuffer *buffer, VkNativeBufferPropertiesOHOS *pProperties) | 获取OH_NativeBuffer属性。 |

**开发步骤**

以下步骤说明了如何将视频解码器输出的本机缓冲区（OHNativeBuffer）导入为Vulkan内存，并绑定到VkImage/VkBuffer。

1.

启动渲染子线程，初始化Vulkan环境，动态加载libvulkan.so, 并加载Vulkan基础函数的指针。
```ets
void VulkanRenderThread::ThreadMainLoop() {
    threadId_ = std::this_thread::get_id();
    if (!InitRenderContext()) {
        return;
    }
    if (!InitNativeVsync()) {
        return;
    }
    if (!CreateNativeImage()) {
        return;
    }
    while (running_) {
        {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread", "Waiting for Vsync.");
            std::unique_lock<std::mutex> Lock(wakeUpMutex_);
            wakeUpCond_.wait(Lock, [this]() { return wakeup_ || vSyncCnt_ > 0 || availableFrameCnt_ > 0; });
            wakeup_ = false;
            vSyncCnt_--;
            (void)OH_NativeVSync_RequestFrame(nativeVsync_, &VulkanRenderThread::OnVsync, this);
        }

        std::vector<VulkanRenderTask> tasks;
        {
            std::lock_guard<std::mutex> lock(taskMutex_);
            tasks.swap(tasks_);
        }
        for (const auto &task : tasks) {
            task(*vulkanRenderContext_);
        }
        if (availableFrameCnt_ <= 0) {
            continue;
        }
        DrawImage();
        availableFrameCnt_--;
    }
```

 动态加载libvulkan.so，并加载Vulkan基础函数的指针。
```ets
// Dynamically load Vulkan library and base function pointers
bool LoadVulkanLibrary() {
    // Load vulkan library
    constexpr char *path = "libvulkan.so";
    dlerror();
    g_libVulkan = dlopen(path, RTLD_NOW | RTLD_LOCAL);
    if (!g_libVulkan) {
        OH_LOG_ERROR(LOG_APP, "Failed to load vulkan Library, %{public}s", dlerror());
        return false;
    }

    // // Load base function pointers
    vkEnumerateInstanceExtensionProperties = reinterpret_cast<PFN_vkEnumerateInstanceExtensionProperties>(
        dlsym(g_libVulkan, "vkEnumerateInstanceExtensionProperties"));
    vkEnumerateInstanceLayerProperties = reinterpret_cast<PFN_vkEnumerateInstanceLayerProperties>(
        dlsym(g_libVulkan, "vkEnumerateInstanceLayerProperties"));
    vkCreateInstance = reinterpret_cast<PFN_vkCreateInstance>(dlsym(g_libVulkan, "vkCreateInstance"));
    vkGetInstanceProcAddr = reinterpret_cast<PFN_vkGetInstanceProcAddr>(dlsym(g_libVulkan, "vkGetInstanceProcAddr"));
    vkGetDeviceProcAddr = reinterpret_cast<PFN_vkGetDeviceProcAddr>(dlsym(g_libVulkan, "vkGetDeviceProcAddr"));

    return true;
}
```

1.

创建NatvieImage对象作为OHNativeBuffer的消费端，并根据NativeImage对象获取对应的NativeWindow对象，将NativeWindow句柄传给视频编解码，作为OHNativeBuffer的生产端，用于生产视频帧内容。
```ets
bool VulkanRenderThread::CreateNativeImage() {
    nativeImage_ = OH_ConsumerSurface_Create();
    if (nativeImage_ == nullptr) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread", "OH_NativeImage_Create failed.");
        return false;
    }
    int ret = 0;
    {
        std::lock_guard<std::mutex> Lock(nativeImageSurfaceIdMutex_);
        nativeImageWindow_ = OH_NativeImage_AcquireNativeWindow(nativeImage_);
        ret = OH_NativeImage_GetSurfaceId(nativeImage_, &nativeImageSurfaceId_);
    }
    if (ret != 0) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread",
                    "OH_NativeImage_GetSurfaceId failed, ret is %{public}d.", ret);
        return false;
    }

    nativeImageFrameAvailableListener_.context = this;
    nativeImageFrameAvailableListener_.onFrameAvailable = &VulkanRenderThread::OnNativeImageFrameAvailable;
    ret = OH_NativeImage_SetOnFrameAvailableListener(nativeImage_, nativeImageFrameAvailableListener_);
    if (ret != 0) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread",
                    "OH_NativeImage_SetonFrameAvailableListener failed, ret is %{public}d.", ret);
        return false;
    }
    return true;
}
```

1.

获取XComponent的NativeWindow对象，根据NativeWindow对象创建出Vulkan环境的VkSurface，用于绘制显示内容。
```ets
void VulkanRenderThread::UpdateNativeWindow(void *window, uint64_t width, uint64_t height) {
    OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "RenderThread", "UpdateNativeWindow.");
    auto nativeWindow = reinterpret_cast<OHNativeWindow *>(window);
    PostTask([this, nativeWindow, width, height](VulkanRender &renderContext) {
        if (nativeWindow_ != nativeWindow) {
            if (nativeWindow_ != nullptr) {
                (void)OH_NativeWindow_NativeObjectUnreference(nativeWindow_);
            }
            nativeWindow_ = nativeWindow;
            if (nativeWindow_ != nullptr) {
                (void)OH_NativeWindow_NativeObjectReference(nativeWindow_);
            }
        if (nativeWindow_ != nullptr) {
            vulkanRenderContext_->SetupWindow(nativeWindow_);
        }
    });
}
```

 同时更新初始化Vulkan的上下文，包括Vulkan的实列、选择物理设备、创建渲染管线等。
```ets
void VulkanRender::SetupWindow(NativeWindow *nativeWindow) {
    nativeWindow_ = nativeWindow;
    CreateInstance();
    vkExample::utils::LoadVulkanFunctions(instance);
    CreateSurface();
    PickPhysicalDevice();
    CreateLogicalDevice();
    vkExample::utils::LoadVulkanFunctions(device);

    createSwapChain();
    createRenderPass();
    createFrameBuffersAndImages();
    createVertexBuffer();
    createUniformBuffer();
    deviceInfoInitialized = true;
}
```

 通过vkCreateSurfaceOHOS()创建VkSurface对象。
```ets
bool VulkanRender::CreateSurface() {
    VkSurfaceCreateInfoOHOS surfaceCreateInfo{};
    surfaceCreateInfo.sType = VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS;
    if (nativeWindow_ == nullptr) {
        OH_LOG_INFO(LOG_APP, "nativeWindow_ is nulptr.Failed to create surface !");
        return false;
    }
    surfaceCreateInfo.window = nativeWindow_;
    surfaceCreateInfo.flags = 0;
    surfaceCreateInfo.pNext = nullptr;
    bool res = CheckResult(vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, nullptr, &surface));
    return res;
}
```

1.

初始化视频解码的环境，包括初始化解封装器、初始化解码器。
```ets
napi_value PluginRender::StartPlayer(napi_env env, napi_callback_info info)
{
    SampleInfo sampleInfo;
    size_t argc = 4;
    napi_value args[4] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    napi_get_value_int32(env, args[0], &sampleInfo.inputFd);
    napi_get_value_int64(env, args[1], &sampleInfo.inputFileOffset);
    napi_get_value_int64(env, args[2], &sampleInfo.inputFileSize);
    size_t length = 0;
    napi_status status = napi_get_value_string_utf8(env, args[3], nullptr, 0, &length);
    char* buf = new char[length + 1];
    std::memset(buf, 0, length + 1);
    status = napi_get_value_string_utf8(env, args[3], buf, length + 1, &length);
    std::string type = buf;
    PluginRender *render = PluginRender::GetInstance(type);
    if (render != nullptr) {
        if (type == "Vulkan") {
            sampleInfo.window = render->vulkanRenderThread_->GetNativeImageWindow();
        } else {
            sampleInfo.window = render->nativeWindow;
        }
    int32_t ret = Player::GetInstance().Init(sampleInfo);
    if (ret != AVCODEC_SAMPLE_ERR_OK) {
        return nullptr;
    }
    Player::GetInstance().Start();
    return nullptr;
}
```

1.

启动解码器、解码输入子线程、解码输出子线程。
```ets
int32_t Player::Start() {
    std::unique_lock<std::mutex> lock(mutex_);
    int32_t ret;
    if (isStarted_ || demuxer_ == nullptr) {
        OH_LOG_ERROR(LOG_APP, "Already started.");
        return AVCODEC_SAMPLE_ERR_ERROR;
    }

    if (videoDecContext_) {
        ret = videoDecoder_->Start();
        if (ret != AVCODEC_SAMPLE_ERR_OK) {
            OH_LOG_ERROR(LOG_APP, "Video Decoder start failed");
            lock.unlock();
            StartRelease();
            return AVCODEC_SAMPLE_ERR_ERROR;
        }
        isStarted_ = true;
        videoDecInputThread_ = std::make_unique<std::thread>(&Player::VideoDecInputThread, this);
        videoDecOutputThread_ = std::make_unique<std::thread>(&Player::VideoDecOutputThread, this);

        if (videoDecInputThread_ == nullptr || videoDecOutputThread_ == nullptr) {
            OH_LOG_ERROR(LOG_APP, "Create thread failed");
            lock.unlock();
            StartRelease();
            return AVCODEC_SAMPLE_ERR_ERROR;
        }

    OH_LOG_INFO(LOG_APP, "Succeed");
    doneCond_.notify_all();
    return AVCODEC_SAMPLE_ERR_OK;
}
```

1.

在解码输入子线程中，通过解封装器读取视频数据，并交给解码器。
```ets
void Player::VideoDecInputThread() {
    while (true) {
        if (!isStarted_) {
            OH_LOG_ERROR(LOG_APP, "Decoder input thread out");
            break;;
        }

        std::unique_lock<std::mutex> lock(videoDecContext_->inputMutex);
        bool condRet = videoDecContext_->inputCond.wait_for(
            lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->inputBufferInfoQueue.empty(); });
        if (!isStarted_) {
            OH_LOG_ERROR(LOG_APP, "Work done, thread out");
            break;
        }
        if (videoDecContext_->inputBufferInfoQueue.empty()) {
            OH_LOG_ERROR(LOG_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
            continue;
        }

        CodecBufferInfo bufferInfo = videoDecContext_->inputBufferInfoQueue.front();
        videoDecContext_->inputBufferInfoQueue.pop();
        videoDecContext_->inputFrameCount++;
        lock.unlock();

        demuxer_->ReadSample(demuxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                            bufferInfo.attr);

        int32_t ret = videoDecoder_->PushInputBuffer(bufferInfo);
        if (ret != AVCODEC_SAMPLE_ERR_OK) {
            OH_LOG_ERROR(LOG_APP, "Push data failed, thread out");
            break;
        }

        if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
            OH_LOG_ERROR(LOG_APP, "Catch EOS, thread out");
            break;
        }
```

1.

在解码输出子线程中，将解码后的视频提交给输出Surface。
```ets
void Player::VideoDecOutputThread() {
    sampleInfo_.frameInterval = MICROSECOND / sampleInfo_.frameRate;
    while (true) {
        thread_local auto lastPushTime = std::chrono::system_clock::now();
        if (!isStarted_) {
            OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
            break;
        }
        std::unique_lock<std::mutex> lock(videoDecContext_->outputMutex);
        bool condRet = videoDecContext_->outputCond.wait_for(
            lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->outputBufferInfoQueue.empty(); });
        if (!isStarted_) {
            OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
            break;
        }
        if (videoDecContext_->outputBufferInfoQueue.empty()) {
            OH_LOG_ERROR(LOG_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
            continue;
        }

        CodecBufferInfo bufferInfo = videoDecContext_->outputBufferInfoQueue.front();
        videoDecContext_->outputBufferInfoQueue.pop();
        if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
            OH_LOG_ERROR(LOG_APP, "Catch EOS, thread out");
            break;
        }
        videoDecContext_->outputFrameCount++;
        OH_LOG_INFO(LOG_APP,"Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}ld",
                            videoDecContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
                            bufferInfo.attr.pts);
        lock.unlock();

        int32_t ret = videoDecoder_->FreeOutputBuffer(bufferInfo.bufferIndex, true);
        if (ret != AVCODEC_SAMPLE_ERR_OK) {
            OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
            break;
        }

        std::this_thread::sleep_until(lastPushTime + std::chrono::microseconds(sampleInfo_.frameInterval));
        lastPushTime = std::chrono::system_clock::now();
    }
    StartRelease();
}
```

1.

在NativeImage有可用数据后，通过OH_NativeImage_AcquireNativeWindowBuffer()获取视频数据，并通过OH_NativeBuffer_FromNativeWindowBuffer()转化NativeBuffer的类型。
```ets
void VulkanRenderThread::DrawImage() {
    OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "VulkanRenderThread", "DrawImage.");
    int ret;
    OHNativeWindowBuffer *inBuffer = nullptr;
    OH_NativeBuffer *nativeBuffer = nullptr;
    int32_t fenceFd1 = -1;
    ret = OH_NativeImage_AcquireNativeWindowBuffer(nativeImage_, &inBuffer, &fenceFd1);
    ret = OH_NativeWindow_NativeObjectReference(inBuffer);
    ret = OH_NativeBuffer_FromNativeWindowBuffer(inBuffer, &nativeBuffer);
    if (nativeBuffer == nullptr) {
        OH_NativeWindow_NativeObjectUnreference(inBuffer);
        OH_NativeImage_ReleaseNativeWindowBuffer(nativeImage_, inBuffer, -1);
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "VulkanRenderThread", "nativeBuffer is null.");
        return;
    }
    ret = OH_NativeImage_GetTransformMatrix(nativeImage_, matrix_);
    int32_t transformTmp = 0;
    ComputeTransform(transformTmp, matrix_);
    vulkanRenderContext_->hwBufferToTexture(nativeBuffer, matrix_);
    vulkanRenderContext_->render();
    if (lastInBuffer_ != nullptr) {
        OH_NativeWindow_NativeObjectUnreference(lastInBuffer_);
        OH_NativeImage_ReleaseNativeWindowBuffer(nativeImage_, lastInBuffer_, -1);
    }
    lastInBuffer_ = inBuffer;
}
```

1.

Vulkan根据NativeBuffer创建对应的ImageView用于渲染显示，同时创建对应格式的采样器，将YUV格式的图像采样成RGBA的图像，用于正确的渲染显示。

     ![image](public_sys-resources/note_3.0-zh-cn.webp)

  - API version 23之前，基于标准库VkExternalMemoryImageCreateInfo结构体，系统支持扩展类型VK_EXTERNAL_MEMORY_HANDLE_TYPE_OHOS_NATIVE_BUFFER_BIT_OHOS。

  - 从API version 23开始，VK_EXTERNAL_MEMORY_HANDLE_TYPE_OHOS_NATIVE_BUFFER_BIT_OHOS已废弃，请改用VK_EXTERNAL_MEMORY_HANDLE_TYPE_OH_NATIVE_BUFFER_BIT_OHOS。

```ets
void VulkanRender::hwBufferToTexture(OH_NativeBuffer *buffer, float transformMatrix[16]) {
    OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "VulkanRenderThread", "hwBufferToTexture.");
    if (!deviceInfoInitialized) {
        return;
    }
    UniformBufferObject ubo{};
    memcpy(ubo.mvp, transformMatrix, sizeof(float) * 16);
    memcpy(buffersInfo.uniformBufferMapped, &ubo, sizeof(ubo));
    VkNativeBufferFormatPropertiesOHOS nbFormatProps = {
        .sType = VK_STRUCTURE_TYPE_NATIVE_BUFFER_FORMAT_PROPERTIES_OHOS,
        .pNext = nullptr
    };
    VkNativeBufferPropertiesOHOS nbProps = {.sType = VK_STRUCTURE_TYPE_NATIVE_BUFFER_PROPERTIES_OHOS,
                                            .pNext = &nbFormatProps};
    CheckResult(vkGetNativeBufferPropertiesOHOS(device, buffer, &nbProps));

    VkImportNativeBufferInfoOHOS importBufferInfo = {
        .sType = VK_STRUCTURE_TYPE_IMPORT_NATIVE_BUFFER_INFO_OHOS,
        .pNext = nullptr,
        .buffer = buffer
    };

    VkMemoryDedicatedAllocateInfo dedicatedAllocateInfo = {
        .sType = VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO,
        .pNext = &importBufferInfo,
        .image = VK_NULL_HANDLE, // wiLl be set later
        .buffer = VK_NULL_HANDLE
    };

    VkPhysicalDeviceMemoryProperties physicalDeviceMemProps;
    uint32_t foundTypeIndex = 0;
    vkGetPhysicalDeviceMemoryProperties(gpuDevice, &physicalDeviceMemProps);
    uint32_t memTypeCnt = physicalDeviceMemProps.memoryTypeCount;
    for (uint32_t i = 0; i < memTypeCnt; ++i) {
        if (nbProps.memoryTypeBits & (1 << i)) {
            const VkPhysicalDeviceMemoryProperties &pdmp = physicalDeviceMemProps;
            uint32_t supportedFLags = pdmp.memoryTypes[i].propertyFlags & VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT;
            if (supportedFLags == VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT) {
                foundTypeIndex = i;
                break;
            }

    VkMemoryAllocateInfo allocInfo{
        .sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO,
        .pNext = &dedicatedAllocateInfo,
        .allocationSize = nbProps.allocationSize,
        .memoryTypeIndex = 0 // Memory type assigned in the next step
    };

    mapMemoryTypeToIndex(nbProps.memoryTypeBits, VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT, &allocInfo.memoryTypeIndex);
    VkExternalFormatOHOS externalFormat;
    externalFormat.sType = VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_OHOS;
    externalFormat.pNext = nullptr;
    externalFormat.externalFormat = 0;
    if (nbFormatProps.format == VK_FORMAT_UNDEFINED) {
        externalFormat.externalFormat = nbFormatProps.externalFormat;
    }

    VkExternalMemoryImageCreateInfo externalMemoryImageInfo = {
        .sType = VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO,
        .pNext = &externalFormat,
        .handleTypes = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OH_NATIVE_BUFFER_BIT_OHOS,
    };

    VkImageUsageFlags usageFlags = VK_IMAGE_USAGE_SAMPLED_BIT;
    if (nbFormatProps.format != VK_FORMAT_UNDEFINED) {
        usageFlags = usageFlags | VK_IMAGE_USAGE_TRANSFER_SRC_BIT | VK_IMAGE_USAGE_TRANSFER_DST_BIT |
                    VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT | VK_IMAGE_USAGE_INPUT_ATTACHMENT_BIT;
    }
    OH_NativeBuffer_Config config;
    OH_NativeBuffer_GetConfig(buffer, &config);
    VkImageCreateInfo image_create_info = {
        .sType = VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO,
        .pNext = &externalMemoryImageInfo,
        .flags = 0,
        .imageType = VK_IMAGE_TYPE_2D,
        .format = nbFormatProps.format,
        .extent = {static_cast<uint32_t>(config.width), static_cast<uint32_t>(config.height), 1},
        .mipLevels = 1,
        .arrayLayers = 1,
        .samples = VK_SAMPLE_COUNT_1_BIT,
        .tiling = VK_IMAGE_TILING_OPTIMAL,
        .usage = usageFlags,
        .sharingMode = VK_SHARING_MODE_EXCLUSIVE,
        .queueFamilyIndexCount = 1,
        .pQueueFamilyIndices = &queueFamilyIndex_,
        // VK_IMAGE_LAYOUT_UNDEFINED is mandatory when using external memory
        .initialLayout = VK_IMAGE_LAYOUT_UNDEFINED
    };

    CheckResult(vkCreateImage(device, &image_create_info, nullptr, &externalTextureImage));
    dedicatedAllocateInfo.image = externalTextureImage;
    CheckResult(vkAllocateMemory(device, &allocInfo, nullptr, &externalTextureMemory));
    CheckResult(vkBindImageMemory(device, externalTextureImage, externalTextureMemory, 0));

    VkSamplerYcbcrConversionCreateInfo ycbcrCreateInfo = {
        .sType = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO,
        .ycbcrRange = nbFormatProps.suggestedYcbcrRange,
        .components = nbFormatProps.samplerYcbcrConversionComponents,
        .xChromaOffset = nbFormatProps.suggestedXChromaOffset,
        .yChromaOffset = nbFormatProps.suggestedYChromaOffset,
        .chromaFilter = VK_FILTER_LINEAR,
        .forceExplicitReconstruction = false
    };

    if (nbFormatProps.format == VK_FORMAT_UNDEFINED) {
        ycbcrCreateInfo.pNext = &externalFormat;
        ycbcrCreateInfo.format = VK_FORMAT_UNDEFINED;
        ycbcrCreateInfo.ycbcrModel = nbFormatProps.suggestedYcbcrModel;
    }

    CheckResult(
        vkCreateSamplerYcbcrConversion(device, &ycbcrCreateInfo, nullptr, &externalTextureInfo.ycbcrConversion));

    VkSamplerYcbcrConversionInfo convInfoWrap = {
        .sType = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO,
        .conversion = externalTextureInfo.ycbcrConversion,
        .pNext = nullptr,
    };

    VkImageViewCreateInfo view = {
        .sType = VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO,
        .pNext = &convInfoWrap,
        .flags = 0,
        .image = externalTextureImage,
        .viewType = VK_IMAGE_VIEW_TYPE_2D,
        .format = nbFormatProps.format,
        .components =
            {
                VK_COMPONENT_SWIZZLE_IDENTITY,
                VK_COMPONENT_SWIZZLE_IDENTITY
            },
        .subresourceRange = {VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1},
    };
    CheckResult(vkCreateImageView(device, &view, nullptr, &externalTextureInfo.view));

    // Create sampler
    const VkSamplerCreateInfo sampler = {
        .sType = VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO,
        .pNext = &convInfoWrap,
        .magFilter = VK_FILTER_NEAREST,
        .minFilter = VK_FILTER_NEAREST,
        .mipmapMode = VK_SAMPLER_MIPMAP_MODE_NEAREST,
        .addressModeU = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
        .addressModeV = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
        .addressModeW = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
        .mipLodBias = 0.0f,
        .compareEnable = VK_FALSE,
        .anisotropyEnable = VK_FALSE,
        .maxAnisotropy = 1,
        .compareOp = VK_COMPARE_OP_NEVER,
        .minLod = 0.0f,
        .maxLod = 0.0f,
        .borderColor = VK_BORDER_COLOR_FLOAT_OPAQUE_WHITE,
        .unnormalizedCoordinates = VK_FALSE
    };
    CheckResult(vkCreateSampler(device, &sampler, nullptr, &externalTextureInfo.sampler));

    createDescriptorSetLayout();
    createDescriptorSet();

    VkDescriptorImageInfo imageInfo = {
        .sampler = externalTextureInfo.sampler,
        .imageView = externalTextureInfo.view,
        .imageLayout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL
    };

    VkDescriptorBufferInfo bufferInfo = {
        .buffer = buffersInfo.uniformBuf, .offset = 0, .range = sizeof(UniformBufferObject)};
    VkWriteDescriptorSet bufferWrite = {.sType = VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET,
                                        .dstSet = gfxPipelineInfo.descSet,
                                        .dstBinding = 0,
                                        .dstArrayElement = 0,
                                        .descriptorCount = 1,
                                        .descriptorType = VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER,
                                        .pImageInfo = nullptr,
                                        .pBufferInfo = &bufferInfo,
                                        .pTexelBufferView = nullptr};
    VkWriteDescriptorSet imageWrite = {.sType = VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET,
                                    .dstSet = gfxPipelineInfo.descSet,
                                    .dstBinding = 1,
                                    .dstArrayElement = 0,
                                    .descriptorCount = 1,
                                    .descriptorType = VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER,
                                    .pImageInfo = &imageInfo,
                                    .pBufferInfo = nullptr,
                                    .pTexelBufferView = nullptr};
    gfxPipelineInfo.descWrites[0] = bufferWrite;
    gfxPipelineInfo.descWrites[1] = imageWrite;
    vkUpdateDescriptorSets(device, 2, gfxPipelineInfo.descWrites, 0, nullptr);

    createGraphicsPipeline();
    createOtherStaff();

    recordCommandBuffer();
    OH_LOG_INFO(LOG_APP, "hwBufferToTexture end");
}
```