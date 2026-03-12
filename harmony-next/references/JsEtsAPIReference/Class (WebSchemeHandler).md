# Class (WebSchemeHandler)

用于拦截指定scheme的请求的拦截器。

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

#### onRequestStart12+

onRequestStart(callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void

当请求开始时的回调，在该回调函数中可以决定是否拦截该请求。当回调返回false时，表示不拦截此请求，此时handler失效；当回调返回true时，表示拦截此请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数**：

参数名类型必填说明callback(request: [WebSchemeHandlerRequest](Class (WebSchemeHandlerRequest).md), handler: [WebResourceHandler](Class (WebResourceHandler).md)) => boolean是拦截对应scheme请求开始时触发的回调。request为请求，handler用于提供自定义的返回头以及返回体给Web组件，返回值表示该请求是否拦截。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
// xxx.ets
import { webview, WebNetErrorList } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();
  htmlData: string = "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>";

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

              let response = new webview.WebSchemeHandlerResponse();
              try {
                response.setNetErrorCode(WebNetErrorList.NET_OK);
                response.setStatus(200);
                response.setStatusText("OK");
                response.setMimeType("text/html");
                response.setEncoding("utf-8");
                response.setHeaderByName("header1", "value1", false);
              } catch (error) {
                console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }

              // 调用 didFinish/didFail 前需要优先调用 didReceiveResponse 将构造的响应头传递给被拦截的请求。
              let buf = buffer.from(this.htmlData)
              try {
                if (buf.length == 0) {
                  console.info("[schemeHandler] length 0");
                  resourceHandler.didReceiveResponse(response);
                  // 如果认为buf.length为0是正常情况，则调用resourceHandler.didFinish，否则调用resourceHandler.didFail
                  resourceHandler.didFail(WebNetErrorList.ERR_FAILED);
                } else {
                  console.info("[schemeHandler] length 1");
                  resourceHandler.didReceiveResponse(response);
                  resourceHandler.didReceiveResponseBody(buf.buffer);
                  resourceHandler.didFinish();
                }
              } catch (error) {
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

#### onRequestStop12+

onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void

当请求完成时的回调，仅当[onRequestStart](#ZH-CN_TOPIC_0000002497445218__onrequeststart12)回调决定拦截此请求时触发。触发的时机有以下两点：

1.WebResourceHandler调用didFail或者didFinish。

2.此请求因为其他原因中断。

**系统能力：** SystemCapability.Web.Webview.Core

**参数**：

参数名类型必填说明callbackCallback<[WebSchemeHandlerRequest](Class (WebSchemeHandlerRequest).md)>是对应请求结束的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Invalid input parameter.

**示例：**

完整示例代码参考[onRequestStart](#ZH-CN_TOPIC_0000002497445218__onrequeststart12)。