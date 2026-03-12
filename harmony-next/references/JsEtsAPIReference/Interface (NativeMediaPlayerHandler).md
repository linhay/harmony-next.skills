# Interface (NativeMediaPlayerHandler)

[CreateNativeMediaPlayerCallback](Types.md#ZH-CN_TOPIC_0000002497605202__createnativemediaplayercallback12)回调函数的参数。应用通过该对象，将播放器的状态报告给ArkWeb内核。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Interface首批接口从API version 12开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### handleStatusChanged12+

handleStatusChanged(status: PlaybackStatus): void

当播放器的播放状态发生变化时，调用该方法将播放状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明status[PlaybackStatus](Enums.md#ZH-CN_TOPIC_0000002529445167__playbackstatus12)是播放器的播放状态。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleVolumeChanged12+

handleVolumeChanged(volume: number): void

当播放器的音量发生变化时，调用该方法将音量通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明volumenumber是播放器的音量，取值范围：[0, 1.0]。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleMutedChanged12+

handleMutedChanged(muted: boolean): void

当播放器的静音状态发生变化时，调用该方法将静音状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明mutedboolean是

当前播放器是否静音。

true表示当前播放器静音，false表示当前播放器未静音。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handlePlaybackRateChanged12+

handlePlaybackRateChanged(playbackRate: number): void

当播放器的播放速度发生变化时，调用该方法将播放速度通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明playbackRatenumber是播放速率，取值范围：[0, +∞)

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleDurationChanged12+

handleDurationChanged(duration: number): void

当播放器解析出媒体的总时长时，调用该方法将媒体的总时长通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明durationnumber是

媒体的总时长。

单位：秒，取值范围：[0, +∞)

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleTimeUpdate12+

handleTimeUpdate(currentPlayTime: number): void

当媒体的播放进度发生变化时，调用该方法将媒体的播放进度通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明currentPlayTimenumber是

当前播放时间。

单位：秒，取值范围：[0, duration]

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleBufferedEndTimeChanged12+

handleBufferedEndTimeChanged(bufferedEndTime: number): void

当媒体的缓冲时长发生变化时，调用该方法将媒体的缓冲时长通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明bufferedEndTimenumber是

媒体缓冲的时长。

单位：秒，取值范围：[0, duration]

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleEnded12+

handleEnded(): void

当媒体播放结束时，调用该方法通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleNetworkStateChanged12+

handleNetworkStateChanged(state: NetworkState): void

当播放器的网络状态发生变化时，调用该方法将播放器的网络状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明state[NetworkState](Enums.md#ZH-CN_TOPIC_0000002529445167__networkstate12)是播放器的网络状态。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleReadyStateChanged12+

handleReadyStateChanged(state: ReadyState): void

当播放器的缓存状态发生变化时，调用该方法将播放器的缓存状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明state[ReadyState](Enums.md#ZH-CN_TOPIC_0000002529445167__readystate12)是播放器的缓存状态。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleFullscreenChanged12+

handleFullscreenChanged(fullscreen: boolean): void

当播放器的全屏状态发生变化时，调用该方法将播放器的全屏状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明fullscreenboolean是

是否全屏。

true表示全屏，false表示未全屏。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleSeeking12+

handleSeeking(): void

当播放器进入seek 状态时，调用该方法通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleSeekFinished12+

handleSeekFinished(): void

当播放器 seek 完成后，调用该方法通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleError12+

handleError(error: MediaError, errorMessage: string): void

当播放器发生错误时， 调用该方法通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明error[MediaError](Enums.md#ZH-CN_TOPIC_0000002529445167__mediaerror12)是错误类型。errorMessagestring是错误的详细描述。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### handleVideoSizeChanged12+

handleVideoSizeChanged(width: number, height: number): void

当播放器解析出视频的尺寸时， 调用该方法通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明widthnumber是视频的宽，单位为像素，取值范围：[0, +∞)heightnumber是视频的高，单位为像素，取值范围：[0, +∞)

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。