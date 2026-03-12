# Class (WebResourceError)

Web组件资源管理错误信息对象。示例代码参考[onErrorReceive事件](事件.md#ZH-CN_TOPIC_0000002497445228__onerrorreceive)。

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 8开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### constructor

constructor()

WebResourceError的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getErrorCode

getErrorCode(): number

获取加载资源的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明number返回加载资源的错误码。错误码的含义可以参考[WebNetErrorList](@ohos.web.netErrorList (ArkWeb网络协议栈错误列表).md)

#### getErrorInfo

getErrorInfo(): string

获取加载资源的错误信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string返回加载资源的错误信息。