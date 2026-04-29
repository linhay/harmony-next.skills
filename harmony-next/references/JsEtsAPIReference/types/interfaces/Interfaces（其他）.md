# Interfaces（其他）

-

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准。

#### WebOptions

通过[接口](组件描述.md#ZH-CN_TOPIC_0000002522241166__接口)定义Web选项。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | string | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 否 | 网页资源地址。如果访问本地资源文件，请使用$rawfile或者resource协议。如果加载应用包外沙箱路径的本地资源文件(文件支持html和txt类型)，请使用file://沙箱文件路径。 src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过loadUrl()重新加载。 |
| controller | WebController | WebviewController | 否 | 否 | 控制器，通过controller可以控制Web组件各种行为（包括页面导航、声明周期状态、JavaScript交互等行为）。从API version 9开始，WebController不再维护，建议使用WebviewController替代。 |
| renderMode12+ | [RenderMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__rendermode12) | 否 | 是 | 表示当前Web组件的渲染方式，RenderMode.ASYNC_RENDER表示Web组件异步渲染，RenderMode.SYNC_RENDER表示支持Web组件同步渲染能力，默认值RenderMode.ASYNC_RENDER，该模式不支持动态调整。 |
| incognitoMode11+ | boolean | 否 | 是 | 表示当前创建的webview是否是隐私模式。true表示创建隐私模式的webview，false表示创建正常模式的webview。 默认值：false。 传入undefined或null时为false。 |
| sharedRenderProcessToken12+ | string | 否 | 是 | 表示当前Web组件指定共享渲染进程的token，多渲染进程模式下，相同token的Web组件会优先尝试复用与token相绑定的渲染进程。token与渲染进程的绑定发生在渲染进程的初始化阶段。当渲染进程没有关联的Web组件时，其与token绑定关系将被移除。 默认值： ""。 |
| emulateTouchFrom[MouseEvent](../../topics/components/鼠标事件.md#ZH-CN_TOPIC_0000002497604812__mouseevent对象说明)22+ | boolean | 否 | 是 | 设定鼠标事件是否被转换成触摸事件。 默认值：false。 |

#### WebMediaOptions10+

Web媒体策略的配置。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resumeInterval | number | 否 | 是 | 被其他应用暂停的Web音视频能够自动续播的有效期，单位：秒。取值范围：[-2147483648, 2147483647]。resumeInterval值为0时，不自动续播；大于0时，将在该时间内尝试续播；小于0时，将在无限时间内尝试续播。由于近似值原因，该有效期可能存在一秒内的误差。 说明： HLS视频被打断后，回到前台将自动续播，不受该时间控制。 |
| audioExclusive | boolean | 否 | 是 | 应用内多个Web实例的音频是否独占。 true表示应用内多个Web实例的音频独占，false表示应用内多个Web实例的音频不独占。 默认值:true。 |
| audioSessionType20+ | [AudioSessionType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__audiosessiontype20) | 否 | 是 | 应用中Web音频类型。默认值对应[系统音频流类型](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)STREAM_USAGE_MUSIC。设置该参数会改变组件音频类型与系统音频类型映射关系，进而影响ArkWeb音频焦点策略。 |

#### ScriptItem11+

通过[javaScriptOnDocumentStart](属性.md#ZH-CN_TOPIC_0000002553201131__javascriptondocumentstart11)属性注入到Web组件的ScriptItem对象。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| script | string | 否 | 否 | 需要注入、执行的JavaScript脚本。 |
| scriptRules | Array<string> | 否 | 否 | 一组允许来源的匹配规则。 1.如果需要允许所有来源的网址，使用通配符“ * ”。 2.如果需要精确匹配，则描述网站地址，如"https://www.example.com"。 3.如果模糊匹配网址，可以使用“ * ”通配符替代，如"https://*.example.com"。不允许使用"x. * .y.com"、" * foobar.com"等。 4.如果来源是ip地址，则使用规则2。 5.对于http/https以外的协议(自定义协议)，不支持使用精确匹配和模糊匹配，且必须以://结尾，例如"resource://"。 6.一组scriptRule中，如果其中一条不满足以上规则，则整组scriptRule都不生效。 |
| urlRegexRules23+ | Array<UrlRegexRule> | 否 | 是 | 一组允许来源的正则匹配规则。 当scriptRules设置为[]时，才使用urlRegexRules进行匹配。 模型约束： 此[接口](../../topics/misc/组件描述.md#ZH-CN_TOPIC_0000002529445171__接口)仅可在Stage模型下使用。 |

**UrlRegexRule23+**

定义Url正则表达式规则。

模型约束： 此[接口](../../topics/misc/组件描述.md#ZH-CN_TOPIC_0000002529445171__接口)仅可在Stage模型下使用。

系统能力： SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| secondLevelDomain | string | 否 | 否 | 二级域名的精确匹配。例如，"https://www.example.com"的二级域名为example.com；"https://www.example.com.cn"二级域名为example.com.cn。网址没有二级域名则为空。 |
| rule | string | 否 | 否 | url正则表达式。 在secondLevelDomain匹配成功后，才进行url正则匹配。 |

#### NestedScrollOptionsExt14+

通过NestedScrollOptionsExt可以设置上下左右四个方向的嵌套滚动规则。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scrollUp | [NestedScrollMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10) | 否 | 是 | 可滚动组件往上滚动时的嵌套滚动选项。 默认值：NestedScrollMode.SELF_FIRST。 |
| scrollDown | [NestedScrollMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10) | 否 | 是 | 可滚动组件往下滚动时的嵌套滚动选项。 默认值：NestedScrollMode.SELF_FIRST。 |
| scrollLeft | [NestedScrollMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10) | 否 | 是 | 可滚动组件往左滚动时的嵌套滚动选项。 默认值：NestedScrollMode.SELF_FIRST。 |
| scrollRight | [NestedScrollMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__nestedscrollmode10) | 否 | 是 | 可滚动组件往右滚动时的嵌套滚动选项。 默认值：NestedScrollMode.SELF_FIRST。 |

#### NativeMediaPlayerConfig12+

用于[开启应用接管网页媒体播放功能](属性.md#ZH-CN_TOPIC_0000002553201131__enablenativemediaplayer12)的配置信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enable | boolean | 否 | 否 | 是否[开启应用接管网页媒体播放功能](../../topics/misc/属性.md#ZH-CN_TOPIC_0000002497605206__enablenativemediaplayer12)。 true表示开启应用接管网页媒体播放功能，false表示关闭应用接管网页媒体播放功能。 默认值：false。 |
| shouldOverlay | boolean | 否 | 否 | [开启应用接管网页媒体播放功能](../../topics/misc/属性.md#ZH-CN_TOPIC_0000002497605206__enablenativemediaplayer12)后，应用接管网页视频的播放器画面是否覆盖网页内容。 true表示改变视频图层的高度，使其覆盖网页内容。false表示不覆盖网页内容，跟原视频图层高度一样，嵌入在网页中。 默认值：false。 |

#### ExpandedMenuItemOptions(deprecated)


从API version 12开始支持，从API version 20开始废弃，建议使用[editMenuOptions](属性.md#ZH-CN_TOPIC_0000002553201131__editmenuoptions12)替代。

自定义菜单扩展项。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Str | 否 | 否 | 显示内容。 |
| startIcon | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Str | 否 | 是 | 显示图标。默认值为空，不显示图标。 |
| action | (selectedText: {plainText: string}) => void | 否 | 否 | 选中的文本信息。 |

#### AdsBlockedDetails12+

发生广告拦截时，广告资源信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 发生广告过滤的页面url。 |
| adsBlocked | Array<string> | 否 | 否 | 被过滤的资源的url或dompath标识，被过滤的多个对象url相同则可能出现重复元素。 |

#### SelectionMenuOptionsExt13+

自定义菜单扩展项。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onAppear | Callback<void> | 否 | 是 | 自定义选择菜单弹出时回调。 |
| onDisappear | Callback<void> | 否 | 是 | 自定义选择菜单关闭时回调。 |
| preview | [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | 否 | 是 | 自定义选择菜单的预览内容样式，未配置时无预览内容。 |
| menuType | [MenuType](../../topics/components/文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__menutype13枚举说明) | 否 | 是 | 自定义选择菜单类型。 默认值：MenuType.SELECTION_MENU。 从API version 20起，MenuType.PREVIEW_MENU支持超链接预览。 |
| previewMenuOptions20+ | PreviewMenuOptions | 否 | 是 | 自定义选择预览菜单选项。 |
| onMenuShow21+ | Callback<void> | 否 | 是 | 自定义选择菜单显示时回调。 |
| onMenuHide21+ | Callback<void> | 否 | 是 | 自定义选择菜单隐藏时回调。 |

#### PreviewMenuOptions20+

预览菜单选项。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hapticFeedbackMode | [HapticFeedbackMode](../../topics/components/菜单控制.md#ZH-CN_TOPIC_0000002497604848__hapticfeedbackmode18) | 否 | 是 | 菜单弹出时振动效果。需配置"ohos.permission.VIBRATE"权限 默认值：HapticFeedbackMode.DISABLED，菜单弹出时不振动。 |

#### EmbedOptions16+

Web同层渲染的配置。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportDefaultIntrinsicSize | boolean | 否 | 是 | 设置同层渲染元素是否支持固定大小 300 * 150。 当H5侧CSS设置了大小时，同层渲染元素大小为CSS大小，否则为固定大小。 为true时，固定大小为 300 * 150。 为false时，若H5侧CSS未设置大小，则同层渲染元素不渲染。 默认值：false 单位：px |
| supportCssDisplayChange20+ | boolean | 否 | 是 | 设置同层渲染可见性[接口](../../topics/misc/组件描述.md#ZH-CN_TOPIC_0000002529445171__接口)是否支持显示属性。 同层渲染可见性接口默认支持同层标签相对于视口的可见状态。 设置为true时，支持显示CSS属性，包括visibility、display和宽高。 设置为false时，不支持显示CSS属性，仅支持同层标签相对于视口的可见性。 |

#### OnAlertEvent12+

定义网页触发 alert() 告警时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 当前显示弹窗的网页的URL。 |
| message | string | 否 | 否 | 显示在弹窗中的信息。 |
| result | JsResult | 否 | 否 | 通知Web组件用户的操作结果。 |

#### OnBeforeUnloadEvent12+

定义刷新或关闭场景下，在即将离开当前页面时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 当前显示弹窗所在网页的URL。 |
| message | string | 否 | 否 | 弹窗中显示的信息。 |
| result | JsResult | 否 | 否 | 通知Web组件用户操作行为。 |
| isReload20+ | boolean | 否 | 是 | 页面是否刷新。 当页面因刷新即将离开时，isReload参数被设置为true；当页面因关闭即将离开时，isReload参数被设置为false。 默认值：false。 |

#### OnConfirmEvent12+

定义网页触发 confirm() 弹窗时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 当前显示弹窗的网页的URL。 |
| message | string | 否 | 否 | 显示在弹窗中的信息。 |
| result | JsResult | 否 | 否 | 通知Web组件用户的操作结果。 |

#### OnPromptEvent12+

定义网页触发 prompt() 弹窗时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 当前显示弹窗的网页的URL。 |
| message | string | 否 | 否 | 显示在弹窗中的信息。 |
| value | string | 否 | 否 | 对话框默认返回的信息。 |
| result | JsResult | 否 | 否 | 通知Web组件用户的操作结果。 |

#### OnConsoleEvent12+

定义通知宿主应用JavaScript console消息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | ConsoleMessage | 否 | 否 | 触发的控制台信息。 |

#### OnErrorReceiveEvent12+

定义网页加载遇到错误时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Request | 否 | 否 | 网页请求的封装信息。 |
| error | Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Error | 否 | 否 | 网页加载资源错误的封装信息 。 |

#### OnHttpErrorReceiveEvent12+

定义网页收到加载资源加载HTTP错误时触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Request | 否 | 否 | 网页请求的封装信息。 |
| response | Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Response | 否 | 否 | 资源响应的封装信息。 |

#### OnDownloadStartEvent12+

定义通知主应用开始下载一个文件。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 文件下载的URL。 |
| userAgent | string | 否 | 否 | 用于下载的用户代理。 |
| contentDisposition | string | 否 | 否 | 服务器返回的 Content-Disposition响应头，服务器可能返回空。 |
| mimetype | string | 否 | 否 | 服务器返回内容媒体类型（MIME）信息。 |
| contentLength | number | 否 | 否 | 服务器返回文件的长度。 |

#### OnRefreshAccessedHistoryEvent12+

定义导航完成时触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 访问的url。 |
| isRefreshed | boolean | 否 | 否 | true表示该页面是被重新加载的（调用refresh9+[接口](../../topics/misc/组件描述.md#ZH-CN_TOPIC_0000002529445171__接口)），false表示该页面是新加载的。 |
| isMainFrame22+ | boolean | 否 | 是 | 是否是主文档触发。 true表示是主文档触发，false表示不是主文档触发。 |

#### OnRenderExitedEvent12+

定义渲染过程退出时触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| renderExitReason | [RenderExitReason](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__renderexitreason9) | 否 | 否 | 渲染进程异常退出的具体原因。 |

#### OnShowFileSelectorEvent12+

定义文件选择器结果。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | FileSelectorResult | 否 | 否 | 用于通知Web组件文件选择的结果。 |
| fileSelector | FileSelectorParam | 否 | 否 | 文件选择器的相关信息。 |

#### On[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)LoadEvent12+

定义加载url时触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 所加载的资源文件url信息。 |

#### OnScaleChangeEvent12+

定义当前页面显示比例的变化时触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| oldScale | number | 否 | 否 | 变化前的显示比例百分比。 |
| newScale | number | 否 | 否 | 变化后的显示比例百分比。 |

#### OnHttpAuthRequestEvent12+

定义通知收到http auth认证请求。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | HttpAuthHandler | 否 | 否 | 通知Web组件用户操作行为。 |
| host | string | 否 | 否 | HTTP身份验证凭据应用的主机。 |
| realm | string | 否 | 否 | HTTP身份验证凭据应用的域。 |

#### OnInterceptRequestEvent12+

定义当Web组件加载url之前触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Request | 否 | 否 | url请求的相关信息。 |

#### OnPermissionRequestEvent12+

定义通知收到获取权限请求。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | PermissionRequest | 否 | 否 | 通知Web组件用户操作行为。 |

#### OnScreenCaptureRequestEvent12+

定义通知收到屏幕捕获请求。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | ScreenCaptureHandler | 否 | 否 | 通知Web组件用户操作行为。 |

#### OnContextMenuShowEvent12+

定义调用时触发的回调，以允许自定义显示上下文菜单。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| param | WebContextMenuParam | 否 | 否 | 菜单相关参数。 |
| result | WebContextMenuResult | 否 | 否 | 菜单相应事件传入内核。 |

#### OnSearchResultReceiveEvent12+

定义通知调用方网页页内查找的结果。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| activeMatchOrdinal | number | 否 | 否 | 当前匹配的查找项的序号（从0开始）。 |
| numberOfMatches | number | 否 | 否 | 所有匹配到的关键词的个数。 |
| isDoneCounting | boolean | 否 | 否 | 当次页内查找操作是否结束。 true表示当次页内查找操作结束，false表示当次页内查找操作未结束。 该方法可能会回调多次，直到isDoneCounting为true为止。 |

#### OnScrollEvent12+

定义滚动条滑动到指定位置时触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xOffset | number | 否 | 否 | 以网页最左端为基准，水平滚动条滚动所在位置。 单位：vp。 |
| yOffset | number | 否 | 否 | 以网页最上端为基准，竖直滚动条滚动所在位置。 单位：vp。 |

#### On[SslError](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9)EventReceiveEvent12+

定义网页收到SSL错误时触发。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | [SslError](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9)Handler | 否 | 否 | 通知Web组件用户操作行为。 |
| error | [SslError](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9) | 否 | 否 | 错误码。 |
| certChainData15+ | Array<Uint8Array> | 否 | 是 | 证书链数据。 |

#### [SslError](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9)Event12+

用户加载资源时发生SSL错误时触发的回调详情。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | [SslError](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9)Handler | 否 | 否 | 通知Web组件用户操作行为。 |
| error | [SslError](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__sslerror9) | 否 | 否 | 错误码。 |
| url | string | 否 | 否 | url地址。 |
| originalUrl | string | 否 | 否 | 请求的原始url地址。 |
| referrer | string | 否 | 否 | referrer url地址。 |
| isFatalError | boolean | 否 | 否 | 是否是致命错误。 true表示致命错误，false表示非致命错误。 |
| isMainFrame | boolean | 否 | 否 | 是否是主资源。 true表示主资源，false表示非主资源。 |
certChainData20+Array<Uint8Array>否是证书链数据。

#### OnClientAuthenticationEvent12+

定义当需要用户提供SSL客户端证书时触发回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | ClientAuthenticationHandler | 否 | 否 | 通知Web组件用户操作行为。 |
| host | string | 否 | 否 | 请求证书服务器的主机名。 |
| port | number | 否 | 否 | 请求证书服务器的端口号。 |
| keyTypes | Array<string> | 否 | 否 | 可接受的非对称秘钥类型。 |
| issuers | Array<string> | 否 | 否 | 与私钥匹配的证书可接受颁发者。 |

#### VerifyPinEvent22+

定义当需要用户进行PIN码认证时触发回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | VerifyPinHandler | 否 | 否 | 通知Web组件用户操作行为。 |
| identity | string | 否 | 否 | 用于认证的证书凭据标识。 |

#### OnWindowNewEvent12+

定义网页要求用户创建窗口时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isAlert | boolean | 否 | 否 | true代表请求创建对话框，false代表新标签页。 |
| isUserTrigger | boolean | 否 | 否 | true代表用户触发，false代表非用户触发。 |
| targetUrl | string | 否 | 否 | 目标url。 |
| handler | ControllerHandler | 否 | 否 | 用于设置新建窗口的WebviewController实例。 |

**WindowFeatures23+**

网页请求创建的新窗口特征信息，包括大小和位置。

系统能力： SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 新窗口左上角横坐标（单位：像素）。 |
| y | number | 否 | 否 | 新窗口左上角纵坐标（单位：像素）。 |
| width | number | 否 | 否 | 新窗口宽度（单位：像素）。 |
| height | number | 否 | 否 | 新窗口高度（单位：像素）。 |

**OnWindowNewExtEvent23+**

定义网页请求用户创建窗口时触发的回调。

系统能力： SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isAlert | boolean | 否 | 否 | true代表请求创建对话框，false代表请求创建新标签页。 |
| isUserTrigger | boolean | 否 | 否 | true代表用户触发，false代表非用户触发。 |
| targetUrl | string | 否 | 否 | 请求的新窗口中需要打开的url。 |
| handler | ControllerHandler | 否 | 否 | 用于设置新建窗口的WebviewController实例。 |
| windowFeatures | WindowFeatures | 否 | 否 | 网页请求创建的新窗口特征信息。 |
| navigationPolicy | NavigationPolicy | 否 | 否 | 网页请求用户创建新窗口时的窗口打开方式。 |

#### OnTouchIconUrlReceivedEvent12+

定义设置接收到apple-touch-icon url地址时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 接收到的apple-touch-icon url地址。 |
| precomposed | boolean | 否 | 否 | 对应apple-touch-icon是否为预合成。 true表示对应apple-touch-icon为预合成，false表示对应apple-touch-icon不是预合成。 |

#### OnFaviconReceivedEvent12+

定义应用为当前页面接收到新的favicon时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| favicon | PixelMap | 否 | 否 | 接收到的favicon图标的PixelMap对象。 |

#### OnPageVisibleEvent12+

定义旧页面不再呈现，新页面即将可见时触发的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 旧页面不再呈现，新页面即将可见时新页面的url地址。 |

#### OnDataResubmittedEvent12+

定义网页表单可以重新提交时触发的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | DataResubmissionHandler | 否 | 否 | 表单数据重新提交句柄。 |

#### OnAudioStateChangedEvent12+

定义网页上的音频播放状态发生改变时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| playing | boolean | 否 | 否 | 当前页面的音频播放状态，true表示正在播放，false表示未播放。 |

#### OnFirstContentfulPaintEvent12+

定义网页首次内容绘制回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| navigationStartTick | number | 否 | 否 | 启动页面加载开始的时间，单位以微秒表示。 |
| firstContentfulPaintMs | number | 否 | 否 | 从启动页面加载开始到第一次绘制内容的时间，单位是以毫秒表示。 |

#### OnLoadInterceptEvent12+

定义截获资源加载时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Web[Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Request | 否 | 否 | url请求的相关信息。 |

#### OnOverScrollEvent12+

定义网页过度滚动时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xOffset | number | 否 | 否 | 以网页最左端为基准，水平过度滚动的偏移量。 单位：vp。 |
| yOffset | number | 否 | 否 | 以网页最上端为基准，竖直过度滚动的偏移量。 单位：vp。 |

#### JavaScriptProxy12+

定义要注入的JavaScript对象。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| object | object | 否 | 否 | 参与注册的对象。只能声明方法，不能声明属性。 |
| name | string | 否 | 否 | 注册对象的名称，与window中调用的对象名一致。 |
| methodList | Array<string> | 否 | 否 | 参与注册的应用侧JavaScript对象的同步方法。 |
| controller | WebController | WebviewController9+ | 否 | 否 | 控制器。从API version 9开始，WebController不再维护，建议使用WebviewController替代。 |
| asyncMethodList12+ | Array<string> | 否 | 是 | 参与注册的应用侧JavaScript对象的异步方法。异步方法无法获取返回值。 |
| permission12+ | string | 否 | 是 | json字符串，默认为空，通过该字符串配置JSBridge的权限管控，可以定义object、method一级的url白名单。 JavaScriptProxy的permission参数支持resource/http/https协议，不支持file协议。 示例请参考前端页面调用应用侧函数。 |

#### OnPageEndEvent12+

定义网页加载结束时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |

#### OnPageBeginEvent12+

定义网页加载开始时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |

#### OnProgressChangeEvent12+

定义网页加载进度变化时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| newProgress | number | 否 | 否 | 新的加载进度，取值范围为0到100的整数。 |

#### OnTitleReceiveEvent12+

定义网页document标题更改时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | document标题内容。 |
| isRealTitle20+ | boolean | 否 | 是 | document标题来源，true表示来自网页的title标签，false表示该title是根据url自动生成。 默认值：false |

#### OnGeolocationShowEvent12+

定义通知用户收到地理位置信息获取请求。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| origin | string | 否 | 否 | 指定源的字符串索引。 |
| geolocation | JsGeolocation | 否 | 否 | 通知Web组件用户操作行为。 |

#### NativeEmbedVisibilityInfo12+

提供同层标签的可见性信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| visibility | boolean | 否 | 否 | 可见性。 true表示可见，false表示不可见。 |
embedIdstring否否同层渲染标签的唯一id。

#### RenderProcessNotRespondingData12+

提供渲染进程无响应的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| jsStack | string | 否 | 否 | 网页的javaScript调用栈信息。 |
| pid | number | 否 | 否 | 网页的进程id。 |
| reason | [RenderProcessNotRespondingReason](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__renderprocessnotrespondingreason12) | 否 | 否 | 触发渲染进程无响应回调的原因。 |

#### FullScreenEnterEvent12+

Web组件进入全屏回调事件的详情。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handler | FullScreenExitHandler | 否 | 否 | 用于退出全屏模式的函数句柄。 |
| videoWidth | number | 否 | 是 | 视频的宽度，单位：px。如果进入全屏的是 <video> 元素，表示其宽度；如果进入全屏的子元素中包含 <video> 元素，表示第一个子视频元素的宽度；其他情况下，为0。 |
| videoHeight | number | 否 | 是 | 视频的高度，单位：px。如果进入全屏的是 <video> 元素，表示其高度；如果进入全屏的子元素中包含 <video> 元素，表示第一个子视频元素的高度；其他情况下，为0。 |

#### LoadCommittedDetails11+

提供已提交跳转的网页的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isMainFrame | boolean | 否 | 否 | 是否是主文档。 true表示是主文档，false表示不是主文档。 |
| isSameDocument | boolean | 否 | 否 | 是否在不更改文档的情况下进行的网页跳转。 true表示在不更改文档的情况下进行的网页跳转，false表示在更改文档的情况下进行的网页跳转。 在同文档跳转的示例：1.参考片段跳转；2.pushState或replaceState触发的跳转；3.同一页面历史跳转。 |
| didReplaceEntry | boolean | 否 | 否 | 是否提交的新节点替换了已有的节点。 true表示提交的新节点替换了已有的节点，false表示提交的新节点未替换已有的节点。 另外在一些子文档跳转的场景，虽然没有实际替换已有节点，但是有一些属性发生了变更。 |
| navigationType | [WebNavigationType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__webnavigationtype11) | 否 | 否 | 网页跳转的类型。 |
| url | string | 否 | 否 | 当前跳转网页的URL。 |

#### [NativeEmbedInfo](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedinfo11)11+

提供同层标签的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 是 | 同层标签的id信息。 |
| type | string | 否 | 是 | 同层标签的type信息，统一为小写字符。 |
| src | string | 否 | 是 | 同层标签的src信息。 |
| width | number | 否 | 是 | 同层标签的宽，单位为px。 |
| height | number | 否 | 是 | 同层标签的高，单位为px。 |
| url | string | 否 | 是 | 同层标签的url信息。 |
| tag12+ | string | 否 | 是 | 标签名，统一为大写字符。 |
| params12+ | Map<string, string> | 否 | 是 | object标签包含的param标签键值对列表，该map本质为Object类型，请使用Object提供的方法操作该对象，即embed.info?.param?.["name"]。 |
| position12+ | Position | 否 | 是 | 同层标签相对于Web组件左上角为坐标原点的位置信息，此处区别于标准Position，单位为px。 |

#### [NativeEmbedParamItem](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedparamitem21)21+

提供同层渲染object标签内嵌param元素的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | [NativeEmbedParamStatus](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__nativeembedparamstatus21) | 否 | 否 | param元素的状态变化类型。 |
| id | string | 否 | 否 | param元素的id信息。 |
| name | string | 否 | 是 | param元素的参数名称。 |
| value | string | 否 | 是 | param元素的参数值。 |

#### IntelligentTrackingPreventionDetails12+

提供智能防跟踪拦截的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| host | string | 否 | 否 | 网站域名。 |
| trackerHost | string | 否 | 否 | 追踪者域名。 |

#### WebKeyboardCallbackInfo12+

拦截网页可编辑元素拉起软键盘的回调入参，其中包括[WebKeyboardController](Class (WebKeyboardController).md)、可编辑元素的属性。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | WebKeyboardController | 否 | 否 | 提供控制自定义键盘的输入、删除、关闭等操作。 |
| attributes | Record<string, string> | 否 | 否 | 触发本次软键盘弹出的网页元素属性。 |

#### WebKeyboardOptions12+

拦截网页可编辑元素拉起软键盘的回调返回值，可以指定使用的键盘类型，并返回给web内核，以控制拉起不同类型的软键盘；

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| useSystemKeyboard | boolean | 否 | 否 | 是否使用系统默认软键盘。 true表示使用系统默认软键盘，false表示不使用系统默认软键盘。 默认值：true。 |
| enterKeyType | number | 否 | 是 | 指定系统软键盘enter键的类型，取值范围见输入框架的定义EnterKeyType，该参数为可选参数，默认值为UNSPECIFIED。当useSystemKeyboard为true，并且设置了有效的enterKeyType时候，才有效。 |
| customKeyboard | [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | 否 | 是 | 指定自定义键盘组件builder，可选参数，当useSystemKeyboard为false时，需要设置该参数，然后Web组件会拉起该自定义键盘。 |

#### FirstMeaningfulPaint12+

提供网页绘制页面主要内容的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| navigationStartTime | number | 否 | 是 | 导航条加载时间，单位以微秒表示。 |
| firstMeaningfulPaintTime | number | 否 | 是 | 绘制页面主要内容时间，单位以毫秒表示。 |

#### LargestContentfulPaint12+

提供网页绘制页面最大内容的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| navigationStartTime | number | 否 | 是 | 导航条加载时间，单位以微秒表示。 |
| largestImagePaintTime | number | 否 | 是 | 最大图片加载的时间，单位是以毫秒表示。 |
| largestTextPaintTime | number | 否 | 是 | 最大文本加载时间，单位是以毫秒表示。 |
| largestImageLoadStartTime | number | 否 | 是 | 最大图片开始加载时间，单位是以毫秒表示。 |
| largestImageLoadEndTime | number | 否 | 是 | 最大图片结束加载时间，单位是以毫秒表示。 |
| imageBPP | number | 否 | 是 | 最大图片像素位数。 |

#### NativeEmbedDataInfo11+

提供同层标签生命周期变化的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | [NativeEmbedStatus](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__nativeembedstatus11) | 否 | 是 | 同层标签生命周期状态。 |
| surfaceId | string | 否 | 是 | NativeImage的psurfaceid。 |
| embedId | string | 否 | 是 | 同层标签的唯一id。 |
| info | [NativeEmbedInfo](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedinfo11) | 否 | 是 | 同层标签的详细信息。 |

#### NativeEmbedTouchInfo11+

提供手指触摸到同层标签的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| embedId | string | 否 | 是 | 同层标签的唯一id。 |
| touchEvent | [TouchEvent](../../topics/components/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明) | 否 | 是 | 手指触摸动作信息。 |
| result12+ | EventResult | 否 | 是 | 通知Web组件手势事件的消费结果。 |

#### NativeEmbedMouseInfo20+

提供鼠标/触摸板在同层标签上点击或长按的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| embedId | string | 否 | 是 | 同层标签的唯一id。 |
| mouseEvent | [MouseEvent](../../topics/components/鼠标事件.md#ZH-CN_TOPIC_0000002497604812__mouseevent对象说明) | 否 | 是 | 鼠标/触摸板点击/长按信息。 |
| result | EventResult | 否 | 是 | 通知Web组件鼠标事件的消费结果。 |

#### NativeEmbedParamDataInfo21+

提供同层渲染object标签内嵌param元素变化时同层标签的详细信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| embedId | string | 否 | 否 | 同层标签的唯一id。 |
| objectAttributeId | string | 否 | 是 | 同层标签的id信息。 |
| paramItems | Array<[NativeEmbedParamItem](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembedparamitem21)> | 否 | 是 | 发生变化的param元素的详细信息，包括每一个param元素的状态变化类型、id、参数名称和参数值。 |

#### OnLoadStartedEvent20+

定义网页加载开始时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |

#### OnLoadFinishedEvent20+

定义网页加载结束时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |

#### OnPdfLoadEvent20+

定义PDF加载成功或失败时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |
| result | [PdfLoadResult](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__pdfloadresult20) | 否 | 否 | PDF页面加载结果。 |

#### OnPdfScrollEvent20+

定义PDF页面滚动到底时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |

#### Header

Web组件返回的请求/响应头对象。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| headerKey | string | 否 | 否 | 请求/响应头的key。 |
| headerValue | string | 否 | 否 | 请求/响应头的value。 |

#### ScreenCaptureConfig10+

Web屏幕捕获的配置。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| captureMode | [WebCaptureMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__webcapturemode10) | 否 | 否 | Web屏幕捕获模式。 |

#### BlankScreenDetectionEventInfo22+

定义检测到白屏时的事件信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 检测到白屏时，页面的url。 |
| blankScreenReason | [DetectedBlankScreenReason](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__detectedblankscreenreason22) | 否 | 否 | 本次检测到白屏时，具体原因与检测的方法相关。 |
| blankScreenDetails | [BlankScreenDetails](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__blankscreendetails22) | 否 | 是 | 本次检测白屏的结果的细节。 如当发现近似白屏的现象产生，这个细节就包含具体命中了多少点。否则没有该属性。 |

#### [BlankScreenDetails](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__blankscreendetails22)22+

定义检测到白屏时的结果的细节。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| detectedContentfulNodesCount | number | 否 | 是 | 在使用到检测有内容的节点检测策略时，且开发者自己设置了检测到节点数量阈值时，可能包含该属性。否则没有该属性。 表示当前命中了多少有内容的节点。 |

#### BlankScreenDetectionConfig22+

定义白屏检测的策略配置选项。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enable | boolean | 否 | 否 | 是否使能白屏策略功能。 |
| detectionTiming | number[] | 否 | 是 | 用以设置需要在加载后多少秒的时机来检测是否白屏。 单位：秒。 注： 1.重复值会忽略。 2.需大于0，小于0的值会被忽略。 默认值：[1.0,3.0,5.0]。 |
| detectionMethods | [BlankScreenDetectionMethod](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__blankscreendetectionmethod22)[] | 否 | 是 | 使用检测策略的方法，是一个数组。 注： 1.重复值会忽略。 默认值：[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN]。 |
| contentfulNodesCountThreshold | number | 否 | 是 | 在使用到检测有内容的节点检测策略时，才会生效。 可以设置0-${检测策略最大节点}，如果小于等于阈值则会触发近似白屏。 默认值：0。 |

**CameraCaptureStateChangeInfo23+**

定义摄像头触发回调时的改变前后的状态信息。

系统能力： SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| originalState | CameraCaptureState | 否 | 否 | 原来的状态 |
| newState | CameraCaptureState | 否 | 否 | 改变后的状态 |

**MicrophoneCaptureStateChangeInfo23+**

定义麦克风触发回调时的改变前后的状态信息。

系统能力： SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| originalState | MicrophoneCaptureState | 否 | 否 | 原来的状态。 |
| newState | MicrophoneCaptureState | 否 | 否 | 改变后的状态。 |

**AcceptableFileType23+**

定义文件选择器拉取文件时网页推荐的文件类型信息。

系统能力： SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mimeType | string | 否 | 否 | 文件MIME类型。 |
| acceptableType | Array<string> | 否 | 否 | 文件类型数组，包含若干可供选择的文件类型。 |

**FirstScreenPaint23+**

检测到首屏渲染时的事件信息。

系统能力： SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 本次首屏渲染统计所对应的url。 |
| navigationStartTime | number | 否 | 否 | url所指页面开始导航的时刻。 |
| firstScreenPaintTime | number | 否 | 否 | url所指页面首屏绘制完成的时刻。 |