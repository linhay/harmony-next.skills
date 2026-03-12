# raw_file.h

#### 概述

提供rawfile文件相关功能，功能包括搜索、读取和关闭。

**引用文件：** <rawfile/raw_file.h>

**库：** librawfile.z.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 8

**相关模块：**[rawfile](rawfile.md)

#### 汇总

#### 结构体

名称typedef关键字描述[RawFileDescriptor](RawFileDescriptor.md)RawFileDescriptor提供rawfile文件描述符信息。RawFileDescriptor是[OH_ResourceManager_GetRawFileDescriptor](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfiledescriptor)的输出参数，涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。[RawFileDescriptor64](zh-cn_topic_0000002529445293.html)RawFileDescriptor64提供较大rawfile文件描述符信息。RawFileDescriptor64是[OH_ResourceManager_GetRawFileDescriptor64](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfiledescriptor64)的输出参数，涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。[RawFile](zh-cn_topic_0000002497605328.html)RawFile提供对rawfile的访问功能。[RawFile64](RawFile64.md)RawFile64提供对较大rawfile的访问功能。

#### 函数

名称描述[int OH_ResourceManager_ReadRawFile(const RawFile *rawFile, void *buf, size_t length)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_readrawfile)读取rawfile内容，从当前位置读取指定长度的数据。[int OH_ResourceManager_SeekRawFile(const RawFile *rawFile, long offset, int whence)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_seekrawfile)基于指定的偏移量，在rawfile文件内搜索读写数据的位置。[long OH_ResourceManager_GetRawFileSize(RawFile *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfilesize)获取rawfile长度，单位为long。[long OH_ResourceManager_GetRawFileRemainingLength(const RawFile *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfileremaininglength)获取rawfile的剩余长度，单位为long。[void OH_ResourceManager_CloseRawFile(RawFile *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_closerawfile)关闭已打开的[RawFile](zh-cn_topic_0000002497605328.html) 以及释放所有相关联的资源。[long OH_ResourceManager_GetRawFileOffset(const RawFile *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfileoffset)获取rawfile当前的偏移量，单位为long。rawfile当前的偏移量。[bool OH_ResourceManager_GetRawFileDescriptor(const RawFile *rawFile, RawFileDescriptor &descriptor)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfiledescriptor)基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。(API12废弃)[bool OH_ResourceManager_GetRawFileDescriptorData(const RawFile *rawFile, RawFileDescriptor *descriptor)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfiledescriptordata)基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。[bool OH_ResourceManager_ReleaseRawFileDescriptor(const RawFileDescriptor &descriptor)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_releaserawfiledescriptor)关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。(API12废弃)[bool OH_ResourceManager_ReleaseRawFileDescriptorData(const RawFileDescriptor *descriptor)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_releaserawfiledescriptordata)关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。[int64_t OH_ResourceManager_ReadRawFile64(const RawFile64 *rawFile, void *buf, int64_t length)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_readrawfile64)读取较大的rawfile文件内容，从当前位置读取指定长度的数据。[int OH_ResourceManager_SeekRawFile64(const RawFile64 *rawFile, int64_t offset, int whence)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_seekrawfile64)基于指定的偏移量，在较大的rawfile文件内搜索读写数据的位置。[int64_t OH_ResourceManager_GetRawFileSize64(RawFile64 *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfilesize64)获取较大rawfile文件的长度，单位为int64_t。[int64_t OH_ResourceManager_GetRawFileRemainingLength64(const RawFile64 *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfileremaininglength64)获取较大rawfile的剩余长度，单位为int64_t。[void OH_ResourceManager_CloseRawFile64(RawFile64 *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_closerawfile64)关闭已打开的[RawFile64](zh-cn_topic_0000002497445350.html) 以及释放所有相关联的资源。[int64_t OH_ResourceManager_GetRawFileOffset64(const RawFile64 *rawFile)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfileoffset64)获取较大rawfile文件的偏移量，单位为int64_t。[bool OH_ResourceManager_GetRawFileDescriptor64(const RawFile64 *rawFile, RawFileDescriptor64 *descriptor)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfiledescriptor64)基于偏移量（单位为int64_t）和文件长度（单位为int64_t）打开较大的rawfile，并获取文件描述符。打开的文件描述符被用于读取rawfile。[bool OH_ResourceManager_ReleaseRawFileDescriptor64(const RawFileDescriptor64 *descriptor)](#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_releaserawfiledescriptor64)关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。

#### 函数说明

#### OH_ResourceManager_ReadRawFile()

```ets
int OH_ResourceManager_ReadRawFile(const RawFile *rawFile, void *buf, size_t length)
```

**描述**

读取rawfile内容，从当前位置读取指定长度的数据。

**起始版本：** 8

**参数：**

参数项描述[const RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。void *buf用于接收读取数据的缓冲区指针。size_t length读取数据的字节长度。

**返回：**

类型说明int返回读取的字节数，如果读取长度超过文件末尾长度或者rawfile为空时，则返回0。

#### OH_ResourceManager_SeekRawFile()

```ets
int OH_ResourceManager_SeekRawFile(const RawFile *rawFile, long offset, int whence)
```

**描述**

基于指定的偏移量，在rawfile文件内搜索读写数据的位置。

**起始版本：** 8

**参数：**

参数项描述[const RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。long offset表示指定的偏移量。int whence

读写位置，有以下场景:

 0: 读写位置为文件起始位置加上offset。

 1: 读写位置为当前位置加上offset。

 2: 读写位置为文件末尾加上offset。

**返回：**

类型说明int如果搜索成功返回0，如果发生错误返回-1。

#### OH_ResourceManager_GetRawFileSize()

```ets
long OH_ResourceManager_GetRawFileSize(RawFile *rawFile)
```

**描述**

获取rawfile长度，单位为long。

**起始版本：** 8

**参数：**

参数项描述[RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。

**返回：**

类型说明long返回rawfile的整体长度，如果rawfile为空时返回0。

#### OH_ResourceManager_GetRawFileRemainingLength()

```ets
long OH_ResourceManager_GetRawFileRemainingLength(const RawFile *rawFile)
```

**描述**

获取rawfile的剩余长度，单位为long。

**起始版本：** 11

**参数：**

参数项描述[const RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。

**返回：**

类型说明long返回rawfile的剩余长度，如果rawfile为空时返回0。

#### OH_ResourceManager_CloseRawFile()

```ets
void OH_ResourceManager_CloseRawFile(RawFile *rawFile)
```

**描述**

关闭已打开的[RawFile](RawFile.md) 以及释放所有相关联的资源。

**起始版本：** 8

**参数：**

参数项描述[RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。

**参考：**

[OH_ResourceManager_OpenRawFile](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawfile)

#### OH_ResourceManager_GetRawFileOffset()

```ets
long OH_ResourceManager_GetRawFileOffset(const RawFile *rawFile)
```

**描述**

获取rawfile当前的偏移量，单位为long。rawfile当前的偏移量。

**起始版本：** 8

**参数：**

参数项描述[const RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。

**返回：**

类型说明long返回rawfile当前的偏移量，如果rawfile为空时返回0。

#### OH_ResourceManager_GetRawFileDescriptor()

```ets
bool OH_ResourceManager_GetRawFileDescriptor(const RawFile *rawFile, RawFileDescriptor &descriptor)
```

**描述**

基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。

**起始版本：** 8

**废弃版本：** 12

**替代接口：**[OH_ResourceManager_GetRawFileDescriptorData](raw_file.h.md#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfiledescriptordata)

**参数：**

参数项描述[const RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。RawFileDescriptor &descriptor显示rawfile文件描述符，以及在HAP包中的起始位置和长度。

**返回：**

类型说明bool返回true表示打开rawfile文件描述符成功，返回false表示rawfile不允许被访问。

#### OH_ResourceManager_GetRawFileDescriptorData()

```ets
bool OH_ResourceManager_GetRawFileDescriptorData(const RawFile *rawFile, RawFileDescriptor *descriptor)
```

**描述**

基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。

**起始版本：** 12

**参数：**

参数项描述[const RawFile](RawFile.md) *rawFile表示指向[RawFile](RawFile.md)的指针。[RawFileDescriptor](RawFileDescriptor.md) *descriptor显示rawfile文件描述符，以及在HAP包中的起始位置和长度。

**返回：**

类型说明bool返回true表示打开rawfile文件描述符成功，返回false表示rawfile不允许被访问。

#### OH_ResourceManager_ReleaseRawFileDescriptor()

```ets
bool OH_ResourceManager_ReleaseRawFileDescriptor(const RawFileDescriptor &descriptor)
```

**描述**

关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。

**起始版本：** 8

**废弃版本：** 12

**替代接口：**[OH_ResourceManager_ReleaseRawFileDescriptorData](raw_file.h.md#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_releaserawfiledescriptordata)

**参数：**

参数项描述[ const RawFileDescriptor](RawFileDescriptor.md) &descriptor包含rawfile文件描述符，以及在HAP包中的起始位置和长度。

**返回：**

类型说明bool返回true表示关闭文件描述符成功，返回false表示关闭文件描述符失败。

#### OH_ResourceManager_ReleaseRawFileDescriptorData()

```ets
bool OH_ResourceManager_ReleaseRawFileDescriptorData(const RawFileDescriptor *descriptor)
```

**描述**

关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。

**起始版本：** 12

**参数：**

参数项描述[const RawFileDescriptor](RawFileDescriptor.md) *descriptor包含rawfile文件描述符，以及在HAP包中的起始位置和长度。

**返回：**

类型说明bool返回true表示关闭文件描述符成功，返回false表示关闭文件描述符失败。

#### OH_ResourceManager_ReadRawFile64()

```ets
int64_t OH_ResourceManager_ReadRawFile64(const RawFile64 *rawFile, void *buf, int64_t length)
```

**描述**

读取较大的rawfile文件内容，从当前位置读取指定长度的数据。

**起始版本：** 11

**参数：**

参数项描述[const RawFile64](RawFile64.md) *rawFile表示指向[RawFile64](RawFile64.md)的指针。void *buf用于接收读取数据的缓冲区指针。int64_t length读取数据的字节长度。

**返回：**

类型说明int64_t返回读取的字节数，如果读取长度超过文件末尾长度或者rawfile为空时，则返回0。

#### OH_ResourceManager_SeekRawFile64()

```ets
int OH_ResourceManager_SeekRawFile64(const RawFile64 *rawFile, int64_t offset, int whence)
```

**描述**

基于指定的偏移量，在较大的rawfile文件内搜索读写数据的位置。

**起始版本：** 11

**参数：**

参数项描述[const RawFile64](RawFile64.md) *rawFile表示指向[RawFile64](RawFile64.md)的指针。int64_t offset表示指定的偏移量。int whence

读写位置，有以下场景:

 0: 读写位置为文件起始位置加上offset。

 1: 读写位置为当前位置加上offset。

 2: 读写位置为文件末尾加上offset。

**返回：**

类型说明int如果搜索成功返回0，如果发生错误返回-1。

#### OH_ResourceManager_GetRawFileSize64()

```ets
int64_t OH_ResourceManager_GetRawFileSize64(RawFile64 *rawFile)
```

**描述**

获取较大rawfile文件的长度，单位为int64_t。

**起始版本：** 11

**参数：**

参数项描述[RawFile64](RawFile64.md) *rawFile表示指向[RawFile64](RawFile64.md)的指针。

**返回：**

类型说明int64_t返回rawfile的整体长度，如果rawfile为空时返回0。

#### OH_ResourceManager_GetRawFileRemainingLength64()

```ets
int64_t OH_ResourceManager_GetRawFileRemainingLength64(const RawFile64 *rawFile)
```

**描述**

获取较大rawfile的剩余长度，单位为int64_t。

**起始版本：** 11

**参数：**

参数项描述[const RawFile64](RawFile64.md) *rawFile表示指向[RawFile64](RawFile64.md)的指针。

**返回：**

类型说明int64_t返回rawfile的剩余长度，如果rawfile为空时返回0。

#### OH_ResourceManager_CloseRawFile64()

```ets
void OH_ResourceManager_CloseRawFile64(RawFile64 *rawFile)
```

**描述**

关闭已打开的[RawFile64](RawFile64.md) 以及释放所有相关联的资源。

**起始版本：** 11

**参数：**

参数项描述[RawFile64](RawFile64.md) *rawFile表示指向[RawFile64](RawFile64.md)的指针。

**参考：**

[OH_ResourceManager_OpenRawFile64](raw_file_manager.h.md#ZH-CN_TOPIC_0000002497605324__oh_resourcemanager_openrawfile64)

#### OH_ResourceManager_GetRawFileOffset64()

```ets
int64_t OH_ResourceManager_GetRawFileOffset64(const RawFile64 *rawFile)
```

**描述**

获取较大rawfile文件的偏移量，单位为int64_t。

**起始版本：** 11

**参数：**

参数项描述[const RawFile64](RawFile64.md) *rawFile表示指向[RawFile64](RawFile64.md)的指针。

**返回：**

类型说明int64_t返回rawfile当前的偏移量，如果rawfile为空时返回0。

#### OH_ResourceManager_GetRawFileDescriptor64()

```ets
bool OH_ResourceManager_GetRawFileDescriptor64(const RawFile64 *rawFile, RawFileDescriptor64 *descriptor)
```

**描述**

基于偏移量（单位为int64_t）和文件长度（单位为int64_t）打开较大的rawfile，并获取文件描述符。打开的文件描述符被用于读取rawfile。

**起始版本：** 11

**参数：**

参数项描述[const RawFile64](RawFile64.md) *rawFile表示指向[RawFile64](RawFile64.md)的指针。[RawFileDescriptor64](RawFileDescriptor64.md) *descriptor显示rawfile文件描述符，以及在HAP包中的起始位置和长度。

**返回：**

类型说明bool返回true表示打开rawfile文件描述符成功，返回false表示rawfile不允许被访问。

#### OH_ResourceManager_ReleaseRawFileDescriptor64()

```ets
bool OH_ResourceManager_ReleaseRawFileDescriptor64(const RawFileDescriptor64 *descriptor)
```

**描述**

关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。

**起始版本：** 11

**参数：**

参数项描述[const RawFileDescriptor64](RawFileDescriptor64.md) *descriptor包含rawfile文件描述符，以及在HAP包中的起始位置和长度。

**返回：**

类型说明bool返回true表示关闭文件描述符成功，返回false表示关闭文件描述符失败。