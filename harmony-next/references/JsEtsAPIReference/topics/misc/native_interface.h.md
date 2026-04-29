# native_interface.h

**概述**

提供NativeModule接口的统一入口函数。

引用文件： <arkui/native_interface.h>

库： libace_ndk.z.so

系统能力： SystemCapability.ArkUI.ArkUI.Full

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

相关示例： [NativeNodeInterfaceSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/NativeNodeInterfaceSample)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_NativeAPIVariantKind | ArkUI_NativeAPIVariantKind | 定义Native接口集合类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| void* OH_ArkUI_QueryModuleInterfaceByName(ArkUI_NativeAPIVariantKind type, const char* structName) | 需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| OH_ArkUI_GetModuleInterface(nativeAPIVariantKind, structType, structPtr) | 基于结构体类型获取对应结构体指针的宏函数。 |

**枚举类型说明**

**ArkUI_NativeAPIVariantKind**

```ets
enum ArkUI_NativeAPIVariantKind
```

描述：

定义Native接口集合类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_NATIVE_NODE = 0 | UI组件相关接口类型，详见native_node.h中的结构体类型定义。 |
| ARKUI_NATIVE_DIALOG = 1 | 弹窗相关接口类型，详见native_dialog.h中的结构体类型定义。 |
| ARKUI_NATIVE_GESTURE = 2 | 手势相关接口类型，详见native_gesture.h中的结构体类型定义。 |
| ARKUI_NATIVE_ANIMATE = 3 | 动画相关接口类型。详见native_animate.h中的结构体类型定义。 |
| ARKUI_MULTI_THREAD_NATIVE_NODE = 4 | 多线程UI组件相关接口类型，详见native_node.h中的结构体类型定义。 起始版本： 22 |

**函数说明**

**OH_ArkUI_QueryModuleInterfaceByName()**

```ets
void* OH_ArkUI_QueryModuleInterfaceByName(ArkUI_NativeAPIVariantKind type, const char* structName)
```

描述：

需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeAPIVariantKind type | ArkUI提供的native接口集合大类，例如UI组件接口类：ARKUI_NATIVE_NODE, 手势类：ARKUI_NATIVE_GESTURE。 |
| const char* structName | native接口结构体的名称，通过查询对应头文件内结构体定义，例如位于native_node.h中的"ArkUI_NativeNodeAPI_1"。 |

返回：

| 类型 | 说明 |
| --- | --- |
| void* | 返回native接口抽象指针，在转换为具体类型后进行使用。 |

**OH_ArkUI_GetModuleInterface()**

```ets
OH_ArkUI_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)                             \
do {                                                                                                 \
        void* anyNativeAPI = OH_ArkUI_QueryModuleInterfaceByName(nativeAPIVariantKind, #structType); \
        if (anyNativeAPI) {                                                                          \
            structPtr = (structType*)(anyNativeAPI);                                                 \
        }                                                                                            \
    } while (0)
```

描述：

基于结构体类型获取对应结构体指针的宏函数。此宏函数接收[ArkUI_NativeAPIVariantKind](native_interface.h.md#ZH-CN_TOPIC_0000002553200991__arkui_nativeapivariantkind)类型枚举参数nativeAPIVariantKind、const char*类型参数structType、structType*类型参数structPtr，调用[OH_ArkUI_QueryModuleInterfaceByName](#ZH-CN_TOPIC_0000002553200991__oh_arkui_querymoduleinterfacebyname)获取native接口抽象指针，转换为structType*类型后赋值给structPtr。

起始版本： 12