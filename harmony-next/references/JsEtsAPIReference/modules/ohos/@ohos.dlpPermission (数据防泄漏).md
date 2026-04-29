# @ohos.dlpPermission (数据防泄漏)

数据防泄漏（DLP）是系统提供的系统级的数据防泄漏解决方案，提供跨设备的文件的权限管理、加密存储、授权访问等能力。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- @ohos.dlpPermission归属的Kit已由DataLossPreventionKit变更为DataProtectionKit，建议开发者使用新模块名@kit.DataProtectionKit完成模块导入。如果使用@kit.DataLossPreventionKit导入，仅能调用改名前的接口，无法使用新增接口。

#### 导入模块

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
```

#### dlpPermission.isDLPFile

isDLPFile(fd: number): Promise<boolean>

根据文件的fd，查询该文件是否是DLP文件。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待查询文件的fd（文件描述符）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示是DLP文件，返回false表示非DLP文件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码]([DLP服务错误码](../../errors/DLP服务错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
let file: number | undefined = undefined;
try {
  file = fileIo.openSync(uri).fd;
  let res = dlpPermission.isDLPFile(file);
  console.info('res', res);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
} finally {
  if (file !== undefined) {
    fileIo.closeSync(file);
  }
```

#### dlpPermission.isDLPFile

isDLPFile(fd: number, callback: AsyncCallback<boolean>): void

根据文件的fd，查询该文件是否是DLP文件。使用callback方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待查询文件的fd（文件描述符）。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示是DLP文件，返回false表示非DLP文件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
let file: number | undefined = undefined;
try {
  file = fileIo.openSync(uri).fd;
  dlpPermission.isDLPFile(file, (err, res) => {
    if (err != undefined) {
      console.error('isDLPFile error,', err.code, err.message);
    } else {
      console.info('res', res);
    }
    fileIo.closeSync(file);
  });
} catch (err) {
  console.error('isDLPFile error,', (err as BusinessError).code, (err as BusinessError).message);
  if (file !== undefined) {
    fileIo.closeSync(file);
  }
```

#### dlpPermission.getDLPPermissionInfo

getDLPPermissionInfo(): Promise<DLPPermissionInfo>

查询当前DLP沙箱的权限信息。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DLPPermissionInfo> | Promise对象。返回查询的DLP文件的权限信息，无异常则表明查询成功。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    dlpPermission.isInSandbox().then(async (inSandbox) => { // 是否在沙箱内。
      if (inSandbox) {
        let res: dlpPermission.DLPPermissionInfo = await dlpPermission.getDLPPermissionInfo(); // 获取当前权限信息。
        console.info('res', JSON.stringify(res));
      }
    });
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
  }
```

#### dlpPermission.getDLPPermissionInfo

getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void

查询当前DLP沙箱的权限信息。使用callback方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<DLPPermissionInfo> | 是 | 回调函数。err为undefined时表示查询成功；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.isInSandbox().then((inSandbox) => { // 是否在沙箱内。
    if (inSandbox) {
      dlpPermission.getDLPPermissionInfo((err, res) => {
        if (err != undefined) {
          console.error('getDLPPermissionInfo error', err.code, err.message);
        } else {
          console.info('res', JSON.stringify(res));
        }
      }); // 获取当前权限信息。
    }
  });
} catch (err) {
  console.error('getDLPPermissionInfo error', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.getOriginalFileName

getOriginalFileName(fileName: string): string

获取指定DLP文件名的原始文件名。接口为同步接口。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileName | string | 是 | 指定要查询的文件名。不超过255字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回DLP文件的原始文件名。例如：DLP文件名为test.txt.dlp，则返回的原始文件名为test.txt。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let res = dlpPermission.getOriginalFileName('test.txt.dlp'); // 获取原始文件名。
  console.info('res', res);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.getDLPSuffix

getDLPSuffix(): string

获取DLP文件扩展名。接口为同步接口。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回DLP文件扩展名。例如：原文件"text.txt"，加密后的DLP文件名为"test.txt.dlp"，返回拓展名为".dlp"。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let res = dlpPermission.getDLPSuffix(); // 获取DLP拓展名。
  console.info('res', res);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.on('openDLPFile')

on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void

监听打开DLP文件。在当前应用的沙箱应用打开DLP文件时，通知当前应用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'openDLPFile' | 是 | 监听事件类型。固定值为'openDLPFile'：打开DLP文件事件。 |
| listener | Callback<AccessedDLPFileInfo> | 是 | DLP文件打开事件的回调。在当前应用的沙箱应用打开DLP文件时，通知当前应用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.on('openDLPFile', (info: dlpPermission.AccessedDLPFileInfo) => {
    console.info('openDlpFile event', info.uri, info.lastOpenTime)
  }); // 订阅。
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.off('openDLPFile')

off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void

取消监听打开DLP文件。在当前应用的沙箱应用打开DLP文件时，取消通知当前应用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'openDLPFile' | 是 | 监听事件类型。固定值为'openDLPFile'：打开DLP文件事件。 |
| listener | Callback<AccessedDLPFileInfo> | 否 | DLP文件被打开的事件的回调。在当前应用的沙箱应用打开DLP文件时，取消通知当前应用。默认为空，表示取消该类型事件的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.off('openDLPFile', (info: dlpPermission.AccessedDLPFileInfo) => {
    console.info('openDlpFile event', info.uri, info.lastOpenTime)
  }); // 取消订阅。
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.isInSandbox

isInSandbox(): Promise<boolean>

查询当前应用是否运行在DLP沙箱环境。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前应用运行在沙箱中，返回false表示当前应用不是运行在沙箱中。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let inSandbox = dlpPermission.isInSandbox(); // 是否在沙箱内。
  console.info('res', inSandbox);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.isInSandbox

isInSandbox(callback: AsyncCallback<boolean>): void

查询当前应用是否运行在DLP沙箱环境。使用callback方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。err为undefined时表示查询成功；否则为错误对象。返回true表示当前应用运行在沙箱中，返回false表示当前应用不是运行在沙箱中。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.isInSandbox((err, data) => {
    if (err) {
      console.error('isInSandbox error', err.code, err.message);
    } else {
      console.info('isInSandbox, data', JSON.stringify(data));
    }
  }); // 是否在沙箱内。
} catch (err) {
  console.error('isInSandbox error', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.getDLPSupportedFileTypes

getDLPSupportedFileTypes(): Promise<Array<string>>

查询当前可支持权限设置和校验的文件扩展名类型列表。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象。返回当前可支持权限设置和校验的文件扩展名类型列表。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let res = dlpPermission.getDLPSupportedFileTypes(); // 获取支持DLP的文件类型。
  console.info('res', JSON.stringify(res));
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.getDLPSupportedFileTypes

getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void

查询当前可支持权限设置和校验的文件扩展名类型列表。使用callback方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数。err为undefined时表示查询成功；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getDLPSupportedFileTypes((err, res) => {
    if (err != undefined) {
      console.error('getDLPSupportedFileTypes error', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // 获取支持DLP的文件类型。
} catch (err) {
  console.error('getDLPSupportedFileTypes error', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.setRetentionState

setRetentionState(docUris: Array<string>): Promise<void>

打开DLP文件时自动安装沙箱，关闭DLP文件时自动卸载沙箱。设置沙箱保留状态时DLP文件关闭时自动卸载暂时失效。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| docUris | Array<string> | 是 | 表示需要设置保留状态的文件uri列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
  try {
    let inSandbox = await dlpPermission.isInSandbox(); // 是否在沙箱内。
    if (inSandbox) {
      dlpPermission.setRetentionState([uri]); // 设置沙箱保留。
    }
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
  }
```

#### dlpPermission.setRetentionState

setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void

打开DLP文件时自动安装沙箱，关闭DLP文件时自动卸载沙箱。设置沙箱保留状态时DLP文件关闭时自动卸载暂时失效。使用callback方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| docUris | Array<string> | 是 | 表示需要设置保留状态的文件uri列表。Array不限长度，每个string不超过4095字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数。err为undefined时表示设置成功；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
try {
  dlpPermission.setRetentionState([uri], (err, res) => {
    if (err != undefined) {
      console.error('setRetentionState error,', err.code, err.message);
    } else {
      console.info('setRetentionState success');
      console.info('res', JSON.stringify(res));
    }
  }); // 设置沙箱保留。
} catch (err) {
  console.error('setRetentionState error,', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.cancelRetentionState

cancelRetentionState(docUris: Array<string>): Promise<void>

取消沙箱保留状态即恢复DLP文件关闭时自动卸载沙箱策略。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| docUris | Array<string> | 是 | 表示需要设置保留状态的文件uri列表。Array不限长度，每个string不超过4095字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
try {
  dlpPermission.cancelRetentionState([uri]); // 取消沙箱保留。
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.cancelRetentionState

cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void

取消沙箱保留状态即恢复DLP文件关闭时自动卸载沙箱策略。使用callback方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| docUris | Array<string> | 是 | 表示需要设置保留状态的文件uri列表。Array不限长度，每个string不超过4095字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数。err为undefined时表示设置成功；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
try {
  dlpPermission.cancelRetentionState([uri], (err, res) => {
    if (err != undefined) {
      console.error('cancelRetentionState error,', err.code, err.message);
    } else {
      console.info('cancelRetentionState success');
    }
  }); // 取消沙箱保留。
} catch (err) {
  console.error('cancelRetentionState error,', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.getRetentionSandboxList

getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>

查询指定应用的保留沙箱信息列表。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 否 | 指定应用包名。默认为空，查询当前应用的保留沙箱信息列表。最小7字节，最大128字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<RetentionSandboxInfo>> | Promise对象。返回查询的沙箱信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res: Array<dlpPermission.RetentionSandboxInfo> = await dlpPermission.getRetentionSandboxList(); // 获取沙箱保留列表。
    console.info('res', JSON.stringify(res))
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
  }
```

#### dlpPermission.getRetentionSandboxList

getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void

查询指定应用的保留沙箱信息列表。使用callback异步回调。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 指定应用包名。最小7字节，最大128字节。 |
| callback | AsyncCallback<Array<RetentionSandboxInfo>> | 是 | 回调函数。err为undefined时表示查询成功；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getRetentionSandboxList("bundleName", (err, res) => {
    if (err != undefined) {
      console.error('getRetentionSandboxList error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // 获取沙箱保留列表。
} catch (err) {
  console.error('getRetentionSandboxList error,', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.getRetentionSandboxList

getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void

查询当前应用的保留沙箱信息列表。使用callback异步回调。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<RetentionSandboxInfo>> | 是 | 回调函数。err为undefined时表示查询成功；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getRetentionSandboxList((err, res) => {
    if (err != undefined) {
      console.error('getRetentionSandboxList error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // 获取沙箱保留列表。
} catch (err) {
  console.error('getRetentionSandboxList error,', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.getDLPFileAccessRecords

getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>

查询最近访问的DLP文件列表。使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<AccessedDLPFileInfo>> | Promise对象。返回最近访问的DLP文件列表。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res: Array<dlpPermission.AccessedDLPFileInfo> = await dlpPermission.getDLPFileAccessRecords(); // 获取DLP访问列表。
    console.info('res', JSON.stringify(res))
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
  }
```

#### dlpPermission.getDLPFileAccessRecords

getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void

查询最近访问的DLP文件列表。使用callback方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<AccessedDLPFileInfo>> | 是 | 回调函数。err为undefined时表示查询成功；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getDLPFileAccessRecords((err, res) => {
    if (err != undefined) {
      console.error('getDLPFileAccessRecords error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // 获取DLP访问列表。
} catch (err) {
  console.error('getDLPFileAccessRecords error,', (err as BusinessError).code, (err as BusinessError).message);
}
```

#### dlpPermission.startDLPManagerForResult11+

startDLPManagerForResult(context: [common.UIAbilityContext](../../topics/misc/UIAbilityContext.md), want: Want): Promise<DLPManagerResult>

在当前UIAbility界面以无边框形式打开DLP权限管理应用。使用Promise方式异步返回结果。


该接口仅支持域账号调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](../../topics/misc/UIAbilityContext.md) | 是 | 当前窗口UIAbility上下文。 |
| want | Want | 是 | 请求对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DLPManagerResult> | Promise对象。打开DLP权限管理应用并退出后的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |
| 19100016 | The uri field is missing in the want parameter. |
| 19100017 | The displayName field is missing in the want parameter. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { common, Want } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

try {
  let context = new UIContext().getHostContext() as common.UIAbilityContext; // 获取当前UIAbilityContext。
  let want: Want = {
    "uri": "file://docs/storage/Users/currentUser/Desktop/1.txt",
    "parameters": {
      "displayName": "1.txt"
    }
  }; // 请求参数。
  dlpPermission.startDLPManagerForResult(context, want).then((res) => {
    console.info('res.resultCode', res.resultCode);
    console.info('res.want', JSON.stringify(res.want));
  }); // 打开DLP权限管理应用。
} catch (err) {
  console.error('error', err.code, err.message); // 失败报错。
}
```

#### dlpPermission.setSandboxAppConfig11+

setSandboxAppConfig(configInfo: string): Promise<void>

设置沙箱应用配置信息，使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configInfo | string | 是 | 沙箱应用配置信息。长度小于4MB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |
| 19100018 | The application is not authorized. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.setSandboxAppConfig('configInfo'); // 设置沙箱应用配置信息。
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.cleanSandboxAppConfig11+

cleanSandboxAppConfig(): Promise<void>

清理沙箱应用配置信息，使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |
| 19100018 | The application is not authorized. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.cleanSandboxAppConfig(); // 清理沙箱应用配置信息。
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
}
```

#### dlpPermission.getSandboxAppConfig11+

getSandboxAppConfig(): Promise<string>

获取沙箱应用配置信息，使用Promise方式异步返回结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回沙箱应用配置信息。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |
| 19100018 | The application is not authorized. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res = await dlpPermission.getSandboxAppConfig() // 获取沙箱应用配置信息。
    console.info('res', JSON.stringify(res));
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
  }
```

#### dlpPermission.isDLPFeatureProvided12+

isDLPFeatureProvided(): Promise<boolean>

查询当前系统是否提供加密保护特性，使用Promise方式异步返回结果。


该接口由[MDM](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro)配置使能，且使能场景为企业设备。其他设备（如消费者终端设备）无需关注该接口，如若调用该接口，则返回值为false。

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前系统提供加密保护特性，返回false表示不提供加密保护特性。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19100011 | The system ability works abnormally. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

dlpPermission.isDLPFeatureProvided().then((res) => {
  console.info('res', JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // 失败报错。
});
```

#### dlpPermission.setEnterprisePolicy21+

setEnterprisePolicy(policy: EnterprisePolicy): void

设置企业应用防护策略。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | EnterprisePolicy | 是 | 待设置的企业应用防护策略。 |

**错误码：**

以下错误码的详细介绍请参见[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |
| 19100021 | Failed to set the enterprise policy. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';

interface Attribute {
  attributeId: string;
  attributeValues: Array<string>;
  valueType: number;
  opt: number;
}

interface Rule {
  ruleId: string;
  attributes: Array<Attribute>;
}

interface Policy {
  rules: Array<Rule>;
  policyId: string;
  ruleConflictAlg: number;
}

try {
  let attributeValues: Array<string> = [ '1' ];
  let attribute: Attribute = {
    attributeId: 'DeviceHealthyStatus',
    attributeValues: attributeValues,
    valueType: 0,
    opt: 2
  }; // 属性信息。
  let rule: Rule = {
    ruleId: 'ruleId',
    attributes: [ attribute ]
  }; // 规则。
  let policy: Policy = {
    rules: [ rule ],
    policyId: 'policyId',
    ruleConflictAlg: 0
  }; // 策略。
  let enterprisePolicy: dlpPermission.EnterprisePolicy = {
    policyString: JSON.stringify(policy)
  };
  dlpPermission.setEnterprisePolicy(enterprisePolicy);
  console.info('set enterprise policy success');
} catch (err) {
  console.error('error:' + err.code + err.message); // 失败报错。
}
```

#### ActionFlagType

可以对DLP文件进行的操作类型枚举。例如：DLP沙箱应用可以根据是否具有操作权限，对其按钮进行置灰。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION_VIEW | 0x00000001 | 表示文件的查看权限。 |
| ACTION_SAVE | 0x00000002 | 表示文件的保存权限。 |
| ACTION_SAVE_AS | 0x00000004 | 表示文件的另存为权限。 |
| ACTION_EDIT | 0x00000008 | 表示文件的编辑权限。 |
| ACTION_SCREEN_CAPTURE | 0x00000010 | 表示文件的截屏权限。 |
| ACTION_SCREEN_SHARE | 0x00000020 | 表示文件的共享屏幕权限。 |
| ACTION_SCREEN_RECORD | 0x00000040 | 表示文件的录屏权限。 |
| ACTION_COPY | 0x00000080 | 表示文件的复制权限。 |
| ACTION_PRINT | 0x00000100 | 表示文件的打印权限。 |
| ACTION_EXPORT | 0x00000200 | 表示文件的导出权限。 |
| ACTION_PERMISSION_CHANGE | 0x00000400 | 表示文件的修改文件权限。 |

#### DLPFileAccess

DLP文件授权类型的枚举。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_PERMISSION | 0 | 表示无文件权限。 |
| READ_ONLY | 1 | 表示文件的只读权限。 |
| CONTENT_EDIT | 2 | 表示文件的编辑权限。 |
| FULL_CONTROL | 3 | 表示文件的完全控制权限。 |

#### DLPPermissionInfo

表示DLP文件的权限信息。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dlpFileAccess | DLPFileAccess | 否 | 否 | 表示DLP文件针对用户的授权类型，例如：只读。 |
| flags | number | 否 | 否 | 表示DLP文件的详细操作权限，是不同ActionFlagType的组合。 |

#### AccessedDLPFileInfo

表示被打开的DLP文件的信息。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 表示DLP文件的uri。不超过4095字节。 |
| lastOpenTime | number | 否 | 否 | 表示DLP文件最近打开时间。 |

#### DLPManagerResult11+

表示打开DLP权限管理应用的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | number | 否 | 否 | 表示打开DLP权限管理应用并退出后返回的结果码。 |
| want | Want | 否 | 否 | 表示打开DLP权限管理应用并退出后返回的数据。 |

#### RetentionSandboxInfo

保留沙箱的沙箱信息。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appIndex | number | 否 | 否 | 表示DLP沙箱应用索引。 |
| bundleName | string | 否 | 否 | 表示应用包名。最小7字节，最大128字节。 |
| docUris | Array<string> | 否 | 否 | 表示DLP文件的URI列表。Array不限长度，每个string不超过4095字节。 |

#### EnterprisePolicy21+

表示企业定制策略。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| policyString | string | 否 | 否 | 表示企业定制策略的json字符串。长度不超过4M（单位：兆）。 |

#### dlpPermission.generateDlpFileForEnterprise21+

generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>

获取DLPFile管理对象。使用Promise异步回调。


该接口仅支持企业账号调用，需要企业自行搭建企业账号服务器配套使用。使用该接口可以将明文文件加密生成权限受控文件，由企业服务器管控账号是否有权限解密该文件。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| plaintextFd | number | 是 | 明文文件的文件描述符。 |
| dlpFd | number | 是 | 加密文件的文件描述符。 |
| property | DLPProperty | 是 | DLP文件通用策略。 |
| customProperty | CustomProperty | 是 | 企业定制策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |
| 19100005 | Credential authentication server error. |
| 19100009 | Failed to operate the DLP file. |
| 19100011 | The system ability works abnormally. |
| 19100014 | Account not logged in. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction(plainFilePath: string, dlpFilePath: string) {
  let plaintextFd: number | undefined = undefined;
  let dlpFd: number | undefined = undefined;
  try {
    plaintextFd = fileIo.openSync(plainFilePath, fileIo.OpenMode.READ_ONLY).fd;
    dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).fd;
    let dlpProperty: dlpPermission.DLPProperty = {
      ownerAccount: 'zhangsan',
      ownerAccountType: dlpPermission.AccountType.DOMAIN_ACCOUNT,
      authUserList: [],
      contactAccount: 'zhangsan',
      offlineAccess: true,
      ownerAccountID: 'xxxxxxx',
      everyoneAccessList: []
    };
    let customProperty: dlpPermission.CustomProperty = {
      enterprise: 'customProperty'
    };
    await dlpPermission.generateDlpFileForEnterprise(plaintextFd, dlpFd, dlpProperty, customProperty);
    console.info('Successfully generate DLP file for enterprise.');
  } catch(err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message);
  } finally {
    if (dlpFd) {
      fileIo.closeSync(dlpFd);
    }
    if (plaintextFd) {
      fileIo.closeSync(plaintextFd);
    }
```

#### dlpPermission.decryptDlpFile21+

decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>

将DLP文件解密生成明文文件。使用Promise异步回调。


该接口仅支持企业账号调用，需要企业自行搭建企业账号服务器配套使用。由企业服务器管控账号是否有权限解密DLP文件。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dlpFd | number | 是 | 待解密文件的fd。 |
| plaintextFd | number | 是 | 目标解密文件的fd。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |
| 19100005 | Credential authentication server error. |
| 19100008 | The file is not a DLP file. |
| 19100009 | Failed to operate the DLP file. |
| 19100011 | The system ability works abnormally. |
| 19100013 | The user does not have the permission. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction(plainFilePath: string, dlpFilePath: string) {
  let plaintextFd: number | undefined = undefined;
  let dlpFd: number | undefined = undefined;
  try {
    plaintextFd = fileIo.openSync(plainFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).fd;
    dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ_ONLY).fd;
    await dlpPermission.decryptDlpFile(dlpFd, plaintextFd);
    console.info('Successfully decrypt DLP file.');
  } catch(err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message);
  } finally {
    if (dlpFd) {
      fileIo.closeSync(dlpFd);
    }
    if (plaintextFd) {
      fileIo.closeSync(plaintextFd);
    }
```

#### dlpPermission.queryDlpPolicy21+

queryDlpPolicy(dlpFd: number): Promise<string>

在DLP文件中解析文件头，获取DLP明文策略。使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dlpFd | number | 是 | 待解密文件的fd。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回当前DLP策略的json字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |
| 19100005 | Credential authentication server error. |
| 19100008 | The file is not a DLP file. |
| 19100009 | Failed to operate the DLP file. |
| 19100011 | The system ability works abnormally. |
| 19100013 | The user does not have the permission. |

**示例：**

```ets
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction(dlpFilePath: string) {
  let dlpFd : number | undefined = undefined;
  try {
    dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ_ONLY).fd;
    let policy: string = await dlpPermission.queryDlpPolicy(dlpFd);
    console.info('DLP policy:' + policy);
  } catch(err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message);
  } finally {
    if (dlpFd) {
      fileIo.closeSync(dlpFd);
    }
```

#### ActionType21+

表示在文件设定的权限时间到期后所执行的动作枚举，默认为NOT_OPEN。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT_OPEN | 0 | 表示超过权限管控时间后，用户无权限打开DLP文件。 |
| OPEN | 1 | 表示超过权限管控时间后，登录账号的用户拥有编辑权限。 |

#### AccountType21+

表示授权账号类型的枚举。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLOUD_ACCOUNT | 1 | 表示云账号。 |
| DOMAIN_ACCOUNT | 2 | 表示域账号。 |
| ENTERPRISE_ACCOUNT | 4 | 表示企业账号。 |

#### CustomProperty21+

表示自定义策略。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enterprise | string | 否 | 否 | 表示企业定制策略的json字符串。长度不超过4M（单位：兆）。 |

#### DLPProperty21+

表示授权相关信息。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ownerAccount | string | 否 | 否 | 表示权限设置者账号。不超过255字节。 |
| ownerAccountID | string | 否 | 否 | 表示权限设置者账号的ID。不超过255字节。 |
| ownerAccountType | AccountType | 否 | 否 | 表示权限设置者账号类型。 |
| authUserList | Array<AuthUser> | 否 | 是 | 表示授权用户列表，默认为空。 |
| contactAccount | string | 否 | 否 | 表示联系人账号。不超过255字节。 |
| offlineAccess | boolean | 否 | 否 | 表示是否是离线打开。true表示允许离线打开，false表示不可离线打开。 |
| everyoneAccessList | Array<DLPFileAccess> | 否 | 是 | 表示授予所有人的权限，默认为空。 |
| expireTime | number | 否 | 是 | 表示文件权限到期时间戳，默认为空。 |
| actionUponExpiry | ActionType | 否 | 是 | 表示到期后文件是否允许打开（打开后拥有编辑权限），仅在expireTime不为空时生效。 |
| fileId | string | 否 | 是 | 表示文件的标识。不超过255字节。 |
| allowedOpenCount | number | 否 | 是 | 表示允许打开的次数。 |
| waterMarkConfig23+ | boolean | 否 | 是 | 表示是否要求添加水印。true表示要求添加水印，false表示不要求添加水印。 |
| countdown23+ | number | 否 | 是 | 表示文件可被查看的有效时间，超时后打开的文件将自动关闭，单位：s。 模型约束：此接口仅可在Stage模型下使用。 |

#### AuthUser21+

表示授权用户数据。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authAccount | string | 否 | 否 | 表示被授权用户账号。不超过255字节。 |
| authAccountType | AccountType | 否 | 否 | 表示被授权用户账号类型。 |
| dlpFileAccess | DLPFileAccess | 否 | 否 | 表示被授予的权限。 |
| permExpiryTime | number | 否 | 否 | 表示授权到期时间。 |

#### DlpConnPlugin21+

被用于registerPlugin接口中，将回调能力注册到SA（System Ability）中。


[registerPlugin](#ZH-CN_TOPIC_0000002522241354__registerplugin21)接口的参数需要继承该接口，[connectServer](#ZH-CN_TOPIC_0000002522241354__connectserver21)由SA（System Ability）侧调用，通过callback进行回传参数。

#### connectServer21+

connectServer(requestId: string, requestData: string, callback: Callback<string>): void

该函数提供给SA（System Ability）侧调用，待该函数处理完连云能力后，通过callback调用回SA（System Ability）中。

connectServer接口代表系统能力侧向前端通信的一次调用。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | string | 是 | SA（System Ability）侧传递的本次请求的标识。 |
| requestData | string | 是 | SA（System Ability）侧传递的数据。 |
| callback | Callback<string> | 是 | SA（System Ability）侧传递的接口，用于回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 19100011 | The system ability works abnormally. |

#### DlpConnManager21+

用于调用registerPlugin和unregisterPlugin接口，将回调能力在SA（System Ability）中注册/注销。

registerPlugin接口将回调能力注册进SA（System Ability），而unregisterPlugin接口将回调能力从SA（System Ability）中注销。

#### constructor21+

constructor()

[DlpConnManager](#ZH-CN_TOPIC_0000002522241354__dlpconnmanager21) 实例化时的构造函数。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

#### registerPlugin21+

static registerPlugin(plugin: DlpConnPlugin): number

该接口提供将回调注册到SA（System Ability）侧的功能。

registerPlugin将plugin注册到SA（System Ability）侧，待SA（System Ability）调用。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| plugin | DlpConnPlugin | 是 | 代表回调能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 注册结果，代表该回调的id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |

#### unregisterPlugin21+

static unregisterPlugin(): void

提供将回调从SA（System Ability）侧注销的能力。

unregisterPlugin将plugin从SA（System Ability）侧注销注册。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码](DLP服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |