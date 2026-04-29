# Vulkan Surface开发指导

**场景介绍**

在HarmonyOS中，扩展VK_OHOS_surface相关的API创建出来的VkSurfaceKHR会对接到本机窗口（OHNativeWindow）模块，实现本机缓冲区（OHNativeBuffer）的轮转，用于屏幕显示。

创建VkSurfaceKHR对象需要通过OHNativeWindow，而OHNativeWindow需要从XComponent中获取，所以此场景下需要配合XComponent模块和NativeWindow模块一起使用。XComponent模块的具体使用方法请参考[XComponent开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。

**接口说明**

| 接口名 | 描述 |
| --- | --- |
| vkCreateSurfaceOHOS (VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface) | 创建VkSurfaceKHR对象。 |

更多的接口说明请参考[Vulkan](Vulkan支持能力.md)。

**开发步骤**

以下步骤说明了如何创建一个VkSurfaceKHR对象。

HarmonyOS平台宏

使用平台扩展的接口，需要定义一个宏VK_USE_PLATFORM_OHOS，我们在CMakeLists.txt定义这个宏。

```ets
ADD_DEFINITIONS(-DVK_USE_PLATFORM_OHOS=1)
```

添加动态链接库

CMakeLists.txt中添加Vulkan的lib和周边模块的lib。

```ets
libvulkan.so
libace_ndk.z.so
libnative_window.so
libnative_image.so
libnative_buffer.so
```

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

在程序中通过dlopen函数链接libvulkan.so动态库时不需要在CMake中增加依赖，否则会导致符号冲突。

头文件

```ets
#include <ace/xcomponent/native_interface_xcomponent.h>
#include <native_window/external_window.h>
#include <vulkan/vulkan.h>
```

1.

首先需要创建一个Vulkan实例。
```ets
VkInstance instance = VK_NULL_HANDLE;

VkApplicationInfo appInfo = {};
appInfo.sType = VK_STRUCTURE_TYPE_APPLICATION_INFO;
appInfo.pApplicationName = "vulkanExample";
appInfo.pEngineName = "vulkanExample";
appInfo.apiVersion = VK_API_VERSION_1_3;

VkInstanceCreateInfo instanceCreateInfo = {};
instanceCreateInfo.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO;
instanceCreateInfo.pNext = NULL;
instanceCreateInfo.pApplicationInfo = &appInfo;

std::vector<const char *> instanceExtensions = {
    VK_KHR_SURFACE_EXTENSION_NAME,
    VK_OHOS_SURFACE_EXTENSION_NAME // Surface扩展
};
instanceCreateInfo.enabledExtensionCount = static_cast<uint32_t>(instanceExtensions.size());
instanceCreateInfo.ppEnabledExtensionNames = instanceExtensions.data();

vkCreateInstance(&instanceCreateInfo, nullptr, &instance);
```

1.

获取OHNativeWindow。

OHNativeWindow需要从XComponent组件中获取，下面提供一份从XComponent组件中获取OHNativeWindow的代码示例，XComponent模块的具体使用方法请参考[XComponent模块的介绍文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。

  1.

ets/pages/Index.ets中增加一个XComponent组件。
```ets
XComponent({
    id: 'xcomponentId',
    type: 'surface',
    libraryname: 'entry'
})
.margin({ bottom: 20 })
.width(360)
.height(360)
```

  1.

从XComponent组件中获取OHNativeWindow。
```ets
// XComponent在创建Surface时的回调函数
void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window) {
    // 在回调函数里可以拿到OHNativeWindow
    OHNativeWindow *nativeWindow = static_cast<OHNativeWindow *>(window);
}

static napi_value Init(napi_env env, napi_value exports) {
    napi_property_descriptor desc[] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr}};
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);

    napi_value exportInstance = nullptr;
    OH_NativeXComponent *nativeXComponent = nullptr;
    // 获取nativeXComponent
    napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance);
    napi_unwrap(env, exportInstance, reinterpret_cast<void **>(&nativeXComponent));
    // 获取XComponentId
    char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {};
    uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
    OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize);

    // 声明一个XComponent的Callback
    OH_NativeXComponent_Callback callback;
    // 注册OnSurfaceCreated回调函数
    callback.OnSurfaceCreated = OnSurfaceCreatedCB;
    // 将callback注册给nativeXComponent
    OH_NativeXComponent_RegisterCallback(nativeXComponent, &callback);

    return exports;
}
```

1.

创建VkSurfaceKHR对象。
```ets
VkSurfaceKHR surface = VK_NULL_HANDLE;
VkSurfaceCreateInfoOHOS surfaceCreateInfo = {};
surfaceCreateInfo.sType = VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS;
surfaceCreateInfo.window = nativeWindow; // 这里的nativeWindow就是从上一步骤OnSurfaceCreatedCB回调函数中拿到的
int err = vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, NULL, &surface);
if (err != VK_SUCCESS) {
    // Create Surface Failed.
}
```