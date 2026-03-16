# @ohos.xml (XML解析与生成)

本模块提供XML生成和解析的接口。

本模块提供了两种生成XML文件的方式:

- [XmlSerializer](#ZH-CN_TOPIC_0000002497444784__xmlserializer)：适用于已知XML文本大小的情况
- [XmlDynamicSerializer20+](#ZH-CN_TOPIC_0000002497444784__xmldynamicserializer20)：适用于未知XML文本大小的情况。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { xml } from '@kit.ArkTS';
```

#### XmlSerializer

XmlSerializer接口用于生成XML文件。

#### constructor

constructor(buffer: ArrayBuffer | DataView, encoding?: string)

XmlSerializer的构造函数。

buffer是开发者根据需要自定义大小的缓存区域，用于临时存储生成的XML文本。在使用过程中必须确保缓存区域足以容纳生成的文本内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明bufferArrayBuffer | DataView是用于接收写入XML信息的ArrayBuffer或DataView内存。encodingstring否编码格式，默认'utf-8'（目前仅支持'utf-8'）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer, "utf-8");
```

#### setAttributes

setAttributes(name: string, value: string): void

添加元素的属性和属性值。

该接口对所添加数据不做标准XML校验处理，确保所添加的数据符合标准XML规范。例如不允许添加数字开头的属性名称以及添加多个同名的属性名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是属性。valuestring是属性值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setAttributes("importance", "high");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high"/>
```

#### addEmptyElement

addEmptyElement(name: string): void

添加一个空元素。

该接口对所添加数据不做标准XML校验处理，确保所添加的数据符合标准XML规范。例如不允许添加数字开头的元素名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是元素的名称。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.addEmptyElement("d");
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <d/>
```

#### setDeclaration

setDeclaration(): void

设置带有编码信息的文件声明。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setDeclaration();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <?xml version="1.0" encoding="utf-8"?>
```

#### startElement

startElement(name: string): void

根据给定名称添加元素开始标记。

-

调用该接口后须调用[endElement](#ZH-CN_TOPIC_0000002497444784__endelement)写入元素结束标记，以确保节点正确闭合。

-

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是当前元素的元素名。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <note>Happy</note>
```

#### endElement

endElement(): void

添加元素结束标记。

调用该接口前必须先调用[startElement](#ZH-CN_TOPIC_0000002497444784__startelement)接口写入元素开始标记。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <note>Happy</note>
```

#### setNamespace

setNamespace(prefix: string, namespace: string): void

添加当前元素标记的命名空间。

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。例如禁止添加数字开头的前缀以及为同一个元素设置多个命名空间。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明prefixstring是当前元素及其子元素的前缀。namespacestring是当前元素及其子元素的命名空间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setNamespace("h", "http://www.w3.org/TR/html4/");
thatSer.startElement("note");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <h:note xmlns:h="http://www.w3.org/TR/html4/"/>
```

#### setComment

setComment(text: string): void

添加注释内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是当前元素的注释内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setComment("Hello, World!");
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!--Hello, World!-->
```

#### setCDATA

setCDATA(text: string): void

提供在CDATA标签中添加数据的能力，所生成的CDATA标签结构为："<![CDATA[" + 所添加的数据 + "]]>"。

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许在CDATA标签中添加包含"]]>"字符串的数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是CDATA属性的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setCDATA('root SYSTEM')
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <![CDATA[root SYSTEM]]>
```

#### setText

setText(text: string): void

添加标签值。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是text属性的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setAttributes("importance", "high");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high">Happy</note>
```

#### setDocType

setDocType(text: string): void

添加文档类型。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是DocType属性的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">
```

#### XmlDynamicSerializer20+

XmlDynamicSerializer类用于动态生成XML字符串。当无法确定XML内容长度时，推荐使用该类。

使用该类构造的对象无需自行创建ArrayBuffer，程序动态扩容，可以不断添加XML元素，最终序列化结果字符串长度上限为100000。

#### constructor20+

constructor(encoding?: string)

XmlDynamicSerializer的构造函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否编码格式，默认'utf-8'(目前仅支持'utf-8')。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200066Incorrect encoding format, only support utf-8.

**示例：**

```ets
let serializer = new xml.XmlDynamicSerializer('utf-8');
```

#### getOutput20+

getOutput(): ArrayBuffer

返回XML字符串的ArrayBuffer。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明ArrayBuffer用于接收写入XML信息的ArrayBuffer内存。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arr = serializer.getOutput();
let uint8 = new Uint8Array(arr);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>
```

#### setAttributes20+

setAttributes(name: string, value: string): void

写入元素的属性和属性值。

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的属性名称以及添加多个同名的属性名称。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是属性。所组成的XML长度不能超过100000，不可为空字符。valuestring是属性值。所组成的XML长度不能超过100000。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200063Illegal position for xml.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setAttributes("importance", "high");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high"/>
```

#### addEmptyElement20+

addEmptyElement(name: string): void

写入一个空元素。

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是该空元素的元素名。所组成的XML长度不能超过100000。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.addEmptyElement("d");
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <d/>
```

#### setDeclaration20+

setDeclaration(): void

编写带有编码的文件声明。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200063Illegal position for xml.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setDeclaration();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <?xml version="1.0" encoding="utf-8"?>
```

#### startElement20+

startElement(name: string): void

写入元素开始标记。

-

调用该接口后须调用[endElement](#ZH-CN_TOPIC_0000002497444784__endelement)写入元素结束标记，以确保节点正确闭合。

-

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是当前元素的元素名。所组成的XML长度不能超过100000。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>
```

#### endElement20+

endElement(): void

写入元素结束标记。

调用该接口前必须先调用[startElement](#ZH-CN_TOPIC_0000002497444784__startelement)接口写入元素开始标记。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200065There is no match between the startElement and the endElement.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>
```

#### setNamespace20+

setNamespace(prefix: string, namespace: string): void

写入当前元素标记的命名空间。

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的前缀以及对同一个元素设置多个命名空间。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明prefixstring是当前元素及其子元素的前缀。所组成的XML长度不能超过100000，不可为空字符。namespacestring是当前元素及其子元素的命名空间。所组成的XML长度不能超过100000，不可为空字符。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setNamespace("h", "http://www.w3.org/TR/html4/");
serializer.startElement("note");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <h:note xmlns:h="http://www.w3.org/TR/html4/"/>
```

#### setComment20+

setComment(text: string): void

写入注释内容。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是当前元素的注释内容。所组成的XML长度不能超过100000。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setComment("Hello, World!");
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!--Hello, World!-->
```

#### setCdata20+

setCdata(text: string): void

提供在CDATA标签中添加数据的能力，所生成的CDATA标签结构为："<![CDATA[" + 所添加的数据 + "]]>"。

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许在CDATA标签中添加包含"]]>"字符串的数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是CDATA属性的内容。所组成的XML长度不能超过100000。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setCdata('root SYSTEM')
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <![CDATA[root SYSTEM]]>
```

#### setText20+

setText(text: string): void

写入标签值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是标签值。所组成的XML长度不能超过100000。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setAttributes("importance", "high");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high">Happy</note>
```

#### setDocType20+

setDocType(text: string): void

写入文档类型。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是DocType属性的内容。所组成的XML长度不能超过100000。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200062The cumulative length of xml has exceeded the upper limit 100000.10200064Cannot be an empty string.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">
```

#### XmlPullParser

XmlPullParser接口用于解析现有的XML文件。

#### constructor

constructor(buffer: ArrayBuffer | DataView, encoding?: string)

构造并返回一个XmlPullParser对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明bufferArrayBuffer | DataView是用于解析的XML文本信息。encodingstring否编码格式，默认'utf-8'（目前仅支持'utf-8'）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml = '<title>Happy</title>'
let textEncoder = new util.TextEncoder();
let uint8Array = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(uint8Array.buffer as object as ArrayBuffer, 'UTF-8');
```

#### parseXml14+

parseXml(option: ParseOptions): void

解析XML。

**元服务API**：从API version 14 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明option[ParseOptions](#ZH-CN_TOPIC_0000002497444784__parseoptions)是XML解析选项。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

具体使用场景可参照[解析XML标签和标签值](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-parsing#解析xml标签和标签值)和[解析XML属性和属性值](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-parsing#解析xml属性和属性值)

```ets
import { xml, util } from '@kit.ArkTS';

let strxml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title><![CDATA[测试\n测试]]></title>' +
    '</note>';
let textEncoder = new util.TextEncoder();
let uint8 = textEncoder.encodeInto(strxml);

function func(key: xml.EventType, value: xml.ParseInfo) {
  if (key == xml.EventType.CDSECT) {
    console.info(JSON.stringify(value.getText()));
  }
  return true;
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
let pullParser = new xml.XmlPullParser(uint8.buffer as object as ArrayBuffer);
pullParser.parseXml(options);
// "测试\n测试"
```

#### parse(deprecated)

parse(option: ParseOptions): void

该接口用于解析XML。

从API version 8开始支持，从API version 14开始废弃，建议使用[parseXml14+](#ZH-CN_TOPIC_0000002497444784__parsexml14)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明option[ParseOptions](#ZH-CN_TOPIC_0000002497444784__parseoptions)是XML解析选项。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
    '<company>John &amp; Hans</company>' +
    '<title>Happy</title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
let str = '';
function func(name: string, value: string) {
  str = name + value;
  console.info(str);
  return true;
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tagValueCallbackFunction:func}
that.parse(options);
// note
// company
// John & Hans
// company
// title
// Happy
// title
// note
```

#### AttributeWithTagCb20+

type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明tagNamestring是标签名称。keystring是属性名称。valuestring是属性的值。

**返回值：**

类型说明boolean是否继续解析标签名称、属性名称及属性的值。true表示继续解析，false表示停止解析。

#### ParseOptions

XML解析选项。

**系统能力：** SystemCapability.Utils.Lang。

名称类型只读可选说明supportDoctypeboolean否是

是否解析文档类型，false表示不解析文档类型，true表示解析文档类型，默认值false。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

ignoreNameSpaceboolean否是

是否忽略命名空间，忽略命名空间后，将不会对其进行解析。true表示忽略命名空间，false表示不忽略命名空间，默认值false。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

tagValueCallbackFunction(name: string, value: string) => boolean否是

解析开始标签、标签值和结束标签，默认值undefined，表示不解析。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

attributeValueCallbackFunction(name: string, value: string) => boolean否是

解析属性和属性值，默认值undefined，表示不解析。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

tokenValueCallbackFunction(eventType: [EventType](#ZH-CN_TOPIC_0000002497444784__eventtype), value: [ParseInfo](#ZH-CN_TOPIC_0000002497444784__parseinfo)) => boolean否是

解析元素事件类型([EventType](#ZH-CN_TOPIC_0000002497444784__eventtype))和[ParseInfo](#ZH-CN_TOPIC_0000002497444784__parseinfo)属性，默认值undefined，表示不解析。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

attributeWithTagCallbackFunction20+[AttributeWithTagCb](#ZH-CN_TOPIC_0000002497444784__attributewithtagcb20)否是

解析标签名称、属性名称及属性的值，默认值为undefined，表示不执行解析。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

#### ParseInfo

当前XML解析信息。

#### getColumnNumber

getColumnNumber(): number

获取当前列号，从1开始计数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回当前列号。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getColumnNumber() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:1 key:2 value:45 key:4 value:50 key:3 value:57 key:1 value:57
```

#### getDepth

getDepth(): number

获取元素的当前深度。

标签内的空白事件深度与标签的深度保持一致。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回元素的当前深度。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high">' +
    '<title>Happy</title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getDepth() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:0 key:2 value:1 key:2 value:2 key:4 value:2 key:3 value:2 key:3 value:1 key:1 value:0
```

#### getLineNumber

getLineNumber(): number

获取当前行号，从1开始。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回当前行号。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Work</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getLineNumber() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:1 key:2 value:1 key:4 value:1 key:3 value:1 key:1 value:1
```

#### getName

getName(): string

获取当前元素名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回当前元素名称。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getName() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value:note key:4 value: key:3 value:note key:1 value:
```

#### getNamespace

getNamespace(): string

获取当前元素的命名空间。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回当前元素的命名空间。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note xmlns:h="http://www.w3.org">' +
    '<h:title>Happy</h:title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getNamespace() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:false, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value: key:2 value:http://www.w3.org key:4 value: key:3 value:http://www.w3.org key:3 value: key:1 value:
```

#### getPrefix

getPrefix(): string

获取当前元素前缀。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回当前元素前缀。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note xmlns:h="http://www.w3.org/TR/html4">' +
    '<h:title>Happy</h:title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getPrefix() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:false, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value: key:2 value:h key:4 value: key:3 value:h key:3 value: key:1 value:
```

#### getText

getText(): string

获取当前事件的文本内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回当前事件的文本内容。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getText() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value: key:4 value:Happy key:3 value: key:1 value:
```

#### isEmptyElementTag

isEmptyElementTag(): boolean

判断当前元素是否为空元素。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回true，表示当前元素为空元素。返回false，表示当前元素为非空元素。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
    '<title/>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.isEmptyElementTag() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:false key:2 value:false key:2 value:true key:3 value:false key:3 value:false key:1 value:false
```

#### isWhitespace

isWhitespace(): boolean

判断当前事件是否仅包含空格字符。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回true，表示当前文本事件仅包含空格字符。返回false，表示当前文本事件包含非空格字符。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
    '<title> </title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.isWhitespace() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:true key:2 value:false key:2 value:true key:10 value:true key:3 value:true key:3 value:true key:1 value:true
```

#### getAttributeCount

getAttributeCount(): number

获取当前开始标记的属性数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number当前开始标记的属性数。

**示例：**

```ets
import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note importance="high" logged="true"/>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getAttributeCount() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:0 key:2 value:2 key:3 value:2 key:1 value:0
```

#### EventType

事件类型枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称值说明START_DOCUMENT0启动文件事件。END_DOCUMENT1结束文件事件。START_TAG2启动标签事件。END_TAG3结束标签事件。TEXT4文本事件。CDSECT5CDATA事件。COMMENT6XML注释事件。DOCDECL7XML文档类型声明事件。INSTRUCTION8XML处理指令声明事件。ENTITY_REFERENCE9实体引用事件。WHITESPACE10空白事件。