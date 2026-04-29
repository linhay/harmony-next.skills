# fileGuard (文件分级管控)

文件分级管控服务为企业安全管控类[MDM](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit)应用提供统一企业关键信息资产（KIA）文件的识别和外发管控能力，保证企业数据安全。功能包括扫描全盘目录下的文档，识别KIA文件，并管控KIA文件通过网络发送到非可信网段。

仅供企业安全管控类MDM应用申请权限后使用。

起始版本： 4.0.0(10)

**导入模块**

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
```

**CommonDirScanType**

公共目录扫描类型枚举。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA_ONLY | 0 | 表示媒体库目录。 |
| MEDIA_AND_SANDBOX | 1 | 表示媒体库和沙箱目录。 |

**SecurityLevel**

文件安全等级枚举。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | -1 | 表示文件安全等级不生效。 起始版本： 5.1.1(19) |
| EXTERNAL | 0 | 表示文件安全等级为外部公开。 |
| INTERNAL | 1 | 表示文件安全等级为内部公开。 |
| SECRET | 2 | 表示文件安全等级为秘密。 |
| CONFIDENTIAL | 3 | 表示文件安全等级为机密。 |
| TOP_SECRET | 4 | 表示文件安全等级为绝密。 |

**FilePathInfo**

表示文件路径信息。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| absolutePath | string | 否 | 否 | 表示文件绝对路径。 |
| uri | string | 否 | 否 | 表示文件URI。 |

**FileTagInfo**

表示文件的标签属性信息。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| securityLevel | number | 否 | 否 | 表示文件安全等级，其值参考SecurityLevel枚举类型。 |
| tag | string | 否 | 否 | 表示文件标签信息。 |

**ScanFileCallback**

表示扫描结果回调类。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

**onReceiveFileList**

onReceiveFileList(files: Array<string>): void

文件目录扫描结果回调函数。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 表示扫描文件的绝对路径列表。 |

示例：

```ets
let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
  files.forEach((value: string, index: number) => {
    console.info(`Succeeded in getting file: ${value}.`);
  })
};
```

**onTaskCompleted**

onTaskCompleted(count: number): void

文件目录扫描完成信息获取回调函数。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 表示扫描完成后文件的数量。 |

示例：

```ets
let onTaskCompleted: (count: number) => void = (count: number) => {
  console.info(`Succeeded in getting count: ${count}.`);
};
```

**FileGuard**

FileGuard类提供了文件分级管控相关接口，包括如下功能：文件目录扫描、标注文件扩展属性、下发文件管控策略等。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

**constructor**

constructor()

创建FileGuard对象。

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

示例：

```ets
let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
```

**startFileScanTask**

startFileScanTask(type: CommonDirScanType, callback: ScanFileCallback, batchNum?: number): void

启动公共目录文件扫描任务。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | CommonDirScanType | 是 | 公共目录扫描范围。取值：MEDIA_ONLY | MEDIA_AND_SANDBOX。 |
| callback | ScanFileCallback | 是 | 回调函数，返回的文件列表和扫描结束通知。 |
| batchNum | number | 否 | 每次调用回调函数时返回的文件列表数量。取值在1~200间，如果超出此范围，参数设置无效，按照默认每次调用回调函数返回100个文件，直到扫描结束。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
  console.info(`Succeeded in getting number of files obtained in each callback: ${files.length}.`);
  files.forEach((value: string, index: number) => {
    console.info(`Succeeded in getting file: ${value}.`);
  })
};
let onCompleteScanTask: (count: number) => void = (count: number) => {
  console.info(`Succeeded in getting count: ${count}.`);
};
let scanFileCallback: fileGuard.ScanFileCallback = {
  onReceiveFileList: onReceiveFileList,
  onTaskCompleted: onCompleteScanTask
};
guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA_ONLY, scanFileCallback);
```

**startFileScanTask**

startFileScanTask(path: string, callback: ScanFileCallback, batchNum?: number): void

启动指定目录文件扫描任务。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的目录子集。 |
| callback | ScanFileCallback | 是 | 回调函数，返回的文件列表和扫描结束通知。 |
| batchNum | number | 否 | 每次调用回调函数时返回的文件列表数量。取值在1~200间，如果超出此范围，参数设置无效，按照默认每次调用回调函数返回100个文件，直到扫描结束。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test';
let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
  console.info(`Succeeded in getting number of files obtained in each callback: ${files.length}.`);
  files.forEach((value: string, index: number) => {
    console.info(`Succeeded in getting file: ${value}.`);
  })
};
let onCompleteScanTask: (count: number) => void = (count: number) => {
  console.info(`Succeeded in getting count: ${count}.`);
};
let scanFileCallback: fileGuard.ScanFileCallback = {
  onReceiveFileList: onReceiveFileList,
  onTaskCompleted: onCompleteScanTask
};
guard.startFileScanTask(path, scanFileCallback);
```

**openFile**

openFile(path: string, callback: AsyncCallback<number>): void

打开文件。使用callback异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当打开文件成功，err为undefined，data为获取到的文件描述符，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.openFile(path, (err: BusinessError, fd: number) => {
  if (err) {
    console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
});
```

**openFile**

openFile(path: string): Promise<number>

打开文件。使用Promise异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.openFile(path).then((fd: number) => {
  console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
});
```

**openFileWrite**

openFileWrite(path: string, callback: AsyncCallback<number>): void

只写模式打开文件。使用callback回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 用户的个人数据目录下的绝对路径子集。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当打开文件成功，err为undefined，data为获取到的文件描述符，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.openFileWrite(path, (err: BusinessError, fd: number) => {
  if (err) {
    console.error(`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
});
```

**openFileWrite**

openFileWrite(path: string): Promise<number>

只写模式打开文件。使用Promise异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 用户的个人数据目录下的绝对路径子集。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.openFileWrite(path).then((fd: number) => {
  console.info(`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
});
```

**setFileTag**

setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void

设置文件属性标签。使用callback异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| level | SecurityLevel | 是 | 用于标识文件安全等级（外部公开、内部公开、秘密、机密、绝密），需由开发者设定，并配合queryFileTag接口使用。 |
| tag | string | 是 | 标签名称，使用updatePolicy接口设置自定义标签策略后，根据标签名称进行相应管控。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置文件属性标签成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
let tag: string = 'test';
guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in setting file tag.`);
});
```

**setFileTag**

setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>

设置文件属性标签。使用Promise异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| level | SecurityLevel | 是 | 用于标识文件安全等级（外部公开、内部公开、秘密、机密、绝密），需由开发者设定，并配合queryFileTag接口使用。 |
| tag | string | 是 | 标签名称，使用updatePolicy接口设置自定义标签策略后，根据标签名称进行相应管控。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
let tag: string = 'test';
guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
  console.info(`Succeeded in setting file tag.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
});
```

**queryFileTag**

queryFileTag(path: string, callback: AsyncCallback<FileTagInfo>): void

获取文件属性标签。使用callback异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| callback | AsyncCallback<FileTagInfo> | 是 | 回调函数，返回文件标签信息对象。 回调函数，当异步获取文件属性标签成功，err为undefined，data为获取到的FileTagInfo，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
  if (err) {
    console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in querying file tag.`);
});
```

**queryFileTag**

queryFileTag(path: string): Promise<FileTagInfo>

获取文件属性标签。使用Promise异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<FileTagInfo> | Promise对象，返回文件标签信息对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
  console.info(`Succeeded in querying file tag.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
});
```

**getFileUri**

getFileUri(path: string, callback: AsyncCallback<FilePathInfo>): void

获取文件URI。使用callback异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 用户的个人数据目录下的绝对路径子集。 |
| callback | AsyncCallback<FilePathInfo> | 是 | 回调函数。当获取文件URI成功，err为undefined，data为获取到的FilePathInfo；否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/test/test.txt';
guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
  if (err) {
    console.error(`Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
  }else{
    console.info(`Succeeded in getting file uri.`);
  }
});
```

**getFileUri**

getFileUri(path: string): Promise<FilePathInfo>

获取文件URI。使用Promise异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 用户的个人数据目录下的绝对路径子集。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<FilePathInfo> | Promise对象，返回文件绝对路径和URI。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/test/test.txt';
guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
  console.info(`Succeeded in getting file uri.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
});
```

**deleteFile**

deleteFile(path: string, callback: AsyncCallback<void>): void

删除指定路径下的文件。使用callback异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 用户的个人数据目录下的绝对路径子集。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步删除文件成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.deleteFile(path, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
  }else{
    console.info(`Succeeded in deleting file.`);
  }
});
```

**deleteFile**

deleteFile(path: string): Promise<void>

删除指定路径下的文件。使用Promise异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 用户的个人数据目录下的绝对路径子集。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.deleteFile(path).then(() => {
  console.info(`Succeeded in deleting file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
});
```

**updatePolicy**

updatePolicy(policy: string, callback: AsyncCallback<void>): void

更新安全管控策略。使用callback异步回调。

需要权限： ohos.permission.SET_FILE_GUARD_POLICY

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | string | 是 | 安全管控策略：网络策略、文件策略、蓝牙策略、星闪策略、多用户策略、可信任应用列表和五种自定义标签。 - 网络策略 - net_intercept_toggle：网络拦截管控开关，开启后，将KIA文件通过网络外发到不可信网段会被拦截。0关闭，1开启，默认为1。 - net_reject_cache_time：网络外发拦截管控时间，当成功触发网络外发拦截后，在该管控时间范围内，通过网络进行的任何文件外发操作都会被拦截。正整数，默认为30，单位：秒。 - boundary：默认网段范围，限定默认管控的网段范围，向不在此范围内的ip地址外发文件默认会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。 - netsegment_trustlist：可信任网段，限定可信任的网段范围，外发至该网段内的文件不会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。 - netsegment_blocklist：不可信网段，限定不可信任的网段范围，外发至该网段内的文件会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。 - default_policy：网段管控默认策略，判断在默认网段范围范围内，但不处于可信任网段和不可信任网段范围内的ip是否需要被管控。0不管控，1管控，默认为0。 - netsegment_update_type：网段更新方式，0表示下发策略中的网段信息将覆盖原有策略中的网段信息；1表示在原有网段信息的基础下追加新下发策略中的网段信息，默认为0。 - 文件策略 - usb_intercept_toggle：USB拦截管控开关，开启后，将KIA文件外发到USB设备中会被拦截。0关闭，1开启，默认为0。 - smb_client_intercept_toggle：Samba客户端拦截管控开关，开启后，通过网络邻居外发KIA文件会被拦截。0关闭，1开启，默认为1。从6.0.1(21)版本开始支持此管控策略。 - smb_server_intercept_toggle：Samba服务端拦截管控开关，开启后，通过网络邻居访问KIA文件会被拦截。0关闭，1开启，默认为1。从6.0.1(21)版本开始支持此管控策略。 - new_file_audit_toggle：新建文件审计开关，开启后，会向审计框架上报文件新建的审计事件。0关闭，1开启，默认为0。起始版本：从5.1.1(19)版本开始支持此管控策略。 - kia_variant_toggle：KIA变种开关，开启后，会监控KIA变种事件，可通过注册回调的方式监听并处理相关变种事件。0关闭，1开启，默认为1。从5.0.3(15)版本开始支持此管控策略。 - audit_filter_toggle：审计事件过滤开关，开启后，记录所有被拦截的进程信息；反之，仅记录被拦截的应用信息。0关闭，1开启，默认为0。从5.0.3(15)版本开始支持此管控策略。 - 蓝牙策略 从6.0.1(21)版本开始支持此管控策略。 - bluetooth_intercept_toggle：蓝牙拦截管控开关，开启后，通过蓝牙外发KIA文件会被拦截。字符串列表，蓝牙三种协议，可填入"bt_socket","bt_ble","bt_opp"，默认为空。 - bluetooth_intercept_time：蓝牙外发拦截管控时间，当成功触发蓝牙外发拦截后，在该管控时间范围内，通过蓝牙进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：秒。 - 星闪策略 从6.0.1(21)版本开始支持此管控策略。 - nearlink_intercept_toggle：星闪拦截管控开关，设置后，通过相关星闪协议外发KIA文件会被拦截。字符串列表，星闪二种协议，可填入"nearlink_ssap","nearlink_dataTransfer"，默认为空。 - nearlink_intercept_time：星闪外发拦截管控时间，当成功触发星闪外发拦截后，在该管控时间范围内，通过星闪进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：秒。 - 多用户策略 从5.1.1(19)版本开始支持此管控策略。 - user_id：用户ID，设置用户ID后，本次下发的管控策略范围将仅适用于该user_id对应的用户；若未指定user_id，则采用默认的管控策略。在使用过程中，系统会优先采用用户的专属策略，若无法匹配，则自动采用默认策略。 - 可信任应用列表 从5.0.3(15)版本开始支持此管控策略。 - trust_app_list：可信任应用列表，在可信任应用列表中的应用才可读取KIA文件。字符串列表，元素为appId，默认为空。 - 五种自定义标签 从5.1.1(19)版本开始支持此管控策略。最多支持五种自定义标签管控策略，该策略会自动识别文件扩展属性中包含指定"tag"内容的文件，并对这些文件进行相应管控。 - "tag": 标签名称，用于在setFileTag、setFileCustomTag和unsetFileCustomTag中管控对应标签的文件，默认为空。 - "usb_intercept_toggle"：USB拦截管控开关，默认为0。 - "net_intercept_toggle"：网络拦截管控开关，默认为0。 - "boundary"：默认网段范围。 - "netsegment_trustlist"：可信任网段。 - "netsegment_blocklist"：不可信网段。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步更新安全管控策略成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function updatePolicy() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  let userId: number = await accountManager.getOsAccountLocalId();

  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    '"net_intercept_toggle":1,' +
    '"default_policy":1,' +
    '"net_reject_cache_time":30,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '"netsegment_trustlist":["10.0.0.0-10.255.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
    '"netsegment_update_type": 0,' +
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    `"user_id": ${userId},` +
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag2":{' +
    '   "tag":"confidential",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag3":{' +
    '   "tag":"public",' +
    '   "usb_intercept_toggle":0,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag4":{' +
    '   "tag":"general",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag5":{' +
    '   "tag":"special",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  }' +
    '}';
  guard.updatePolicy(policy, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
    } else {
      console.info(`Succeeded in updating policy.`);
    }
  });
}
```

**updatePolicy**

updatePolicy(policy: string): Promise<void>

更新安全管控策略。使用Promise异步回调。

需要权限： ohos.permission.SET_FILE_GUARD_POLICY

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | string | 是 | 安全管控策略：网络策略、文件策略、蓝牙策略、星闪策略、多用户策略、可信任应用列表和五种自定义标签。 - 网络策略 - net_intercept_toggle：网络拦截管控开关，开启后，将KIA文件通过网络外发到不可信网段会被拦截。0关闭，1开启，默认为1。 - net_reject_cache_time：网络外发拦截管控时间，当成功触发网络外发拦截后，在该管控时间范围内，通过网络进行的任何文件外发操作都会被拦截。正整数，默认为30，单位：秒。 - boundary：默认网段范围，限定默认管控的网段范围，向不在此范围内的ip地址外发文件默认会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。 - netsegment_trustlist：可信任网段，限定可信任的网段范围，外发至该网段内的文件不会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。 - netsegment_blocklist：不可信网段，限定不可信任的网段范围，外发至该网段内的文件会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。 - default_policy：网段管控默认策略，判断在默认网段范围范围内，但不处于可信任网段和不可信任网段范围内的ip是否需要被管控。0不管控，1管控，默认为0。 - netsegment_update_type：网段更新方式，0表示下发策略中的网段信息将覆盖原有策略中的网段信息；1表示在原有网段信息的基础下追加新下发策略中的网段信息，默认为0。 - 文件策略 - usb_intercept_toggle：USB拦截管控开关，开启后，将KIA文件外发到USB设备中会被拦截。0关闭，1开启，默认为0。 - smb_client_intercept_toggle：Samba客户端拦截管控开关，开启后，通过网络邻居外发KIA文件会被拦截。0关闭，1开启，默认为1。从6.0.1(21)版本开始支持此管控策略。 - smb_server_intercept_toggle：Samba服务端拦截管控开关，开启后，通过网络邻居访问KIA文件会被拦截。0关闭，1开启，默认为1。从6.0.1(21)版本开始支持此管控策略。 - new_file_audit_toggle：新建文件审计开关，开启后，会向审计框架上报文件新建的审计事件。0关闭，1开启，默认为0。起始版本：从5.1.1(19)版本开始支持此管控策略。 - kia_variant_toggle：KIA变种开关，开启后，会监控KIA变种事件，可通过注册回调的方式监听并处理相关变种事件。0关闭，1开启，默认为1。从5.0.3(15)版本开始支持此管控策略。 - audit_filter_toggle：审计事件过滤开关，开启后，记录所有被拦截的进程信息；反之，仅记录被拦截的应用信息。0关闭，1开启，默认为0。从5.0.3(15)版本开始支持此管控策略。 - 蓝牙策略 从6.0.1(21)版本开始支持此管控策略。 - bluetooth_intercept_toggle：蓝牙拦截管控开关，开启后，通过蓝牙外发KIA文件会被拦截。字符串列表，蓝牙三种协议，可填入"bt_socket","bt_ble","bt_opp"，默认为空。 - bluetooth_intercept_time：蓝牙外发拦截管控时间，当成功触发蓝牙外发拦截后，在该管控时间范围内，通过蓝牙进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：秒。 - 星闪策略 从6.0.1(21)版本开始支持此管控策略。 - nearlink_intercept_toggle：星闪拦截管控开关，设置后，通过相关星闪协议外发KIA文件会被拦截。字符串列表，星闪二种协议，可填入"nearlink_ssap","nearlink_dataTransfer"，默认为空。 - nearlink_intercept_time：星闪外发拦截管控时间，当成功触发星闪外发拦截后，在该管控时间范围内，通过星闪进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：秒。 - 多用户策略 从5.1.1(19)版本开始支持此管控策略。 - user_id：用户ID，设置用户ID后，本次下发的管控策略范围将仅适用于该user_id对应的用户；若未指定user_id，则采用默认的管控策略。在使用过程中，系统会优先采用用户的专属策略，若无法匹配，则自动采用默认策略。 - 可信任应用列表 从5.0.3(15)版本开始支持此管控策略。 - trust_app_list：可信任应用列表，在可信任应用列表中的应用才可读取KIA文件。字符串列表，元素为appId，默认为空。 - 五种自定义标签 从5.1.1(19)版本开始支持此管控策略。最多支持五种自定义标签管控策略，该策略会自动识别文件扩展属性中包含指定"tag"内容的文件，并对这些文件进行相应管控。 - "tag": 标签名称，用于在setFileTag、setFileCustomTag和unsetFileCustomTag中管控对应标签的文件，默认为空。 - "usb_intercept_toggle"：USB拦截管控开关，默认为0。 - "net_intercept_toggle"：网络拦截管控开关，默认为0。 - "boundary"：默认网段范围。 - "netsegment_trustlist"：可信任网段。 - "netsegment_blocklist"：不可信网段。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function updatePolicy() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  let userId: number = await accountManager.getOsAccountLocalId();

  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    '"net_intercept_toggle":1,' +
    '"default_policy":1,' +
    '"net_reject_cache_time":30,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '"netsegment_trustlist":["10.0.0.0-10.255.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
    '"netsegment_update_type": 0,' +
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    `"user_id": ${userId},` +
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag2":{' +
    '   "tag":"confidential",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag3":{' +
    '   "tag":"public",' +
    '   "usb_intercept_toggle":0,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag4":{' +
    '   "tag":"general",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  },' +
    '"Tag5":{' +
    '   "tag":"special",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
    '  }' +
    '}';
  guard.updatePolicy(policy).then(() => {
    console.info(`Succeeded in updating policy.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

**setKiaFilelist**

setKiaFilelist(filelist: string, callback: AsyncCallback<void>): void

设置KIA文件列表。使用callback异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filelist | string | 是 | kia_filelist：默认路径范围下的KIA文件绝对路径列表，相关文件会被标记为KIA文件。 kia_keyword：受控文件关键字列表，文件名中包含相关关键字的文件会被管控。 kia_suffix：受控文件后缀名列表，文件名包含相关后缀名的文件会被管控。 compress_suffix：压缩文件后缀名列表，只有经过压缩后的文件后缀名在该列表范围内，才会上报压缩变种事件。 kia_update_type：KIA文件更新类型，当type为0时，新增策略将会替换原有策略；当type为1时，会在原有策略的基础上追加新增策略；当type为2时，会在原有策略的基础上删除新的策略，默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置KIA文件列表成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let fileListStr: string =
  '{"kia_filelist":["/data/service/el2/100/hmdfs/account/files/Docs/Documents/1.txt","/data/service/el2/100/hmdfs/account/files/Docs/Documents/2.txt"],' +
    '"kia_keyword":["key1","key2","key3"],' +
    '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
    '"compress_suffix":[".rar", ".zip"],' +
    '"kia_update_type":0}';
guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
  } else {
    console.info(`Succeeded in setting the list of KIA file.`);
  }
});
```

**setKiaFilelist**

setKiaFilelist(filelist: string): Promise<void>

设置KIA文件列表。使用Promise异步回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filelist | string | 是 | kia_filelist：默认路径范围下的KIA文件绝对路径列表，相关文件会被标记为KIA文件。 kia_keyword：受控文件关键字列表，文件名中包含相关关键字的文件会被管控。 kia_suffix：受控文件后缀名列表，文件名包含相关后缀名的文件会被管控。 compress_suffix：压缩文件后缀名列表，只有经过压缩后的文件后缀名在该列表范围内，才会上报压缩变种事件。 kia_update_type：KIA文件更新类型，当type为0时，新增策略将会替换原有策略；当type为1时，会在原有策略的基础上追加新增策略；当type为2时，会在原有策略的基础上删除新的策略，默认为0。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let fileListStr: string =
  '{"kia_filelist":["/data/service/el2/100/hmdfs/account/files/Docs/Documents/1.txt","/data/service/el2/100/hmdfs/account/files/Docs/Documents/2.txt"],' +
    '"kia_keyword":["key1","key2","key3"],' +
    '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
    '"compress_suffix":[".rar", ".zip"],' +
    '"kia_update_type":0}';
guard.setKiaFilelist(fileListStr).then(() => {
  console.info(`Succeeded in setting the list of KIA file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
});
```

**on('kiaCopy')**

on(type: 'kiaCopy', callback: Callback<string>): void

订阅KIA文件拷贝事件。使用callback回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCopy'：固定取值，表示监听KIA文件拷贝事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件拷贝事件。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaCopyCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.on('kiaCopy', onKiaCopyCallback);
} catch (e) {
  console.error(`Failed to listen the kia file copy event. Code: ${e.code}, message: ${e.message}.`);
}
```

**off('kiaCopy')**

off(type: 'kiaCopy', callback?: Callback<string>): void

取消订阅KIA文件拷贝事件。使用callback回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCopy'：固定取值，表示取消监听KIA文件拷贝事件。 |
| callback | Callback<string> | 否 | 回调函数，返回KIA文件拷贝信息。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaCopyCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.off('kiaCopy', offKiaCopyCallback);
} catch (e) {
  console.error(`Failed to cancel listen the KIA file copy event. Code: ${e.code}, message: ${e.message}.`);
}
```

**on('kiaRename')**

on(type: 'kiaRename', callback: Callback<string>): void

订阅KIA文件重命名事件。使用callback回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaRename'：固定取值，表示监听KIA文件重命名事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件重命名事件。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaRenameCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.on('kiaRename', onKiaRenameCallback);
} catch (e) {
  console.error(`Failed to listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.`);
}
```

**off('kiaRename')**

off(type: 'kiaRename', callback?: Callback<string>): void

取消订阅KIA文件重命名事件。使用callback回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaRename'：固定取值，表示取消监听KIA文件重命名事件。 |
| callback | Callback<string> | 否 | 回调函数，返回KIA文件重命名信息。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaRenameCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.off('kiaRename', offKiaRenameCallback);
} catch (e) {
  console.error(`Failed to cancel listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.`);
}
```

**on('kiaCompress')**

on(type: 'kiaCompress', callback: Callback<string>): void

订阅KIA文件压缩事件。使用callback回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCompress'：固定取值，表示监听KIA文件压缩事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件压缩事件。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaCompressCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.on('kiaCompress', onKiaCompressCallback);
} catch (e) {
  console.error(`Failed to listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.`);
}
```

**off('kiaCompress')**

off(type: 'kiaCompress', callback?: Callback<string>): void

取消订阅KIA文件压缩事件。使用callback回调。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCompress'：固定取值，表示取消监听KIA文件压缩事件。 |
| callback | Callback<string> | 否 | 回调函数，返回KIA文件压缩信息。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaCompressCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.off('kiaCompress', offKiaCompressCallback);
} catch (e) {
  console.error(`Failed to cancel listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.`);
}
```

**setKiaWatermarkImage**

setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>

设置KIA文件水印图片。

需要权限： ohos.permission.SET_FILE_GUARD_POLICY

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Uint8Array | 是 | 水印图片。当传入的数组为空时，可取消已设置的水印。 |
| info | string | 是 | 水印附加信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

示例：

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function testSetKiaWaterMarkImage() {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let imagePath: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/1.png';
    let fd: number = await guard.openFile(imagePath);
    let stat: fs.Stat = fs.statSync(fd);
    let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
    fs.readSync(fd, buffer);

    let image: Uint8Array = new Uint8Array(buffer);
    let info: string = new Date().toLocaleString();
    guard.setKiaWatermarkImage(image, info).then(() => {
      console.info(`Succeeded in setting the watermark image for Kia file.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.`);
    })
  } catch (e) {
    console.error(`testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}`);
  }
```

**setFileCustomTag**

setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

设置文件自定义属性标签。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置文件自定义属性标签成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.setFileCustomTag(path, tagList, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
  } else {
    console.info(`Succeeded in setting file custom tag.`);
  }
});
```

**setFileCustomTag**

setFileCustomTag(path: string, tagList: Array<string>): Promise<void>

设置文件自定义属性标签。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.setFileCustomTag(path, tagList).then(() => {
  console.info(`Succeeded in setting file custom tag.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
});
```

**unsetFileCustomTag**

unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

取消文件自定义属性标签。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步取消文件自定义属性标签成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.unsetFileCustomTag(path, tagList, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
  } else {
    console.info(`Succeeded in unsetting file custom tag.`);
  }
});
```

**unsetFileCustomTag**

unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>

取消文件自定义标签。

需要权限： ohos.permission.FILE_GUARD_MANAGER

系统能力： SystemCapability.PCService.FileGuard

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 默认路径范围下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.unsetFileCustomTag(path, tagList).then(() => {
  console.info(`Succeeded in unsetting file custom tag.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
});
```