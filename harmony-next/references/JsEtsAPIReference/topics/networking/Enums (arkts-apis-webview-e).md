[]()[]()

# Enums

本模块首批接口从API version 9开始支持，后续版本的新增接口，则采用上角标单独标记接口的起始版本。

[]()[]()

#### WebHitTestType

[getLastHitTest](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__getlasthittest18)接口用于指示游标节点。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明EditText0可编辑的区域。Email1电子邮件地址。HttpAnchor2超链接，其中src为http。HttpAnchorImg3带有超链接的图片，其中src为http + HTML::img。Img4HTML::img标签。Map5地理地址。Phone6电话号码。Unknown7未知内容。[]()[]()

#### SecureDnsMode10+

Web组件使用HTTPDNS的模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明OFF0不使用HTTPDNS， 可以用于撤销之前使用的HTTPDNS配置。AUTO1自动模式，用于解析的设定DNS服务器不可用时，可自动回落至系统DNS。SECURE_ONLY2强制使用设定的HTTPDNS服务器进行域名解析。[]()[]()

#### SecurityLevel11+

当前网页的安全级别。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NONE0页面既不绝对安全，也不是不安全，即是中立。例如，部分scheme非http/https的URL。SECURE1页面安全，页面使用的是HTTPS协议，且使用了信任的证书。WARNING2页面不安全。例如，使用HTTP协议或使用HTTPS协议但使用旧版TLS版本。DANGEROUS3页面不安全。尝试HTTPS并失败、页面未通过身份验证、页面上包含不安全活动内容的HTTPS、恶意软件、网络钓鱼或任何其他可能危险的严重安全问题。[]()[]()

#### MediaPlaybackState12+

当前网页的播控状态。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NONE0页面无音视频启播。PLAYING1页面音视频播放中。PAUSED2页面音视频暂停。STOPPED3页面音视频停止。[]()[]()

#### PressureLevel14+

内存压力等级。在应用主动清理Web组件占用的缓存时，Web内核会根据内存压力等级，进行缓存释放。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明MEMORY_PRESSURE_LEVEL_MODERATE1中等内存压力等级。这个等级下，Web内核会尝试释放重新分配开销较小且不需要立即使用的缓存。MEMORY_PRESSURE_LEVEL_CRITICAL2严重内存压力等级。这个等级下，Web内核会尝试释放所有可能的内存缓存。[]()[]()

#### WebMessageType10+

[webMessagePort](../../types/interfaces/Interface (WebMessagePort).md)接口所支持的数据类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NOT_SUPPORT0不支持的数据类型。STRING1字符串类型。NUMBER2数值类型。BOOLEAN3布尔类型。ARRAY_BUFFER4原始二进制数据缓冲区。ARRAY5数组类型。ERROR6错误类型。[]()[]()

#### JsMessageType10+

[runJavaScriptExt](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)接口脚本执行后返回的结果的类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NOT_SUPPORT0不支持的数据类型。STRING1字符串类型。NUMBER2数值类型。BOOLEAN3布尔类型。ARRAY_BUFFER4原始二进制数据缓冲区。ARRAY5数组类型[]()[]()

#### RenderProcessMode12+

ArkWeb渲染子进程模式类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明SINGLE0ArkWeb单渲染子进程模式。该模式下，多个Web复用一个渲染子进程。MULTIPLE1ArkWeb多渲染子进程模式。该模式下，每个Web一个渲染子进程。[]()[]()

#### OfflineResourceType12+

[OfflineResourceMap](../../types/interfaces/Interfaces (其他) (arkts-apis-webview-i).md#ZH-CN_TOPIC_0000002529285193__offlineresourcemap12)对象对应的本地离线资源的接口类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明IMAGE0图片类型的资源。CSS1CSS类型的资源。CLASSIC_JS2通过<script src="" />标签加载的Javascript资源。MODULE_JS3通过<script src="" type="module" />标签加载的Javascript资源。[]()[]()

#### ScrollType12+

Scroll滚动类型，用于[setScrollable](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__setscrollable12)。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明EVENT0滚动事件，表示通过触摸屏，触摸板，鼠标滚轮生成的网页滚动。[]()[]()

#### WebDownloadState11+

下载任务的状态。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明IN_PROGRESS0下载任务正在进行中。COMPLETED1下载任务已经完成。CANCELED2下载任务已经被取消。INTERRUPTED3下载任务被中断。PENDING4下载任务等待开始。PAUSED5下载任务已经被暂停。UNKNOWN6下载任务未知状态。[]()[]()

#### WebDownloadErrorCode11+

下载任务的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明ERROR_UNKNOWN0未知的错误。FILE_FAILED1常规文件操作失败。FILE_ACCESS_DENIED2没有权限访问文件。FILE_NO_SPACE3磁盘没有足够的空间。FILE_NAME_TOO_LONG5文件名字过长。FILE_TOO_LARGE6文件太大。FILE_TRANSIENT_ERROR10出现了一些临时问题，例如内存不足、文件正在使用以及同时打开的文件过多。FILE_BLOCKED11由于某些本地策略，文件被阻止访问。FILE_TOO_SHORT13当尝试恢复下载时，发现文件不够长，可能该文件已不存在。FILE_HASH_MISMATCH14哈希不匹配。FILE_SAME_AS_SOURCE15文件已存在。NETWORK_FAILED20一般网络错误。NETWORK_TIMEOUT21网络超时。NETWORK_DISCONNECTED22网络断开连接。NETWORK_SERVER_DOWN23服务器关闭。NETWORK_INVALID_REQUEST24无效的网络请求，可能重定向到不支持的方案或无效的URL。SERVER_FAILED30服务器返回了一个一般性错误。SERVER_NO_RANGE31服务器不支持范围请求。SERVER_BAD_CONTENT33服务器没有请求的数据。SERVER_UNAUTHORIZED34服务器不允许下载该文件。SERVER_CERT_PROBLEM35服务器证书错误。SERVER_FORBIDDEN36服务器访问被禁止。SERVER_UNREACHABLE37无法访问服务器。SERVER_CONTENT_LENGTH_MISMATCH38接收到的数据与内容长度不匹配。SERVER_CROSS_ORIGIN_REDIRECT39发生意外的跨站重定向。USER_CANCELED40用户取消了下载。USER_SHUTDOWN41用户关闭了应用。CRASH50应用发生了崩溃。[]()[]()

#### WebResourceType12+

资源请求的资源类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明MAIN_FRAME0顶层页面。SUB_FRAME1Frame或Iframe。STYLE_SHEET2CSS样式表。SCRIPT3外部脚本。IMAGE4图片（jpg/gif/png/以及其他）。FONT_RESOURCE5字体。SUB_RESOURCE6其他子资源。如果实际类型未知，则是默认类型。OBJECT7插件的Object（或embed）标签，或者插件请求的资源。MEDIA8媒体资源。WORKER9专用工作线程的主资源。SHARED_WORKER10共享工作线程的主资源。PREFETCH11明确的预取请求。FAVICON12网站图标。XHR13XMLHttpRequest。PING14<a ping>/sendBeacon的Ping请求。SERVICE_WORKER15service worker的主资源。CSP_REPORT16内容安全策略违规报告。PLUGIN_RESOURCE17插件请求的资源。NAVIGATION_PRELOAD_MAIN_FRAME19触发service worker预热的主frame跳转请求。NAVIGATION_PRELOAD_SUB_FRAME20触发service worker预热的子frame跳转请求。[]()[]()

#### PlaybackStatus12+

[handleStatusChanged](../../types/interfaces/Interface (NativeMediaPlayerHandler).md#ZH-CN_TOPIC_0000002497605200__handlestatuschanged12) 接口参数， 用于表示播放器的播放状态。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明PAUSED0播放状态为播放状态。PLAYING1播放状态为暂停状态。[]()[]()

#### NetworkState12+

播放器的网络状态。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明EMPTY0播放器还没有开始下载数据。IDLE1播放器网络状态空闲，比如媒体分片下载完成，下一个分片还没有开始下载。LOADING2播放器正在下载媒体数据。NETWORK_ERROR3发生了网络错误。[]()[]()

#### ReadyState12+

播放器的缓存状态。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明HAVE_NOTHING0没有缓存。HAVE_METADATA1只缓存了媒体元数据。HAVE_CURRENT_DATA2只缓存到当前的播放进度。HAVE_FUTURE_DATA3缓存时长超过了当前的播放进度, 但是仍有可能导致卡顿。HAVE_ENOUGH_DATA4缓存了足够的数据，保证播放流畅。[]()[]()

#### MediaError12+

播放器的错误类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NETWORK_ERROR1网络错误。FORMAT_ERROR2媒体格式错误。DECODE_ERROR3解码错误。[]()[]()

#### SuspendType12+

表示播放器的挂起类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明ENTER_BACK_FORWARD_CACHE0页面进BFCache。ENTER_BACKGROUND1页面进后台。AUTO_CLEANUP2系统自动清理。[]()[]()

#### MediaType12+

表示媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明VIDEO0视频。AUDIO1音频。[]()[]()

#### SourceType12+

表示媒体源的类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明URL0媒体源的类型是URL。MSE1媒体源的类型是blob。[]()[]()

#### Preload12+

播放器预加载媒体数据。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NONE0不预加载。METADATA1只预加载媒体的元数据。AUTO2预加载足够多的媒体数据，以保证能流畅地播放。[]()[]()

#### ProxySchemeFilter15+

使用代理的请求的scheme信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明MATCH_ALL_SCHEMES0所有的scheme都会使用代理。MATCH_HTTP1HTTP请求会使用代理。MATCH_HTTPS2HTTPS请求会使用代理。[]()[]()

#### WebDestroyMode20+

Web组件的销毁模式，当Web组件销毁时，销毁模式会影响Web内核的资源释放时机，例如JavaScript运行上下文、渲染上下文等等。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NORMAL_MODE0普通模式，由系统决定Web组件资源的销毁时机。FAST_MODE1快速模式，当Web组件触发销毁时，立即销毁相关的内部资源。[]()[]()

#### ScrollbarMode23+

Web页面场景下，全局滚动条模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明OVERLAY_LAYOUT_SCROLLBAR0非常驻滚动条。FORCE_DISPLAY_SCROLLBAR1常驻滚动条。[]()[]()

#### WebBlanklessErrorCode20+

无白屏加载的异常错误码。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明SUCCESS0成功。ERR_UNKNOWN-1未知错误，内部状态错误等。ERR_INVALID_PARAM-2参数不合法。ERR_CONTROLLER_NOT_INITED-3WebViewController未绑定组件。ERR_KEY_NOT_MATCH-4未匹配到key值，对于[setBlanklessLoadingWithKey](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__setblanklessloadingwithkey20)需与[getBlanklessInfoWithKey](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__getblanklessinfowithkey20)配套使用并且key值一致，否则返回该错误码。ERR_SIGNIFICANT_CHANGE-5当相似度较低时，系统会判定为跳变太大，[setBlanklessLoadingWithKey](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__setblanklessloadingwithkey20)接口不会成功启用插帧。[]()[]()

#### ArkWebEngineVersion20+

ArkWeb内核版本，请参考[M114内核在HarmonyOS6.0系统上的适配指导](https://gitcode.com/HarmonyOS-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明SYSTEM_DEFAULT0系统默认内核，HarmonyOS 6.0版本默认为M132。M1141HarmonyOS 6.0版本的遗留内核。开发者可选择此遗留内核，若系统版本上不存在此内核则设置无效。M1322HarmonyOS 6.0版本的常青内核，M132为此版本的默认内核。若系统版本上不存在此内核则设置无效。

**表1** 常青内核与遗留内核含义说明

**内核类型****英文****说明**常青内核EVERGREEN WebCore当前系统的最新Web内核，系统基于此内核进行完整的功能实现，推荐应用使用。遗留内核LEGACY WebCore复用上一版本的内核，只做安全补丁及舆情问题修复，仅作为兼容性回滚使用，且遗留内核的支持有时间限制。[]()[]()

#### SiteIsolationMode21+

站点隔离机制将不同源的网站隔离在不同的Render进程中，减少跨域攻击面。例如，PC上原有进程模型是每一个Tab对应一个Render进程，站点隔离打开后，让不同源的Iframe运行在独立的Render进程中。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明PARTIAL0部分站点隔离，即在同一个Render进程内加载新站点。STRICT1严格站点隔离，跨站点的Iframe将切换到新的渲染进程。[]()[]()

#### WebSoftKeyboardBehaviorMode22+

Web软键盘自动控制模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明DEFAULT0当Web组件失去焦点或获得焦点、状态切换为inactive或active时，系统均会尝试触发软键盘自动隐藏或拉起（默认值）。DISABLE_AUTO_KEYBOARD_ON_ACTIVE1Web组件在inactive或active状态切换时，系统不再尝试触发软键盘自动隐藏或拉起。