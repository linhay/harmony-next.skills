# Class (SslErrorHandler)

Web组件返回的SSL错误通知事件的处理对象。示例代码参考[onSslErrorEvent](事件.md#ZH-CN_TOPIC_0000002522081170__onsslerrorevent12)事件。


-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准。

#### constructor9+

constructor()

SslErrorHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleCancel9+

handleCancel(): void

通知Web组件取消此请求。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleConfirm9+

handleConfirm(): void

通知Web组件继续使用SSL证书。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleCancel20+

handleCancel(abortLoading: boolean): void

通知Web组件取消此请求，并根据参数abortLoading决定是否停止加载。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abortLoading | boolean | 是 | 是否在取消请求后停止加载页面。 true表示停止加载页面，false表示继续加载页面。 默认值为false。 |