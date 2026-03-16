[]()[]()

# Enums

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### MessageLevel

ConsoleMessage的信息级别。

- 在html5侧，调用console.log或console.info对应ConsoleMessage的信息级别都为MessageLevel.Info。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明Debug1调试级别。Error4错误级别。Info2消息级别。Log5日志级别。Warn3警告级别。[]()[]()

#### MixedMode

混合内容模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明All0宽松模式：允许加载HTTP和HTTPS混合内容。所有不安全的内容都可以被加载。Compatible1兼容模式：混合内容兼容性模式，部分不安全的内容可能被加载。None2严格模式：不允许加载HTTP和HTTPS混合内容。[]()[]()

#### HitTestType(deprecated)

点击事件检测结果类型。

**系统能力：** SystemCapability.Web.Webview.Core

从API version9开始支持，从API version 21开始废弃。建议使用[WebHitTestType](../networking/Enums (arkts-apis-webview-e).md#ZH-CN_TOPIC_0000002529445167__webhittesttype)替代。

名称值说明EditText0可编辑的区域。Email1电子邮件地址。HttpAnchor2超链接，其src为http。HttpAnchorImg3带有超链接的图片，其中超链接的src为http。Img4HTML::img标签。Map5地理地址。Phone6电话号码。Unknown7未知内容。[]()[]()

#### CacheMode

缓存模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明Default9+0优先使用未过期cache加载资源，无效或无cache时从网络获取。None1优先使用cache(含过期)加载资源，无cache时从网络获取。Online2强制从网络获取最新资源，不使用任何cache。Only3仅使用本地cache加载资源。[]()[]()

#### OverScrollMode11+

设置Web的过滚动模式为关闭或开启。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NEVER0Web过滚动模式关闭。ALWAYS1Web过滚动模式开启。[]()[]()

#### BlurOnKeyboardHideMode14+

设置手动收起软键盘时Web元素是否失焦。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

名称值说明SILENT0软键盘收起时Web组件失焦功能关闭，当用户手动收起软键盘时焦点仍在文本框。BLUR1软键盘收起时Web组件失焦功能开启，当用户手动收起软键盘时，焦点会从文本框转移到Web的body上，文本框失焦。[]()[]()

#### WebDarkMode9+

Web深色模式的配置。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明Off0Web深色模式关闭。On1Web深色模式开启。Auto2Web深色模式跟随系统。[]()[]()

#### WebCaptureMode10+

Web屏幕捕获模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明HOME_SCREEN0主屏捕获模式。[]()[]()

#### ThreatType11+

定义网站风险类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明THREAT_ILLEGAL0非法网站。THREAT_FRAUD1欺诈网站。THREAT_RISK2存在安全风险的网站。THREAT_WARNING3涉嫌包含不健康内容的网站。THREAT_NONE21+4安全检查通过，未发现任何风险。THREAT_UNPROCESSED21+5未进行安全检查。[]()[]()

#### RenderExitReason9+

onRenderExited接口返回的渲染进程退出的具体原因。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明ProcessAbnormalTermination0渲染进程异常退出。ProcessWasKilled1收到SIGKILL，或被手动终止。ProcessCrashed2渲染进程崩溃退出，如段错误。ProcessOom3程序内存不足。ProcessExitUnknown4其他原因。[]()[]()

#### SslError9+

onSslErrorEventReceive接口返回的SSL错误的具体原因。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明Invalid0一般错误。HostMismatch1主机名不匹配。DateInvalid2证书日期无效。Untrusted3证书颁发机构不受信任。[]()[]()

#### FileSelectorMode9+

文件选择器的模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明FileOpenMode0打开上传单个文件。FileOpenMultipleMode1打开上传多个文件。FileOpenFolderMode2打开上传文件夹模式。FileSaveMode3文件保存模式。[]()[]()

#### WebLayoutMode11+

Web布局模式的配置。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NONE0Web布局跟随系统。FIT_CONTENT1Web基于页面大小的自适应网页布局。[]()[]()

#### RenderProcessNotRespondingReason12+

触发渲染进程无响应回调的原因。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明INPUT_TIMEOUT0发送给渲染进程的input事件响应超时。NAVIGATION_COMMIT_TIMEOUT1新的网页加载导航响应超时。[]()[]()

#### ProtectedResourceType9+

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明可申请的权限MidiSysexTYPE_MIDI_SYSEX

MIDI SYSEX资源。

目前仅支持权限事件上报，MIDI设备的使用还未支持。

暂不支持申请使用MIDI(Musical Instrument Digital Interface)设备相关权限。VIDEO_CAPTURE10+TYPE_VIDEO_CAPTURE视频捕获资源，例如相机。相机权限：ohos.permission.CAMERA。AUDIO_CAPTURE10+TYPE_AUDIO_CAPTURE音频捕获资源，例如麦克风。麦克风权限：ohos.permission.MICROPHONE。SENSOR12+TYPE_SENSOR传感器资源，例如加速度传感器。

加速度传感器权限：ohos.permission.ACCELEROMETER、

陀螺仪传感器权限：ohos.permission.GYROSCOPE。

[]()[]()

#### ContextMenuSourceType9+

触发上下文菜单的事件来源。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明None0其他事件来源。Mouse1鼠标事件。LongPress2长按事件。[]()[]()

#### ContextMenuMediaType9+

触发上下文菜单的网页元素类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明None0其他非图片媒体类型。Image1图片类型。[]()[]()

#### ContextMenuDataMediaType22+

触发上下文菜单的网页元素类型（增强获取类型能力）。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NONE0默认值，表示当前上下文菜单不关联任何媒体类型（例如右键文本或空白区域）。IMAGE1图片类型。VIDEO2视频类型。AUDIO3音频类型。CANVAS4Canvas类型。[]()[]()

#### ContextMenuInputFieldType9+

输入框类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明None0非输入框。PlainText1纯文本类型，包括text、search、email等。Password2密码类型。Number3数字类型。Telephone4电话号码类型。Other5其他类型。[]()[]()

#### NativeEmbedStatus11+

定义同层标签生命周期，当加载页面中有同层标签会触发CREATE，同层标签移动或者放大会触发UPDATE，退出页面会触发DESTROY。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明CREATE0同层标签创建。UPDATE1同层标签更新。DESTROY2同层标签销毁。ENTER_BFCACHE12+3同层标签进入BFCache。LEAVE_BFCACHE12+4同层标签离开BFCache。[]()[]()

#### NativeEmbedParamStatus21+

定义同层渲染object标签内嵌param元素的状态变化类型，当添加param元素时触发ADD，修改param元素属性触发UPDATE，删除param元素触发DELETE。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明ADD0添加param元素。UPDATE1更改param元素属性。DELETE2删除param元素。[]()[]()

#### ContextMenuEditStateFlags9+

支持以按位或的方式使用此枚举。例如，如果需要同时支持CAN_CUT、CAN_COPY和CAN_SELECT_ALL，可使用CAN_CUT | CAN_COPY | CAN_SELECT_ALL或11。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NONE0不可编辑。CAN_CUT1 << 0支持剪切。CAN_COPY1 << 1支持拷贝。CAN_PASTE1 << 2支持粘贴。CAN_SELECT_ALL1 << 3支持全选。[]()[]()

#### WebNavigationType11+

定义navigation类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明UNKNOWN0未知类型。MAIN_FRAME_NEW_ENTRY1主文档上产生的新的历史节点跳转。MAIN_FRAME_EXISTING_ENTRY2主文档上产生的到已有的历史节点的跳转。NAVIGATION_TYPE_NEW_SUBFRAME4子文档上产生的用户触发的跳转。NAVIGATION_TYPE_AUTO_SUBFRAME5子文档上产生的非用户触发的跳转。[]()[]()

#### RenderMode12+

定义Web组件的渲染方式，默认为异步渲染模式。

建议使用异步渲染模式，异步渲染模式有更好的性能和更低的功耗。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明ASYNC_RENDER0Web组件异步渲染模式，ArkWeb组件作为图形surface节点，独立送显，Web组件的宽度最大规格不超过7,680 px（物理像素）。SYNC_RENDER1Web组件同步渲染模式，ArkWeb组件作为图形canvas节点，跟随系统组件一起送显，可以渲染更长的Web组件内容，Web组件的宽度最大规格不超过500,000 px（物理像素）。[]()[]()

#### ViewportFit12+

网页meta中viewport-fit配置的视口类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明AUTO0默认值，整个网页可见。CONTAINS1初始布局视口和视觉视口为适应设备显示屏的最大矩形内。COVER2初始布局视口和视觉视口为设备物理屏幕的外接矩形内。[]()[]()

#### WebKeyboardAvoidMode12+

软键盘避让的模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明RESIZE_VISUAL0软键盘避让时，仅调整可视视口大小，不调整布局视口大小。RESIZE_CONTENT1默认值，软键盘避让时，同时调整可视视口和布局视口的大小。OVERLAYS_CONTENT2不调整任何视口大小，不会触发软键盘避让。RETURN_TO_UICONTEXT22+3Web组件的软键盘避让行为将跟随UIcontext设置的[KeyboardAvoidMode](../graphics/Enums (arkts-apis-uicontext-e).md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11)模式，Web组件不再处理组件的避让。[]()[]()

#### WebElementType13+

网页元素信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

名称值说明IMAGE1网页元素为图像类型。LINK20+2网页元素为超链接类型。TEXT21+3网页元素为文本或可编辑区域类型。[]()[]()

#### WebResponseType13+

菜单的响应类型。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

名称值说明LONG_PRESS1通过长按触发菜单弹出。RIGHT_CLICK21+2通过鼠标右键触发菜单弹出。[]()[]()

#### AudioSessionType20+

应用中Web音频类型。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

名称值说明AMBIENT3适用于网页游戏场景，支持Web游戏声音与系统音乐同时播放。对应系统音频流类型STREAM_USAGE_GAME。[]()[]()

#### GestureFocusMode20+

手势获焦的模式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明DEFAULT0默认值，Web会在触摸按下屏幕时申请获焦，包括点击、长按、滑动、缩放等任何触摸屏幕的手势行为。GESTURE_TAP_AND_LONG_PRESS1Web只会在点击和长按手势事件生成时申请获焦，点击和长按在触摸抬起之后生成，滑动和缩放等手势行为不会获焦。[]()[]()

#### WebRotateEffect22+

组件旋转时，宽高动画过程中组件内容如何填充以适应新尺寸的方式。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明TOPLEFT_EFFECT0默认值，组件旋转时，保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。RESIZE_COVER_EFFECT1组件旋转时，保持动画终态内容的宽高比进行缩小或放大，使内容两边都大于或等于组件两边，且与组件保持中心对齐，显示内容的中间部分。[]()[]()

#### WebBypassVsyncCondition20+

跳过渲染vsync条件。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NONE0默认值，按vsync调度流程绘制。SCROLLBY_FROM_ZERO_OFFSET1在使用scrollby（只支持带滚动偏移量）且Web页面滚动偏移量为0，渲染流程跳过vsync调度直接绘制。[]()[]()

#### PdfLoadResult20+

定义PDF页面的加载结果。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明LOAD_SUCCESS0PDF页面加载成功。PARSE_ERROR_FILE1PDF文件加载失败的错误码。PARSE_ERROR_FORMAT2PDF文件格式不支持的错误码。PARSE_ERROR_PASSWORD3PDF文件密码不正确的错误码。PARSE_ERROR_HANDLER4PDF文件处理失败的错误码。[]()[]()

#### DetectedBlankScreenReason22+

白屏的具体原因。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明NO_CONTENTFUL_NODES0

没有命中任何有内容的节点。

当检测策略为DETECTION_CONTENTFUL_NODES_SEVENTEEN时可能触发。

SUB_THRESHOLD_CONTENTFUL_NODES1

命中有内容节点的数量小于等于阈值。

当检测策略为DETECTION_CONTENTFUL_NODES_SEVENTEEN，且开发者设置了节点数量阈值contentfulNodesCountThreshold时可能触发。

[]()[]()

#### BlankScreenDetectionMethod22+

白屏检测使用的检测策略的方法。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明DETECTION_CONTENTFUL_NODES_SEVENTEEN0

以17点检测法进行页面检测。当检测点命中已经渲染了且有意义的节点，则认为有命中。有意义的节点指的是图片，视频和文字节点。

当无命中，或少于用户设置阈值命中时，则认为是白屏或者近似白屏。

其中，检测的17个点位包括：

中心点 (1个)： 位于页面的几何中心。

内部网格交点 (16个)：在页面区域内定义一个5×5 的均匀网格，这16个点即为页面内4条垂直等分线和4条水平等分线的交点。

[]()[]()

#### CredentialType22+

凭证类型。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明CREDENTIAL_USER2用户凭证。CREDENTIAL_APP3应用凭证。CREDENTIAL_UKEY4ukey凭证。[]()[]()

#### PinVerifyResult22+

PIN码认证结果。

**系统能力：** SystemCapability.Web.Webview.Core

名称值说明PIN_VERIFICATION_SUCCESS0成功。PIN_VERIFICATION_FAILED1失败。