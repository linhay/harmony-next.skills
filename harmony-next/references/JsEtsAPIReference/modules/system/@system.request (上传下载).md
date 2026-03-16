# @system.request (上传下载)

system.request部件主要给应用提供上传下载文件的基础能力。

-

从API Version 9开始所有接口不再维护，推荐使用新接口[@ohos.request](../ohos/@ohos.request (上传下载).md)。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import request from '@system.request';
```

#### request.upload(deprecated)

upload(options: UploadRequestOptions): void

上传文件，无返回值。

**系统能力**：SystemCapability.MiscServices.Upload

**参数：**

参数名类型必填说明options[UploadRequestOptions](#ZH-CN_TOPIC_0000002529445487__uploadrequestoptionsdeprecated)是上传的配置信息。

**示例：**

```ets
import request, { UploadRequestOptions } from '@system.request';

let uploadRequestOptions: UploadRequestOptions = {
  url: 'http://www.path.com',
  method: 'POST',
  files: [{
    filename: "test",
    name: "test",
    uri: "internal://cache/test.jpg",
    type: "jpg"
  }],
  data: [{
    name: "name123",
    value: "123"
  }],
  success: (data: object) => {
    console.info(' upload success, code:' + JSON.stringify(data));
  },
  fail: (data:string, code:number) => {
    console.info(' upload fail data: ' + data + 'code: ' + code);
  },
  complete: () => {
    console.info(' upload complete');
  }
}

try {
  request.upload(uploadRequestOptions);
  console.info('upload start ');
} catch (err) {
  console.info(' upload err:' + err);
}
```

#### UploadRequestOptions(deprecated)

**系统能力**：SystemCapability.MiscServices.Upload

名称类型必填说明urlstring是上传服务器地址。dataArray<[RequestData](#ZH-CN_TOPIC_0000002529445487__requestdatadeprecated)>否请求的表单数据。filesArray<[RequestFile](#ZH-CN_TOPIC_0000002529445487__requestfiledeprecated)>是待上传文件列表。请使用multipart/form-data进行提交。headerObject否请求头。methodstring否请求方法：POST、PUT。缺省POST。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

**success参数：**

参数名类型必填说明data[UploadResponse](#ZH-CN_TOPIC_0000002529445487__uploadresponsedeprecated)是上传任务成功返回信息。

**fail参数：**

参数名类型必填说明dataany是上传任务失败返回header信息。codenumber是上传任务失败返回HTTP状态码。

#### UploadResponse(deprecated)

**系统能力**：SystemCapability.MiscServices.Upload

名称类型必填说明codenumber是服务器返回的HTTP状态码。datastring是服务器返回的内容。根据返回头内容中的type决定该值的类型。headersObject是服务器返回的返回头内容。

#### RequestFile(deprecated)

**系统能力**：SystemCapability.MiscServices.Upload

名称类型必填说明filenamestring否multipart 提交时，请求头中的文件名。namestring否multipart 提交时，表单项目的名称，缺省为file。uristring是文件的本地存储路径。typestring否文件的内容类型，默认根据文件名或路径的后缀获取。

#### RequestData(deprecated)

**系统能力**：SystemCapability.MiscServices.Upload

名称类型必填说明namestring是表示form 元素的名称。valuestring是表示form 元素的值。

#### request.download(deprecated)

download(options: DownloadRequestOptions): void

下载文件，无返回值。

**系统能力**：SystemCapability.MiscServices.Download

**参数：**

参数名类型必填说明options[DownloadRequestOptions](#ZH-CN_TOPIC_0000002529445487__downloadrequestoptionsdeprecated)是下载的配置信息。

**示例：**

```ets
import request, { DownloadRequestOptions } from '@system.request';

let downloadRequestOptions: DownloadRequestOptions = {
  url: 'http://www.path.com',
  filename: 'requestSystenTest',
  header: "",
  description: 'this is requeSystem download response',
  success: (data:object) => {
    console.info(' download success, code:' + JSON.stringify(data));
  },
  fail: (data:string, code:number) => {
    console.info(' download fail data: ' + data + 'code: ' + code);
  },
  complete: () => {
    console.info(' download complete');
  }
}

try {
  request.download(downloadRequestOptions);
  console.info('download start ');
} catch(err) {
  console.info(' download err:' + err);
}
```

#### DownloadRequestOptions(deprecated)

**系统能力**：SystemCapability.MiscServices.Download

名称类型必填说明urlstring是资源地址。filenamestring否本次下载文件的名称。默认从本次请求或资源地址中获取。headerObject否请求头。descriptionstring否资源地址的下载描述，默认为文件名称。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

**success参数：**

参数名类型必填说明data[DownloadResponse](#ZH-CN_TOPIC_0000002529445487__downloadresponsedeprecated)是下载任务成功返回信息。

**fail参数：**

参数名类型必填说明dataany是下载任务失败返回header信息。codenumber是下载任务失败返回HTTP状态码。

#### DownloadResponse(deprecated)

**系统能力**：SystemCapability.MiscServices.Download

名称类型必填说明tokenstring是表示下载的token，获取下载状态的依据。

#### request.onDownloadComplete(deprecated)

onDownloadComplete(options: OnDownloadCompleteOptions): void

获取下载任务状态，无返回值。

**系统能力**：SystemCapability.MiscServices.Download

**参数：**

参数名类型必填说明options[OnDownloadCompleteOptions](#ZH-CN_TOPIC_0000002529445487__ondownloadcompleteoptionsdeprecated)是监听下载任务的配置信息。

**示例：**

```ets
import request, { OnDownloadCompleteOptions } from '@system.request';

let onDownloadCompleteOptions: OnDownloadCompleteOptions = {
  token: 'token-index',
  success: (data:object) => {
    console.info(' download success, code:' + JSON.stringify(data));
  },
  fail: (data:string, code:number) => {
    console.info(' download fail data: ' + data + 'code: ' + code);
  },
  complete: () => {
    console.info(' download complete');
  }
}

request.onDownloadComplete(onDownloadCompleteOptions);
```

#### OnDownloadCompleteOptions(deprecated)

**系统能力**：SystemCapability.MiscServices.Download

名称类型必填说明tokenstring是download 接口返回的结果 token。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

**success参数：**

参数名类型必填说明data[OnDownloadCompleteResponse](#ZH-CN_TOPIC_0000002529445487__ondownloadcompleteresponsedeprecated)是下载任务成功返回信息。

**fail参数：**

参数名类型必填说明dataany是下载任务失败返回header信息。codenumber是下载任务失败返回HTTP状态码。

#### OnDownloadCompleteResponse(deprecated)

**系统能力**：SystemCapability.MiscServices.Download

名称类型必填说明uristring是表示下载文件的uri。