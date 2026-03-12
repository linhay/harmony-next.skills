# Interfaces（其他）

-

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### WebOptions

通过[接口](组件描述.md#ZH-CN_TOPIC_0000002529445171__接口)定义Web选项。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明srcstring | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否

网页资源地址。如果访问本地资源文件，请使用$rawfile或者resource协议。如果加载应用包外沙箱路径的本地资源文件(文件支持html和txt类型)，请使用file://沙箱文件路径。

src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过[loadUrl()](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__loadurl)重新加载。

controller[WebController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontroller) | [WebviewController9+](zh-cn_topic_0000002497445240.md#ZH-CN_TOPIC_0000002497445240__webviewcontroller9)否否控制器，通过controller可以控制Web组件各种行为（包括页面导航、声明周期状态、JavaScript交互等行为）。从API version 9开始，WebController不再维护，建议使用WebviewController替代。renderMode12+[RenderMode](Enums.md#ZH-CN_TOPIC_0000002497605218__rendermode12)否是表示当前Web组件的渲染方式，RenderMode.ASYNC_RENDER表示Web组件异步渲染，RenderMode.SYNC_RENDER表示支持Web组件同步渲染能力，默认值RenderMode.ASYNC_RENDER，该模式不支持动态调整。incognitoMode11+boolean否是

表示当前创建的webview是否是隐私模式。true表示创建隐私模式的webview，false表示创建正常模式的webview。

默认值：false。

传入undefined或null时为false。

sharedRenderProcessToken12+string否是

表示当前Web组件指定共享渲染进程的token，多渲染进程模式下，相同token的Web组件会优先尝试复用与token相绑定的渲染进程。token与渲染进程的绑定发生在渲染进程的初始化阶段。当渲染进程没有关联的Web组件时，其与token绑定关系将被移除。

默认值： ""。

emulateTouchFromMouseEvent22+boolean否是

设定鼠标事件是否被转换成touch事件。

默认值：false。

#### WebMediaOptions10+

Web媒体策略的配置。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明resumeIntervalnumber否是

被其他应用暂停的Web音视频能够自动续播的有效期，单位：秒。取值范围：[-2147483648, 2147483647]。resumeInterval值为0时，不自动续播；大于0时，将在该时间内尝试续播；小于0时，将在无限时间内尝试续播。由于近似值原因，该有效期可能存在一秒内的误差。

**说明：**

HLS视频被打断后，回到前台将自动续播，不受该时间控制。

audioExclusiveboolean否是

应用内多个Web实例的音频是否独占。

true表示应用内多个Web实例的音频独占，false表示应用内多个Web实例的音频不独占。

默认值:true。

audioSessionType20+[AudioSessionType](Enums.md#ZH-CN_TOPIC_0000002497605218__audiosessiontype20)否是应用中Web音频类型。默认值对应[系统音频流类型](Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)STREAM_USAGE_MUSIC。设置该参数会改变组件音频类型与系统音频类型映射关系，进而影响ArkWeb音频焦点策略。

#### ScriptItem11+

通过[javaScriptOnDocumentStart](属性.md#ZH-CN_TOPIC_0000002497605206__javascriptondocumentstart11)属性注入到Web组件的ScriptItem对象。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明scriptstring否否需要注入、执行的JavaScript脚本。scriptRulesArray<string>否否

一组允许来源的匹配规则。

1.如果需要允许所有来源的网址，使用通配符“ * ”。

2.如果需要精确匹配，则描述网站地址，如"https://www.example.com"。

3.如果模糊匹配网址，可以使用“ * ”通配符替代，如"https://*.example.com"。不允许使用"x. * .y.com"、" * foobar.com"等。

4.如果来源是ip地址，则使用规则2。

5.对于http/https以外的协议(自定义协议)，不支持使用精确匹配和模糊匹配，且必须以://结尾，例如"resource://"。

6.一组scriptRule中，如果其中一条不满足以上规则，则整组scriptRule都不生效。

#### NestedScrollOptionsExt14+

通过NestedScrollOptionsExt可以设置上下左右四个方向的嵌套滚动规则。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明scrollUp[NestedScrollMode](枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10)否是

可滚动组件往上滚动时的嵌套滚动选项。

默认值：NestedScrollMode.SELF_FIRST。

scrollDown[NestedScrollMode](枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10)否是

可滚动组件往下滚动时的嵌套滚动选项。

默认值：NestedScrollMode.SELF_FIRST。

scrollLeft[NestedScrollMode](枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10)否是

可滚动组件往左滚动时的嵌套滚动选项。

默认值：NestedScrollMode.SELF_FIRST。

scrollRight[NestedScrollMode](枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10)否是

可滚动组件往右滚动时的嵌套滚动选项。

默认值：NestedScrollMode.SELF_FIRST。

#### NativeMediaPlayerConfig12+

用于[开启应用接管网页媒体播放功能](属性.md#ZH-CN_TOPIC_0000002497605206__enablenativemediaplayer12)的配置信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明enableboolean否否

是否开启应用接管网页媒体播放功能。

true表示开启应用接管网页媒体播放功能，false表示关闭应用接管网页媒体播放功能。

默认值：false。

shouldOverlayboolean否否

开启应用接管网页媒体播放功能后，应用接管网页视频的播放器画面是否覆盖网页内容。

true表示改变视频图层的高度，使其覆盖网页内容。false表示不覆盖网页内容，跟原视频图层高度一样，嵌入在网页中。

默认值：false。

#### ExpandedMenuItemOptions(deprecated)

从API version 12开始支持，从API version 20开始废弃，建议使用[editMenuOptions](属性.md#ZH-CN_TOPIC_0000002497605206__editmenuoptions12)替代。

自定义菜单扩展项。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明content[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否显示内容。startIcon[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是显示图标。默认值为空，不显示图标。action(selectedText: {plainText: string}) => void否否选中的文本信息。

#### AdsBlockedDetails12+

发生广告拦截时，广告资源信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否发生广告过滤的页面url。adsBlockedArray<string>否否被过滤的资源的url或dompath标识，被过滤的多个对象url相同则可能出现重复元素。

#### SelectionMenuOptionsExt13+

自定义菜单扩展项。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明onAppearCallback<void>否是自定义选择菜单弹出时回调。onDisappearCallback<void>否是自定义选择菜单关闭时回调。preview[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否是自定义选择菜单的预览内容样式，未配置时无预览内容。menuType[MenuType](文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__menutype13枚举说明)否是

自定义选择菜单类型。

默认值：MenuType.SELECTION_MENU。

从API version 20起，MenuType.PREVIEW_MENU支持超链接预览。

previewMenuOptions20+[PreviewMenuOptions](#ZH-CN_TOPIC_0000002529445183__previewmenuoptions20)否是自定义选择预览菜单选项。onMenuShow21+Callback<void>否是自定义选择菜单显示时回调。onMenuHide21+Callback<void>否是自定义选择菜单隐藏时回调。

#### PreviewMenuOptions20+

预览菜单选项。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明hapticFeedbackMode[HapticFeedbackMode](菜单控制.md#ZH-CN_TOPIC_0000002497604848__hapticfeedbackmode18)否是

菜单弹出时振动效果。需配置"ohos.permission.VIBRATE"权限

默认值：HapticFeedbackMode.DISABLED，菜单弹出时不振动。

#### EmbedOptions16+

Web同层渲染的配置。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明supportDefaultIntrinsicSizeboolean否是

设置同层渲染元素是否支持固定大小 300 * 150。

当H5侧CSS设置了大小时，同层渲染元素大小为CSS大小，否则为固定大小。

为true时，固定大小为 300 * 150。

为false时，若H5侧CSS未设置大小，则同层渲染元素不渲染。

默认值：false

单位：px

supportCssDisplayChange20+boolean否是

设置同层渲染可见性接口是否支持显示属性。

同层渲染可见性接口默认支持同层标签相对于视口的可见状态。

设置为true时，支持显示CSS属性，包括visibility、display和宽高。

设置为false时，不支持显示CSS属性，仅支持同层标签相对于视口的可见性。

#### OnAlertEvent12+

定义网页触发 alert() 告警时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否当前显示弹窗的网页的URL。messagestring否否显示在弹窗中的信息。result[JsResult](Class (JsResult).md)否否通知Web组件用户的操作结果。

#### OnBeforeUnloadEvent12+

定义刷新或关闭场景下，在即将离开当前页面时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否当前显示弹窗所在网页的URL。messagestring否否弹窗中显示的信息。result[JsResult](Class (JsResult).md)否否通知Web组件用户操作行为。isReload20+boolean否是

页面是否刷新。

当页面因刷新即将离开时，isReload参数被设置为true；当页面因关闭即将离开时，isReload参数被设置为false。

默认值：false。

#### OnConfirmEvent12+

定义网页触发 confirm() 弹窗时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否当前显示弹窗的网页的URL。messagestring否否显示在弹窗中的信息。result[JsResult](Class (JsResult).md)否否通知Web组件用户的操作结果。

#### OnPromptEvent12+

定义网页触发 prompt() 弹窗时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否当前显示弹窗的网页的URL。messagestring否否显示在弹窗中的信息。valuestring否否对话框默认返回的信息。result[JsResult](Class (JsResult).md)否否通知Web组件用户的操作结果。

#### OnConsoleEvent12+

定义通知宿主应用JavaScript console消息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明message[ConsoleMessage](Class (ConsoleMessage).md)否否触发的控制台信息。

#### OnErrorReceiveEvent12+

定义网页加载遇到错误时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明request[WebResourceRequest](Class (WebResourceRequest).md)否否网页请求的封装信息。error[WebResourceError](Class (WebResourceError).md)否否网页加载资源错误的封装信息 。

#### OnHttpErrorReceiveEvent12+

定义网页收到加载资源加载HTTP错误时触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明request[WebResourceRequest](Class (WebResourceRequest).md)否否网页请求的封装信息。response[WebResourceResponse](Class (WebResourceResponse).md)否否资源响应的封装信息。

#### OnDownloadStartEvent12+

定义通知主应用开始下载一个文件。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否文件下载的URL。userAgentstring否否用于下载的用户代理。contentDispositionstring否否服务器返回的 Content-Disposition响应头，服务器可能返回空。mimetypestring否否服务器返回内容媒体类型（MIME）信息。contentLengthnumber否否服务器返回文件的长度。

#### OnRefreshAccessedHistoryEvent12+

定义导航完成时触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否访问的url。isRefreshedboolean否否true表示该页面是被重新加载的（调用[refresh9+](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__refresh)接口），false表示该页面是新加载的。isMainFrame22+boolean否是

是否是主文档触发。

true表示是主文档触发，false表示不是主文档触发。

#### OnRenderExitedEvent12+

定义渲染过程退出时触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明renderExitReason[RenderExitReason](Enums.md#ZH-CN_TOPIC_0000002497605218__renderexitreason9)否否渲染进程异常退出的具体原因。

#### OnShowFileSelectorEvent12+

定义文件选择器结果。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明result[FileSelectorResult](Class (FileSelectorResult).md)否否用于通知Web组件文件选择的结果。fileSelector[FileSelectorParam](Class (FileSelectorParam).md)否否文件选择器的相关信息。

#### OnResourceLoadEvent12+

定义加载url时触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否所加载的资源文件url信息。

#### OnScaleChangeEvent12+

定义当前页面显示比例的变化时触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明oldScalenumber否否变化前的显示比例百分比。newScalenumber否否变化后的显示比例百分比。

#### OnHttpAuthRequestEvent12+

定义通知收到http auth认证请求。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[HttpAuthHandler](Class (HttpAuthHandler).md)否否通知Web组件用户操作行为。hoststring否否HTTP身份验证凭据应用的主机。realmstring否否HTTP身份验证凭据应用的域。

#### OnInterceptRequestEvent12+

定义当Web组件加载url之前触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明request[WebResourceRequest](Class (WebResourceRequest).md)否否url请求的相关信息。

#### OnPermissionRequestEvent12+

定义通知收到获取权限请求。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明request[PermissionRequest](Class (PermissionRequest).md)否否通知Web组件用户操作行为。

#### OnScreenCaptureRequestEvent12+

定义通知收到屏幕捕获请求。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[ScreenCaptureHandler](Class (ScreenCaptureHandler).md)否否通知Web组件用户操作行为。

#### OnContextMenuShowEvent12+

定义调用时触发的回调，以允许自定义显示上下文菜单。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明param[WebContextMenuParam](Class (WebContextMenuParam).md)否否菜单相关参数。result[WebContextMenuResult](Class (WebContextMenuResult).md)否否菜单相应事件传入内核。

#### OnSearchResultReceiveEvent12+

定义通知调用方网页页内查找的结果。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明activeMatchOrdinalnumber否否当前匹配的查找项的序号（从0开始）。numberOfMatchesnumber否否所有匹配到的关键词的个数。isDoneCountingboolean否否

当次页内查找操作是否结束。

true表示当次页内查找操作结束，false表示当次页内查找操作未结束。

该方法可能会回调多次，直到isDoneCounting为true为止。

#### OnScrollEvent12+

定义滚动条滑动到指定位置时触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明xOffsetnumber否否

以网页最左端为基准，水平滚动条滚动所在位置。

单位：vp。

yOffsetnumber否否

以网页最上端为基准，竖直滚动条滚动所在位置。

单位：vp。

#### OnSslErrorEventReceiveEvent12+

定义网页收到SSL错误时触发。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[SslErrorHandler](Class (SslErrorHandler).md)否否通知Web组件用户操作行为。error[SslError](Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9)否否错误码。certChainData15+Array<Uint8Array>否是证书链数据。

#### SslErrorEvent12+

用户加载资源时发生SSL错误时触发的回调详情。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[SslErrorHandler](Class (SslErrorHandler).md)否否通知Web组件用户操作行为。error[SslError](Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9)否否错误码。urlstring否否url地址。originalUrlstring否否请求的原始url地址。referrerstring否否referrer url地址。isFatalErrorboolean否否

是否是致命错误。

true表示致命错误，false表示非致命错误。

isMainFrameboolean否否

是否是主资源。

true表示主资源，false表示非主资源。

certChainData20+Array<Uint8Array>否是证书链数据。

#### OnClientAuthenticationEvent12+

定义当需要用户提供SSL客户端证书时触发回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[ClientAuthenticationHandler](Class (ClientAuthenticationHandler).md)否否通知Web组件用户操作行为。hoststring否否请求证书服务器的主机名。portnumber否否请求证书服务器的端口号。keyTypesArray<string>否否可接受的非对称秘钥类型。issuersArray<string>否否与私钥匹配的证书可接受颁发者。

#### VerifyPinEvent22+

定义当需要用户进行PIN码认证时触发回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[VerifyPinHandler](Class (VerifyPinHandler).md)否否通知Web组件用户操作行为。identitystring否否用于认证的证书凭据标识。

#### OnWindowNewEvent12+

定义网页要求用户创建窗口时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明isAlertboolean否否true代表请求创建对话框，false代表新标签页。isUserTriggerboolean否否true代表用户触发，false代表非用户触发。targetUrlstring否否目标url。handler[ControllerHandler](Class (ControllerHandler).md)否否用于设置新建窗口的WebviewController实例。

#### OnTouchIconUrlReceivedEvent12+

定义设置接收到apple-touch-icon url地址时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否接收到的apple-touch-icon url地址。precomposedboolean否否

对应apple-touch-icon是否为预合成。

true表示对应apple-touch-icon为预合成，false表示对应apple-touch-icon不是预合成。

#### OnFaviconReceivedEvent12+

定义应用为当前页面接收到新的favicon时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明favicon[PixelMap](Interface (PixelMap).md)否否接收到的favicon图标的PixelMap对象。

#### OnPageVisibleEvent12+

定义旧页面不再呈现，新页面即将可见时触发的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否旧页面不再呈现，新页面即将可见时新页面的url地址。

#### OnDataResubmittedEvent12+

定义网页表单可以重新提交时触发的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[DataResubmissionHandler](Class (DataResubmissionHandler).md)否否表单数据重新提交句柄。

#### OnAudioStateChangedEvent12+

定义网页上的音频播放状态发生改变时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明playingboolean否否当前页面的音频播放状态，true表示正在播放，false表示未播放。

#### OnFirstContentfulPaintEvent12+

定义网页首次内容绘制回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明navigationStartTicknumber否否启动页面加载开始的时间，单位以微秒表示。firstContentfulPaintMsnumber否否从启动页面加载开始到第一次绘制内容的时间，单位是以毫秒表示。

#### OnLoadInterceptEvent12+

定义截获资源加载时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明data[WebResourceRequest](Class (WebResourceRequest).md)否否url请求的相关信息。

#### OnOverScrollEvent12+

定义网页过度滚动时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明xOffsetnumber否否

以网页最左端为基准，水平过度滚动的偏移量。

单位：vp。

yOffsetnumber否否

以网页最上端为基准，竖直过度滚动的偏移量。

单位：vp。

#### JavaScriptProxy12+

定义要注入的JavaScript对象。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明objectobject否否参与注册的对象。只能声明方法，不能声明属性。namestring否否注册对象的名称，与window中调用的对象名一致。methodListArray<string>否否参与注册的应用侧JavaScript对象的同步方法。controller[WebController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontroller) | [WebviewController9+](zh-cn_topic_0000002497605192.md)否否控制器。从API version 9开始，WebController不再维护，建议使用WebviewController替代。asyncMethodList12+Array<string>否是参与注册的应用侧JavaScript对象的异步方法。异步方法无法获取返回值。permission12+string否是

json字符串，默认为空，通过该字符串配置JSBridge的权限管控，可以定义object、method一级的url白名单。

JavaScriptProxy的permission参数支持resource/http/https协议，不支持file协议。

示例请参考[前端页面调用应用侧函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-page-app-function-invoking)。

#### OnPageEndEvent12+

定义网页加载结束时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否页面的URL地址。

#### OnPageBeginEvent12+

定义网页加载开始时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否页面的URL地址。

#### OnProgressChangeEvent12+

定义网页加载进度变化时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明newProgressnumber否否新的加载进度，取值范围为0到100的整数。

#### OnTitleReceiveEvent12+

定义网页document标题更改时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明titlestring否否document标题内容。isRealTitle20+boolean否是

document标题来源，true表示来自网页的title标签，false表示该title是根据url自动生成。

默认值：false

#### OnGeolocationShowEvent12+

定义通知用户收到地理位置信息获取请求。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明originstring否否指定源的字符串索引。geolocation[JsGeolocation](Class (JsGeolocation).md)否否通知Web组件用户操作行为。

#### NativeEmbedVisibilityInfo12+

提供同层标签的可见性信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明visibilityboolean否否

可见性。

true表示可见，false表示不可见。

embedIdstring否否同层渲染标签的唯一id。

#### RenderProcessNotRespondingData12+

提供渲染进程无响应的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明jsStackstring否否网页的javaScript调用栈信息。pidnumber否否网页的进程id。reason[RenderProcessNotRespondingReason](Enums.md#ZH-CN_TOPIC_0000002497605218__renderprocessnotrespondingreason12)否否触发渲染进程无响应回调的原因。

#### FullScreenEnterEvent12+

Web组件进入全屏回调事件的详情。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明handler[FullScreenExitHandler](Class (FullScreenExitHandler).md)否否用于退出全屏模式的函数句柄。videoWidthnumber否是视频的宽度，单位：px。如果进入全屏的是 <video> 元素，表示其宽度；如果进入全屏的子元素中包含 <video> 元素，表示第一个子视频元素的宽度；其他情况下，为0。videoHeightnumber否是视频的高度，单位：px。如果进入全屏的是 <video> 元素，表示其高度；如果进入全屏的子元素中包含 <video> 元素，表示第一个子视频元素的高度；其他情况下，为0。

#### LoadCommittedDetails11+

提供已提交跳转的网页的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明isMainFrameboolean否否

是否是主文档。

true表示是主文档，false表示不是主文档。

isSameDocumentboolean否否

是否在不更改文档的情况下进行的网页跳转。

true表示在不更改文档的情况下进行的网页跳转，false表示在更改文档的情况下进行的网页跳转。

在同文档跳转的示例：1.参考片段跳转；2.pushState或replaceState触发的跳转；3.同一页面历史跳转。

didReplaceEntryboolean否否

是否提交的新节点替换了已有的节点。

true表示提交的新节点替换了已有的节点，false表示提交的新节点未替换已有的节点。

另外在一些子文档跳转的场景，虽然没有实际替换已有节点，但是有一些属性发生了变更。

navigationType[WebNavigationType](Enums.md#ZH-CN_TOPIC_0000002497605218__webnavigationtype11)否否网页跳转的类型。urlstring否否当前跳转网页的URL。

#### NativeEmbedInfo11+

提供同层标签的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明idstring否是同层标签的id信息。typestring否是同层标签的type信息，统一为小写字符。srcstring否是同层标签的src信息。widthnumber否是同层标签的宽，单位为px。heightnumber否是同层标签的高，单位为px。urlstring否是同层标签的url信息。tag12+string否是标签名，统一为大写字符。params12+Map<string, string>否是object标签包含的param标签键值对列表，该map本质为Object类型，请使用Object提供的方法操作该对象，即embed.info?.param?.["name"]。position12+Position否是同层标签在屏幕坐标系中相对于Web组件的位置信息，此处区别于标准Position，单位为px。

#### NativeEmbedParamItem21+

提供同层渲染object标签内嵌param元素的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明status[NativeEmbedParamStatus](Enums.md#ZH-CN_TOPIC_0000002497605218__nativeembedparamstatus21)否否param元素的状态变化类型。idstring否否param元素的id信息。namestring否是param元素的参数名称。valuestring否是param元素的参数值。

#### IntelligentTrackingPreventionDetails12+

提供智能防跟踪拦截的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明hoststring否否网站域名。trackerHoststring否否追踪者域名。

#### WebKeyboardCallbackInfo12+

拦截网页可编辑元素拉起软键盘的回调入参，其中包括[WebKeyboardController](Class (WebKeyboardController).md)、可编辑元素的属性。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明controller[WebKeyboardController](Class (WebKeyboardController).md)否否提供控制自定义键盘的输入、删除、关闭等操作。attributesRecord<string, string>否否触发本次软键盘弹出的网页元素属性。

#### WebKeyboardOptions12+

拦截网页可编辑元素拉起软键盘的回调返回值，可以指定使用的键盘类型，并返回给web内核，以控制拉起不同类型的软键盘；

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明useSystemKeyboardboolean否否

是否使用系统默认软键盘。

true表示使用系统默认软键盘，false表示不使用系统默认软键盘。

默认值：true。

enterKeyTypenumber否是指定系统软键盘enter键的类型，取值范围见输入框架的定义[EnterKeyType](@ohos.inputMethod (输入法框架).md#ZH-CN_TOPIC_0000002529285281__enterkeytype10)，该参数为可选参数，默认值为UNSPECIFIED。当useSystemKeyboard为true，并且设置了有效的enterKeyType时候，才有效。customKeyboard[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否是指定自定义键盘组件builder，可选参数，当useSystemKeyboard为false时，需要设置该参数，然后Web组件会拉起该自定义键盘。

#### FirstMeaningfulPaint12+

提供网页绘制页面主要内容的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明navigationStartTimenumber否是导航条加载时间，单位以微秒表示。firstMeaningfulPaintTimenumber否是绘制页面主要内容时间，单位以毫秒表示。

#### LargestContentfulPaint12+

提供网页绘制页面最大内容的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明navigationStartTimenumber否是导航条加载时间，单位以微秒表示。largestImagePaintTimenumber否是最大图片加载的时间，单位是以毫秒表示。largestTextPaintTimenumber否是最大文本加载时间，单位是以毫秒表示。largestImageLoadStartTimenumber否是最大图片开始加载时间，单位是以毫秒表示。largestImageLoadEndTimenumber否是最大图片结束加载时间，单位是以毫秒表示。imageBPPnumber否是最大图片像素位数。

#### NativeEmbedDataInfo11+

提供同层标签生命周期变化的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明status[NativeEmbedStatus](Enums.md#ZH-CN_TOPIC_0000002497605218__nativeembedstatus11)否是同层标签生命周期状态。surfaceIdstring否是NativeImage的psurfaceid。embedIdstring否是同层标签的唯一id。info[NativeEmbedInfo](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedinfo11)否是同层标签的详细信息。

#### NativeEmbedTouchInfo11+

提供手指触摸到同层标签的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明embedIdstring否是同层标签的唯一id。touchEvent[TouchEvent](触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)否是手指触摸动作信息。result12+[EventResult](Class (EventResult).md)否是通知Web组件手势事件的消费结果。

#### NativeEmbedMouseInfo20+

提供鼠标/触摸板在同层标签上点击或长按的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明embedIdstring否是同层标签的唯一id。mouseEvent[MouseEvent](鼠标事件.md#ZH-CN_TOPIC_0000002497604812__mouseevent对象说明)否是鼠标/触摸板点击/长按信息。result[EventResult](Class (EventResult).md)否是通知Web组件鼠标事件的消费结果。

#### NativeEmbedParamDataInfo21+

提供同层渲染object标签内嵌param元素变化时同层标签的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明embedIdstring否否同层标签的唯一id。objectAttributeIdstring否是同层标签的id信息。paramItemsArray<[NativeEmbedParamItem](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedparamitem21)>否是发生变化的param元素的详细信息，包括每一个param元素的状态变化类型、id、参数名称和参数值。

#### OnLoadStartedEvent20+

定义网页加载开始时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否页面的URL地址。

#### OnLoadFinishedEvent20+

定义网页加载结束时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否页面的URL地址。

#### OnPdfLoadEvent20+

定义PDF加载成功或失败时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否页面的URL地址。result[PdfLoadResult](Enums.md#ZH-CN_TOPIC_0000002497605218__pdfloadresult20)否否PDF页面加载结果。

#### OnPdfScrollEvent20+

定义PDF页面滚动到底时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否页面的URL地址。

#### Header

Web组件返回的请求/响应头对象。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明headerKeystring否否请求/响应头的key。headerValuestring否否请求/响应头的value。

#### ScreenCaptureConfig10+

Web屏幕捕获的配置。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明captureMode[WebCaptureMode](Enums.md#ZH-CN_TOPIC_0000002497605218__webcapturemode10)否否Web屏幕捕获模式。

#### BlankScreenDetectionEventInfo22+

定义检测到白屏时的事件信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否检测到白屏时，页面的url。blankScreenReason[DetectedBlankScreenReason](Enums.md#ZH-CN_TOPIC_0000002497605218__detectedblankscreenreason22)否否本次检测到白屏时，具体原因与检测的方法相关。blankScreenDetails[BlankScreenDetails](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__blankscreendetails22)否是

本次检测白屏的结果的细节。

如当发现近似白屏的现象产生，这个细节就包含具体命中了多少点。否则没有该属性。

#### BlankScreenDetails22+

定义检测到白屏时的结果的细节。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明detectedContentfulNodesCountnumber否是

在使用到检测有内容的节点检测策略时，且开发者自己设置了检测到节点数量阈值时，可能包含该属性。否则没有该属性。

表示当前命中了多少有内容的节点。

#### BlankScreenDetectionConfig22+

定义白屏检测的策略配置选项。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明enableboolean否否是否使能白屏策略功能。detectionTimingnumber[]否是

用以设置需要在加载后多少秒的时机来检测是否白屏。

单位：秒。

注：

1.重复值会忽略。

2.需大于0，小于0的值会被忽略。

默认值：[1.0,3.0,5.0]。

detectionMethods[BlankScreenDetectionMethod](Enums.md#ZH-CN_TOPIC_0000002497605218__blankscreendetectionmethod22)[]否是

使用检测策略的方法，是一个数组。

注：

1.重复值会忽略。

默认值：[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN]。

contentfulNodesCountThresholdnumber否是

在使用到检测有内容的节点检测策略时，才会生效。

可以设置0-${检测策略最大节点}，如果小于等于阈值则会触发近似白屏。

默认值：0。