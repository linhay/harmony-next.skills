# rcp

本模块提供HTTP数据请求功能。应用程序可通过HTTP发起数据请求。常见的HTTP方法包括GET、POST、HEAD、PUT、DELETE、PATCH、OPTIONS等。

起始版本： 4.1.0(11)

**导入模块**

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
```

**rcp.createSession**

createSession(sessionConfiguration?: SessionConfiguration): Session

创建HTTP会话。这是启动HTTP交互的主要方法。开发者可以使用此API与[SessionConfiguration](#ZH-CN_TOPIC_0000002522081536__sessionconfiguration)一起创建会话。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

自5.1.0(18)版本开始变更为最多可创建1024个session实例，应用在通过创建的session实例访问完网络请求后，应及时关闭session，保证资源合理利用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionConfiguration | SessionConfiguration | 否 | 会话配置，应用于会话请求的设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Session | 代表一个会话，用于发送HTTP请求并管理其配置、取消和关闭的生命周期。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007900994 | Sessions number reached limit. |

示例：

```ets
const session = rcp.createSession();
```

**Session**

Session类表示可用于发出HTTP请求的通信会话。它提供了各种HTTP方法（FETCH、GET、POST、PUT、HEAD、DELETE、CANCEL、CLOSE）。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 否 | 表示会话的标识符。 |
| configuration | SessionConfiguration | undefined | 是 | 否 | 表示会话的配置设置。 |

**fetch**

fetch(request: Request): Promise<Response>

发送一个HTTP请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 是 | 要发送的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
let req = new rcp.Request("http://example.com/fetch", "POST");
session.fetch(req).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**fetchForSendable**

fetchForSendable(request: Request): Promise<ResponseSendable>

发送一个HTTP请求，并返回服务器的HTTP响应，该响应消息支持Sendable。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 是 | 待发送的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ResponseSendable> | Promise对象，返回来自服务器的响应对象，该响应对象支持Sendable。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { ArkTSUtils, collections, taskpool, util } from '@kit.ArkTS';

@Concurrent
async function taskFunc(sendableResponse: rcp.ResponseSendable) {
  console.info(`sendableResponse: ${ArkTSUtils.ASON.stringify(sendableResponse)}`);
  // 打印Sendable类型的body数据
  if (ArkTSUtils.isSendable(sendableResponse.body) && sendableResponse.body != undefined) {
    const decoder = util.TextDecoder.create('utf-8');
    let arr: collections.Uint8Array = new collections.Uint8Array(sendableResponse.body);
    let str = decoder.decodeToString(arr as Object as Uint8Array).trim();
    console.info(`body:${ArkTSUtils.ASON.stringify(str)}`);
  }

async function test() {
  try {
    const session = rcp.createSession();
    let request = new rcp.Request('https://www.example.com'); // 请在使用中将其替换为真实的网址。
    let sendableResponse = await session.fetchForSendable(request);
    let isSendable = ArkTSUtils.isSendable(sendableResponse);
    if (isSendable) {
      console.info(`Succeeded in getting the response, the response is sendable`);
    } else {
      console.info(`Succeeded in getting the response, the response is not sendable`);
    }
    let task: taskpool.Task = new taskpool.Task(taskFunc, sendableResponse);
    await taskpool.execute(task);
  } catch (err) {
    console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err)}`);
  }
```

**get**

get(url: URLOrString, destination?: ResponseBodyDestination): Promise<Response>

发送一个带有默认HTTP参数的HTTP GET请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP GET请求资源的URL。 |
| destination | ResponseBodyDestination | 否 | HTTP响应的目标位置或目的地。 起始版本： 5.0.0(12) |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.get("http://example.com/get").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**post**

post(url: URLOrString, content?: RequestContent, destination?: ResponseBodyDestination): Promise<Response>

发送一个带有默认HTTP参数的HTTP POST请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP POST请求资源的URL。 |
| content | RequestContent | 否 | 请求的正文内容。默认为undefined。 |
| destination | ResponseBodyDestination | 否 | HTTP响应的目标位置或目的地。 起始版本： 5.0.0(12) |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.post("http://example.com/post", "data to send").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**put**

put(url: URLOrString, content?: RequestContent, destination?: ResponseBodyDestination): Promise<Response>

发送一个带有默认HTTP参数的HTTP PUT请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP PUT请求资源的URL。 |
| content | RequestContent | 否 | 请求正文发送的内容。默认为undefined。 |
| destination | ResponseBodyDestination | 否 | HTTP响应的目标位置或目的地。 起始版本： 5.0.0(12) |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.put("http://example.com/put", "data to send").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**downloadToFile**

downloadToFile(url: URLOrString, downloadTo: DownloadToFile): Promise<Response>

发送一个带有默认HTTP参数的HTTP DOWNLOADTOFILE请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP DOWNLOADTOFILE请求资源的URL。 |
| downloadTo | DownloadToFile | 是 | HTTP中用于将服务器上下载的文件保存到本地文件系统中的指定位置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let downloadToFile: rcp.DownloadToFile = {
  kind: 'folder',
  path: "/path/dir" // 请根据自身业务选择合适的路径
} as rcp.DownloadToFile
const session = rcp.createSession();
session.downloadToFile("http://www.example.com", downloadToFile).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`DownloadToFile failed, the error message is ${JSON.stringify(err)}`);
});
```

**uploadFromFile**

uploadFromFile(url: URLOrString, uploadFrom: UploadFromFile): Promise<Response>

发送一个带有默认HTTP参数的HTTP UPLOADFROMFILE请求，完成上传文件功能，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP UPLOADFROMFILE请求资源的URL。 |
| uploadFrom | UploadFromFile | 是 | HTTP中从本地计算机上传文件到服务器的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let fileDir = "/path/dir/"; // 请根据自身业务定义此路径
let uploadFromFile: rcp.UploadFromFile = {
  fileOrPath: fileDir
};
const session = rcp.createSession();
session.uploadFromFile("http://example.com/head", uploadFromFile).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**downloadToStream**

downloadToStream(url: URLOrString, downloadTo: DownloadToStream): Promise<Response>

发起一个带默认HTTP参数的流式下载（DOWNLOADTOSTREAM）请求，从服务器下载数据流，并返回HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP DOWNLOADTOSTREAM请求资源的URL。 |
| downloadTo | DownloadToStream | 是 | HTTP中将请求文件从服务器下载到客户端，并将其写入到一个数据流中。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit'

const streamData: rcp.WriteStream = {
  write(buffer: ArrayBuffer): Promise<void | number> {
    return Promise.resolve(buffer.byteLength)
  }
};

let downloadToStream: rcp.DownloadToStream = {
  kind: 'stream',
  stream: streamData
}
const session = rcp.createSession();
session.downloadToStream("http://example.com/head", downloadToStream).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**uploadFromStream**

uploadFromStream(url: URLOrString, uploadFrom: UploadFromStream): Promise<Response>

发起一个带默认HTTP参数的流式上传（UPLOADFROMSTREAM）请求，将数据流上传至服务器，并返回HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP UPLOADFROMSTREAM请求资源的URL。 |
| uploadFrom | UploadFromStream | 是 | HTTP中从一个输入流中上传数据到服务器的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let uploadFromStream: rcp.UploadFromStream = {
  stream: object // 此处请自行定义类型为Stream、ReadStream、SyncReadStream的对象
}
const session = rcp.createSession();
session.uploadFromStream("http://example.com/head", uploadFromStream).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**head**

head(url: URLOrString): Promise<Response>

发送一个带有默认HTTP参数的HTTP HEAD请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP HEAD请求资源的URL。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.head("http://example.com/head").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**delete**

delete(url: URLOrString): Promise<Response>

发送一个带有默认HTTP参数的HTTP DELETE请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP DELETE请求资源的URL。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.delete("http://example.com/delete").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**cancel**

cancel(requestToCancel?: Request | Request[]): void

取消指定或正在进行的会话请求。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestToCancel | Request | Request[] | 否 | 要取消的请求或请求数组。在不指定Request情况下，默认取消所有请求。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
let req = new rcp.Request("http://example.com/fetch", "GET");
session.fetch(req).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
  session.cancel(req);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**close**

close(): void

关闭会话。调用此方法以释放与此会话关联的资源。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
let req = new rcp.Request("http://example.com/fetch", "GET");
session.fetch(req).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
  session.close();
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
  session.close();
});
```

**rcp.getDefaultSession**

getDefaultSession(): DefaultSession

获取默认的HTTP会话。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

返回值：

| 类型 | 说明 |
| --- | --- |
| DefaultSession | 代表一个默认会话，用于发送或取消HTTP请求。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
```

**DefaultSession**

DefaultSession类表示一个默认的通信会话，可用于发送HTTP请求。如果不需要定制Session的配置，可以使用DefaultSession便捷地发起网络请求。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

**fetch**

fetch(request: Request): Promise<Response>

发送一个HTTP请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 是 | 要发送的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
let req = new rcp.Request("http://example.com/fetch", "POST");
defaultSession.fetch(req).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**fetchForSendable**

fetchForSendable(request: Request): Promise<ResponseSendable>

发送一个HTTP请求，并返回服务器的HTTP响应，该响应消息支持Sendable。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 是 | 待发送的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ResponseSendable> | Promise对象，返回来自服务器的响应对象，该响应对象支持Sendable。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { ArkTSUtils, collections, taskpool, util } from '@kit.ArkTS';
import utils from '@arkts.utils';

@Concurrent
async function taskFunc(sendableResponse: rcp.ResponseSendable) {
  console.info(`sendableResponse: ${ArkTSUtils.ASON.stringify(sendableResponse)}`);
  // 打印Sendable类型的body数据
  if (utils.isSendable(sendableResponse.body) && sendableResponse.body != undefined) {
    const decoder = util.TextDecoder.create('utf-8');
    let arr: collections.Uint8Array = new collections.Uint8Array(sendableResponse.body);
    let str = decoder.decodeToString(arr as Object as Uint8Array).trim();
    console.info(`body:${ArkTSUtils.ASON.stringify(str)}`);
  }

async function test() {
  try {
    const defaultSession = rcp.getDefaultSession();
    let request = new rcp.Request('https://www.example.com'); // 请在使用中将其替换为真实的网址。
    let sendableResponse = await defaultSession.fetchForSendable(request);
    let isSendable = utils.isSendable(sendableResponse);
    if (isSendable) {
      console.info(`Succeeded in getting the response, the response is sendable`);
    } else {
      console.info(`Succeeded in getting the response, the response is not sendable`);
    }
    let task: taskpool.Task = new taskpool.Task(taskFunc, sendableResponse);
    await taskpool.execute(task);
  } catch (err) {
    console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err)}`);
  }
```

**get**

get(url: URLOrString, destination?: ResponseBodyDestination): Promise<Response>

发送一个带有默认HTTP参数的HTTP GET请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP GET请求资源的URL。 |
| destination | ResponseBodyDestination | 否 | HTTP响应的目标位置或目的地。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
defaultSession.get("http://example.com/get").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**post**

post(url: URLOrString, content?: RequestContent, destination?: ResponseBodyDestination): Promise<Response>

发送一个带有默认HTTP参数的HTTP POST请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP POST请求资源的URL。 |
| content | RequestContent | 否 | 请求的正文内容。默认为undefined。 |
| destination | ResponseBodyDestination | 否 | HTTP响应的目标位置或目的地。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
defaultSession.post("http://example.com/post", "data to send").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**put**

put(url: URLOrString, content?: RequestContent, destination?: ResponseBodyDestination): Promise<Response>

发送一个带有默认HTTP参数的HTTP PUT请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP PUT请求资源的URL。 |
| content | RequestContent | 否 | 请求正文发送的内容。默认为undefined。 |
| destination | ResponseBodyDestination | 否 | HTTP响应的目标位置或目的地。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
defaultSession.put("http://example.com/put", "data to send").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**downloadToFile**

downloadToFile(url: URLOrString, downloadTo: DownloadToFile): Promise<Response>

发送一个带有默认HTTP参数的HTTP DOWNLOADTOFILE请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP DOWNLOADTOFILE请求资源的URL。 |
| downloadTo | DownloadToFile | 是 | HTTP中用于将服务器上下载的文件保存到本地文件系统中的指定位置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let downloadToFile: rcp.DownloadToFile = {
  kind: 'folder',
  path: "/path/dir" // 请根据自身业务选择合适的路径
} as rcp.DownloadToFile
const defaultSession = rcp.getDefaultSession();
defaultSession.downloadToFile("http://www.example.com", downloadToFile).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`DownloadToFile failed, the error message is ${JSON.stringify(err)}`);
});
```

**uploadFromFile**

uploadFromFile(url: URLOrString, uploadFrom: UploadFromFile): Promise<Response>

发送一个带有默认HTTP参数的HTTP UPLOADFROMFILE请求，完成上传文件功能，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP UPLOADFROMFILE请求资源的URL。 |
| uploadFrom | UploadFromFile | 是 | HTTP中从本地计算机上传文件到服务器的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let fileDir = "/path/dir/"; // 请根据自身业务定义此路径
let uploadFromFile: rcp.UploadFromFile = {
  fileOrPath: fileDir
};
const defaultSession = rcp.getDefaultSession();
defaultSession.uploadFromFile("http://example.com/head", uploadFromFile).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**downloadToStream**

downloadToStream(url: URLOrString, downloadTo: DownloadToStream): Promise<Response>

发起一个带默认HTTP参数的流式下载（DOWNLOADTOSTREAM）请求，从服务器下载数据流，并返回HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP DOWNLOADTOSTREAM请求资源的URL。 |
| downloadTo | DownloadToStream | 是 | HTTP中将请求文件从服务器下载到客户端，并将其写入到一个数据流中。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit'

const streamData: rcp.WriteStream = {
  write(buffer: ArrayBuffer): Promise<void | number> {
    return Promise.resolve(buffer.byteLength)
  }
};

let downloadToStream: rcp.DownloadToStream = {
  kind: 'stream',
  stream: streamData
}
const defaultSession = rcp.getDefaultSession();
defaultSession.downloadToStream("http://example.com/head", downloadToStream).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**uploadFromStream**

uploadFromStream(url: URLOrString, uploadFrom: UploadFromStream): Promise<Response>

发起一个带默认HTTP参数的流式上传（UPLOADFROMSTREAM）请求，将数据流上传至服务器，并返回HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP UPLOADFROMSTREAM请求资源的URL。 |
| uploadFrom | UploadFromStream | 是 | HTTP中从一个输入流中上传数据到服务器的请求。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let uploadFromStream: rcp.UploadFromStream = {
  stream: object // 此处请自行定义类型为Stream、ReadStream、SyncReadStream的对象
}
const defaultSession = rcp.getDefaultSession();
defaultSession.uploadFromStream("http://example.com/head", uploadFromStream).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**head**

head(url: URLOrString): Promise<Response>

发送一个带有默认HTTP参数的HTTP HEAD请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP HEAD请求资源的URL。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
defaultSession.head("http://example.com/head").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**delete**

delete(url: URLOrString): Promise<Response>

发送一个带有默认HTTP参数的HTTP DELETE请求，并返回来自服务器的HTTP响应。使用Promise异步回调。

需要权限： ohos.permission.INTERNET（如果使用[PathPreference](#ZH-CN_TOPIC_0000002522081536__pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO）

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | HTTP DELETE请求资源的URL。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

错误码： 错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
defaultSession.delete("http://example.com/delete").then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**cancel**

cancel(requestToCancel?: Request | Request[]): void

取消指定或正在进行的会话请求。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestToCancel | Request | Request[] | 否 | 要取消的请求或请求数组。在不指定Request情况下，默认取消所有请求。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const defaultSession = rcp.getDefaultSession();
let req = new rcp.Request("http://example.com/fetch", "GET");
defaultSession.fetch(req).then((response) => {
  console.info(`Succeeded in getting the response ${response}`);
  defaultSession.cancel(req);
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**RequestHandler**

拦截器的请求处理器。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**handle**

handle(context: RequestContext): Promise<Response>

远场通信框架会预置两种处理器，一种会调用拦截器的[intercept](#ZH-CN_TOPIC_0000002522081536__intercept)函数，一种会调用系统的fetchInternal使用系统能力发起请求，使用promise异步回调。

比如，拦截器：[A, B, C, D]会被构造成：

A {handler->B{handler->C{handler-D{handler->系统能力}}}}

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | RequestContext | 是 | 请求上下文 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | Promise对象，返回来自服务器的响应对象。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

class RequestHandler implements rcp.RequestHandler {
  handle(context: rcp.RequestContext): Promise<rcp.Response> {
    let handlerRequest = new rcp.Request("https://www.example.com", 'GET');
    let handlerSession = rcp.createSession();
    context.request = handlerRequest;
    context.session = handlerSession;
    return new Promise<rcp.Response>((resolve, reject) => {
      handlerSession.get("https://www.example.com").then((response: rcp.Response) => {
        resolve(response);
      }).catch((error: Error) => {
        reject(error);
      })
    });
  }
```

**RequestContext**

拦截器请求上下文。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | Request | 否 | 否 | HTTP请求 |
| session | Session | 否 | 否 | 持有此拦截器的会话 |

**Interceptor**

拦截器。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**intercept**

intercept(context: RequestContext, next: RequestHandler): Promise<Response>

拦截器，用于修改请求、修改响应或者直接返回响应，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | RequestContext | 是 | 请求上下文 |
| next | RequestHandler | 是 | 下一个请求处理器 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Response> | 直接返回一个 Promise对象 ，或者返回下一个拦截器的值。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

class ResponseCache {
  private readonly cache: Record<string, rcp.Response> = {};

  getResponse(url: string): rcp.Response {
    return this.cache[url];
  }

  setResponse(url: string, response: rcp.Response): void {
    this.cache[url] = response;
  }

class ResponseCachingInterceptor implements rcp.Interceptor {
  private readonly cache: ResponseCache;

  constructor(cache: ResponseCache) {
    this.cache = cache;
  }

  async intercept(context: rcp.RequestContext, next: rcp.RequestHandler): Promise<rcp.Response> {
    const url = context.request.url.href;
    const responseFromCache = this.cache.getResponse(url);
    if (responseFromCache) {
      return Promise.resolve(responseFromCache);
    }
    const promise = next.handle(context);
    promise.then((resp) => {
      resp.statusCode;
      cache.setResponse(url, resp);
    });
    return promise;
  }

const cache = new ResponseCache();

async function testInterceptor() {
  const session = rcp.createSession({
    interceptors: [new ResponseCachingInterceptor(cache)]
  });

  await session.get('https://www.example.com').then((response: rcp.Response) => {
    console.info(`Response succeeded: ${response}`);
  }).catch((error: BusinessError) => {
    console.error(`Response failed: error message is ${JSON.stringify(error)}`);
  });

  let request = new rcp.Request("https://www.example.com", 'GET');
  const response2 = await session.fetch(request).then((response: rcp.Response) => {
    console.info(`Response succeeded: ${response}`);
  }).catch((error: BusinessError) => {
    console.error(`Response failed: error message is ${JSON.stringify(error)}`);
  });
}
```

**SessionConfiguration**

SessionConfiguration接口定义了会话的配置参数，为开发者提供了对HTTP会话各个方面的详细控制。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interceptors | Interceptor[] | 否 | 是 | 请求/响应拦截器。 起始版本： 5.0.0(12) |
| requestConfiguration | Configuration | 否 | 是 | 指定与会话关联的HTTP请求的配置。包括transfer、proxy、DNS、connection和security configurations。 |
| baseAddress | URLOrString | 否 | 是 | 设置会话中URL的基地址。这允许开发者为会话中的多个请求定义一个通用的基本URL。如果请求URL不是绝对URL，则把基地址预制在请求URL的前面。例如，"https://example.com?name=value"，“https://example.com”为基地址，"?name=value"为请求URL。 |
| headers | RequestHeaders | 否 | 是 | 为Session发出的HTTP请求定义headers（可自定义）。开发者可以根据他们的需求定制的特定headers。 |
| cookies | RequestCookies | 否 | 是 | 提供在与会话关联的HTTP请求中包含自定义cookie的方法。适用于需要将某些cookie附加到每个请求的场景。需要手动设置cookie，携带cookie为用户行为。 |
| sessionListener | SessionListener | 否 | 是 | 允许开发者将侦听器附加到会话，接收会话取消或关闭等事件的通知，更好地处理应用程序中与会话相关的事件。 |
| connectionConfiguration | ConnectionConfiguration | 否 | 是 | 连接配置。用于指定此会话中允许的并发TCP连接总数以及单个主机所允许的最大并发TCP 连接数。 起始版本： 5.0.0(12) |
| cacheControl | CacheControl | 否 | 是 | 缓存控制配置。用于主动控制会话中缓存验证策略，影响服务器或中间代理如何响应请求。 起始版本： 6.0.0(20) |
| cookieRepository | CookieRepository | 否 | 是 | cookie仓库。会话中的所有请求会共享cookie仓库。如果配置此项，那么此Session上的请求实际上都会由DefaultSession处理。 起始版本： 6.1.0(23) |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

let cookieRepository = rcp.CookieRepository.create();
const sessionConfig: rcp.SessionConfiguration = {
  requestConfiguration: {
    transfer: {
      autoRedirect: true,
      timeout: {
        connectMs: 5000,
        transferMs: 10000
      }
    },
    tracing: {
      verbose: true
    }
  },
  baseAddress: "http://api.example.com",
  headers: {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
  },
  cookies: {
    "user": "john_doe",
    "session_id": "abc123"
  },
  sessionListener: {
    onCanceled: () => console.info("Session was cancelled"),
    onClosed: () => console.info("Session was closed")
  },
  cookieRepository: cookieRepository,
  // ...
};

const session = rcp.createSession(sessionConfig);
```

interceptors属性示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

class ResponseCache {
  private readonly cache: Record<string, rcp.Response> = {};

  getResponse(url: string): rcp.Response {
    return this.cache[url];
  }

  setResponse(url: string, response: rcp.Response): void {
    this.cache[url] = response;
  }

class ResponseCachingInterceptor implements rcp.Interceptor {
  private readonly cache: ResponseCache;

  constructor(cache: ResponseCache) {
    this.cache = cache;
  }

  async intercept(context: rcp.RequestContext, next: rcp.RequestHandler): Promise<rcp.Response> {
    const url = context.request.url.href;
    const responseFromCache = this.cache.getResponse(url);
    if (responseFromCache) {
      return Promise.resolve(responseFromCache);
    }
    const promise = next.handle(context);
    promise.then((resp) => {
      this.cache.setResponse(url, resp);
    });
    return promise;
  }

const cache = new ResponseCache();

async function testInterceptor() {
  const session = rcp.createSession({
    interceptors: [new ResponseCachingInterceptor(cache)]
  });

  await session.get('https://www.example.com').then((response: rcp.Response) => {
    console.info(`Response succeeded: ${response}`);
  }).catch((error: BusinessError) => {
    console.error(`Response failed: error message is ${JSON.stringify(error)}`);
  });

  let request = new rcp.Request("https://www.example.com", 'GET');
  const response2 = await session.fetch(request).then((response: rcp.Response) => {
    console.info(`Response succeeded: ${response}`);
  }).catch((error: BusinessError) => {
    console.error(`Response failed: error message is ${JSON.stringify(error)}`);
  });
}
```

**Configuration**

Configuration接口包含一组配置参数，开发者可以利用这些参数来微调会话中HTTP请求的行为。这包括传输、跟踪、代理、DNS和安全配置的设置。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| transfer | TransferConfiguration | 否 | 是 | 配置与HTTP请求期间的数据传输相关的各个方面，例如自动重定向和超时设置。 |
| tracing | TracingConfiguration | 否 | 是 | 使开发者能够在HTTP请求期间捕获详细的跟踪信息，有助于调试和性能分析。 |
| proxy | ProxyConfiguration | 否 | 是 | 配置会话的代理设置，允许开发者定义'system'、'no-proxy'或WebProxy配置。 |
| dns | DnsConfiguration | 否 | 是 | 指定与DNS相关的配置，包括自定义DNS规则和通过HTTPS使用DNS的选项。 |
| security | SecurityConfiguration | 否 | 是 | 包括用于处理安全相关方面的设置，如证书和服务器身份验证。 |
| processing | ProcessingConfiguration | 否 | 是 | 响应处理配置。 起始版本： 5.0.0(12) |
| cache | ResponseCache | 否 | 是 | 指定与HTTP缓存相关的配置。 起始版本： 6.0.0(20) |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const cache: rcp.ResponseCache = new rcp.ResponseCache({
  persistent: {
    kind: 'file-system',
    pathToFolder: "/path/dir/" // 请根据自身业务指定缓存路径
  }
});
const requestConfig: rcp.Configuration = {
  transfer: {
    autoRedirect: true,
    timeout: {
      connectMs: 5000,
      transferMs: 10000
    },
    assumesHTTP3Capable: true,
    pathPreference: "cellular"
  },
  tracing: {
    verbose: true
  },
  proxy: "system",
  dns: {
    dnsRules: [
      { host: "https://example.com", port: 443, ipAddresses: ["192.168.1.1", "192.168.1.2"] }
    ]
  },

  security: {
    certificate: {
      content: "-----BEGIN CERTIFICATE-----\n...",
      type: "PEM",
      key: "/path/dir/", // 请根据自身业务对key进行修改
      keyPassword: "your-password"
    },
    serverAuthentication: {
      credential: {
        username: "your-username",
        password: "your-password"
      },
      authenticationType: "basic"
    }
  },
  cache: cache
};

// Use the configuration in the session creation
const session = rcp.createSession({ requestConfiguration: requestConfig });
```

**ConnectionConfiguration**

ConnectionConfiguration接口包含两个参数，开发者可以调整最大并发TCP的连接数也可以对单个主机或此次会话中的TCP最大连接数进行调整。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxConnectionsPerHost | number | 是 | 是 | 单个主机允许的最大并发 TCP 连接数（主机与主机名+端口号对相同）。默认值为 6，最大值为 2147483647。 |
| maxTotalConnections | number | 是 | 是 | 此会话中允许的最大同时 TCP 连接总数。 默认值为 64，最大值为 2147483647。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit'

const connectionConfig: rcp.ConnectionConfiguration = {
  maxConnectionsPerHost: 6,
  maxTotalConnections: 64
}
const session = rcp.createSession({ connectionConfiguration: connectionConfig });
```

**TcpConfiguration**

TcpConfiguration接口为开发者提供设置TCP选项的能力。

当keepIdleSec、keepCnt、keepIntervalSec三个参数中至少有一个设置时，客户端会主动发送探测报文，未设置的参数将使用本文档中规定的默认值。若服务器一直不回复探测报文，TCP连接将在keepIdleSec + (keepCnt + 1) * keepIntervalSec秒后断开。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keepIdleSec | number | 否 | 是 | 该参数设置一个计时器，TCP连接将在计时器触发时发送探测报文。 单位：s。 取值范围：1~7200。 默认值：7200。 |
| userTimeoutMs | number | 否 | 是 | 该参数设置一个超时时间。若传输的数据在超时时间内未收到服务器的确认报文，TCP连接将被断开。 单位：ms。 取值范围：1~3600000。 默认值：和Timeout.transferMs保持一致。 |
| keepCnt | number | 否 | 是 | 该参数设置发送探测报文的次数。 单位：次。 取值范围：1~9。 默认值：9。 |
| keepIntervalSec | number | 否 | 是 | 该参数设置每个探测报文之间的时间间隔。 单位：s。 取值范围：1~75。 默认值：75。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const transferConfig: rcp.TransferConfiguration = {
  tcp: {
    keepIdleSec: 20,
    userTimeoutMs: 3000,
    keepCnt: 6,
    keepIntervalSec: 30,
  }
};

// Use the configuration in the session creation.
const session = rcp.createSession({
  requestConfiguration: {
    transfer: transferConfig
  }
});

// Use the configuration in the request.
const request = new rcp.Request('https://example.com');
request.configuration = {
  transfer: transferConfig
};
```

**CookieRepository**

cookie仓库。cookie仓库能够自动存储HTTP响应中的cookie，自动在HTTP请求中携带cookie，也支持手动管理仓库中的cookie。cookie仓库约每30秒将现有的cookie存储到本地，也可以使用[setCookies](#ZH-CN_TOPIC_0000002522081536__setcookies)主动将cookie存储到本地。使用cookie仓库的[Session](#ZH-CN_TOPIC_0000002522081536__session)实际上都会通过[DefaultSession](#ZH-CN_TOPIC_0000002522081536__defaultsession)处理请求。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

**create**

static create(identifier?: string): CookieRepository

创建cookie仓库。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| identifier | string | 否 | cookie仓库标识。只能包含大写字母、小写字母和下划线。 传入undefined、null或空字符串时默认为'default'。 传入其他字符时抛出1007900401错误。 具有同样标识的cookie仓库共享cookie信息（即具有同样标识的cookie仓库实例使用起来如同同一个实例）。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| CookieRepository | cookie仓库实例。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  rcp.CookieRepository.create('myRepo');
} catch (err) {
  console.error(`create error, code: ${err.code}`);
}
```

**setCookies**

setCookies(cookies: ResponseCookie | ResponseCookie[]): Promise<void>

添加或修改cookie，并将cookie仓库中现有的cookie存储到本地。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookies | ResponseCookie | ResponseCookie[] | 是 | 传入cookie仓库的cookie。cookie仓库里实际会存如下7项数据：domain、httpOnly、path、isSecure、expires、name和value。当两个cookie的name、domain、path三项完全相同时，视为同一个cookie。 path默认为'/'。 domain不设置或者设置为空字符串时抛出1007900401错误。 maxAge会转化为expires。maxAge和expires都设置时，使用maxAge。 expires应是符合RFC 7231协议，并且是GMT时间的字符串，精确到秒，例如：'Wed, 21 Oct 2025 07:28:00 GMT'。当expires字段传入无效字符串时抛出1007900401错误。 系统会不定期清除expires过期的cookie。传入空数组时，仅将cookie仓库中现有的cookie存储到本地。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 返回空值，使用Promise异步回调。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |
| 1007900999 | Internal Error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let cookieRepository = rcp.CookieRepository.create('myRepo');
let cookie: rcp.ResponseCookie = {
   name:'session_1',
   value:'10001',
   domain:'www.huawei.com', // 域名请根据实际业务配置
   maxAge: 60,
   isSecure: true
}
cookieRepository.setCookies(cookie).then(() => {
  console.info('setCookies success.');
}).catch((err: BusinessError) => {
  console.error(`setCookies error, code: ${err.code}`);
})
```

**getAllCookies**

getAllCookies(): Promise<ResponseCookie[]>

查询cookie仓库中所有的cookie。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ResponseCookie[]> | 返回ResponseCookie列表，使用Promise异步回调。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900999 | Internal Error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let cookieRepository = rcp.CookieRepository.create('myRepo');
cookieRepository.getAllCookies().then((cookies) => {
  console.info(`cookies num: ${cookies.length}`);
}).catch((err: BusinessError) => {
  console.error(`getAllCookies error, code: ${err.code}`);
})
```

**getCookiesByUrl**

getCookiesByUrl(url: URL): Promise<ResponseCookie[]>

根据url从cookie仓库获取cookie。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URL | 是 | HTTP请求的url，用于匹配cookie。匹配规则符合RFC 6265协议。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ResponseCookie[]> | 匹配url的cookie列表，使用Promise异步回调。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900999 | Internal Error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { url } from '@kit.ArkTS';

let cookieRepository = rcp.CookieRepository.create('myRepo');
cookieRepository.getCookiesByUrl(url.URL.parseURL('https://www.huawei.com')).then((cookies) => {
  console.info(`cookies num: ${cookies.length}`);
}).catch((err: BusinessError) => {
  console.error(`getAllCookies error, code: ${err.code}`);
})
```

**deleteCookies**

deleteCookies(cookies?: ResponseCookie | ResponseCookie[]): Promise<void>

删除指定的cookie。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookies | ResponseCookie | ResponseCookie[] | 否 | 需要删除的cookie。cookie的匹配规则和抛出错误的规则参考setCookies。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 返回空值，使用Promise异步回调。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |
| 1007900999 | Internal Error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let cookieRepository = rcp.CookieRepository.create('myRepo');
let cookie: rcp.ResponseCookie = {
   name:'session_1',
   value:'10001',
   domain:'www.huawei.com', // 域名请根据实际业务配置
   maxAge: 60,
   isSecure: true
}
cookieRepository.deleteCookies(cookie).then(() => {
  console.info('deleteCookies success.');
}).catch((err: BusinessError) => {
  console.error(`deleteCookies error, code: ${err.code}`);
})
```

**deleteCookiesByUrl**

deleteCookiesByUrl(url: URL): Promise<void>

根据url从cookie仓库删除cookie。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URL | 是 | HTTP请求的url，用于匹配cookie。匹配规则符合RFC 6265协议。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 删除匹配url的cookie后返回，使用Promise异步回调。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900999 | Internal Error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { url } from '@kit.ArkTS';

let cookieRepository = rcp.CookieRepository.create('myRepo');
cookieRepository.deleteCookiesByUrl(url.URL.parseURL('https://www.huawei.com')).then(() => {
  console.info('deleteCookiesByUrl success.');
}).catch((err: BusinessError) => {
  console.error(`deleteCookiesByUrl error, code: ${err.code}`);
})
```

**identifier**

get identifier(): string

获取cookie仓库标识。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 返回cookies仓库标识。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

let cookieRepository = rcp.CookieRepository.create('myRepo');
let identifier = cookieRepository.identifier;
console.info(`identifier is: ${identifier}`);
```

**TransferConfiguration**

TransferConfiguration接口为开发者提供了一组选项，用于调整会话中HTTP请求期间的数据传输行为。这包括与自动重定向和超时配置相关的设置。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| autoRedirect | boolean | 否 | 是 | 指定HTTP客户端是否应自动遵循重定向。如果设置为true，客户端将自动遵循HTTP重定向；否则，不会自动重定向。默认值为true。 |
| timeout | Timeout | 否 | 是 | 配置HTTP请求的超时值，允许开发者定义连接和传输数据所允许的最长时间。如果未设置，则使用默认时间。 |
| assumesHTTP3Capable | boolean | 否 | 是 | 指定连接是否具有HTTP/3功能，true代表连接具有HTTP/3功能，false代表没有，默认为false。 |
| pathPreference | PathPreference | 否 | 是 | HTTP请求路径首选项，此处配置的为建议路径，在实际使用过程中，系统会决定使用哪个路径。可以是'自动'或'蜂窝'路径。默认为'自动'路径。 |
| serviceType | ServiceType | 否 | 是 | 服务类型。默认为undefined。 |
| maxAutoRedirects | number | 否 | 是 | 请求要遵循的最大重定向次数，如果 autoRedirect 属性为 true，则需要对其设置。默认值为50，最大值为2147483647。 起始版本： 5.0.0(12) |
| pausePolicy | PausePolicy | 否 | 是 | 请求暂停策略。 起始版本： 5.0.0(12) |
| tcp | TcpConfiguration | 否 | 是 | TCP连接的相关配置。 起始版本： 6.0.0(20) |
| connectionReusePolicy | ConnectionReusePolicy | 否 | 是 | HTTP连接复用方式。默认是'naive'。 起始版本： 6.1.0(23) |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const transferConfig: rcp.TransferConfiguration = {
  autoRedirect: true,
  timeout: {
    connectMs: 5000,
    transferMs: 10000
  },
  assumesHTTP3Capable: true,
  pathPreference: "cellular",
  connectionReusePolicy: "balanced"
};

// Use the configuration in the session creation
const session = rcp.createSession({ requestConfiguration: { transfer: transferConfig } });
```

**TracingConfiguration**

TracingConfiguration接口使开发者能够在会话中的HTTP请求期间捕获详细的跟踪信息。跟踪有助于调试、性能分析和深入了解通信过程中的数据流。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| verbose | boolean | 否 | 是 | 启用详细跟踪，捕获有关HTTP请求/响应流的大量信息。默认值为false，true表示开启捕获，false表示不开启。 |
| infoToCollect | InfoToCollect | 否 | 是 | 配置要收集的特定类型的信息事件。默认无事件需要收集。 |
| collectTimeInfo | boolean | 否 | 是 | 指示在跟踪过程中是否应收集与时间相关的信息，true代表收集，false代表不收集，默认值为false。 |
| httpEventsHandler | HttpEventsHandler | 否 | 是 | 为HTTP请求/响应过程中的特定操作定义响应处理程序的回调。默认值为undefined。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

// Define a custom response handler
const customHttpEventsHandler: rcp.HttpEventsHandler = {
  onDataReceive: (incomingData: ArrayBuffer) => {
    // Custom logic for handling incoming data
    console.info("Received data:", incomingData);
    return incomingData.byteLength;
  },
  onUploadProgress: (totalSize: number, transferredSize: number) => {
    // Custom logic for handling upload progress
    console.info("Upload progress:", transferredSize, "of", totalSize);
  },
  onDownloadProgress: (totalSize: number, transferredSize: number) => {
    // Custom logic for handling download progress
    console.info("Download progress:", transferredSize, "of", totalSize);
  },
  onHeaderReceive: (headers: rcp.ResponseHeaders) => {
    // Custom logic for handling response headers
    console.info("Received headers:", headers);
  },
  onDataEnd: () => {
    // Custom logic for handling data transfer completion
    console.info("Data transfer complete");
  },
  onCanceled: () => {
    // Custom logic for handling cancellation
    console.info("Request/response canceled");
  },
  onStatusCodeReceive: (statusCode: number, request?: rcp.Request) => {
    // Custom logic for handling statusCode
    console.info("Received statusCode:", statusCode);
  }
};

// Configure tracing settings
const tracingConfig: rcp.TracingConfiguration = {
  verbose: true,
  infoToCollect: {
    textual: true,
    incomingHeader: true,
    outgoingHeader: true,
    incomingData: true,
    outgoingData: true,
    incomingSslData: true,
    outgoingSslData: true
  },
  collectTimeInfo: true,
  httpEventsHandler: customHttpEventsHandler
};

// Use the configuration in the session creation
const session = rcp.createSession({ requestConfiguration: { tracing: tracingConfig } });
```

**ProxyConfiguration**

type ProxyConfiguration = 'system' | 'no-proxy' | [WebProxy](#ZH-CN_TOPIC_0000002522081536__webproxy)

ProxyConfiguration接口允许开发者为会话中的HTTP请求配置代理设置，从而提供在系统、自定义或无代理之间进行选择的灵活性。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| 'system' | HTTP代理配置。'system'：表示使用系统代理配置。 |
| 'no-proxy' | HTTP代理配置。'no-proxy'：表示不使用代理。 |
| WebProxy | HTTP代理配置。WebProxy：表示提供自定义代理设置。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

// Configure system proxy (default)
const systemProxyConfig = "system";

// Configure custom proxy
const customProxyConfig: rcp.WebProxy = {
  url: "http://custom-proxy.example.com",
  createTunnel: "always",
  exclusions: ["http://exclude.example.com"],
  security: {
    certificate: {
      content: "-----BEGIN CERTIFICATE-----\n...",
      type: "PEM",
      key: "-----BEGIN PRIVATE KEY-----\n...", // 请根据实际业务选择合适的key
      keyPassword: "your-password"
    },
    serverAuthentication: {
      credential: {
        username: "proxy-username",
        password: "proxy-password"
      },
      authenticationType: "basic"
    }
};

// Configure no proxy
const noProxyConfig = "no-proxy";

// Use the proxy configuration in the session creation
const sessionWithSystemProxy = rcp.createSession({ requestConfiguration: { proxy: systemProxyConfig } });
const sessionWithCustomProxy = rcp.createSession({ requestConfiguration: { proxy: customProxyConfig } });
const sessionWithNoProxy = rcp.createSession({ requestConfiguration: { proxy: noProxyConfig } });
```

**DnsConfiguration**

允许开发者为会话中的HTTP请求配置域名系统（DNS）设置。它提供了指定DNS规则的灵活性，包括自定义DNS服务器或静态DNS规则。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dnsRules | DnsServers | StaticDnsRules | DynamicDnsRule | 否 | 是 | 配置DNS规则，默认值为undefined。 DnsServers：表示优先使用指定的DNS服务器解析主机名。 StaticDnsRules：静态DNS规则，表示如果hostname匹配，则优先使用指定的地址。 DynamicDnsRule：动态DNS规则，表示优先使用函数中返回的地址。 说明： 针对同一域名配置多个静态或者动态DNS规则后，默认情况下，仅有最后一个IP地址生效。如果希望多个IP地址同时生效，在6.0.0(20)版本后，支持同一域名配置多个静态或者动态DNS规则，此时将happyEyeballOnDnsRule设置为true可以让多个IP地址同时生效。 |
| dnsOverHttps | DnsOverHttpsConfiguration | 否 | 是 | DNS over HTTPS配置。默认值为undefined。 如果设置，则优先使用DNS服务器解析的地址。 |
| happyEyeballOnDnsRule | boolean | 否 | 是 | 是否启用Happy Eyeball竞速连接。 当特定地址或地址族（IPv4或IPv6）被阻止、损坏或网络不佳质量差时，可通过Happy Eyeball竞速连接更快地建立连接。 true：当DNS规则（dnsRules参数）被设置时启用Happy Eyeball竞速连接功能。 false：当DNS规则（dnsRules参数）被设置时不启用Happy Eyeball竞速连接功能。 默认值是false。 起始版本： 6.0.0(20) 说明： 只有设置了DNS规则（dnsRules参数）时该配置项才有意义；否则，Happy Eyeball竞速连接功能是默认启用的，而且无法关闭，此时设置此选项无任何作用。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

// Configure custom DNS servers
const customDnsServers: rcp.DnsServers = [
  { ip: "8.8.8.8" },
  { ip: "8.8.4.4", port: 53 }
];

// Configure static DNS rules
const staticDnsRules: rcp.StaticDnsRules = [
  { host: "example.com", port: 80, ipAddresses: ["192.168.1.1", "192.168.1.2"] },
  { host: "sub.example.com", port: 443, ipAddresses: ["192.168.2.1"] }
];

// Configure DNS over HTTPS
const dohConfig: rcp.DnsOverHttpsConfiguration = {
  url: "https://dns.example.com/dns-query",
  skipCertificatesValidation: true
};

// Use DNS configuration in the session creation.
const sessionWithCustomDns = rcp.createSession({ requestConfiguration: { dns: { dnsRules: customDnsServers } } });
const sessionWithStaticDns = rcp.createSession({
  requestConfiguration: {
    dns: {
      // for example.com, '192.168.1.2' is effective.
      // for sub.example.com, '192.168.2.1' is effective.
      dnsRules: staticDnsRules,
    }
});
const sessionWithDoh = rcp.createSession({ requestConfiguration: { dns: { dnsOverHttps: dohConfig } } });

// Enable happy eyeball in the session creation when dns rules is set.
const sessionWithStaticDnsRulesAndHappyEyeball = rcp.createSession({
  requestConfiguration: {
    dns: {
      dnsRules: staticDnsRules, // Set dns rules here.
      happyEyeballOnDnsRule: true, // Enable happy eyeball here.
    }
});

// Enable happy eyeball in the request configuration when dns rules is set.
const request = new rcp.Request('https://example.com');
request.configuration = {
  dns: {
    dnsRules: staticDnsRules, // Set dns rule here.
    happyEyeballOnDnsRule: true, // Enable happy eyeball here.
  }
};
```

**DnsOverHttpsConfiguration**

允许开发者配置HTTPS上的DNS（DOH）设置，从而通过HTTPS端点实现安全的DNS解析。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | URLOrString | 否 | 否 | DOH端点的URL或字符串表示形式。 |
| skipCertificatesValidation | boolean | 否 | 是 | 指定是否跳过DOH终结点的SSL/TLS证书验证。true代表跳过，false代表不跳过，默认值为false。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

// Configure DNS over HTTPS settings
const dohConfig: rcp.DnsOverHttpsConfiguration = {
  url: "https://dns.example.com/dns-query",
  skipCertificatesValidation: true
};

// Use the DNS over HTTPS configuration in the session creation
const sessionWithDoh = rcp.createSession({ requestConfiguration: { dns: { dnsOverHttps: dohConfig } } });
```

**SecurityConfiguration**

SecurityConfiguration接口允许开发者在会话中配置与安全相关的设置，包括证书和服务器身份验证。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| remoteValidation | 'system' | 'skip' | CertificateAuthority | ValidationCallback | 否 | 是 | 证书颁发机构（CA），用于验证远程服务器的身份。默认值为'system'。 如果未设置此字段，系统CA将被用于验证远程服务器的标识。 'system'：表示使用系统CA配置。 'skip'：跳过验证。 CertificateAuthority：证书颁发机构（CA）验证。 ValidationCallback：自定义证书校验。 说明： 从5.0.0(12)版本开始，新增支持ValidationCallback类型。 |
| certificate | ClientCertificate | 否 | 是 | 发送到远程服务器的客户端证书，用于远程服务器使用其验证委托人的身份证明。默认值为undefined，表示服务器不需要验证客户端。 |
| tlsOptions | 'system' | CipherSuite[] | TlsV13Option | TlsV12Option| TlsV11Option | TlsV10Option | 否 | 是 | TLS版本选择器，用于选择TLS的版本，默认为'system'。 'system'：表示使用系统的TLS版本。 CipherSuite[]：用来声明加密套件的类型的数组。 TlsV13Option：表示使用TLS1.3版本。 TlsV12Option：表示使用TLS1.2版本。 TlsV11Option：表示使用TLS1.1版本。 TlsV10Option：表示使用TLS1.0版本。 起始版本： 5.0.0(12) |
| tlsRange | TlsVersionRangeOptions | 否 | 是 | TLS版本范围配置器，用于设置客户端可使用TLS版本的范围，默认不配置。 起始版本： 6.0.0(20) |
| serverAuthentication | ServerAuthentication | 否 | 是 | 安全连接期间的服务器身份验证配置。默认不认证。 |
| certificatePinning | CertificatePinning| CertificatePinning[] | 否 | 是 | 证书锁定配置。 起始版本： 5.0.0(12) |
| challenge | OnAuthenticationChallenge | 否 | 是 | 自定义认证挑战。 起始版本： 6.1.0(23) |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

// Configure security settings
const securityConfig: rcp.SecurityConfiguration = {
  remoteValidation: "system",
  certificate: {
    content: "-----BEGIN CERTIFICATE-----\n...",
    type: "PEM",
    key: "-----BEGIN PRIVATE KEY-----\n...", // 请根据自身业务选择合适的key
    keyPassword: "your-password"
  },
  serverAuthentication: {
    credential: {
      username: "exampleUser",
      password: "examplePassword"
    },
    authenticationType: "basic"
  }
};

// Use the security configuration in the session creation
const sessionWithSecurityConfig = rcp.createSession({ requestConfiguration: { security: securityConfig } });
```

**CertificateAuthority**

证书颁发机构（CA）用于验证远程服务器的身份。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | ArrayBuffer | 否 | 是 | 用于验证对等方的证书颁发机构证书捆绑包。是PEM格式。 |
| filePath | string | 否 | 是 | 用于验证对等方的证书颁发机构证书文件的路径。该文件应为PEM格式。 |
| folderPath | string | 否 | 是 | 用于验证对等方包含多个CA证书目录的路径。此目录中的文件应为PEM格式。 |

**ClientCertificate**

ClientCertificate接口允许开发者为会话中的安全连接配置与证书相关的设置。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | ArrayBuffer | 否 | 是 | 证书颁发机构（CA）证书的内容。它可以作为字符串或ArrayBuffer提供。 |
| filePath | string | 否 | 是 | 包含证书颁发机构（CA）证书的文件的路径。默认值为undefined。 |
| type | 'PEM' | 'DER' | 'P12' | 否 | 是 | 客户端证书编码格式类型。默认值为undefined。 |
| key | string | 否 | 是 | 客户端证书私钥文件的路径。默认值为undefined。 |
| keyPassword | string | 否 | 是 | 客户端证书密码。默认值为undefined。 |

**ServerAuthentication**

HTTP服务器身份验证。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credential | Credential | 否 | 否 | 服务器的凭证。默认值为undefined。 |
| authenticationType | AuthenticationType | 否 | 是 | 服务器的认证类型。如果没有设置，需与服务器协商。 |

**TlsVersionRangeOptions**

TLS版本可用范围配置属性，开发者能够设置安全相关TLS版本的上限和下限，并指定该范围内加密套件列表。

系统能力：SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| min | TlsVersion | 否 | 是 | TLS可用最小版本，默认不设置，由系统选择。 |
| max | TlsVersion | 否 | 是 | TLS可用最大版本，默认不设置，由系统选择。 |
| cipherSuite | CipherSuite[] | 否 | 是 | TLS可用版本范围内的加密套件列表，默认不设置，由系统选择。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | 当开发者设置TLS最小版本大于最大版本时，系统将抛出该参数错误码。表示Parameter error. |

**OnAuthenticationChallenge**

type OnAuthenticationChallenge = (info: AuthenticationChallengeInfo[], response: Response, challengeCount: number) => ServerAuthentication | null

认证挑战回调函数。开发者可通过此回调函数处理认证挑战。当HTTP响应的状态码为401时，系统会调用此回调函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | AuthenticationChallengeInfo[] | 是 | 认证挑战参数。系统解析响应头中的WWW-Authenticate信息，并将信息转化为键值对。 |
| response | Response | 是 | 此次认证挑战的HTTP响应。 |
| challengeCount | number | 是 | 认证挑战的次数。如果挑战不被服务器认证通过，可能会再次触发认证挑战。系统不限制挑战的次数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ServerAuthentication | null | 返回类型为HTTP服务器的身份验证信息或null。若返回验证信息，系统将使用用户提供的信息进行认证挑战；若返回null，则放弃认证挑战。 |

**AuthenticationChallengeInfo**

type AuthenticationChallengeInfo = Record<string, string>

服务器返回的认证挑战信息。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

| 类型 | 说明 |
| --- | --- |
| Record<string, string> | 从WWW-Authenticate中解析到的认证挑战信息，常见的键包括'type'、'realm'等。 |

**Request**

HTTP请求。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 否 | 请求对象的唯一标识符。由系统生成。 |
| url | URL | 否 | 否 | HTTP请求的URL。 |
| method | HttpMethod | 否 | 否 | 要使用的HTTP方法。默认值为'GET'。 |
| headers | RequestHeaders | 否 | 是 | HTTP请求头。默认值为undefined。 |
| content | RequestContent | 否 | 是 | HTTP请求内容。默认值为undefined。 |
| cookies | RequestCookies | 否 | 是 | HTTP请求的Cookie。将设置转换为HTTP Cookies标头。默认值为undefined。 |
| transferRange | TransferRange | TransferRange[] | 否 | 是 | HTTP传输范围。转换为HTTP Range头。带有range头的HTTP请求要求服务器只返回HTTP响应的一部分。默认值为undefined。 |
| configuration | Configuration | 否 | 是 | HTTP请求配置。用于覆盖默认或会话范围的设置。默认值为undefined。 |
| destination | ResponseBodyDestination | 否 | 是 | HTTP响应体放置位置。 起始版本： 5.0.0(12) |
| cacheControl | CacheControl | 否 | 是 | HTTP请求缓存控制配置。若配置，则SessionConfiguration中的配置的缓存控制不生效。默认值为undefined。 起始版本： 6.0.0(20) |

**constructor**

constructor(url: URLOrString, method?: HttpMethod, headers?: RequestHeaders, content?: RequestContent, cookies?: RequestCookies, transferRange?: TransferRange | TransferRange[], configuration?: Configuration)

提供用于创建Request对象的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | 请求的地址类型，在构造函数中，参数可以是 URLOrString，但 URL 只是 URL，字符串需要转换为URL。 |
| method | HttpMethod | 否 | HTTP 请求方法。默认是GET。 |
| headers | RequestHeaders | 否 | HTTP请求头。 |
| content | RequestContent | 否 | HTTP 请求正文。 |
| cookies | RequestCookies | 否 | HTTP 请求 cookie。该设置将转换为 HTTP Cookies header。 |
| transferRange | TransferRange| TransferRange[] | 否 | HTTP 传输范围。该设置将转换为 HTTP Range header。 |
| configuration | Configuration | 否 | HTTP 请求配置。见Configuration。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let content = "data to send";
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };
let req = new rcp.Request("http://example.com", "POST", headers, content, cookies, transferRange, configuration);
```

**URL**

type URL = url.URL

请求的地址类型，链接到@[ohos.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-url)中的URL。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| url.URL | 表示值的类型为@ohos.url.URL，请求的地址类型，可取任意值。 |

**X509Cert**

type X509Cert = cert.X509Cert

提供 x509 证书类型，链接到@[ohos.security.cert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert)中的X509Cert。

取值范围请见下表。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| cert.X509Cert | 表示值的类型为@ohos.security.cert.X509Cert，可取任意值。 |

**File**

type File = fs.File

文件系统中的文件，链接到@[ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)中的File。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| fs.File | 表示值的类型为@ohos.file.fs.File，可取任意值。 |

**RandomAccessFile**

type RandomAccessFile = fs.RandomAccessFile

可以随机访问的文件，链接到@[ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)中的RandomAccessFile。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| fs.RandomAccessFile | 表示值的类型为@ohos.file.fs.RandomAccessFile，可取任意值。 |

**Stream**

type Stream = fs.Stream

提供数据流的形式，链接到@[ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)中的Stream。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| fs.Stream | 表示值的类型为@ohos.file.fs.Stream，可取任意值。 |

**RawDataContent**

type RawDataContent = string | ArrayBuffer | object

ArkTs的基本类型数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| string | 表示数据以文本字符串的形式存在，可取任意值。 |
| ArrayBuffer | 表示数据以二进制形式存在，可取任意值。 |
| object | 表示数据以对象的形式存在，可取任意值。 |

**FileDescriptor**

type FileDescriptor = number

文件的描述符，用于访问文件或者I/O设备的抽象表示。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| number | 表示值的类型为number，可取任意值。 |

**LocalFile**

type LocalFile = [FileDescriptor](#ZH-CN_TOPIC_0000002522081536__filedescriptor) | [File](#ZH-CN_TOPIC_0000002522081536__file) | [RandomAccessFile](#ZH-CN_TOPIC_0000002522081536__randomaccessfile)

具有文件特性的对象，允许用户使用不同类型的文件描述符或文件对象进行操作。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| FileDescriptor | 表示文件的描述符。文件描述符是一个整数，用于标识一个打开的文件。 |
| File | 文件系统中的文件，用于获取文件的描述符、路径和名称，以及对文件的锁定和解锁操作。 |
| RandomAccessFile | 提供随机访问文件的操作功能。用于处理随机访问文件的一种类型。提供了文件描述符、文件指针的读取，以及文件指针的设置和文件的写入操作。 |

**WriteFile**

提供向文件写入数据的函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**write**

write(buffer: ArrayBuffer): Promise<void | number>

向文件写入数据，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 向文件中写入的数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void | number> | 使用Promise异步回调，返回写入的number类型数据，或者无返回值。 |

**ReadFile**

提供从文件中读取数据的函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**read**

read(buffer: ArrayBuffer): Promise<number>

从文件中读取数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 需要读取数据的文件。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回从文件中读取到的数据，类型为number。 |

**WriteStream**

提供将数据写入流中的函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**write**

write(buffer: ArrayBuffer): Promise<void | number>

从文件中写入数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 需要写入流中的数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void | number> | Promise对象，返回写入的number类型数据，或者无返回值。 |

**SyncWriteStream**

提供同步将数据写入流中的函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**writeSync**

writeSync(buffer: ArrayBuffer): void | number

将数据写入流中。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 需要写入流中的数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回写入的number类型数据。 |

**ReadStream**

提供从流中读取数据的函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**read**

read(buffer: ArrayBuffer): Promise<number>

从流中读取数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 需要写入流中的数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回从文件中读取到的数据，类型为number。 |

**SyncReadStream**

提供同步从流中读取数据的函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**readSync**

readSync(buffer: ArrayBuffer): number

从流中读取数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 需要写入流中的数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回写入的number类型数据。 |

**DownloadedTo**

根据请求，最后的结果将会保存到DownloadToFile指定的路径中。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | Path | 否 | 否 | 如果请求目标（Request.destination）是下载到文件时，path表示文件保存的路径。 |
| requestSkipped | true | 否 | 是 | 当前仅支持true，若配置时选择此项则默认跳过请求，若不想跳过则不必选择此项。 |

**TargetFile**

下载后的数据存放在本地设备的指定目录中，通常是下载文件夹或指定的默认存储位置。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | Path | 否 | 否 | 指定的数据下载路径。 |
| skipRequest | boolean | 否 | 是 | 是否跳过请求，true代表跳过，false代表不跳过，默认值为false。 |

**TargetFileCallback**

type TargetFileCallback = (request: [Request](#ZH-CN_TOPIC_0000002522081536__request), suggestedPath: [Path](#ZH-CN_TOPIC_0000002522081536__path)) => [TargetFile](#ZH-CN_TOPIC_0000002522081536__targetfile) | Promise<[TargetFile](#ZH-CN_TOPIC_0000002522081536__targetfile)>

[TargetFile](#ZH-CN_TOPIC_0000002522081536__targetfile)回调函数，返回一个[TargetFile](#ZH-CN_TOPIC_0000002522081536__targetfile)对象，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 是 | 表示入参的类型为一个HTTP请求。 |
| suggestedPath | Path | 是 | 表示入参的类型为Path，请求中指定的路径。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| TargetFile | Promise<TargetFile> | 直接返回TargetFile，或者使用Promise异步回调，表示下载数据的存放位置，或是默认文件夹。 |

**IncomingDataCallback**

type IncomingDataCallback = (incomingData: ArrayBuffer) => void | Promise<void>

处理下载数据的回调函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incomingData | ArrayBuffer | 是 | 表示需要处理的ArrayBuffer类型数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 表示入参类型为ArrayBuffer，返回空值，使用Promise异步回调。 |

**UploadFromFile**

UploadFromFile表示一种文件上传的方式，允许客户端将本地计算机上的文件上传到服务器。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fileOrPath | Path | LocalFile | ReadFile | 是 | 否 | 表示需要上传的文件或者上传文件的路径，参考应用文件。 |

**constructor**

constructor(fileOrPath: Path | LocalFile | ReadFile)

提供用于创建UploadFromFile对象的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileOrPath | Path | LocalFile | ReadFile | 是 | 表示需要上传的文件或者上传文件的路径，参考应用文件。 |

**UploadFromStream**

UploadFromStream表示以流的形式进行上传操作。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stream | Stream | ReadStream | SyncReadStream | 是 | 否 | 表示需要上传的流。 |

**constructor**

constructor(stream: Stream | ReadStream | SyncReadStream)

提供用于创建UploadFromStream对象的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stream | Stream | ReadStream | SyncReadStream | 是 | 表示需要上传的流。 |

**DownloadToFile**

type DownloadToFile = { kind: 'file'; file: TargetFileCallback; } | { kind: 'file'; file: Path; keepLocal?: boolean; } | { kind: 'file'; file: LocalFile | WriteFile; } | { kind: 'folder'; path: Path; keepLocal?: boolean; }

将文件下载到文件夹或文件中。如果下载到文件夹，文件名将与服务器中的文件名相同。取值范围为以下表中类型的并集。其中，kind 用于指定想要下载到文件或目录，file 指的是具体要下载到的目标文件或目录（参考[应用文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file)）。

取值范围为以下表中类型的并集。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| { kind: 'file'; file: TargetFileCallback; } | 表示键kind的键值为'file'，键file的键值为TargetFileCallback。 |
| { kind: 'file'; file: Path; keepLocal?: boolean; } | 表示键kind的值为'file'，键file的值为Path对象，其中keepLocal为可选参数值，当本地文件名和下载的文件名相同时，不会重复下载。 |
| { kind: 'file'; file: LocalFile| WriteFile; } | 表示键kind的值为'file'，键file的值为LocalFile或WriteFile对象。 |
| { kind: 'folder'; path: Path; keepLocal?: boolean; } | 键kind的值为'folder'，键path的值为Path对象，其中keepLocal为可选参数值，当本地文件夹名和下载的文件夹名相同时，不会重复下载。 |

**DownloadToStream**

type DownloadToStream = { kind: 'stream'; stream: Stream | WriteStream | SyncWriteStream; }

将文件下载到一个数据流中。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| { kind: 'stream'; stream: Stream| WriteStream| SyncWriteStream } | 表示键kind值为'stream'，键stream的值为 Stream或WriteStream或SyncWriteStream的对象。 |

**PausePolicy**

请求的暂停策略。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| receiving | ReceivingPausePolicy | 否 | 是 | 设置暂停响应体接收的策略。 |
| sending | SendingPausePolicy | 否 | 是 | 设置暂停请求体发送的策略。 |

**ReceivingPauseByTimeout**

暂停接收流程的按超时的策略。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'timeout' | 否 | 否 | 策略类型。 |
| timeoutMs | number | 否 | 否 | 超时时间，如果超过了该时间，框架还没从服务端收到数据，就会暂停请求。单位为毫秒。 |

**ReceivingPauseByCache**

暂停接收流程的按缓存的策略。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'cacheSize' | 否 | 否 | 策略类型。 |
| size | number | 否 | 否 | 缓存策略的最大值，框架缓存的数据超过该值，应用一直不处理，就会暂停请求。取值范围[0, 1048576]。 |

**ReceivingPausePolicy**

type ReceivingPausePolicy = ReceivingPauseByCache | ReceivingPauseByTimeout

接收流程的暂停策略。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| ReceivingPauseByCache | 策略的缓存大小。 |
| ReceivingPauseByTimeout | 策略的超时时间。 |

**NetworkOutputQueue**

const NetworkOutputQueue: NetworkOutputQueueConstructor

通过 new NetworkInputQueue()来创建一个[INetworkOutputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkoutputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**NetworkOutputQueueConstructor**

NetworkOutputQueueConstructor是一个[INetworkOutputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkoutputqueue)的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**new**

new (): INetworkOutputQueue

创建一个[INetworkOutputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkoutputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| INetworkOutputQueue | 返回一个同步读队列对象。 |

**new**

new (maxSize: number): INetworkOutputQueue

创建一个[INetworkOutputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkoutputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSize | number | 是 | 队列大小，表示框架可写入的最大字节数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| INetworkOutputQueue | 返回一个同步读队列对象。 |

**new**

new (maxSize: number, pausePolicyOverride: ReceivingPausePolicy): INetworkOutputQueue

创建一个[INetworkOutputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkoutputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSize | number | 是 | 队列大小，表示可写入的最大字节数。 |
| pausePolicyOverride | ReceivingPausePolicy | 是 | 请求的接收暂停策略。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| INetworkOutputQueue | 返回一个同步读队列对象。 |

**INetworkOutputQueue**

INetworkOutputQueue是用读响应体的同步读队列。通过new [NetworkOutputQueue](#ZH-CN_TOPIC_0000002522081536__networkoutputqueue)()来构造。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**read**

read(maxBytesToRead: number): ArrayBuffer

从队列中读取一段数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxBytesToRead | number | 是 | 读取到的数据的最大字节数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 读取到的二进制数据。 |

**readInto**

readInto(buffer: ArrayBuffer): number

将数据从队列中读取并存入指定的缓冲区。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 读到参数中的buffer里面。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 读取的二进制数据的字节数。 |

**getStoredBytes**

getStoredBytes(): number

获取队列中的数据的大小。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 获取队列中的数据的大小。 |

**ResponseBodyDestination**

type ResponseBodyDestination = 'array-buffer'| IncomingDataCallback | DownloadToFile | DownloadToStream | INetworkOutputQueue

ResponseBodyDestination类型指定了响应的目标位置或目的地，指示HTTP客户端应该将响应数据发送到哪个位置。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'array-buffer' | 表示值的类型为'array-buffer'类型数据。默认将响应体写到内存。 |
| IncomingDataCallback | 表示值的类型为IncomingDataCallback类型数据。将响应体写到回调函数中。 |
| DownloadToFile | 表示值的类型为DownloadToFile类型数据。将响应体写到文件中。 |
| DownloadToStream | 表示值的类型为DownloadToStream类型对象。将响应体写到自定义的流中。 |
| INetworkOutputQueue | 表示值的类型为INetworkOutputQueue类型对象。把响应体写到队列。 |

**URLOrString**

type URLOrString = [URL](#ZH-CN_TOPIC_0000002522081536__url) | string

URLOrString类型是表示URL对象或表示URL的字符串的并集类型。可以作为HTTP/HTTPS地址的入参。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| URL | URL对象，可以作为HTTP/HTTPS地址的入参 |
| string | URL的字符串，可以作为HTTP/HTTPS地址的入参 |

**PathPreference**

type PathPreference = 'auto' | 'cellular'

HTTP请求路径偏好设置。此设置仅为开发者的建议，实际使用路径由系统决定。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| 'auto' | 表示系统自动选择路径。 |
| 'cellular' | 表示蜂窝网络路径。 |

**ConnectionReusePolicy**

type ConnectionReusePolicy = 'balanced' | 'forbidden' | 'naive'

HTTP连接复用方式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

| 类型 | 说明 |
| --- | --- |
| 'balanced' | 表示均衡地使用HTTP连接。系统会选择当前负载最低的HTTP连接。 |
| 'forbidden' | 表示禁止连接复用。每次请求都会创建新的HTTP连接。 |
| 'naive' | 表示使用简易的连接复用方式。系统会选择找到的第一个可用的HTTP连接。 |

**IpAddress**

type IpAddress = string

IP地址类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| string | 表示IP地址只是一个字符串。它可以是IPv4字符串或IPv6字符串。 |

**DnsServers**

type DnsServers = IpAndPort[]

DnsServers接口允许开发者在DnsConfiguration中配置DNS设置时，指定自定义DNS服务器。它提供了一种灵活的方式来定义IP地址和相关端口的列表。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| IpAndPort[] | 表示值的类型为IpAndPort数组，数组成员为地址和端口键值对。 |

**IpAndPort**

IpAndPort接口允许开发者定义IP地址和可选端口号。它通常用于需要同时指定IP地址和端口的情况，例如在DnsServers接口中配置自定义DNS服务器时。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ip | IpAddress | 否 | 否 | 要关联的IP地址。IPv4或IPv6地址。 |
| port | number | 否 | 是 | 可选端口号。取值范围[0, 65535]，默认值为53。 |

**ServiceType**

type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser'

网络服务类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| 'default' | 表示默认服务类型，适用于大多数一般性的服务需求。 说明： 除'default'外，其他类型均为5.0.0(12)新增类型。 |
| 'background' | 表示后台服务类型，适用于在后台运行的任务，如定时任务、后台数据同步或推送通知等。 |
| 'realtimeVoice' | 表示实时语音服务类型，适用于实时语音通信，如电话、视频会议或即时通话等。 |
| 'realtimeVideo' | 表示实时视频服务类型，适用于实时视频通信。 |
| 'callSignaling' | 表示呼叫信号服务类型，适用于电话呼叫信号的传输和管理，包括呼叫建立、挂断、转接等操作。 |
| 'realtimeGame' | 表示实时游戏服务类型，适用于实时多人游戏，需要低延迟和高可靠性，以确保玩家之间的同步和游戏体验。 |
| 'normalGame' | 表示普通游戏服务类型，适用于非实时的游戏服务，比如单人游戏、离线游戏或非竞技类游戏。 |
| 'shortVideo' | 表示短视频服务类型，适用于短视频的上传、下载和播放。 |
| 'longVideo' | 表示长视频服务类型，适用于长视频的服务。 |
| 'livestreamingAnchor' | 表示直播播控服务类型，适用于直播平台上的主播端。 |
| 'livestreamingWatcher' | 表示直播观看服务类型，适用于直播平台上的观众端。 |
| 'download' | 表示下载服务类型，适用于资源下载服务。 |
| 'upload' | 表示上传服务类型，适用于上传资源服务。 |
| 'browser' | 表示浏览器服务类型，适 用于浏览器中的网页加载和交互。 |

**HttpMethod**

type HttpMethod = 'GET' | 'POST' | 'HEAD' | 'PUT' | 'DELETE' | 'PATCH' | 'OPTIONS' | (string & NonNullable<unknown>)

HttpMethod是HTTP库中的一种类型，代表网络请求中使用的各种HTTP方法。HTTP方法定义了要对给定资源执行的操作。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| 'GET' | 表示网络请求的方式为GET，通常用于从服务器获取数据，如获取网页、图片、API 数据等。 |
| 'POST' | 表示网络请求的方式为POST，通常用于向服务器发送数据，如提交表单、上传文件等。 |
| 'HEAD' | 表示网络请求的方式为HEAD，类似于 GET 请求，但只请求资源的头部信息，不返回资源本身。通常用于检查资源是否存在、获取资源的元数据等。 |
| 'PUT' | 表示网络请求的方式为PUT，通常用于更新服务器上的现有资源。 |
| 'DELETE' | 表示网络请求的方式为DELETE，通常用于删除服务器上的资源。 |
| 'PATCH' | 表示网络请求的方式为PATCH，通常用于对现有资源进行部分更新。 |
| 'OPTIONS' | 表示网络请求的方式为OPTIONS，可查询目标资源的通信选项。通常用于跨域请求，询问服务器支持哪些 HTTP 方法。 |
| (string & NonNullable<unknown>) | 用以确保 HttpMethod 类型的值必须是非空字符串。 |

**RequestHeaders**

type RequestHeaders = { [k: string]: string | string[] | undefined; 'authorization'?: string; 'accept'?: ContentType | ContentType[]; 'accept-charset'?: string | string[]; 'accept-encoding'?: ContentCoding | ContentCoding[]; 'accept-language'?: string | string[]; 'cache-control'?: string | string[]; 'cookie'?: string | string[]; 'range'?: string | string[]; 'upgrade'?: string | string[]; 'user-agent'?: string; 'content-type'?: ContentType; }

定义请求头类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| { [k: string]: string | string[] | undefined; 'authorization'?: string; 'accept'?: ContentType | ContentType[]; 'accept-charset'?: string | string[]; 'accept-encoding'?: ContentCoding | ContentCoding[]; 'accept-language'?: string | string[]; 'cache-control'?: string | string[]; 'cookie'?: string | string[]; 'range'?: string | string[]; 'upgrade'?: string | string[]; 'user-agent'?: string; 'content-type'?: ContentType; } | 若键取值为[k: string]: string | string[] | undefined，表示值类型为一个包含一个或多个键值对的对象，其键的类型为字符，可取任意值，其值的类型为字符、字符数组或undefined。 若键取值为'authorization'，值的类型为字符，可取任意值。 若键取值为'accept'，值的类型为ContentType或ContentType数组，可取任意值。 若键取值为'accept-charset'，值的类型为字符或字符数组，可取任意值。 若键取值为'accept-encoding'，值的类型为ContentCoding或ContentCoding数组，可取任意值。 若键取值为'accept-language'，值的类型为字符或字符数组，可取任意值。 若键取值为'cache-control'，值的类型为字符或字符数组，可取任意值。 若键取值为'cookie'，值的类型为字符或字符数组，可取任意值。 若键取值为'range'，值的类型为字符或字符数组，可取任意值。 若键取值为'upgrade'，值的类型为字符或字符数组，可取任意值。 若键取值为'user-agent'，值的类型为字符，可取任意值。 若键取值为'content-type'，值的类型为ContentType，可取任意值。当此项不存在或为空字符串时，系统将根据RequestContent配置默认的内容类型。若不希望使用默认内容类型，可以传入单个空格。 |

**SendingPausePolicy**

暂停发送流程的策略。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'timeout' | 否 | 否 | 策略类型。 |
| timeoutMs | number | 否 | 否 | 超时时间，如果超过了该时间，应用还没有给框架数据，就会暂停请求，单位为毫秒。 |

**NetworkInputQueue**

const NetworkInputQueue: NetworkInputQueueConstructor

通过 new NetworkInputQueue()来创建一个[INetworkInputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkinputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**NetworkInputQueueConstructor**

NetworkInputQueueConstructor是一个[INetworkInputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkinputqueue)的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**new**

new (): INetworkInputQueue

创建一个[INetworkInputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkinputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| INetworkInputQueue | 返回一个同步写队列对象。 |

**new**

new (maxSize: number): INetworkInputQueue

创建一个[INetworkInputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkinputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSize | number | 是 | 队列大小，表示可写入的最大字节数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| INetworkInputQueue | 返回一个同步写队列对象。 |

**new**

new (maxSize: number, pausePolicyOverride: SendingPausePolicy): INetworkInputQueue

创建一个[INetworkInputQueue](#ZH-CN_TOPIC_0000002522081536__inetworkinputqueue)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSize | number | 是 | 队列大小，表示可写入的最大字节数。 |
| pausePolicyOverride | SendingPausePolicy | 是 | 请求的发送暂停策略。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| INetworkInputQueue | 返回一个同步写队列对象。 |

**INetworkInputQueue**

INetworkInputQueue是用于写请求体的同步写队列。通过new [NetworkInputQueue](#ZH-CN_TOPIC_0000002522081536__networkinputqueue)()来构造。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**write**

write(buffer: string | ArrayBuffer): void

将一段数据写入队列当中，框架的IO线程会在合适的时候把该数据发送出去。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | string | ArrayBuffer | 是 | 要发送的请求。 |

**close**

close(): void

关闭此同步写队列，IO线程不再从该队列读取数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**getFreeSpace**

getFreeSpace(): number

获取剩余可写空间。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 获取剩余可写空间。 |

**RequestContent**

type RequestContent = RawDataContent | Form | MultipartForm | GetDataCallback | UploadFromFile | UploadFromStream | INetworkInputQueue

RequestContent是HTTP模块中的一种类型，代表HTTP请求的内容。它可以有多种形式，可以灵活指定请求中要发送的数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| RawDataContent | ArkTs的基本类型的数据。 |
| Form | HTTP简单的表格数据。 |
| MultipartForm | HTTP多部分表格数据。 |
| GetDataCallback | 获取任意数据的回调方法的类型，其入参为数据最大字节数。 |
| UploadFromStream | UploadFromStream表示以流的形式进行上传操作。 起始版本： 5.0.0(12) |
| UploadFromFile | UploadFromFile表示一种文件上传的方式，允许客户端将本地计算机上的文件上传到服务器。 起始版本： 5.0.0(12) |
| INetworkInputQueue | INetworkInputQueue是用于写请求体的同步写队列。 起始版本： 5.0.0(12) |

**Form**

HTTP简单的表格数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fields | FormFields | 否 | 否 | HTTP简单表单数据字段，类型为表单字段类型。 |
| keys | string[] | 否 | 是 | 指定表单中key的发送顺序。 指定后按keys列表的先后顺序发送（不在列表中的key不发送）；不指定默认按各个key的hash顺序发送。 起始版本： 6.0.1(21) |

**constructor**

constructor(fields: FormFields)

提供用于创建Form对象的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | FormFields | 是 | HTTP简单表单数据字段，类型为表单字段类型。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };

const simpleForm = new rcp.Form({
  "key1": "value1",
  "key2": ["valueList0", "valueList1"],
});
simpleForm.keys = ["key2", "key1"];
let req = new rcp.Request("http://example.com", "POST", headers, simpleForm, cookies, transferRange, configuration);
req.content = simpleForm;
```

**MultipartForm**

HTTP多部分表格数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fields | MultipartFormFields | 否 | 否 | 表示多部分表单数据，其中值为多表单字段类型。 |
| boundary | string | 否 | 是 | 多表单中自定义分隔符，开发者可在上传多表单时通过自定义boundary字段实现对表单数据的准确分隔与传输。boundary长度不超过46字符，否则抛出参数错误码。 起始版本： 5.1.0(18) |
| keys | string[] | 否 | 是 | 定义多部分表单中的键顺序。 指定后按keys列表的先后顺序发送（不在列表中的key不发送）；不指定默认按各个key的hash顺序发送。 起始版本： 6.0.1(21) |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**constructor**

constructor(fields: MultipartFormFields)

提供用于创建MultipartForm对象的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | MultipartFormFields | 是 | 表示多部分表单数据，其中值为多表单字段类型。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };

const multiForm = new rcp.MultipartForm({
  "key1": "value1",
  "key2": ["valueList0", "valueList1"],
  "key3": {
    contentType: "text/plain",
    remoteFileName: "RemoteFileName",
    contentOrPath: "/file/to/Path",
  },
});
multiForm.keys = ["key3", "key1", "key2"];
let req = new rcp.Request("http://example.com", "POST", headers, multiForm, cookies, transferRange, configuration);
req.content = multiForm;
```

**constructor**

constructor(fields: MultipartFormFields, boundary: string)

提供用于创建MultipartForm对象的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | MultipartFormFields | 是 | 表示多部分表单数据，其中值为多表单字段类型。 |
| boundary | string | 是 | 多表单中自定义分隔符，开发者可在上传多表单时通过自定义boundary字段实现对表单数据的准确分隔与传输。若boundary长度超过46字符，抛出参数错误码。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };
let Boundary: string = "--MULTIPARTFORM BEGIN AND END BOUNDARY"

const multiForm = new rcp.MultipartForm({
  "key1": "value1",
  "key2": ["valueList0", "valueList1"],
  "key3": {
    contentType: "text/plain",
    remoteFileName: "RemoteFileName",
    contentOrPath: "/file/to/Path",
  },
}, Boundary)
multiForm.keys = ["key3", "key1", "key2"];

let req = new rcp.Request("http://example.com", "POST", headers, multiForm, cookies, transferRange, configuration);
req.content = multiForm;
```

**MultipartFormFields**

type MultipartFormFields = { [k: string]: MultipartFormFieldValue | MultipartFormFieldValue[]; }

HTTP多部分表单数据字段。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| { [k: string]: MultipartFormFieldValue | MultipartFormFieldValue[] } | 表示值的类型为一个或者多个多部分表单数据字段值，值的类型为MultipartFormFieldValue或MultipartFormFieldValue的数组，可取任意值。 |

**MultipartFormFieldValue**

type MultipartFormFieldValue = FormFieldValue | FormFieldFileValue

HTTP多部分表单数据字段值。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| FormFieldValue | 表示值的类型为FormFieldValue，HTTP简单表单数据字段值。 |
| FormFieldFileValue | 表示值的类型为FormFieldFileValue，文件表单数据接口。 |

**FormFields**

type FormFields = { [k: string]: FormFieldValue | FormFieldValue[]; }

HTTP简单表单数据字段。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| { [k: string]: FormFieldValue | FormFieldValue[] } | 表示值的类型为简单表单字段或对应数组。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const simpleForm: rcp.FormFields = {
  "key1": "value1",
  "key2": ["valueList0", "valueList1"],
};
```

**FormFieldValue**

type FormFieldValue = string | number | boolean | bigint

HTTP简单表单数据字段值。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| string | 表示字段的值是一个字符串。 |
| number | 表示字段的值是一个数字，可以是整数或浮点数。如传入的数据大于2147483647，请使用bigint类型。 |
| boolean | 表示字段的值是一个布尔值。 |
| bigint | 表示字段的值是一个大整数。使用此类型传入大于32位的整数。 |

**Path**

type Path = string

HTTP表单数据内容中的文件路径类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| string | 表示值的类型为string，可取任意值。 |

**FileContent**

HTTP表单数据内容中的文件内容类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | ArrayBuffer | 否 | 否 | 要发送到远程服务器的内容，可取任意值。 |

**FormFieldFileValue**

文件表单数据接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | ContentType | 否 | 是 | HTTP多部分表单数据内容类型。默认值为undefined。 |
| remoteFileName | string | 否 | 是 | 保存到远程服务器的文件名。默认值为undefined。 |
| contentOrPath | Path | FileContent | GetDataCallback | 否 | 否 | 要发送到远程服务器的内容或文件路径。具体允许的类型见链接。 |

示例

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const formFieldFileValue: rcp.FormFieldFileValue = {
  contentType: "image/png",
  remoteFileName: "remoteFile1",
  contentOrPath: "/path/to/file",
};
```

**RequestCookies**

RequestCookies是HTTP模块中的一个接口，用于表示HTTP请求中包含的cookie。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [name: string] | string | 否 | 否 | Cookies数据。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const cookies: rcp.RequestCookies = {
  "sessionID": "abc123",
  "userToken": "xyz789",
  // Additional cookies can be added here
};
```

**TransferRange**

设置传输数据范围。HTTP范围请求要求服务器只将HTTP消息的一部分发回客户端。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| from | number | 否 | 是 | 用于设置传输数据的起始字节。默认值为undefined。 |
| to | number | 否 | 是 | 用于设置传输数据的结束字节。默认值为undefined。 |

**Response**

HTTP请求的响应数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | Request | 是 | 否 | 收到此响应的相关HTTP请求内容。 |
| statusCode | number | 是 | 否 | HTTP请求的结果代码。如果回调函数成功执行，将返回ResponseCode中定义的结果代码。否则，将在AsyncCallback中的error字段中返回错误代码。 |
| headers | ResponseHeaders | 是 | 否 | 响应头。 |
| effectiveUrl | URL | 是 | 是 | 重定向后请求的有效URL。默认值为undefined。 |
| body | ArrayBuffer | 是 | 是 | 响应内容根据响应头中的Content-type返回。响应内容必须与服务器返回的数据类型相同。默认最大下载字节数是50M。如果超过50M，为了防止内存溢出，请通过OnDataReceive来流式接收数据。 |
| downloadedTo | DownloadedTo | 是 | 是 | 内容下载的路径。在使用下载至文件对象和文件标识符两种方式时，默认情况下，并未设置回调信息。 起始版本： 5.0.0(12) |
| debugInfo | DebugInfo[] | 是 | 是 | 与响应相关联的调试信息。默认值为undefined。 |
| timeInfo | TimeInfo | 是 | 是 | HTTP请求各阶段的定时信息。默认值为undefined。 |
| cookies | ResponseCookie[] | 是 | 是 | 响应中的Cookie数组。 |
| httpVersion | HttpVersion | 是 | 是 | HTTP的版本。 起始版本： 5.0.0(12) |
| reasonPhrase | string | 是 | 是 | HTTP响应状态行的reasonPhrase，提供与数字状态代码相关的文本描述。 起始版本： 5.0.0(12) |
| cacheInfo | CacheInfo | 是 | 是 | 缓存信息，包含缓存已存在时长、原始HTTP请求ID信息。当HTTP响应从缓存中获取时，该属性有值，否则为undefined。 起始版本： 6.0.0(20) |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

// 以下为如何修改response，仅供参考
interface ChangeableResponse {
  request: rcp.Request;
  statusCode: number;
  headers: rcp.ResponseHeaders;
  effectiveUrl?: rcp.URL;
  body?: ArrayBuffer;
  downloadedTo?: rcp.DownloadedTo;
  debugInfo?: rcp.DebugInfo[];
  timeInfo?: rcp.TimeInfo;
  cookies?: rcp.ResponseCookie[];
  httpVersion?: rcp.HttpVersion;
  reasonPhrase?: string;
  cacheInfo?: rcp.CacheInfo;
}

async function TestRcp() {
  const session = rcp.createSession();
  const resp = await session.get('https://www.example.com');
  const changeableResponse = resp as ChangeableResponse;
  changeableResponse.headers = HEADERS // 此处请自行定义
  changeableResponse.statusCode = STATUSCODE // 此处请自行定义
}
```

**toString**

toString(): string | null

将响应正文转换为字符串。如果转换失败，则返回空值。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| string | null | 如果HTTP响应体不是UTF-8格式，则返回UTF-8格式字符串；或者返回null。 |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
const request = new rcp.Request("https://www.example.com");
session.fetch(request).then((response: rcp.Response) => {
  if (response) {
    console.info("response: " + response.toString());
  }
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**toJSON**

toJSON(): object | null

返回默认的JSON反序列化结果，如需要定制JSON反序列化方式，请参考[JSON解析与生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| object | null | 如果没有异常，则返回带有toString()的JSON格式字符串，toJSON是针对body的，如果body不是JSON那么返回值会是null。 |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
const request = new rcp.Request("https://www.example.com");
session.fetch(request).then((response: rcp.Response) => {
  if (response) {
    console.info("response: ", response.toJSON());
  }
}).catch((err: BusinessError) => {
  console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
});
```

**toJSON**

toJSON(param: json.ParseOptions): object | null

根据解析配置对[toString](#ZH-CN_TOPIC_0000002522081536__tostring)方法返回的字符串进行JSON解析，并返回解析后的结果。详情请参阅[JSON解析与生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json)的详细介绍。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | json.ParseOptions | 是 | 解析配置项。支持定义处理BigInt的模式。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| object | null | 对通过toString()方法转换后的字符串进行JSON解析的结果，如果解析过程中发生异常，则返回null。toJSON方法用于处理body，当body不是JSON格式时，返回值同样为null。 |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import json from '@ohos.util.json';

const session = rcp.createSession();
const request = new rcp.Request("https://www.example.com");
session.fetch(request).then((response: rcp.Response) => {
  if (response) {
    const obj = response.toJSON({ bigIntMode: json.BigIntMode.PARSE_AS_BIGINT }); // 此处仅为示意，实际response的body应为JSON格式，且可能包含大整型数据
    console.info(`response json result: ${JSON.stringify(obj)}`);
  }
}).catch((err: Error) => {
  console.error(`err: err is ${JSON.stringify(err)}`);
});
```

**ResponseSendable**

HTTP请求的响应数据，该响应数据支持Sendable。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestId | string | 是 | 否 | 待发送请求的序列号。 |
| statusCode | number | 是 | 否 | HTTP请求的结果码。 |
| headers | ResponseHeaders | 是 | 否 | 响应头。 |
| effectiveUrl | string | 是 | 是 | 重定向后请求的有效URL字符串。默认值为undefined。 |
| body | ArrayBuffer | 是 | 是 | 响应内容将依据响应头中的content-type返回，并且必须与服务器返回的数据类型相匹配。 |
| downloadedTo | DownloadedTo | 是 | 是 | 内容下载的路径，在使用下载至文件对象和文件标识符两种方式时，默认情况下，不设置回调信息。 |
| debugInfo | DebugInfo[] | 是 | 是 | 与响应相关联的调试信息，默认值为undefined。 |
| timeInfo | TimeInfo | 是 | 是 | HTTP请求各阶段的定时信息，默认值为undefined。 |
| cookies | ResponseCookie[] | 是 | 是 | 响应中的Cookie数组。 |
| httpVersion | HttpVersion | 是 | 是 | HTTP的版本。 |
| reasonPhrase | string | 是 | 是 | 提供HTTP请求结果代码的文本描述。 |
| cacheInfo | CacheInfo | 是 | 是 | 缓存信息，包含缓存已存在时长、原始HTTP请求ID信息。当HTTP响应从缓存中获取时，该属性有值，否则为undefined。 |

**ResponseHeaders**

type ResponseHeaders = { [k: string]: string | string[] | undefined; 'accept-ranges'?: 'none' | 'bytes' | (string & NonNullable<unknown>); 'allow'?: HttpMethod | HttpMethod[]; 'cache-control'?: string | string[]; 'content-encoding'?: ContentCoding; 'content-range'?: string; 'content-type'?: ContentType; 'date'?: string; 'etag'?: string; 'expires'?: string; 'location'?: string; 'retry-after'?: string; 'set-cookie'?: string | string[]; 'server'?: string; 'www-authenticate'?: string | string[]; }

定义响应头类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| { [k: string]: string | string[] | undefined; 'accept-ranges'?: 'none' | 'bytes' | (string & NonNullable<unknown>); 'allow'?: HttpMethod | HttpMethod[]; 'cache-control'?: string | string[]; 'content-encoding'?: ContentCoding; 'content-range'?: string; 'content-type'?: ContentType; 'date'?: string; 'etag'?: string; 'expires'?: string; 'location'?: string; 'retry-after'?: string; 'set-cookie'?: string | string[]; 'server'?: string; 'www-authenticate'?: string | string[]; } | 若键取值为[k: string]: string | string[] | undefined，表示值类型为一个包含一个或多个键值对的对象，其键的类型为字符，可取任意值，其值的类型为字符、字符数组或undefined。 'accept-ranges'表示响应头accept-ranges数据。 若键的值为'allow'，值的类型为HttpMethod或者HttpMethod[]，可取任意值。 若键取值为'cache-control'，值的类型为字符串或字符串数组，可取任意值。 若键的值为'content-encoding'，值的类型为ContentCoding，可取任意值。 若键的值为'content-range'，值的类型为字符串，可取任意值。 若键的值为'content-type'，值的类型为ContentType，可取任意值。 若键的值为'date'，值的类型为字符串，可取任意值。 若键的值为'etag'，值的类型为字符串，可取任意值。 若键的值为'expires'，值的类型为字符串，可取任意值。 若键的值为'location'，值的类型为字符串，可取任意值。 若键的值为'retry-after'，值的类型为字符串，可取任意值。 若键的值为'set-cookie'，值的类型为字符串或字符串数组，可取任意值。 若键的值为'server'，值的类型为字符串，可取任意值。 若键的值为'www-authenticate'，值的类型为字符串或字符串数组，可取任意值。 |

**ResponseCookie**

HTTP响应的cookie接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | cookie的名称。 |
| value | string | 否 | 是 | cookie的值。 |
| domain | string | 否 | 是 | cookie的域。 |
| path | string | 否 | 是 | cookie的路径。 |
| expires | string | 否 | 是 | cookie的过期日期。 |
| maxAge | number | 否 | 是 | cookie的最大保存时间，单位为秒。 |
| isSecure | true | 否 | 是 | 指定cookie是否只能通过安全连接发送。默认值为true。 |
| httpOnly | true | 否 | 是 | 指定cookie是否只能通过HTTP请求访问。默认值为true。 |
| sameSite | string | 否 | 是 | sameSite属性，指定何时在跨站请求中发送cookie。 |
| rawSize | number | 否 | 是 | cookie的大小。 |
| cookieAttributes | CookieAttributes | 否 | 是 | 响应cookie中的所有属性。 |

**DebugInfo**

请求/响应处理调试信息的接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | DebugEvent | 否 | 否 | 调试信息的类型。具体类型值见类型链接。 |
| data | ArrayBuffer | 否 | 否 | 调试信息的数据。 |

**HttpVersion**

type HttpVersion = '1.0' | '1.1' | '2' | '3' | 'unknown'

HTTP的版本。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| '1.0' | 表示值的类型为字符串，'1.0'代表HTTP版本为1.0。 |
| '1.1' | 表示值的类型为字符串，'1.1'代表HTTP版本为1.1。 |
| '2' | 表示值的类型为字符串，'2'代表HTTP版本为2。 |
| '3' | 表示值的类型为字符串，'3'代表HTTP版本为3。 |
| 'unknown' | 表示值的类型为字符串'unknown'。 |

**TimeInfo**

HTTP请求各阶段相关的时间信息的接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nameLookupTimeMs | number | 否 | 否 | DNS解析所需的时间，单位为毫秒。 |
| connectTimeMs | number | 否 | 否 | 建立连接时间，单位为毫秒。 |
| tlsHandshakeTimeMs | number | 否 | 否 | 从开始到远程主机（或代理）的 TLS 握手完成的时间（以毫秒为单位）。 起始版本： 5.0.0(12) |
| preTransferTimeMs | number | 否 | 否 | 传输开始前的时间，单位为毫秒。 |
| startTransferTimeMs | number | 否 | 否 | 传输开始时间，单位为毫秒。 |
| totalTimeMs | number | 否 | 否 | 请求总耗时，单位为毫秒。 |
| redirectTimeMs | number | 否 | 否 | 重定向所需的时间，单位为毫秒。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

TimeInfo时间线：请求开始 （0时刻） -> nameLookupTimeMs（DNS解析）-> connectTimeMs（建立连接）-> tlsHandshakeTimeMs（TLS握手）-> preTransferTimeMs（请求业务数据发送到服务器的时间点） -> startTransferTimeMs（从服务器接收到首包数据的时间点），各时间节点所显示的时间均相对于0时刻，即从0时刻开始计时的时间。例如tlsHandshakeTimeMs为150.1ms，指从发起请求时间0开始，直到TLS握手结束所花费的时间为150.1ms。

网络请求过程中关键节点时间计算方法：

-

首包耗时：startTransferTimeMs - preTransferTimeMs

-

TLS握手（不包含建连时间）耗时：tlsHandshakeTimeMs - connectTimeMs

-

接收剩余数据的耗时：totalTimeMs - startTransferTimeMs

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1、创建session、requestURL
const session = rcp.createSession();
const requestURL = "https://www.example.com";

// 2、在需要跟踪分析请求过程中各个时间段消耗的时间，请将此开关打开
const configuration: rcp.Configuration = {
  tracing: {
    collectTimeInfo: true
  }

// 3、创建请求
const request = new rcp.Request(requestURL, "GET");
request.configuration = configuration;

// 4、使用fetch发起网络请求，request中携带上面配置好的configuration
session.fetch(request).then((response: rcp.Response) => {
// 由于timeInfo中各个参数有可能为undefined，所以需要在两个时间段做运算前添加判空操作
  if (!response.timeInfo) {
    console.error(`TimeInfo is undefined ${response.timeInfo}`);
    return;
  }
  let remainderDataTime = response.timeInfo?.totalTimeMs - response.timeInfo?.startTransferTimeMs;
  let firstPackageTime = response.timeInfo?.startTransferTimeMs - response.timeInfo?.preTransferTimeMs;
  let TLSTime = response.timeInfo?.tlsHandshakeTimeMs - response.timeInfo?.connectTimeMs;

  console.info(`首包耗时${firstPackageTime}`);
  console.info(`TLS握手（不包含建连时间）耗时${TLSTime}`);
  console.info(`接收剩余数据的耗时${remainderDataTime}`);
}).catch((err: BusinessError) => {
  console.error(`Response err, the err is ${JSON.stringify(err)}`);
})
```

**CookieAttributes**

type CookieAttributes = { [k: string]: string | undefined; }

Cookie属性类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| { [k: string]: string | undefined; } | 表示值的类型为一个包含一个或多个键值对的对象。其中键的类型为字符，可取任意值，值的类型为字符或者undefined，可取任意值。 |

**ContentType**

type ContentType = 'application/json' | 'text/plain' | 'multipart/form-data' | 'application/octet-stream' | 'application/x-www-form-urlencoded' | (string & NonNullable<unknown>)

定义内容类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| 'application/json' | 'application/json': 表示数据内容的类型为json字符串。 |
| 'text/plain' | 'text/plain': 表示数据内容的类型为文本数据。 |
| 'multipart/form-data' | 'multipart/form-data': 表示数据内容的类型为表单数据。 |
| 'application/octet-stream' | 'application/octet-stream': 表示数据内容的类型为二进制数据流。 |
| 'application/x-www-form-urlencoded' | 'application/x-www-form-urlencoded': 表示数据内容的类型为表单数据。 |
| (string & NonNullable<unknown>) | string & NonNullable<unknown>：表示值的类型为字符，可取任意非空字符。 |

**ValidationContext**

证书上下文。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pemCerts | string[] | 否 | 否 | PEM格式证书。 |
| x509Certs | X509Cert[] | 否 | 否 | X509证书对象。 |
| host | string | 否 | 否 | 建立连接的服务器的域名。 |
| ip | string | 否 | 否 | 建立连接的服务器的IP地址。 |

**ValidationCallback**

type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>

自定义证书校验函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | ValidationContext | 是 | 表示值的类型为context，是证书上下文。 |

返回值：

| 取值范围 | 说明 |
| --- | --- |
| boolean | Promise<boolean> | 返回一个布尔值表示是否校验成功，或以Promise形式异步调用；返回Promise.reject()也表示校验失败。 |

**TlsV13SpecificCipherSuite**

type TlsV13SpecificCipherSuite = 'TLS_AES_128_GCM_SHA256' | 'TLS_AES_256_GCM_SHA384' | 'TLS_CHACHA20_POLY1305_SHA256'

TLS1.3及以上版本支持的加密套件。本框架有内置的优先顺序，且用户自身的选择也会被记录。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'TLS_AES_128_GCM_SHA256' | 表示值的类型为字符，可取'TLS_AES_128_GCM_SHA256'。 |
| 'TLS_AES_256_GCM_SHA384' | 表示值的类型为字符，可取'TLS_AES_256_GCM_SHA384'。 |
| 'TLS_CHACHA20_POLY1305_SHA256' | 表示值的类型为字符，可取'TLS_CHACHA20_POLY1305_SHA256'。 |

**TlsV12SpecificCipherSuite**

type TlsV12SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256' | 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256' | 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384' | 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384' | 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256' | 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256' | 'TLS_RSA_WITH_AES_128_GCM_SHA256' | 'TLS_RSA_WITH_AES_256_GCM_SHA384';

TLS1.2及以上版本支持的加密套件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256' | 表示值的类型为字符串，可取'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256'。 |
| 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256' | 表示值的类型为字符串，可取'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256'。 |
| 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384' | 表示值的类型为字符串，可取'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384'。 |
| 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384' | 表示值的类型为字符串，可取'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384'。 |
| 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256' | 表示值的类型为字符串，可取'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256'。 |
| 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256' | 表示值的类型为字符串，可取'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256'。 |
| 'TLS_RSA_WITH_AES_128_GCM_SHA256' | 表示值的类型为字符串，可取'TLS_RSA_WITH_AES_128_GCM_SHA256'。 |
| 'TLS_RSA_WITH_AES_256_GCM_SHA384' | 表示值的类型为字符串，可取'TLS_RSA_WITH_AES_256_GCM_SHA384'。 |

**TlsV10SpecificCipherSuite**

type TlsV10SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA' | 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA' | 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA' | 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA' | 'TLS_RSA_WITH_AES_128_CBC_SHA' | 'TLS_RSA_WITH_AES_256_CBC_SHA' | 'TLS_RSA_WITH_3DES_EDE_CBC_SHA'

TLS1.0及以上版本支持的加密套件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA' | 表示值的类型为字符串，可取'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA'。 |
| 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA' | 表示值的类型为字符串，可取'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA'。 |
| 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA' | 表示值的类型为字符串，可取'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA'。 |
| 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA' | 表示值的类型为字符串，可取'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA'。 |
| 'TLS_RSA_WITH_AES_128_CBC_SHA' | 表示值的类型为字符串，可取'TLS_RSA_WITH_AES_128_CBC_SHA'。 |
| 'TLS_RSA_WITH_AES_256_CBC_SHA' | 表示值的类型为字符串，可取'TLS_RSA_WITH_AES_256_CBC_SHA'。 |
| 'TLS_RSA_WITH_3DES_EDE_CBC_SHA' | 表示值的类型为字符串，可取'TLS_RSA_WITH_3DES_EDE_CBC_SHA'。 |

**CipherSuite**

type CipherSuite = TlsV13CipherSuite

加密套件声明函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| TlsV13CipherSuite | 表示值的类型为TlsV13CipherSuite。 |

**TlsV13CipherSuite**

type TlsV13CipherSuite = TlsV12CipherSuite | TlsV13SpecificCipherSuite

TLS1.3的加密套件声明函数，支持TLS1.3版本，兼容TLS1.2版本。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| TlsV12CipherSuite | 表示值的类型为TlsV12CipherSuite。 |
| TlsV13SpecificCipherSuite | 表示值的类型为TlsV13SpecificCipherSuite。 |

**TlsV12CipherSuite**

type TlsV12CipherSuite = TlsV11CipherSuite | TlsV12SpecificCipherSuite

TLS1.2的加密套件声明函数，支持TLS1.2版本，兼容TLS1.1版本。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| TlsV11CipherSuite | 表示值的类型为TlsV11CipherSuite。 |
| TlsV12SpecificCipherSuite | 表示值的类型为TlsV12SpecificCipherSuite。 |

**TlsV11CipherSuite**

type TlsV11CipherSuite = TlsV10CipherSuite

TLS1.1的加密套件声明函数，与TLS1.0相同。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| TlsV10CipherSuite | 表示值的类型为TlsV10CipherSuite。 |

**TlsV10CipherSuite**

type TlsV10CipherSuite = TlsV10SpecificCipherSuite

TLS1.0的加密套件声明函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| TlsV10SpecificCipherSuite | 表示值的类型为TlsV10SpecificCipherSuite。 |

**TlsV13Option**

TLS1.3选择器，用来选择Tls的使用版本，以及配套加密套件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tlsVersion | 'TlsV1.3' | 否 | 否 | TLS版本为"TlsV1.3"。 |
| cipherSuite | TlsV13CipherSuite[] | 否 | 是 | TLS1.3版本对应的加密套件。 |

**TlsV12Option**

TLS1.2选择器，用来选择Tls的使用版本，以及配套加密套件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tlsVersion | 'TlsV1.2' | 否 | 否 | TLS版本为'TlsV1.2'。 |
| cipherSuite | TlsV12CipherSuite[] | 否 | 是 | TLS1.2版本对应的加密套件。 |

**TlsV11Option**

TLS1.1选择器，用来选择Tls的使用版本，以及配套加密套件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tlsVersion | 'TlsV1.1' | 否 | 否 | TLS版本为'TlsV1.1'。 |
| cipherSuite | TlsV11CipherSuite[] | 否 | 是 | TLS1.1版本对应的加密套件。 |

**TlsV10Option**

TLS1.0选择器，用来选择Tls的使用版本，以及配套加密套件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tlsVersion | 'TlsV1.0' | 否 | 否 | TLS版本为'TlsV1.0'。 |
| cipherSuite | TlsV10CipherSuite[] | 否 | 是 | TLS1.0版本对应的加密套件。 |

**ContentCoding**

type ContentCoding = 'aes128gcm' | 'br' | 'compress' | 'deflate' | 'exi' | 'gzip' | 'pack200-gzip' | 'x-compress' | 'x-gzip' | 'zstd' | (string & NonNullable<unknown>)

预定义内容编码类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 取值范围 | 说明 |
| --- | --- |
| 'aes128gcm' | 表示使用AES-128-GCM加密算法对内容进行编码，用于对称加密。 |
| 'br' | 表示使用Brotli算法对内容进行编码，适用于需要高压缩比的场景，如网页、文档等。 |
| 'compress' | 表示使用Unix compress算法对内容进行编码。 |
| 'deflate' | 表示使用DEFLATE算法对内容进行编码，适用于需要高压缩比和较快压缩速度的场景。 |
| 'exi' | 表示使用XML扩展格式（EXI）对内容进行编码，适用于需要高压缩比的XML数据传输。 |
| 'gzip' | 表示使用GZIP算法对内容进行编码，广泛用于Web服务器和应用中。 |
| 'pack200-gzip' | 表示使用Pack200和GZIP算法对内容进行编码。 |
| 'x-compress' | 表示使用Zlib的compress方法对内容进行编码。 |
| 'x-gzip' | 表示使用Zlib的gzip方法对内容进行编码，gzip方法使用DEFLATE压缩算法，提供了高压缩比和较快压缩速度。 |
| 'zstd' | 表示使用Zstandard算法对内容进行编码，适用于需要高压缩比的场景，如数据库、文件压缩等。 |
| (string & NonNullable<unknown>) | 用以确保ContentCoding类型的值必须是非空字符串。 |

**ResponseValidationCallback**

type ResponseValidationCallback = (response: Response) => boolean | Promise<boolean>

响应校验回调函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | Response | 是 | 框架传入的响应，即需要进行校验的响应。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | Promise<boolean> | 回调函数会直接返回一个对响应的校验结果，或者以Promise形式异步回调，true代表校验成功，false代表校验失败。 |

**ProcessingConfiguration**

请求处理配置。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| validateResponse | 'default' | ResponseValidationCallback | 否 | 是 | 默认不处理。或者使用ResponseValidationCallback对响应进行校验。 |

**GetDataCallback**

type GetDataCallback = (maxSize: number) => ArrayBuffer | Promise<ArrayBuffer>

获取任意数据的回调方法的类型，其入参为数据最大字节数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSize | number | 是 | 数据最大字节数。 返回值为ArrayBuffer或使用Promise异步回调的方法，可取任意值。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回一段ArrayBuffer类型数据，为获取到的回调方法的类型。 |
| Promise<ArrayBuffer> | 使用Promise异步回调方式返回ArrayBuffer类型数据。为获取到的回调方法的类型。 说明： 5.0.0(12)新增返回值Promise<ArrayBuffer>。 |

**DynamicExclusionRule**

type DynamicExclusionRule = (url: URLOrString) => boolean

返回是否要从代理中排除入参的URL的回调函数类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | 表示URL对象或表示URL的字符串的并集类型。 表示入参的类型为URLOrString，返回值为boolean的方法。为true，代表主机使用代理，false则代表未使用。 |

表1 返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回一个boolean类型值，为true，代表主机使用代理，false则代表未使用。 |

**StaticDnsRule**

StaticDnsRule接口表示一个单独的静态DNS规则，将特定的IP地址与主机名和端口相关联。此配置是StaticDnsRule接口的一部分，用于自定义DNS映射。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| host | string | 否 | 否 | 应用静态DNS规则的主机名。 |
| port | number | 否 | 否 | 应用静态DNS规则的端口号。范围是[0, 65535]。 |
| ipAddresses | IpAddress[] | 否 | 否 | 要与指定的主机名和端口关联的IP地址阵列。 |

**StaticDnsRules**

type StaticDnsRules = StaticDnsRule[]

允许开发者定义静态DNS规则，将特定的IP地址与主机名和端口关联起来。此配置适用于特定域和端口需要自定义IP映射的情况。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| StaticDnsRule[] | 表示值的类型为StaticDnsRule数组。 |

**DynamicDnsRule**

type DynamicDnsRule = (host: string, port: number) => IpAddress[]

一个可以根据hostname和port直接返回IP地址的函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 指定的主机名。 |
| port | number | 是 | 指定的端口。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| IpAddress[] | 一个IP地址数组。 |

**WebProxy**

WebProxy接口使开发者能够在[ProxyConfiguration](#ZH-CN_TOPIC_0000002522081536__proxyconfiguration)中配置自定义代理时定义自定义代理设置。它允许指定代理URL、排除和其他安全配置。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | URLOrString | 否 | 否 | 自定义代理的URL。 |
| createTunnel | 'auto' | 'always' | 否 | 是 | 用于控制何时创建代理隧道。隧道是指将HTTP CONNECT请求发送到代理，要求其连接到一个特定端口号上的远程主机，然后流量通过代理。默认值为'auto'。 'auto'表示为HTTPS创建隧道，而不是为HTTP创建。 'always'表示始终创建隧道。 |
| exclusions | URLOrString | URLOrString[] | DynamicExclusionRule | 否 | 是 | 要从代理中排除的URL （例如："http://exclude.example.com"或["http://exclude1.com", "http://exclude2.com"]）。默认值为undefined。 |
| security | SecurityConfiguration | 否 | 是 | 设置代理安全配置。默认值为undefined。 |

**InfoToCollect**

InfoToCollect接口可以帮助开发者收集信息事件。收集到的信息事件会在[Response](#ZH-CN_TOPIC_0000002522081536__response)的debugInfo字段中返回。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textual | boolean | 否 | 是 | 是否收集文本信息事件。默认值为false。 |
| incomingHeader | boolean | 否 | 是 | 是否收集传入的header信息事件。默认值为false。 |
| outgoingHeader | boolean | 否 | 是 | 是否收集传出的header信息事件。默认值为false。 |
| incomingData | boolean | 否 | 是 | 是否收集传入的数据信息事件。默认值为false。 |
| outgoingData | boolean | 否 | 是 | 是否收集传出数据信息事件。默认值为false。 |
| incomingSslData | boolean | 否 | 是 | 是否收集传入的SSL/TLS数据信息事件。默认值为false。 |
| outgoingSslData | boolean | 否 | 是 | 是否收集传出的SSL/TLS数据信息事件。默认值为false。 |
| srcAddr | boolean | 否 | 是 | 客户端地址。 true：收集客户端地址及端口号。 false：不收集客户端地址及端口号。 默认值是false。 起始版本： 6.0.0(20) |
| dstAddr | boolean | 否 | 是 | 服务器地址。 true：收集服务器地址及端口号。 false：不收集服务器地址及端口号。 默认值是false。 起始版本： 6.0.0(20) |
| redirectCount | boolean | 否 | 是 | 是否收集重定向次数。 true：收集重定向次数。 false：不收集重定向次数。 默认值为false。 起始版本： 6.1.0(23) |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

此项开启后会占用内存，建议仅在开发调试阶段使用。

**HttpEventsHandler**

HttpEventsHandler接口使开发者能够定义自定义逻辑，用于处理会话中HTTP请求/响应过程中的各种操作。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onDataReceive | OnDataReceive | 否 | 是 | 当接收到HTTP响应正文的一部分时调用的回调。默认为undefined。当开发者需要请求超过50M字节的数据时，使用此回调接受数据。使用后，返回的Response对象的body字段将不再含有数据。 |
| onUploadProgress | OnUploadProgress | 否 | 是 | 用于在响应期间处理上传进度的回调。默认为undefined。 |
| onDownloadProgress | OnDownloadProgress | 否 | 是 | 用于在响应期间处理下载进度的的回调。默认为undefined。 |
| onHeaderReceive | OnHeaderReceive | 否 | 是 | 用于在响应期间处理接收到的headers的回调。默认为undefined。 |
| onDataEnd | OnDataEnd | 否 | 是 | 数据传输完成时触发的回调。默认为undefined。 |
| onCanceled | OnCanceled | 否 | 是 | 取消请求/响应时触发的回调。默认为undefined。 |
| onTimeInfo | OnTimeInfo | 否 | 是 | HTTP请求失败/成功时触发的回调。默认为undefined。 起始版本： 5.0.3(15) |
| onStatusCodeReceive | OnStatusCodeReceive | 否 | 是 | 用于在响应期间处理接收到的状态码的回调。默认为undefined。 起始版本： 6.0.0(20) |

**Timeout**

配置HTTP请求的超时值，允许开发者定义连接和传输数据所允许的最长时间。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectMs | number | 否 | 是 | 允许建立连接的最长时间（以毫秒为单位）。如果连接过程超过这个时间限制，连接将被认为超时。默认值为60000。 |
| transferMs | number | 否 | 是 | 允许传输数据的最长时间（以毫秒为单位）。如果数据传输过程中超过这个时间限制，传输将被认为超时。默认值为60000。 |
| inactivityMs | number | 否 | 是 | 允许在没有数据传输或连接活动的情况下，允许的最长时间。用于在从服务器接收数据或向服务器发送数据的时间间隔不能超过这个值的情况下，防止长时间的空闲连接。默认情况下，超时值没有设置，即不限制时间间隔。 起始版本： 5.0.0(12) |

**CertificatePinning**

证书锁定是校验服务器的证书的公钥SHA-256哈希值是否与设置的值匹配。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'public-key' | 否 | 否 | 证书的校验类型。 |
| publicKeyHash | string | 否 | 否 | 公钥哈希值。 |
| hashAlgorithm | 'SHA-256' | 否 | 否 | 用于计算公钥哈希值的算法。 |

**SessionListener**

定义会话监听器。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onCanceled | OnCanceled | 否 | 是 | 会话取消事件的回调。会话取消时调用。默认为undefined。 |
| onClosed | OnClosed | 否 | 是 | 会话关闭事件回调。会话关闭时调用。默认为undefined。 |

**Credential**

凭据接口表示会话中服务器身份验证设置中使用的身份验证凭据，包括用户名和密码。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| username | string | 否 | 否 | 用于身份验证的用户名。默认值为' '。 |
| password | string | 否 | 否 | 用于身份验证的密码。默认值为' '。 |

**TlsVersion**

type TlsVersion = 'TlsV1.0' | 'TlsV1.1' | 'TlsV1.2' | 'TlsV1.3'

安全配置项TLS允许设置的版本，可选择TLS的使用版本。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

| 取值范围 | 说明 |
| --- | --- |
| 'TlsV1.0' | 表示使用TLS1.0版本。 |
| 'TlsV1.1' | 表示使用TLS1.1版本。 |
| 'TlsV1.2' | 表示使用TLS1.2版本。 |
| 'TlsV1.3' | 表示使用TLS1.3版本。 |

**DebugEvent**

type DebugEvent = 'text' | 'headerIn' | 'headerOut' | 'dataIn' | 'dataOut' | 'sslDataIn' | 'sslDataOut' | 'srcAddr' | 'dstAddr' | 'redirectCount'

定义调试事件类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| 'text' | 表示调试事件与HTTP响应的文本内容相关。 |
| 'headerIn' | 表示调试事件与HTTP响应的头部信息（在客户端接收响应时）相关。 |
| 'headerOut' | 表示调试事件与HTTP请求的头部信息（在客户端发送请求时）相关。 |
| 'dataIn' | 表示调试事件与HTTP响应的主体数据（在客户端接收响应时）相关。 |
| 'dataOut' | 表示调试事件与HTTP请求的主体数据（在客户端发送请求时）相关。 |
| 'sslDataIn' | 表示调试事件与通过SSL/TLS协议接收的HTTP响应数据相关。 |
| 'sslDataOut' | 表示调试事件与通过SSL/TLS协议发送的HTTP请求数据相关。 |
| 'srcAddr' | 表示调试事件与获取客户端地址和端口相关。 起始版本： 6.0.0(20) |
| 'dstAddr' | 表示调试事件与获取服务器地址和端口相关。 起始版本： 6.0.0(20) |
| 'redirectCount' | 表示调试事件与获取重定向次数相关。 起始版本： 6.1.0(23) |

**AuthenticationType**

type AuthenticationType = 'basic' | 'ntlm' | 'digest'

此类型表示可以在会话中的服务器身份验证设置中使用的不同身份验证机制。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

| 类型 | 说明 |
| --- | --- |
| 'basic' | 表示使用基本身份验证，通过将用户名和密码组合成一个字符串并进行Base64编码来进行身份验证。 |
| 'ntlm' | 表示使用NT LAN Manager身份验证。 |
| 'digest' | 表示使用HTTP摘要身份验证，通过将用户名、密码和其他信息进行哈希运算来生成认证信息。 |

**OnCanceled**

type OnCanceled = (request?: Request) => void

此类型表示当请求或会话被取消时的回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 否 | 触发回调的HTTP请求。 起始版本： 6.0.0(20) |

**OnClosed**

type OnClosed = () => void

此类型表示会话关闭时的回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

**OnDataReceive**

type OnDataReceive = (incomingData: ArrayBuffer, request?: Request) => number | void | Promise<void>

此类型表示接收到HTTP body时的回调。当开发者需要请求超过50M字节的数据时，使用此回调接受数据。使用后，返回的[Response](#ZH-CN_TOPIC_0000002522081536__response)对象的body字段将不再含有数据。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incomingData | ArrayBuffer | 是 | 参数为收到HTTP数据。 |
| request | Request | 否 | 触发回调的HTTP请求。 起始版本： 6.0.0(20) |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回number类型数据，是处理的字节数。 |
| Promise<void> | 以Promise形式返回空值。 说明： 5.0.0(12)版本上新增返回值void | Promise<void>。 |

**OnUploadProgress**

type OnUploadProgress = (totalSize: number, transferredSize: number, request?: Request) => void

此类型表示上传进度时的回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| totalSize | number | 是 | 上传总大小。 |
| transferredSize | number | 是 | 已上传大小。 |
| request | Request | 否 | 触发回调的HTTP请求。 起始版本： 6.0.0(20) |

**OnDownloadProgress**

type OnDownloadProgress = (totalSize: number, transferredSize: number, request?: Request) => void

此类型表示显示下载进度的回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| totalSize | number | 是 | 下载总大小。 |
| transferredSize | number | 是 | 已下载大小。 |
| request | Request | 否 | 触发回调的HTTP请求。 起始版本： 6.0.0(20) |

**OnHeaderReceive**

type OnHeaderReceive = (headers: ResponseHeaders, request?: Request) => void

此类型表示接收到HTTP头时的回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| headers | ResponseHeaders | 是 | 参数为HTTP响应头，返回为空。 |
| request | Request | 否 | 触发回调的HTTP请求。 起始版本： 6.0.0(20) |

**OnDataEnd**

type OnDataEnd = (request?: Request) => void

此类型表示HTTP传输结束时的回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 否 | 触发回调的HTTP请求。 起始版本： 6.0.0(20) |

**OnTimeInfo**

type OnTimeInfo = (timeInfo: TimeInfo, request?: Request) => void

此类型是HTTP请求成功/失败时的回调。请求成功开发者可获得请求各阶段的时间信息，请求失败可获得失败的阶段之前各阶段时间信息。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeInfo | TimeInfo | 是 | HTTP各个阶段耗时。 |
| request | Request | 否 | 触发回调的HTTP请求。 起始版本： 6.0.0(20) |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1、创建session、requestURL和request。
const session = rcp.createSession();
const requestURL = "https://www.example.com";
const request = new rcp.Request(requestURL);

// 2、配置请求的configuration，设置onTimeInfo回调函数以获取网络请求相关的时间信息
request.configuration = {
  tracing: {
    httpEventsHandler: {
      onTimeInfo: (timeInfo: rcp.TimeInfo) => {
        console.info('Time information for each phase in the HTTP request. ', JSON.stringify(timeInfo));
        let remainderDataTime = timeInfo?.totalTimeMs - timeInfo?.startTransferTimeMs;
        let firstPackageTime = timeInfo?.startTransferTimeMs - timeInfo?.preTransferTimeMs;
        let TLSTime = timeInfo?.tlsHandshakeTimeMs - timeInfo?.connectTimeMs;
        console.info(`首包耗时${firstPackageTime}`);
        console.info(`TLS握手（不包含建连时间）耗时${TLSTime}`);
        console.info(`接收剩余数据的耗时${remainderDataTime}`);
      },
};
// 3、使用 fetch 发起网络请求，请求中携带上述配置好的 configuration。
session.fetch(request).then((response) => {
  if (response) {
    console.info(`The request was successful. The statusCode of the response is ${response.statusCode}`);
    session.close();
  }
}).catch((err: BusinessError) => {
  console.error(`Response err, the err is ${JSON.stringify(err)}`);
})
```

**OnStatusCodeReceive**

type OnStatusCodeReceive = (statusCode: number, request?: Request) => void

此类型是HTTP请求成功/失败时的回调，开发者可获得响应状态码信息。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| statusCode | number | 是 | HTTP状态码。 |
| request | Request | 否 | 触发回调的HTTP请求。 |

**CacheControl**

CacheControl 接口提供了一系列配置参数，开发者可通过这些参数精准控制会话中 HTTP 请求的缓存行为，包括资源缓存策略、更新机制及存储规则等。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| expirationPolicy | TimeLimitedExpirationPolicy | 否 | 是 | 为HTTP请求所创建的缓存配置过期策略。如果设置该属性，则会覆盖HTTP响应过期策略。 |
| keepCache | boolean | 否 | 是 | 是否需要保留缓存，默认为false。该参数为true时，使用不安全的 HTTP 方法的请求（PUT，POST，或者DELETE）不会使缓存记录失效。 |
| noCache | boolean | 否 | 是 | 是否在请求头中添加no-cache，默认为false。该参数为true时，则会强制客户端在使用缓存前必须向服务器验证资源有效性（即使缓存存在）。 |
| noStore | boolean | 否 | 是 | 是否在请求头中添加no-store，默认为false。该参数为true时，则会严格禁止任何缓存存储请求或响应的内容，确保敏感数据不会被持久化。 |
| maxAge | TimeInterval | 否 | 是 | 该属性指定缓存资源的有效时长，在此期间客户端可直接使用缓存而无需请求服务器。 |
| maxStale | TimeInterval | 否 | 是 | 该属性允许客户端接受已过期但未超过指定时间的缓存资源，提升数据可用性。 |
| minFresh | TimeInterval | 否 | 是 | 该属性要求服务器返回的响应在指定时间内保持新鲜，确保资源短期内不过期。 |
| noTransform | boolean | 否 | 是 | 是否在请求头中添加no-transform，默认为false。该参数为true时，则会禁止缓存服务器对响应内容进行任何转换（如压缩），保证内容与原始响应一致。 |
| onlyIfCached | boolean | 否 | 是 | 是否在请求头中添加only-if-cached，默认为false。该参数为true时，则会强制客户端仅使用缓存资源，若缓存不存在则直接失败（不发起网络请求）。 |

**CacheInfo**

缓存信息，包含该缓存对应的原始HTTP请求ID和已存在时长。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| originalRequestId | string | 否 | 否 | 创建该缓存时的HTTP请求ID。 |
| age | TimeInterval | 否 | 否 | 缓存已存在时长。 |

**ExpirationPolicy**

type ExpirationPolicy = NeverExpirationPolicy | TimeLimitedExpirationPolicy

缓存过期策略。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| NeverExpirationPolicy | 永不过期类型过期策略。 |
| TimeLimitedExpirationPolicy | 时间限制类型过期策略。 |

**NeverExpirationPolicy**

缓存记录永不过期的过期策略。缓存记录会一直停留在缓存中，直到超过缓存大小限制。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'never' | 否 | 否 | 缓存过期策略类型表示键，键值为'never'，表示永不过期的过期策略。 |

**TimeLimitedExpirationPolicy**

type TimeLimitedExpirationPolicy = AbsoluteTimeExpirationPolicy | RelativeTimeExpirationPolicy | SlidingTimeExpirationPolicy

时间限制类型过期策略。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| AbsoluteTimeExpirationPolicy | 绝对时间过期策略。到达指定时间，该缓存记录过期。 |
| RelativeTimeExpirationPolicy | 相对时间过期策略。经过指定的时间间隔后，该缓存记录过期。 |
| SlidingTimeExpirationPolicy | 滑动时间过期策略。指定的时间间隔期间，若无任何访问，该缓存记录过期；若有访问，则重置过期时间。 |

**AbsoluteTimeExpirationPolicy**

绝对时间过期策略。到达指定时间，该缓存记录过期。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'absolute' | 否 | 否 | 缓存过期策略类型表示键，键值为'absolute'，表示绝对时间过期策略。 |
| time | Date | 否 | 否 | 指定缓存过期时间。 |

**RelativeTimeExpirationPolicy**

相对时间过期策略。经过指定的时间间隔后，该缓存记录过期。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'relative' | 否 | 否 | 缓存过期策略类型表示键，键值为'relative'，表示相对时间过期策略。 |
| time | TimeInterval | 否 | 否 | 指定时间间隔。 |

**SlidingTimeExpirationPolicy**

滑动时间过期策略。指定的时间间隔期间，若无任何访问，该缓存记录过期；若有访问，则重置过期时间。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'sliding' | 否 | 否 | 缓存过期策略类型表示键，键值为'sliding'，表示滑动时间过期策略。 |
| time | TimeInterval | 否 | 否 | 指定时间间隔。 |

**TimeInterval**

时间间隔。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| units | TimeIntervalUnits | 否 | 否 | 时间间隔单位。 |
| value | number | 否 | 否 | 时间长度。 |

**TimeIntervalUnits**

type TimeIntervalUnits = 'seconds' | 'minutes' | 'hours' | 'days'

时间间隔单位。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| 'seconds' | 时间单位：秒。 |
| 'minutes' | 时间单位：分。 |
| 'hours' | 时间单位：时。 |
| 'days' | 时间单位：天。 |

**CachedResponse**

缓存中存储的HTTP响应数据。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeStamp | Date | 否 | 否 | 从网络获取HTTP响应的时间。 |
| originalRequestId | string | 否 | 否 | 原始HTTP请求ID。 |
| statusCode | number | 否 | 否 | HTTP响应状态码。 |
| headers | ResponseHeaders | 否 | 否 | HTTP响应头信息。 |
| body | ArrayBuffer | 否 | 是 | HTTP响应内容。 |
| effectiveUrl | string | 否 | 是 | 重定向后请求的有效URL。默认值为undefined。 |
| httpVersion | HttpVersion | 否 | 是 | HTTP的版本。 |
| reasonPhrase | string | 否 | 是 | HTTP响应状态行的reasonPhrase，提供与数字状态代码相关的文本描述。 |
| extra | ArrayBuffer | 否 | 是 | 附加信息。 |

**ResponseCacheKey**

标识HTTP响应缓存记录的键。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | URLOrString | 否 | 否 | 请求URL。 |
| method | HttpMethod | 否 | 否 | HTTP方法 |
| extra | string | 否 | 是 | 附加信息。该属性允许相同的URL和HTTP方法存储多条响应缓存记录。例如，开发者可以尝试放置语言类型字符串，用以匹配对应语言的响应内容。 |

**ResponseCacheRecord**

缓存记录。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| expirationPolicy | ExpirationPolicy | 否 | 否 | 缓存过期策略。 |
| response | CachedResponse | 否 | 否 | 存储的缓存响应。 |
| key | ResponseCacheKey | 否 | 否 | 缓存响应对应的缓存键。 |

**CacheConfiguration**

缓存配置。开发者可以通过该接口控制缓存行为，包括内存和磁盘缓存配置、缓存内存和条数上限、默认过期策略等。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| persistent | PersistentStorageConfiguration | 否 | 否 | 指定持久化缓存配置。 |
| inMemory | InMemoryCacheConfiguration | 否 | 是 | 指定内存缓存配置。 |
| maxItems | number | 否 | 是 | 指定内存/持久化存储的缓存最大数量。如果设置，当缓存数量超过该阈值时，将基于LRU算法（选出最久未被使用的数据）执行淘汰策略：首先淘汰时间过期策略类型的缓存记录，其次再淘汰永不过期的缓存记录。 |
| maxSize | number | 否 | 是 | 指定内存/持久化存储所占用存储空间的上限。当缓存内存超过该阈值时，将基于LRU算法（选出最久未被使用的数据）执行淘汰策略：首先淘汰时间过期策略类型的缓存记录，其次再淘汰永不过期的缓存记录。 单位：MB。 默认值：50。 |
| defaultExpirationPolicy | TimeLimitedExpirationPolicy | 否 | 是 | 默认缓存过期策略。 如果设置，它将应用于每个新增的响应记录； 如果未设置，将默认设置为1小时的SlidingTimeExpirationPolicy。 set方法配置的缓存过期策略会覆盖本接口默认缓存过期策略。 |

**PersistentStorageConfiguration**

type PersistentStorageConfiguration = FileSystemStorageConfiguration

持久化缓存存储配置。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| FileSystemStorageConfiguration | 基于文件系统的缓存存储配置。 |

**FileSystemStorageConfiguration**

基于文件系统的缓存存储配置。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| kind | 'file-system' | 否 | 否 | 持久化缓存存储介质键，键值为'file-system'，表示基于文件系统介质存储。 |
| pathToFolder | string | 否 | 否 | 指定存储缓存的文件路径。可以参考应用文件。 |

**InMemoryCacheConfiguration**

基于内存的缓存存储配置。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxItems | number | 否 | 是 | 指定内存缓存中的最大记录数上限。 |
| maxSize | number | 否 | 是 | 指定内存缓存所占用内存上限。若设置，则CacheConfiguration中配置的maxSize对内存缓存存储不生效。 单位：MB。 默认值：10。 |

**CacheState**

缓存状态信息。包含当前缓存条数、缓存大小和缓存命中数。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | number | 否 | 否 | 持久化存储缓存的字节数。 单位：Byte。 |
| count | number | 否 | 否 | 当前持久化存储的缓存数量。 |
| hitCount | number | 否 | 否 | 缓存命中数。 |

**ResponseCache**

HTTP响应缓存，为开发者提供了记录和操作HTTP缓存的能力。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

**constructor**

constructor(configuration: CacheConfiguration)

创建HTTP响应缓存实例。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | CacheConfiguration | 是 | 缓存配置。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

const cache = new rcp.ResponseCache({
  persistent: {
    kind: 'file-system',
    pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
  }
});
```

**close**

close(): Promise<void>

关闭HTTP缓存响应实例，终止所有待处理的缓存操作。使用Promise异步回调。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900985 | File system IO error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  await cache.close();
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**set**

set(key: ResponseCacheKey, response: CachedResponse, expirationPolicy?: ExpirationPolicy): Promise<void>

添加或替换缓存键对应的缓存内容。使用Promise异步回调。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | ResponseCacheKey | 是 | 缓存键。 |
| response | CachedResponse | 是 | 需要添加或替换的HTTP缓存响应内容。 |
| expirationPolicy | ExpirationPolicy | 否 | 缓存过期策略。若传入该参数，则会覆盖CacheConfiguration中的默认缓存过期策略，即defaultExpirationPolicy。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |
| 1007900985 | File system IO error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  const session: rcp.Session = rcp.createSession({
    requestConfiguration: {
      cache: cache
    }
  });
  const key: rcp.ResponseCacheKey = {
    url: 'https://www.example.com',
    method: 'GET'
  };
  const response = await session.get('https://www.example.com');
  const cachedRecord = rcp.createCachedResponse(response);
  const policy: rcp.TimeLimitedExpirationPolicy = {
    kind: 'relative',
    time: {
      units: 'seconds',
      value: 3
    }
  };
  cache.set(key, cachedRecord, policy).then(() => {
  })
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**get**

get(key: ResponseCacheKey): Promise<ResponseCacheRecord>

获得缓存键对应的HTTP响应缓存记录。使用Promise异步回调。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | ResponseCacheKey | 是 | 缓存键。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ResponseCacheRecord> | Promise对象，返回HTTP响应缓存记录。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |
| 1007900985 | File system IO error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  const record = await cache.get({
    url: 'https://www.example.com',
    method: 'GET'
  });
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**clear**

clear(): Promise<void>

清除HTTP响应缓存。使用Promise异步回调。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900985 | File system IO error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  await cache.clear();
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**getState**

getState(): Promise<CacheState>

获取缓存状态信息。使用Promise异步回调。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<CacheState> | Promise对象，返回缓存状态信息。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900985 | File system IO error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  const cacheState = await cache.getState();
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**remove**

remove(key: ResponseCacheKey): Promise<boolean>

删除缓存键对应的HTTP响应缓存记录。使用Promise异步回调。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | ResponseCacheKey | 是 | 缓存键。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示删除成功；返回false表示删除失败。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |
| 1007900985 | File system IO error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  const key: rcp.ResponseCacheKey = {
    url: 'https://www.example.com',
    method: 'GET'
  };
  const result = await cache.remove(key);
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**removeMultiple**

removeMultiple(url: URLOrString, matchKind: URLMatchKind, method?: HttpMethod): Promise<boolean>

按照URL匹配类型，检索并删除一条或者多条HTTP响应缓存记录，开发者可以通过matchKind配置URL匹配类型。使用Promise异步回调。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | URLOrString | 是 | URL，用于与缓存键中的URL进行匹配。 |
| matchKind | URLMatchKind | 是 | URL匹配类型。 |
| method | HttpMethod | 否 | HTTP请求方法。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示删除成功；返回false表示删除失败。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1007900401 | Parameter error. |
| 1007900985 | File system IO error. |

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  const result = await cache.removeMultiple('https://www.example.com', 'exact', 'GET');
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**URLMatchKind**

type URLMatchKind = 'exact' | 'as-substring'

URL匹配类型。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| 'exact' | 指定URL精准匹配。匹配的URL应等于提供的URL。 |
| 'as-substring' | 指定URL应作为子字符串进行匹配。匹配的URL应包含提供的URL。 |

**rcp.createResponse**

createResponse(request: Request, cachedResponse: CachedResponse, currentTime: Date): Response

根据HTTP响应缓存创建HTTP响应。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Request | 是 | 要创建响应的HTTP请求。 |
| cachedResponse | CachedResponse | 是 | 缓存中存储的HTTP响应缓存。 |
| currentTime | Date | 是 | 当前时间。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Response | HTTP响应。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
    }
  });
  const request = new rcp.Request('https://www.example.com', 'GET');
  const key: rcp.ResponseCacheKey = {
    url: request.url,
    method: request.method,
  };
  // 获取HTTP响应缓存结果。
  const responseInCache = await cache.get(key);
  if (responseInCache) {
    // 根据HTTP响应缓存得到HTTP响应。
    const response = rcp.createResponse(request, responseInCache.response, new Date());
  }
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```

**rcp.createCachedResponse**

createCachedResponse(response: Response, timeStamp?: Date): CachedResponse

根据HTTP响应创建HTTP响应缓存。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | Response | 是 | HTTP响应。 |
| timeStamp | Date | 否 | 缓存的响应时间戳。默认为当前系统时间。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| CachedResponse | HTTP响应缓存。 |

错误码：

错误码的详细介绍请参见[API错误码](API错误码.md)。

示例：

```ets
import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir", // 请根据自身业务选择合适的路径
    }
  });
  const session = rcp.createSession();
  const key: rcp.ResponseCacheKey = {
    url: 'https://www.example.com',
    method: 'GET'
  };
  // 获取HTTP响应。
  const response = await session.get('https://www.example.com');
  // 根据HTTP响应创建HTTP响应缓存。
  const cachedRecord = rcp.createCachedResponse(response);
} catch (err) {
  console.error(`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}`);
}
```