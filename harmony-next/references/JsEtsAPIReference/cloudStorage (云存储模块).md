# cloudStorage (云存储模块)

本模块提供使用云存储对文件进行上传、下载、查询和删除等操作的能力。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
```

#### bucket

bucket(name?: string): StorageBucket

初始化云存储实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

name

string

否

存储实例名称。格式受云侧约束，只允许输入小写字母、数字、'-'，以字母或数字开头和结尾，长度为9-63个字符，且不能连续输入两个及以上'-'。

缺省时，将启动异步任务查询云侧默认实例。

非缺省时，请确保当前云侧存在该存储实例，否则后续操作将出现查询存储实例错误。

**返回值****：**

类型

说明

[StorageBucket](#section10732104881420)

云存储实例。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

401

Parameter error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';

let bucket1: cloudStorage.StorageBucket = cloudStorage.bucket(); // name缺省，将启动异步任务查询云侧默认实例

/**
 * 指定云存储实例名称为'mybucket-duaf5'
 * 'mybucket'是创建云存储实例时用户输入的存储实例名称，'duaf5'是创建云存储实例时生成的随机字符串，通过符号'-'连接
 */
let bucket2: cloudStorage.StorageBucket = cloudStorage.bucket('mybucket-duaf5');
```

#### StorageBucket

云存储的实例，提供云存储的上传、下载等相关能力，通过[bucket](#section1286815320203)初始化。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

#### uploadFile

uploadFile(context: common.BaseContext, parameters: UploadParams): Promise<request.agent.Task>

上传指定文件至云侧。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

context

common.[BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext)

是

应用上下文。

parameters

[UploadParams](#section2941124514298)

是

上传相关参数。

**返回值****：**

类型

说明

Promise<[request.agent.Task](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagenttask10)>

Promise对象，返回上传任务。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI上下文
bucket.uploadFile(context, {  // context表示应用上下文
  localPath: cacheFile,       // 本地文件路径（context.cacheDir目录下的文件路径）
  cloudPath: path             // 云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名
}).then((task: request.agent.Task) => {
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', `on progress ${JSON.stringify(progress)}`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', `on completed ${JSON.stringify(progress)}`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', `on failed ${JSON.stringify(progress)}`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', `on response ${JSON.stringify(response)}`);
  });

  // start task
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', `Failed to start a file upload task, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag', `Succeeded in starting a file upload task.`);
    }
  });
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to upload file, code: ${err.code}, message: ${err.message}`);
})
```

#### uploadFile

uploadFile(context: common.BaseContext, parameters: UploadParams, callback: AsyncCallback<request.agent.Task>): void

上传指定文件至云侧。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

context

common.[BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext)

是

应用上下文。

parameters

[UploadParams](#section2941124514298)

是

上传相关参数。

callback

AsyncCallback<[request.agent.Task](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagenttask10)>

是

回调函数。当上传文件成功，err为undefined，data为获取到的request.agent.Task；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI上下文
bucket.uploadFile(context, {  // context表示应用上下文
  localPath: cacheFile,       // 本地文件路径（context.cacheDir目录下的文件路径）
  cloudPath: path             // 云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名
}, (err: BusinessError, task: request.agent.Task) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to upload file, code: ${err.code}, message: ${err.message}`);
    return;
  }
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', `on progress ${JSON.stringify(progress)}`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', `on completed ${JSON.stringify(progress)}`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', `on failed ${JSON.stringify(progress)}`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', `on response ${JSON.stringify(response)}`);
  });

  // start task
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', `Failed to start a file upload task, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag', `Succeeded in starting a file upload task.`);
    }
  });
});
```

#### downloadFile

downloadFile(context: common.BaseContext, parameters: DownloadParams): Promise<request.agent.Task>

下载云侧文件至本地。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

context

common.[BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext)

是

应用上下文。

parameters

[DownloadParams](#section14137913019)

是

下载相关参数。

**返回值****：**

类型

说明

Promise<[request.agent.Task](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagenttask10)>

Promise对象，返回下载任务。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI上下文
bucket.downloadFile(context, {  // context表示应用上下文
  cloudPath: path,              // 云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名
  localPath: cacheFile,         // 保存至本地文件路径（context.cacheDir目录下的文件路径）
}).then((task: request.agent.Task) => {
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', `on progress ${JSON.stringify(progress)}`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', `on completed ${JSON.stringify(progress)}`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', `on failed ${JSON.stringify(progress)}`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', `on response ${JSON.stringify(response)}`);
  });

  // start task
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag',
        `Failed to start a file download task, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag', `Succeeded in starting a file download task.`);
    }
  });
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to download file, code: ${err.code}, message: ${err.message}`);
})
```

#### downloadFile

downloadFile(context: common.BaseContext, parameters: DownloadParams, callback: AsyncCallback<request.agent.Task>): void

下载云侧文件至本地。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

context

common.[BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext)

是

应用上下文。

parameters

[DownloadParams](#section14137913019)

是

下载相关参数。

callback

AsyncCallback<[request.agent.Task](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagenttask10)>

是

回调函数。当下载文件成功，err为undefined，data为获取到的request.agent.Task；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI上下文
bucket.downloadFile(context, {  // context表示应用上下文
  cloudPath: path,              // 云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名
  localPath: cacheFile,         // 保存至本地文件路径（context.cacheDir目录下的文件路径）
}, (err: BusinessError, task: request.agent.Task) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to download file, code: ${err.code}, message: ${err.message}`);
    return;
  }
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', `on progress ${JSON.stringify(progress)}`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', `on completed ${JSON.stringify(progress)}`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', `on failed ${JSON.stringify(progress)}`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', `on response ${JSON.stringify(response)}`);
  });

  // start task
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag',
        `Failed to start a file download task, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag', `Succeeded in starting a file download task.`);
    }
  });
});
```

#### getDownloadURL

getDownloadURL(cloudPath: string): Promise<string>

获取云侧文件下载地址。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

**返回值****：**

类型

说明

Promise<string>

Promise对象，返回云侧文件下载地址。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath是云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名
bucket.getDownloadURL('cloudPath').then((downloadURL: string) => {
  hilog.info(0x0000, 'testTag', `Succeeded in getting download URL: ${downloadURL}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to get download URL, code: ${err.code}, message: ${err.message}`);
})
```

#### getDownloadURL

getDownloadURL(cloudPath: string, callback: AsyncCallback<string>): void

获取云侧文件下载地址。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

callback

AsyncCallback<string>

是

回调函数，返回云侧文件下载地址。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath是云侧文件路径
bucket.getDownloadURL('cloudPath', (err: BusinessError, downloadURL: string) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to get download URL, code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in getting download URL: ${downloadURL}`);
  }
});
```

#### deleteFile

deleteFile(cloudPath: string): Promise<void>

删除云侧文件。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

**返回值****：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名。
bucket.deleteFile('cloudPath').then(() => {
  hilog.info(0x0000, 'testTag', `Succeeded in deleting file.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to delete file, code: ${err.code}, message: ${err.message}`);
})
```

#### deleteFile

deleteFile(cloudPath: string, callback: AsyncCallback<void>): void

删除云侧文件。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

callback

AsyncCallback<void>

是

回调函数。当删除云侧文件成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath是云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名。
bucket.deleteFile('cloudPath', (err: BusinessError) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to delete file, Code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in deleting file.`);
  }
});
```

#### list

list(cloudPath: string, options?: ListOptions): Promise<ListResults>

获取云侧文件列表。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。

传入''（空字符串）表示获取云侧根路径下的文件列表；传入'some_directory/'表示获取指定文件夹some_directory下的文件列表。

options

[ListOptions](#section7984102813013)

否

列举操作的相关参数。

**返回值****：**

类型

说明

Promise<[ListResults](#section181654510303)>

Promise对象，返回列举操作的结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// 获取云侧根路径下的文件列表
bucket.list('').then((result: cloudStorage.ListResults) => {
  hilog.info(0x0000, 'testTag', `Succeeded in listing files, result: ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to list files, code: ${err.code}, message: ${err.message}`);
})

// 获取指定文件夹some_directory下的文件列表
bucket.list('some_directory/').then((result: cloudStorage.ListResults) => {
  hilog.info(0x0000, 'testTag', `Succeeded in listing files, result: ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to list files, code: ${err.code}, message: ${err.message}`);
})
```

#### list

list(cloudPath: string, options: ListOptions, callback: AsyncCallback<ListResults>): void

获取云侧文件列表。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。

传入''（空字符串）表示获取云侧根路径下的文件列表；传入'some_directory/'表示获取指定文件夹some_directory下的文件列表。

options

[ListOptions](#section7984102813013)

是

列举操作的相关参数。

callback

AsyncCallback<[ListResults](#section181654510303)>

是

回调函数。当获取云侧文件列表成功，err为undefined，data为获取到的ListResults；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// 获取云侧根路径下的文件列表
bucket.list('', { maxResults: 10, pageMarker: 'test' }, (err: BusinessError, result: cloudStorage.ListResults) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to list files, code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in listing files, result: ${JSON.stringify(result)}`);
  }
});

// 获取指定文件夹some_directory下的文件列表
bucket.list('some_directory/', {}, (err: BusinessError, result: cloudStorage.ListResults) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to list files, code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in listing files, result: ${JSON.stringify(result)}`);
  }
});
```

#### getMetadata

getMetadata(cloudPath: string): Promise<Metadata>

获取云侧文件的元数据。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

**返回值****：**

类型

说明

Promise<[Metadata](#section3472335144212)>

Promise对象，返回云侧文件的元数据信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath是云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名。
bucket.getMetadata('cloudPath').then((data: cloudStorage.Metadata) => {
  hilog.info(0x0000, 'testTag', `Succeeded in getting metadata: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to get metadata, code: ${err.code}, message: ${err.message}`);
})
```

#### getMetadata

getMetadata(cloudPath: string, callback: AsyncCallback<Metadata>): void

获取云侧文件的元数据。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

callback

AsyncCallback<[Metadata](#section3472335144212)>

是

回调函数。当获取云侧文件的元数据成功，err为undefined，data为获取到的Metadata；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath是云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名。
bucket.getMetadata('cloudPath', (err: BusinessError, data: cloudStorage.Metadata) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to get metadata, code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in getting metadata: ${JSON.stringify(data)}`);
  }
});
```

#### setMetadata

setMetadata(cloudPath: string, metadata: MetadataUpdatable): Promise<Metadata>

设置云侧文件的元数据。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

metadata

[MetadataUpdatable](#section1122119164218)

是

可更新参数的元数据信息。

**返回值****：**

类型

说明

Promise<[Metadata](#section3472335144212)>

Promise对象，返回云侧文件更新后的完整元数据信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath是云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名。
bucket.setMetadata('cloudPath', {
  customMetadata: {
    key1: "value1",
    key2: "value2"
  }
}).then((data: cloudStorage.Metadata) => {
  hilog.info(0x0000, 'testTag', `Succeeded in setting metadata: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to set metadata, code: ${err.code}, message: ${err.message}`);
})
```

#### setMetadata

setMetadata(cloudPath: string, metadata: MetadataUpdatable, callback: AsyncCallback<Metadata>): void

设置云侧文件的元数据。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

cloudPath

string

是

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

metadata

[MetadataUpdatable](#section1122119164218)

是

可更新参数的元数据信息。

callback

AsyncCallback<[Metadata](#section3472335144212)>

是

回调函数。当设置云侧文件的元数据成功，err为undefined，data为设置的Metadata；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008220001

Network connection error.

1008220009

Client internal error.

1008221001

Server error.

**示例****：**

```ets
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// cloudPath是云侧文件路径，支持传入“文件目录/文件名”，或仅传入文件名。
bucket.setMetadata('cloudPath', {
  customMetadata: {
    key1: "value1",
    key2: "value2"
  }
}, (err: BusinessError, data: cloudStorage.Metadata) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to set metadata, code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in setting metadata: ${JSON.stringify(data)}`);
  }
});
```

#### UploadParams

上传相关参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力： **SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

localPath

string

否

否

本地文件路径，根路径为cache目录。

cloudPath

string

否

否

云侧文件路径，上传成功后，可以使用该路径进行其他操作。

metadata

[MetadataUpdatable](#section1122119164218)

否

是

文件元数据信息。

mode

[request.agent.Mode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagentmode10)

否

是

上传任务类型，前端任务在应用切换到后台一段时间后失败/暂停；后台任务不受影响。默认为request.agent.Mode.BACKGROUND。

- request.agent.Mode.BACKGROUND：后台任务。
- request.agent.Mode.FOREGROUND：前端任务。

network

[request.agent.Network](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagentnetwork10)

否

是

上传任务的网络配置，网络不满足设置条件时，未执行的任务等待执行，执行中的任务失败/暂停。默认为request.agent.Network.ANY。

- request.agent.Network.ANY：不限网络类型。
- request.agent.Network.WIFI：无线网络。
- request.agent.Network.CELLULAR：蜂窝数据网络。

#### DownloadParams

下载相关参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力： **SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

localPath

string

否

否

本地文件路径，根路径为cache目录。

cloudPath

string

否

否

云侧文件路径。支持传入“文件目录/文件名”（如“image/demo.jpg”），或仅传入文件名。

mode

[request.agent.Mode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagentmode10)

否

是

下载任务类型，前端任务在应用切换到后台一段时间后失败/暂停；后台任务不受影响。默认为request.agent.Mode.BACKGROUND。

- request.agent.Mode.BACKGROUND：后台任务。
- request.agent.Mode.FOREGROUND：前端任务。

overwrite

boolean

否

是

当本地文件已存在时，是否覆盖本地文件，默认false。

- true：覆盖本地文件。
- false：不覆盖，若存在同名文件则下载失败。

network

[request.agent.Network](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagentnetwork10)

否

是

下载任务的网络配置，网络不满足设置条件时，未执行的任务等待执行，执行中的任务失败/暂停。默认为request.agent.Network.ANY。

- request.agent.Network.ANY：不限网络类型。
- request.agent.Network.WIFI：无线网络。
- request.agent.Network.CELLULAR：蜂窝数据网络。

#### ListOptions

列举操作的相关参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力： **SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

maxResults

number

否

是

列举文件的最大数量，取值范围1-1000，默认则列举所有文件。

pageMarker

string

否

是

分页标识。默认值为空。

#### ListResults

列举操作的结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力： **SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

directories

string[]

否

否

列举操作返回的云侧目录列表。

files

string[]

否

否

列举操作返回的云侧文件列表。

pageMarker

string

否

是

分页标识。默认值为空。

#### MetadataUpdatable

可更新参数的元数据信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力： **SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

contentType

string

否

是

标准HTTP头部的Content-Type。

cacheControl

string

否

是

标准HTTP头部的Cache-Control。

contentDisposition

string

否

是

标准HTTP头部的Content-Disposition。

contentEncoding

string

否

是

标准HTTP头部的Content-Encoding。

contentLanguage

string

否

是

标准HTTP头部的Content-Language。

customMetadata

Record<string, string>

否

是

自定义的云侧文件属性，不区分大小写，并且需要符合标准HTTP头部的规范。

#### Metadata

完整的元数据信息，继承自[MetadataUpdatable](#section1122119164218)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力： **SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

name

string

否

否

云侧文件名称。

size

number

否

否

云侧文件大小，单位为字节。

createTime

Date

否

否

云侧文件创建时间，格式：yyyy-MM-ddTHH:mm:ssZ。

modifyTime

Date

否

否

云侧文件修改时间，格式：yyyy-MM-ddTHH:mm:ssZ。

sha256Hash

string

否

是

云侧文件的SHA256信息。