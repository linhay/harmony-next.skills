# ability_resource_info.h

**概述**

提供组件资源信息的接口，用于获取组件的以下信息：包名、模块名、组件名、图标、分身索引、是否为默认应用等。

引用文件： <bundle/ability_resource_info.h>

库： libbundle_ndk.z.so

系统能力： SystemCapability.BundleManager.BundleFramework.Core

起始版本： 21

相关模块： [Native_Bundle](Native_Bundle.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_NativeBundle_AbilityResourceInfo | OH_NativeBundle_AbilityResourceInfo | 表示组件资源信息。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| BundleManager_ErrorCode OH_NativeBundle_GetBundleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** bundleName) | 获取组件的包名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| BundleManager_ErrorCode OH_NativeBundle_GetModuleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** moduleName) | 获取组件的模块名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| BundleManager_ErrorCode OH_NativeBundle_GetAbilityName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** abilityName) | 获取组件名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| BundleManager_ErrorCode OH_NativeBundle_GetDrawableDescriptor(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, ArkUI_DrawableDescriptor** drawableIcon) | 获取组件图标资源对应的DrawableDescriptor对象。在使用该接口之后，为了防止内存泄漏，需要手动调用OH_AbilityResourceInfo_Destroy释放接口返回的指针。 |
| BundleManager_ErrorCode OH_NativeBundle_GetLabel(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** label) | 获取组件的应用名称。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| BundleManager_ErrorCode OH_NativeBundle_GetAppIndex(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, int* appIndex) | 获取组件的分身索引。 |
| BundleManager_ErrorCode OH_NativeBundle_CheckDefaultApp(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, bool* isDefault) | 查询组件所属的应用是否为默认应用。 |
| BundleManager_ErrorCode OH_AbilityResourceInfo_Destroy(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, size_t count) | 该接口应在对OH_NativeBundle_GetAbilityResourceInfo的使用完成后调用，以避免内存泄漏。 |
| int OH_NativeBundle_GetSize() | 获取单个结构体OH_NativeBundle_AbilityResourceInfo的大小。 |

**函数说明**

**OH_NativeBundle_GetBundleName()**

```ets
BundleManager_ErrorCode OH_NativeBundle_GetBundleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** bundleName)
```

描述

获取组件的包名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 指定组件资源信息。 |
| char** bundleName | 获取的包名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果获取成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果获取失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_NativeBundle_GetModuleName()**

```ets
BundleManager_ErrorCode OH_NativeBundle_GetModuleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** moduleName)
```

描述

获取组件的模块名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 指定组件资源信息。 |
| char** moduleName | 获取的模块名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果获取成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果获取失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_NativeBundle_GetAbilityName()**

```ets
BundleManager_ErrorCode OH_NativeBundle_GetAbilityName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** abilityName)
```

描述

获取组件名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 指定组件资源信息。 |
| char** abilityName | 获取的组件名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果获取成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果获取失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_NativeBundle_GetDrawableDescriptor()**

```ets
BundleManager_ErrorCode OH_NativeBundle_GetDrawableDescriptor(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, ArkUI_DrawableDescriptor** drawableIcon)
```

描述

获取组件图标资源对应的[DrawableDescriptor](ArkUI_DrawableDescriptor.md)对象。在使用该接口之后，为了防止内存泄漏，需要手动调用[OH_AbilityResourceInfo_Destroy](#ZH-CN_TOPIC_0000002553200573__oh_abilityresourceinfo_destroy)释放接口返回的指针。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 指定组件资源信息。 |
| ArkUI_DrawableDescriptor** drawableIcon | 组件图标资源对应的DrawableDescriptor对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果获取成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果获取失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_NativeBundle_GetLabel()**

```ets
BundleManager_ErrorCode OH_NativeBundle_GetLabel(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** label)
```

描述

获取组件的应用名称。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 指定组件资源信息。 |
| char** label | 获取的应用名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果获取成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果获取失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_NativeBundle_GetAppIndex()**

```ets
BundleManager_ErrorCode OH_NativeBundle_GetAppIndex(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, int* appIndex)
```

描述

获取组件的分身索引。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 指定组件资源信息。 |
| int* appIndex | 获取的分身索引。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果获取成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果获取失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_NativeBundle_CheckDefaultApp()**

```ets
BundleManager_ErrorCode OH_NativeBundle_CheckDefaultApp(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, bool* isDefault)
```

描述

查询组件所属的应用是否为默认应用。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 指定组件资源信息。 |
| bool* isDefault | 组件所属的应用是否为默认应用，默认应用是指用户为特定文件类型或操作设定的首选应用。取值true为默认应用，false为非默认应用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果查询成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果查询失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_AbilityResourceInfo_Destroy()**

```ets
BundleManager_ErrorCode OH_AbilityResourceInfo_Destroy(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, size_t count)
```

描述

释放组件资源信息的内存。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo | 要释放的组件资源信息。 |
| size_t count | 表示组件资源信息数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| BundleManager_ErrorCode | 执行结果。  如果释放成功，返回BUNDLE_MANAGER_ERROR_CODE_NO_ERROR。  如果释放失败，返回BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID，这是由于abilityResourceInfo为空指针所致。 |

**OH_NativeBundle_GetSize()**

```ets
int OH_NativeBundle_GetSize()
```

描述

获取单个结构体[OH_NativeBundle_AbilityResourceInfo](OH_NativeBundle_AbilityResourceInfo.md)的大小。

起始版本： 21

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回单个结构体OH_NativeBundle_AbilityResourceInfo的大小。 |