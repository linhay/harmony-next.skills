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
EGL_EGLEXT_PROTOTYPES
```

#### 支持的接口说明

HarmonyOS目前支持EGL部分接口，支持的接口会随着版本演进，持续更新。

目前支持的接口如下：

[native api中导出的EGL符号列表](../networking/Native api中导出的EGL符号列表.md)