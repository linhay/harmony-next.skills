# Class (NativeMediaPlayerSurfaceInfo)

[应用接管网页媒体播放功能](属性.md#ZH-CN_TOPIC_0000002553201131__enablenativemediaplayer12)中用于同层渲染的 surface 信息。


-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 12开始支持。

-

示例效果请以真机运行为准。

#### 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id12+ | string | 否 | 否 | surface的id，用于同层渲染的NativeImage的psurfaceid。 详见[NativeEmbedDataInfo](../interfaces/Interfaces（其他）.md#ZH-CN_TOPIC_0000002529445183__nativeembeddatainfo11)。 |
| rect12+ | RectEvent | 否 | 否 | surface的位置信息。 |