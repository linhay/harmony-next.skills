[]()[]()

# Types

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

[]()[]()

#### WebMessage

type WebMessage = ArrayBuffer | string

用于描述[WebMessagePort](../../types/interfaces/Interface (WebMessagePort).md)所支持的数据类型。

**系统能力：** SystemCapability.Web.Webview.Core

类型说明string字符串类型数据。ArrayBuffer二进制类型数据。[]()[]()

#### OnProxyConfigChangeCallback15+

type OnProxyConfigChangeCallback = () => void

回调函数，回调成功表示代理设置成功。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[removeProxyOverride](../../types/classes/Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

[]()[]()

#### CreateNativeMediaPlayerCallback12+

type CreateNativeMediaPlayerCallback = (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge

[onCreateNativeMediaPlayer](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)方法的参数。一个回调函数，创建一个播放器，用于接管网页中的媒体播放。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明handler[NativeMediaPlayerHandler](../../types/interfaces/Interface (NativeMediaPlayerHandler).md)是通过该对象，将播放器的状态报告给 ArkWeb 内核。mediaInfo[MediaInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-webview-i).md#ZH-CN_TOPIC_0000002529285193__mediainfo12)是网页媒体的信息。

**返回值：**

类型说明[NativeMediaPlayerBridge](../../types/interfaces/Interface (NativeMediaPlayerBridge).md)

接管网页媒体的播放器和 ArkWeb 内核之间的一个接口类。

应用需要实现该接口类。

 ArkWeb 内核通过该接口类的对象来控制应用创建的用来接管网页媒体的播放器。

如果应用返回了 null ， 则表示应用不接管这个媒体，由 ArkWeb 内核来播放该媒体。

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](../../types/classes/Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__oncreatenativemediaplayer12)。