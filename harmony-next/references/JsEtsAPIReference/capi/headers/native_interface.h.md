# native_interface.h

#### 概述

提供NativeModule接口的统一入口函数。

**引用文件：** <arkui/native_interface.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](../../topics/system-services/ArkUI_NativeModule.md)

#### 汇总

#### 枚举

名称typedef关键字描述[ArkUI_NativeAPIVariantKind](#ZH-CN_TOPIC_0000002497445098__arkui_nativeapivariantkind)ArkUI_NativeAPIVariantKind定义Native接口集合类型。

#### 函数

名称描述[void* OH_ArkUI_QueryModuleInterfaceByName(ArkUI_NativeAPIVariantKind type, const char* structName)](#ZH-CN_TOPIC_0000002497445098__oh_arkui_querymoduleinterfacebyname)需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。

#### 宏定义

名称描述[OH_ArkUI_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)](#ZH-CN_TOPIC_0000002497445098__oh_arkui_getmoduleinterface)基于结构体类型获取对应结构体指针的宏函数。

#### 枚举类型说明

#### ArkUI_NativeAPIVariantKind

```ets
enum ArkUI_NativeAPIVariantKind
```

**描述：**

定义Native接口集合类型。

**起始版本：** 12

枚举项描述ARKUI_NATIVE_NODEUI组件相关接口类型，详见[native_node.h](native_node.h.md)中的[结构体](native_node.h.md#ZH-CN_TOPIC_0000002529285071__结构体)类型定义。ARKUI_NATIVE_DIALOG弹窗相关接口类型，详见[native_dialog.h](native_dialog.h.md)中的[结构体](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__结构体)类型定义。ARKUI_NATIVE_GESTURE手势相关接口类型，详见[native_gesture.h](native_gesture.h.md)中的[结构体](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__结构体)类型定义。ARKUI_NATIVE_ANIMATE动画相关接口类型。详见[native_animate.h](native_animate.h.md)中的[结构体](native_animate.h.md#ZH-CN_TOPIC_0000002529285067__结构体)类型定义。ARKUI_MULTI_THREAD_NATIVE_NODE

多线程UI组件相关接口类型，详见[native_node.h](native_node.h.md)中的[结构体](native_node.h.md#ZH-CN_TOPIC_0000002529285071__结构体)类型定义。

**起始版本：** 22

#### 函数说明

#### OH_ArkUI_QueryModuleInterfaceByName()

```ets
void* OH_ArkUI_QueryModuleInterfaceByName(ArkUI_NativeAPIVariantKind type, const char* structName)
```

**描述：**

需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_NativeAPIVariantKind](native_interface.h.md#ZH-CN_TOPIC_0000002497445098__arkui_nativeapivariantkind) typeArkUI提供的native接口集合大类，例如UI组件接口类：ARKUI_NATIVE_NODE, 手势类：ARKUI_NATIVE_GESTURE。const char* structNamenative接口结构体的名称，通过查询对应头文件内结构体定义，例如位于[native_node.h](native_node.h.md)中的"ArkUI_NativeNodeAPI_1"。

**返回：**

类型说明void*返回native接口抽象指针，在转化为具体类型后进行使用。

#### OH_ArkUI_GetModuleInterface()

```ets
OH_ArkUI_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)                             \
do {                                                                                                 \
        void* anyNativeAPI = OH_ArkUI_QueryModuleInterfaceByName(nativeAPIVariantKind, #structType); \
        if (anyNativeAPI) {                                                                          \
            structPtr = (structType*)(anyNativeAPI);                                                 \
        }                                                                                            \
    } while (0)
```

**描述：**

基于结构体类型获取对应结构体指针的宏函数。此宏函数接收[ArkUI_NativeAPIVariantKind](native_interface.h.md#ZH-CN_TOPIC_0000002497445098__arkui_nativeapivariantkind)类型枚举参数nativeAPIVariantKind、const char*类型参数structType、structType*类型参数structPtr，调用[OH_ArkUI_QueryModuleInterfaceByName](#ZH-CN_TOPIC_0000002497445098__oh_arkui_querymoduleinterfacebyname)获取native接口抽象指针，转换为structType*类型后赋值给structPtr。

**起始版本：** 12