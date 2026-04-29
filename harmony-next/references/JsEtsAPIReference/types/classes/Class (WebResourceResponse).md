# Class (Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Response)

Web组件资源响应对象。示例代码参考[onHttpErrorReceive事件](事件.md#ZH-CN_TOPIC_0000002522081170__onhttperrorreceive)。


-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 8开始支持。

-

示例效果请以真机运行为准。

#### constructor

constructor()

Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Response的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getReasonMessage

getReasonMessage(): string

获取资源响应的状态码描述。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回资源响应的状态码描述。 |

#### getResponseCode

getResponseCode(): number

获取资源响应的状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回资源响应的状态码。 |

#### getResponseData

getResponseData(): string

获取资源响应数据。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回资源响应数据。 |

#### getResponseEncoding

getResponseEncoding(): string

获取资源响应的编码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回资源响应的编码。 |

#### getResponse[Header](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__header)

getResponse[Header](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__header)() : Array<Header>

获取资源响应头。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Header](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__header)> | 返回资源响应头。 |

#### getResponseMimeType

getResponseMimeType(): string

获取资源响应的媒体（MIME）类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回资源响应的媒体（MIME）类型。 |

#### getResponseDataEx13+

getResponseDataEx(): string | number | ArrayBuffer | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | undefined

获取资源响应数据，支持多种数据类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | number | ArrayBuffer | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | undefined | string返回HTML格式的字符串。 number返回文件句柄。 ArrayBuffer返回二进制数据。 Resource返回$rawfile资源。 如果没有可用数据，返回undefined。 |

#### getResponseIsReady13+

getResponseIsReady(): boolean

获取响应数据是否已准备就绪。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示响应数据已准备好，false表示未准备好。 |

#### setResponseData9+

setResponseData(data: string | number | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | ArrayBuffer): void

设置资源响应数据。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | number | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | ArrayBuffer11+ | 是 | 要设置的资源响应数据。string表示HTML格式的字符串。number表示文件句柄，此句柄由系统的Web组件负责关闭。Resource表示应用rawfile目录下文件资源。ArrayBuffer表示资源的原始二进制数据。 |

#### setResponseEncoding9+

setResponseEncoding(encoding: string): void

设置资源响应的编码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 是 | 要设置的资源响应的编码。 |

#### setResponseMimeType9+

setResponseMimeType(mimeType: string): void

设置资源响应的媒体（MIME）类型。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 要设置的资源响应的媒体（MIME）类型。 |

#### setReasonMessage9+

setReasonMessage(reason: string): void

设置资源响应的状态码描述。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | string | 是 | 要设置的资源响应的状态码描述。 |

#### setResponse[Header](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__header)9+

setResponse[Header](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__header)(header: Array<Header>): void

设置资源响应头。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| header | Array<[Header](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__header)> | 是 | 要设置的资源响应头。 |

#### setResponseCode9+

setResponseCode(code: number): void

设置资源响应的状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 要设置的资源响应的状态码。如果该资源以错误结束，请参考@ohos.web.netErrorList设置相应错误码，避免设置错误码为 ERR_IO_PENDING，设置为该错误码可能会导致XMLHttpRequest同步请求阻塞。 |

#### setResponseIsReady9+

setResponseIsReady(IsReady: boolean): void

设置资源响应数据是否已经就绪。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| IsReady | boolean | 是 | 资源响应数据是否已经就绪。 true表示资源响应数据已经就绪，false表示资源响应数据未就绪。 如果数据是异步提供，需要显式设置为false。设置为非法值如null，undefined或者不设置都会被认为数据已经准备好。 |