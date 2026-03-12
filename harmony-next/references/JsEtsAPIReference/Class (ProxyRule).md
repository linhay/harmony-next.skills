# Class (ProxyRule)

[insertProxyRule](Class (ProxyConfig).md#ZH-CN_TOPIC_0000002497605190__insertproxyrule15)中使用的代理规则。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 15开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### getSchemeFilter15+

getSchemeFilter(): ProxySchemeFilter

获取代理规则中的ProxySchemeFilter信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明[ProxySchemeFilter](Enums.md#ZH-CN_TOPIC_0000002529445167__proxyschemefilter15)代理规则中的ProxySchemeFilter信息。

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### getUrl15+

getUrl(): string

获取代理规则中的代理的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string代理规则中的代理的Url信息。

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。