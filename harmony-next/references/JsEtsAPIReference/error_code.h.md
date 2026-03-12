# error_code.h

#### 概述

提供文件管理模块的错误码定义。

**引用文件：** <filemanagement/fileio/error_code.h>

**库：** NA

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**相关模块：**[FileIO](FileIO.md)

#### 汇总

#### 枚举

名称typedef关键字描述[FileManagement_ErrCode](#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)FileManagement_ErrCode文件管理模块错误码。

#### 枚举类型说明

#### FileManagement_ErrCode

```ets
enum FileManagement_ErrCode
```

**描述**

文件管理模块错误码。

**起始版本：** 12

枚举项描述ERR_OK = 0接口调用成功。ERR_PERMISSION_ERROR = 201接口权限校验失败。ERR_INVALID_PARAMETER = 401无效入参。ERR_DEVICE_NOT_SUPPORTED = 801当前设备不支持此接口。ERR_EPERM = 13900001操作不被允许。ERR_ENOENT = 13900002不存在此文件或文件夹。ERR_ENOMEM = 13900011内存溢出。ERR_UNKNOWN = 13900042内部未知错误。