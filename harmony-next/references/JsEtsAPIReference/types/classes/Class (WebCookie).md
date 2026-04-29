# Class (WebCookie)

通过WebCookie可以控制Web组件中的cookie的各种行为，其中每个应用中的所有Web组件共享一个WebCookie。通过controller方法中的getCookieManager方法可以获取WebCookie对象，进行后续的cookie管理操作。

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 8开始支持。

-

从API version 8开始支持，从API version 23开始不再维护，建议使用[WebCookieManager](Class (WebCookieManager).md)代替。

-

示例效果请以真机运行为准。

**constructor(deprecated)**

constructor()

WebCookie的构造函数。


从API version 8开始支持，从API version 23开始废弃。且不再提供新的接口作为替代。

**系统能力：** SystemCapability.Web.Webview.Core

#### setCookie(deprecated)

setCookie()

设置cookie，该方法为同步方法。设置成功返回true，否则返回false。


从API version 8开始支持，从API version 9开始废弃，建议使用[setCookie9+](Class (WebCookieManager).md#ZH-CN_TOPIC_0000002522081156__setcookiedeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core

#### saveCookie(deprecated)

saveCookie()

将当前存在内存中的cookie同步到磁盘中，该方法为同步方法。


从API version 8开始支持，从API version 9开始废弃，建议使用[saveCookieAsync9+](Class (WebCookieManager).md#ZH-CN_TOPIC_0000002522081156__savecookieasync)代替。

**系统能力：** SystemCapability.Web.Webview.Core