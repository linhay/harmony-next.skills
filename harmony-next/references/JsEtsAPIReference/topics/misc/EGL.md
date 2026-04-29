# EGL

[EGL](https://registry.khronos.org/EGL/sdk/docs/man/) 是Khronos官方提供的渲染API (如[OpenGLES](https://registry.khronos.org/OpenGL-Refpages/es3/) 或 OpenVG) 与底层窗口系统之间的接口。HarmonyOS 现已支持 EGL。

#### 引入EGL能力

如果开发者需要使用EGL相关功能，首先请添加头文件：

```ets
#include <EGL/egl.h>
```

其次在CMakeLists.txt中添加以下动态链接库：

```ets
libEGL.so
```

如果需要调用EGL扩展接口，需要额外添加头文件并且在CMakeLists.txt中添加宏定义：

```ets
#include <EGL/eglext.h>
```

```ets
EGL_EGLEXT_PROTOTYPES
```

**部分扩展接口使用说明**

eglGetNativeClientBufferANDROID

从API version 23开始，支持使用EGL扩展接口eglGetNativeClientBufferANDROID，将[OH_NativeBuffer](native_buffer.h.md)转换为EGLClientBuffer类型，以实现纹理的绑定并进行GPU采样。具体使用方法请参考如下示例代码：

```ets
// 在EGLCore成员变量中已经定义好了如下变量
EGLDisplay m_eglDisplay = EGL_NO_DISPLAY;
OH_NativeBuffer* m_nativeBuffer = {nullptr};
GLuint m_textureId = 0;
// 通过如下函数流程即可实现将OH_NativeBuffer绑定为纹理
bool EGLCore::PrepareNativeBuffer() {
    // 检查并分配nativeBuffer
    if (m_nativeBuffer != nullptr) {
        return true;
    }
    OH_NativeBuffer_Config config {
        .width = 128,
        .height = 128,
        .format = NATIVEBUFFER_PIXEL_FMT_RGBA_8888,
        .usage = NATIVEBUFFER_USAGE_CPU_WRITE | NATIVEBUFFER_USAGE_CPU_READ | NATIVEBUFFER_USAGE_HW_RENDER | NATIVEBUFFER_USAGE_HW_TEXTURE | NATIVEBUFFER_USAGE_CPU_READ_OFTEN | NATIVEBUFFER_USAGE_ALIGNMENT_512
        };
    m_nativeBuffer = OH_NativeBuffer_Alloc(&config);
    if (m_nativeBuffer == nullptr) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to allocate native buffer.");
    }

    // CPU侧对nativeBuffer进行写入
    uint32_t* nativeBuffer;
    OH_NativeBuffer_Map(m_nativeBuffer, (void**)&nativeBuffer);
    for (uint32_t i = 0; i < 128; i++) {
        for (uint32_t j = 0; j < 128; j++) {
            float ypos = static_cast<float>(i) / 127.0f;
            float hue = ypos * 360.0f;
            float xpos = static_cast<float>(j) / 127.0f * 0.6f + 0.4f;
            // 饱和度和亮度设置为最大值以获取鲜艳的颜色
            nativeBuffer[i * 128 + j] = HSVtoRGB_U32(hue, xpos, 1.0f);
        }
    OH_NativeBuffer_Unmap(m_nativeBuffer);

    // 检查EGL扩展支持
    const char* extensions = eglQueryString(m_eglDisplay, EGL_EXTENSIONS);
    if(!strstr(extensions, "EGL_ANDROID_get_native_client_buffer")) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Extension not support.");
        return false;
    }

    // 获取EGL函数指针
    PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC eglGetNativeClientBufferANDROID =
        reinterpret_cast<PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC>(
            eglGetProcAddress("eglGetNativeClientBufferANDROID"));
    if (!eglGetNativeClientBufferANDROID) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to get eglGetNativeClientBufferANDROID pointer.");
        return false;
    }

    // 获取EGLClientBuffer
    EGLClientBuffer clientBuffer = eglGetNativeClientBufferANDROID((struct AHardwareBuffer*)m_nativeBuffer);
    if(!clientBuffer) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Client buffer error.");
        return false;
    }
    PFNEGLCREATEIMAGEKHRPROC eglCreateImageKHR =
        reinterpret_cast<PFNEGLCREATEIMAGEKHRPROC>(
            eglGetProcAddress("eglCreateImageKHR"));
    if(!eglCreateImageKHR) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to get eglCreateImageKHR pointer.");
        return false;
    }

    // 创建并绑定纹理
    EGLint attribs[] = {EGL_IMAGE_PRESERVED_KHR, EGL_TRUE, EGL_NONE};
    EGLImageKHR eglImage = eglCreateImageKHR(
        m_eglDisplay,
        EGL_NO_CONTEXT,
        EGL_NATIVE_BUFFER_OHOS,
        clientBuffer,
        attribs);
    if (eglImage == EGL_NO_IMAGE_KHR) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to create eglImage.");
        return false;
    }
    glGenTextures(1, &m_textureId);
    if(m_textureId == 0) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to generate textures.");
        return false;
    }
    glBindTexture(GL_TEXTURE_2D, m_textureId);

    // 设置纹理参数
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    // 绑定EGLImage
    glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, eglImage);
    // 此时m_nativeBuffer已经绑定到了m_textureId纹理上，可以当作正常纹理使用
    return true;
}
```

调用eglGetNativeClientBufferANDROID所产生的EGLClientBuffer对象在使用完成后需要主动销毁，否则会产生内存泄漏，具体销毁方式参考下列代码片段的示例：

```ets
// 在前面已经通过eglGetNativeClientBufferANDROID创建了EGLClientBuffer类型的clientBuffer变量
// 使用完成后调用如下函数进行销毁
OH_NativeWindow_DestroyNativeWindowBuffer((OHNativeWindowBuffer*)clientBuffer);
```

#### 支持的接口说明

HarmonyOS目前支持EGL部分接口，支持的接口会随着版本演进，持续更新。

目前支持的接口如下：

[native api中导出的EGL符号列表](Native api中导出的EGL符号列表.md)