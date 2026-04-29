# Class (WebController)

通过WebController可以控制Web组件各种行为。一个WebController对象只能控制一个Web组件，且必须在Web组件和WebController绑定后，才能调用WebController上的方法。

从API version 9开始不再维护，建议使用[WebviewController9+](Class (WebviewController).md)代替。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 8开始支持。

-

示例效果请以真机运行为准。

**创建对象**

```ets
let webController: WebController = new WebController()
```

**constructor(deprecated)**

constructor()

WebController的构造函数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[constructor11+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__constructor11)代替。

系统能力： SystemCapability.Web.Webview.Core

**getCookieManager(deprecated)**

getCookieManager(): WebCookie

获取Web组件cookie管理对象。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 9开始支持，从API version 9开始废弃，建议使用[getCookie](Class (WebCookieManager).md#ZH-CN_TOPIC_0000002522081156__getcookiedeprecated)代替。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| WebCookie | Web组件cookie管理对象，参考WebCookie定义。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('getCookieManager')
        .onClick(() => {
          let cookieManager = this.controller.getCookieManager()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**requestFocus(deprecated)**

requestFocus()

使当前web页面获取焦点。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[requestFocus9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__requestfocus)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('requestFocus')
        .onClick(() => {
          this.controller.requestFocus()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**accessBackward(deprecated)**

accessBackward(): boolean

当前页面是否可后退，即当前页面是否有返回历史记录。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[accessBackward9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__accessbackward)代替。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 可以后退返回true，否则返回false。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('accessBackward')
        .onClick(() => {
          let result = this.controller.accessBackward()
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**accessForward(deprecated)**

accessForward(): boolean

当前页面是否可前进，即当前页面是否有前进历史记录。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[accessForward9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__accessforward)代替。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前页面可以前进，返回false表示当前页面不可以前进。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('accessForward')
        .onClick(() => {
          let result = this.controller.accessForward()
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**accessStep(deprecated)**

accessStep(step: number): boolean

当前页面是否可前进或者后退给定的step步。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[accessStep9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__accessstep)代替。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | number | 是 | 要跳转的步数，正数代表前进，负数代表后退。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 页面是否前进或后退 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State steps: number = 2

  build() {
    Column() {
      Button('accessStep')
        .onClick(() => {
          let result = this.controller.accessStep(this.steps)
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**backward(deprecated)**

backward()

按照历史栈，后退一个页面。一般结合accessBackward一起使用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[backward9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__backward)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('backward')
        .onClick(() => {
          this.controller.backward()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**forward(deprecated)**

forward()

按照历史栈，前进一个页面。一般结合accessForward一起使用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[forward9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__forward)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('forward')
        .onClick(() => {
          this.controller.forward()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**deleteJavaScriptRegister(deprecated)**

deleteJavaScriptRegister(name: string)

删除通过registerJavaScriptProxy注册到window上的指定name的应用侧JavaScript对象。删除后立即生效，无须调用[refresh](#ZH-CN_TOPIC_0000002553361107__refreshdeprecated)接口。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[deleteJavaScriptRegister9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__deletejavascriptregister)代替。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 注册对象的名称，可在网页侧JavaScript中通过此名称调用应用侧JavaScript对象。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State name: string = 'Object'

  build() {
    Column() {
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          this.controller.deleteJavaScriptRegister(this.name)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**getHitTest(deprecated)**

getHitTest(): HitTestType

获取当前被点击区域的元素类型。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[getHitTest9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__gethittestdeprecated)代替。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| HitTestType | 被点击区域的元素类型。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('getHitTest')
        .onClick(() => {
          let hitType = this.controller.getHitTest()
          console.info("hitType: " + hitType)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**loadData(deprecated)**

loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })

baseUrl为空时，通过”data“协议加载指定的一段字符串。

当baseUrl为”data“协议时，编码后的data字符串将被Web组件作为”data"协议加载。

当baseUrl为“http/https"协议时，编码后的data字符串将被Web组件以类似loadUrl的方式以非编码字符串处理。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[loadData9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__loaddata)代替。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 按照”Base64“或者”URL"编码后的一段字符串。 |
| mimeType | string | 是 | 媒体类型（MIME）。 |
| encoding | string | 是 | 编码类型，具体为“Base64"或者”URL编码。 |
| baseUrl | string | 否 | 指定的一个URL路径（“http”/“https”/"data"协议），并由Web组件赋值给window.origin。 |
| historyUrl | string | 否 | 历史记录URL。非空时，可被历史记录管理，实现前后后退功能。当baseUrl为空时，此属性无效。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          this.controller.loadData({
            data: "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
            mimeType: "text/html",
            encoding: "UTF-8"
          })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**loadUrl(deprecated)**

loadUrl(options: { url: string | Resource, headers?: Array<Header> })

使用指定的http头加载指定的URL。

通过loadUrl注入的对象只在当前document有效，即通过loadUrl导航到新的页面会无效。

而通过registerJavaScriptProxy注入的对象，在loadUrl导航到新的页面也会有效。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[loadUrl9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__loadurl)代替。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | Resource | 是 | 需要加载的 URL。 |
| headers | Array<Header> | 否 | URL的附加HTTP请求头。 默认值：[]。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          this.controller.loadUrl({ url: 'www.example.com' })
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**onActive(deprecated)**

onActive(): void

调用此接口通知Web组件进入前台激活状态。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[onActive9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__onactive)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('onActive')
        .onClick(() => {
          this.controller.onActive()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**onInactive(deprecated)**

onInactive(): void

调用此接口通知Web组件进入未激活状态。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[onInactive9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__oninactive)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('onInactive')
        .onClick(() => {
          this.controller.onInactive()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**zoom(deprecated)**

zoom(factor: number): void

调整当前网页的缩放比例。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[zoom9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__zoom)代替。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factor | number | 是 | 基于当前网页所需调整的相对缩放比例，正值为放大，负值为缩小。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State factor: number = 1

  build() {
    Column() {
      Button('zoom')
        .onClick(() => {
          this.controller.zoom(this.factor)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**refresh(deprecated)**

refresh()

调用此接口通知Web组件刷新网页。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[refresh9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__refresh)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          this.controller.refresh()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**registerJavaScriptProxy(deprecated)**

registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })

注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。注册后，须调用[refresh](#ZH-CN_TOPIC_0000002553361107__refreshdeprecated)接口生效。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[registerJavaScriptProxy9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__registerjavascriptproxy)代替。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | object | 是 | 参与注册的应用侧JavaScript对象。可以声明方法，也可以声明属性，但是不支持h5直接调用。其中方法的参数和返回类型只能为string，number，boolean |
| name | string | 是 | 注册对象的名称，与window中调用的对象名一致。注册后window对象可以通过此名字访问应用侧JavaScript对象。 |
| methodList | Array<string> | 是 | 参与注册的应用侧JavaScript对象的方法。 |

示例：

```ets
// xxx.ets
class TestObj {
  constructor() {
  }

  test(): string {
    return "ArkUI Web Component"
  }

  toString(): void {
    console.info('Web Component toString')
  }

@Entry
@Component
struct Index {
  controller: WebController = new WebController()
  testObj = new TestObj();
  build() {
    Column() {
      Row() {
        Button('Register JavaScript To Window').onClick(() => {
          this.controller.registerJavaScriptProxy({
            object: this.testObj,
            name: "objName",
            methodList: ["test", "toString"],
          })
      }
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
```

 加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        Hello world!
        <script type="text/javascript">
            function htmlTest() {
                str = objName.test("test function")
                console.info('objName.test result:'+ str)
            }
        </script>
    </body>
</html>
```

**runJavaScript(deprecated)**

runJavaScript(options: { script: string, callback?: (result: string) => void })

异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScript需要在loadUrl完成后，比如onPageEnd中调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[runJavaScript9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__runjavascript)代替。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |
| callback | (result: string) => void | 否 | 回调执行JavaScript脚本结果。JavaScript脚本若执行失败或无返回值时，返回null。 |

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State webResult: string = ''
  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
      .javaScriptAccess(true)
      .onPageEnd((event) => {
        this.controller.runJavaScript({
          script: 'test()',
          callback: (result: string)=> {
            this.webResult = result
            console.info(`The test() return value is: ${result}`)
          }})
        if (event) {
          console.info('url: ', event.url)
        }
      })
    }
```

 加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8">
  </head>
  <body>
      Hello world!
      <script type="text/javascript">
          function test() {
              console.info('Ark WebComponent')
              return "This value is from index.html"
          }
      </script>
  </body>
</html>
```

**stop(deprecated)**

stop()

停止页面加载。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[stop9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__stop)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('stop')
        .onClick(() => {
          this.controller.stop()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

**clearHistory(deprecated)**

clearHistory(): void

删除所有前进后退记录。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 9开始废弃，建议使用[clearHistory9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__clearhistory)代替。

系统能力： SystemCapability.Web.Webview.Core

示例：

```ets
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('clearHistory')
        .onClick(() => {
          this.controller.clearHistory()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```