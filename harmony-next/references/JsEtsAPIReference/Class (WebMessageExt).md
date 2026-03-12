# Class (WebMessageExt)

[WebMessagePort](Interface (WebMessagePort).md)接口接收、发送的数据对象。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 10开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### getType10+

getType(): WebMessageType

获取数据对象的类型。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明[WebMessageType](Enums.md#ZH-CN_TOPIC_0000002529445167__webmessagetype10)[webMessagePort](Interface (WebMessagePort).md)接口所支持的数据类型。

#### getString10+

getString(): string

获取数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明string返回字符串类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getNumber10+

getNumber(): number

获取数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明number返回数值类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getBoolean10+

getBoolean(): boolean

获取数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明boolean返回布尔类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getArrayBuffer10+

getArrayBuffer(): ArrayBuffer

获取数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明ArrayBuffer返回原始二进制数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getArray10+

getArray(): Array<string | number | boolean>

获取数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Array<string | number | boolean>返回数组类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### getError10+

getError(): Error

获取数据对象的错误类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Error返回错误对象类型的数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.

#### setType10+

setType(type: WebMessageType): void

设置数据对象的类型。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明type[WebMessageType](Enums.md#ZH-CN_TOPIC_0000002529445167__webmessagetype10)是[webMessagePort](Interface (WebMessagePort).md)接口所支持的数据类型。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

#### setString10+

setString(message: string): void

设置数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明messagestring是字符串类型数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

#### setNumber10+

setNumber(message: number): void

设置数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明messagenumber是数值类型数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

#### setBoolean10+

setBoolean(message: boolean): void

设置数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明messageboolean是布尔类型数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

#### setArrayBuffer10+

setArrayBuffer(message: ArrayBuffer): void

设置数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明messageArrayBuffer是原始二进制类型数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

#### setArray10+

setArray(message: Array<string | number | boolean>): void

设置数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明messageArray<string | number | boolean>是数组类型数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

#### setError10+

setError(message: Error): void

设置数据对象的错误对象类型数据。完整示例代码参考[onMessageEventExt](Interface (WebMessagePort).md#ZH-CN_TOPIC_0000002497445222__onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明messageError是错误对象类型数据。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

错误码ID错误信息17100014The type and value of the message do not match.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.