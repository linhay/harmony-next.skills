# oh_environment.h

#### 概述

environment模块接口定义，使用environment提供的native接口，获取公共文件根目录的沙箱路径。

**引用文件：** <filemanagement/environment/oh_environment.h>

**库：** libohenvironment.so

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**起始版本：** 12

**相关模块：**[Environment](../../topics/misc/Environment.md)

#### 汇总

#### 函数

名称描述[FileManagement_ErrCode OH_Environment_GetUserDownloadDir(char **result)](#ZH-CN_TOPIC_0000002497605266__oh_environment_getuserdownloaddir)获取Download根目录沙箱路径。[FileManagement_ErrCode OH_Environment_GetUserDesktopDir(char **result)](#ZH-CN_TOPIC_0000002497605266__oh_environment_getuserdesktopdir)获取Desktop根目录沙箱路径。[FileManagement_ErrCode OH_Environment_GetUserDocumentDir(char **result)](#ZH-CN_TOPIC_0000002497605266__oh_environment_getuserdocumentdir)获取Document根目录沙箱路径。

#### 函数说明

#### OH_Environment_GetUserDownloadDir()

```ets
FileManagement_ErrCode OH_Environment_GetUserDownloadDir(char **result)
```

**描述**

获取Download根目录沙箱路径。

**起始版本：** 12

**参数：**

参数项描述char **resultDownload根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。

#### OH_Environment_GetUserDesktopDir()

```ets
FileManagement_ErrCode OH_Environment_GetUserDesktopDir(char **result)
```

**描述**

获取Desktop根目录沙箱路径。

**起始版本：** 12

**参数：**

参数项描述char **resultDesktop根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。

#### OH_Environment_GetUserDocumentDir()

```ets
FileManagement_ErrCode OH_Environment_GetUserDocumentDir(char **result)
```

**描述**

获取Document根目录沙箱路径。

**起始版本：** 12

**参数：**

参数项描述char **resultDocument根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。