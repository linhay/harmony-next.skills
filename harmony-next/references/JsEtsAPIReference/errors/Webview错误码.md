# Webview错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 17100001 WebviewController没有和具体的Web组件关联

**错误信息**

Init error. The WebviewController must be associated with a Web component.

**错误描述**

WebviewController还没有和具体的Web组件关联，无法进行相应的操作。

**处理步骤**

请检查WebviewController对象是否已与Web组件关联，可以通过[onControllerAttached()](../topics/misc/事件.md#ZH-CN_TOPIC_0000002497445228__oncontrollerattached10)接口进行检查。详情可以参考[Web组件调用WebviewController相关接口报17100001错误定位指南](https://developer.huawei.com/consumer/cn/doc/architecture-guides/educate-v1_1-ts_18-0000002334531357)。

#### 17100002 Url格式错误

**错误信息**

URL error. Possible causes: 1. No valid cookie found for the specified URL. 2. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024.

**错误描述**

URL错误，可能原因：

1.

未找到指定URL的有效Cookie。

1.

该URL对应的网页无效，或URL长度超过2*1024*1024。

**处理步骤**

请检查输入的url是否正确且url长度不超过2*1024*1024。

#### 17100003 resource路径错误

**错误信息**

Invalid resource path or file type.

**错误描述**

resource路径错误。

**可能原因**

资源路径下文件不存在或无法访问。

**处理步骤**

请检查输入的resource路径是否正确。

#### 17100004 功能开关未打开

**错误信息**

Function not enabled.

**错误描述**

功能开关未打开。

**处理步骤**

请检查相关功能开关是否已配置打开，如该功能对应的XXXAccess是否配置为true。

#### 17100005 cookie value格式错误

**错误信息**

The provided cookie value is invalid. It must follow the format specified in RFC 6265.

**错误描述**

cookie value格式错误。

**可能原因**

不支持的cookie value类型。

**处理步骤**

请检查输入的value是否正确。

#### 17100006 无法注册message port回调

**错误信息**

Failed to register a message event for the port.

**错误描述**

无法注册message port回调。

**可能原因**

port可能已经关闭。

**处理步骤**

请检查port是否关闭。

#### 17100008 删除不存在的javaScriptProxy

**错误信息**

Failed to delete JavaScriptProxy because it does not exist.

**错误描述**

删除不存在的javaScriptProxy。

**可能原因**

传入的javaScriptProxy之前没有注册。

**处理步骤**

检查传入的javaScriptProxy是否注册成功。

#### 17100010 无法使用该端口发送消息

**错误信息**

Failed to post messages through the port.

**错误描述**

无法使用该端口发送消息。

**可能原因**

该端口已关闭，或者对端端口已关闭。

**处理步骤**

1.

请确认本端端口是否调用了close接口。

1.

请确认本端是否设置了port的onMessageEvent回调。

#### 17100011 输入参数origin错误

**错误信息**

Invalid origin.The origin format must follow defined in RFC 6454.

**错误描述**

输入参数origin错误。origin格式必须遵循RFC 6454中定义的格式。

**可能原因**

1.

参数origin为空。

1.

参数origin不合法。

**处理步骤**

检查输入的参数。

#### 17100012 无可获取的webstorage源

**错误信息**

Invalid web storage origin.

**错误描述**

无可获取的webstorage源。

**可能原因**

没有使用相关的JS数据库API。

**处理步骤**

1.

检查是否有使用JS数据库API。

1.

如果已经使用，检查调用失败原因，如databaseAccess开关是否打开。

#### 17100013 预连接时，输入socket数目无效

**错误信息**

The number of sockets to be preconnected is invalid.

**错误描述**

预连接时，输入socket的数目是无效的。

**可能原因**

预连接时，输入socket的数目小于等于0，或者大于6。

**处理步骤**

检查输入的socket的数目范围是否大于0且小于等于6。

#### 17100014 类型和值不匹配

**错误信息**

The type and value of the message do not match.

**错误描述**

消息的类型和值不匹配。

**可能原因**

获取消息的值和消息本身的类型不匹配。

**处理步骤**

需要根据消息的类型调用相应的接口来获取消息的值。举例：如获取到的类型是BOOLEAN，则需要调用GetBoolean接口来获取布尔值。

#### 17100016 下载任务没有处于暂停状态

**错误信息**

The download task is not paused.

**错误描述**

下载任务没有处于暂停状态。

**可能原因**

在下载没有暂停的情况下调用了WebDownloadItem.resume。

**处理步骤**

下载并没有被暂停，不需要恢复。

#### 17100018 没有设置一个委托类来接收下载状态

**错误信息**

No WebDownloadDelegate has been set yet.

**错误描述**

没有设置一个委托类来接收下载状态。

**可能原因**

没有设置委托类就调用了WebDownloadManager.resumeDownload。

**处理步骤**

先通过WebDownloadManager.setDownloadDelegate设置一个委托类。

#### 17100019 下载还没开始

**错误信息**

The download task is not started yet.

**错误描述**

下载任务还未开始。

**可能原因**

下载任务还没开始，此时调用pause/resume是无效的。

**处理步骤**

需要在WebDownloadDelegate.onBeforeDownload中调用start('xxx')并指定下载路径。

#### 17100020 注册自定义协议失败

**错误信息**

Failed to register custom schemes.

**错误描述**

注册自定义协议失败。

**可能原因**

在ArkWeb引擎初始化之后才设置自定义协议。

**处理步骤**

注册自定义协议需要在ArkWeb引擎初始化之前设置。

#### 17100021 WebResourceHandler已经失效

**错误信息**

The resource handler is invalid.

**错误描述**

WebResourceHandler已经失效。

**可能原因**

1.对应的请求在WebSchemeHandler中没有拦截；

2.该请求拦截在构造返回体之前，因为某些原因已经请求结束；

3.该WebResourceHandler已经调用过didFinish和didFail。

**处理步骤**

请勿在以上所说的情况下调用WebResourceHandler的接口。

#### 17100022 WebHttpBodyStream初始化失败

**错误信息**

Failed to initialize the HTTP body stream.

**错误描述**

WebHttpBodyStream数据初始化失败。

**可能原因**

发起的POST等类型的请求中，携带的数据不合法。例如里面数据流中有文件类型的数据，但是该文件路径不存在，则数据流初始化失败。

**处理步骤**

检查发起的POST等类型的请求中，携带的数据是否合法。

#### 17100023 使用了不被允许的端口号

**错误信息**

The port number is not within the allowed range.

**错误描述**

使用的端口号不在允许的取值范围内。

**可能原因**

由于部分端口号（例如小于1024的端口号）作为熟知或系统端口，在操作系统上需要特权才能开启，因此禁止应用使用这些端口号。

**处理步骤**

检查使用的端口号是否在允许的取值范围内。

#### 17100101 使用了错误的网络错误码

**错误信息**

The errorCode is either ARKWEB_NET_OK or outside the range of error codes in WebNetErrorList.

**错误描述**

网络错误码为ARKWEB_NET_OK或者超出了WebNetErrorList中的错误码范围。

**可能原因**

使用的错误码不在[WebNetErrorList](../modules/ohos/@ohos.web.netErrorList (ArkWeb网络协议栈错误列表).md#ZH-CN_TOPIC_0000002497445224__webneterrorlist)范围内，或者调用didFail接口时使用了NET_OK错误码。

**处理步骤**

检查使用的错误码是否在[WebNetErrorList](../modules/ohos/@ohos.web.netErrorList (ArkWeb网络协议栈错误列表).md#ZH-CN_TOPIC_0000002497445224__webneterrorlist)范围内，或者调用difFail时是否使用了NET_OK错误码。