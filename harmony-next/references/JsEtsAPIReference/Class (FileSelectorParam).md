# Class (FileSelectorParam)

Web组件获取文件对象。示例代码参考[onShowFileSelector事件](事件.md#ZH-CN_TOPIC_0000002497445228__onshowfileselector9)。

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### constructor9+

constructor()

FileSelectorParam的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getTitle9+

getTitle(): string

获取文件选择器标题。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string返回文件选择器标题。

#### getMode9+

getMode(): FileSelectorMode

获取文件选择器的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明[FileSelectorMode](Enums.md#ZH-CN_TOPIC_0000002497605218__fileselectormode9)返回文件选择器的模式。

#### getAcceptType9+

getAcceptType(): Array<string>

获取文件过滤类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<string>返回文件过滤类型。

#### isCapture9+

isCapture(): boolean

获取是否调用多媒体能力。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明boolean

返回是否调用多媒体能力。

true表示返回调用多媒体能力，false表示返回未调用多媒体能力。

#### getMimeTypes18+

getMimeTypes(): Array<string>

获取文件MIME类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<string>返回文件MIME类型。