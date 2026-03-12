# OpenGL ES

OpenGL 是一种跨平台的图形 API，用于为 3D 图形处理硬件指定标准的软件接口。[OpenGL ES](https://www.khronos.org/opengles/) 是 OpenGL 规范的一种形式，适用于嵌入式设备。HarmonyOS 现已支持 OpenGL ES 3.2。

#### 支持的能力

OpenGL ES 3.2

#### 标准库中导出的符号列表

[native api中导出的OpenGL ES 3.2符号列表](Native api中导出的OpenGL ES 3.2符号列表.md)

#### 引入OpenGL能力

如果开发者使用OpenGL的相关能力，需要添加相关动态链接库和头文件。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```ets
libace_ndk.z.so
libace_napi.z.so
libGLESv3.so
libEGL.so
```

**头文件**

```ets
#include <ace/xcomponent/native_interface_xcomponent.h>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <EGL/eglplatform.h>
#include <GLES3/gl3.h>
```

#### 相关参考

针对OpenGL ES的使用和相关开发，需要同步了解NDK的开发过程，以及XComponent组件等的使用。具体可参考:

-

[NDK开发参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-development-overview)

-

[NodeAPI参考](Node-API.md)

-

[XComponentNode参考](XComponentNode.md)

-

[XComponent参考](XComponent.md)

#### OpenGL ES扩展接口

- OpenGL ES扩展接口的官方参考文档：[OpenGL ES扩展接口](https://registry.khronos.org/OpenGL/index_es.php)
- 开发者可以调用glGetString查询芯片厂商支持的扩展接口，调用之前务必初始化上下文。具体示例如下：

```ets
EGLDisplay display;
EGLConfig config;
EGLContext context;
EGLSurface surface;
EGLint majorVersion;
EGLint minorVersion;
EGLNativeWindowType win;
display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
eglInitialize(display, &majorVersion, &minorVersion);
EGLint attribs[] = {
    EGL_RENDERABLE_TYPE,
    EGL_OPENGL_ES2_BIT,
    EGL_BLUE_SIZE, 8,
    EGL_GREEN_SIZE, 8,
    EGL_RED_SIZE, 8,
    EGL_NONE
};
eglChooseConfig(display, attribs, &config, 1, &numConfigs);
context = eglCreateContext(display, config, EGL_NO_CONTEXT, NULL);
surface = eglCreatePbufferSurface(display, config, NULL);
eglMakeCurrent(display, surface, surface, context);

char *strTest = new char[1024];
strTest = (char *)glGetString(GL_EXTENSIONS); // 返回值strTest中会列出所有的扩展接口，并且用空格分隔开
bool isHave = strTest.find("GL_OES_matrix_palette") != -1 ?
    true :
    false; // 查询是否有某个扩展接口，有则isHave为true，没有则为false
```

#### 简单示例

```ets
void enableVertexAttrib(GLuint index, float *data, int32_t len)
{
    GLuint buffer;
    glGenBuffers(1, &buffer);
    glBindBuffer(GL_ARRAY_BUFFER, buffer);
    glBufferData(GL_ARRAY_BUFFER, len, data, GL_STATIC_DRAW);
    glVertexAttribPointer(index, TRIANGLES_POINT, GL_FLOAT, GL_FALSE, 0, 0);
    glEnableVertexAttribArray(index);
    return;
}

int32_t Init(void *window, int32_t width,  int32_t height)
{
    EGLNativeWindowType mEglWindow;
    EGLDisplay mEGLDisplay = EGL_NO_DISPLAY;
    EGLConfig mEGLConfig = nullptr;
    EGLContext mEGLContext = EGL_NO_CONTEXT;
    EGLContext mSharedEGLContext = EGL_NO_CONTEXT;
    EGLSurface mEGLSurface = nullptr;
    EGLint configsNum;
    mEglWindow = reinterpret_cast<EGLNativeWindowType>(window);

    //初始化EGL Display
    mEGLDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);
    EGLint eglMajVers;
    EGLint eglMinVers;
    eglInitialize(mEGLDisplay, &eglMajVers, &eglMinVers);

    //配置EGL
    EGLint attribList[] = {
            EGL_SURFACE_TYPE, EGL_WINDOW_BIT, EGL_RENDERABLE_TYPE, EGL_OPENGL_ES3_BIT,
            EGL_RED_SIZE, 8,
            EGL_GREEN_SIZE, 8,
            EGL_BLUE_SIZE, 8,
            EGL_NONE
    };
    eglChooseConfig(mEGLDisplay, attribList, &mEGLConfig, 1, &configsNum);

    EGLint winAttribs[] = {EGL_GL_COLORSPACE_KHR, EGL_GL_COLORSPACE_SRGB_KHR, EGL_NONE};

    //创建EGL Surface
    mEGLSurface = eglCreateWindowSurface(mEGLDisplay, mEGLConfig, mEglWindow, winAttribs);

    //创建EGL Context
    EGLint attrib3_list[] = {
        EGL_CONTEXT_CLIENT_VERSION, 3,
    };
    mEGLContext = eglCreateContext(mEGLDisplay, mEGLConfig, mSharedEGLContext, attrib3_list);

    //绑定EGL Context和Surface
    eglMakeCurrent(mEGLDisplay, mEGLSurface, mEGLSurface, mEGLContext);

    // 创建着色点程序
    const char* g_vertexShader =
        "#version 300 es\n"
        "in vec4 a_pos;\n"
        "in vec4 a_color;\n"
        "uniform mat4 a_mx;\n"
        "uniform mat4 a_my;\n"
        "out vec4 v_color;\n"
        "void main() {\n"
        "    gl_Position = a_mx * a_my * a_pos;\n"
        "    v_color = a_color;\n"
        "}";

    const char* g_fragmentShader =
        "#version 300 es\n"
        "precision mediump float;\n"
        "in vec4 v_color;\n"
        "out vec4 fragColor;\n"
        "void main() {\n"
        "    fragColor = v_color;\n"
        "}";

    // 创建顶点着色器
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &g_vertexShader, nullptr);
    glCompileShader(vertexShader);

    //创建片段着色器
    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &g_fragmentShader, nullptr);
    glCompileShader(fragmentShader);

    //创建着色器程序
    mProgramHandle = glCreateProgram();
    glAttachShader(mProgramHandle, vertexShader);
    glAttachShader(mProgramHandle, fragmentShader);
    glLinkProgram(mProgramHandle);

    //使用着色器程序
    glUseProgram(mProgramHandle);

    // 清理
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    return 0;
}

void Update(float angleXOffset, float angleYOffset)
{
    const float pi = 3.141592;

    // 创建顶点位置数据数组vertexData
    float g_vertexData[] = {
        -0.75, -0.50, -0.43, 0.75, -0.50, -0.43, 0.00,  -0.50, 0.87,  0.75, -0.50, -0.43,
        0.00,  -0.50, 0.87,  0.00, 1.00,  0.00,  0.00,  -0.50, 0.87,  0.00, 1.00,  0.00,
        -0.75, -0.50, -0.43, 0.00, 1.00,  0.00,  -0.75, -0.50, -0.43, 0.75, -0.50, -0.43,
    };

    // 创建顶点颜色数组colorData
    float g_colorData[] = {
        1, 0, 0, 1, 0, 0, 1, 0, 0, /* 红色——面1 */
        1, 0, 0, 1, 0, 0, 1, 0, 0, /* 红色——面2 */
        1, 0, 0, 1, 0, 0, 1, 0, 0, /* 红色——面3 */
        1, 0, 0, 1, 0, 0, 1, 0, 0  /* 红色——面4 */
    };

    // 顶点法向量数组normalData
    float g_normalData[] = {
        0.00,  -1.00, 0.00,  0.00,  -1.00, 0.00,  0.00,  -1.00, 0.00, -0.83, -0.28, -0.48,
        -0.83, -0.28, -0.48, -0.83, -0.28, -0.48, -0.83, 0.28,  0.48, -0.83, 0.28,  0.48,
        -0.83, 0.28,  0.48,  0.00,  -0.28, 0.96,  0.00,  -0.28, 0.96, 0.00,  -0.28, 0.96,
    };

    // 设置视口大小
    glViewport(0, 0, m_width, m_height);

    // 清除颜色缓存
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    // 获取着色器程序中变量的位置句柄
    GLint aPos = glGetAttribLocation(mProgramHandle, "a_pos");
    GLint aColor = glGetAttribLocation(mProgramHandle, "a_color");
    GLint aNormal = glGetAttribLocation(mProgramHandle, "a_normal");
    GLint uLightColor = glGetUniformLocation(mProgramHandle, "u_lightColor");
    GLint uLightDirection = glGetUniformLocation(mProgramHandle, "u_lightDirection");
    GLint aMx = glGetUniformLocation(mProgramHandle, "a_mx");
    GLint aMy = glGetUniformLocation(mProgramHandle, "a_my");

    angleX = angleXOffset;
    angleY = angleYOffset;

    // y轴旋转度
    float radianY = (angleY * pi) / 180.0;
    float cosY = cosf(radianY);
    float sinY = sinf(radianY);
    float myArr[] = {
        cosY, 0, -sinY, 0,
        0, 1, 0, 0,
        sinY, 0, cosY, 0,
        0, 0, 0, 1
    };

    // 向着色器传递4x4矩阵数据
    glUniformMatrix4fv(aMy, 1, false, myArr);

    // x轴旋转度
    float radianX = (angleX * pi) / 180.0;
    float cosX = cosf(radianX);
    float sinX = sinf(radianX);
    float mxArr[] = {
        1, 0, 0, 0, 0, cosX, -sinX, 0, 0, sinX, cosX, 0, 0, 0, 0, 1
    };

    glUniformMatrix4fv(aMx, 1, false, mxArr);

    // 给平行光传入颜色和方向数据，RGB(1,1,1),单位向量(x,y,z)
    glUniform3f(uLightColor, 1.0, 1.0, 1.0);

    // 保证向量(x,y,z)的长度为1，即单位向量
    float x = 2.0 / sqrt(15);
    float y = 2.0 / sqrt(15);
    float z = 3.0 / sqrt(15);

    glUniform3f(uLightDirection, x, -y, z);

    // 创建缓冲区buffer，传入顶点位置数据g_vertexData
    enableVertexAttrib(aPos, g_vertexData, sizeof(g_vertexData));
    enableVertexAttrib(aNormal, g_normalData, sizeof(g_normalData));
    // 创建缓冲区colorBuffer，传入顶点颜色数据g_colorData
    enableVertexAttrib(aColor, g_colorData, sizeof(g_colorData));

    glEnable(GL_DEPTH_TEST);

    // 绘制四棱锥
    glDrawArrays(GL_TRIANGLES, 0, TETRAHEDRON_POINT);

    //交换缓冲区
    eglSwapBuffers(mEGLDisplay, mEGLSurface);
}
```

该示例通过EGL创建和设置整个OpenGL ES渲染环境，实现一个3D四棱锥的渲染程序，下面详细地解释下每个步骤。

#### 使用eglGetDisplay连接渲染目标设备

```ets
EGLDisplay eglGetDisplay(EGLNativeDisplayType display_id);
```

eglGetDisplay是EGL库中的函数，它返回EGLDisplay对象用于表示与渲染目标设备的连接。当显示连接不可用时，将返回EGL_NO_DISPLAY表示连接不可用。

display_id 参数通常是一个表示显示设备的本地显示类型，EGLNativeDisplayType是为了匹配窗口显示类型，在各个平台有不同的定义。如果您只是希望使用默认的显示设备，那么您可以直接使用 EGL_DEFAULT_DISPLAY，而不需要显式地指定 display_id。

#### 使用eglInitialize初始化EGL

当成功打开连接之后则需要调用eglInitialize初始化EGL。

```ets
EGLBoolean eglInitialize(EGLDisplay display,    // 指定EGL显示连接
                         EGLint *majorVersion,  // 指定EGL实现返回的主版本号，可能为NULL
                         EGLint *minorVersion); // 指定EGL实现返回的次版本号，可能为NULL
```

这个函数用于初始化EGL内部数据结构，将返回EGL的版本号，并将其保存在majorVersion和minorVersion中。

如果初始化成功，则返回EGL_TRUE，否则返回EGL_FALSE。另外还可以通过EGLint eglGetError()，查询EGL的错误状态：

-

EGL_BAD_DISPLAY：表示没有指定有效的EGLDisplay。

-

EGL_NOT_INITIALIZED：表示EGL不能初始化。

#### 使用eglChooseConfig确定渲染配置

EGL初始化成功之后，需要确定可用渲染表面的类型和配置，目前支持两种方法：

-

可以指定一组需要的配置，使用eglChooseConfig使EGL推荐最佳配置。

当没有特殊配置需求时建议使用此种方法，因为这样更容易获得最佳配置。

```ets
EGLBoolean eglChooseConfig(EGLDisplay dpy,     // EGL显示连接句柄，标识了要进行配置选择的显示连接。
                    const EGLint *attrib_list, // 一个以EGL_NONE结尾的整数数组，用于指定所需配置的属性。属性列表中的每个元素都由属性名称（如EGL_RED_SIZE）和相应的属性值组成。如{EGL_RED_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_BLUE_SIZE, 8, EGL_NONE}。
                        EGLConfig *configs,     // 一个用于存储选择配置的指针数组。eglChooseConfig函数将从可用配置中选择适合条件的配置，并将其存储在此数组中。
                        EGLint config_size,     // configs数组的大小
                        EGLint *num_config);    // 存储满足attrib_list需求，得到的满足需求的实际配置数量。
```

```ets
// 如以上代码所示这里指定所需配置的属性为
EGLint attribList[] = {
        EGL_SURFACE_TYPE, EGL_WINDOW_BIT, EGL_RENDERABLE_TYPE, EGL_OPENGL_ES3_BIT,  // 指定了渲染类型为 OpenGL ES 3
        EGL_RED_SIZE, 8,    // 指定红色缓冲区的位数是8位
        EGL_GREEN_SIZE, 8,  // 指定绿色缓冲区的位数是8位
        EGL_BLUE_SIZE, 8,   // 指定蓝色缓冲区的位数是8位
        EGL_NONE
};
eglChooseConfig(mEGLDisplay, attribList, &mEGLConfig, 1, &configsNum);
```

在调用eglChooseConfig函数后，系统将根据指定的配置属性attribList返回满足需求的EGL配置，这些配置将存储在mEGLConfig参数中。示例代码中的configsNum参数传入值为1，表明mEGLConfig数组的大小为1，即仅能保存一组可用配置。尽管此设置限制了返回配置的数量，但在大多数应用场景下已能满足基本需求。同时，configsNum参数将实际保存满足指定属性的配置总数，为开发者提供完整的可选配置数量信息。

-

也可以使用eglGetConfigs查询支持的所有配置，并使用eglGetConfigAttrib筛选需要的配置。

以下提供使用此种方法得到满足需求的配置，具体可见示例：

```ets
#include <EGL/egl.h>
#include <iostream>
#include <vector>
int main() {
    // 初始化 EGL
    EGLDisplay display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
    eglInitialize(display, nullptr, nullptr);

    // 获取所有配置
    EGLint numConfigs;
    eglGetConfigs(display, nullptr, 0, &numConfigs);
    std::vector<EGLConfig> configs(numConfigs);
    eglGetConfigs(display, configs.data(), numConfigs, &numConfigs);

    // 选择合适的配置
    EGLConfig chosenConfig = nullptr;
    for (const auto& config : configs) {
        EGLint redSize, greenSize, blueSize;
        eglGetConfigAttrib(display, config, EGL_RED_SIZE, &redSize);
        eglGetConfigAttrib(display, config, EGL_GREEN_SIZE, &greenSize);
        eglGetConfigAttrib(display, config, EGL_BLUE_SIZE, &blueSize);
        if (redSize == 8 && greenSize == 8 && blueSize == 6) {
            chosenConfig = config;
            break;
        }
    }

    // 如果未选择配置，则打印错误信息并退出
    if (!chosenConfig) {
        std::cerr << "Failed to find a suitable EGL configuration." << std::endl;
        return 1;
    }
    return 0;
}
```

```ets
EGLBoolean eglGetConfigs(EGLDisplay display, // EGL显示连接句柄，标识了要进行配置选择的显示连接。
                         EGLConfig *configs, // 用于保存得到配置的数组
                         EGLint config_size, // configs的数组大小
                         EGLint *num_config);// 得到的EGL所有可用配置数量
```

eglGetConfigs接口有以下两种用法：

  - 当我们传递configs为nullptr时，接口会返回EGL_TRUE，并将得到的EGL所有可用配置数量保存在num_config中，这时即可根据得到的数量初始化configs来保存这些配置了，具体见如上代码。
  - 当传递configs数组接受所有配置时，将得到所有配置并保存在configs，这样即可得到所有的可用配置，接下来可以根据具体需求筛选一组config保存下来。

```ets
// 选择合适的配置
   EGLConfig chosenConfig = nullptr;
       for (const auto& config : configs) {
           EGLint redSize, greenSize, blueSize;
           eglGetConfigAttrib(display, config, EGL_RED_SIZE, &redSize);
           eglGetConfigAttrib(display, config, EGL_GREEN_SIZE, &greenSize);
           eglGetConfigAttrib(display, config, EGL_BLUE_SIZE, &blueSize);
           if (redSize == 8 && greenSize == 8 && blueSize == 6) {
               chosenConfig = config;
               break;
           }
       }
```

如上所示遍历configs每个配置，使用eglGetConfigAttrib查询该配置下特定属性的值，将该值保存在第4个参数中，并判断值是否是自己需要的，如果需要则保存该配置，以待使用。调用成功则返回EGL_TRUE，调用失败则返回EGL_FALSE。 如果返回EGL_FALSE，可以使用eglGetError查询失败的原因，如果返回EGL_BAD ATTRIBUTE则attribute不是有效的属性。

```ets
EGLBoolean eglGetConfigAttrib(EGLDisplay display,     //EGL 显示连接句柄，标识了要进行配置选择的显示连接
                                   EGLConfig config,  //EGLConfig 对象，表示要查询的 EGL 配置
                                   EGLint attribute,  //EGLint 类型的属性标识符，表示要查询的属性
                                   EGLint *value);    //指向 EGLint 类型变量的指针，用于存储查询到的属性值。
```

#### 使用eglCreateWindowSurface创建窗口表面

得到符合渲染需求的EGLConfig之后，可以使用eglCreateWindowSurface创建窗口表面。

```ets
EGLSurface eglCreateWindowSurface(EGLDisplay dpy,             // EGLDisplay对象，表示与窗口表面关联的显示连接。
                                  EGLConfig config,           // EGLConfig对象，表示要创建窗口表面的EGL配置。
                                  EGLNativeWindowType win,    // EGLNativeWindowType类型的参数，表示窗口的句柄或标识符，用于与EGL表面关联。
                                  const EGLint *attrib_list); // 指向EGL属性列表的指针，用于指定窗口表面的属性。是一个以EGL_NONE结尾的整数数组。
```

eglCreateWindowSurface接受的属性attrib_list的值如下所示：

```ets
EGL_RENDER_BUFFER EGL_SINGLE_BUFFER或EGL_BACK_BUFFER
EGL_SINGLE_BUFFER // 表示渲染表面将只有一个渲染缓冲区，在绘制完成后，渲染缓冲区中的内容将直接显示到屏幕上，不会进行双缓冲，可能会出现闪烁或撕裂的现象。
EGL_BACK_BUFFER   // 表示渲染表面将具有双缓冲区，即前缓冲区和后缓冲区。在绘制完成后，渲染缓冲区中的内容首先会绘制到后缓冲区，然后通过交换缓冲区的操作将后缓冲区的内容显示到屏幕上，这样可以避免闪烁和撕裂现象。
// 默认情况下是EGL_BACK_BUFFER，当设置为null，则为默认属性。
```

eglCreateWindowSurface创建窗口表面失败的可能原因如下：

-

EGL_BAD_MATCH：表示窗口属性与提供的 EGLConfig 不匹配。这可能是因为EGLConfig不支持渲染到窗口（即EGL_SURFACE_TYPE 属性没有设置为 EGL_WINDOW_BIT）。

-

EGL_BAD_CONFIG：如果提供的EGLConfig没有得到系统的支持，则会发生这种错误。

-

EGL_BAD_NATIVE_WINDOW：如果提供的窗口句柄无效，则会发生这种错误。

-

EGL_BAD_ALLOC：如果eglCreateWindowSurface无法为新的EGL窗口分配资源，或者已经有与提供的窗口关联的EGLConfig，则会发生这种错误。

```ets
EGLint attribList[] = { EGL_RENDER_BUFFER, EGL_BACK_BUFFER, EGL_NONE };
EGLSurface surface = eglCreateWindowSurface(display, config, nativeWindow, attribList);
if (surface == EGL_NO_SURFACE) {
    switch (eglGetError()) {
        case EGL_BAD_MATCH:
            // 检查窗口和 EGLConfig 属性以确定兼容性，或者验证 EGLConfig 是否支持渲染到窗口
            break;
        case EGL_BAD_CONFIG:
            // 验证提供的 EGLConfig 是否有效
            break;
        case EGL_BAD_NATIVE_WINDOW:
            // 验证提供的 EGLNativeWindow 是否有效
            break;
        case EGL_BAD_ALLOC:
            // 资源不足；处理并恢复
            break;
        default:
            // 处理任何其他错误
            break;
    }
}
```

在使用XComponent获取nativeWindow的过程中，通常涉及以下步骤：

1. 首先需要在ArkTS 中定义XComponent并设置 XComponentController。XComponent组件用于在UI中嵌入基于OpenGL或Vulkan等图形API实现的渲染内容。

```ets
Column() {
    XComponent({
        id: 'myXComponent',
        type: XComponentType.SURFACE,
        controller: this.xComponentController
    })
}
```

1. 创建 XComponentController子类，实现回调方法：

```ets
class MyXComponentController extends XComponentController {
    onSurfaceCreated(surfaceId: string): void {
        console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
        nativeRender.SetSurfaceId(BigInt(surfaceId));
        // 之后会使用 surfaceId 关联 native window
    }

    onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
        console.info(`onSurfaceChanged surfaceId: ${surfaceId}`);
    }

    onSurfaceDestroyed(surfaceId: string): void {
        console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    }
}
```

1. 使用surfaceId获取NativeWindow：surfaceId是在XComponent创建过程中生成的。在onSurfaceCreated 回调中，可以使用OH_NativeWindow_CreateNativeWindowFromSurfaceId函数通过surfaceId获取nativeWindow。

```ets
napi_value PluginManager::SetSurfaceId(napi_env env, napi_callback_info info)
{
    int64_t surfaceId = ParseId(env, info);
    OHNativeWindow *nativeWindow;
    PluginRender *pluginRender;
    if (windowMap_.find(surfaceId) == windowMap_.end()) {
        OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &nativeWindow);
        windowMap_[surfaceId] = nativeWindow;
    } else {
        return nullptr;
    }
    if (pluginRenderMap_.find(surfaceId) == pluginRenderMap_.end()) {
        pluginRender = new PluginRender(surfaceId);
        pluginRenderMap_[surfaceId] = pluginRender;
    }
    pluginRender->InitNativeWindow(nativeWindow);
    return nullptr;
}
```

#### 使用eglCreateContext创建渲染上下文

eglCreateContext函数用于创建一个新的EGL上下文，并将其与特定的显示设备（display）和配置（config）关联起来。允许指定共享上下文（shareContext），以便与已经存在的OpenGL上下文共享状态信息。该函数的参数说明如下：

```ets
EGLContext eglCreateContext(EGLDisplay display,        // EGLDisplay类型，表示要创建上下文的EGL显示连接。
                            EGLConfig config,          // EGLConfig类型，表示与上下文关联的EGL配置。
                            EGLContext shareContext,   // EGLContext类型，表示要与新创建的上下文共享状态信息的现有上下文。如果不想共享状态信息，可以传递EGL_NO_CONTEXT。
                            const EGLint *attribList); // 指向属性列表的指针，用于指定上下文的属性。属性列表是以EGL_NONE结尾的一系列属性值对。
```

eglCreateContext 的attribList属性列表如下：

```ets
EGLint attrib3_list[] = {
    EGL_CONTEXT_CLIENT_VERSION, 3, //指定使用的openglES版本3相关的上下文类型
    EGL_NONE
};
```

eglCreateContext 创建渲染上下文失败的原因为EGL_BAD_CONFIG，即提供的EGLConfig无效。

#### 使用eglMakeCurrent将EGL上下文与绘图表面进行关联

```ets
EGLBoolean eglMakeCurrent(EGLDisplay display, // EGL显示连接的句柄，用于标识渲染设备。
                          EGLSurface draw,    // EGL绘图表面的句柄，指定要渲染到的目标表面。
                          EGLSurface read,    // EGL读取表面的句柄，用于像素读取等操作。通常情况下，可以将其设为与 draw 相同的值。
                          EGLContext context);// 要与指定表面关联的 EGL 上下文的句柄。
```

#### 创建并使用着色器程序

```ets
// 创建顶点着色器
GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
glShaderSource(vertexShader, 1, &g_vertexShader, nullptr);
glCompileShader(vertexShader);

// 创建片段着色器
GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
glShaderSource(fragmentShader, 1, &g_fragmentShader, nullptr);
glCompileShader(fragmentShader);

// 创建着色器程序
mProgramHandle = glCreateProgram();
glAttachShader(mProgramHandle, vertexShader);
glAttachShader(mProgramHandle, fragmentShader);
glLinkProgram(mProgramHandle);

// 使用着色器程序
glUseProgram(mProgramHandle);
```

```ets
GLuint glCreateShader(GLenum shaderType);
```

glCreateShader用于创建一个指定类型（顶点着色器、片段着色器等）的着色器对象，并返回该对象的句柄。其中shaderType参数指定要创建的着色器类型，可以是GL_VERTEX_SHADER（顶点着色器）或 GL_FRAGMENT_SHADER（片段着色器）等。

```ets
void glShaderSource(GLuint shader, GLsizei count, const GLchar \**string, const GLint *length);
```

glShaderSource函数用于设置着色器对象的源代码。其中各参数含义如下：

- shader：要设置源代码的着色器对象的标识符。
- count：源代码字符串的数量。
- string：指向源代码字符串的指针数组。
- length：指向包含每个源代码字符串长度的整数数组，可以为nullptr，表示每个字符串都以null结尾。

```ets
void glCompileShader(GLuint shader);
```

glCompileShader函数用于编译指定的着色器对象，其中shader参数是要编译的着色器对象的标识符。

```ets
GLuint glCreateProgram(void);
```

glCreateProgram函数用于创建一个新的着色器程序对象，该函数返回一个新创建的着色器程序对象的标识符。

```ets
void glAttachShader(GLuint program, GLuint shader);
```

glAttachShader函数用于将一个着色器对象附加到一个着色器程序对象上，参数program是目标着色器程序对象的标识符，参数shader是要附加的着色器对象的标识符。

```ets
void glLinkProgram(GLuint program);
```

glLinkProgram函数用于链接一个着色器程序对象，将附加到该程序对象的着色器链接成一个可执行的渲染管线。

参数program是要链接的着色器程序对象的标识符。链接着色器程序时，OpenGL将会执行以下操作：将各个着色器对象中的代码合并成一个可执行的渲染管线。执行连接器优化，以优化渲染管线的性能。并将Uniform变量和Uniform块的信息进行绑定。

```ets
void glUseProgram(GLuint program);
```

glUseProgram函数用于激活指定的着色器程序对象。在调用glUseProgram 之后，所有的渲染调用将会使用该着色器程序进行处理。

在使用glCompileShader时可以使用以下代码检查是否正常。

```ets
// 编译着色器
glCompileShader(shader);

// 检查编译状态
glGetShaderiv(shader, GL_COMPILE_STATUS, &compiled);

if (!compiled)
{
    GLint infoLen = 0;
    // 获取着色器信息日志的长度
    glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &infoLen);
    if ( infoLen > 1 )
    {
        // 分配存储信息日志的内存
        char *infoLog = malloc(sizeof(char) * infoLen);
        // 获取并打印着色器信息日志
        glGetShaderInfoLog(shader, infoLen, NULL, infoLog);
        esLogMessage("Error compiling shader:\n%s\n", infoLog);
        // 释放分配的内存
        free(infoLog);
    }
    // 删除编译失败的着色器
    glDeleteShader(shader);
    return 0;
}
```

在使用glLinkProgram可使用如下代码检查是否正常。

```ets
// 链接程序对象
glLinkProgram(programObject);

// 检查链接状态
glGetProgramiv(programObject, GL_LINK_STATUS, &linked);

if (!linked)
{
    GLint infoLen = 0;
    // 获取程序对象信息日志的长度
    glGetProgramiv(programObject, GL_INFO_LOG_LENGTH, &infoLen);
    if (infoLen > 1)
    {
        // 分配存储信息日志的内存
        char *infoLog = malloc(sizeof(char) * infoLen);
        // 获取并打印程序对象的信息日志
        glGetProgramInfoLog(programObject, infoLen, NULL, infoLog);
        esLogMessage("Error linking program:\n%s\n", infoLog);
        // 释放分配的内存
        free(infoLog);
    }
    // 删除链接失败的程序对象
    glDeleteProgram(programObject);
    return FALSE;
}
```

#### 使用glViewport设置视口大小

```ets
void glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
```

glViewport函数用于设置视口，指定OpenGL ES渲染区域在窗口的位置和大小。其中x、y指定视口的左下角在窗口中的坐标，width、height参数则指定视口的宽度和高度。

#### 使用glClearColor设置清除颜色缓冲区时使用的颜色

```ets
void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
```

glClearColor(1.0f, 1.0f, 1.0f, 1.0f)此时设置清除颜色缓冲区时使用的颜色为 (1.0, 1.0, 1.0)，即红色分量为1.0、绿色分量为1.0、蓝色分量为1.0、透明度为1.0（不透明）。

#### 使用glClear执行清除操作

```ets
void glClear(GLbitfield mask);
```

glClear函数用于清除指定的缓冲区。参数mask指定需要清除的缓冲区，可以是以下值的组合：

- GL_COLOR_BUFFER_BIT：清除颜色缓冲区。
- GL_DEPTH_BUFFER_BIT：清除深度缓冲区。
- GL_STENCIL_BUFFER_BIT：清除模板缓冲区。

可调用glClear(GL_COLOR_BUFFER_BIT)清除颜色缓冲区，并用之前glClearColor设置的颜色填充整个缓冲区。清除颜色缓冲区是在开始绘制新帧之前的一个常见操作，这可以确保屏幕上的每个像素都被初始化为指定的颜色值，以便绘制新的图像。也是绘制新帧的准备工作，类似于在画布上涂上底色，以便开始新的绘画。

#### 使用glGetAttribLocation获取属性变量位置

```ets
GLint glGetAttribLocation(GLuint program, const GLchar *name);
```

glGetAttribLocation函数用于获取顶点着色器中某个属性的位置，这个位置在编译链接顶点着色器程序后就已经确定了，它是根据属性的名称来确定的。其中program指要查询的程序对象，name指要查询其位置的属性变量的名称。

#### 使用glGetUniformLocation获取统一变量位置

```ets
GLint glGetUniformLocation(GLuint program, const GLchar *name);
```

glGetUniformLocation函数用于查询特定统一变量在程序对象中的位置。其中program指要查询的程序对象，name指要查询其位置的统一变量的名称。

#### 使用glUniformMatrix4fv传递4×4矩阵

```ets
void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
```

glGetUniformLocation函数用于获取着色器中uniform变量的位置。其中各个参数含义如下：

- location：要修改的uniform变量的位置。
- count：要修改的矩阵的数量。如果目标uniform变量不是数组，则此值应为1；如果是数组，则应大于等于1。
- transpose：是否转置矩阵。如果是GL_FALSE，则矩阵按列优先(column major)顺序传递；如果是GL_TRUE，则矩阵按行优先(row major)顺序传递。
- value：由count个元素组成的数组的指针，这些元素将用于更新指定的uniform变量。

#### 使用glUniform3f向着色器传递颜色和方向

```ets
void glUniform3f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2);
```

glUniform3f函数为当前程序对象指定Uniform变量的值。其中location指明要更改的变量位置，v0、v1、v2表示变量中要使用的新值。

#### 创建缓冲区并上传数据到GPU

```ets
GLuint buffer;
glGenBuffers(1, &buffer);                                                  // 生成一个缓冲区对象
glBindBuffer(GL_ARRAY_BUFFER, buffer);                                     // 绑定缓冲区，将缓冲区设置为当前操作的缓冲区
glBufferData(GL_ARRAY_BUFFER, len, data, GL_STATIC_DRAW);                  // 上传数据到GPU
glVertexAttribPointer(index, TRIANGLES_POINT, GL_FLOAT, GL_FALSE, 0, 0);   // 设置顶点属性指针
glEnableVertexAttribArray(index);                                          // 启用顶点属性数组
```

```ets
void glBindBuffer(GLenum target,   // target：指定要绑定的缓冲目标,可为以下值之一：
                                   // GL_ARRAY_BUFFER：用于存储顶点属性数据；
                                   // GL_ELEMENT_ARRAY_BUFFER：用于存储索引数据等其他。
                  GLuint buffer);  // buffer为要绑定的顶点缓冲对象的名称。
```

```ets
void glBufferData(GLenum target,       // target：指定缓冲对象的类型，可为以下值之一：
                                       // GL_ARRAY_BUFFER：用于存储顶点属性数据;
                                       // GL_ELEMENT_ARRAY_BUFFER：用于存储索引数据。
                  GLsizeiptr size,     // 指定要分配的缓冲区的大小（以字节为单位）。
                  const GLvoid* data,  // 指定要复制到缓冲区的初始数据。
                  GLenum usage);       // 指定缓冲区的预期使用方式，可为以下值之一：
                                       // GL_STATIC_DRAW：数据不会或几乎不会被修改，并且被绘制命令多次使用；
                                       // GL_DYNAMIC_DRAW：数据会被频繁修改，并且被绘制命令多次使用；
                                       // GL_STREAM_DRAW：数据会被修改，并且被绘制命令少量使用。
```

一旦调用glBufferData函数，数据就被复制到了OpenGL的缓冲对象中，并存储在GPU的显存中。这意味着数据可以在GPU上被高效地访问和处理，而无需频繁地从CPU内存传输数据，从而提高了渲染性能。

```ets
void glVertexAttribPointer(GLuint index,         // 指定要修改的顶点数组的起始索引，索引它与顶点着色器中的属性变量绑定。（layout (location = 0) in vec3 aPos;）
                           GLint size,           // 指定每个顶点属性的分量个数
                           GLenum type,          // 指定每个顶点属性分量的类型
                           GLboolean normalized, // 指定在访问顶点数据时是否将其映射到[0, 1]或[-1, 1]范围内
                           GLsizei stride,       // 指定顶点属性之间的偏移量,如果是精密性排列可以设置为0
                           const void *offset);  //属性在缓冲区中的偏移量，允许在缓冲区中指定一个位置开始读取数据。
```

```ets
void glEnableVertexAttribArray(GLuint index);
```

glEnableVertexAttribArray函数用于启用指定索引的顶点属性数组。例如，调用glEnableVertexAttribArray(0)可以启用位置索引为0的顶点属性数组。

#### 启用功能

```ets
void glEnable(GLenum cap);
```

glEnable函数用于启用各种功能，具体功能由参数cap决定，cap可为以下值：

- GL_BLEND：启用颜色混合，例如实现半透明效果。
- GL_DEPTH_TEST：启用深度测试，根据坐标的远近自动隐藏被遮住的图形。
- GL_CULL_FACE：根据多边形在窗口坐标中的缠绕来剔除多边形。

#### 绘制图元并显示

```ets
void glDrawArrays(GLenum mode,   // 参数指定要绘制的图元的类型，比如GL_TRIANGLES表示绘制三角形。
                  GLint first,   // 参数指定要绘制的顶点数组的起始索引。
                  GLsizei count  // 参数指定要绘制的顶点数量
                  );
```

glDrawArrays函数用于根据当前绑定的顶点数组和顶点属性以及其他设置来绘制图元。

```ets
EGLBoolean eglSwapBuffers(EGLDisplay dpy,      // EGL显示连接
                          EGLSurface surface); // 要交换其缓冲区的EGL表面
```

eglSwapBuffers函数用于交换前后缓冲区的内容，并将渲染结果显示在屏幕上。

#### 示例代码

- [基于OpenGL图形库实现绘制三棱锥功能](https://gitcode.com/HarmonyOS_Samples/ndk-opengl)