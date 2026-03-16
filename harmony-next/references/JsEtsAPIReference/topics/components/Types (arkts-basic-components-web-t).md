[]()[]()

# Types

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

[]()[]()

#### WebviewController9+

type WebviewController = WebviewController

提供Web控制器的方法。

**系统能力：** SystemCapability.Web.Webview.Core

类型说明[WebviewController](../../types/classes/Class (WebviewController).md)通过WebviewController可以控制Web组件各种行为。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。[]()[]()

#### OnAdsBlockedCallback12+

type OnAdsBlockedCallback = (details: AdsBlockedDetails) => void

当页面发生广告过滤时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明details[AdsBlockedDetails](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__adsblockeddetails12)是发生广告拦截时，广告资源信息。[]()[]()

#### OnSslErrorEventCallback12+

type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void

用户加载资源时发生SSL错误时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明sslErrorEvent[SslErrorEvent](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__sslerrorevent12)是用户加载资源时发生SSL错误时触发的回调详情。[]()[]()

#### OnVerifyPinCallback22+

type OnVerifyPinCallback = (verifyPinEvent: VerifyPinEvent) => void

需要用户进行PIN码认证时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明verifyPinEvent[VerifyPinEvent](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__verifypinevent22)是需要用户进行PIN码认证时触发的回调详情。[]()[]()

#### OnContextMenuHideCallback11+

type OnContextMenuHideCallback = () => void

上下文菜单自定义隐藏的回调。

**系统能力：** SystemCapability.Web.Webview.Core

[]()[]()

#### OnRenderProcessNotRespondingCallback12+

type OnRenderProcessNotRespondingCallback = (data : RenderProcessNotRespondingData) => void

渲染进程无响应时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明data[RenderProcessNotRespondingData](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__renderprocessnotrespondingdata12)是渲染进程无响应的详细信息。[]()[]()

#### OnRenderProcessRespondingCallback12+

type OnRenderProcessRespondingCallback = () => void

渲染进程由无响应状态变回正常运行状态时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

[]()[]()

#### OnViewportFitChangedCallback12+

type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void

网页meta中viewport-fit配置项更改时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明viewportFit[ViewportFit](Enums (arkts-basic-components-web-e).md#ZH-CN_TOPIC_0000002497605218__viewportfit12)是网页meta中viewport-fit配置的视口类型。[]()[]()

#### OnNativeEmbedVisibilityChangeCallback12+

type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) => void

当同层标签可见性变化时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明nativeEmbedVisibilityInfo[NativeEmbedVisibilityInfo](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedvisibilityinfo12)是提供同层标签的可见性信息。[]()[]()

#### OnFullScreenEnterCallback12+

type OnFullScreenEnterCallback = (event: FullScreenEnterEvent) => void

Web组件进入全屏时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明event[FullScreenEnterEvent](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__fullscreenenterevent12)是Web组件进入全屏的回调事件详情。[]()[]()

#### OnFirstMeaningfulPaintCallback12+

type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: [FirstMeaningfulPaint](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__firstmeaningfulpaint12)) => void

网页绘制页面度量信息的回调，当网页加载完页面主要内容时会触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明firstMeaningfulPaint[FirstMeaningfulPaint](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__firstmeaningfulpaint12)是绘制页面主要内容度量的详细信息。[]()[]()

#### OnLargestContentfulPaintCallback12+

type OnLargestContentfulPaintCallback = (largestContentfulPaint: [LargestContentfulPaint](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__largestcontentfulpaint12)) => void

网页绘制页面最大内容度量信息的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明largestContentfulPaint[LargestContentfulPaint](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__largestcontentfulpaint12)是网页绘制页面最大内容度量的详细信息。[]()[]()

#### OnNavigationEntryCommittedCallback11+

type OnNavigationEntryCommittedCallback = (loadCommittedDetails: [LoadCommittedDetails](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__loadcommitteddetails11)) => void

导航条目提交时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明loadCommittedDetails[LoadCommittedDetails](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__loadcommitteddetails11)是提供已提交跳转的网页的详细信息。[]()[]()

#### OnSafeBrowsingCheckResultCallback11+

type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void

网站安全风险检查触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明threatType[ThreatType](Enums (arkts-basic-components-web-e).md#ZH-CN_TOPIC_0000002497605218__threattype11)是定义网站threat类型。[]()[]()

#### OnIntelligentTrackingPreventionCallback12+

type OnIntelligentTrackingPreventionCallback = (details: IntelligentTrackingPreventionDetails) => void

当跟踪者cookie被拦截时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明details[IntelligentTrackingPreventionDetails](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__intelligenttrackingpreventiondetails12)是提供智能防跟踪拦截的详细信息。[]()[]()

#### OnOverrideUrlLoadingCallback12+

type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean

onOverrideUrlLoading的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明webResourceRequest[WebResourceRequest](../../types/classes/Class (WebResourceRequest).md)是url请求的相关信息。

**返回值：**

类型说明boolean返回true表示阻止此次加载，否则允许此次加载。[]()[]()

#### WebKeyboardCallback12+

type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions

拦截网页可编辑元素拉起软键盘的回调，一般在点击网页input标签时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明keyboardCallbackInfo[WebKeyboardCallbackInfo](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__webkeyboardcallbackinfo12)是拦截网页拉起软键盘回调通知的入参，其中包括[WebKeyboardController](../../types/classes/Class (WebKeyboardController).md)、可编辑元素的属性。

**返回值：**

类型说明[WebKeyboardOptions](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__webkeyboardoptions12)回调函数通过返回[WebKeyboardOptions](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__webkeyboardoptions12)来决定ArkWeb内核拉起不同类型的软键盘。[]()[]()

#### OnOverrideErrorPageCallback20+

type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string

onOverrideErrorPage的回调函数，网页加载失败时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明errorPageEvent[OnErrorReceiveEvent](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__onerrorreceiveevent12)是网页加载遇到错误时返回的相关信息。

**返回值：**

类型说明string返回以Base64编码的HTML文本内容。[]()[]()

#### MouseInfoCallback20+

type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void

当鼠标/触摸板点击到同层标签时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明event[NativeEmbedMouseInfo](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedmouseinfo20)是提供鼠标/触摸板在同层标签上点击或长按的详细信息。

**示例：**

完整示例代码参考[onNativeEmbedMouseEvent](../misc/事件.md#ZH-CN_TOPIC_0000002497445228__onnativeembedmouseevent20)。

[]()[]()

#### OnNativeEmbedObjectParamChangeCallback21+

type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void

增加、修改或删除同层渲染object标签内嵌param元素时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明event[NativeEmbedParamDataInfo](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedparamdatainfo21)是object标签内嵌param元素的详细变化信息。

**示例：**

完整示例代码参考[onNativeEmbedObjectParamChange](../misc/事件.md#ZH-CN_TOPIC_0000002497445228__onnativeembedobjectparamchange21)。

[]()[]()

#### OnDetectBlankScreenCallback22+

type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void

检测到白屏时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明event[BlankScreenDetectionEventInfo](../../types/interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__blankscreendetectioneventinfo22)是检测到白屏时的详细信息。

**示例：**

完整示例代码参考[onDetectedBlankScreen](../misc/事件.md#ZH-CN_TOPIC_0000002497445228__ondetectedblankscreen22)。