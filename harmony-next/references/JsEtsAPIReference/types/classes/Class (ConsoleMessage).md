# Class (ConsoleMessage)

Web组件获取控制台信息对象。示例代码参考[onConsole事件](事件.md#ZH-CN_TOPIC_0000002522081170__onconsole)。


-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 8开始支持。

-

示例效果请以真机运行为准。

#### constructor(deprecated)

constructor(message: string, sourceId: string, lineNumber: number, messageLevel: [MessageLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__messagelevel))

ConsoleMessage的构造函数。


从API version 8开始支持，从API version 9开始废弃。建议使用[constructor](#ZH-CN_TOPIC_0000002522241168__constructor9)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | ConsoleMessage的日志输出信息。 |
| sourceId | string | 是 | 网页源文件的路径和文件名。 |
| lineNumber | number | 是 | ConsoleMessage的行号。 |
| messageLevel | [MessageLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__messagelevel) | 是 | ConsoleMessage的日志级别。 |

#### constructor9+

constructor()

ConsoleMessage的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getLineNumber

getLineNumber(): number

获取ConsoleMessage的行数。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回ConsoleMessage的行数。 |

#### getMessage

getMessage(): string

获取ConsoleMessage的日志信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回ConsoleMessage的日志信息。 |

#### get[MessageLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__messagelevel)

get[MessageLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__messagelevel)(): MessageLevel

获取ConsoleMessage的信息级别。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MessageLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__messagelevel) | 返回ConsoleMessage的信息级别。 |

#### getSourceId

getSourceId(): string

获取网页源文件路径和名字。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回网页源文件路径和名字。 |

**getSource23+**

getSource(): ConsoleMessageSource

获取ConsoleMessage的日志来源。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| ConsoleMessageSource | 返回ConsoleMessage的日志来源。 |