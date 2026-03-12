# Class (WebResourceHandler)

通过WebResourceHandler，可以提供自定义的返回头以及返回体给Web组件。

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

#### didReceiveResponse12+

didReceiveResponse(response: WebSchemeHandlerResponse): void

将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明response[WebSchemeHandlerResponse](Class (WebSchemeHandlerResponse).md)是该拦截请求的响应。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.17100021The resource handler is invalid.

**示例：**

示例请参考[OnRequestStart](Class (WebSchemeHandler).md#ZH-CN_TOPIC_0000002497445218__onrequeststart12)。

#### didReceiveResponseBody12+

didReceiveResponseBody(data: ArrayBuffer): void

将构造的响应体传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明dataArrayBuffer是响应体数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.17100021The resource handler is invalid.

**示例：**

示例请参考[OnRequestStart](Class (WebSchemeHandler).md#ZH-CN_TOPIC_0000002497445218__onrequeststart12)。

#### didFinish12+

didFinish(): void

通知Web组件被拦截的请求已经完成，并且没有更多的数据可用，调用前需要优先调用[didReceiveResponse](#ZH-CN_TOPIC_0000002497605196__didreceiveresponse12)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100021The resource handler is invalid.

**示例：**

示例请参考[OnRequestStart](Class (WebSchemeHandler).md#ZH-CN_TOPIC_0000002497445218__onrequeststart12)。

#### didFail12+

didFail(code: WebNetErrorList): void

通知ArkWeb内核被拦截请求应该返回失败，调用前需要优先调用[didReceiveResponse](#ZH-CN_TOPIC_0000002497605196__didreceiveresponse12)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明code[WebNetErrorList](@ohos.web.netErrorList (ArkWeb网络协议栈错误列表).md#ZH-CN_TOPIC_0000002497445224__webneterrorlist)是网络错误码。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.17100021The resource handler is invalid.

**示例：**

示例请参考[OnRequestStart](Class (WebSchemeHandler).md#ZH-CN_TOPIC_0000002497445218__onrequeststart12)。

#### didFail20+

didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void

通知ArkWeb内核，被拦截请求应返回失败。若completeIfNoResponse为false，调用前需优先调用[didReceiveResponse](#ZH-CN_TOPIC_0000002497605196__didreceiveresponse12)，将构造的响应头传递给被拦截的请求。若completeIfNoResponse为true，且调用前未调用[didReceiveResponse](#ZH-CN_TOPIC_0000002497605196__didreceiveresponse12)，则自动生成一个响应头，网络错误码为-104，详情参见[WebNetErrorList](zh-cn_topic_0000002497445224.html#ZH-CN_TOPIC_0000002497445224__webneterrorlist)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明code[WebNetErrorList](@ohos.web.netErrorList (ArkWeb网络协议栈错误列表).md#ZH-CN_TOPIC_0000002497445224__webneterrorlist)是网络错误码。completeIfNoResponseboolean是调用当前接口时，若之前未调用过[didReceiveResponse](#ZH-CN_TOPIC_0000002497605196__didreceiveresponse12)，是否完成此次网络请求；值为true时，若之前未调用过[didReceiveResponse](#ZH-CN_TOPIC_0000002497605196__didreceiveresponse12)，则会自动生成一个response以完成此次网络请求，网络错误码为-104；值为false时，将等待应用调用[didReceiveResponse](#ZH-CN_TOPIC_0000002497605196__didreceiveresponse12)并传入response，不会直接完成此次网络请求。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100101The errorCode is either ARKWEB_NET_OK or outside the range of error codes in WebNetErrorList.17100021The resource handler is invalid.

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
      Web({ src: 'https://www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          try {
            this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
              console.info("[schemeHandler] onRequestStart");
              try {
                console.info("[schemeHandler] onRequestStart url:" + request.getRequestUrl());
                console.info("[schemeHandler] onRequestStart method:" + request.getRequestMethod());
                console.info("[schemeHandler] onRequestStart referrer:" + request.getReferrer());
                console.info("[schemeHandler] onRequestStart isMainFrame:" + request.isMainFrame());
                console.info("[schemeHandler] onRequestStart hasGesture:" + request.hasGesture());
                console.info("[schemeHandler] onRequestStart header size:" + request.getHeader().length);
                console.info("[schemeHandler] onRequestStart resource type:" + request.getRequestResourceType());
                console.info("[schemeHandler] onRequestStart frame url:" + request.getFrameUrl());
                let header = request.getHeader();
                for (let i = 0; i < header.length; i++) {
                  console.info("[schemeHandler] onRequestStart header:" + header[i].headerKey + " " + header[i].headerValue);
                }
                let stream = request.getHttpBodyStream();
                if (stream) {
                  console.info("[schemeHandler] onRequestStart has http body stream");
                } else {
                  console.info("[schemeHandler] onRequestStart has no http body stream");
                }
              } catch (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }

              if (request.getRequestUrl().endsWith("example.com")) {
                return false;
              }

              try {
                // 直接调用didFail(WebNetErrorList.ERR_FAILED, true)，自动构造一个网络请求错误ERR_CONNECTION_FAILED
                resourceHandler.didFail(WebNetErrorList.ERR_FAILED, true);
              } catch (error) {
                // 当error.code为17100101(The errorCode is either ARKWEB_NET_OK or outside the range of error codes in WebNetErrorList)
                // 且didFail(code: WebNetErrorList, completeIfNoResponse: boolean)的code值不为null时，接口会继续调用不会中断。
                console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }
              return true;
            })

            this.schemeHandler.onRequestStop((request: webview.WebSchemeHandlerRequest) => {
              console.info("[schemeHandler] onRequestStop");
            });

            this.controller.setWebSchemeHandler('https', this.schemeHandler);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        .javaScriptAccess(true)
        .domStorageAccess(true)
    }
  }
}
```