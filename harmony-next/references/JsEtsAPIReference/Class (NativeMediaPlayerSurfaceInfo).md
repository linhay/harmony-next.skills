# Class (NativeMediaPlayerSurfaceInfo)

[应用接管网页媒体播放功能](属性.md#ZH-CN_TOPIC_0000002497605206__enablenativemediaplayer12)中用于同层渲染的 surface 信息。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 12开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### 属性

**系统能力：** SystemCapability.Web.Webview.Core

名称类型只读可选说明id12+string否否

surface的id，用于同层渲染的NativeImage的psurfaceid。

详见[NativeEmbedDataInfo](Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembeddatainfo11)。

rect12+[RectEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285193__rectevent12)否否surface的位置信息。