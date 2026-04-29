# @ohos.convertxml (xml转换JavaScript)

本模块提供将XML文本转换为JavaScript对象的解析能力。


本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { convertxml } from '@kit.ArkTS';
```

#### ConvertXML

#### fastConvertToJSObject14+

fastConvertToJSObject(xml: string, options?: ConvertOptions) : Object

转换XML文本为Object类型对象。


该接口无法满足解析大数据量的XML文件，当单元素文本内容超过10M时，会打印异常信息并返回一个仅包含XML标签头的基础Object对象。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。fastConvertToJSObject接口转换后的对象以换行符（LF）表示换行。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | ConvertOptions | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[语言基础类库错误码]([语言基础类库错误码](../../errors/语言基础类库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200002 | Invalid xml string. |

**示例：**

```ets
try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '   <title>Hello\r\nWorld</title>' +
    '   <todo><![CDATA[Work\r\n]]></todo>' +
    '</note>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  let result = JSON.stringify(conv.fastConvertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Hello\nWorld"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"cdata","_cdata":"Work\n"}]}]}]}
```

**largeConvertToJSObject23+**

largeConvertToJSObject(xml: string, options?: ConvertOptions): Object

将XML文本转换为Object类型对象，此方法支持解析单个节点大小超过10M的大型XML文本。


当传入的XML文本无法正确解析为Object类型对象时，打印异常信息并返回一个仅包含XML标签头的基础Object对象。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

元服务API：从API version 23开始，该接口支持在元服务中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Utils.Lang

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | ConvertOptions | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象。 |

错误码：

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200002 | Invalid xml string. |

示例：

```ets
try {
  let xmlstr =
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<?custom-pi processing="example"?>' +
    '<catalog id="books">' +
      '<!-- Bestseller Example -->' +
      '<book category="fiction" ref="B101">' +
        '<title>Echoes &amp; Whispers</title>' +
        '<price unit="USD">19.99</price>' +
        '<descr>' +
          '<![CDATA[<b>suspense</b>novel & Legendary Stories]]>' +
        '</descr>' +
        '<popular/>' +
      '</book>' +
    '</catalog>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  let result = JSON.stringify(conv.largeConvertToJSObject(xmlstr, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"instruction","_name":"custom-pi","_instruction":"processing=\"example\""},{"_type":"element","_name":"catalog","_attributes":{"id":"books"},"_elements":[{"_type":"comment","_comment":" Bestseller Example "},{"_type":"element","_name":"book","_parent":"catalog","_attributes":{"category":"fiction","ref":"B101"},"_elements":[{"_type":"element","_name":"title","_parent":"book","_elements":[{"_type":"text","_text":"Echoes & Whispers"}]},{"_type":"element","_name":"price","_parent":"book","_attributes":{"unit":"USD"},"_elements":[{"_type":"text","_text":"19.99"}]},{"_type":"element","_name":"descr","_parent":"book","_elements":[{"_type":"cdata","_cdata":"<b>suspense</b>novel & Legendary Stories"}]},{"_type":"element","_name":"popular","_parent":"book"}]}]}]}
```

#### convertToJSObject(deprecated)

convertToJSObject(xml: string, options?: ConvertOptions) : Object

转换XML文本为Object类型对象。


从API version 9开始支持，从API version 14开始废弃，建议使用[fastConvertToJSObject14+](#ZH-CN_TOPIC_0000002522080700__fastconverttojsobject14)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | 传入的XML文本，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | ConvertOptions | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 处理后返回的JavaScript对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200002 | Invalid xml string. |

**示例：**

```ets
try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
      '<note importance="high" logged="true">' +
      '    <title>Happy</title>' +
      '    <todo>Work</todo>' +
      '    <todo>Play</todo>' +
      '</note>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  let result = JSON.stringify(conv.convertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

#### convert(deprecated)

convert(xml: string, options?: ConvertOptions) : Object

转换XML文本为JavaScript对象。


从API version 8开始支持，从API version 9开始废弃，建议使用[fastConvertToJSObject14+](#ZH-CN_TOPIC_0000002522080700__fastconverttojsobject14)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | 传入的XML文本。 |
| options | ConvertOptions | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 处理后返回的JavaScript对象。 |

**示例：**

```ets
let xml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title>Happy</title>' +
    '    <todo>Work</todo>' +
    '    <todo>Play</todo>' +
    '</note>';
let conv = new convertxml.ConvertXML();
let options: convertxml.ConvertOptions = {
  trim: false,
  declarationKey: "_declaration",
  instructionKey: "_instruction",
  attributesKey: "_attributes",
  textKey: "_text",
  cdataKey: "_cdata",
  doctypeKey: "_doctype",
  commentKey: "_comment",
  parentKey: "_parent",
  typeKey: "_type",
  nameKey: "_name",
  elementsKey: "_elements"
};
let result = JSON.stringify(conv.convert(xml, options));
console.info(result);
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

#### ConvertOptions

转换选项。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trim | boolean | 否 | 否 | 是否修剪位于文本前后的空白字符，true表示xml文本前后的空白字符将会被修剪，false则表示空白字符会被保留。 |
| ignoreDeclaration | boolean | 否 | 是 | 是否忽略xml写入声明指示，true表示忽略xml写入声明指示，false则相反，默认false。 |
| ignoreInstruction | boolean | 否 | 是 | 是否忽略xml的写入处理指令，true表示忽略xml的写入处理指令，false则相反，默认false。 |
| ignoreAttributes | boolean | 否 | 是 | 是否忽略元素的属性信息，true表示忽略元素的属性信息，false则相反，默认false。 |
| ignoreComment | boolean | 否 | 是 | 是否忽略元素的注释信息，true表示忽略元素的注释信息，false则相反，默认false。 |
| ignoreCDATA | boolean | 否 | 是 | 是否忽略元素的CDATA信息，true表示忽略元素的CDATA信息，false则相反，默认false。 |
| ignoreDoctype | boolean | 否 | 是 | 是否忽略元素的Doctype信息，true表示忽略元素的Doctype信息，false则相反，默认false。 |
| ignoreText | boolean | 否 | 是 | 是否忽略元素的文本信息，true表示忽略元素的文本信息，false则相反，默认false。 |
| declarationKey | string | 否 | 否 | 用于输出对象中declaration的属性键的名称。 |
| instructionKey | string | 否 | 否 | 用于输出对象中instruction的属性键的名称。 |
| attributesKey | string | 否 | 否 | 用于输出对象中attributes的属性键的名称。 |
| textKey | string | 否 | 否 | 用于输出对象中text的属性键的名称。 |
| cdataKey | string | 否 | 否 | 用于输出对象中cdata的属性键的名称 |
| doctypeKey | string | 否 | 否 | 用于输出对象中doctype的属性键的名称。 |
| commentKey | string | 否 | 否 | 用于输出对象中comment的属性键的名称。 |
| parentKey | string | 否 | 否 | 用于输出对象中parent的属性键的名称。 |
| typeKey | string | 否 | 否 | 用于输出对象中type的属性键的名称。 |
| nameKey | string | 否 | 否 | 用于输出对象中name的属性键的名称。 |
| elementsKey | string | 否 | 否 | 用于输出对象中elements的属性键的名称。 |