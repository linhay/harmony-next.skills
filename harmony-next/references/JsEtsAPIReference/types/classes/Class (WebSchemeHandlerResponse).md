# Class (WebSchemeHandlerResponse)

请求的响应，可以为被拦截的请求创建一个Response并填充自定义的内容返回给Web组件。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 12开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

#### constructor12+

constructor()

Response的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ets
// xxx.ets
import { webview, WebNetErrorList } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('response').onClick(() => {
        let response = new webview.WebSchemeHandlerResponse();
        try {
          response.setUrl("http://www.example.com")
          response.setStatus(200)
          response.setStatusText("OK")
          response.setMimeType("text/html")
          response.setEncoding("utf-8")
          response.setHeaderByName("header1", "value1", false)
          response.setNetErrorCode(WebNetErrorList.NET_OK)
          console.info("[schemeHandler] getUrl:" + response.getUrl())
          console.info("[schemeHandler] getStatus:" + response.getStatus())
          console.info("[schemeHandler] getStatusText:" + response.getStatusText())
          console.info("[schemeHandler] getMimeType:" + response.getMimeType())
          console.info("[schemeHandler] getEncoding:" + response.getEncoding())
          console.info("[schemeHandler] getHeaderByValue:" + response.getHeaderByName("header1"))
          console.info("[schemeHandler] getNetErrorCode:" + response.getNetErrorCode())

        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'https://www.example.com', controller: this.controller })
    }
  }
}
```

#### setUrl12+

setUrl(url: string): void

给当前的Response设置重定向或因HSTS而更改后的URL，设置了url后会触发请求的跳转。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明urlstring是即将要跳转的URL。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

#### setNetErrorCode12+

setNetErrorCode(code: WebNetErrorList): void

给当前的Response设置网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明code[WebNetErrorList](../../modules/ohos/@ohos.web.netErrorList (ArkWeb网络协议栈错误列表).md#ZH-CN_TOPIC_0000002497445224__webneterrorlist)是网络错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### setStatus12+

setStatus(code: number): void

给当前的Response设置HTTP状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明codenumber是Http状态码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### setStatusText12+

setStatusText(text: string): void

给当前的Response设置状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明textstring是状态文本。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### setMimeType12+

setMimeType(type: string): void

给当前的Response设置媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明typestring是媒体类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### setEncoding12+

setEncoding(encoding: string): void

给当前的Response设置字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明encodingstring是字符集。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### setHeaderByName12+

setHeaderByName(name: string, value: string, overwrite: boolean): void

给当前的Response设置头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明namestring是头部（header）的名称。valuestring是头部（header）的值。overwriteboolean是如果为true，将覆盖现有的头部，否则不覆盖。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### getUrl12+

getUrl(): string

获取重定向或由于HSTS而更改后的URL。

风险提示：如果想获取url来做JavascriptProxy通信接口认证，请使用[getLastJavascriptProxyCallingFrameUrl12+](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__getlastjavascriptproxycallingframeurl12)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string获取经过重定向或由于HSTS而更改后的URL。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### getNetErrorCode12+

getNetErrorCode(): WebNetErrorList

获取Response的网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明[WebNetErrorList](../../modules/ohos/@ohos.web.netErrorList (ArkWeb网络协议栈错误列表).md#ZH-CN_TOPIC_0000002497445224__webneterrorlist)获取Response的网络错误码。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### getStatus12+

getStatus(): number

获取Response的Http状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明number获取Response的Http状态码。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### getStatusText12+

getStatusText(): string

获取Response的状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string状态文本。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### getMimeType12+

getMimeType(): string

获取Response的媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string媒体类型。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### getEncoding12+

getEncoding(): string

获取Response的字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string字符集。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。

#### getHeaderByName12+

getHeaderByName(name: string): string

按名称获取Response头部字段值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明namestring是头部（header）的名称。

**返回值：**

类型说明string头部（header）的值。

**示例：**

完整示例代码参考[constructor](#ZH-CN_TOPIC_0000002529445163__constructor12)。