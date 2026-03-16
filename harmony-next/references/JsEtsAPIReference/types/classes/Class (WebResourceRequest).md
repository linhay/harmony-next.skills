# Class (WebResourceRequest)

Web组件获取资源请求对象。示例代码参考[onErrorReceive事件](../../topics/misc/事件.md#ZH-CN_TOPIC_0000002497445228__onerrorreceive)。

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 8开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### constructor

constructor()

WebResourceRequest的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getRequestHeader

getRequestHeader(): Array<Header>

获取资源请求头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<[Header](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__header)>返回资源请求头信息。

#### getRequestUrl

getRequestUrl(): string

获取资源请求的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string返回资源请求的URL信息。

#### isMainFrame

isMainFrame(): boolean

判断资源请求是否为主frame。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明boolean

返回资源请求是否为主frame。

true表示返回资源请求为主frame，false表示返回资源请求不为主frame。

#### isRedirect

isRedirect(): boolean

判断资源请求是否被服务端重定向。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明boolean

返回资源请求是否被服务端重定向。

true表示返回资源请求被服务端重定向，false表示返回资源请求未被服务端重定向。

#### isRequestGesture

isRequestGesture(): boolean

获取资源请求是否与手势（如点击）相关联。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明boolean

返回资源请求是否与手势（如点击）相关联。

true表示返回资源请求与手势（如点击）相关联，false表示返回资源请求与手势（如点击）不相关联。

#### getRequestMethod9+

getRequestMethod(): string

获取请求方法。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string返回请求方法。