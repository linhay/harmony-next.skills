# oh_fileio.h

#### 概述

fileio模块接口定义，提供获取文件存储位置的native接口。

**引用文件：** <filemanagement/fileio/oh_fileio.h>

**库：** libohfileio.so

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**相关模块：**[FileIO](../../topics/misc/FileIO.md)

#### 汇总

#### 枚举

名称typedef关键字描述[FileIO_FileLocation](#ZH-CN_TOPIC_0000002529285259__fileio_filelocation)FileIO_FileLocation文件存储位置枚举值。

#### 函数

名称描述[FileManagement_ErrCode OH_FileIO_GetFileLocation(char *uri, int uriLength, FileIO_FileLocation *location)](#ZH-CN_TOPIC_0000002529285259__oh_fileio_getfilelocation)获取文件存储位置。

#### 枚举类型说明

#### FileIO_FileLocation

```ets
enum FileIO_FileLocation
```

**描述**

文件存储位置枚举值。

**起始版本：** 12

枚举项描述LOCAL = 1文件存储于本地。CLOUD = 2文件存储于云侧。LOCAL_AND_CLOUD = 3文件存储于本地及云侧。

#### 函数说明

#### OH_FileIO_GetFileLocation()

```ets
FileManagement_ErrCode OH_FileIO_GetFileLocation(char *uri, int uriLength, FileIO_FileLocation *location)
```

**描述**

获取文件存储位置。

**起始版本：** 12

**参数：**

参数项描述char *uri指向入参uri的指针。int uriLength入参uri字符串的长度。[FileIO_FileLocation](oh_fileio.h.md#ZH-CN_TOPIC_0000002529285259__fileio_filelocation) *location输出文件存储位置的指针。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)返回FileManageMent模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。