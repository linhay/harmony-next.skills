# Class (JsMessageExt)

[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)接口执行脚本返回的数据对象。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 10开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### getType10+

getType(): JsMessageType

获取数据对象的类型。完整示例代码参考[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明[JsMessageType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445167__jsmessagetype10)[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)接口脚本执行后返回的结果的类型。

#### getString10+

getString(): string

获取数据对象的字符串类型数据。完整示例代码参考[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string返回字符串类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getNumber10+

getNumber(): number

获取数据对象的数值类型数据。完整示例代码参考[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明number返回数值类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getBoolean10+

getBoolean(): boolean

获取数据对象的布尔类型数据。完整示例代码参考[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明boolean返回布尔类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getArrayBuffer10+

getArrayBuffer(): ArrayBuffer

获取数据对象的原始二进制数据。完整示例代码参考[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明ArrayBuffer返回原始二进制数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getArray10+

getArray(): Array<string | number | boolean>

获取数据对象的数组类型数据。完整示例代码参考[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<string | number | boolean>返回数组类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getErrorDescription22+

getErrorDescription(): string | null

获取JS执行的异常信息。完整示例代码参考[runJavaScriptExt](Class (WebviewController).md#ZH-CN_TOPIC_0000002497605192__runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string | null若发生异常或返回类型不支持时，将其序列化为字符串类型并返回；否则，返回null。