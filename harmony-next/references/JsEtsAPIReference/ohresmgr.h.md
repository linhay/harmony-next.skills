# ohresmgr.h

#### 概述

提供资源管理native侧获取资源的能力。

**引用文件：** <resourcemanager/ohresmgr.h>

**库：** libohresmgr.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**相关模块：**[resourcemanager](resourcemanager.md)

#### 汇总

#### 函数

名称描述[ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density = 0)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmediabase64)通过指定资源ID，获取屏幕密度对应的media资源的Base64码。[ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64Data(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmediabase64data)通过指定资源ID，获取屏幕密度对应的media资源的Base64码。[ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64ByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density = 0)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmediabase64byname)通过指定资源名称，获取屏幕密度对应的media资源的Base64码。[ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64DataByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmediabase64databyname)通过指定资源名称，获取屏幕密度对应的media资源的Base64码。[ResourceManager_ErrorCode OH_ResourceManager_GetMedia(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmedia)通过指定资源ID，获取屏幕密度对应的media资源的内容。[ResourceManager_ErrorCode OH_ResourceManager_GetMediaData(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmediadata)通过指定资源ID，获取屏幕密度对应的media资源的内容。[ResourceManager_ErrorCode OH_ResourceManager_GetMediaByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmediabyname)通过指定资源名称，获取屏幕密度对应的media资源的内容。[ResourceManager_ErrorCode OH_ResourceManager_GetMediaDataByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getmediadatabyname)通过指定资源名称，获取屏幕密度对应的media资源的内容。[ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptor(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getdrawabledescriptor)通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。[ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorData(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getdrawabledescriptordata)通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。[ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getdrawabledescriptorbyname)通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。[ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorDataByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getdrawabledescriptordatabyname)通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。[ResourceManager_ErrorCode OH_ResourceManager_GetSymbol(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getsymbol)通过指定资源ID，获取对应的symbol资源。[ResourceManager_ErrorCode OH_ResourceManager_GetSymbolByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getsymbolbyname)通过指定资源名称，获取对应的symbol资源。[ResourceManager_ErrorCode OH_ResourceManager_GetLocales(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem = false)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getlocales)获取语言列表。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()方法来释放localinfo的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetLocalesData(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getlocalesdata)获取语言列表。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()方法来释放localinfo的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getconfiguration)获取设备配置。使用此接口后，需要调用[OH_ResourceManager_ReleaseConfiguration](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager_Configuration对象，还需要调用free()方法来释放它。(API20废弃)[ResourceManager_ErrorCode OH_ResourceManager_GetResourceConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getresourceconfiguration)获取设备配置。使用此接口后，需要调用[OH_ResourceManager_ReleaseConfiguration](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager_Configuration对象，还需要调用free()方法来释放它。[ResourceManager_ErrorCode OH_ResourceManager_ReleaseConfiguration(ResourceManager_Configuration *configuration)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_releaseconfiguration)释放[OH_ResourceManager_GetConfiguration](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getconfiguration)和[OH_ResourceManager_GetResourceConfiguration](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getresourceconfiguration)方法申请的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetString(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, ...)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getstring)通过指定资源ID，获取对应的string资源。获取普通string资源使用OH_ResourceManager_GetString(mgr, resId, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH_ResourceManager_GetString(mgr, resId, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetStringByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, ...)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getstringbyname)通过指定资源名称，获取对应的string资源。获取普通string资源使用OH_ResourceManager_GetString(mgr, resName, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH_ResourceManager_GetString(mgr, resName, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetStringArray(const NativeResourceManager *mgr, uint32_t resId, char ***resultValue, uint32_t *resultLen)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getstringarray)通过指定资源ID，获取字符串数组。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()接口来释放字符串数组内存。[ResourceManager_ErrorCode OH_ResourceManager_GetStringArrayByName(const NativeResourceManager *mgr, const char *resName, char ***resultValue, uint32_t *resultLen)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getstringarraybyname)通过指定资源名称，获取字符串数组。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()接口来释放字符串数组内存。[ResourceManager_ErrorCode OH_ResourceManager_ReleaseStringArray(char ***resValue, uint32_t len)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_releasestringarray)释放字符串数组内存。[ResourceManager_ErrorCode OH_ResourceManager_GetPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getpluralstring)通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。(API18废弃)[ResourceManager_ErrorCode OH_ResourceManager_GetPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getpluralstringbyname)通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。(API18废弃)[ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue, ...)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getintpluralstring)通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralString(const NativeResourceManager *mgr, uint32_t resId, double num, char **resultValue, ...)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getdoublepluralstring)通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue, ...)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getintpluralstringbyname)通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralStringByName(const NativeResourceManager *mgr, const char *resName, double num, char **resultValue, ...)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getdoublepluralstringbyname)通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。[ResourceManager_ErrorCode OH_ResourceManager_GetColor(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getcolor)通过指定资源ID，获取对应的颜色值。[ResourceManager_ErrorCode OH_ResourceManager_GetColorByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getcolorbyname)通过指定资源ID，获取对应的颜色值。[ResourceManager_ErrorCode OH_ResourceManager_GetInt(const NativeResourceManager *mgr, uint32_t resId, int *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getint)通过指定资源ID，获取对应的int值。[ResourceManager_ErrorCode OH_ResourceManager_GetIntByName(const NativeResourceManager *mgr, const char *resName, int *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getintbyname)通过指定资源名称，获取对应的int值。[ResourceManager_ErrorCode OH_ResourceManager_GetFloat(const NativeResourceManager *mgr, uint32_t resId, float *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getfloat)通过指定资源ID，获取对应的float值。[ResourceManager_ErrorCode OH_ResourceManager_GetFloatByName(const NativeResourceManager *mgr, const char *resName, float *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getfloatbyname)通过指定资源名称，获取对应的float值。[ResourceManager_ErrorCode OH_ResourceManager_GetBool(const NativeResourceManager *mgr, uint32_t resId, bool *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getbool)通过指定资源ID，获取对应的bool值。[ResourceManager_ErrorCode OH_ResourceManager_GetBoolByName(const NativeResourceManager *mgr, const char *resName, bool *resultValue)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getboolbyname)通过指定资源名称，获取对应的bool值。[ResourceManager_ErrorCode OH_ResourceManager_AddResource(const NativeResourceManager *mgr, const char *path)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_addresource)在应用程序运行时添加overlay资源。[ResourceManager_ErrorCode OH_ResourceManager_RemoveResource(const NativeResourceManager *mgr, const char *path)](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_removeresource)在应用程序运行时删除overlay资源。

#### 函数说明

#### OH_ResourceManager_GetMediaBase64()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，默认值为0，表示使用当前系统dpi的密度。char **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetMediaBase64Data()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64Data(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。char **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetMediaBase64ByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64ByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。char **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，默认值为0，表示使用当前系统dpi的密度。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_NAME_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetMediaBase64DataByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64DataByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。char **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_NAME_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetMedia()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMedia(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，默认值为0，表示使用当前系统dpi的密度。uint8_t **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetMediaData()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMediaData(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。uint8_t **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetMediaByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMediaByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，默认值为0，表示使用当前系统dpi的密度。uint8_t **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_NAME_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetMediaDataByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetMediaDataByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。uint8_t **resultValue写入resultValue的结果。uint64_t *resultLen写入resultLen的media长度。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_NAME_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetDrawableDescriptor()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptor(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)
```

**描述**

通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t资源ID。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，默认值为0，表示使用当前系统dpi的密度。uint32_t type可选参数，表示图标类型，0表示自身图标，1表示主题图标。[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md) **drawableDescriptor写入drawableDescriptor的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

#### OH_ResourceManager_GetDrawableDescriptorData()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorData(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)
```

**描述**

通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md) **drawableDescriptor写入drawableDescriptor的结果。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。uint32_t type可选参数，表示图标类型，0表示自身图标，1表示主题图标。如果该属性不是必需的，请将该参数设为0。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

#### OH_ResourceManager_GetDrawableDescriptorByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)
```

**描述**

通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，默认值为0，表示使用当前系统dpi的密度。uint32_t type可选参数，表示图标类型，0表示自身图标，1表示主题图标，2表示动态图标。[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md) **drawableDescriptor写入drawableDescriptor的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_NAME_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

#### OH_ResourceManager_GetDrawableDescriptorDataByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorDataByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)
```

**描述**

通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。[ArkUI_DrawableDescriptor](ArkUI_DrawableDescriptor.md) **drawableDescriptor写入drawableDescriptor的结果。uint32_t density可选参数，取值范围参考[ScreenDensity](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。uint32_t type可选参数，表示图标类型，0表示自身图标，1表示主题图标。如果该属性不是必需的，请将该参数设为0。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_NAME_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

#### OH_ResourceManager_GetSymbol()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetSymbol(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)
```

**描述**

通过指定资源ID，获取对应的symbol资源。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。uint32_t *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetSymbolByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetSymbolByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)
```

**描述**

通过指定资源名称，获取对应的symbol资源。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。uint32_t *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_NAME_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetLocales()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetLocales(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem = false)
```

**描述**

获取语言列表。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()方法来释放localinfo的内存。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。char ***resultValue写入resultValue的结果。uint32_t *resultLen写入resultLen的locales长度。bool includeSystem是否包含系统资源，默认值为false，当只有系统资源查询locales列表时它不起作用。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetLocalesData()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetLocalesData(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem)
```

**描述**

获取语言列表。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()方法来释放localinfo的内存。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。char ***resultValue写入resultValue的结果。uint32_t *resultLen写入resultLen的locales长度。bool includeSystem是否包含系统资源，如果不需要此属性，请将此参数设置为 false。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetConfiguration()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)
```

**描述**

获取设备配置。使用此接口后，需要调用[OH_ResourceManager_ReleaseConfiguration](ohresmgr.h.md#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager_Configuration对象，还需要调用free()方法来释放它。

**起始版本：** 12

**废弃版本：** 20

**替代接口：**[OH_ResourceManager_GetResourceConfiguration](#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getresourceconfiguration)

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。[ResourceManager_Configuration](ResourceManager_Configuration.md) *configuration写入获取的设备配置。其中configuration.screenDensity的返回值为设备DPI除以160取整后的值。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_SYSTEM_RES_MANAGER_GET_FAILED](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001009 - 无法访问系统资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetResourceConfiguration()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetResourceConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)
```

**描述**

获取设备配置。使用此接口后，需要调用[OH_ResourceManager_ReleaseConfiguration](ohresmgr.h.md#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager_Configuration对象，还需要调用free()方法来释放它。

**起始版本：** 20

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。[ResourceManager_Configuration](ResourceManager_Configuration.md) *configuration写入获取的设备配置。其中configuration.screenDensity的返回值为设备DPI。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_SYSTEM_RES_MANAGER_GET_FAILED](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001009 - 无法访问系统资源。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_ReleaseConfiguration()

```ets
ResourceManager_ErrorCode OH_ResourceManager_ReleaseConfiguration(ResourceManager_Configuration *configuration)
```

**描述**

释放[OH_ResourceManager_GetConfiguration](ohresmgr.h.md#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getconfiguration)和[OH_ResourceManager_GetResourceConfiguration](ohresmgr.h.md#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getresourceconfiguration)方法申请的内存。

**起始版本：** 12

**参数：**

参数项描述[ResourceManager_Configuration](ResourceManager_Configuration.md) *configuration需要释放内存的configuration对象。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

#### OH_ResourceManager_GetString()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetString(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, ...)
```

**描述**

通过指定资源ID，获取对应的string资源。获取普通string资源使用OH_ResourceManager_GetString(mgr, resId, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH_ResourceManager_GetString(mgr, resId, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。char **resultValue写入resultValue的结果。...格式化字符串资源参数，可变参数，支持const char*、int、float类型。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetStringByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetStringByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, ...)
```

**描述**

通过指定资源名称，获取对应的string资源。获取普通string资源使用OH_ResourceManager_GetString(mgr, resName, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH_ResourceManager_GetString(mgr, resName, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。char **resultValue写入resultValue的结果。...格式化字符串资源参数，可变参数，支持const char*、int、float类型。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetStringArray()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetStringArray(const NativeResourceManager *mgr, uint32_t resId, char ***resultValue, uint32_t *resultLen)
```

**描述**

通过指定资源ID，获取字符串数组。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()接口来释放字符串数组内存。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。char ***resultValue写入resultValue的结果。uint32_t *resultLen写入resultLen的StringArray长度。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetStringArrayByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetStringArrayByName(const NativeResourceManager *mgr, const char *resName, char ***resultValue, uint32_t *resultLen)
```

**描述**

通过指定资源名称，获取字符串数组。使用此接口后，需要调用OH_ResourceManager_ReleaseStringArray()接口来释放字符串数组内存。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。char ***resultValue写入resultValue的结果。uint32_t *resultLen写入resultLen的StringArray长度。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_ReleaseStringArray()

```ets
ResourceManager_ErrorCode OH_ResourceManager_ReleaseStringArray(char ***resValue, uint32_t len)
```

**描述**

释放字符串数组内存。

**起始版本：** 12

**参数：**

参数项描述char ***resValue需要释放的字符串数组。uint32_t len字符串数组长度。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

#### OH_ResourceManager_GetPluralString()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue)
```

**描述**

通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**废弃版本：** 18

**替代接口：**[OH_ResourceManager_GetIntPluralString](ohresmgr.h.md#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getintpluralstring)

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。uint32_t num数量值。char **resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetPluralStringByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue)
```

**描述**

通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**废弃版本：** 18

**替代接口：**[OH_ResourceManager_GetIntPluralStringByName](ohresmgr.h.md#ZH-CN_TOPIC_0000002497445344__oh_resourcemanager_getintpluralstringbyname)

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。uint32_t num数量值。char **resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetIntPluralString()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue, ...)
```

**描述**

通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。uint32_t num数量值（整数）。根据当前语言的复数规则获取该数量值对应的字符串数字。char **resultValue写入resultValue的结果。...格式化字符串资源参数，可变参数，支持const char*、int、float类型。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetDoublePluralString()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralString(const NativeResourceManager *mgr, uint32_t resId, double num, char **resultValue, ...)
```

**描述**

通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。double num数量值（浮点数）。根据当前语言的复数规则获取该数量值对应的字符串数字。char **resultValue写入resultValue的结果。...格式化字符串资源参数，可变参数，支持const char*、int、float类型。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetIntPluralStringByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue, ...)
```

**描述**

通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。uint32_t num数量值（整数）。根据当前语言的复数规则获取该数量值对应的字符串数字。char **resultValue写入resultValue的结果。...格式化字符串资源参数，可变参数，支持const char*、int、float类型。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetDoublePluralStringByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralStringByName(const NativeResourceManager *mgr, const char *resName, double num, char **resultValue, ...)
```

**描述**

通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。double num数量值（浮点数）。根据当前语言的复数规则获取该数量值对应的字符串数字。char **resultValue写入resultValue的结果。...格式化字符串资源参数，可变参数，支持const char*、int、float类型。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

[ERROR_CODE_OUT_OF_MEMORY](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001100 - 内存溢出。

#### OH_ResourceManager_GetColor()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetColor(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)
```

**描述**

通过指定资源ID，获取对应的颜色值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。uint32_t *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetColorByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetColorByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)
```

**描述**

通过指定资源ID，获取对应的颜色值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。uint32_t *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetInt()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetInt(const NativeResourceManager *mgr, uint32_t resId, int *resultValue)
```

**描述**

通过指定资源ID，获取对应的int值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。int *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetIntByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetIntByName(const NativeResourceManager *mgr, const char *resName, int *resultValue)
```

**描述**

通过指定资源名称，获取对应的int值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。int *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetFloat()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetFloat(const NativeResourceManager *mgr, uint32_t resId, float *resultValue)
```

**描述**

通过指定资源ID，获取对应的float值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。float *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetFloatByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetFloatByName(const NativeResourceManager *mgr, const char *resName, float *resultValue)
```

**描述**

通过指定资源名称，获取对应的float值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。float *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetBool()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetBool(const NativeResourceManager *mgr, uint32_t resId, bool *resultValue)
```

**描述**

通过指定资源ID，获取对应的bool值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。uint32_t resId资源ID。bool *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001001 - 无效的资源ID。

[ERROR_CODE_RES_NOT_FOUND_BY_ID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_GetBoolByName()

```ets
ResourceManager_ErrorCode OH_ResourceManager_GetBoolByName(const NativeResourceManager *mgr, const char *resName, bool *resultValue)
```

**描述**

通过指定资源名称，获取对应的bool值。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *resName资源名称。bool *resultValue写入resultValue的结果。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_RES_ID_NOT_FOUND](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001003 - 无效的资源名称。

[ERROR_CODE_RES_NOT_FOUND_BY_NAME](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。

[ERROR_CODE_RES_REF_TOO_MUCH](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001006 - 资源被循环引用。

#### OH_ResourceManager_AddResource()

```ets
ResourceManager_ErrorCode OH_ResourceManager_AddResource(const NativeResourceManager *mgr, const char *path)
```

**描述**

在应用程序运行时添加overlay资源。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *path资源路径。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_OVERLAY_RES_PATH_INVALID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001010 - 无效的资源路径.

#### OH_ResourceManager_RemoveResource()

```ets
ResourceManager_ErrorCode OH_ResourceManager_RemoveResource(const NativeResourceManager *mgr, const char *path)
```

**描述**

在应用程序运行时删除overlay资源。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](NativeResourceManager.md) *mgr指向[NativeResourceManager](NativeResourceManager.md)的指针，此指针通过[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *path资源路径。

**返回：**

类型说明[ResourceManager_ErrorCode](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode)

[SUCCESS](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 0 - 成功。

[ERROR_CODE_INVALID_INPUT_PARAMETER](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。

[ERROR_CODE_OVERLAY_RES_PATH_INVALID](resmgr_common.h.md#ZH-CN_TOPIC_0000002497445346__resourcemanager_errorcode) 9001010 - 无效的资源路径.