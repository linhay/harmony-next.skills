# oh_file_share.h

#### 概述

提供基于URI的文件及目录授予持久化权限、权限激活、权限查询等方法。

**引用文件：** <filemanagement/fileshare/oh_file_share.h>

**库：** libohfileshare.so

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 12

**相关模块：**[fileShare](fileShare.md)

#### 汇总

#### 结构体

名称typedef关键字描述[FileShare_PolicyErrorResult](FileShare_PolicyErrorResult.md)FileShare_PolicyErrorResult授予或使能权限失败的URI策略结果。[FileShare_PolicyInfo](FileShare_PolicyInfo.md)FileShare_PolicyInfo需要授予或使能权限URI的策略信息。

#### 枚举

名称typedef关键字描述[FileShare_OperationMode](#ZH-CN_TOPIC_0000002529445233__fileshare_operationmode)FileShare_OperationModeURI操作模式枚举值。[FileShare_PolicyErrorCode](#ZH-CN_TOPIC_0000002529445233__fileshare_policyerrorcode)FileShare_PolicyErrorCode授予或使能权限策略失败的URI对应的错误码。

#### 函数

名称描述[FileManagement_ErrCode OH_FileShare_PersistPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)](#ZH-CN_TOPIC_0000002529445233__oh_fileshare_persistpermission)对所选择的多个文件或目录URI持久化授权。[FileManagement_ErrCode OH_FileShare_RevokePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)](#ZH-CN_TOPIC_0000002529445233__oh_fileshare_revokepermission)对所选择的多个文件或目录URI取消持久化授权。[FileManagement_ErrCode OH_FileShare_ActivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)](#ZH-CN_TOPIC_0000002529445233__oh_fileshare_activatepermission)使能多个已经持久化授权的文件或目录。[FileManagement_ErrCode OH_FileShare_DeactivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)](#ZH-CN_TOPIC_0000002529445233__oh_fileshare_deactivatepermission)取消使能持久化授权过的多个文件或目录。[FileManagement_ErrCode OH_FileShare_CheckPersistentPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, bool **result, unsigned int *resultNum)](#ZH-CN_TOPIC_0000002529445233__oh_fileshare_checkpersistentpermission)校验所选择的多个文件或目录URI的持久化授权。[void OH_FileShare_ReleasePolicyErrorResult(FileShare_PolicyErrorResult *errorResult, unsigned int resultNum)](#ZH-CN_TOPIC_0000002529445233__oh_fileshare_releasepolicyerrorresult)释放FileShare_PolicyErrorResult指针指向的内存资源。

#### 枚举类型说明

#### FileShare_OperationMode

```ets
enum FileShare_OperationMode
```

**描述**

URI操作模式枚举值。

**起始版本：** 12

枚举项描述READ_MODE = 1 << 0读取权限。WRITE_MODE = 1 << 1写入权限。

#### FileShare_PolicyErrorCode

```ets
enum FileShare_PolicyErrorCode
```

**描述**

授予或使能权限策略失败的URI对应的错误码。

**起始版本：** 12

枚举项描述PERSISTENCE_FORBIDDEN = 1URI禁止被持久化。INVALID_MODE = 2无效的模式。INVALID_PATH = 3无效路径。PERMISSION_NOT_PERSISTED = 4权限没有被持久化。

#### 函数说明

#### OH_FileShare_PersistPermission()

```ets
FileManagement_ErrCode OH_FileShare_PersistPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

对所选择的多个文件或目录URI持久化授权。

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**起始版本：** 12

**参数：**

参数项描述[const FileShare_PolicyInfo](FileShare_PolicyInfo.md) *policies一个指向FileShare_PolicyInfo实例的指针。unsigned int policyNumFileShare_PolicyInfo实例数组的大小。[FileShare_PolicyErrorResult](FileShare_PolicyErrorResult.md) **resultFileShare_PolicyErrorResult数组指针。请使用OH_FileShare_ReleasePolicyErrorResult()进行资源释放。unsigned int *resultNumFileShare_PolicyErrorResult数组大小。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)

返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。

 ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因有：

 1. 参数policies或参数result或参数resultNum为空指针；

 2. 参数policyNum值为0或者超过最大长度(500)；

 3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。

 ERR_DEVICE_NOT_SUPPORTED 801 - 当前设备类型不支持此接口。

 ERR_PERMISSION_ERROR 201 - 接口权限校验失败。

 ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。

 ERR_EPERM 13900001 - 操作不被允许。

 ERR_OK 0 - 接口调用成功。

#### OH_FileShare_RevokePermission()

```ets
FileManagement_ErrCode OH_FileShare_RevokePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

对所选择的多个文件或目录URI取消持久化授权。

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**起始版本：** 12

**参数：**

参数项描述[const FileShare_PolicyInfo](FileShare_PolicyInfo.md) *policies一个指向FileShare_PolicyInfo实例的指针。unsigned int policyNumFileShare_PolicyInfo实例数组的大小。[FileShare_PolicyErrorResult](FileShare_PolicyErrorResult.md) **resultFileShare_PolicyErrorResult数组指针。请使用OH_FileShare_ReleasePolicyErrorResult()进行资源释放。unsigned int *resultNumFileShare_PolicyErrorResult数组大小。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)

返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。

 ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因有：1. 参数policies或参数result或参数resultNum为空指针；

 2. 参数policyNum值为0或者超过最大长度(500)；3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。

 ERR_DEVICE_NOT_SUPPORTED 801 - 当前设备类型不支持此接口。

 ERR_PERMISSION_ERROR 201 - 接口权限校验失败。

 ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。

 ERR_EPERM 13900001 - 操作不被允许。

 ERR_OK 0 - 接口调用成功。

#### OH_FileShare_ActivatePermission()

```ets
FileManagement_ErrCode OH_FileShare_ActivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

使能多个已经持久化授权的文件或目录。

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**起始版本：** 12

**参数：**

参数项描述[const FileShare_PolicyInfo](FileShare_PolicyInfo.md) *policies一个指向FileShare_PolicyInfo实例的指针。unsigned int policyNumFileShare_PolicyInfo实例数组的大小。[FileShare_PolicyErrorResult](FileShare_PolicyErrorResult.md) **resultFileShare_PolicyErrorResult数组指针。请使用OH_FileShare_ReleasePolicyErrorResult()进行资源释放。unsigned int *resultNumFileShare_PolicyErrorResult数组大小。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)

返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。

 ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因有：

 1. 参数policies或参数result或参数resultNum为空指针；

 2. 参数policyNum值为0或者超过最大长度(500)；

 3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。

 ERR_DEVICE_NOT_SUPPORTED 801 - 当前设备类型不支持此接口。

 ERR_PERMISSION_ERROR 201 - 接口权限校验失败。

 ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。

 ERR_EPERM 13900001 - 操作不被允许。

 ERR_OK 0 - 接口调用成功。

#### OH_FileShare_DeactivatePermission()

```ets
FileManagement_ErrCode OH_FileShare_DeactivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum)
```

**描述**

取消使能持久化授权过的多个文件或目录。

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**起始版本：** 12

**参数：**

参数项描述[const FileShare_PolicyInfo](FileShare_PolicyInfo.md) *policies一个指向FileShare_PolicyInfo实例的指针。unsigned int policyNumFileShare_PolicyInfo实例数组的大小。[FileShare_PolicyErrorResult](FileShare_PolicyErrorResult.md) **resultFileShare_PolicyErrorResult数组指针。请使用OH_FileShare_ReleasePolicyErrorResult()进行资源释放。unsigned int *resultNumFileShare_PolicyErrorResult数组大小。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)

返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。

 ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因有：

 1. 参数policies或参数result或参数resultNum为空指针；

 2. 参数policyNum值为0或者超过最大长度(500)；

 3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。

 ERR_DEVICE_NOT_SUPPORTED 801 - 当前设备类型不支持此接口。

 ERR_PERMISSION_ERROR 201 - 接口权限校验失败。

 ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。

 ERR_EPERM 13900001 - 操作不被允许。

 ERR_OK 0 - 接口调用成功。

#### OH_FileShare_CheckPersistentPermission()

```ets
FileManagement_ErrCode OH_FileShare_CheckPersistentPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, bool **result, unsigned int *resultNum)
```

**描述**

校验所选择的多个文件或目录URI的持久化授权。

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**起始版本：** 12

**参数：**

参数项描述[const FileShare_PolicyInfo](FileShare_PolicyInfo.md) *policies一个指向FileShare_PolicyInfo实例的指针。unsigned int policyNumFileShare_PolicyInfo实例数组的大小。bool **result授权校验结果指针。请引用头文件malloc.h并使用free()进行资源释放。unsigned int *resultNum校验结果数组的大小。

**返回：**

类型说明[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)

返回FileManagement模块错误码[FileManagement_ErrCode](error_code.h.md#ZH-CN_TOPIC_0000002497445288__filemanagement_errcode)。

 ERR_INVALID_PARAMETER 401 - 输入参数无效。可能的原因有：

 1. 参数policies或参数result或参数resultNum为空指针；

 2. 参数policyNum值为0或者超过最大长度(500)；

 3. 参数policies中携带的uri为空或者length为0或者uri的长度与length不一致。

 ERR_DEVICE_NOT_SUPPORTED 801 - 当前设备类型不支持此接口。

 ERR_PERMISSION_ERROR 201 - 接口权限校验失败。

 ERR_ENOMEM 13900011 - 分配或者拷贝内存失败。

 ERR_EPERM 13900001 - 操作不被允许。可能的原因为policies中携带的所有uri都不符合规范或者uri转换出来的路径不存在。

 ERR_OK 0 - 接口调用成功。

#### OH_FileShare_ReleasePolicyErrorResult()

```ets
void OH_FileShare_ReleasePolicyErrorResult(FileShare_PolicyErrorResult *errorResult, unsigned int resultNum)
```

**描述**

释放FileShare_PolicyErrorResult指针指向的内存资源。

**起始版本：** 12

**参数：**

参数项描述[FileShare_PolicyErrorResult](FileShare_PolicyErrorResult.md) *errorResult一个指向FileShare_PolicyErrorResult实例的指针。unsigned int resultNumFileShare_PolicyErrorResult实例数组的大小。