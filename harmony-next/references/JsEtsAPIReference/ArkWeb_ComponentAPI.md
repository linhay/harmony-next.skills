# ArkWeb_ComponentAPI

```ets
typedef struct {...} ArkWeb_ComponentAPI
```

#### 概述

Component相关的Native API结构体。

**起始版本：** 12

**相关模块：**[Web](Web.md)

**所在头文件：**[arkweb_type.h](arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述size_t size结构体的大小。

#### 成员函数

名称描述[void (*onControllerAttached)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)](#ZH-CN_TOPIC_0000002497605234__oncontrollerattached)当Controller成功绑定到Web组件时触发该回调。[void (*onPageBegin)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)](#ZH-CN_TOPIC_0000002497605234__onpagebegin)网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。[void (*onPageEnd)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)](#ZH-CN_TOPIC_0000002497605234__onpageend)网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。[void (*onDestroy)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)](#ZH-CN_TOPIC_0000002497605234__ondestroy)当前Web组件销毁时触发该回调。

#### 成员函数说明

#### onControllerAttached()

```ets
void (*onControllerAttached)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

当Controller成功绑定到Web组件时触发该回调。

**参数：**

参数项描述const char* webTagWeb组件名称。ArkWeb_OnComponentCallback callbackonControllerAttached的回调函数。void* userData用户自定义数据。

#### onPageBegin()

```ets
void (*onPageBegin)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**参数：**

参数项描述const char* webTagWeb组件名称。ArkWeb_OnComponentCallback callbackonPageBegin的回调函数。void* userData用户自定义数据。

#### onPageEnd()

```ets
void (*onPageEnd)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**参数：**

参数项描述const char* webTagWeb组件名称。ArkWeb_OnComponentCallback callbackonPageEnd的回调函数。void* userData用户自定义数据。

#### onDestroy()

```ets
void (*onDestroy)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

当前Web组件销毁时触发该回调。

**参数：**

参数项描述const char* webTagWeb组件名称。ArkWeb_OnComponentCallback callbackonDestroy的回调函数。void* userData用户自定义数据。