# Class (PdfData)

createPdf函数输出数据流类。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 14开始支持。

-

示例效果请以真机运行为准。

-

在网页生成PDF过程中，返回的是数据流，由PdfData类封装。

#### pdfArrayBuffer14+

pdfArrayBuffer(): Uint8Array

获取网页生成的数据流。完整示例代码参考[createPdf](Class (WebviewController).md#ZH-CN_TOPIC_0000002553201117__createpdf14)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 数据流。 |