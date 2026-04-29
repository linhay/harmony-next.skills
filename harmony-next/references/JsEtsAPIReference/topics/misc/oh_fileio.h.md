# oh_fileio.h

**概述**

fileio模块接口定义，提供获取文件存储位置的native接口。

引用文件： <filemanagement/fileio/oh_fileio.h>

库： libohfileio.so

系统能力： SystemCapability.FileManagement.File.FileIO

起始版本： 12

相关模块： [FileIO](FileIO.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| FileIO_FileLocation | FileIO_FileLocation | 文件存储位置枚举值。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| FileManagement_ErrCode OH_FileIO_GetFileLocation(char *uri, int uriLength, FileIO_FileLocation *location) | 获取文件存储位置。 |

**枚举类型说明**

**FileIO_FileLocation**

```ets
enum FileIO_FileLocation
```

描述

文件存储位置枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| LOCAL = 1 | 文件存储于本地。 |
| CLOUD = 2 | 文件存储于云侧。 |
| LOCAL_AND_CLOUD = 3 | 文件存储于本地及云侧。 |

**函数说明**

**OH_FileIO_GetFileLocation()**

```ets
FileManagement_ErrCode OH_FileIO_GetFileLocation(char *uri, int uriLength, FileIO_FileLocation *location)
```

描述

获取文件存储位置。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| char *uri | 指向入参uri的指针。 |
| int uriLength | 入参uri字符串的长度。 |
| FileIO_FileLocation *location | 输出文件存储位置的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FileManagement_ErrCode | 返回FileManagement模块错误码FileManagement_ErrCode。 |