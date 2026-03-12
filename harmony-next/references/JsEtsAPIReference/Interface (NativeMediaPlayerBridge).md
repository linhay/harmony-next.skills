# Interface (NativeMediaPlayerBridge)

[CreateNativeMediaPlayerCallback](Types.md#ZH-CN_TOPIC_0000002497605202__createnativemediaplayercallback12)回调函数的返回值类型。接管网页媒体的播放器和 ArkWeb 内核之间的一个接口类。

ArkWeb 内核通过该接口类的实例对象来控制应用创建的用来接管网页媒体的播放器。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Interface首批接口从API version 12开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### updateRect12+

updateRect(x: number, y: number, width: number, height: number): void

更新 surface 位置信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明xnumber是surface相对于Web组件的x坐标信息。ynumber是surface相对于Web组件的y坐标信息。widthnumber是

surface的宽度。

单位：像素。

heightnumber是

surface的高度。

单位：像素。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### play12+

play(): void

播放视频。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### pause12+

pause(): void

暂停播放。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### seek12+

seek(targetTime: number): void

播放跳转到某个时间点。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明targetTimenumber是

播放跳转到的时间点。

单位：秒。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### setVolume12+

setVolume(volume: number): void

设置播放器音量值。

**参数：**

参数名类型必填说明volumenumber是

播放器的音量。

取值范围:[0, 1.0]，其中0表示静音，1.0表示最大音量。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### setMuted12+

setMuted(muted: boolean): void

设置静音状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明mutedboolean是

是否静音。

true表示静音，false表示未静音。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### setPlaybackRate12+

setPlaybackRate(playbackRate: number): void

设置播放速度。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明playbackRatenumber是

播放倍率。

取值范围: [0, 10.0]，其中1表示原速播放。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### release12+

release(): void

销毁播放器。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### enterFullscreen12+

enterFullscreen(): void

播放器进入全屏。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### exitFullscreen12+

exitFullscreen(): void

播放器退出全屏。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### resumePlayer12+

resumePlayer?(): void

通知应用重建应用内播放器，并恢复应用内播放器的状态信息。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。

#### suspendPlayer12+

suspendPlayer?(type: SuspendType): void

通知应用销毁应用内播放器，并保存应用内播放器的状态信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明type[SuspendType](Enums.md#ZH-CN_TOPIC_0000002529445167__suspendtype12)是播放器挂起类型。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。