# oh_file_uri.h

**概述**

提供uri和路径path之间的相互转换，目录uri获取，以及uri的有效性校验的方法。

引用文件： <filemanagement/file_uri/oh_file_uri.h>

库： libohfileuri.so

系统能力： SystemCapability.FileManagement.AppFileService

起始版本： 12

相关模块： [fileUri](fileUri.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| FileManagement_ErrCode OH_FileUri_GetUriFromPath(const char *path, unsigned int length, char **result) | 通过传入的路径path生成应用自己的uri；  将path转uri时，路径中的中文及非数字字母的特殊字符将会被编译成对应的ASCII码，拼接在uri中。 |
| FileManagement_ErrCode OH_FileUri_GetPathFromUri(const char *uri, unsigned int length, char **result) | 将uri转换成对应的沙箱路径path。   1、uri转path过程中会将uri中存在的ASCII码进行解码后拼接在原处，非系统接口生成的uri中可能存在ASCII码解析范围之外的字符， 导致字符串无法正常拼接；2、转换处理为系统约定的字符串替换规则（规则随系统演进可能会发生变化），转换过程中不进行路径校验操作，无法保证转换结果的一定可以访问。 |
| FileManagement_ErrCode OH_FileUri_GetFullDirectoryUri(const char *uri, unsigned int length, char **result) | 获取所在路径uri。uri指向文件则返回所在路径的uri，uri指向目录则不处理直接返回原串；  uri指向的文件不存在或属性获取失败则返回空串。 |
| bool OH_FileUri_IsValidUri(const char *uri, unsigned int length) | 判断传入的uri的格式是否正确。仅校验uri是否满足系统定义的格式规范，不校验uri的有效性。 |
| FileManagement_ErrCode OH_FileUri_GetFileName(const char *uri, unsigned int length, char **result) | 通过传入的uri获取到对应的文件名称。（如果文件名中存在ASCII码将会被解码处理后拼接在原处）。 |

**函数说明**

**OH_FileUri_GetUriFromPath()**

```ets
FileManagement_ErrCode OH_FileUri_GetUriFromPath(const char *path, unsigned int length, char **result)
```

描述

通过传入的路径path生成应用自己的uri；

 将path转uri时，路径中的中文及非数字字母的特殊字符将会被编译成对应的ASCII码，拼接在uri中。

系统能力： SystemCapability.FileManagement.AppFileService

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *path | 表示要转换的路径。 |
| unsigned int length | 表示要转换路径的字节长度。 |
| char **result | 表示转换后的uri, 需要使用standard library标准库的free()方法释放申请的资源。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FileManagement_ErrCode | 返回特定的错误码值，详细信息可以查看FileManagement_ErrCode。  ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因：  1. 参数path为空指针；  2. 参数result为空指针；  3. 输入的path长度与length不一致。  ERR_UNKNOWN 13900042 - 未知错误。转换后的uri长度为0会返回此错误。  ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR_OK 0 - 接口调用成功。 |

**OH_FileUri_GetPathFromUri()**

```ets
FileManagement_ErrCode OH_FileUri_GetPathFromUri(const char *uri, unsigned int length, char **result)
```

描述

将uri转换成对应的沙箱路径path。

 1、uri转path过程中会将uri中存在的ASCII码进行解码后拼接在原处，非系统接口生成的uri中可能存在ASCII码解析范围之外的字符， 导致字符串无法正常拼接；2、转换处理为系统约定的字符串替换规则（规则随系统演进可能会发生变化），转换过程中不进行路径校验操作，无法保证转换结果的一定可以访问。

系统能力： SystemCapability.FileManagement.AppFileService

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *uri | 表示要转换的uri。 |
| unsigned int length | 表示要转换uri的字节长度。 |
| char **result | 表示转换后的路径path。需要使用standard library标准库的free()方法释放申请的资源。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FileManagement_ErrCode | 返回特定的错误码值，详细信息可以查看FileManagement_ErrCode。  ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因：  1. 参数uri为空指针；  2. 参数result为空指针；  3. 输入的uri长度与length不一致。  ERR_UNKNOWN 13900042 - 未知错误。转换后的路径path长度为0会返回此错误。  ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR_OK 0 - 接口调用成功。 |

**OH_FileUri_GetFullDirectoryUri()**

```ets
FileManagement_ErrCode OH_FileUri_GetFullDirectoryUri(const char *uri, unsigned int length, char **result)
```

描述

获取所在路径uri。uri指向文件则返回所在路径的uri，uri指向目录则不处理直接返回原串；

 uri指向的文件不存在或属性获取失败则返回空串。

系统能力： SystemCapability.FileManagement.AppFileService

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *uri | 表示要获取目录的uri的原始uri。 |
| unsigned int length | 表示原始uri的字节长度。 |
| char **result | 表示获取到的目录uri，需要使用standard library标准库的free()方法释放申请的资源。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FileManagement_ErrCode | 返回特定的错误码值，详细信息可以查看FileManagement_ErrCode。  ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因：  1. 参数uri为空指针；  2. 参数result为空指针；  3. 输入的uri长度与length不一致。  ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR_ENOENT 13900002 - 没有该文件或目录。  ERR_UNKNOWN 13900042 - 未知错误。获取到的目录uri长度为0会返回此错误。  ERR_OK 0 - 接口调用成功。 |

**OH_FileUri_IsValidUri()**

```ets
bool OH_FileUri_IsValidUri(const char *uri, unsigned int length)
```

描述

判断传入的uri的格式是否正确。仅校验uri是否满足系统定义的格式规范，不校验uri的有效性。

系统能力： SystemCapability.FileManagement.AppFileService

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *uri | 表示需要校验的uri。 |
| unsigned int length | 需要校验uri的字节长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回 true: 传入uri是有效的uri；false: 传入的uri是无效的uri。 |

**OH_FileUri_GetFileName()**

```ets
FileManagement_ErrCode OH_FileUri_GetFileName(const char *uri, unsigned int length, char **result)
```

描述

通过传入的uri获取到对应的文件名称。（如果文件名中存在ASCII码将会被解码处理后拼接在原处）。

系统能力： SystemCapability.FileManagement.AppFileService

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *uri | 传入的uri。 |
| unsigned int length | 表示传入uri的字节长度。 |
| char **result | 表示转换后的名称。需要使用standard library标准库的free()方法释放申请的资源。 |

返回：

| 类型 | 说明 |
| --- | --- |
| FileManagement_ErrCode | 返回特定的错误码值，详细信息可以查看FileManagement_ErrCode。  ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因：  1. 参数uri为空指针；  2. 参数result为空指针；  3. 输入的uri长度与length不一致；  4. uri格式不正确。  ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。  ERR_OK 0 - 接口调用成功。 |