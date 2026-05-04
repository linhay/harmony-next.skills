# Class (WebviewController)

通过WebviewController可以控制Web组件各种行为（包括页面导航、生命周期状态、JavaScript交互等行为）。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

#### constructor11+

constructor(webTag?: string)

用于创建 WebviewController 对象的构造函数。

不传参：new webview.WebviewController()表示构造函数为空，不使用C API时不需要传参。

传参且参数是合法字符串：new webview.WebviewController("xxx")，用于开发者区分多实例，并调用对应实例下的方法。

传入参数为空：new webview.WebviewController("")或new webview.WebviewController(undefined)，该场景下参数无意义，无法区分多个实例，直接返回undefined，需要开发者判断返回值是否正常。

Web组件销毁后会解绑WebViewController，之后调用WebviewController的非静态方法会抛出17100001异常，应注意调用时机和捕获异常，防止进程异常退出。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webTag | string | 否 | 指定了 Web 组件的名称。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString');
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  @State webTestObj: WebObj = new WebObj();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: '', controller: this.controller })
        .javaScriptAccess(true)
        .onControllerAttached(() => {
          this.controller.loadUrl($rawfile("index.html"));
          this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
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
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)
        }
      </script>
    </body>
</html>
```

#### initializeWebEngine

static initializeWebEngine(): void

在 Web 组件初始化之前，通过此接口加载 Web 引擎的动态库文件，以提高启动性能。自动预连接历史访问过的高频网站。

- initializeWebEngine不支持在异步线程中调用，否则会造成崩溃。
- initializeWebEngine全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

本示例以EntryAbility为例，描述了在 Ability 创建阶段完成 Web 组件动态库加载的功能。

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.initializeWebEngine()
    console.info("EntryAbility onCreate done")
  }
```

#### setHttpDns10+

static setHttpDns(secureDnsMode:[SecureDnsMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__securednsmode10), secureDnsConfig:string): void

设置Web组件是否使用HTTPDNS解析DNS。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| secureDnsMode | [SecureDnsMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__securednsmode10) | 是 | 使用HTTPDNS的模式。 |
| secureDnsConfig | string | 是 | HTTPDNS server的配置，必须是https协议并且只允许配置一个server。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    try {
      webview.WebviewController.setHttpDns(webview.SecureDnsMode.AUTO, "https://example1.test")
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done")
  }
```

#### setWebDebuggingAccess

static setWebDebuggingAccess(webDebuggingAccess: boolean): void

设置是否启用网页调试功能。详情请参考[DevTools工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-debugging-with-devtools)。

安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患，不建议在应用正式发布版本中启用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | 是 | 设置是否启用网页调试功能。 true表示启用网页调试功能。false表示不启用网页调试功能。 默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.setWebDebuggingAccess(true);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
}
```

#### loadUrl

loadUrl(url: string | Resource, headers?: Array<WebHeader>): void

加载指定的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | Resource | 是 | 需要加载的 URL。 |
| headers | Array<WebHeader> | 否 | URL的附加HTTP请求头。 默认值： []。 传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码]([Webview错误码](../../errors/Webview错误码.md).md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid. |
| 17100003 | Invalid resource path or file type. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // 需要加载的URL是string类型。
            this.controller.loadUrl('www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // 带参数headers。
            this.controller.loadUrl('www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
}
```

加载本地网页，加载本地资源文件有三种方式。

1.$rawfile方式。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // 通过$rawfile加载本地资源文件。
            this.controller.loadUrl($rawfile('index.html'));
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

2.resources协议。

使用 resource://rawfile/ 协议前缀可以避免常规 $rawfile 方式在处理带有“#”路由链接时的局限性。当URL中包含“#”号时，“#”后面的内容会被视为锚点（fragment）。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // 通过resource协议加载本地资源文件。
            this.controller.loadUrl("resource://rawfile/index.html#home");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

在“src\main\resources\rawfile”文件夹下创建index.html：

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<div id="content"></div>

<script>
    function loadContent() {
      var hash = window.location.hash;
      var contentDiv = document.getElementById('content');

      if (hash === '#home') {
        contentDiv.innerHTML = '<h1>Home Page</h1><p>Welcome to the Home Page!</p>';
      } else {
        contentDiv.innerHTML = '<h1>Default Page</h1><p>This is the default content.</p>';
    }

    // 加载界面
    window.addEventListener('load', loadContent);

    // 当hash变化时，更新界面
    window.addEventListener('hashchange', loadContent);
</script>
</body>
</html>
```

3.通过沙箱路径加载本地文件，可以参考[web](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-page-loading-with-web-components#加载本地页面)加载沙箱路径的示例代码。

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
  <body>
    <p>Hello World</p>
  </body>
</html>
```

#### loadData

loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void

加载指定的数据。

baseUrl与historyUrl同时为空的情况下：

encoding如果为非base64（包括空值），则假定数据对安全URL字符范围内的八位字节使用ASCII编码，对该范围外的八位字节使用URL的标准%xx十六进制编码。

data数据必须使用base64编码或将内容中的任何#字符编码为%23。否则#将被视为内容的结尾而剩余的文本将被用作文档片段标识符。

-

若加载本地图片，可以给baseUrl或historyUrl任一参数赋值空格，详情请参考示例代码。

-

加载本地图片场景，baseUrl和historyUrl不能同时为空，否则图片无法成功加载。

-

若html中的富文本中带有注入#等特殊字符，建议将baseUrl和historyUrl两个参数的值设置为"空格"。

-

加载文字场景，需主动设置<meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">避免文本字体大小不一致。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 按照"base64"或者"URL"编码后的一段字符串。 |
| mimeType | string | 是 | 媒体类型（MIME）。 |
| encoding | string | 是 | 编码类型，具体为"base64"或者"URL"编码。 |
| baseUrl | string | 否 | 指定的一个URL路径（"http"/"https"/"data"协议），并由Web组件赋值给window.origin。当加载大量html文件时，需设置为"data"。 传入undefined或null会抛出异常错误码401。 |
| historyUrl | string | 否 | 用作历史记录所使用的URL。非空时，历史记录以此URL进行管理。当baseUrl为空时，此属性无效。 传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

baseUrl与historyUrl同时为空。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
              "text/html",
              // UTF-8为charset。
              "UTF-8"
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              // Coding tests通过base64编码后的字符串。
              "Q29kaW5nIHRlc3Rz",
              "text/html",
              "base64"
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
}
```

指定baseURL。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<img src=aa/bb.jpg>", // 会尝试从"https://xxx.com/" + "aa/bb.jpg"加载该图片
              "text/html",
              "UTF-8",
              "https://xxx.com/",
              "about:blank"
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

加载本地资源。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  updataContent: string = '<body><div><image src="resource://rawfile/xxx.png" alt="image -- end" width="500" height="250"></image></div></body>'

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            // UTF-8为charset。
            this.controller.loadData(this.updataContent, "text/html", "UTF-8", " ", " ");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
}
```

加载沙箱图片。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<img src=bb.jpg>", // 尝试从"file:///xxx/" + "bb.jpg"加载该图片。
              "text/html",
              "UTF-8",
              // 加载本地应用沙箱内的图片路径，请将路径改为实际使用的沙箱路径。
              "file:///data/storage/el2/base/haps/entry/files/data/.cache_dir/",
              ""
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(true) // 为了加载应用沙箱内的图片，需要启用文件访问功能。
    }
```

#### accessForward

accessForward(): boolean

当前页面是否可前进，即当前页面是否有前进历史记录。

可以结合使用[getBackForwardEntries](#ZH-CN_TOPIC_0000002553201117__getbackforwardentries)来获取当前WebView的历史信息列表，以及使用[accessStep](#ZH-CN_TOPIC_0000002553201117__accessstep)来判断是否可以按照给定的步数前进或后退。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可以前进返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('accessForward')
        .onClick(() => {
          try {
            let result = this.controller.accessForward();
            console.info('result:' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### forward

forward(): void

按照历史栈，前进一个页面。一般结合accessForward一起使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('forward')
        .onClick(() => {
          try {
            this.controller.forward();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### accessBackward

accessBackward(): boolean

当前页面是否可后退，即当前页面是否有返回历史记录。

可以结合使用[getBackForwardEntries](#ZH-CN_TOPIC_0000002553201117__getbackforwardentries)来获取当前WebView的历史信息列表，以及使用[accessStep](#ZH-CN_TOPIC_0000002553201117__accessstep)来判断是否可以按照给定的步数前进或后退。


在Web组件首次加载过程中调用[setCustomUserAgent](#ZH-CN_TOPIC_0000002553201117__setcustomuseragent10)，可能会导致在当前存在多个历史节点的情况下，获取的accessBackward实际为false，即没有后退节点。建议先调用setCustomUserAgent方法设置UserAgent，再通过loadUrl加载具体页面。

该现象是由于在Web组件首次加载时，调用[setCustomUserAgent](#ZH-CN_TOPIC_0000002553201117__setcustomuseragent10)会导致组件重新加载并保持初始历史节点的状态。随后新增的节点将替换初始历史节点，不会生成新的历史节点，导致accessBackward为false。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前页面可以后退返回true,否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('accessBackward')
        .onClick(() => {
          try {
            let result = this.controller.accessBackward();
            console.info('result:' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### backward

backward(): void

按照历史栈，后退一个页面。一般结合[accessBackward](#ZH-CN_TOPIC_0000002553201117__accessbackward)一起使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('backward')
        .onClick(() => {
          try {
            this.controller.backward();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### onActive

onActive(): void

调用此接口通知Web组件进入前台激活状态。

激活状态是应用与用户互动的状态。应用会保持这种状态，直到发生某些事件（例如收到来电或设备屏幕关闭）时将焦点从应用移开。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('onActive')
        .onClick(() => {
          try {
            this.controller.onActive();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### onInactive

onInactive(): void

调用此接口通知Web组件进入未激活状态。开发者可以在此回调中实现应用失去焦点时应表现的恰当行为。

此状态下会尽可能的暂停任何可以安全暂停的内容，例如动画和地理位置。但不会暂停JavaScript，要全局暂停JavaScript，请使用[pauseAllTimers](#ZH-CN_TOPIC_0000002553201117__pausealltimers12)。要重新激活Web组件，请调用[onActive](#ZH-CN_TOPIC_0000002553201117__onactive)。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('onInactive')
        .onClick(() => {
          try {
            this.controller.onInactive();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### refresh

refresh(): void

调用此接口通知Web组件刷新网页。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### accessStep

accessStep(step: number): boolean

当前页面是否可前进或者后退给定的step步。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | number | 是 | 要跳转的步数，正数代表前进，负数代表后退。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 页面是否前进或后退。 返回true表示可以前进或者后退，返回false表示不可以前进或后退。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State steps: number = 2;

  build() {
    Column() {
      Button('accessStep')
        .onClick(() => {
          try {
            let result = this.controller.accessStep(this.steps);
            console.info('result:' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### clearHistory

clearHistory(): void

删除所有前进后退记录，不建议在onErrorReceive与onPageBegin中调用clearHistory，会造成异常退出。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearHistory')
        .onClick(() => {
          try {
            this.controller.clearHistory();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### registerJavaScriptProxy

registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string): void

registerJavaScriptProxy提供了应用与Web组件加载的网页之间强大的交互能力。注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。

示例请参考[前端页面调用应用侧函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-page-app-function-invoking)。

- registerJavaScriptProxy需要和deleteJavaScriptRegister接口配合使用，防止内存泄漏。
- 请尽可能只在可信的URL及安全通信HTTPS场景下进行registerJavaScriptProxy注册。在非可信的Web组件中注入JavaScript对象，可能会导致应用被恶意攻击。
- 在注册registerJavaScriptProxy后，应用会将JavaScript对象暴露给所有的页面frames。
- 同一方法在同步与异步列表中重复注册，将默认异步调用。
- 同步函数列表和异步函数列表不可同时为空，否则此次调用接口注册失败。
- 异步的作用在于：H5线程将异步JavaScript任务提交给ETS主线程后，无需等待任务执行完成并返回结果，H5线程即可继续执行后续任务。这在执行耗时较长的JavaScript任务或ETS线程较为拥堵的情况下，可以有效减少H5线程因JavaScript任务而被阻塞的情况。然而，异步JavaScript任务无法返回值，且任务执行的顺序无法保证，因此需要根据具体情境判断是否使用同步或异步方式。
- 注入的对象在页面下一次（重新）加载前不会出现在JavaScript中。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jsObject | object | 是 | 参与注册的应用侧JavaScript对象。可以单独声明方法和属性，但无法同时进行注册与使用。对象只包含属性时，H5可以访问对象中的属性。对象只包含方法时，H5可以访问对象中的方法。 1. 方法的参数和返回类型可以为string，number，boolean。 2. 方法的参数和返回类型支持Dictionary，Array，最多嵌套10层，每层1w个数据。 3. 方法的参数和返回类型支持Object，需要在Object里添加属性methodNameListForJsProxy:[fun1, fun2]，fun1和fun2为可被调用的方法。 4. 方法的参数支持Function，Promise，它们的Callback不能有返回值。 5. 方法的返回类型支持Promise，Promise的Callback不能有返回值。 |
| name | string | 是 | 注册对象的名称，与window中调用的对象名一致。注册后window对象可以通过此名字访问应用侧JavaScript对象。 |
| methodList | Array<string> | 是 | 参与注册的应用侧JavaScript对象的同步方法。 |
| asyncMethodList12+ | Array<string> | 否 | 参与注册的应用侧JavaScript对象的异步方法，默认为空。异步方法无法获取返回值。 传入undefined或null会抛出异常错误码401。 |
| permission12+ | string | 否 | JSON字符串，默认为空，通过该字符串配置JSBridge的权限管控，可以定义object和method级别的URL白名单。 1. scheme（协议）和host（域名）参数不可为空，且host不支持通配符，只能填写完整的host。 2. 可以仅配置object级别的白名单，该白名单对所有JSBridge方法生效。 3. 若JSBridge方法A设置了method级别的白名单，那么方法A最终的白名单是object级别白名单与method级别白名单的交集。 传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr);
    return testStr;
  }

  toString(): void {
    console.info('Web Component toString');
  }

  testNumber(testNum: number): number {
    console.info('Web Component number' + testNum);
    return testNum;
  }

  asyncTestBool(testBol: boolean): void {
    console.info('Web Component boolean' + testBol);
  }

class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString');
  }

class AsyncObj {
  constructor() {
  }

  asyncTest(): void {
    console.info('Async test');
  }

  asyncString(testStr: string): void {
    console.info('Web async string' + testStr);
}

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();
  @State webTestObj: WebObj = new WebObj();
  @State asyncTestObj: AsyncObj = new AsyncObj();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            // 同时注册同步和异步函数
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber"], ["asyncTestBool"]);
            // 仅注册同步函数
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
            // 仅注册异步函数
            this.controller.registerJavaScriptProxy(this.asyncTestObj, "objAsyncName", [], ["asyncTest", "asyncString"]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
            this.controller.deleteJavaScriptRegister("objTestName");
            this.controller.deleteJavaScriptRegister("objAsyncName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
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
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <p id="asyncDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "ArkUI Web Component"
          let str=objName.test("webtest data");
          objName.testNumber(1);
          objName.asyncTestBool(true);
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)

          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)

          objAsyncName.asyncTest();
          objAsyncName.asyncString("async test data");
        }
      </script>
    </body>
</html>
```

更多示例，请参考[前端页面调用应用侧函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-page-app-function-invoking)。

#### runJavaScript

runJavaScript(script: string, callback : AsyncCallback<string>): void

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过异步回调方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

- 跨导航操作（如loadUrl）时，JavaScript状态将不再保留。例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。
- 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。
- 目前不支持传递对象，支持传递结构体。
- 执行异步方法无法获取返回值，需要根据具体情境判断是否使用同步或异步方式。
- 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |
| callback | AsyncCallback<string> | 是 | 回调执行JavaScript脚本结果。JavaScript脚本若执行失败或无返回值时，返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webResult: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScript(
              'test()',
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                  return;
                }
                if (result) {
                  this.webResult = result;
                  console.info(`The test() return value is: ${result}`);
                }
              });
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
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

#### runJavaScript

runJavaScript(script: string): Promise<string>

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过Promise方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

- 跨导航操作（如loadUrl）时，JavaScript状态 将不再保留，例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。
- 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。
- 目前不支持传递对象，支持传递结构体。
- 执行异步方法无法获取返回值，需要根据具体情境判断是否使用同步或异步方式。
- 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise实例，返回脚本执行的结果，执行失败返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScript('test()')
              .then((result) => {
                console.info('result: ' + result);
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              })
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
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

#### runJavaScriptExt10+

runJavaScriptExt(script: string | ArrayBuffer, callback : AsyncCallback<JsMessageExt>): void

异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中调用。

- 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | ArrayBuffer12+ | 是 | JavaScript脚本。 |
| callback | AsyncCallback<JsMessageExt> | 是 | 回调执行JavaScript脚本结果。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScriptExt(
              'test()',
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
                  return;
                }
                if (result) {
                  try {
                    if (result.getErrorDescription()) {
                      // 若发生异常或返回类型不支持时，getErrorDescription不为空
                      console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                      return;
                    }
                    let type = result.getType();
                    switch (type) {
                      case webview.JsMessageType.STRING: {
                        this.msg1 = "result type:" + typeof (result.getString());
                        this.msg2 = "result getString:" + ((result.getString()));
                        break;
                      }
                      case webview.JsMessageType.NUMBER: {
                        this.msg1 = "result type:" + typeof (result.getNumber());
                        this.msg2 = "result getNumber:" + ((result.getNumber()));
                        break;
                      }
                      case webview.JsMessageType.BOOLEAN: {
                        this.msg1 = "result type:" + typeof (result.getBoolean());
                        this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                        break;
                      }
                      case webview.JsMessageType.ARRAY_BUFFER: {
                        this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                        this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                        break;
                      }
                      case webview.JsMessageType.ARRAY: {
                        this.msg1 = "result type:" + typeof (result.getArray());
                        this.msg2 = "result getArray:" + result.getArray();
                        break;
                      }
                      default: {
                        this.msg1 = "default break, type:" + type;
                        break;
                      }
                  catch (resError) {
                    console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
                }
              });
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (resError) {
            console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
          }
        })
}
```

```ets
// 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据。
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = ''
  @State msg2: string = ''

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let uiContext : UIContext = this.getUIContext();
            let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // 新建并打开文件。
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // 写入一段内容至文件。
            fileIo.writeSync(file.fd, "test()");
            // 从文件中读取内容。
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // 关闭文件。
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(
              arrayBuffer,
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
                  return;
                }
                if (result) {
                  try {
                    if (result.getErrorDescription()) {
                      // 若发生异常或返回类型不支持时，getErrorDescription不为空
                      console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                      return;
                    }
                    let type = result.getType();
                    switch (type) {
                      case webview.JsMessageType.STRING: {
                        this.msg1 = "result type:" + typeof (result.getString());
                        this.msg2 = "result getString:" + ((result.getString()));
                        break;
                      }
                      case webview.JsMessageType.NUMBER: {
                        this.msg1 = "result type:" + typeof (result.getNumber());
                        this.msg2 = "result getNumber:" + ((result.getNumber()));
                        break;
                      }
                      case webview.JsMessageType.BOOLEAN: {
                        this.msg1 = "result type:" + typeof (result.getBoolean());
                        this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                        break;
                      }
                      case webview.JsMessageType.ARRAY_BUFFER: {
                        this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                        this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                        break;
                      }
                      case webview.JsMessageType.ARRAY: {
                        this.msg1 = "result type:" + typeof (result.getArray());
                        this.msg2 = "result getArray:" + result.getArray();
                        break;
                      }
                      default: {
                        this.msg1 = "default break, type:" + type;
                        break;
                      }
                  catch (resError) {
                    console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
                }
              });
          } catch (resError) {
            console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
}
```

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html lang="en-gb">
<body>
<h1>run JavaScript Ext demo</h1>
</body>
<script type="text/javascript">
function test() {
  return "hello, world";
}
</script>
</html>
```

#### runJavaScriptExt10+

runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>

异步执行JavaScript脚本，并通过Promise方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中调用。

- 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | ArrayBuffer12+ | 是 | JavaScript脚本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<JsMessageExt> | Promise实例，返回脚本执行的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webResult: string = '';
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(() => {
          this.controller.runJavaScriptExt('test()')
            .then((result) => {
              try {
                if (result.getErrorDescription()) {
                  // 若发生异常或返回类型不支持时，getErrorDescription不为空
                  console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                  return;
                }
                let type = result.getType();
                switch (type) {
                  case webview.JsMessageType.STRING: {
                    this.msg1 = "result type:" + typeof (result.getString());
                    this.msg2 = "result getString:" + ((result.getString()));
                    break;
                  }
                  case webview.JsMessageType.NUMBER: {
                    this.msg1 = "result type:" + typeof (result.getNumber());
                    this.msg2 = "result getNumber:" + ((result.getNumber()));
                    break;
                  }
                  case webview.JsMessageType.BOOLEAN: {
                    this.msg1 = "result type:" + typeof (result.getBoolean());
                    this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                    break;
                  }
                  case webview.JsMessageType.ARRAY_BUFFER: {
                    this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                    this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                    break;
                  }
                  case webview.JsMessageType.ARRAY: {
                    this.msg1 = "result type:" + typeof (result.getArray());
                    this.msg2 = "result getArray:" + result.getArray();
                    break;
                  }
                  default: {
                    this.msg1 = "default break, type:" + type;
                    break;
                  }
              catch (resError) {
                console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
              }
            }).catch((error: BusinessError) => {
            console.error("error: " + error);
          })
}
```

```ets
// 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据。
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let uiContext : UIContext = this.getUIContext();
            let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // 新建并打开文件。
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // 写入一段内容至文件。
            fileIo.writeSync(file.fd, "test()");
            // 从文件中读取内容。
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // 关闭文件。
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(arrayBuffer)
              .then((result) => {
                try {
                  if (result.getErrorDescription()) {
                    // 若发生异常或返回类型不支持时，getErrorDescription不为空
                    console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                    return;
                  }
                  let type = result.getType();
                  switch (type) {
                    case webview.JsMessageType.STRING: {
                      this.msg1 = "result type:" + typeof (result.getString());
                      this.msg2 = "result getString:" + ((result.getString()));
                      break;
                    }
                    case webview.JsMessageType.NUMBER: {
                      this.msg1 = "result type:" + typeof (result.getNumber());
                      this.msg2 = "result getNumber:" + ((result.getNumber()));
                      break;
                    }
                    case webview.JsMessageType.BOOLEAN: {
                      this.msg1 = "result type:" + typeof (result.getBoolean());
                      this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                      break;
                    }
                    case webview.JsMessageType.ARRAY_BUFFER: {
                      this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                      this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                      break;
                    }
                    case webview.JsMessageType.ARRAY: {
                      this.msg1 = "result type:" + typeof (result.getArray());
                      this.msg2 = "result getArray:" + result.getArray();
                      break;
                    }
                    default: {
                      this.msg1 = "default break, type:" + type;
                      break;
                    }
                catch (resError) {
                  console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
                }
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
}
```

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html lang="en-gb">
<body>
<h1>run JavaScript Ext demo</h1>
</body>
<script type="text/javascript">
function test() {
  return "hello, world";
}
</script>
</html>
```

#### deleteJavaScriptRegister

deleteJavaScriptRegister(name: string): void

删除通过[registerJavaScriptProxy](#ZH-CN_TOPIC_0000002553201117__registerjavascriptproxy)或者[javaScriptProxy](属性.md#ZH-CN_TOPIC_0000002553201131__javascriptproxy)注册到window上的指定name的应用侧JavaScript对象。删除操作在页面下次（重新）加载后生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 注册对象的名称，可在网页侧JavaScript中通过此名称调用应用侧JavaScript对象。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100008 | Failed to delete JavaScriptProxy because it does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(): string {
    return "ArkUI Web Component";
  }

  toString(): void {
    console.info('Web Component toString');
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();
  @State name: string = 'objName';
  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            this.controller.registerJavaScriptProxy(this.testObjtest, this.name, ["test", "toString"]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister(this.name);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
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
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <script type="text/javascript">
        function htmlTest() {
          let str=objName.test();
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)
        }
      </script>
    </body>
</html>
```

#### zoom

zoom(factor: number): void

调整当前网页的缩放比例，[zoomAccess](属性.md#ZH-CN_TOPIC_0000002553201131__zoomaccess)需为true。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factor | number | 是 | 基于当前网页所需调整的相对缩放比例，入参要求大于0，当入参为1时为默认加载网页的缩放比例，入参小于1为缩小，入参大于1为放大。 取值范围：(0，100]。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State factor: number = 2;

  build() {
    Column() {
      Button('zoom')
        .onClick(() => {
          try {
            this.controller.zoom(this.factor);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
```

#### searchAllAsync

searchAllAsync(searchString: string): void

异步查找网页中所有匹配关键字'searchString'的内容并高亮，结果通过[onSearchResultReceive](事件.md#ZH-CN_TOPIC_0000002522081170__onsearchresultreceive9)异步返回。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 | 查找的关键字。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State searchString: string = "Hello World";

  build() {
    Column() {
      Button('searchString')
        .onClick(() => {
          try {
            this.controller.searchAllAsync(this.searchString);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onSearchResultReceive(ret => {
          if (ret) {
            console.info("on search result receive:" + "[cur]" + ret.activeMatchOrdinal +
              "[total]" + ret.numberOfMatches + "[isDone]" + ret.isDoneCounting);
          }
        })
    }
```

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
  <body>
    <p>Hello World Highlight Hello World</p>
  </body>
</html>
```

#### clearMatches

clearMatches(): void

清除所有通过[searchAllAsync](#ZH-CN_TOPIC_0000002553201117__searchallasync)匹配到的高亮字符查找结果。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearMatches')
        .onClick(() => {
          try {
            this.controller.clearMatches();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
```

加载的html文件，请参考[searchAllAsync](#ZH-CN_TOPIC_0000002553201117__searchallasync)接口下加载的html文件。

#### searchNext

searchNext(forward: boolean): void

滚动到下一个匹配的查找结果并高亮。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| forward | boolean | 是 | 从前向后或者逆向查找方式。 true表示从前向后查找，false表示从后向前查找。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('searchNext')
        .onClick(() => {
          try {
            this.controller.searchNext(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
```

加载的html文件，请参考[searchAllAsync](#ZH-CN_TOPIC_0000002553201117__searchallasync)接口下加载的html文件。

#### clearSslCache

clearSslCache(): void

清除Web组件记录的SSL证书错误事件对应的用户操作行为。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearSslCache')
        .onClick(() => {
          try {
            this.controller.clearSslCache();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### clearClientAuthenticationCache

clearClientAuthenticationCache(): void

清除Web组件记录的客户端证书请求事件对应的用户操作行为。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearClientAuthenticationCache')
        .onClick(() => {
          try {
            this.controller.clearClientAuthenticationCache();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### createWebMessagePorts

createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>

创建Web消息端口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isExtentionType10+ | boolean | 否 | 是否使用扩展增强接口。 true表示使用扩展增强接口，false表示不使用扩展增强接口。 默认值：false。 传入undefined或null会抛出异常错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<WebMessagePort> | web消息端口列表。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002522081164__onmessageeventext10)。

#### postMessage

postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void

发送Web消息端口到HTML。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要发送的消息名称。 |
| ports | Array<WebMessagePort> | 是 | 要发送的消息端口。 |
| uri | string | 是 | 接收该消息的URI。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  ports: webview.WebMessagePort[] = [];
  @State sendFromEts: string = 'Send this message from ets to HTML';
  @State receivedFromHtml: string = 'Display received message send from HTML';

  build() {
    Column() {
      // 展示接收到的来自HTML的内容
      Text(this.receivedFromHtml)
      // 输入框的内容发送到html
      TextInput({ placeholder: 'Send this message from ets to HTML' })
        .onChange((value: string) => {
          this.sendFromEts = value;
        })

      Button('postMessage')
        .onClick(() => {
          try {
            // 1、创建两个消息端口。
            this.ports = this.controller.createWebMessagePorts();
            // 2、在应用侧的消息端口(如端口1)上注册回调事件。
            this.ports[1].onMessageEvent((result: webview.WebMessage) => {
              let msg = 'Got msg from HTML:';
              if (typeof (result) == "string") {
                console.info("received string message from html5, string is:" + result);
                msg = msg + result;
              } else if (typeof (result) == "object") {
                if (result instanceof ArrayBuffer) {
                  console.info("received arraybuffer from html5, length is:" + result.byteLength);
                  msg = msg + "length is " + result.byteLength;
                } else {
                  console.info("not support");
                }
              } else {
                console.info("not support");
              }
              this.receivedFromHtml = msg;
            })
            // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
            this.controller.postMessage('__init_port__', [this.ports[0]], '*');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })

      // 4、使用应用侧的端口给另一个已经发送到html的端口发送消息。
      Button('SendDataToHTML')
        .onClick(() => {
          try {
            if (this.ports && this.ports[1]) {
              this.ports[1].postMessageEvent(this.sendFromEts);
            } else {
              console.error(`ports is null, Please initialize first`);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
```

加载的html文件。

```ets
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebView Message Port Demo</title>
</head>

  <body>
    <h1>WebView Message Port Demo</h1>
    <div>
        <input type="button" value="SendToEts" onclick="PostMsgToEts(msgFromJS.value);"/><br/>
        <input id="msgFromJS" type="text" value="send this message from HTML to ets"/><br/>
    </div>
    <p class="output">display received message send from ets</p>
  </body>
  <script src="xxx.js"></script>
</html>
```

```ets
//xxx.js
var h5Port;
var output = document.querySelector('.output');
window.addEventListener('message', function (event) {
    if (event.data == '__init_port__') {
        if (event.ports[0] != null) {
            h5Port = event.ports[0]; // 1. 保存从ets侧发送过来的端口
            h5Port.onmessage = function (event) {
              // 2. 接收ets侧发送过来的消息.
              var msg = 'Got message from ets:';
              var result = event.data;
              if (typeof(result) == "string") {
                console.info("received string message from html5, string is:" + result);
                msg = msg + result;
              } else if (typeof(result) == "object") {
                if (result instanceof ArrayBuffer) {
                  console.info("received arraybuffer from html5, length is:" + result.byteLength);
                  msg = msg + "length is " + result.byteLength;
                } else {
                  console.info("not support");
                }
              } else {
                console.info("not support");
              }
              output.innerHTML = msg;
            }
})

// 3. 使用h5Port往ets侧发送消息.
function PostMsgToEts(data) {
    if (h5Port) {
      h5Port.postMessage(data);
    } else {
      console.error("h5Port is null, Please initialize first");
    }
```

#### requestFocus

requestFocus(): void

使当前web页面获取焦点。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('requestFocus')
        .onClick(() => {
          try {
            this.controller.requestFocus();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### zoomIn

zoomIn(): void

调用此接口将当前网页进行放大，比例为25%。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('zoomIn')
        .onClick(() => {
          try {
            this.controller.zoomIn();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### zoomOut

zoomOut(): void

调用此接口将当前网页进行缩小，比例为20%。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('zoomOut')
        .onClick(() => {
          try {
            this.controller.zoomOut();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getWebId

getWebId(): number

获取当前Web组件的索引值，用于多个Web组件的管理。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前Web组件的索引值。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getWebId')
        .onClick(() => {
          try {
            let id = this.controller.getWebId();
            console.info("id: " + id);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getUserAgent

getUserAgent(): string

获取当前默认用户代理。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../guides/User-Agent开发指导.md)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 默认用户代理。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getUserAgent')
        .onClick(() => {
          try {
            let userAgent = this.controller.getUserAgent();
            console.info("userAgent: " + userAgent);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
}
```

支持开发者基于默认的User-Agent去定制User-Agent。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State ua: string = "";

  aboutToAppear(): void {
    webview.once('webInited', () => {
      try {
        // 应用侧用法示例，定制User-Agent。
        this.ua = this.controller.getUserAgent() + 'xxx';
        this.controller.setCustomUserAgent(this.ua);
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
      }
    })
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getTitle

getTitle(): string

获取当前网页的标题。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前网页的标题。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例:**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getTitle')
        .onClick(() => {
          try {
            let title = this.controller.getTitle();
            console.info("title: " + title);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getPageHeight

getPageHeight(): number

获取当前网页的页面高度。具体使用详情请参考[获取网页内容高度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-getpage-height)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前网页的页面高度。单位：vp。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例:**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getPageHeight')
        .onClick(() => {
          try {
            let pageHeight = this.controller.getPageHeight();
            console.info("pageHeight : " + pageHeight);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### storeWebArchive

storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void

以回调方式异步保存当前页面。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseName | string | 是 | 生成的离线网页存储位置，该值不能为空。 |
| autoName | boolean | 是 | 决定是否自动生成文件名。 false表示按baseName的文件名存储，true表示根据当前Url自动生成文件名，并按baseName的文件目录存储。 |
callbackAsyncCallback<string>是返回文件存储路径，保存网页失败会返回null。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100003 | Invalid resource path or file type. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('storeWebArchive')
        .onClick(() => {
          try {
            this.controller.storeWebArchive("/data/storage/el2/base/", true, (error, filename) => {
              if (error) {
                console.error(`save web archive error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              if (filename != null) {
                console.info(`save web archive success: ${filename}`);
              }
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### storeWebArchive

storeWebArchive(baseName: string, autoName: boolean): Promise<string>

以Promise方式异步保存当前页面。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseName | string | 是 | 生成的离线网页存储位置，该值不能为空。 |
| autoName | boolean | 是 | 决定是否自动生成文件名。 false表示按baseName的文件名存储，true表示根据当前Url自动生成文件名，并按baseName的文件目录存储。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise实例，保存成功返回文件路径，保存失败返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100003 | Invalid resource path or file type. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('storeWebArchive')
        .onClick(() => {
          try {
            this.controller.storeWebArchive("/data/storage/el2/base/", true)
              .then(filename => {
                if (filename != null) {
                  console.info(`save web archive success: ${filename}`)
                }
              })
              .catch((error: BusinessError) => {
                console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getUrl

getUrl(): string

获取当前页面的url地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前页面的url地址。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getUrl')
        .onClick(() => {
          try {
            let url = this.controller.getUrl();
            console.info("url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### stop

stop(): void

停止页面加载。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('stop')
        .onClick(() => {
          try {
            this.controller.stop();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### backOrForward

backOrForward(step: number): void

按照历史栈，前进或者后退指定步长的页面，当历史栈中不存在对应步长的页面时，不会进行页面跳转。

前进或者后退页面时，直接使用已加载过的网页，无需重新加载网页。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | number | 是 | 需要前进或后退的步长。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State step: number = -2;

  build() {
    Column() {
      Button('backOrForward')
        .onClick(() => {
          try {
            this.controller.backOrForward(this.step);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### scrollTo

scrollTo(x:number, y:number, duration?:number): void

在指定时间内，将页面滚动到指定的绝对位置。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 绝对位置的水平坐标，当传入数值为负数时，按照传入0处理。 单位：vp。 |
| y | number | 是 | 绝对位置的垂直坐标，当传入数值为负数时，按照传入0处理。 单位：vp。 |
| duration14+ | number | 否 | 滚动动画时间。 单位：ms。 不传入为无动画，当传入数值为负数或传入0时，按照不传入处理。 传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('scrollTo')
        .onClick(() => {
          try {
            this.controller.scrollTo(50, 50, 500);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        Button('stopScroll')
        .onClick(() => {
          try {
            this.controller.scrollBy(0, 0, 1); //如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
```

加载的html文件。

```ets
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

#### scrollBy

scrollBy(deltaX:number, deltaY:number,duration?:number): void

在指定时间内将页面滚动指定的偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deltaX | number | 是 | 水平偏移量，其中水平向右为正方向。 单位：vp。 |
| deltaY | number | 是 | 垂直偏移量，其中垂直向下为正方向。 单位：vp。 |
| duration14+ | number | 否 | 滚动动画时间。 单位：ms。 不传入为无动画，当传入数值为负数或传入0时，按照不传入处理。 传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


嵌套滚动场景中，调用scrollBy不会触发父组件的嵌套滚动。

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('scrollBy')
        .onClick(() => {
          try {
            this.controller.scrollBy(50, 50, 500);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('stopScroll')
        .onClick(() => {
          try {
            this.controller.scrollBy(0, 0, 1); //如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
```

加载的html文件。

```ets
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

#### scrollByWithResult12+

scrollByWithResult(deltaX: number, deltaY: number): boolean

将页面滚动指定的偏移量，返回值表示此次滚动是否执行成功。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deltaX | number | 是 | 水平偏移量，其中水平向右为正方向。 单位：vp。 |
| deltaY | number | 是 | 垂直偏移量，其中垂直向下为正方向。 单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示当前网页可以滑动，false表示当前网页不可以滑动。 默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


- 返回值场景：Web页面处于触摸中状态时，返回false，否则返回true。
- 同层渲染场景中，Web的同层渲染区域处于触摸中状态时，返回值为true。
- 嵌套滚动场景中，调用scrollByWithResult不会触发父组件的嵌套滚动。
- 此接口不保证滑动帧率性能。

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('scrollByWithResult')
        .onClick(() => {
          try {
          let result = this.controller.scrollByWithResult(50, 50);
          console.info("original result: " + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
}
```

加载的html文件。

```ets
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

#### slideScroll

slideScroll(vx:number, vy:number): void

按照指定速度模拟对页面的轻扫滚动动作。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vx | number | 是 | 轻扫滚动的水平速度分量，其中水平向右为速度正方向。 单位：vp/ms。 |
| vy | number | 是 | 轻扫滚动的垂直速度分量，其中垂直向下为速度正方向。 单位：vp/ms。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('slideScroll')
        .onClick(() => {
          try {
            this.controller.slideScroll(500, 500);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
}
```

加载的html文件。

```ets
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:3000px;
            height:3000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

#### getOriginalUrl

getOriginalUrl(): string

获取当前页面的原始url地址。

风险提示：如果想获取url来做JavascriptProxy通信接口认证，请使用[getLastJavascriptProxyCallingFrameUrl12+](#ZH-CN_TOPIC_0000002553201117__getlastjavascriptproxycallingframeurl12)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前页面的原始url地址。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getOrgUrl')
        .onClick(() => {
          try {
            let url = this.controller.getOriginalUrl();
            console.info("original url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getFavicon

getFavicon(): image.PixelMap

获取页面的favicon图标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | 页面favicon图标的PixelMap对象。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State pixelmap: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Button('getFavicon')
        .onClick(() => {
          try {
            this.pixelmap = this.controller.getFavicon();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setNetworkAvailable

setNetworkAvailable(enable: boolean): void

设置JavaScript中的window.navigator.onLine属性。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置JavaScript中的window.navigator.onLine属性。 true表示设置JavaScript中的window.navigator.onLine属性为true，false表示设置JavaScript中的window.navigator.onLine属性为false。 默认值：true。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setNetworkAvailable')
        .onClick(() => {
          try {
            this.controller.setNetworkAvailable(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
}
```

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<h1>online 属性</h1>
<p id="demo"></p>
<button onclick="func()">click</button>
<script>
    // 检测浏览器是否在线。
    var online1 = navigator.onLine;
    document.getElementById("demo").innerHTML = "浏览器在线：" + online1;

    function func(){
      var online2 = navigator.onLine;
      document.getElementById("demo").innerHTML = "浏览器在线：" + online2;
    }
</script>
</body>
</html>
```

#### hasImage

hasImage(callback: AsyncCallback<boolean>): void

通过Callback方式异步查找当前页面是否存在图像。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 返回查找页面是否存在图像。 true表示页面存在图像；false表示页面不存在图像。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('hasImageCb')
        .onClick(() => {
          try {
            this.controller.hasImage((error, data) => {
              if (error) {
                console.error(`hasImage error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              console.info("hasImage: " + data);
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### hasImage

hasImage(): Promise<boolean>

通过Promise方式异步查找当前页面是否存在图像。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise实例，返回查找页面是否存在图像。 true表示页面存在图像；false表示页面不存在图像。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('hasImagePm')
        .onClick(() => {
          try {
            this.controller.hasImage().then((data) => {
              console.info('hasImage: ' + data);
            }).catch((error: BusinessError) => {
              console.error("error: " + error);
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### removeCache

removeCache(clearRom: boolean): void

清除应用中的资源缓存文件，此方法将会清除同一应用中所有Webview的缓存文件。

可以通过在data/storage/el2/base/cache/web/Cache目录下查看Webview的缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearRom | boolean | 是 | 设置为true时同时清除ROM和RAM中的缓存，设置为false时只清除RAM中的缓存。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('removeCache')
        .onClick(() => {
          try {
            this.controller.removeCache(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### removeAllCache18+

static removeAllCache(clearRom: boolean): void

清除应用中的资源缓存文件，此方法将会清除同一应用中所有Webview的缓存文件。

可以通过在data/app/el2/100/base/<applicationPackageName>/cache/web/目录下查看Webview的缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearRom | boolean | 是 | 设置为true时同时清除ROM和RAM中的缓存，设置为false时只清除RAM中的缓存。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('removeAllCache')
        .onClick(() => {
          try {
            webview.WebviewController.removeAllCache(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### pageUp

pageUp(top: boolean): void

将Webview的内容向上滚动半个视框大小或者跳转到页面最顶部，通过top入参控制。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| top | boolean | 是 | 是否跳转到页面最顶部。 false表示将页面内容向上滚动半个视框大小，true表示跳转到页面最顶部。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('pageUp')
        .onClick(() => {
          try {
            this.controller.pageUp(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile("index.html"), controller: this.controller })
}
```

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

#### pageDown

pageDown(bottom: boolean): void

将Webview的内容向下滚动半个视框大小或者跳转到页面最底部，通过bottom入参控制。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bottom | boolean | 是 | 是否跳转到页面最底部。 false时表示将页面内容向下滚动半个视框大小，true表示跳转到页面最底部。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('pageDown')
        .onClick(() => {
          try {
            this.controller.pageDown(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile("index.html"), controller: this.controller })
}
```

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

#### getBackForwardEntries

getBackForwardEntries(): BackForwardList

获取当前Webview的历史信息列表。


[onLoadIntercept](事件.md#ZH-CN_TOPIC_0000002522081170__onloadintercept10)在加载开始的时候触发，该时刻还未生成历史节点，所以在onLoadIntercept中调用getBackForwardEntries拿到的历史栈不包括当前正在加载中的跳转。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| BackForwardList | 当前Webview的历史信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getBackForwardEntries')
        .onClick(() => {
          try {
            let list = this.controller.getBackForwardEntries()
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### serializeWebState

serializeWebState(): Uint8Array

将当前Webview的页面状态历史记录信息序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 当前Webview的页面状态历史记录序列化后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

1.对文件的操作需要导入文件管理模块，详情请参考[文件管理](@ohos.file.fs (文件管理).md)。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('serializeWebState')
        .onClick(() => {
          try {
            let state = this.controller.serializeWebState();
            let path:string | undefined = AppStorage.get("cacheDir");
            if (path) {
              path += '/WebState';
              // 以同步方法打开文件。
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              fileIo.writeSync(file.fd, state.buffer);
              fileIo.closeSync(file.fd);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

2.修改EntryAbility.ets。

获取应用缓存文件路径。

```ets
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
        AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
    }
```

#### restoreWebState

restoreWebState(state: Uint8Array): void

当前Webview从序列化数据中恢复页面状态历史记录。

如果state过大，可能会导致异常。建议state大于512k时，放弃恢复页面状态历史记录。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | Uint8Array | 是 | 页面状态历史记录序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

1.对文件的操作需要导入文件管理模块，详情请参考[文件管理](@ohos.file.fs (文件管理).md)。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('RestoreWebState')
        .onClick(() => {
          try {
            let path: string | undefined = AppStorage.get("cacheDir");
            if (path) {
              path += '/WebState';
              // 以同步方法打开文件。
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE);
              let stat = fileIo.statSync(path);
              let size = stat.size;
              let buf = new ArrayBuffer(size);
              fileIo.read(file.fd, buf, (err, readLen) => {
                if (err) {
                  console.error("console error with error message: " + err.message + ", error code: " + err.code);
                } else {
                  console.info("read file data succeed");
                  this.controller.restoreWebState(new Uint8Array(buf.slice(0, readLen)));
                  fileIo.closeSync(file);
                }
              });
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

2.修改EntryAbility.ets。

获取应用缓存文件路径。

```ets
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
    AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
  }
```

#### customizeSchemes

static customizeSchemes(schemes: Array<WebCustomScheme>): void

对Web内核赋予自定义协议url的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议url时，该fetch请求可被[onInterceptRequest](事件.md#ZH-CN_TOPIC_0000002522081170__oninterceptrequest9)事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| schemes | Array<WebCustomScheme> | 是 | 自定义协议配置，最多支持同时配置10个自定义协议。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100020 | Failed to register custom schemes. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
  scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
  scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

  aboutToAppear(): void {
    try {
      webview.WebviewController.customizeSchemes([this.scheme1, this.scheme2, this.scheme3]);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onInterceptRequest((event) => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
          }
          return this.responseWeb;
        })
    }
```

#### customizeSchemes21+

static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void

对Web内核赋予自定义协议url的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议url时，该fetch请求可被[onInterceptRequest](事件.md#ZH-CN_TOPIC_0000002522081170__oninterceptrequest9)事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| schemes | Array<WebCustomScheme> | 是 | 自定义协议配置，最多支持同时配置10个自定义协议。 |
| lazyInitWebEngine | boolean | 是 | 表示接口内部是否跳过初始化WebEngine。 true表示接口内部跳过初始化WebEngine，并将注册的Schemes暂存，当它真正初始化时，这些Schemes将传递给WebEngine。false表示接口内部自动进行WebEngine初始化。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. The length of the schemes array is greater than 10. 2. The character length of the scheme is greater than 32. 3. The character in the scheme is not within the allowed range of lowercase English letters, numbers, and the symbols ".", "+", "-". |
| 17100020 | Failed to register custom schemes. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
  scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
  scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

  aboutToAppear(): void {
    try {
      webview.WebviewController.customizeSchemes([this.scheme1, this.scheme2, this.scheme3], true);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getCertificate10+

getCertificate(): Promise<Array<cert.X509Cert>>

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过Promise异步返回当前网站的X509格式证书（X509Cert证书类型定义见[X509Cert](@ohos.security.cert (证书模块).md#ZH-CN_TOPIC_0000002522081410__x509cert)定义），便于开发者展示网站证书信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<cert.X509Cert>> | Promise实例，用于获取当前加载的https网站的X509格式证书数组。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { cert } from '@kit.DeviceCertificateKit';

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray[i]);
  }
  return dataString;
}

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
  let res: string = 'getCertificate success: len = ' + x509CertArray.length;
  for (let i = 0; i < x509CertArray.length; i++) {
    res += ', index = ' + i + ', issuer name = '
      + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
      + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
      + x509CertArray[i].getNotBeforeTime()
      + ', valid end = ' + x509CertArray[i].getNotAfterTime();
  }
  return res;
}

@Entry
@Component
struct Index {
  // outputStr在UI界面显示调试信息
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          ListItem() {
            Button() {
              Text('load bad ssl')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // 加载一个过期的证书网站，查看获取到的证书信息
              this.webviewCtl.loadUrl('https://expired.badssl.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('load example')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // 加载一个https网站，查看网站的证书信息
              this.webviewCtl.loadUrl('https://www.example.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate Promise')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
                  this.outputStr = ParseX509CertInfo(x509CertArray);
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate AsyncCallback')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
                  if (error) {
                    this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
                  } else {
                    this.outputStr = ParseX509CertInfo(x509CertArray);
                  }
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }
        .listDirection(Axis.Horizontal)
        .height('10%')

        Text(this.outputStr)
          .width('100%')
          .fontSize(10)

        Web({ src: 'https://www.example.com', controller: this.webviewCtl })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .onPageEnd((e) => {
            if (e) {
              this.outputStr = 'onPageEnd : url = ' + e.url;
            }
          })
          .onSslErrorEventReceive((e) => {
            // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com
            e.handler.handleConfirm();
          })
          .width('100%')
          .height('70%')
      }
      .height('100%')
    }
```

#### getCertificate10+

getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过AsyncCallback异步返回当前网站的X509格式证书（X509Cert证书类型定义见[X509Cert定义](@ohos.security.cert (证书模块).md)），便于开发者展示网站证书信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<cert.X509Cert>> | 是 | 通过AsyncCallback异步返回当前网站的X509格式证书。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { cert } from '@kit.DeviceCertificateKit';

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray[i]);
  }
  return dataString;
}

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
  let res: string = 'getCertificate success: len = ' + x509CertArray.length;
  for (let i = 0; i < x509CertArray.length; i++) {
    res += ', index = ' + i + ', issuer name = '
      + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
      + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
      + x509CertArray[i].getNotBeforeTime()
      + ', valid end = ' + x509CertArray[i].getNotAfterTime();
  }
  return res;
}

@Entry
@Component
struct Index {
  // outputStr在UI界面显示调试信息
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          ListItem() {
            Button() {
              Text('load bad ssl')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // 加载一个过期的证书网站，查看获取到的证书信息
              this.webviewCtl.loadUrl('https://expired.badssl.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('load example')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // 加载一个https网站，查看网站的证书信息
              this.webviewCtl.loadUrl('https://www.example.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate Promise')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
                  this.outputStr = ParseX509CertInfo(x509CertArray);
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate AsyncCallback')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
                  if (error) {
                    this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
                  } else {
                    this.outputStr = ParseX509CertInfo(x509CertArray);
                  }
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }
        .listDirection(Axis.Horizontal)
        .height('10%')

        Text(this.outputStr)
          .width('100%')
          .fontSize(10)

        Web({ src: 'https://www.example.com', controller: this.webviewCtl })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .onPageEnd((e) => {
            if (e) {
              this.outputStr = 'onPageEnd : url = ' + e.url;
            }
          })
          .onSslErrorEventReceive((e) => {
            // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com
            e.handler.handleConfirm();
          })
          .width('100%')
          .height('70%')
      }
      .height('100%')
    }
```

#### setAudioMuted10+

setAudioMuted(mute: boolean): void

设置网页静音。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 表示是否将网页设置为静音状态。 true表示将网页设置为静音状态，false表示将网页取消静音状态。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State muted: boolean = false;

  build() {
    Column() {
      Button("Toggle Mute")
        .onClick(event => {
          if (event) {
            this.muted = !this.muted;
            this.controller.setAudioMuted(this.muted);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### prefetchPage21+

prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void

在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度。

-

下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。

-

prefetchPage对302重定向页面同样正常预取。

-

先执行prefetchPage再加载页面时，已预取的资源将直接从缓存中加载。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 预加载的url。 |
| additionalHeaders | Array<WebHeader> | 否 | url的附加HTTP请求头。 默认值： [] |
| prefetchOptions | PrefetchOptions | 否 | 用来自定义预取行为的相关选项。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
            let options = new webview.PrefetchOptions();
            options.ignoreCacheControlNoStore = true;
            options.minTimeBetweenPrefetchesMs = 100;
            this.controller.prefetchPage('https://www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }], options);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // 需要将'www.example1.com'替换成一个真实的网站地址。
      Web({ src: 'www.example1.com', controller: this.controller })
    }
```

#### prefetchPage10+

prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void

在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度。

-

下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。

-

prefetchPage对302重定向页面同样正常预取。

-

先执行prefetchPage再加载页面时，已预取的资源将直接从缓存中加载。

-

连续prefetchPage多个url只有第一个生效。

-

prefetchPage有时间限制，500ms内不能多次预取。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 预加载的url。 |
| additionalHeaders | Array<WebHeader> | 否 | url的附加HTTP请求头。 默认值： [] |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
            this.controller.prefetchPage('https://www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // 需要将'www.example1.com'替换成一个真实的网站地址。
      Web({ src: 'www.example1.com', controller: this.controller })
    }
```

#### prefetchResource12+

static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void

根据指定的请求信息和附加的http请求头去预获取资源请求，存入内存缓存，并指定其缓存key和有效期，以加快加载速度。目前仅支持Content-Type为application/x-www-form-urlencoded的post请求。最多可以预获取6个post请求。如果要预获取第7个，请通过[clearPrefetchedResource](#ZH-CN_TOPIC_0000002553201117__clearprefetchedresource12)清除不需要的post请求缓存，否则会自动清除最早预获取的post缓存。如果要使用预获取的资源缓存，开发者需要在正式发起的post请求的请求头中增加键值“ArkWebPostCacheKey”，其内容为对应缓存的cacheKey。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | RequestInfo | 是 | 预获取请求的信息。 |
| additionalHeaders | Array<WebHeader> | 否 | 预获取请求的附加HTTP请求头。 传入undefined或null会抛出异常错误码401。 |
| cacheKey | string | 否 | 用于后续查询预获取资源缓存的key。仅支持字母和数字，未传入或传入空则取默认值url作为key。 传入undefined或null会抛出异常错误码401。 |
| cacheValidTime | number | 否 | 预获取资源缓存的有效期。 取值范围：(0, 2147483647]。 默认值：300秒。 单位：秒。 传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**示例：**

```ets
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
    webview.WebviewController.prefetchResource(
      {
        url: "https://www.example1.com/post?e=f&g=h",
        method: "POST",
        formData: "a=x&b=y",
      },
      [{
        headerKey: "c",
        headerValue: "z",
      },],
      "KeyX", 500);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
```

#### clearPrefetchedResource12+

static clearPrefetchedResource(cacheKeyList: Array<string>): void

根据指定的缓存key列表清除对应的预获取资源缓存。入参中的缓存key必须是[prefetchResource](#ZH-CN_TOPIC_0000002553201117__prefetchresource12)指定预获取到的资源缓存key。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cacheKeyList | Array<string> | 是 | 用于后续查询预获取资源缓存的key。仅支持字母和数字，未传入或传入空则取默认值url作为key。 |

**示例：**

```ets
// Index.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: "https://www.example.com/", controller: this.controller })
        .onAppear(() => {
          // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
          webview.WebviewController.prefetchResource(
            {
              url: "https://www.example1.com/post?e=f&g=h",
              method: "POST",
              formData: "a=x&b=y",
            },
            [{
              headerKey: "c",
              headerValue: "z",
            },],
            "KeyX", 500);
        })
        .onPageEnd(() => {
          // 清除后续不再使用的预获取缓存。
          webview.WebviewController.clearPrefetchedResource(["KeyX",]);
        })
    }
```

#### prepareForPageLoad10+

static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void

预连接url，在加载url之前调用此API，对url只进行DNS解析，socket建链操作，并不获取主资源子资源。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 预连接的url。 |
| preconnectable | boolean | 是 | 是否进行预连接。如果preconnectable为true，则对url进行DNS解析，socket建链预连接；如果preconnectable为false，则不做任何预连接操作。 |
| numSockets | number | 是 | 要预连接的socket数。socket数目连接需要大于0，最多允许6个连接。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |
| 17100013 | The number of preconnect sockets is invalid. |

**示例：**

```ets
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 预连接时，需要將'https://www.example.com'替换成一个真实的网站地址。
    webview.WebviewController.prepareForPageLoad("https://www.example.com", true, 2);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
```

#### setCustomUserAgent10+

setCustomUserAgent(userAgent: string): void

设置自定义用户代理，会覆盖系统的用户代理。

当Web组件src设置了url时，建议在onControllerAttached回调事件中设置User-Agent，设置方式请参考示例。不建议将User-Agent设置在[onLoadIntercept](../../topics/misc/事件.md#ZH-CN_TOPIC_0000002497445228__onloadintercept10)回调事件中，会概率性出现设置失败。

当Web组件src设置为空字符串时，建议先调用setCustomUserAgent方法设置User-Agent，再通过loadUrl加载具体页面。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../guides/User-Agent开发指导.md)

当Web组件src设置了url，且未在onControllerAttached回调事件中设置User-Agent。再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 用户自定义代理信息。建议先使用getUserAgent获取当前默认用户代理，在此基础上追加自定义用户代理信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State customUserAgent: string = ' DemoApp';

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .onControllerAttached(() => {
        console.info("onControllerAttached");
        try {
          let userAgent = this.controller.getUserAgent() + this.customUserAgent;
          this.controller.setCustomUserAgent(userAgent);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
```

#### setDownloadDelegate11+

setDownloadDelegate(delegate: WebDownloadDelegate): void

为当前的Web组件设置一个WebDownloadDelegate，该delegate用来接收页面内触发的下载进度的委托。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | WebDownloadDelegate | 是 | 用来接收下载进度的委托。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### startDownload11+

startDownload(url: string): void

使用Web组件的下载能力来下载指定的url, 比如下载网页中指定的图片。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 下载地址。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('startDownload')
        .onClick(() => {
          try {
            this.controller.startDownload('https://www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getCustomUserAgent10+

getCustomUserAgent(): string

获取自定义用户代理。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../guides/User-Agent开发指导.md)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用户自定义代理信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State userAgent: string = '';

  build() {
    Column() {
      Button('getCustomUserAgent')
        .onClick(() => {
          try {
            this.userAgent = this.controller.getCustomUserAgent();
            console.info("userAgent: " + this.userAgent);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setAppCustomUserAgent20+

static setAppCustomUserAgent(userAgent: string): void

设置应用级自定义用户代理，会覆盖系统的用户代理，应用内所有Web组件生效。

当需要设置应用级自定义用户代理时，建议在Web组件创建前调用setAppCustomUserAgent方法设置User-Agent，再创建指定src的Web组件或通过[loadUrl](#ZH-CN_TOPIC_0000002553201117__loadurl)加载具体页面。

默认User-Agent定义与使用场景，及相关User-Agent接口定义优先级请参考[User-Agent开发指导](../../guides/User-Agent开发指导.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 用户自定义代理信息。建议先使用getDefaultUserAgent获取当前默认用户代理，在此基础上追加自定义用户代理信息。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.initializeWebEngine();
      let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
      let appUA = defaultUserAgent + " appUA";
      webview.WebviewController.setAppCustomUserAgent(appUA);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setUserAgentForHosts20+

static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void

针对特定网站设置自定义用户代理，会覆盖系统的用户代理，应用内所有Web组件生效。

当需要对特定网站设置自定义用户代理时，建议在Web组件创建前调用setUserAgentForHosts方法设置User-Agent，再创建指定src的Web组件或通过[loadUrl](#ZH-CN_TOPIC_0000002553201117__loadurl)加载具体页面。

默认User-Agent定义与使用场景，及相关User-Agent接口定义优先级请参考[User-Agent开发指导](../../guides/User-Agent开发指导.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 用户自定义代理信息。建议先使用getDefaultUserAgent获取当前默认用户代理，在此基础上追加自定义用户代理信息。 |
| hosts | Array<string> | 是 | 用户自定义代理的相关域名列表，每次调用时仅保留最新传入的列表，并限制最大条目数为两万，超出部分自动截断。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.initializeWebEngine();
      let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
      let appUA = defaultUserAgent + " appUA";
      webview.WebviewController.setUserAgentForHosts(
        appUA,
        [
          "www.example.com",
          "www.baidu.com"
        ]
      );
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setConnectionTimeout11+

static setConnectionTimeout(timeout: number): void

设置网络连接超时时间，使用者可通过Web组件中的onErrorReceive方法获取超时错误码。若未调用该接口则默认超时时间为30秒。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | socket连接超时时间，以秒为单位，必须为大于0的整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setConnectionTimeout')
        .onClick(() => {
          try {
            webview.WebviewController.setConnectionTimeout(5);
            console.info("setConnectionTimeout: 5s");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onErrorReceive((event) => {
          if (event) {
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
          }
        })
    }
```

#### warmupServiceWorker12+

static warmupServiceWorker(url: string): void

预热ServiceWorker，以提升首屏页面的加载速度（仅限于会使用ServiceWorker的页面）。在加载url之前调用此API。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 需要预热ServiceWorker的url。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**示例：**

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        console.info("EntryAbility onCreate");
        webview.WebviewController.initializeWebEngine();
        webview.WebviewController.warmupServiceWorker("https://www.example.com");
        AppStorage.setOrCreate("abilityWant", want);
    }
```

#### enableSafeBrowsing11+

enableSafeBrowsing(enable: boolean): void

启用检查网站安全风险的功能，非法和欺诈网站是强制启用的，不能通过此功能禁用。

本功能默认不生效，HarmonyOS只提供恶意网址拦截页WebUI，网址风险检测以及显示WebUI的功能由Vendor实现。推荐在WebContentsObserver中监听跳转[DidStartNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h)、[DidRedirectNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h)进行检测。


该接口不生效，调用不会产生任何实际效果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用检查网站安全风险的功能。 true表示启用检查网站安全风险的功能，false表示不启用检查网站安全风险的功能。 默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('enableSafeBrowsing')
        .onClick(() => {
          try {
            this.controller.enableSafeBrowsing(true);
            console.info("enableSafeBrowsing: true");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### isSafeBrowsingEnabled11+

isSafeBrowsingEnabled(): boolean

获取当前网页是否启用了检查网站安全风险。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前网页是否启用了检查网站安全风险的功能。 true表示启用了检查网站安全风险的功能，false表示未启用检查网站安全风险的功能。 默认值：false。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isSafeBrowsingEnabled')
        .onClick(() => {
          let result = this.controller.isSafeBrowsingEnabled();
          console.info("result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### enableIntelligentTrackingPrevention12+

enableIntelligentTrackingPrevention(enable: boolean): void

启用智能防跟踪功能。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用智能防跟踪功能。 true表示启用智能防跟踪功能，false表示不启用智能防跟踪功能。 默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('enableIntelligentTrackingPrevention')
        .onClick(() => {
          try {
            this.controller.enableIntelligentTrackingPrevention(true);
            console.info("enableIntelligentTrackingPrevention: true");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### isIntelligentTrackingPreventionEnabled12+

isIntelligentTrackingPreventionEnabled(): boolean

获取当前Web是否启用了智能防跟踪功能。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前Web是否启用了智能防跟踪功能。 true表示启用了智能防跟踪功能，false表示未启用智能防跟踪功能。 默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isIntelligentTrackingPreventionEnabled')
        .onClick(() => {
          try {
            let result = this.controller.isIntelligentTrackingPreventionEnabled();
            console.info("result: " + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### addIntelligentTrackingPreventionBypassingList12+

static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void

添加智能防跟踪功能绕过的域名列表。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostList | Array<string> | 是 | 绕过智能防跟踪功能的域名列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('addIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = ["www.test1.com", "www.test2.com", "www.test3.com"];
            webview.WebviewController.addIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### removeIntelligentTrackingPreventionBypassingList12+

static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void

删除通过addIntelligentTrackingPreventionBypassingList接口添加的部分域名列表。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostList | Array<string> | 是 | 绕过智能防跟踪功能的域名列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('removeIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = ["www.test1.com", "www.test2.com"];
            webview.WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### clearIntelligentTrackingPreventionBypassingList12+

static clearIntelligentTrackingPreventionBypassingList(): void

删除通过addIntelligentTrackingPreventionBypassingList接口添加的所有域名。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          webview.WebviewController.clearIntelligentTrackingPreventionBypassingList();
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getDefaultUserAgent14+

static getDefaultUserAgent(): string

获取默认用户代理。

此接口只允许在UI线程调用。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../guides/User-Agent开发指导.md)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | ArkWeb默认User-Agent字符串。 |

**示例：**

```ets
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
    console.info("defaultUserAgent: " + defaultUserAgent);
  }
```

#### enableAdsBlock12+

enableAdsBlock(enable: boolean): void

启用广告过滤功能。

- 广告过滤功能需要release包，使用debug包不生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用广告过滤功能。 true表示启用广告过滤功能，false表示取消广告过滤功能。 默认值：false。 |

**错误码：**


从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('enableAdsBlock')
        .onClick(() => {
          try {
            this.controller.enableAdsBlock(true);
            console.info("enableAdsBlock: true")
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### isAdsBlockEnabled12+

isAdsBlockEnabled() : boolean

查询广告过滤功能是否开启。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true代表广告过滤功能已开启，返回false代表广告过滤功能关闭。 默认值：false。 |

**错误码：**


从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isAdsBlockEnabled')
        .onClick(() => {
          try {
            let isAdsBlockEnabled: boolean = this.controller.isAdsBlockEnabled();
            console.info("isAdsBlockEnabled:", isAdsBlockEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### isAdsBlockEnabledForCurPage12+

isAdsBlockEnabledForCurPage() : boolean

查询当前网页是否开启广告过滤功能。

当Web组件使能广告过滤功能后，默认所有页面都是开启广告过滤的，支持通过[addAdsBlockDisallowedList](Class (AdsBlockManager).md#ZH-CN_TOPIC_0000002553201111__addadsblockdisallowedlist12)指定域名禁用广告过滤。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true代表此网页已开启广告过滤，返回false代表当前网页已关闭广告过滤。 |

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isAdsBlockEnabledForCurPage')
        .onClick(() => {
          try {
            let isAdsBlockEnabledForCurPage: boolean = this.controller.isAdsBlockEnabledForCurPage();
            console.info("isAdsBlockEnabledForCurPage:", isAdsBlockEnabledForCurPage);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### set[RenderProcessMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__renderprocessmode12)12+

static set[RenderProcessMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__renderprocessmode12)(mode: RenderProcessMode): void

设置ArkWeb渲染子进程模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [RenderProcessMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__renderprocessmode12) | 是 | 渲染子进程模式。 可以先调用getRenderProcessMode()查看当前设备的ArkWeb渲染子进程模式，枚举值0为单子进程模式，枚举值1为多子进程模式。 手机默认为单渲染子进程模式，平板和PC/2in1默认为多渲染子进程模式。 如果传入RenderProcessMode枚举值之外的非法数字，则默认识别为多渲染子进程模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setRenderProcessMode')
        .onClick(() => {
          try {
            webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### get[RenderProcessMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__renderprocessmode12)12+

static get[RenderProcessMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__renderprocessmode12)(): RenderProcessMode

查询ArkWeb的渲染子进程模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderProcessMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__renderprocessmode12) | 渲染子进程模式类型。 调用getRenderProcessMode()获取当前设备的ArkWeb渲染子进程模式，枚举值0为单子进程模式，枚举值1为多子进程模式。 如果获取的值不在RenderProcessMode枚举值范围内，则默认为多渲染子进程模式。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getRenderProcessMode')
        .onClick(() => {
          let mode = webview.WebviewController.getRenderProcessMode();
          console.info("getRenderProcessMode: " + mode);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### terminateRenderProcess12+

terminateRenderProcess(): boolean

销毁渲染进程。

调用该接口将会主动销毁相关联的渲染进程。如果渲染进程尚未启动，或者已销毁则没有任何影响。此外销毁渲染进程会同时影响所有与该渲染进程关联的其他实例。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回销毁渲染进程的结果。 返回true表示渲染进程可以被销毁或已被销毁，返回false表示渲染进程不可以被销毁。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('terminateRenderProcess')
        .onClick(() => {
          let result = this.controller.terminateRenderProcess();
          console.info("terminateRenderProcess result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### postUrl11+

postUrl(url: string, postData: ArrayBuffer): void

使用"POST"方法加载带有postData的url。如果url不是网络url，则会使用[loadUrl](#ZH-CN_TOPIC_0000002553201117__loadurl)方法加载url，忽略postData参数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 需要加载的 URL。 |
| postData | ArrayBuffer | 是 | 使用"POST"方法传递数据。 该请求必须采用"application/x-www-form-urlencoded"编码。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(str: string): ArrayBuffer {
    let buf = new ArrayBuffer(str.length);
    let buff = new Uint8Array(buf);

    for (let i = 0; i < str.length; i++) {
      buff[i] = str.charCodeAt(i);
    }
    return buf;
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();

  build() {
    Column() {
      Button('postUrl')
        .onClick(() => {
          try {
            // 数据转化为ArrayBuffer类型。
            let postData = this.testObjtest.test("Name=test&Password=test");
            this.controller.postUrl('www.example.com', postData);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: '', controller: this.controller })
    }
```

#### createWebPrintDocumentAdapter11+

createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter

创建web相关打印功能。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobName | string | 是 | 需要打印的文件名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| print.PrintDocumentAdapter | 返回打印文档的适配器。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError, print } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('createWebPrintDocumentAdapter')
        .onClick(() => {
          try {
            let webPrintDocadapter = this.controller.createWebPrintDocumentAdapter('example.pdf');
            print.print('example_jobid', webPrintDocadapter, null, this.getUIContext().getHostContext());
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### isIncognitoMode11+

isIncognitoMode(): boolean

查询当前是否是隐私模式的Webview。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否是隐私模式的Webview。 true表示是隐私模式，false表示不是隐私模式。 默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isIncognitoMode')
        .onClick(() => {
          try {
            let result = this.controller.isIncognitoMode();
            console.info('isIncognitoMode' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### get[SecurityLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__securitylevel11)11+

get[SecurityLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__securitylevel11)(): SecurityLevel

获取当前网页的安全级别。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SecurityLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__securitylevel11) | 当前网页的安全级别，具体值为NONE、SECURE、WARNING、DANGEROUS。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageEnd((event) => {
          if (event) {
            let securityLevel = this.controller.getSecurityLevel();
            console.info('securityLevel: ', securityLevel);
          }
        })
    }
```

#### setScrollable12+

setScrollable(enable: boolean, type?: [ScrollType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__scrolltype12)): void

设置网页是否允许滚动。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否将网页设置为允许滚动。 true表示设置为允许滚动，false表示禁止滚动。 默认值：true。 |
| type | [ScrollType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__scrolltype12) | 否 | 网页可触发的滚动类型，支持缺省配置。 - enable为false时，表示禁止ScrollType类型的滚动，当ScrollType缺省时表示禁止所有类型网页滚动。 - enable为true时，ScrollType缺省与否，都表示允许所有类型的网页滚动。 传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setScrollable')
        .onClick(() => {
          try {
            this.controller.setScrollable(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getScrollable12+

getScrollable(): boolean

获取当前网页是否允许滚动。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前网页是否允许滚动。 true为允许滚动，false为禁止滚动。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getScrollable')
        .onClick(() => {
          try {
            let scrollEnabled = this.controller.getScrollable();
            console.info("scrollEnabled: " + scrollEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setPrintBackground12+

setPrintBackground(enable: boolean): void

设置是否打印网页背景，该接口与[PrintAttributes](@ohos.print (打印).md#ZH-CN_TOPIC_0000002522081596__printattributes11)打印参数配置不一致时，本接口设置优先级高于打印参数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否打印网页背景。 true表示设置为打印网页背景，false表示取消网页背景打印。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setPrintBackground')
        .onClick(() => {
          try {
            this.controller.setPrintBackground(false);
          } catch (error) {
            console.error(`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getPrintBackground12+

getPrintBackground(): boolean

查询webview是否打印网页背景。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Webview是否打印网页背景。 true:打印网页背景；false:不打印网页背景。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setPrintBackground')
        .onClick(() => {
          try {
            let enable = this.controller.getPrintBackground();
            console.info("getPrintBackground: " + enable);
          } catch (error) {
            console.error(`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getLastJavascriptProxyCallingFrameUrl12+

getLastJavascriptProxyCallingFrameUrl(): string

通过[registerJavaScriptProxy](#ZH-CN_TOPIC_0000002553201117__registerjavascriptproxy)或者[javaScriptProxy](属性.md#ZH-CN_TOPIC_0000002553201131__javascriptproxy)注入JavaScript对象到window对象中。该接口可以获取最后一次调用注入的对象的frame的url。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 最后一次调用注入的对象的frame的url。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  mycontroller: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.mycontroller = controller;
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testStr;
  }

  toString(): void {
    console.info('Web Component toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
  }

  testNumber(testNum: number): number {
    console.info('Web Component number' + testNum + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testNum;
  }

  testBool(testBol: boolean): boolean {
    console.info('Web Component boolean' + testBol + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testBol;
  }

class WebObj {
  mycontroller: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.mycontroller = controller;
  }

  webTest(): string {
    console.info('Web test ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
}

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj(this.controller);
  @State webTestObj: WebObj = new WebObj(this.controller);

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber", "testBool"]);
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
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
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "ArkUI Web Component"
          let str=objName.test("webtest data");
          objName.testNumber(1);
          objName.testBool(true);
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)

          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)
        }
      </script>
    </body>
</html>
```

#### pauseAllTimers12+

static pauseAllTimers(): void

暂停所有WebView的定时器。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button('PauseAllTimers')
          .onClick(() => {
            webview.WebviewController.pauseAllTimers();
          })
      }
      Web({ src: $rawfile("index.html"), controller: this.controller })
}
```

加载的html文件。

```ets
<!DOCTYPE html>
<html>
    <body>
        <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
        <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
        <input style="width:300px;height:150px;font-size:50px" value="0" id="show_num">
    </body>
</html>
<script>
    var timer = null;
    var num = 0;

    function startTimer() {
        timer = setInterval(function() {
            document.getElementById("show_num").value = ++num;
        }, 1000);
    }

    function resetTimer() {
        clearInterval(timer);
        document.getElementById("show_num").value = 0;
        num = 0;
    }
</script>
```

#### resumeAllTimers12+

static resumeAllTimers(): void

恢复从pauseAllTimers()接口中被暂停的所有的定时器。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button('ResumeAllTimers')
          .onClick(() => {
            webview.WebviewController.resumeAllTimers();
          })
        Button('PauseAllTimers')
          .onClick(() => {
            webview.WebviewController.pauseAllTimers();
          })
      }
      Web({ src: $rawfile("index.html"), controller: this.controller })
}
```

加载的html文件。

```ets
<!DOCTYPE html>
<html>
    <body>
        <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
        <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
        <input style="width:300px;height:150px;font-size:50px" value="0" id="show_num">
    </body>
</html>
<script>
    var timer = null;
    var num = 0;

    function startTimer() {
        timer = setInterval(function() {
            document.getElementById("show_num").value = ++num;
        }, 1000);
    }

    function resetTimer() {
        clearInterval(timer);
        document.getElementById("show_num").value = 0;
        num = 0;
    }
</script>
```

#### stopAllMedia12+

stopAllMedia(): void

控制网页所有音视频停止。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('stopAllMedia')
        .onClick(() => {
          try {
            this.controller.stopAllMedia();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### pauseAllMedia12+

pauseAllMedia(): void

控制网页所有音视频暂停。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('pauseAllMedia')
        .onClick(() => {
          try {
            this.controller.pauseAllMedia();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### resumeAllMedia12+

resumeAllMedia(): void

控制网页被pauseAllMedia接口暂停的音视频继续播放。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('resumeAllMedia')
        .onClick(() => {
          try {
            this.controller.resumeAllMedia();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### closeAllMediaPresentations12+

closeAllMediaPresentations(): void

控制网页所有全屏视频关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('closeAllMediaPresentations')
        .onClick(() => {
          try {
            this.controller.closeAllMediaPresentations();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### get[MediaPlaybackState](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__mediaplaybackstate12)12+

get[MediaPlaybackState](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__mediaplaybackstate12)(): MediaPlaybackState

查询当前网页音视频播放状态。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaPlaybackState](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__mediaplaybackstate12) | 当前网页的播放状态，具体值为NONE、PLAYING、PAUSED、STOPPED。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getMediaPlaybackState')
        .onClick(() => {
          try {
            console.info("MediaPlaybackState : " + this.controller.getMediaPlaybackState());
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setWebSchemeHandler12+

setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void

为当前Web组件设置[WebSchemeHandler](Class (WebSchemeHandler).md), [WebSchemeHandler](Class (WebSchemeHandler).md)类用于拦截指定scheme的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 是 | 要拦截的协议。 |
| handler | WebSchemeHandler | 是 | 拦截此协议的拦截器。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('setWebSchemeHandler')
        .onClick(() => {
          try {
            this.controller.setWebSchemeHandler('http', this.schemeHandler);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### clearWebSchemeHandler12+

clearWebSchemeHandler(): void

清除当前Web组件设置的所有WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearWebSchemeHandler')
        .onClick(() => {
          try {
            this.controller.clearWebSchemeHandler();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setServiceWorkerWebSchemeHandler12+

setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void

为当前应用的所有Web组件设置用于拦截ServiceWorker的WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 是 | 要拦截的协议。 |
| handler | WebSchemeHandler | 是 | 拦截此协议的拦截器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('setWebSchemeHandler')
        .onClick(() => {
          try {
            webview.WebviewController.setServiceWorkerWebSchemeHandler('http', this.schemeHandler);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### clearServiceWorkerWebSchemeHandler12+

clearServiceWorkerWebSchemeHandler(): void

清除应用中设置的所有用于拦截ServiceWorker的WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearServiceWorkerWebSchemeHandler')
        .onClick(() => {
          webview.WebviewController.clearServiceWorkerWebSchemeHandler();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### startCamera12+

startCamera(): void

开启当前网页摄像头捕获。使用摄像头功能前请在module.json5中添加权限: ohos.permission.CAMERA，具体权限的添加方法请参考[在配置文件中声明权限](../../guides/声明权限.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err: BusinessError, data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
  }

  build() {
    Column() {
      Button("startCamera").onClick(() => {
        try {
          this.controller.startCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("stopCamera").onClick(() => {
        try {
          this.controller.stopCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("closeCamera").onClick(() => {
        try {
          this.controller.closeCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
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
    <meta charset="UTF-8">
  </head>
  <body>
    <video id="video" width="400px" height="400px" autoplay>
    </video>
    <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()" />
    <script>
      function getMedia() {
        let constraints = {
          video: {
            width: 500,
            height: 500
          },
          audio: true
        }
        let video = document.getElementById("video");
        let promise = navigator.mediaDevices.getUserMedia(constraints);
        promise.then(function(mediaStream) {
          video.srcObject = mediaStream;
          video.play();
        })
      }
    </script>
  </body>
</html>
```

#### stopCamera12+

stopCamera(): void

停止当前网页摄像头捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

完整示例代码参考[startCamera](#ZH-CN_TOPIC_0000002553201117__startcamera12)。

#### closeCamera12+

closeCamera(): void

关闭当前网页摄像头捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

完整示例代码参考[startCamera](#ZH-CN_TOPIC_0000002553201117__startcamera12)。

#### precompileJavaScript12+

precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>

预编译JavaScript生成字节码缓存或根据提供的参数更新已有的字节码缓存。

接口通过提供的文件信息、E-Tag响应头和Last-Modified响应头判断是否需要更新已有的字节码缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 本地JavaScript文件对应的网络地址，即业务网页请求该文件的服务器版本时使用的网络地址。网络地址仅支持http或https协议，长度不超过2048。如果该网络地址对应的缓存失效，则业务网页将通过网络请求对应的资源。 |
| script | string | Uint8Array | 是 | 本地JavaScript的文本内容。内容不能为空。 |
| cacheOptions | CacheOptions | 是 | 用于控制字节码缓存更新。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 生成字节码缓存的错误码，0表示无错误，-1表示内部错误。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter.Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

接口推荐配合动态组件使用，使用离线的Web组件用于生成字节码缓存，并在适当的时机加载业务用Web组件使用这些字节码缓存。下方是代码示例：

1.

首先，在EntryAbility中将UIContext存到localStorage中。
```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

const localStorage: LocalStorage = new LocalStorage('uiContext');

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', this.storage, (err, data) => {
      if (err.code) {
        return;
      }

      this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
    });
}
```

1.

编写动态组件所需基础代码。
```ets
// DynamicComponent.ets
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

export interface BuilderData {
  url: string;
  controller: WebviewController;
  context: UIContext;
}

let storage : LocalStorage | undefined = undefined;

export class NodeControllerImpl extends NodeController {
  private rootNode: BuilderNode<BuilderData[]> | null = null;
  private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

  constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
    storage = context.getSharedLocalStorage();
    super();
    this.wrappedBuilder = wrappedBuilder;
  }

  makeNode(): FrameNode | null {
    if (this.rootNode != null) {
      return this.rootNode.getFrameNode();
    }
    return null;
  }

  initWeb(url: string, controller: WebviewController) {
    if(this.rootNode != null) {
      return;
    }

    const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
    if (!uiContext) {
      return;
    }
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
  }

export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
  const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
  baseNode.initWeb(data.url, data.controller);
  return baseNode;
}
```

1.

编写用于生成字节码缓存的组件，本例中的本地Javascript资源内容通过文件读取接口读取rawfile目录下的本地文件。
```ets
// PrecompileWebview.ets
import { BuilderData } from "./DynamicComponent";
import { Config, configs } from "./PrecompileConfig";

@Builder
function WebBuilder(data: BuilderData) {
  Web({ src: data.url, controller: data.controller })
    .onControllerAttached(() => {
      precompile(data.controller, configs, data.context);
    })
    .fileAccess(true)
}

export const precompileWebview = wrapBuilder<BuilderData[]>(WebBuilder);

export const precompile = async (controller: WebviewController, configs: Array<Config>, context: UIContext) => {
  for (const config of configs) {
    let content = await readRawFile(config.localPath, context);

    try {
      controller.precompileJavaScript(config.url, content, config.options)
        .then(errCode => {
          console.error("precompile successfully! " + errCode);
        }).catch((errCode: number) => {
          console.error("precompile failed. " + errCode);
      });
    } catch (err) {
      console.error("precompile failed. " + err.code + " " + err.message);
    }

async function readRawFile(path: string, context: UIContext) {
  try {
    return await context.getHostContext()!.resourceManager.getRawFileContent(path);
  } catch (err) {
    return new Uint8Array(0);
  }
```

JavaScript资源的获取方式也可通过[网络请求](@ohos.net.http (数据请求).md)的方式获取，但此方法获取到的http响应头非标准HTTP响应头格式，需额外将响应头转换成标准HTTP响应头格式后使用。如通过网络请求获取到的响应头是e-tag，则需要将其转换成E-Tag后使用。

1.

编写业务用组件代码。
```ets
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  // 此处组件可根据业务需要自行扩展
  Web({ src: data.url, controller: data.controller })
    .cacheMode(CacheMode.Default)
}

export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```

1.

编写资源配置信息。
```ets
// PrecompileConfig.ets
import { webview } from '@kit.ArkWeb'

export interface Config {
  url:  string,
  localPath: string, // 本地资源路径
  options: webview.CacheOptions
}

export let configs: Array<Config> = [
  {
    url: "https://www.example.com/example.js",
    localPath: "example.js",
    options: {
      responseHeaders: [
        { headerKey: "E-Tag", headerValue: "aWO42N9P9dG/5xqYQCxsx+vDOoU="},
        { headerKey: "Last-Modified", headerValue: "Wed, 21 Mar 2024 10:38:41 GMT"}
      ]
  }
]
```

1.

在页面中使用。
```ets
// Index.ets
import { webview } from '@kit.ArkWeb';
import { NodeController } from '@kit.ArkUI';
import { createNode } from "./DynamicComponent"
import { precompileWebview } from "./PrecompileWebview"
import { businessWebview } from "./BusinessWebview"

@Entry
@Component
struct Index {
  @State precompileNode: NodeController | undefined = undefined;
  precompileController: webview.WebviewController = new webview.WebviewController();

  @State businessNode: NodeController | undefined = undefined;
  businessController: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    // 初始化用于注入本地资源的Web组件
    this.precompileNode = createNode(precompileWebview,
      { url: "https://www.example.com/empty.html", controller: this.precompileController, context: this.getUIContext()});
  }

  build() {
    Column() {
      // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
      Button("加载页面")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, {
            url:  "https://www.example.com/business.html",
            controller: this.businessController,
            context: this.getUIContext()
          });
        })
      // 用于业务的Web组件
      NodeContainer(this.businessNode);
    }
```

当需要更新本地已经生成的编译字节码时，修改cacheOptions参数中responseHeaders中的E-Tag或Last-Modified响应头对应的值，再次调用接口即可。

#### onCreateNativeMediaPlayer12+

onCreateNativeMediaPlayer(callback: [CreateNativeMediaPlayerCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605202__createnativemediaplayercallback12)): void

注册回调函数，开启[应用接管网页媒体播放功能](属性.md#ZH-CN_TOPIC_0000002553201131__enablenativemediaplayer12)后，当网页中有播放媒体时，触发注册的回调函数。

如果[应用接管网页媒体播放功能](../../topics/misc/属性.md#ZH-CN_TOPIC_0000002497605206__enablenativemediaplayer12)未开启，则注册的回调函数不会被触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CreateNativeMediaPlayerCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605202__createnativemediaplayercallback12) | 是 | 接管网页媒体播放的回调函数。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

class ActualNativeMediaPlayerListener {
  handler: webview.NativeMediaPlayerHandler;

  constructor(handler: webview.NativeMediaPlayerHandler) {
    this.handler = handler;
  }

  onPlaying() {
    // 本地播放器开始播放。
    this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
  }
  onPaused() {
    // 本地播放器暂停播放。
    this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
  }
  onSeeking() {
    // 本地播放器开始执行跳转到目标时间点。
    this.handler.handleSeeking();
  }
  onSeekDone() {
    // 本地播放器 seek 完成。
    this.handler.handleSeekFinished();
  }
  onEnded() {
    // 本地播放器播放完成。
    this.handler.handleEnded();
  }
  onVolumeChanged() {
    // 获取本地播放器的音量。
    let volume: number = getVolume();
    this.handler.handleVolumeChanged(volume);
  }
  onCurrentPlayingTimeUpdate() {
    // 更新播放时间。
    let currentTime: number = getCurrentPlayingTime();
    // 将时间单位换算成秒。
    let currentTimeInSeconds = convertToSeconds(currentTime);
    this.handler.handleTimeUpdate(currentTimeInSeconds);
  }
  onBufferedChanged() {
    // 缓存发生了变化。
    // 获取本地播放器的缓存时长。
    let bufferedEndTime: number = getCurrentBufferedTime();
    // 将时间单位换算成秒。
    let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
    this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);

    // 检查缓存状态。
    // 如果缓存状态发生了变化，则向 ArkWeb 内核通知缓存状态。
    let lastReadyState: webview.ReadyState = getLastReadyState();
    let currentReadyState:  webview.ReadyState = getCurrentReadyState();
    if (lastReadyState != currentReadyState) {
      this.handler.handleReadyStateChanged(currentReadyState);
  }
  onEnterFullscreen() {
    // 本地播放器进入了全屏状态。
    let isFullscreen: boolean = true;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onExitFullscreen() {
    // 本地播放器退出了全屏状态。
    let isFullscreen: boolean = false;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onUpdateVideoSize(width: number, height: number) {
    // 当本地播放器解析出视频宽高时， 通知 ArkWeb 内核。
    this.handler.handleVideoSizeChanged(width, height);
  }
  onDurationChanged(duration: number) {
    // 本地播放器解析到了新的媒体时长， 通知 ArkWeb 内核。
    this.handler.handleDurationChanged(duration);
  }
  onError(error: webview.MediaError, errorMessage: string) {
    // 本地播放器出错了，通知 ArkWeb 内核。
    this.handler.handleError(error, errorMessage);
  }
  onNetworkStateChanged(state: webview.NetworkState) {
    // 本地播放器的网络状态发生了变化， 通知 ArkWeb 内核。
    this.handler.handleNetworkStateChanged(state);
  }
  onPlaybackRateChanged(playbackRate: number) {
    // 本地播放器的播放速率发生了变化， 通知 ArkWeb 内核。
    this.handler.handlePlaybackRateChanged(playbackRate);
  }
  onMutedChanged(muted: boolean) {
    // 本地播放器的静音状态发生了变化， 通知 ArkWeb 内核。
    this.handler.handleMutedChanged(muted);
  }

  // ... 监听本地播放器其他的状态 ...
}

class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
  constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
    // 1. 创建一个本地播放器的状态监听。
    let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
    // 2. 创建一个本地播放器。
    // 3. 监听该本地播放器。
    // ...
  }

  updateRect(x: number, y: number, width: number, height: number) {
    // <video> 标签的位置和大小发生了变化。
    // 根据该信息变化，作出相应的改变。
  }

  play() {
    // 启动本地播放器播放。
  }

  pause() {
    // 暂停本地播放器播放。
  }

  seek(targetTime: number) {
    // 本地播放器跳转到指定的时间点。
  }

  release() {
    // 销毁本地播放器。
  }

  setVolume(volume: number) {
    // ArkWeb 内核要求调整本地播放器的音量。
    // 设置本地播放器的音量。
  }

  setMuted(muted: boolean) {
    // 将本地播放器静音或取消静音。
  }

  setPlaybackRate(playbackRate: number) {
    // 调整本地播放器的播放速度。
  }

  enterFullscreen() {
    // 将本地播放器设置为全屏播放。
  }

  exitFullscreen() {
    // 将本地播放器退出全屏播放。
  }

  resumePlayer() {
    // 重新创建应用内播放器。
    // 恢复应用内播放器的状态信息。
  }

  suspendPlayer(type: webview.SuspendType) {
    // 记录应用内播放器的状态信息。
    // 销毁应用内播放器。
  }

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
        .onPageBegin((event) => {
          this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
            if (!shouldHandle(mediaInfo)) {
              // 本地播放器不接管该媒体。
              // ArkWeb 内核将用自己的播放器来播放该媒体。
              return null;
            }
            let nativePlayer: webview.NativeMediaPlayerBridge = new NativeMediaPlayerImpl(handler, mediaInfo);
            return nativePlayer;
          });
        })
}

// stub
function getVolume() {
  return 1;
}
function getCurrentPlayingTime() {
  return 1;
}
function getCurrentBufferedTime() {
  return 1;
}
function convertToSeconds(input: number) {
  return input;
}
function getLastReadyState() {
  return webview.ReadyState.HAVE_NOTHING;
}
function getCurrentReadyState() {
  return webview.ReadyState.HAVE_NOTHING;
}
function shouldHandle(mediaInfo: webview.MediaInfo) {
  return true;
}
```

#### enableWholeWebPageDrawing12+

static enableWholeWebPageDrawing(): void

设置开启网页全量绘制能力。仅在web初始化时设置。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.enableWholeWebPageDrawing();
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
}
```

#### webPageSnapshot12+

webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void

获取网页全量绘制结果。

仅支持对渲染进程上的资源进行截图：静态图片和文本。

如果页面有视频则截图时会显示该视频的占位图片，没有占位图片则显示空白。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | SnapshotInfo | 是 | 全量绘制结果入参。 |
| callback | AsyncCallback<SnapshotResult> | 是 | 全量绘制回调结果。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('webPageSnapshot')
        .onClick(() => {
          try {
            this.controller.webPageSnapshot({ id: "1234", size: { width: 100, height: 100 } }, (error, result) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              if (result) {
                console.info(`return value is:${result}`);
                //开发者可以根据需要处理返回结果
              }
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### injectOfflineResources12+

injectOfflineResources(resourceMaps: Array<[OfflineResourceMap](Interfaces (其他).md#ZH-CN_TOPIC_0000002553361089__offlineresourcemap12)>): void

将本地离线资源注入到内存缓存中，以提升页面首次启动速度。

内存缓存中的资源由内核自动管理，当注入的资源过多导致内存压力过大，内核自动释放未使用的资源，应避免注入大量资源到内存缓存中。

正常情况下，资源的有效期由提供的Cache-Control或Expires响应头控制其有效期，默认的有效期为86400秒，即1天。

资源的MIMEType通过提供的Content-Type响应头配置，Content-Type需符合标准，否则无法正常使用，MODULE_JS必须提供有效的MIMEType，其他类型可不提供。

以此方式注入的资源，仅支持通过HTML中的标签加载。如果业务网页中的script标签使用了crossorigin属性，则必须在接口的responseHeaders参数中设置Cross-Origin响应头的值为anonymous或use-credentials。

当调用webview.WebviewController.Set[RenderProcessMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__renderprocessmode12)(webview.RenderProcessMode.MULTIPLE)接口后，应用会启动多渲染进程模式，此接口在此场景下不会生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceMaps | Array<OfflineResourceMap> | 是 | 本地离线资源配置对象，单次调用最大支持注入30个资源，单个资源最大支持10Mb。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**示例：**

接口推荐配合动态组件使用，使用离线的Web组件用于将资源注入到内核的内存缓存中，并在适当的时机加载业务用Web组件使用这些资源。下方是代码示例：

1.

首先，在EntryAbility中将UIContext存到localStorage中。
```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

const localStorage: LocalStorage = new LocalStorage('uiContext');

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', this.storage, (err, data) => {
      if (err.code) {
        return;
      }

      this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
    });
}
```

1.

编写动态组件所需基础代码。
```ets
// DynamicComponent.ets
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

export interface BuilderData {
  url: string;
  controller: WebviewController;
  context: UIContext;
}

let storage : LocalStorage | undefined = undefined;

export class NodeControllerImpl extends NodeController {
  private rootNode: BuilderNode<BuilderData[]> | null = null;
  private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

  constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
    storage = context.getSharedLocalStorage();
    super();
    this.wrappedBuilder = wrappedBuilder;
  }

  makeNode(): FrameNode | null {
    if (this.rootNode != null) {
      return this.rootNode.getFrameNode();
    }
    return null;
  }

  initWeb(url: string, controller: WebviewController) {
    if(this.rootNode != null) {
      return;
    }

    const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
    if (!uiContext) {
      return;
    }
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
}

export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
  const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
  baseNode.initWeb(data.url, data.controller);
  return baseNode;
}
```

1.

编写用于注入资源的组件代码，本例中的本地资源内容通过文件读取接口读取rawfile目录下的本地文件。
```ets
// InjectWebview.ets
import { webview } from '@kit.ArkWeb';
import { resourceConfigs } from "./Resource";
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  Web({ src: data.url, controller: data.controller })
    .onControllerAttached(async () => {
      try {
        data.controller.injectOfflineResources(await getData (data.context));
      } catch (err) {
        console.error("error: " + err.code + " " + err.message);
      }
    })
    .fileAccess(true)
}

export const injectWebview = wrapBuilder<BuilderData[]>(WebBuilder);

export async function getData(context: UIContext) {
  const resourceMapArr: Array<webview.OfflineResourceMap> = [];

  // 读取配置，从rawfile目录中读取文件内容
  for (let config of resourceConfigs) {
    let buf: Uint8Array = new Uint8Array(0);
    if (config.localPath) {
      buf = await readRawFile(config.localPath, context);
    }

    resourceMapArr.push({
      urlList: config.urlList,
      resource: buf,
      responseHeaders: config.responseHeaders,
      type: config.type,
    })
  }

  return resourceMapArr;
}

export async function readRawFile(url: string, context: UIContext) {
  try {
    return await context.getHostContext()!.resourceManager.getRawFileContent(url);
  } catch (err) {
    return new Uint8Array(0);
}
```

1.

编写业务用组件代码。
```ets
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  // 此处组件可根据业务需要自行扩展
  Web({ src: data.url, controller: data.controller })
    .cacheMode(CacheMode.Default)
}

export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```

1.

编写资源配置信息。
```ets
// Resource.ets
import { webview } from '@kit.ArkWeb';

export interface ResourceConfig {
  urlList: Array<string>,
  type: webview.OfflineResourceType,
  responseHeaders: Array<Header>,
  localPath: string, // 本地资源存放在rawfile目录下的路径
}

export const resourceConfigs: Array<ResourceConfig> = [
  {
    localPath: "example.png",
    urlList: [
      "https://www.example.com/",
      "https://www.example.com/path1/example.png",
      "https://www.example.com/path2/example.png",
    ],
    type: webview.OfflineResourceType.IMAGE,
    responseHeaders: [
      { headerKey: "Cache-Control", headerValue: "max-age=1000" },
      { headerKey: "Content-Type", headerValue: "image/png" },
    ]
  },
  {
    localPath: "example.js",
    urlList: [ // 仅提供一个url，这个url既作为资源的源，也作为资源的网络请求地址
      "https://www.example.com/example.js",
    ],
    type: webview.OfflineResourceType.CLASSIC_JS,
    responseHeaders: [
      // 以<script crossorigin="anonymous" />方式使用，提供额外的响应头
      { headerKey: "Cross-Origin", headerValue:"anonymous" }
    ]
  },
];
```

1.

在页面中使用。
```ets
// Index.ets
import { webview } from '@kit.ArkWeb';
import { NodeController } from '@kit.ArkUI';
import { createNode } from "./DynamicComponent"
import { injectWebview } from "./InjectWebview"
import { businessWebview } from "./BusinessWebview"

@Entry
@Component
struct Index {
  @State injectNode: NodeController | undefined = undefined;
  injectController: webview.WebviewController = new webview.WebviewController();

  @State businessNode: NodeController | undefined = undefined;
  businessController: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    // 初始化用于注入本地资源的Web组件, 提供一个空的html页面作为url即可
    this.injectNode = createNode(injectWebview,
        { url: "https://www.example.com/empty.html", controller: this.injectController, context: this.getUIContext()});
  }

  build() {
    Column() {
      // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
      Button("加载页面")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, {
            url: "https://www.example.com/business.html",
            controller: this.businessController,
            context: this.getUIContext()
          });
        })
      // 用于业务的Web组件
      NodeContainer(this.businessNode);
    }
```

1.

加载的HTML网页示例。
```ets
<!DOCTYPE html>
<html lang="en">
<head></head>
<body>
  <img src="https://www.example.com/path1/request.png" />
  <img src="https://www.example.com/path2/request.png" />
  <script src="https://www.example.com/example.js" crossorigin="anonymous"></script>
</body>
</html>
```

#### setHostIP12+

static setHostIP(hostName: string, address: string, aliveTime: number): void

设置主机域名解析后的IP地址。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | 要添加DNS记录的主机域名。 |
| address | string | 是 | 主机域名解析地址（支持IPv4，IPv6）。 |
| aliveTime | number | 是 | 缓存有效时间（秒）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |

**示例：**

请参考[clearHostIP](#ZH-CN_TOPIC_0000002553201117__clearhostip12)。

#### clearHostIP12+

static clearHostIP(hostName: string): void

清除指定主机域名解析后的IP地址。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | 要清除DNS记录的主机域名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // url加载前设置生效.
      Button('setHostIP')
        .onClick(() => {
          try {
            webview.WebviewController.setHostIP('www.example.com', '127.0.0.1', 30);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('clearHostIP')
        .onClick(() => {
          try {
            webview.WebviewController.clearHostIP('www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getSurfaceId12+

getSurfaceId(): string

获取ArkWeb对应Surface的ID，此ID可用于网页截图。

仅Web组件渲染模式是ASYNC_RENDER时有效。getSurfaceId需要在Web组件初始化之后才能获取到值。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | ArkWeb持有Surface的ID。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Example{
  controller: webview.WebviewController = new webview.WebviewController();

  @State imagePixelMap: image.PixelMap | undefined = undefined;

  build(){
    Column(){
      Button("截图")
        .onClick(()=>{
          try {
            let surfaceId = this.controller.getSurfaceId();
            console.info("surfaceId: " + surfaceId);
            if(surfaceId.length != 0) {
              let region:image.Region = { x: 0, y: 0, size: { height: 800, width: 1000}}
              this.imagePixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region)
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Image(this.imagePixelMap)
        .height(100)
      Web({src: 'www.example.com', controller: this.controller})
    }
```

#### setUrlTrustList12+

setUrlTrustList(urlTrustList: string): void

设置当前web的url白名单，只有白名单内的url才能允许加载/跳转，否则将拦截并弹出告警页。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| urlTrustList | string | 是 | url白名单列表，使用json格式配置，最大支持10MB。 白名单设置接口为覆盖方式，多次调用接口时，以最后一次设置为准。 当本参数为空字符串时，表示取消白名单，放行所有url的访问。 json格式示例： { "UrlPermissionList": [ { "scheme": "https", "host": "www.example1.com", "port": 443, "path": "pathA/pathB" }, { "scheme": "http", "host": "www.example2.com", "port": 80, "path": "test1/test2/test3" } ] } |

**白名单json格式参数**

| 字段 | 参数类型 | 必填 | 参数描述 |
| --- | --- | --- | --- |
| scheme | string | 否 | 可选参数，不设置即不匹配该项，支持协议：http、https。 |
| host | string | 是 | 必选参数，精准匹配，即url的host字段和规则字段完全一致才会放行，可允许同一host多条规则同时生效。 |
| port | number | 否 | 可选字段，不设置即不匹配该项。 |
| path | string | 否 | 可选字段，不设置即不匹配该项，匹配方式为前缀匹配，以"pathA/pathB/pathC"为例：pathA/pathB/pathC三级目录下全部允许访问，其中pathC必须是完整的目录名或者文件名，不允许部分匹配。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Parameter string is too long.3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  urltrustList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"port\":80, \"path\":\"test\"}]}"

  build() {
    Column() {
      Button('Setting the trustlist')
        .onClick(() => {
          try {
            // 设置白名单，只允许访问trust网页
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Cancel the trustlist.')
        .onClick(() => {
          try {
            // 白名单传入空字符串表示关闭白名单机制，所有url都可以允许访问
            this.controller.setUrlTrustList("");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // 白名单生效，可以访问trust网页
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the untrust web')
        .onClick(() => {
          try {
            // 白名单生效，此时不可以访问untrust网页，并弹出错误页
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // onControllerAttached回调中设置白名单，可以保证在加载url之前生效，此时不可以访问untrust网页，并弹出错误页
          this.controller.setUrlTrustList(this.urltrustList);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
```

#### setPathAllowingUniversalAccess12+

setPathAllowingUniversalAccess(pathList: Array<string>): void

设置一个路径列表，当file协议访问该路径列表中的资源时，允许跨域访问本地文件，也允许跨域访问其他在线资源。此外，当设置了路径列表时，file协议仅允许访问路径列表中的资源（[fileAccess](属性.md#ZH-CN_TOPIC_0000002553201131__fileaccess)的行为将会被此接口行为覆盖）。路径列表中的路径必须满足以下路径格式之一：

1.应用文件目录的子目录（应用文件目录通过Ability Kit中的[Context.filesDir](Context (Stage模型的上下文基类).md#ZH-CN_TOPIC_0000002522240572__context)获取），例如：

- /data/storage/el2/base/files/example
- /data/storage/el2/base/haps/entry/files/example

2.应用资源目录及其子目录（应用资源目录通过Ability Kit中的[Context.resourceDir](Context (Stage模型的上下文基类).md#ZH-CN_TOPIC_0000002522240572__context)获取），例如：

- /data/storage/el1/bundle/entry/resources/resfile

- /data/storage/el1/bundle/entry/resources/resfile/example

3.从API version 21开始，还包括了应用缓存目录及其子目录（应用缓存目录通过Ability Kit中的[Context.cacheDir](Context (Stage模型的上下文基类).md#ZH-CN_TOPIC_0000002522240572__context)获取），例如：

- /data/storage/el2/base/cache
- /data/storage/el2/base/haps/entry/cache/example
- 设置的目录路径中，不允许包含cache/web，否则会抛出异常码401。如果设置目录路径是cache，cache/web也不允许访问。

4.从API version 21开始，还包括了应用临时目录及其子目录（应用临时目录通过Ability Kit中的[Context.tempDir](Context (Stage模型的上下文基类).md#ZH-CN_TOPIC_0000002522240572__context)获取），例如：

- /data/storage/el2/base/temp
- /data/storage/el2/base/haps/entry/temp/example

当路径列表中有其中一个路径不满足以上条件之一，则会抛出异常码401，并且设置路径列表失败。当设置的路径列表为空，则file协议可访问范围以[fileAccess](属性.md#ZH-CN_TOPIC_0000002553201131__fileaccess)的行为为准。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathList | Array<string> | 是 | 路径列表 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Row() {
      Web({ src: "", controller: this.controller })
        .onControllerAttached(() => {
          try {
            // 设置允许可以跨域访问的路径列表
            this.controller.setPathAllowingUniversalAccess([
              this.uiContext.getHostContext()!.resourceDir,
              this.uiContext.getHostContext()!.filesDir + "/example"
            ])
            this.controller.loadUrl("file://" + this.getUIContext().getHostContext()!.resourceDir + "/index.html")
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        .javaScriptAccess(true)
        .fileAccess(true)
        .domStorageAccess(true)
    }
```

加载的html文件，位于应用资源目录resource/resfile/index.html。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Demo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no, viewport-fit=cover">
    <script>
        function getFile() {
            var file = "file:///data/storage/el1/bundle/entry/resources/resfile/js/script.js";
            var xmlHttpReq = new XMLHttpRequest();
            xmlHttpReq.onreadystatechange = function(){
                console.info("readyState:" + xmlHttpReq.readyState);
                console.info("status:" + xmlHttpReq.status);
                if(xmlHttpReq.readyState == 4){
                    if (xmlHttpReq.status == 200) {
                // 如果ets侧正确设置路径列表，则此处能正常获取资源
                        const element = document.getElementById('text');
                        element.textContent = "load " + file + " success";
                    } else {
                // 如果ets侧不设置路径列表，则此处会触发CORS跨域检查错误
                        const element = document.getElementById('text');
                        element.textContent = "load " + file + " failed";
                    }
            xmlHttpReq.open("GET", file);
            xmlHttpReq.send(null);
        }

    </script>
</head>

<body>
<div class="page">
    <button id="example" onclick="getFile()">stealFile</button>
</div>
<div id="text"></div>
</body>

</html>
```

html中使用file协议通过XMLHttpRequest跨域访问本地js文件，js文件位于resource/resfile/js/script.js。

```ets
const body = document.body;
const element = document.createElement('div');
element.textContent = 'success';
body.appendChild(element);
```

#### enableBackForwardCache12+

static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void

开启Web组件前进后退缓存功能，通过参数指定是否允许使用特定的页面进入前进后退缓存。

需要在[initializeWebEngine()](#ZH-CN_TOPIC_0000002553201117__initializewebengine)初始化内核之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| features | BackForwardCacheSupportedFeatures | 是 | 允许使用特定的页面进入前进后退缓存中。 |

**示例：**

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        let features = new webview.BackForwardCacheSupportedFeatures();
        features.nativeEmbed = true;
        features.mediaTakeOver = true;
        // 如果一个页面同时使用了同层渲染和视频托管的能力，需要 nativeEmbed 和
        // mediaTakeOver 同时设置为 true，该页面才可以进入前进后退缓存中。
        webview.WebviewController.enableBackForwardCache(features);
        webview.WebviewController.initializeWebEngine();
        AppStorage.setOrCreate("abilityWant", want);
    }
```

#### setBackForwardCacheOptions12+

setBackForwardCacheOptions(options: BackForwardCacheOptions): void

可以设置Web组件中前进后退缓存的相关选项。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | BackForwardCacheOptions | 是 | 用来控制Web组件前进后退缓存相关选项。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button("Add options").onClick((event: ClickEvent) => {
          let options = new webview.BackForwardCacheOptions();
          options.size = 3;
          options.timeToLive = 10;
          this.controller.setBackForwardCacheOptions(options);
        })
        Button("Backward").onClick((event: ClickEvent) => {
          this.controller.backward();
        })
        Button("Forward").onClick((event: ClickEvent) => {
          this.controller.forward();
        })
      }
      Web({ src: "https://www.example.com", controller: this.controller })
    }
    .height('100%')
    .width('100%')
  }
```

#### trimMemoryBy[PressureLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__pressurelevel14)14+

trimMemoryBy[PressureLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__pressurelevel14)(level: PressureLevel): void

根据指定的内存压力等级，主动清理Web组件占用的缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [PressureLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__pressurelevel14) | 是 | 需要清理内存的内存等级。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Row() {
        Button('trim_Memory')
          .onClick(() => {
            try {
              // 设置当前内存压力等级为适中，释放少量内存
              webview.WebviewController.trimMemoryByPressureLevel(
                webview.PressureLevel.MEMORY_PRESSURE_LEVEL_MODERATE);
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
      }.height('10%')
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### createPdf14+

createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void

异步callback方式获取指定网页的数据流。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | PdfConfiguration | 是 | 生成PDF所需参数。 |
| callback | AsyncCallback<PdfData> | 是 | 回调返回网页PDF数据流。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例**:

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  }

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(
            this.pdfConfig,
            (error, result: webview.PdfData) => {
              try {
                // 获取组件上下文
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // 获取沙箱路径，设置pdf文件名
                let filePath = context.filesDir + "/test.pdf";
                let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeed and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fs.closeSync(file);
                });
              } catch (resError) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }
            });
        })
      Web({ src: "www.example.com", controller: this.controller })
    }
```

#### createPdf14+

createPdf(configuration: PdfConfiguration): Promise<PdfData>

以Promise方式异步获取指定网页的数据流。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | PdfConfiguration | 是 | 生成PDF所需参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PdfData> | Promise实例，返回网页数据流。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例**:

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  }

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(this.pdfConfig)
            .then((result: webview.PdfData) => {
              try {
                // 获取组件上下文
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // 获取沙箱路径，设置pdf文件名
                let filePath = context.filesDir + "/test.pdf";
                let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeed and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fs.closeSync(file);
                });
              } catch (resError) {
                console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
              }
            })
      Web({ src: "www.example.com", controller: this.controller })
}
```

#### getScrollOffset13+

getScrollOffset(): ScrollOffset

获取网页当前的滚动偏移量（包含过滚动偏移量）。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值**

| 类型 | 说明 |
| --- | --- |
| ScrollOffset | 网页当前的滚动偏移量（包含过滚动偏移量）。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State testTitle: string = 'webScroll'
  controller: webview.WebviewController = new webview.WebviewController();
  @State controllerX: number =-100;
  @State controllerY: number =-100;
  @State mode: OverScrollMode = OverScrollMode.ALWAYS;

  build() {
    Column() {
      Row() {
        Text(this.testTitle)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin(5)
      }
      Column() {
        Text(`controllerX: ${this.controllerX}, controllerY: ${this.controllerY}`)
      }
      .margin({ top: 10, bottom: 10 })
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .key("web_01")
        .overScrollMode(this.mode)
        .onTouch(() => {
          this.controllerX = this.controller.getScrollOffset().x;
          this.controllerY = this.controller.getScrollOffset().y;
          let componentInfo = this.getUIContext().getComponentUtils().getRectangleById("web_01");
          let webHeight = this.getUIContext().px2vp(componentInfo.size.height);
          let pageHeight = this.controller.getPageHeight();
          if (this.controllerY < 0) {
            // case1：网页向下过滚动时，可直接使用ScrollOffset.y
            console.info(`get downwards overscroll offsetY = ${this.controllerY}`);
          } else if ((this.controllerY != 0) && (this.controllerY > (pageHeight - webHeight))) {
            // case2：网页向上过滚动时，需计算出网页下边界与Web组件下边界的偏移量
            console.info(`get upwards overscroll offsetY = ${this.controllerY - (pageHeight >= webHeight ? (pageHeight - webHeight) : 0)}`);
          } else {
            // case3：网页未发生过滚动时，可直接使用ScrollOffset.y
            console.info(`get scroll offsetY = ${this.controllerY}`);
          }
        })
        .height(600)
    }
    .width('100%')
    .height('100%')
  }
```

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
    <title>Demo</title>
    <style>
        body {
          width:3000px;
          height:6000px;
          padding-right:170px;
          padding-left:170px;
          border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

#### getPageOffset20+

getPageOffset(): ScrollOffset

获取网页当前的滚动偏移量（不包含过滚动偏移量）。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值**

| 类型 | 说明 |
| --- | --- |
| ScrollOffset | 网页当前的滚动偏移量（不包含过滚动偏移量）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onScroll((event) => {
          try {
            console.info("getPageOffset x:" + this.controller.getPageOffset().x + ",y:" +
            this.controller.getPageOffset().y);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
}
```

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

#### getLastHitTest18+

getLastHitTest(): HitTestValue

获取上一次被点击区域的元素信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HitTestValue | 点击区域的元素信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getLastHitTest')
        .onClick(() => {
          try {
            let hitValue = this.controller.getLastHitTest();
            console.info("hitType: " + hitValue.type);
            console.info("extra: " + hitValue.extra);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getAttachState20+

getAttachState(): ControllerAttachState

查询当前WebViewController是否绑定一个Web组件。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ControllerAttachState | WebViewController与Web组件的绑定状态。 |

**示例：**

点击Button可以获取当前WebViewController的绑定状态并输出日志。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getAttachState')
        .onClick(() => {
          try {
            if (this.controller.getAttachState() == webview.ControllerAttachState.ATTACHED) {
              console.info('Controller is attached.');
            } else {
              console.info('Controller is unattached.');
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### on('controllerAttachStateChange')20+

on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void

注册WebViewController绑定状态事件，通过Callback方式获取WebViewController绑定状态的变化通知。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示注册WebViewController绑定状态事件，固定为"controllerAttachStateChange"。 |
| callback | Callback<ControllerAttachState> | 是 | WebViewController绑定状态改变时的回调函数。 |

**示例：**

请参考[off](#ZH-CN_TOPIC_0000002553201117__offcontrollerattachstatechange20)。

#### off('controllerAttachStateChange')20+

off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void

取消WebViewController绑定状态事件的注册，取消后将不再接收Callback通知。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示注册WebViewController绑定状态事件，固定为"controllerAttachStateChange"。 |
| callback | Callback<ControllerAttachState> | 否 | WebViewController绑定状态发生改变时的回调函数，默认情况下不填写回调函数。如果填写了Callback，将仅取消注册该特定的回调。如果不填写Callback，将取消注册所有回调。 传入null或undefined时会抛出异常错误码401。 |

**示例：**

on可以注册多个回调，当绑定状态改变后会获取当前的绑定状态并触发这些回调。off可以取消注册某个回调，也可以取消注册所有回调。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  // 构建回调函数
  handleControllerAttachStateChange = (state: webview.ControllerAttachState) => {
    if (state == webview.ControllerAttachState.UNATTACHED) {
      console.info('handleControllerAttachStateChange: Controller is unattached.');
    } else {
      console.info('handleControllerAttachStateChange: Controller is attached.');
    }
  };
  aboutToAppear() {
    try {
      this.controller.on('controllerAttachStateChange', this.handleControllerAttachStateChange);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
    try {
      // 注册回调以接收controller绑定状态更改通知
      this.controller.on('controllerAttachStateChange', (state: webview.ControllerAttachState) => {
        if (state == webview.ControllerAttachState.UNATTACHED) {
          console.info('Controller is unattached.');
        } else {
          console.info('Controller is attached.');
        }
      })
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  aboutToDisappear() {
    // 取消指定注册回调
    // this.controller.off('controllerAttachStateChange', this.handleControllerAttachStateChange);
    // 取消所有注册回调
    this.controller.off('controllerAttachStateChange');
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### waitForAttached20+

waitForAttached(timeout: number):Promise<ControllerAttachState>

异步等待WebViewController与Web组件绑定完成，绑定完成或超时触发回调，通过Promise方式返回当前[ControllerAttachState](Interfaces (其他).md#ZH-CN_TOPIC_0000002553361089__controllerattachstate20)状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 异步等待时长。 取值范围: [0, 65535] 单位: ms |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ControllerAttachState> | Promise实例，返回当前ControllerAttachState状态。 |

**示例：**

在初始化阶段设置WebViewController等待绑定完成，超时时间为1000ms。若绑定完成或者超时则会触发回调。

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  async aboutToAppear() {
    this.controller.waitForAttached(1000).then((state: webview.ControllerAttachState) => {
      if (state == webview.ControllerAttachState.ATTACHED) {
        //绑定完成或者超时都会触发回调
        console.info('Controller is attached.');
      }
    })
    try {
      const state = await this.controller.waitForAttached(1000);
      if (state == webview.ControllerAttachState.ATTACHED) {
        console.info('Controller is attached.');
      }
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setWebDebuggingAccess20+

static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void

设置是否启用无线网页调试功能，默认不开启。

- 当没有指定端口port时，该接口等同于[setWebDebuggingAccess](#ZH-CN_TOPIC_0000002553201117__setwebdebuggingaccess)接口，ArkWeb会启动一个本地domain socket监听。

- 当指定了端口port时，ArkWeb会启动一个tcp socket监听。这时可以无线调试网页。详情请参考[无线调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-debugging-with-devtools#无线调试)。

由于小于1024的端口号作为熟知或系统端口，在操作系统上需要特权才能开启，因此port的取值必须大于1024，否则该接口会抛出异常。

安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患，不建议在应用正式发布版本中启用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | 是 | 设置是否启用网页调试功能。 true表示开启网页调试功能，false表示关闭网页调试功能。 |
| port | number | 是 | 指定DevTools服务的tcp端口号。如果没有指定port，那么该接口等同于setWebDebuggingAccess接口。 取值范围: (1024, 65535] 如果port的值在区间[0, 1024]内，则会抛出BusinessError异常，错误码为17100023。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100023 | The port number is not within the allowed range. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.setWebDebuggingAccess(true, 8888);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
}
```

#### getProgress20+

getProgress(): number

获取当前网页加载进度。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值**

| 类型 | 说明 |
| --- | --- |
| number | 当前页面加载进度，取值范围[0, 100] |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageBegin(() => {
          let curProgress = this.controller.getProgress();
          console.info("current page loading progress is :" + curProgress);
        })
    }
```

#### getHitTest(deprecated)

getHitTest(): [WebHitTestType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webhittesttype)

获取当前被点击区域的元素类型。


从API version11开始支持，从API version 18开始废弃。建议使用[getLastHitTest](#ZH-CN_TOPIC_0000002553201117__getlasthittest18)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebHitTestType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webhittesttype) | 被点击区域的元素类型。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getHitTest')
        .onClick(() => {
          try {
            let hitTestType = this.controller.getHitTest();
            console.info("hitTestType: " + hitTestType);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getHitTestValue(deprecated)

getHitTestValue(): HitTestValue

获取当前被点击区域的元素信息。


从API version11开始支持，从API version 18开始废弃。建议使用[getLastHitTest](#ZH-CN_TOPIC_0000002553201117__getlasthittest18)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HitTestValue | 点击区域的元素信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getHitTestValue')
        .onClick(() => {
          try {
            let hitValue = this.controller.getHitTestValue();
            console.info("hitType: " + hitValue.type);
            console.info("extra: " + hitValue.extra);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### avoidVisibleViewportBottom20+

avoidVisibleViewportBottom(avoidHeight: number): void

设置Web网页可视视口底部避让高度。

- avoidHeight有效值区间为[0, Web组件高度]，超出有效值区间时取边界值。
- 该接口高度设置为非0时，Web组件位置和尺寸不变，可视视口向上避让avoidHeight，表现为Web网页内容抬升avoidHeight。该接口一般用于应用自定义网页底部避让区，不建议和点击web网页可编辑区拉起键盘的场景同时使用。同时使用时，键盘弹起避让模式将使用OVERLAYS_CONTENT。

- 该接口高度设置为0时，Web网页内容可恢复，键盘弹起避让模式将使用[keyboardAvoidMode()](属性.md#ZH-CN_TOPIC_0000002553201131__keyboardavoidmode12)声明的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| avoidHeight | number | 是 | 设置Web网页可视视口底部避让高度。 单位：vp 合法取值范围：0~Web组件高度 非法值设置行为：小于0取值为0，大于Web组件高度取值为Web组件高度。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  avoidHeight: number = 100;

  build() {
    Column() {
      Button('avoid')
        .onClick(() => {
          try {
            this.controller.avoidVisibleViewportBottom(this.avoidHeight);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('reset')
        .onClick(() => {
          try {
            this.controller.avoidVisibleViewportBottom(0);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setErrorPageEnabled20+

setErrorPageEnabled(enable: boolean): void

设置是否启用默认错误页。

在当前接口设置为true时如果页面加载发生错误将触发[onOverrideErrorPage](事件.md#ZH-CN_TOPIC_0000002522081170__onoverrideerrorpage20)回调，可在该回调接口中设置自定义的错误展示页面。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否启用默认错误页。true表示启用，false表示不启用。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
    }
```

#### getErrorPageEnabled20+

getErrorPageEnabled(): boolean

查询是否启用了默认错误页功能。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否启用默认错误页功能。 true：已启用；false：未启用。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
    }
```

#### enablePrivateNetworkAccess20+

static enablePrivateNetworkAccess(enable: boolean): void

设置私有网络访问检查功能（Private Network Access）的启用状态。

启用后，Web组件将对私有网络请求（如访问本地服务器或内网资源）进行CORS预检。它会先发送OPTIONS预检请求，获取目标服务器的显式授权，然后传输实际数据。禁用此功能将跳过安全检查。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用私有网络访问检查功能开关。true表示启用，false表示禁用。 |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          // 设置为false时ArkWeb将不再检查私有网络请求是否合法
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
```

#### isPrivateNetworkAccessEnabled20+

static isPrivateNetworkAccessEnabled(): boolean

获取Web组件是否启用了私有网络访问检查功能。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Web组件是否启用了私有网络访问检查功能。true表示已启用；false表示已禁用。 |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isPrivateNetworkAccessEnabled')
        .onClick(() => {
          try {
            let isEnabled: boolean = webview.WebviewController.isPrivateNetworkAccessEnabled();
            console.info("isPrivateNetworkAccessEnabled:", isEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          // 设置为false时ArkWeb将不再检查私有网络请求是否合法
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
```

#### getBlanklessInfoWithKey20+

getBlanklessInfoWithKey(key: string): BlanklessInfo

获取页面首屏加载预测信息（详细说明见[BlanklessInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002553361089__blanklessinfo20)），并开始本次加载过渡帧生成，应用根据此信息确定是否需要启用无白屏加载。必须与[setBlanklessLoadingWithKey](#ZH-CN_TOPIC_0000002553201117__setblanklessloadingwithkey20)接口配套使用，并且必须在触发加载页面的接口之前或在onLoadIntercept中调用。需在WebViewController与Web组件绑定后才能使用。


- 持久缓存容量：默认大小为30MB（约30页），可以通过接口[setBlanklessLoadingCacheCapacity](#ZH-CN_TOPIC_0000002553201117__setblanklessloadingcachecapacity20)设置缓存容量，具体见该接口说明。超过容量时根据LRU（Least Recently Used，淘汰不常用缓存的策略）机制更新缓存。自动清理超过7天的持久缓存数据，缓存清除后第三次加载页面开始有优化效果。

- 如果发现快照相似度（即[BlanklessInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002553361089__blanklessinfo20)中的similarity）极低，请确认key值是否传递正确。

- 调用本接口后，将启用页面加载快照检测及生成过渡帧计算，会产生一定的资源开销。
- 启用无白屏加载的页面会带来一定的资源开销，开销的大小与Web组件的分辨率相关。假设分辨率的宽度和高度分别为：w, h。页面在打开阶段会增加峰值内存，增加约12wh B，页面打开后内存回收，不影响稳态内存。增加固态应用缓存的大小，每个页面增加的缓存约w*h/10 B，缓存位于应用缓存的位置。
- 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，具体权限的添加方法请参考[在配置文件中声明权限](../../guides/声明权限.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 唯一标识本页面的key值。 合法取值范围：非空，长度不超过2048个字符。 设置非法值时不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| BlanklessInfo | 页面首屏加载预测信息，主要包括首屏相似度预测值，首屏加载耗时预测值，应用需根据此信息来决策是否启用无白屏加载插帧。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                if (info.similarity >= 0.5 && info.loadingTime < 1000) {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
                } else {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
                }
              } else {
                console.info('getBlankless info err');
              }
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
            return false;
        })
    }
```

#### setBlanklessLoadingWithKey20+

setBlanklessLoadingWithKey(key: string, is_start: boolean): [WebBlanklessErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webblanklesserrorcode20)

设置无白屏加载是否启用，本接口必须与[getBlanklessInfoWithKey](#ZH-CN_TOPIC_0000002553201117__getblanklessinfowithkey20)接口配套使用。


- 需在触发页面加载的接口之后调用，其他约束同[getBlanklessInfoWithKey](#ZH-CN_TOPIC_0000002553201117__getblanklessinfowithkey20)。

- 页面加载必须在调用本接口的组件中进行。
- 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。
- 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，具体权限的添加方法请参考[在配置文件中声明权限](../../guides/声明权限.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 唯一标识本页面的key值。必须与getBlanklessInfoWithKey接口的key值相同。 合法取值范围：非空，长度不超过2048个字符。 非法值设置行为：返回错误码[WebBlanklessErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webblanklesserrorcode20)，方案不生效。 |
| is_start | boolean | 是 | 是否启用开始插帧。true：启用，false：不启用。 传入undefined或null时为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebBlanklessErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webblanklesserrorcode20) | 返回接口调用是否成功，具体见WebBlanklessErrorCode定义。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                if (info.similarity >= 0.5 && info.loadingTime < 1000) {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
                } else {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
                }
              } else {
                console.info('getBlankless info err');
              }
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
            return false;
        })
    }
```

**setBlanklessLoadingWithParams23+**

setBlanklessLoadingWithParams(key: string, param: BlanklessLoadingParam): [WebBlanklessErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webblanklesserrorcode20)

设置白屏插帧的配置参数，本接口必须与[getBlanklessInfoWithKey](#ZH-CN_TOPIC_0000002553201117__getblanklessinfowithkey20)接口配套使用。相比于[setBlanklessLoadingWithKey](#ZH-CN_TOPIC_0000002553201117__setblanklessloadingwithkey20)，本接口支持白屏插帧更多的参数设置，包括插帧持续时间，缓存数据有效时间，插帧完成后的自定义回调。


- 需在触发页面加载的接口之后调用，其他约束同[getBlanklessInfoWithKey](#ZH-CN_TOPIC_0000002553201117__getblanklessinfowithkey20)。

- 页面加载必须在调用本接口的组件中进行。

- 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。

- 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，具体权限的添加方法请参考[在配置文件中声明权限](../../guides/声明权限.md#在配置文件中声明权限)。

系统能力： SystemCapability.Web.Webview.Core

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 唯一标识本页面的key值。必须与getBlanklessInfoWithKey接口的key值相同。 合法取值范围：非空，长度不超过2048个字符。 非法值设置行为：返回错误码[WebBlanklessErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webblanklesserrorcode20)，方案不生效。 |
| param | BlanklessLoadingParam | 是 | 白屏插帧加载的各项参数设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| [WebBlanklessErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webblanklesserrorcode20) | 返回接口调用结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

示例：

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                let data = new Date(2026, 5, 10, 0, 0, 0, 0);
                let param: webview.BlanklessLoadingParam = {
                  enable: info.similarity > 0.4 && info.similarity < 2000,
                  duration: info.loadingTime,
                  expirationTime: data.getTime(),
                  callback: (info: webview.BlanklessFrameInterpolationInfo)=>{
                    // 数据监控
                  },
                };
                this.controller.setBlanklessLoadingWithParams('http://www.example.com/page1', param);
              } else {
                console.info('getBlankless info err');
  }
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},
                Message: ${(error as BusinessError).message}`);
            }
            return false;
        })
}
```

#### clearBlanklessLoadingCache20+

static clearBlanklessLoadingCache(keys?: Array<string>): void

清除指定key值页面无白屏优化缓存，本接口只清除缓存。

在小程序或Web应用场景中，当页面加载时内容变化显著，可能会出现一次明显的跳变。若对此跳变有所顾虑，可使用该接口清除页面缓存。

- 清除之后的页面，需在第三次加载页面时才会产生优化效果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array<string> | 否 | 清除Blankless优化方案页面的key值列表，key值为getBlanklessInfoWithKey中指定过的。 默认值：所有Blankless优化方案缓存的页面key列表。 合法取值范围：长度不超过2048，key列表长度<=100。key和加载页面时输入给ArkWeb的相同。 非法值设置行为：传入undefined/null会抛出异常错误码401；key长度超过2048时该key不生效；长度超过100时，取前100个；当为空时，使用默认值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    // 假设应用的Web页面在2025/06/10会进行大幅改动，例如商品促销活动等，该提案清除白屏插帧优化缓存
    webview.WebviewController.initializeWebEngine();
    let pageUpdateTime: number = Date.UTC(2025, 5, 10, 0, 0, 0, 0);
    let pageUpdateTime1: number = Date.UTC(2025, 5, 11, 0, 0, 0, 0);
    let pageUpdateTimeNow: number = Date.now();
    if (pageUpdateTimeNow > pageUpdateTime && pageUpdateTime < pageUpdateTime1) {
      // 清除指定页面的白屏插帧方案缓存
      try {
        webview.WebviewController.clearBlanklessLoadingCache(["https://www.example.com", "https://www.example1.com"]);
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
      }
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
}
```

#### setBlanklessLoadingCacheCapacity20+

static setBlanklessLoadingCacheCapacity(capacity: number): number

设置无白屏加载方案的持久化缓存容量，返回实际生效值。当接口没有显式调用时，默认缓存容量为30MB。当实际缓存超过容量时，将采用淘汰不常用的过渡帧的方式清理。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capacity | number | 是 | 设置持久化缓存设置，单位MB，最大设置不超过100MB。 合法取值范围：0~100，当设置为0时，无缓存空间，则功能全局不开启。 非法值设置行为：小于0时生效值为0，大于100时生效值为100。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回实际生效的容量值，范围0~100。 小于0时生效值为0，大于100时生效值为100。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 设置缓存容量为10MB
    try {
      webview.WebviewController.setBlanklessLoadingCacheCapacity(10);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
```

#### set[WebDestroyMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webdestroymode20)20+

set[WebDestroyMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webdestroymode20)(mode: WebDestroyMode): void

设置Web组件的销毁模式。当Web组件销毁时，销毁模式会影响Web内核资源释放的时机，例如JavaScript运行上下文、渲染上下文等。默认值：[WebDestroyMode.NORMAL_MODE](Enums.md#ZH-CN_TOPIC_0000002522241162__webdestroymode20)（普通模式），由系统决定销毁时机。应用可设置[WebDestroyMode.FAST_MODE](Enums.md#ZH-CN_TOPIC_0000002522241162__webdestroymode20)（快速模式），以立即销毁资源，从而提升特定场景的性能。


[WebDestroyMode.FAST_MODE](Enums.md#ZH-CN_TOPIC_0000002522241162__webdestroymode20)（快速模式）会改变Web组件销毁时机，应用需关注依赖Web组件销毁时机的错误实现，例如：Web组件销毁后仍调用WebviewController的未定义行为，与[WebDestroyMode.NORMAL_MODE](Enums.md#ZH-CN_TOPIC_0000002522241162__webdestroymode20)（普通模式）相比，销毁时机提前，有更高的几率触发未关联绑定的异常（17100001），建议应用捕捉异常，或者通过[getAttachState](#ZH-CN_TOPIC_0000002553201117__getattachstate20)方法查询是否绑定状态，来避免稳定性问题。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | WebDestroyMode | 是 | 设置Web组件的销毁模式。 默认值：[WebDestroyMode.NORMAL_MODE](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__webdestroymode20) |

**示例：**

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 设置快速销毁模式
    webview.WebviewController.setWebDestroyMode(webview.WebDestroyMode.FAST_MODE);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
```

#### set[ScrollbarMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__scrollbarmode23)23+

static set[ScrollbarMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__scrollbarmode23)(scrollbarMode: ScrollbarMode): void

在Web页面场景，设置全局滚动条模式。不显式调用时，默认为[ScrollbarMode.OVERLAY_LAYOUT_SCROLLBAR ](Enums.md#ZH-CN_TOPIC_0000002522241162__scrollbarmode23)（非常驻滚动条）。


- 根据滚动条模式，改变当前应用所有web滚动条模式为常驻滚动条或非常驻滚动条。

- 若[forceDisplayScrollBar](属性.md#ZH-CN_TOPIC_0000002553201131__forcedisplayscrollbar14)接口与当前接口同时设置，[forceDisplayScrollBar](../../topics/misc/属性.md#ZH-CN_TOPIC_0000002497605206__forcedisplayscrollbar14)接口设置不生效。

- 该接口需要在WebViewController绑定Web组件之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollbarMode | [ScrollbarMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__scrollbarmode23) | 是 | 滚动条模式。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  aboutToAppear(): void {
    webview.WebviewController.setScrollbarMode(webview.ScrollbarMode.FORCE_DISPLAY_SCROLLBAR);
  }
  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .height('90%')
}
```

加载的html文件。

```ets
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <style>
      body {
        width:2560px;
        height:2560px;
        padding-right:170px;
        padding-left:170px;
        border:5px solid blueviolet;
      }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

#### setActiveWebEngineVersion20+

static setActiveWebEngineVersion(engineVersion: [ArkWebEngineVersion](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__arkwebengineversion20)): void

设置ArkWeb内核版本。若系统不支持指定版本，则设置无效。该接口为全局静态API，须在调用initializeWebEngine前执行，若已加载任何Web组件，则该设置无效。

**遗留内核适配：**

在HarmonyOS 6.0及以后，使用遗留内核时，部分ArkWeb接口不会生效，参考[M114内核在HarmonyOS6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)。


- setActiveWebEngineVersion不支持在异步线程中调用。
- setActiveWebEngineVersion全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| engineVersion | [ArkWebEngineVersion](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__arkwebengineversion20) | 是 | ArkWeb内核版本。 |

**示例：**

本示例以EntryAbility为例，实现了在Ability创建阶段设置ArkWeb内核版本的功能。

```ets
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.setActiveWebEngineVersion(webview.ArkWebEngineVersion.M114)
    if (webview.WebviewController.getActiveWebEngineVersion() == webview.ArkWebEngineVersion.M114) {
      console.info("Active Web Engine Version set to M114")
    }
    console.info("EntryAbility onCreate done")
  }
```

#### getActiveWebEngineVersion20+

static getActiveWebEngineVersion(): [ArkWebEngineVersion](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__arkwebengineversion20)

获取当前ArkWeb内核版本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArkWebEngineVersion](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__arkwebengineversion20) | 返回由ArkWebEngineVersion所定义的当前使用的ArkWeb内核版本。 |

**示例：**

请参考[setActiveWebEngineVersion](#ZH-CN_TOPIC_0000002553201117__setactivewebengineversion20)。

**isActiveWebEngineEvergreen23+**

static isActiveWebEngineEvergreen(): boolean

判断当前系统是否正在使用常青内核，即系统的最新内核。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否正在使用常青内核。正在使用返回true，否则返回false。 |

示例：

本示例以EntryAbility为例，实现了在Ability创建阶段判断应用是否正在使用常青内核的功能。

```ets
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    if (webview.WebviewController.isActiveWebEngineEvergreen()) {
      console.info("Active Web Engine is Evergreen")
    }
    console.info("EntryAbility onCreate done")
  }
```

#### setAutoPreconnect21+

static setAutoPreconnect(enabled: boolean): void

设置Web内核的自动预连接状态。若未设置，默认启用自动预连接。

需要在[initializeWebEngine()](#ZH-CN_TOPIC_0000002553201117__initializewebengine)初始化内核或者创建Web组件之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用Web内核自动预连接的开关。true表示启用，false表示禁用。 |

**示例：**

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        webview.WebviewController.setAutoPreconnect(false);
        webview.WebviewController.initializeWebEngine();
        AppStorage.setOrCreate("abilityWant", want);
    }
```

#### isAutoPreconnectEnabled21+

static isAutoPreconnectEnabled(): boolean

查询Web内核的自动预连接状态。

如果没有使用[setAutoPreconnect](#ZH-CN_TOPIC_0000002553201117__setautopreconnect21)设置Web内核自动预连接的状态，则默认启用自动预连接，返回true。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Web内核是否启用了自动预连接。true表示已启用；false表示已禁用。 |

**示例：**

```ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  build() {
    Column() {
      Button('isAutoPreconnectEnabled')
        .onClick(() => {
          try {
            let isEnabled: boolean = webview.WebviewController.isAutoPreconnectEnabled();
            console.info("isAutoPreconnectEnabled:", isEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
    }
```

#### get[SiteIsolationMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__siteisolationmode21)21+

static get[SiteIsolationMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__siteisolationmode21)(): SiteIsolationMode

查询当前生效的站点隔离模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SiteIsolationMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__siteisolationmode21) | 站点隔离模式类型。 getSiteIsolationMode()查询当前生效的站点隔离模式。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getSiteIsolationMode')
        .onClick(() => {
          let mode = webview.WebviewController.getSiteIsolationMode();
          console.info("getSiteIsolationMode: " + mode);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### set[SiteIsolationMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__siteisolationmode21)21+

set[SiteIsolationMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__siteisolationmode21)(mode: SiteIsolationMode): void

设置站点隔离模式。站点隔离机制将不同源的网站隔离在不同的Render进程中，减少跨域攻击面。例如：PC等设备上，在未启用站点隔离模式时，原有进程模型是每一个Tab对应一个Render进程，开启站点隔离后，一个Tab下不同源的Iframe可在独立的Render进程中运行。

对于仅加载可信网页的第三方应用，可以关闭此功能，以提升性能并减少内存占用，同时减少跨域访问的拦截。默认值根据不同的设备而定，PC/Table采用严格站点隔离[SiteIsolationMode.STRICT](Enums.md#ZH-CN_TOPIC_0000002522241162__siteisolationmode21)，Phone默认部分站点隔离[SiteIsolationMode.PARTIAL](Enums.md#ZH-CN_TOPIC_0000002522241162__siteisolationmode21)。[坚盾守护模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-secure-shield-mode)下采用严格站点隔离。


不能在单子进程模式下设置严格站点隔离。

接口只能在初始化时调用一次，不支持反复修改。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SiteIsolationMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__siteisolationmode21) | 是 | 设置站点隔离模式。 默认值取决于设备类型和设备模式：PC/Tablet默认严格站点隔离，Phone默认部分站点隔离；坚盾守护模式默认严格站点隔离。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. Possible causes: 1. Site Isolation mode is already set by the developer. 2. Site Isolation mode cannot be strict in single-render-process mode. 3. Site Isolation mode cannot be changed while Secure Shield mode is active. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setSiteIsolationMode')
        .onClick(() => {
          try {
            webview.WebviewController.setSiteIsolationMode(webview.SiteIsolationMode.PARTIAL);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### setSocketIdleTimeout21+

static setSocketIdleTimeout(timeout: number): void

设置ArkWeb中已使用过的空闲socket的超时时间，即已使用过的socket可以处于空闲状态的最大时长。如果设置的值与已存在的空闲socket超时时间不同，则根据新的值对已存在的空闲socket进行清理。

未使用该接口设置空闲socket的超时时间时，ArkWeb的默认值为300s。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | ArkWeb中已经使用过的空闲socket的超时时间。 取值范围：[30,300]，单位：s。 小于30时生效值为30，大于300时生效值为300。 |

**示例：**

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        webview.WebviewController.setSocketIdleTimeout(200);
        AppStorage.setOrCreate("abilityWant", want);
    }
```

#### setSoftKeyboardBehaviorMode22+

setSoftKeyboardBehaviorMode(mode: [WebSoftKeyboardBehaviorMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__websoftkeyboardbehaviormode22)): void

设置软键盘自动控制模式，当接口没有显式调用时，Web组件失去焦点或获得焦点、状态切换为inactive或active时，系统均会尝试触发软键盘自动隐藏或拉起。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebSoftKeyboardBehaviorMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445167__websoftkeyboardbehaviormode22) | 是 | Web软键盘自动控制模式。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```ets
// index.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('Web InActive').onClick(() => {
        this.controller.setSoftKeyboardBehaviorMode(webview.WebSoftKeyboardBehaviorMode.DISABLE_AUTO_KEYBOARD_ON_ACTIVE);
      })
      Web({ src: 'www.example.com', controller: this.controller })
        .keyboardAvoidMode(WebKeyboardAvoidMode.RETURN_TO_UICONTEXT)
    }
```

**resumeMicrophone23+**

resumeMicrophone(): void

恢复当前网页麦克风捕获。使用麦克风功能前请在module.json5中添加权限: ohos.permission.MICROPHONE，具体权限的添加方法请参考[在配置文件中声明权限](../../guides/声明权限.md#在配置文件中声明权限)。

系统能力： SystemCapability.Web.Webview.Core

错误码：

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

示例：

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.MICROPHONE'], (err: BusinessError, data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
  }

  build() {
    Column() {
      Button("resumeMicrophone").onClick(() => {
        try {
          this.controller.resumeMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
      })
      Button("pauseMicrophone").onClick(() => {
        try {
          this.controller.pauseMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("stopMicrophone").onClick(() => {
        try {
          this.controller.stopMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
        })
        .onMicrophoneCaptureStateChange((event: MicrophoneCaptureStateChangeInfo) => {
          console.info("MicrophoneCapture from ", event.originalState, " to ", event.newState);
        })
    }
```

加载的html文件。

```ets
<!-- index.html -->
<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
 </head>
 <body>
   <video id="video" width="400px" height="400px" autoplay="autoplay">
   </video>
   <input type="button" title="HTML5麦克风" value="开启麦克风" onclick="getMedia()" />
   <script>
     function getMedia() {
       let constraints = {
         video: {
           width: 500,
           height: 500
         },
         audio: true
       }
       let video = document.getElementById("video");
       let promise = navigator.mediaDevices.getUserMedia(constraints);
       promise.then(function(MediaStream) {
         video.srcObject = MediaStream;
         video.play();
       })
     }
   </script>
 </body>
</html>
```

**pauseMicrophone23+**

pauseMicrophone(): void

暂停当前网页麦克风捕获。

系统能力： SystemCapability.Web.Webview.Core

错误码：

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

示例：

完整示例代码参考[resumeMicrophone](#ZH-CN_TOPIC_0000002553201117__resumemicrophone23)。

**stopMicrophone23+**

stopMicrophone(): void

停止当前网页麦克风捕获。

系统能力： SystemCapability.Web.Webview.Core

错误码：

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

示例：

完整示例代码参考[resumeMicrophone](#ZH-CN_TOPIC_0000002553201117__resumemicrophone23)。