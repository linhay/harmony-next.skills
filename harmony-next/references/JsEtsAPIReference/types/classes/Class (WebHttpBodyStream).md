# Class (WebHttpBodyStream)

POST、PUT请求的数据体，支持BYTES、FILE、BLOB、CHUNKED类型的数据。注意本类中其他接口需要在[initialize](#ZH-CN_TOPIC_0000002553361083__initialize12)成功后才能调用。


-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 12开始支持。

-

示例效果请以真机运行为准。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

#### initialize12+

initialize(): Promise<void>

初始化WebHttpBodyStream。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取WebHttpBodyStream是否初始化成功。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码]([Webview错误码](../../errors/Webview错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100022 | Failed to initialize the HTTP body stream. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
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
      Button('postUrl')
        .onClick(() => {
          try {
            let postData = buffer.from(this.htmlData);
            this.controller.postUrl('https://www.example.com', postData.buffer);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'https://www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          try {
            this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
              console.info("[schemeHandler] onRequestStart");
              try {
                let stream = request.getHttpBodyStream();
                if (stream) {
                  stream.initialize().then(() => {
                    if (!stream) {
                      return;
                    }
                    console.info("[schemeHandler] onRequestStart postDataStream size:" + stream.getSize());
                    console.info("[schemeHandler] onRequestStart postDataStream position:" + stream.getPosition());
                    console.info("[schemeHandler] onRequestStart postDataStream isChunked:" + stream.isChunked());
                    console.info("[schemeHandler] onRequestStart postDataStream isEof:" + stream.isEof());
                    console.info("[schemeHandler] onRequestStart postDataStream isInMemory:" + stream.isInMemory());
                    stream.read(stream.getSize()).then((buffer) => {
                      if (!stream) {
                        return;
                      }
                      console.info("[schemeHandler] onRequestStart postDataStream readlength:" + buffer.byteLength);
                      console.info("[schemeHandler] onRequestStart postDataStream isEof:" + stream.isEof());
                      console.info("[schemeHandler] onRequestStart postDataStream position:" + stream.getPosition());
                    }).catch((error: BusinessError) => {
                      console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
                    })
                  }).catch((error: BusinessError) => {
                    console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
                  })
                } else {
                  console.info("[schemeHandler] onRequestStart has no http body stream");
                }
              } catch (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }

              return false;
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
```

#### read12+

read(size: number): Promise<ArrayBuffer>

读取WebHttpBodyStream中的数据。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 读取WebHttpBodyStream中的字节数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise实例，用于获取WebHttpBodyStream中读取的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

完整示例代码参考[initialize](#ZH-CN_TOPIC_0000002553361083__initialize12)。

#### getSize12+

getSize(): number

获取WebHttpBodyStream中的数据大小，分块传输时总是返回零。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取WebHttpBodyStream中的数据大小。 |

**示例：**

完整示例代码参考[initialize](#ZH-CN_TOPIC_0000002553361083__initialize12)。

#### getPosition12+

getPosition(): number

读取WebHttpBodyStream中当前的读取位置。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | WebHttpBodyStream中当前的读取位置。 |

**示例：**

完整示例代码参考[initialize](#ZH-CN_TOPIC_0000002553361083__initialize12)。

#### isChunked12+

isChunked(): boolean

WebHttpBodyStream是否采用分块传输。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream是否采用分块传输，如果采用分块传输则返回true，否则返回false。 |

**示例：**

完整示例代码参考[initialize](#ZH-CN_TOPIC_0000002553361083__initialize12)。

#### isEof12+

isEof(): boolean

判断WebHttpBodyStream中的所有数据是否都已被读取。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream中的所有数据是否都已被读取。 如果所有数据都已被读取，则返回true。对于分块传输类型的WebHttpBodyStream，在第一次读取尝试之前返回false。 |

**示例：**

完整示例代码参考[initialize](#ZH-CN_TOPIC_0000002553361083__initialize12)。

#### isInMemory12+

isInMemory(): boolean

判断WebHttpBodyStream中的上传数据是否在内存中。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream中的上传数据是否在内存中。 如果WebHttpBodyStream中的上传数据完全在内存中，并且所有读取请求都将同步成功，则返回true。对于分块传输类型的数据，预期返回false。 |

**示例：**

完整示例代码参考[initialize](#ZH-CN_TOPIC_0000002553361083__initialize12)。