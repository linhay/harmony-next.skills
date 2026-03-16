[]()[]()

# Interfaces (其他)

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

[]()[]()

#### WebStorageOrigin

提供Web SQL数据库的使用信息。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明originstring否否指定源的字符串索引。usagenumber否否指定源的存储量。quotanumber否否指定源的存储配额。[]()[]()

#### WebHeader

Web组件返回的请求/响应头对象。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明headerKeystring否否请求/响应头的key。headerValuestring否否请求/响应头的value。[]()[]()

#### WebCustomScheme

自定义协议配置。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明schemeNamestring否否自定义协议名称。最大长度为32，其字符仅支持小写字母、数字、'.'、'+'、'-'，同时需要以字母开头。isSupportCORSboolean否否

是否支持跨域请求。

true表示支持跨域请求，false表示不支持跨域请求。

默认值：true。

isSupportFetchboolean否否

是否支持fetch请求。

true表示支持fetch请求，false表示不支持fetch请求。

默认值：true。

isStandard12+boolean否是

设置了该选项的scheme是否将作为标准scheme进行处理。标准scheme需要符合RFC 1738第3.1节中定义的URL规范化和解析规则。

true表示设置了该选项的scheme将作为标准scheme进行处理，false表示设置了该选项的scheme不作为标准scheme进行处理。

默认值：true。

isLocal12+boolean否是

设置了该选项的scheme是否将使用与“file”协议相同的安全规则来处理。

true表示设置了该选项的scheme将使用与“file”协议相同的安全规则来处理，false表示设置了该选项的scheme不使用与“file”协议相同的安全规则来处理。

默认值：true。

isDisplayIsolated12+boolean否是

设置了该选项的scheme的内容是否只能从相同scheme的其他内容中显示或访问。

true表示设置了该选项的scheme的内容只能从相同scheme的其他内容中显示或访问，false表示设置了该选项的scheme的内容不是只能从相同scheme的其他内容中显示或访问。

默认值：true。

isSecure12+boolean否是

设置了该选项的scheme是否将使用与应用于“https”的安全规则相同的安全规则来处理。true表示设置了该选项的scheme将使用与应用于“https”的安全规则相同的安全规则来处理，false表示设置了该选项的scheme不使用与应用于“https”的安全规则相同的安全规则来处理。

默认值：true。

isCspBypassing12+boolean否是

设置了该选项的scheme可以绕过内容安全策略（CSP）检查。

true表示设置了该选项的scheme可以绕过内容安全策略（CSP）检查，false表示设置了该选项的scheme不可以绕过内容安全策略（CSP）检查。

默认值：true。

在大多数情况下，当设置isStandard为true时，不应设置此值。

isCodeCacheSupported12+boolean否是

设置了该选项的scheme的js资源是否支持生成code cache。

true表示设置了该选项的scheme的js资源支持生成code cache，false表示设置了该选项的scheme的js资源不支持生成code cache。

默认值：false。

[]()[]()

#### RequestInfo12+

Web组件发送的资源请求信息。

**系统能力：**: SystemCapability.Web.Webview.Core

名称类型只读可选说明urlstring否否请求的链接。methodstring否否请求的方法。formDatastring否否请求的表单数据。[]()[]()

#### CacheOptions12+

Web组件预编译JavaScript生成字节码缓存的配置对象，用于控制字节码缓存更新。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明responseHeadersArray<[WebHeader](#ZH-CN_TOPIC_0000002529285193__webheader)>否否请求此JavaScript文件时服务器返回的响应头，使用E-Tag或Last-Modified标识文件版本，判断是否需要更新。[]()[]()

#### SnapshotInfo12+

获取全量绘制结果入参。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明idstring否是snapshot的id。size[SizeOptions](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)否是web绘制的尺寸，最多支持16000px * 16000px，长度单位支持px、vp、%，需保持不同参数传入长度单位一致，默认单位vp，超过规格时返回最大规格。（示例：width:'100px'，height:'200px'。或者 width:'20%'，height:'30%'。只写数字时单位为vp。）[]()[]()

#### SnapshotResult12+

全量绘制回调结果。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明idstring否是snapshot的id。statusboolean否是snapshot的状态，正常为true，失败为false，获取全量绘制结果失败，返回size的长宽都为0，map为空。size[SizeOptions](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)否是web绘制的真实尺寸，number类型，单位vp。imagePixelMap[image.PixelMap](Interface (PixelMap).md)否是全量绘制结果为image.PixelMap格式。[]()[]()

#### OfflineResourceMap12+

本地离线资源配置对象，用于配置将被[injectOfflineResources](../classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__injectofflineresources12)接口注入到内存缓存的本地离线资源的相关信息，内核会根据此信息生成资源缓存，并据此控制缓存的有效期。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明urlListArray<string>否否本地离线资源对应的网络地址列表，列表的第一项将作为资源的源(Origin)，如果仅提供一个网络地址，则使用该地址作为这个资源的源。url仅支持http或https协议，长度不超过2048。resourceUint8Array否否本地离线资源的内容。responseHeadersArray<[WebHeader](#ZH-CN_TOPIC_0000002529285193__webheader)>否否资源对应的HTTP响应头。其中提供的Cache-Control或Expires响应头将被用于控制资源在内存缓存中的有效期。如果不提供，默认的有效期为86400秒，即1天。其中提供的Content-Type响应头将被用于定义资源的MIMEType，MODULE_JS必须提供有效的MIMEType，其他类型可不提供，无默认值，不符合标准的MIMEType会导致内存缓存失效。如果业务网页中的script标签使用了crossorigin属性，则必须在接口的responseHeaders参数中设置Cross-Origin响应头的值为anonymous或use-credentials。type[OfflineResourceType](../../topics/networking/Enums (arkts-apis-webview-e).md#ZH-CN_TOPIC_0000002529445167__offlineresourcetype12)否否资源的类型，目前仅支持Javascript、图片和CSS类型的资源。[]()[]()

#### PdfConfiguration14+

createPdf函数输入参数。

英寸与像素之间转换公式：像素 = 96 * 英寸。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明widthnumber否否

页面宽度。

单位：英寸。

推荐值：A4纸页面宽度8.27英寸。

heightnumber否否

页面高度。

单位：英寸。

推荐值：A4纸页面高度11.69英寸。

scalenumber否是

放大倍数。

取值范围：[0.0, 2.0]。如果不在取值范围内，小于0.0设置为0.0，大于2.0设置为2.0。

默认值：1.0。

marginTopnumber否否

上边距。

取值范围：[0.0, 页面高度的一半)。如果不在取值范围内，则设置为0.0。

单位：英寸。

marginBottomnumber否否

下边距。

取值范围：[0.0, 页面高度的一半)。如果不在取值范围内，则设置为0.0。

单位：英寸。

marginRightnumber否否

右边距。

取值范围：[0.0, 页面宽度的一半)。如果不在取值范围内，则设置为0.0。

单位：英寸。

marginLeftnumber否否

左边距。

取值范围：[0.0, 页面宽度的一半)。如果不在取值范围内，则设置为0.0。

单位：英寸。

shouldPrintBackgroundboolean否是

true表示打印背景颜色，false表示不打印背景颜色。

默认值：false。

[]()[]()

#### ScrollOffset13+

网页当前的滚动偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明xnumber否否

网页在水平方向的滚动偏移量。取值为网页左边界x坐标与Web组件左边界x坐标的差值。

当网页向右过滚动时，取值范围为负值。

当网页没有过滚动或者网页向左过滚动时，取值为0或正值。

单位：vp。

ynumber否否

网页在垂直方向的滚动偏移量。取值为网页上边界y坐标与Web组件上边界y坐标的差值。

当网页向下过滚动时，取值范围为负值。

当网页没有过滚动或者网页向上过滚动时，取值为0或正值。

单位：vp。

[]()[]()

#### HitTestValue

提供点击区域的元素信息。示例代码参考[getLastHitTest](../classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__getlasthittest18)。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明type[WebHitTestType](../../topics/networking/Enums (arkts-apis-webview-e).md#ZH-CN_TOPIC_0000002529445167__webhittesttype)否否当前被点击区域的元素类型。extrastring否否点击区域的附加参数信息。若被点击区域为图片或链接，则附加参数信息为其url地址。[]()[]()

#### ControllerAttachState20+

WebViewController与Web组件的绑定状态。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明UNATTACHED0未绑定状态。ATTACHED1已绑定状态。[]()[]()

#### BlanklessInfo20+

页面首屏加载预测信息，主要包括首屏相似度预测值，首屏加载耗时预测值，预测错误码，应用需根据此信息来决策是否启用无白屏加载插帧方案。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明errCodeWebBlanklessErrorCode否否无白屏加载的异常错误码，见[WebBlanklessErrorCode](../../topics/networking/Enums (arkts-apis-webview-e).md#ZH-CN_TOPIC_0000002529445167__webblanklesserrorcode20)定义。similaritynumber否否首屏相似度，根据历史加载首屏内容计算相似度，范围为0~1.0，1.0表示完全一致，数值越接近1，相似度越高。该值存在滞后性，本地加载的相似性将在下次加载时才可反映。建议当相似度较低时，应用不启用无白屏加载插帧方案。loadingTimenumber否否根据历史加载首屏耗时预测本次加载耗时，单位ms，取值范围需大于0。[]()[]()

#### HistoryItem

页面历史记录项。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明icon[image.PixelMap](Interface (PixelMap).md)否否历史页面图标的PixelMap对象。historyUrlstring否否历史记录项的url地址。historyRawUrlstring否否历史记录项的原始url地址。titlestring否否历史记录项的标题。[]()[]()

#### MediaInfo12+

[CreateNativeMediaPlayerCallback](../../topics/networking/Types (arkts-apis-webview-t).md#ZH-CN_TOPIC_0000002497605202__createnativemediaplayercallback12)回调函数的一个参数。包含了网页中媒体的信息。应用可以根据这些信息来创建接管网页媒体播放的播放器。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明embedIDstring否否网页中的 <video> 或 <audio> 的 ID 。mediaType[MediaType](../../topics/networking/Enums (arkts-apis-webview-e).md#ZH-CN_TOPIC_0000002529445167__mediatype12)否否媒体的类型。mediaSrcList[MediaSourceInfo](../classes/Class (MediaSourceInfo).md)[]否否媒体的源。可能有多个源，应用需要选择一个支持的源来播放。surfaceInfo[NativeMediaPlayerSurfaceInfo](../classes/Class (NativeMediaPlayerSurfaceInfo).md)否否用于同层渲染的 surface 信息。controlsShownboolean否否

<video> 或 <audio> 中是否有 controls属性。

true表示有，false表示没有。

controlListstring[]否否<video> 或 <audio> 中的 controlslist 属性的值。mutedboolean否否

是否要求静音播放。

true表示静音播放，false表示未静音播放。

posterUrlstring否否海报的地址。preload[Preload](../../topics/networking/Enums (arkts-apis-webview-e).md#ZH-CN_TOPIC_0000002529445167__preload12)否否是否需要预加载。headersRecord<string, string>否否播放器请求媒体资源时，需要携带的 HTTP 头。attributesRecord<string, string>否否<video> 或 <audio> 标签中的属性。[]()[]()

#### RectEvent12+

矩形定义。

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明xnumber否否矩形区域左上角x坐标。ynumber否否矩形区域左上角y坐标。widthnumber否否

矩形的宽度。

单位：px

heightnumber否否

矩形的高度。

单位：px