# Types


-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准。

**WebviewController9+**

type WebviewController = WebviewController

提供Web控制器的方法。

系统能力： SystemCapability.Web.Webview.Core

| 类型 | 说明 |
| --- | --- |
| WebviewController | 通过WebviewController可以控制Web组件各种行为。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。 |

**OnAdsBlockedCallback12+**

type OnAdsBlockedCallback = (details: AdsBlockedDetails) => void

当页面发生广告过滤时触发此回调。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| details | AdsBlockedDetails | 是 | 发生广告拦截时，广告资源信息。 |

**OnSslErrorEventCallback12+**

type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void

用户加载资源时发生SSL错误时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sslErrorEvent | SslErrorEvent | 是 | 用户加载资源时发生SSL错误时触发的回调详情。 |

**OnVerifyPinCallback22+**

type OnVerifyPinCallback = (verifyPinEvent: VerifyPinEvent) => void

需要用户进行PIN码认证时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verifyPinEvent | VerifyPinEvent | 是 | 需要用户进行PIN码认证时触发的回调详情。 |

**OnContextMenuHideCallback11+**

type OnContextMenuHideCallback = () => void

上下文菜单自定义隐藏的回调。

系统能力： SystemCapability.Web.Webview.Core

**OnRenderProcessNotRespondingCallback12+**

type OnRenderProcessNotRespondingCallback = (data : RenderProcessNotRespondingData) => void

渲染进程无响应时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | RenderProcessNotRespondingData | 是 | 渲染进程无响应的详细信息。 |

**OnRenderProcessRespondingCallback12+**

type OnRenderProcessRespondingCallback = () => void

渲染进程由无响应状态变回正常运行状态时触发该回调。

系统能力： SystemCapability.Web.Webview.Core

**OnViewportFitChangedCallback12+**

type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void

网页meta中viewport-fit配置项更改时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| viewportFit | ViewportFit | 是 | 网页meta中viewport-fit配置的视口类型。 |

**OnNativeEmbedVisibilityChangeCallback12+**

type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) => void

当同层标签可见性变化时触发该回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nativeEmbedVisibilityInfo | NativeEmbedVisibilityInfo | 是 | 提供同层标签的可见性信息。 |

**OnFullScreenEnterCallback12+**

type OnFullScreenEnterCallback = (event: FullScreenEnterEvent) => void

Web组件进入全屏时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | FullScreenEnterEvent | 是 | Web组件进入全屏的回调事件详情。 |

**OnFirstMeaningfulPaintCallback12+**

type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: [FirstMeaningfulPaint](Interfaces（其他）.md#ZH-CN_TOPIC_0000002522241178__firstmeaningfulpaint12)) => void

网页绘制页面度量信息的回调，当网页加载完页面主要内容时会触发该回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstMeaningfulPaint | FirstMeaningfulPaint | 是 | 绘制页面主要内容度量的详细信息。 |

**OnLargestContentfulPaintCallback12+**

type OnLargestContentfulPaintCallback = (largestContentfulPaint: [LargestContentfulPaint](Interfaces（其他）.md#ZH-CN_TOPIC_0000002522241178__largestcontentfulpaint12)) => void

网页绘制页面最大内容度量信息的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| largestContentfulPaint | LargestContentfulPaint | 是 | 网页绘制页面最大内容度量的详细信息。 |

**OnNavigationEntryCommittedCallback11+**

type OnNavigationEntryCommittedCallback = (loadCommittedDetails: [LoadCommittedDetails](Interfaces（其他）.md#ZH-CN_TOPIC_0000002522241178__loadcommitteddetails11)) => void

导航条目提交时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loadCommittedDetails | LoadCommittedDetails | 是 | 提供已提交跳转的网页的详细信息。 |

**OnSafeBrowsingCheckResultCallback11+**

type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void

网站安全风险检查触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| threatType | ThreatType | 是 | 定义网站threat类型。 |

**OnIntelligentTrackingPreventionCallback12+**

type OnIntelligentTrackingPreventionCallback = (details: IntelligentTrackingPreventionDetails) => void

当跟踪者cookie被拦截时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| details | IntelligentTrackingPreventionDetails | 是 | 提供智能防跟踪拦截的详细信息。 |

**OnOverrideUrlLoadingCallback12+**

type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean

onOverrideUrlLoading的回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webResourceRequest | WebResourceRequest | 是 | url请求的相关信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示阻止此次加载，否则允许此次加载。 |

**WebKeyboardCallback12+**

type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions

拦截网页可编辑元素拉起软键盘的回调，一般在点击网页input标签时触发。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyboardCallbackInfo | WebKeyboardCallbackInfo | 是 | 拦截网页拉起软键盘回调通知的入参，其中包括WebKeyboardController、可编辑元素的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WebKeyboardOptions | 回调函数通过返回WebKeyboardOptions来决定ArkWeb内核拉起不同类型的软键盘。 |

**OnOverrideErrorPageCallback20+**

type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string

onOverrideErrorPage的回调函数，网页加载失败时触发。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errorPageEvent | OnErrorReceiveEvent | 是 | 网页加载遇到错误时返回的相关信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回以Base64编码的HTML文本内容。 |

**MouseInfoCallback20+**

type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void

当鼠标/触摸板点击到同层标签时触发该回调。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | NativeEmbedMouseInfo | 是 | 提供鼠标/触摸板在同层标签上点击或长按的详细信息。 |

示例：

完整示例代码参考[onNativeEmbedMouseEvent](事件.md#ZH-CN_TOPIC_0000002522081170__onnativeembedmouseevent20)。

**OnNativeEmbedObjectParamChangeCallback21+**

type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void

增加、修改或删除同层渲染object标签内嵌param元素时触发此回调。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | NativeEmbedParamDataInfo | 是 | object标签内嵌param元素的详细变化信息。 |

示例：

完整示例代码参考[onNativeEmbedObjectParamChange](事件.md#ZH-CN_TOPIC_0000002522081170__onnativeembedobjectparamchange21)。

**OnDetectBlankScreenCallback22+**

type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void

检测到白屏时触发此回调。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | BlankScreenDetectionEventInfo | 是 | 检测到白屏时的详细信息。 |

示例：

完整示例代码参考[onDetectedBlankScreen](事件.md#ZH-CN_TOPIC_0000002522081170__ondetectedblankscreen22)。

**OnCameraCaptureStateChangeCallback23+**

type OnCameraCaptureStateChangeCallback = (event: CameraCaptureStateChangeInfo) => void;

当页面摄像头状态发生改变时触发此回调。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | CameraCaptureStateChangeInfo | 是 | 网页摄像头状态发生改变时，返回原来的状态和改变后的状态。 |

**OnMicrophoneCaptureStateChangeCallback23+**

type OnMicrophoneCaptureStateChangeCallback = (event: MicrophoneCaptureStateChangeInfo) => void;

当页面麦克风状态发生改变时触发此回调。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | MicrophoneCaptureStateChangeInfo | 是 | 网页麦克风状态发生改变时，返回原来的状态和改变后的状态。 |

**TextSelectionChangeCallback23+**

type TextSelectionChangeCallback = (selectionText: string) => void

onTextSelectionChange的回调函数，选区内容改变时触发。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionText | string | 是 | 返回所选文本的内容。 |

示例：

完整示例代码参考[onTextSelectionChange](事件.md#ZH-CN_TOPIC_0000002522081170__ontextselectionchange23)。

**OnFirstScreenPaintCallback23+**

type OnFirstScreenPaintCallback = (firstScreenPaint: FirstScreenPaint) => void

检测到首屏渲染结束时会触发此回调。

系统能力： SystemCapability.Web.Webview.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstScreenPaint | FirstScreenPaint | 是 | 检测到首屏渲染时的详细信息。 |

示例：

完整示例代码参考[onFirstScreenPaint](事件.md#ZH-CN_TOPIC_0000002522081170__onfirstscreenpaint23)。