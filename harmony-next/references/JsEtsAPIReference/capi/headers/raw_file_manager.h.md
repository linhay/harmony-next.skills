# raw_file_manager.h

#### 概述

提供资源管理rawfile相关功能，可以使用ResourceManager打开rawfile进行后续相关操作，像搜索和读取等。

**引用文件：** <rawfile/raw_file_manager.h>

**库：** librawfile.z.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 8

**相关模块：**[rawfile](../../topics/misc/rawfile.md)

#### 汇总

#### 结构体

名称typedef关键字描述[NativeResourceManager](../../topics/system-services/NativeResourceManager.md)NativeResourceManager代表native侧的ResourceManager。此类封装了JavaScript resource manager的native实现，**ResourceManager**指针可以通过调用[OH_ResourceManager_InitNativeResourceManager](#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。

#### 函数

名称描述[NativeResourceManager *OH_ResourceManager_InitNativeResourceManager(napi_env env, napi_value jsResMgr)](#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)基于JavaScript侧的ResourceManager获取native侧的ResourceManager，用来完成rawfile相关功能。[void OH_ResourceManager_ReleaseNativeResourceManager(NativeResourceManager *resMgr)](#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_releasenativeresourcemanager)释放native侧ResourceManager。[RawDir *OH_ResourceManager_OpenRawDir(const NativeResourceManager *mgr, const char *dirName)](#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawdir)打开rawfile目录，打开后可以遍历对应目录下的rawfile文件。[RawFile *OH_ResourceManager_OpenRawFile(const NativeResourceManager *mgr, const char *fileName)](#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawfile)打开rawfile文件，打开后可以读取它的数据。[RawFile64 *OH_ResourceManager_OpenRawFile64(const NativeResourceManager *mgr, const char *fileName)](#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawfile64)打开较大的rawfile文件，打开后可以读取它的数据。[bool OH_ResourceManager_IsRawDir(const NativeResourceManager *mgr, const char *path)](#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_israwdir)判断路径是否是rawfile下的目录。

#### 函数说明

#### OH_ResourceManager_InitNativeResourceManager()

```ets
NativeResourceManager *OH_ResourceManager_InitNativeResourceManager(napi_env env, napi_value jsResMgr)
```

**描述**

基于JavaScript侧的ResourceManager获取native侧的ResourceManager，用来完成rawfile相关功能。

**起始版本：** 8

**参数：**

参数项描述napi_env env表示JavaScript Native Interface（napi）环境指针。napi_value jsResMgr表示JavaScript resource manager。

**返回：**

类型说明[NativeResourceManager *](../../topics/system-services/NativeResourceManager.md)返回[NativeResourceManager](../../topics/system-services/NativeResourceManager.md)指针，如果失败返回空指针。

#### OH_ResourceManager_ReleaseNativeResourceManager()

```ets
void OH_ResourceManager_ReleaseNativeResourceManager(NativeResourceManager *resMgr)
```

**描述**

释放native侧ResourceManager。

**起始版本：** 8

**参数：**

参数项描述[NativeResourceManager](../../topics/system-services/NativeResourceManager.md) *resMgr表示[NativeResourceManager](../../topics/system-services/NativeResourceManager.md)指针。

#### OH_ResourceManager_OpenRawDir()

```ets
RawDir *OH_ResourceManager_OpenRawDir(const NativeResourceManager *mgr, const char *dirName)
```

**描述**

打开rawfile目录，打开后可以遍历对应目录下的rawfile文件。

**起始版本：** 8

**参数：**

参数项描述[const NativeResourceManager](../../topics/system-services/NativeResourceManager.md) *mgr表示指向[NativeResourceManager](../../topics/system-services/NativeResourceManager.md)的指针，此指针是通过调用[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取的。const char *dirName表示要打开的rawfile目录名称，当传递一个空字符串时表示打开rawfile根目录。

**返回：**

类型说明[RawDir *](../../topics/misc/RawDir.md)返回[RawDir](../../topics/misc/RawDir.md)指针。使用完此指针后，调用[OH_ResourceManager_CloseRawDir](raw_dir.h.md#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_closerawdir)释放。如果失败或者mgr为空时返回空指针。

**参考：**

[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)

[OH_ResourceManager_CloseRawDir](raw_dir.h.md#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_closerawdir)

#### OH_ResourceManager_OpenRawFile()

```ets
RawFile *OH_ResourceManager_OpenRawFile(const NativeResourceManager *mgr, const char *fileName)
```

**描述**

打开rawfile文件，打开后可以读取它的数据。

**起始版本：** 8

**参数：**

参数项描述[const NativeResourceManager](../../topics/system-services/NativeResourceManager.md) *mgr表示指向[NativeResourceManager](../../topics/system-services/NativeResourceManager.md)的指针，此指针通过调用[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *fileName表示基于rawfile根目录的相对路径下的文件名称。

**返回：**

类型说明[RawFile *](../../topics/misc/rawfile.md)返回[RawFile](../../topics/misc/rawfile.md)指针。当使用完此指针，调用[OH_ResourceManager_CloseRawFile](raw_file.h.md#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_closerawfile)释放。如果失败或者mgr和fileName为空时返回空指针。

**参考：**

[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)

[OH_ResourceManager_CloseRawFile](raw_file.h.md#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_closerawfile)

#### OH_ResourceManager_OpenRawFile64()

```ets
RawFile64 *OH_ResourceManager_OpenRawFile64(const NativeResourceManager *mgr, const char *fileName)
```

**描述**

打开较大的rawfile文件，打开后可以读取它的数据。

**起始版本：** 11

**参数：**

参数项描述[const NativeResourceManager](../../topics/system-services/NativeResourceManager.md) *mgr表示指向[NativeResourceManager](../../topics/system-services/NativeResourceManager.md)的指针，此指针通过调用[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *fileName表示基于rawfile根目录的相对路径下的文件名称。

**返回：**

类型说明[RawFile64 *](../../topics/misc/RawFile64.md)返回[RawFile64](../../topics/misc/RawFile64.md)指针。当使用完此指针，调用[OH_ResourceManager_CloseRawFile64](raw_file.h.md#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_closerawfile64)释放。如果失败或者mgr和fileName为空时返回空指针。

**参考：**

[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)

[OH_ResourceManager_CloseRawFile64](raw_file.h.md#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_closerawfile64)

#### OH_ResourceManager_IsRawDir()

```ets
bool OH_ResourceManager_IsRawDir(const NativeResourceManager *mgr, const char *path)
```

**描述**

判断路径是否是rawfile下的目录。

**起始版本：** 12

**参数：**

参数项描述[const NativeResourceManager](../../topics/system-services/NativeResourceManager.md) *mgr表示指向[NativeResourceManager](../../topics/system-services/NativeResourceManager.md)的指针，此指针通过调用[OH_ResourceManager_InitNativeResourceManager](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_initnativeresourcemanager)方法获取。const char *pathrawfile路径。

**返回：**

类型说明bool返回true表示是rawfile下的目录，返回false表示不是rawfile下的目录。