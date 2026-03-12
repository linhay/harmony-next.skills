# raw_dir.h

#### 概述

提供rawfile目录相关功能，包括遍历和关闭rawfile目录。

**引用文件：** <rawfile/raw_dir.h>

**库：** librawfile.z.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 8

**相关模块：**[rawfile](rawfile.md)

#### 汇总

#### 结构体

名称typedef关键字描述[RawDir](RawDir.md)RawDir提供对rawfile目录的访问。

#### 函数

名称描述[const char *OH_ResourceManager_GetRawFileName(RawDir *rawDir, int index)](#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_getrawfilename)通过索引获取rawfile文件名称。可以使用此方法遍历rawfile目录。[int OH_ResourceManager_GetRawFileCount(RawDir *rawDir)](#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_getrawfilecount)获取[RawDir](zh-cn_topic_0000002497445348.html)中的rawfile数量。通过此方法可以获取[OH_ResourceManager_GetRawFileName](raw_dir.h.md#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_getrawfilename)中可用的索引。[void OH_ResourceManager_CloseRawDir(RawDir *rawDir)](#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_closerawdir)关闭已打开的[RawDir](zh-cn_topic_0000002497445348.html)并释放所有相关联资源。

#### 函数说明

#### OH_ResourceManager_GetRawFileName()

```ets
const char *OH_ResourceManager_GetRawFileName(RawDir *rawDir, int index)
```

**描述**

通过索引获取rawfile文件名称。可以使用此方法遍历rawfile目录。

**起始版本：** 8

**参数：**

参数项描述[RawDir](RawDir.md) *rawDir表示指向[RawDir](RawDir.md)的指针。int index表示文件在[RawDir](RawDir.md)中的索引位置。

**返回：**

类型说明const char *

通过索引返回文件名称，此返回值可以作为[OH_ResourceManager_OpenRawFile](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawfile)的输入参数。

 如果遍历完所有文件仍未找到，则返回NULL。

**参考：**

[OH_ResourceManager_OpenRawFile](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawfile)

#### OH_ResourceManager_GetRawFileCount()

```ets
int OH_ResourceManager_GetRawFileCount(RawDir *rawDir)
```

**描述**

获取[RawDir](RawDir.md)中的rawfile数量。通过此方法可以获取[OH_ResourceManager_GetRawFileName](raw_dir.h.md#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_getrawfilename)中可用的索引。

**起始版本：** 8

**参数：**

参数项描述[RawDir](RawDir.md) *rawDir表示指向[RawDir](RawDir.md)的指针。

**返回：**

类型说明int返回rawDir下的文件个数。如果rawDir为空时返回0。

**参考：**

[OH_ResourceManager_GetRawFileName](raw_dir.h.md#ZH-CN_TOPIC_0000002529285315__oh_resourcemanager_getrawfilename)

#### OH_ResourceManager_CloseRawDir()

```ets
void OH_ResourceManager_CloseRawDir(RawDir *rawDir)
```

**描述**

关闭已打开的[RawDir](RawDir.md)并释放所有相关联资源。

**起始版本：** 8

**参数：**

参数项描述[RawDir](RawDir.md) *rawDir表示指向[RawDir](RawDir.md)的指针。

**参考：**

[OH_ResourceManager_OpenRawDir](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawdir)