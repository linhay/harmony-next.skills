# Class (ProxyConfig)

可以通过该类提供的接口对代理进行配置。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 15开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### insertProxyRule15+

insertProxyRule(proxyRule: string, schemeFilter?: ProxySchemeFilter): void

插入一条代理规则，与schemeFilter匹配的URL都会使用指定代理。如果schemeFilter为空，所有URL都将使用指定代理。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明proxyRulestring是URL要使用的代理。schemeFilter[ProxySchemeFilter](Enums.md#ZH-CN_TOPIC_0000002529445167__proxyschemefilter15)否

与schemeFilter匹配的URL会使用代理。

默认值：MATCH_ALL_SCHEMES。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### insertDirectRule15+

insertDirectRule(schemeFilter?: ProxySchemeFilter): void

插入一条代理规则，指明符合schemeFilter条件的URL将直接连接到服务器。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明schemeFilter[ProxySchemeFilter](Enums.md#ZH-CN_TOPIC_0000002529445167__proxyschemefilter15)否

与schemeFilter匹配的URL会直接与服务器相连。

默认值：MATCH_ALL_SCHEMES

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### insertBypassRule15+

insertBypassRule(bypassRule: string): void

插入一条bypass规则，指明哪些URL应该绕过代理并直接连接到服务器。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明bypassRulestring是与bypassRule匹配的URL会绕过代理。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### bypassHostnamesWithoutPeriod15+

bypassHostnamesWithoutPeriod(): void

没有点字符的域名将跳过代理并直接连接到服务器。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### clearImplicitRules15+

clearImplicitRules(): void

默认情况下，如果某些主机名是本地IP地址或localhost地址，它们会绕过代理。调用此函数以覆盖默认行为，并强制将localhost或本地IP地址通过代理发送。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### enableReverseBypass15+

enableReverseBypass(reverse: boolean): void

反转bypass规则。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明reverseboolean是参数值默认是false，表示与[insertBypassRule](#ZH-CN_TOPIC_0000002497605190__insertbypassrule15)中的bypassRule匹配的URL会绕过代理，参数值为true时，表示与[insertBypassRule](#ZH-CN_TOPIC_0000002497605190__insertbypassrule15)中的bypassRule匹配的URL会使用代理。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### getBypassRules15+

getBypassRules(): Array<string>

获取不使用代理的URL列表。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<string>不使用代理的URL列表。

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### getProxyRules15+

getProxyRules(): Array<ProxyRule>

获取代理规则。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<[ProxyRule](Class (ProxyRule).md)>代理规则。

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### isReverseBypassEnabled15+

isReverseBypassEnabled(): boolean

获取[enableReverseBypass](#ZH-CN_TOPIC_0000002497605190__enablereversebypass15)的参数值，详见[enableReverseBypass](#ZH-CN_TOPIC_0000002497605190__enablereversebypass15)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明boolean[enableReverseBypass](#ZH-CN_TOPIC_0000002497605190__enablereversebypass15)的参数值。参数值为false，表示与[insertBypassRule](#ZH-CN_TOPIC_0000002497605190__insertbypassrule15)中的bypassRule匹配的URL会绕过代理，参数值为true时，表示与[insertBypassRule](#ZH-CN_TOPIC_0000002497605190__insertbypassrule15)中的bypassRule匹配的URL会使用代理。

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。