# Class (PrefetchOptions)

用来自定义网页的预取行为，包括是否忽略响应头中的Cache-Control: no-store和设置两次预取间的最小时间间隔。

-

本模块接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 21开始支持。

-

示例效果请以真机运行为准。

#### 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minTimeBetweenPrefetchesMs21+ | number | 否 | 否 | 设置两次网页预取的最小时间间隔。 每次预取时会计算和上次预取的间隔时间，若小于设置值，则取消本次预取。 默认为500，最大值为500。 设置为负数时，默认为0。 |
| ignoreCacheControlNoStore21+ | boolean | 否 | 否 | 设置是否忽略响应头中的Cache-Control: no-store。 默认值：false  设置为true时，会忽略响应头中的Cache-Control: no-store，为false时不会。 |

#### constructor21+

constructor()

PrefetchOptions的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core