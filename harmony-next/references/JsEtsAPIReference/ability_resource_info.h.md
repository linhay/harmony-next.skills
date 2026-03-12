# ability_resource_info.h

#### 概述

提供组件资源信息的接口，用于获取组件的以下信息：包名、模块名、组件名、图标、分身索引、是否为默认应用等。

**引用文件：** <bundle/ability_resource_info.h>

**库：** libbundle_ndk.z.so

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 21

**相关模块：**[Native_Bundle](Native_Bundle.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_NativeBundle_AbilityResourceInfo](OH_NativeBundle_AbilityResourceInfo.md)OH_NativeBundle_AbilityResourceInfo表示组件资源信息。

#### 函数

名称描述[BundleManager_ErrorCode OH_NativeBundle_GetBundleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** bundleName)](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_getbundlename)获取组件的包名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。[BundleManager_ErrorCode OH_NativeBundle_GetModuleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** moduleName)](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_getmodulename)获取组件的模块名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。[BundleManager_ErrorCode OH_NativeBundle_GetAbilityName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** abilityName)](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_getabilityname)获取组件名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。[BundleManager_ErrorCode OH_NativeBundle_GetDrawableDescriptor(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, ArkUI_DrawableDescriptor** drawableIcon)](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_getdrawabledescriptor)获取组件图标资源对应的[DrawableDescriptor](zh-cn_topic_0000002497605090.html)对象。在使用该接口之后，为了防止内存泄漏，需要手动调用[OH_AbilityResourceInfo_Destroy](#ZH-CN_TOPIC_0000002529444627__oh_abilityresourceinfo_destroy)释放接口返回的指针。[BundleManager_ErrorCode OH_NativeBundle_GetLabel(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** label)](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_getlabel)获取组件的应用名称。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。[BundleManager_ErrorCode OH_NativeBundle_GetAppIndex(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, int* appIndex)](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_getappindex)获取组件的分身索引。[BundleManager_ErrorCode OH_NativeBundle_CheckDefaultApp(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, bool* isDefault)](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_checkdefaultapp)查询组件所属的应用是否为默认应用。[BundleManager_ErrorCode OH_AbilityResourceInfo_Destroy(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, size_t count)](#ZH-CN_TOPIC_0000002529444627__oh_abilityresourceinfo_destroy)该接口应在对[OH_NativeBundle_GetAbilityResourceInfo](zh-cn_topic_0000002497604660.html#ZH-CN_TOPIC_0000002497604660__oh_nativebundle_getabilityresourceinfo)的使用完成后调用，以避免内存泄漏。[int OH_NativeBundle_GetSize()](#ZH-CN_TOPIC_0000002529444627__oh_nativebundle_getsize)获取单个结构体[OH_NativeBundle_AbilityResourceInfo](zh-cn_topic_0000002529284661.html)的大小。

#### 函数说明

#### OH_NativeBundle_GetBundleName()

```ets
BundleManager_ErrorCode OH_NativeBundle_GetBundleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** bundleName)
```

**描述**

获取组件的包名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo指定组件资源信息。char** bundleName获取的包名。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果获取成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果获取失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_NativeBundle_GetModuleName()

```ets
BundleManager_ErrorCode OH_NativeBundle_GetModuleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** moduleName)
```

**描述**

获取组件的模块名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo指定组件资源信息。char** moduleName获取的模块名。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果获取成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果获取失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_NativeBundle_GetAbilityName()

```ets
BundleManager_ErrorCode OH_NativeBundle_GetAbilityName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** abilityName)
```

**描述**

获取组件名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo指定组件资源信息。char** abilityName获取的组件名。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果获取成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果获取失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_NativeBundle_GetDrawableDescriptor()

```ets
BundleManager_ErrorCode OH_NativeBundle_GetDrawableDescriptor(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, ArkUI_DrawableDescriptor** drawableIcon)
```

**描述**

获取组件图标资源对应的[DrawableDescriptor](ArkUI_DrawableDescriptor.md)对象。在使用该接口之后，为了防止内存泄漏，需要手动调用[OH_AbilityResourceInfo_Destroy](#ZH-CN_TOPIC_0000002529444627__oh_abilityresourceinfo_destroy)释放接口返回的指针。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo指定组件资源信息。ArkUI_DrawableDescriptor** drawableIcon组件图标资源对应的[DrawableDescriptor](ArkUI_DrawableDescriptor.md)对象。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果获取成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果获取失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_NativeBundle_GetLabel()

```ets
BundleManager_ErrorCode OH_NativeBundle_GetLabel(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** label)
```

**描述**

获取组件的应用名称。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo指定组件资源信息。char** label获取的应用名称。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果获取成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果获取失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_NativeBundle_GetAppIndex()

```ets
BundleManager_ErrorCode OH_NativeBundle_GetAppIndex(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, int* appIndex)
```

**描述**

获取组件的分身索引。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo指定组件资源信息。int* appIndex获取的分身索引。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果获取成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果获取失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_NativeBundle_CheckDefaultApp()

```ets
BundleManager_ErrorCode OH_NativeBundle_CheckDefaultApp(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, bool* isDefault)
```

**描述**

查询组件所属的应用是否为默认应用。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo指定组件资源信息。bool* isDefault组件所属的应用是否为默认应用，默认应用是指用户为特定文件类型或操作设定的首选应用。取值true为默认应用，false为非默认应用。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果查询成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果查询失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_AbilityResourceInfo_Destroy()

```ets
BundleManager_ErrorCode OH_AbilityResourceInfo_Destroy(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, size_t count)
```

**描述**

释放组件资源信息的内存。

**起始版本：** 21

**参数：**

参数项描述OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo要释放的组件资源信息。size_t count表示组件资源信息数组的大小。

**返回：**

类型说明[BundleManager_ErrorCode](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)

执行结果。

 如果释放成功，返回[BUNDLE_MANAGER_ERROR_CODE_NO_ERROR](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)。

 如果释放失败，返回[BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID](bundle_manager_common.h.md#ZH-CN_TOPIC_0000002497604662__bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。

#### OH_NativeBundle_GetSize()

```ets
int OH_NativeBundle_GetSize()
```

**描述**

获取单个结构体[OH_NativeBundle_AbilityResourceInfo](OH_NativeBundle_AbilityResourceInfo.md)的大小。

**起始版本：** 21

**返回：**

类型说明int返回单个结构体[OH_NativeBundle_AbilityResourceInfo](OH_NativeBundle_AbilityResourceInfo.md)的大小。