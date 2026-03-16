# Class (PermissionRequest)

Web组件返回授权或拒绝权限功能的对象。示例代码参考[onPermissionRequest事件](../../topics/misc/事件.md#ZH-CN_TOPIC_0000002497445228__onpermissionrequest9)。

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### constructor9+

constructor()

PermissionRequest的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### deny9+

deny(): void

拒绝网页所请求的权限。

**系统能力：** SystemCapability.Web.Webview.Core

#### getOrigin9+

getOrigin(): string

获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string当前请求权限网页的来源。

#### getAccessibleResource9+

getAccessibleResource(): Array<string>

获取网页所请求的权限资源列表，资源列表类型参考[ProtectedResourceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497605218__protectedresourcetype9)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<string>网页所请求的权限资源列表。

#### grant9+

grant(resources: Array<string>): void

对网页访问的给定权限进行授权。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明resourcesArray<string>是授予网页请求的权限的资源列表。