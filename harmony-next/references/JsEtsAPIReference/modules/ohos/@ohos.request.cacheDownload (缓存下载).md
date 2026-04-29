# @ohos.request.cacheDownload (缓存下载)

request部件主要给应用提供上传下载文件、后台传输代理的基础能力。

-

request的cacheDownload子组件主要给应用提供应用资源提前缓存的基础能力。

-

cacheDownload组件使用HTTP协议进行数据下载，并将数据资源缓存至应用内存或应用沙箱目录的指定文件中。

-

这些缓存数据可以被特定的ArkUI组件（例如：Image组件）使用，从而提升资源加载效率。请查看ArkUI组件文档确定组件是否支持该功能。


本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { cacheDownload } from '@kit.BasicServicesKit';
```

#### SslType21+

表示安全通信协议的枚举。

**系统能力**：SystemCapability.Request.FileTransferAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TLS | 'TLS' | 使用TLS安全通信协议。 |
| TLCP | 'TLCP' | 使用TLCP安全通信协议。 |

**ErrorCode23+**

表示错误返回信息的特定类型枚举。

系统能力：SystemCapability.Request.FileTransferAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OTHERS | 0xFF | 表示未分类的其他类型错误。 |
| DNS | 0x00 | 表示DNS相关错误。 |
| TCP | 0x10 | 表示TCP相关错误。 |
| SSL | 0x20 | 表示SSL相关错误。 |
| HTTP | 0x30 | 表示HTTP相关错误。 |

**CacheStrategy23+**

表示缓存刷新策略的枚举。

系统能力：SystemCapability.Request.FileTransferAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORCE | 0 | 强制更新缓存，无论缓存是否已经存在。 |
| LAZY | 1 | 延迟更新缓存，只有当缓存不存在时才会更新。 |

#### CacheDownloadOptions

缓存下载的配置选项。包括HTTP选项、传输选项和任务选项。

**系统能力**：SystemCapability.Request.FileTransferAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| headers | Record<string, string> | 否 | 是 | 缓存下载任务在HTTP传输时使用的请求头。 |
| sslType21+ | SslType | 否 | 是 | 使用安全通信协议TLS或TLCP，默认使用TLS。当前TLS和TLCP均不支持双向认证。 |
| caPath21+ | string | 否 | 是 | CA证书路径。目前仅支持.pem格式证书，默认使用系统预设的CA证书。 |
| cacheStrategy23+ | CacheStrategy | 否 | 是 | 使用缓存刷新策略FORCE或LAZY，默认使用FORCE。 |

#### ResourceInfo20+

预下载的资源信息。

**系统能力**：SystemCapability.Request.FileTransferAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | number | 是 | 否 | 预下载资源解压后的大小。当值为正整数时表示资源下载成功，-1表示下载失败。 |

#### NetworkInfo20+

预下载的网络信息。

**系统能力**：SystemCapability.Request.FileTransferAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dnsServers | string[] | 是 | 否 | 下载资源时使用的dns服务器列表。 |
| ip23+ | string | 是 | 是 | 下载资源时url的ip地址。当dns解析失败时，ip为undefined。 |

#### PerformanceInfo20+

预下载的性能信息。

**系统能力**：SystemCapability.Request.FileTransferAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dnsTime | number | 是 | 否 | 从启动到dns解析完成所需的时间，单位：毫秒（ms）。 |
| connectTime | number | 是 | 否 | 从启动到tcp连接完成所需的时间，单位：毫秒（ms）。 |
| tlsTime | number | 是 | 否 | 从启动到tls连接完成所需的时间，单位：毫秒（ms）。 |
| firstSendTime | number | 是 | 否 | 从启动到开始发送第一个字节所需的时间，单位：毫秒（ms）。 |
| firstReceiveTime | number | 是 | 否 | 从启动到接收第一个字节所需的时间，单位：毫秒（ms）。 |
| totalTime | number | 是 | 否 | 从启动到完成请求所需的时间，单位：毫秒（ms）。 |
| redirectTime | number | 是 | 否 | 从启动到完成所有重定向步骤所需的时间，单位：毫秒（ms）。 |

#### DownloadInfo20+

预下载的下载信息。

**系统能力**：SystemCapability.Request.FileTransferAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resource | ResourceInfo | 是 | 否 | 预下载的资源信息。 |
| network | NetworkInfo | 是 | 否 | 预下载的网络信息。 |
| performance | PerformanceInfo | 是 | 否 | 预下载的性能信息。 |

**DownloadError23+**

预下载错误回调的返回信息。

系统能力：SystemCapability.Request.FileTransferAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| errorCode | ErrorCode | 是 | 否 | 预下载错误回调返回的特定错误类型。 |
| message | string | 是 | 否 | 返回通用错误码或HTTP错误码。 |

#### cacheDownload.download

download(url: string, options: CacheDownloadOptions): void

启动一个缓存下载任务，若传输成功，则将数据下载到内存缓存和文件缓存中。

-

目标资源经过HTTP传输自动解压后的大小不能超过20971520B（即20MB），否则不会保存到内存缓存或文件缓存中。

-

在缓存下载数据时，如果在该url下已存在缓存内容，新的缓存内容会覆盖旧缓存内容。

-

目标资源在存储到内存缓存或文件缓存中时，依照缓存下载组件的各类型缓存大小上限决定文件是否存储到指定位置，并默认使用“LRU”（最近最少使用）方式替换已有缓存内容。

-

该方法为同步方法，不阻塞调用线程。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 目标资源的地址。仅支持HTTP协议，长度不超过8192字节。 |
| options | CacheDownloadOptions | 是 | 目标资源的缓存下载选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 401 | parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**示例：**

```ets
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

// 提供缓存下载任务的配置选项。
let options: cacheDownload.CacheDownloadOptions = {
  headers: { 'Accept': 'application/json' },
  sslType: cacheDownload.SslType.TLS,
  caPath: '/path/to/ca.pem',
  cacheStrategy: cacheDownload.CacheStrategy.FORCE,
};

try {
  // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
  cacheDownload.download("https://www.example.com", options);
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```

#### cacheDownload.cancel

cancel(url: string): void

根据url移除一个正在执行的缓存下载任务，已保存的内存缓存和文件缓存不会受到影响。

-

当不存在对应url的任务时无其他效果。

-

使用该方法同步执行时，不阻塞调用线程。

**系统能力**：SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 目标资源的地址。仅支持HTTP协议，长度不超过8192字节。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**示例：**

```ets
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

// 提供缓存下载任务的配置选项。
let options: cacheDownload.CacheDownloadOptions = {};

try {
  // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
  cacheDownload.download("https://www.example.com", options);
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}

// 处理其他业务逻辑。

try {
  // 在不需要特定任务缓存时，移除缓存下载任务，已缓存的内容不受影响。
  cacheDownload.cancel("https://www.example.com");
} catch (err) {
  console.error(`Failed to cancel the task. err code: ${err.code}, err message: ${err.message}`);
}
```

#### cacheDownload.setMemoryCacheSize

setMemoryCacheSize(bytes: number): void

设置缓存下载组件能够保存的内存缓存上限。

-

使用该接口调整缓存大小时，默认使用“LRU”（最近最少使用）方式清除多余的已缓存的内存缓存内容。

-

该方法为同步方法，不阻塞调用线程。

**系统能力**：SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bytes | number | 是 | 设置的缓存上限。默认值为0B，最大值不超过1073741824B（即1GB）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**示例：**

```ets
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // 设置内存缓存大小上限。
  cacheDownload.setMemoryCacheSize(10 * 1024 * 1024);
} catch (err) {
  console.error(`Failed to set memory cache size. err code: ${err.code}, err message: ${err.message}`);
}
```

#### cacheDownload.setFileCacheSize

setFileCacheSize(bytes: number): void

设置缓存下载组件能够保存的文件缓存的上限。

-

使用该接口调整缓存大小时，默认使用“LRU”（最近最少使用）方式清除多余的已缓存的文件缓存内容。

-

使用该接口时，若bytes设置为0，将会删除所有缓存文件。

-

该方法为同步方法，不会阻塞调用线程。

**系统能力**：SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bytes | number | 是 | 设置的缓存上限。默认值为104857600B（即100MB），最大值不超过4294967296B（即4GB）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**示例：**

```ets
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // 设置文件缓存大小上限。
  cacheDownload.setFileCacheSize(100 * 1024 * 1024);
} catch (err) {
  console.error(`Failed to set file cache size. err code: ${err.code}, err message: ${err.message}`);
}
```

​>

- 预下载模块下载的网络缓存文件会保存在应用沙箱的缓存目录中。
- 应用可以借助该接口的能力达成清理缓存文件的目的。
- 不建议应用直接对缓存目录和文件进行修改，以避免功能异常。

#### cacheDownload.setDownloadInfoListSize20+

setDownloadInfoListSize(size: number): void

设置下载信息列表的大小。

-

下载信息列表用于存储预下载信息。

-

下载信息和url一一对应，每次预下载都会生成一个下载信息，相同url下只会保存最新的下载信息。

-

使用该接口调整列表大小时，size更新增大，列表中原有的信息不变，更新减小，默认使用“LRU”（最近最少使用）方式清除多余的已缓存信息。

**系统能力**：SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 设置的下载信息列表大小。取值范围：[0, 8192]，默认为0，表示不会存储任何下载信息。 |

**示例：**

```ets
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // 设置下载信息列表大小。
  cacheDownload.setDownloadInfoListSize(2048);
} catch (err) {
  console.error(`Failed to set download information list size. err code: ${err.code}, err message: ${err.message}`);
}
```

#### cacheDownload.getDownloadInfo20+

getDownloadInfo(url: string): DownloadInfo | undefined

基于url获取预下载的下载信息。信息存储在内存中的下载信息列表，当应用程序退出时清除。

-

如果下载信息列表中能够找到指定url，返回该url对应的最新[DownloadInfo](#ZH-CN_TOPIC_0000002553201559__downloadinfo20)。

-

如果下载信息列表中找不到指定url，返回undefined。

-

在缓存下载信息时，如果在该url下已存在缓存信息，新的缓存内容会覆盖旧缓存。

-

目标信息在存储到内存时，使用“LRU”（最近最少使用）方式替换已存在的缓存数据。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 待查询的url，最大长度为8192字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DownloadInfo | undefined | 返回对应url的下载信息，url未记录时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |

```ets
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // 设置下载信息列表大小。
  cacheDownload.setDownloadInfoListSize(2048);
} catch (err) {
  console.error(`Failed to set download information list size. err code: ${err.code}, err message: ${err.message}`);
}

// 提供缓存下载任务的配置选项。
let options: cacheDownload.CacheDownloadOptions = {};

try {
  // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
  cacheDownload.download("https://www.example.com", options);
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}

// 处理其他业务逻辑。

try {
  // 在缓存下载完成后，获取缓存下载的信息。
  let downloadInfo = cacheDownload.getDownloadInfo("https://www.example.com");
  if (downloadInfo == undefined) {
    console.error(`CacheDownload get download info undefined.`);
  } else {
    console.info(`CacheDownload get download info : ${JSON.stringify(downloadInfo)}`);
  }
} catch (err) {
  console.error(`Failed to get download info. err code: ${err.code}, err message: ${err.message}`);
}
```

**cacheDownload.clearMemoryCache23+**

clearMemoryCache(): void

清除缓存下载内容的内存缓存。

系统能力：SystemCapability.Request.FileTransferAgent

示例：

```ets
import { cacheDownload } from '@kit.BasicServicesKit';

cacheDownload.clearMemoryCache();
```

**cacheDownload.clearFileCache23+**

clearFileCache(): void

清除保存下载内容的文件缓存。

系统能力：SystemCapability.Request.FileTransferAgent

示例：

```ets
import { cacheDownload } from '@kit.BasicServicesKit';

cacheDownload.clearFileCache();
```

**cacheDownload.onDownloadSuccess23+**

onDownloadSuccess(url: string, callback: Callback<void>): void

订阅预下载的完成事件。使用callback异步回调。

系统能力：SystemCapability.Request.FileTransferAgent

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 待注册回调的url，url字符串的最大长度为8192字节。 |
| callback | Callback<void> | 是 | 回调函数。 |

示例：

```ets
import { cacheDownload } from '@kit.BasicServicesKit';

try {
  const successCallback = () => {
    console.info("Succeeded in getting callback from cacheDownload");
  };
  // 订阅预下载的完成事件，当下载完成时执行回调
  cacheDownload.onDownloadSuccess("https://www.example.com", successCallback)
  // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```

**cacheDownload.onDownloadError23+**

onDownloadError(url: string, callback: Callback<DownloadError>): void

订阅预下载的错误事件。使用callback异步回调。

系统能力：SystemCapability.Request.FileTransferAgent

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 待注册回调的url，URL字符串的最大长度为8192字节。 |
| callback | Callback<DownloadError> | 是 | 回调函数，返回预下载的错误信息。 |

示例：

```ets
import { cacheDownload } from '@kit.BasicServicesKit';

try {
  const errorCallback = (error: cacheDownload.DownloadError) => {
    console.info(`Error callback from cacheDownload.error code: ${error.errorCode}, error message: ${error.message}`);
  };
  // 订阅预下载的错误事件，当下载错误时执行回调，返回错误信息
  cacheDownload.onDownloadError("https://www.example.com", errorCallback)
  // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```

**cacheDownload.offDownloadSuccess23+**

offDownloadSuccess(url: string, callback?: Callback<void>): void

取消订阅预下载的完成事件。使用callback异步回调。

系统能力：SystemCapability.Request.FileTransferAgent

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 待注册回调的url，url字符串的最大长度为8192字节。 |
| callback | Callback<void> | 否 | 回调函数。若不填该参数，表示url下的所有完成回调函数。 |

示例：

```ets
import { cacheDownload } from '@kit.BasicServicesKit';

try {
  const successCallback = () => {
    console.info("Succeeded in getting callback from cacheDownload");
  };
  // 订阅预下载的完成事件，当下载完成时执行回调
  cacheDownload.onDownloadSuccess("https://www.example.com", successCallback);
  // 取消订阅预下载的完成事件
  cacheDownload.offDownloadSuccess("https://www.example.com", successCallback);
  // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```

**cacheDownload.offDownloadError23+**

offDownloadError(url: string, callback?: Callback<DownloadError>): void

取消订阅预下载的错误事件。使用callback异步回调。

系统能力：SystemCapability.Request.FileTransferAgent

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 待注册回调的url，url字符串最大长度为8192字节。 |
| callback | Callback<DownloadError> | 否 | 回调函数，返回预下载的错误信息。若不填该参数，表示url下的所有错误回调函数。 |

示例：

```ets
import { cacheDownload } from '@kit.BasicServicesKit';

try {
  const errorCallback = (error: cacheDownload.DownloadError) => {
    console.info(`Error callback from cacheDownload.error code: ${error.errorCode}, error message: ${error.message}`);
  };
  // 订阅预下载的错误事件，当下载错误时执行回调，返回错误信息
  cacheDownload.onDownloadError("https://www.example.com", errorCallback);
  // 取消订阅预下载的错误事件
  cacheDownload.offDownloadError("https://www.example.com", errorCallback);
  // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```