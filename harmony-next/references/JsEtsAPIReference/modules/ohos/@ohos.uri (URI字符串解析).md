# @ohos.uri (URI字符串解析)

本模块提供URI字符串解析功能。URI遵循RFC3986规范标准，该规范定义了编码和解析网络资源标识符的方法，不支持非标准场景解析。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { uri } from '@kit.ArkTS';
```

#### URI

构造一个URI对象，并提供判断两个URI是否相等、对URI路径部分进行编码规范化等方法。

#### 属性

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scheme | string | 否 | 否 | 获取和设置URI的协议部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| userInfo | string | 否 | 否 | 获取和设置URI的用户信息部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| host | string | 是 | 否 | 获取URI的主机名部分（不带端口），若无此部分则返回null对象。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| port | string | 是 | 否 | 获取URI的端口部分。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| path | string | 否 | 否 | 获取和设置URI的路径部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| query | string | 否 | 否 | 获取和设置URI的查询部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fragment | string | 否 | 否 | 获取和设置URI的片段部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| authority | string | 否 | 否 | 获取和设置此URI的解码权限组件部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| ssp | string | 否 | 否 | 获取和设置URI的解码方案特定部分，方案特定部分是URI的一部分，它包含了特定于协议或方案的信息。 此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| encodedUserInfo12+ | string | 否 | 否 | 获取和设置URI的编码用户信息部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| encodedPath12+ | string | 否 | 否 | 获取和设置URI的编码路径部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| encodedQuery12+ | string | 否 | 否 | 获取和设置URI的编码查询部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| encodedFragment12+ | string | 否 | 否 | 获取和设置URI的编码片段部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| encodedAuthority12+ | string | 否 | 否 | 获取和设置URI的编码权限组件部分，若无此部分则返回null对象。  此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| encodedSSP12+ | string | 否 | 否 | 获取和设置URI的编码方案特定部分。 此属性在API version 19之前为只读属性，不可写，修改此属性会报错。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### 命名规则

**命名形式：**

标准URI定义主要由以下三个部分组成：[scheme:]scheme-specific-part[#fragment]。

细化URI格式，可以将其分为：[scheme:][//authority][path][?query][#fragment]。

将URI格式进一步细化，可以分为：[scheme:][//[user-info@]host[:port]][path][?query][#fragment]。

- scheme: 协议名，与scheme-specific-part以:进行分隔，包含scheme部分的URI为绝对URI，不包含scheme部分的URI为相对URI，根据需要填写。例如http、https、ftp、datashare等。
- scheme-specific-part: URI的特定解码方案特定部分，位于[scheme:]和[#fragment]之间由[//][authority][path][?query]组成，此部分以/开头的为分层URI，不以/开头的为不透明URI，根据需要填写。

  - authority: URI的解码权限组件部分。由[userinfo@]host[:port]组成，根据需要填写。

    - userinfo: 用户信息，与host通过@进行分隔，根据需要填写。
    - host: 服务器的主机名部分，当authority存在时，此项必填。
    - port: 服务器端口，默认值为-1。根据需要填写。

  - path: 路径信息，位于host与query之间以 / 进行分割，根据需要填写。
  - query: 查询部分，位于path和fragment之间，以 ? 开头的键值对格式，以&分割键值对，以=分割键值，根据需要填写。

- fragment: 片段部分，以#与scheme-specific-part进行分隔，根据需要填写。

**URI示例：**

```ets
const uriObj1 = new uri.URI("ftp://ftp.aaa.bbb.ccc/dddd/eee.txt");
console.info(uriObj1.host); // ftp.aaa.bbb.ccc
console.info(uriObj1.fragment); // null
console.info(uriObj1.path); // /dddd/eee.txt
console.info(uriObj1.scheme); // ftp
console.info(uriObj1.userInfo); // null
console.info(uriObj1.port); // -1
console.info(uriObj1.query); // null

const uriObj2 = new uri.URI("gopher://spinaltap.micro.umn.edu/00/Weather/California/Los%20Angeles#fragment");
console.info(uriObj2.host); // spinaltap.micro.umn.edu
console.info(uriObj2.fragment); // fragment
console.info(uriObj2.path); // /00/Weather/California/Los Angeles
console.info(uriObj2.scheme); // gopher
console.info(uriObj2.userInfo); // null
console.info(uriObj2.port); //-1
console.info(uriObj2.query); // null

const uriObj3 = new uri.URI("datashare:///com.samples.datasharetest.DataShare/DB00/TBL00");
console.info(uriObj3.host); // null
console.info(uriObj3.fragment); // null
console.info(uriObj3.path); // /com.samples.datasharetest.DataShare/DB00/TBL00
console.info(uriObj3.scheme); // datashare
console.info(uriObj3.userInfo); // null
console.info(uriObj3.port); // -1
console.info(uriObj3.query); // null

const uriObj4 = new uri.URI("https://username:password@host:8080/directory/file?foo=1&bar=2#fragment");
console.info(uriObj4.host); // host
console.info(uriObj4.fragment); // fragment
console.info(uriObj4.path); // /directory/file
console.info(uriObj4.scheme); // https
console.info(uriObj4.userInfo); // username:password
console.info(uriObj4.port); // 8080
console.info(uriObj4.query); // foo=1&bar=2

const uriObj5 = new uri.URI("dataability:///com.example.DataAbility");
console.info(uriObj5.host); // null
console.info(uriObj5.fragment); // null
console.info(uriObj5.path); // /com.example.DataAbility:
console.info(uriObj5.scheme); // dataability
console.info(uriObj5.userInfo); // null
console.info(uriObj5.port); // -1
console.info(uriObj5.query); // null

const uriObj6 = new uri.URI("https://username:my+name@host:8080/directory/my+file?foo=1&bar=2#fragment");
console.info(uriObj6.encodedUserInfo); // username:my+name
console.info(uriObj6.encodedPath); // /directory/my+file
console.info(uriObj6.encodedQuery); // foo=1&bar=2
console.info(uriObj6.encodedFragment); // fragment
console.info(uriObj6.encodedAuthority); // username:my+name@host:8080
console.info(uriObj6.encodedSSP); // //username:my+name@host:8080/directory/my+file?foo=1&bar=2

let uriObj7 = new uri.URI("www.abc.com:8080/directory/file?ab=pppppp#qwer=da");
console.info(uriObj7.scheme); // www.abc.com
console.info(uriObj7.host); // null
console.info(uriObj7.port); // -1
console.info(uriObj7.path); // null
console.info(uriObj7.query); // null
console.info(uriObj7.authority); // null
console.info(uriObj7.fragment); // qwer=da
console.info(uriObj7.ssp); // 8080/directory/file?ab=pppppp
console.info("result:", uriObj7.checkIsAbsolute()); // result: true
```

#### constructor

constructor(uri: string)

构造函数用于创建URI对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 入参对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[语言基础类库错误码]([语言基础类库错误码](../../errors/语言基础类库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200002 | Invalid uri string. |

**示例：**

```ets
let mm = 'https://username:password@host:8080/directory/file?foo=1&bar=2#fragment';
new uri.URI(mm);
```

```ets
new uri.URI('https://username:password@host:8080');
```

#### toString

toString(): string

将URI转化为编码后的字符串。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回URI的字符串序列化。 |

**示例：**

```ets
const result = new uri.URI('https://username:password@host:8080/directory/file?ab=pppppp#qwer da');
let result1 = result.toString(); // https://username:password@host:8080/directory/file?ab=pppppp#qwer%20da
```

#### equalsTo9+

equalsTo(other: URI): boolean

判断此URI是否与其他URI对象相等。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | URI | 是 | 需要比较的URI对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示相等，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
const uriInstance1 = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
let result = uriInstance.equalsTo(uriInstance1); // true
```

#### checkIsAbsolute

checkIsAbsolute(): boolean

判断URI是否为绝对URI，即是否包含scheme组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是绝对URI返回true，否则返回false。 |

**示例：**

```ets
const uriInstance = new uri.URI('https://username:password@www.qwer.com:8080?query=pppppp');
console.info(`${uriInstance.checkIsAbsolute()}`); // true
const uriInstance1 = new uri.URI('xxx.com/suppliers.htm');
console.info(`${uriInstance1.checkIsAbsolute()}`); // false
```

#### normalize

normalize(): URI

规范化此URI的路径。

如果此URI是不透明的，或者其路径已经是规范形式，则返回该URI。否则将构造一个新的URI，该URI与当前URI相同，唯一的区别是其路径通过规范化当前URI的路径来计算，具体规则如下：

 1.移除所有的 .（点）段。

 2.如果 ..（双点）段前面有一个非 .. 段，则将这两个段一起移除。重复此步骤，直到不再适用为止。

如果路径规范化后以 ..（双点）段开头，这表明之前没有足够的非 .. 段可以移除，因此路径将以 .. 段开始。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| URI | 返回一个path被规范化后的URI对象。 |

**示例：**

```ets
const uriInstance = new uri.URI('https://username:password@www.qwer.com:8080/path/path1/../path2/./path3?query=pppppp');
console.info(uriInstance.path); // /path/path1/../path2/./path3
// 规范化path后，移除所有的.（点）段,如果 ..（双点）段前面有一个非 .. 段，则将这两个段一起移除。
let uriInstance1 = uriInstance.normalize();
console.info(uriInstance1.path); // /path/path2/path3
let uri1 = new uri.URI('http://www.test.com/../../patch/path1/../path2/path3/./path4/../');
console.info(uri1.path); // /../../patch/path1/../path2/path3/./path4/../
// 如果路径规范化后以 ..（双点）段开头，这表明之前没有足够的非 .. 段可以移除，因此路径将以 .. 段开始。
let uri2 = uri1.normalize();
console.info(uri2.path); // /../../patch/path2/path3
```

#### checkRelative12+

checkRelative(): boolean

判断此URI是否为相对URI，相对URI指的是不包含协议(scheme)部分的URI。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是相对URI返回true，否则返回false。 |

**示例：**

```ets
const uriInstance = new uri.URI("https://username:password@www.qwer.com:8080?query=p");
console.info(`${uriInstance.checkRelative()}`); // false
const uriInstance1 = new uri.URI("/images/pic.jpg");
console.info(`${uriInstance1.checkRelative()}`); // true
```

#### checkOpaque12+

checkOpaque(): boolean

判断此URI是否为不透明URI，方案特定部分不以“/”开头的URI为不透明的URI。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是不透明的URI返回true，否则返回false。 |

**示例：**

```ets
const uriInstance = new uri.URI("http://www.test.com/images/pic.jpg");
console.info(`${uriInstance.checkOpaque()}`); // false
const uriInstance1 = new uri.URI("mailto:user@example.com");
console.info(`${uriInstance1.checkOpaque()}`); // true
```

#### checkHierarchical12+

checkHierarchical(): boolean

判断此URI是否为分层的URI，方案特定部分以“/”开头的URI为分层的URI。相对URI也是分层的。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是分层的URI返回true，否则返回false。 |

**示例：**

```ets
const uriInstance = new uri.URI("http://www.test.com/images/pic.jpg");
console.info(`${uriInstance.checkHierarchical()}`); // true
const uriInstance1 = new uri.URI("mailto:user@example.com");
console.info(`${uriInstance1.checkHierarchical()}`); // false
```

#### getQueryValue12+

getQueryValue(key:string): string

根据给定的查询关键词，从URI查询参数部分中提取出该关键词对应的第一个值，若查询参数中存在已编码过的内容，需将对应Key进行解码后获取Value。

查询参数在问号“?”后，由键值对组成。键和值用等号“=”连接，键值对用与号“&”分隔。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 此URI查询参数的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回经解码处理后的URI查询参数的第一个值，若未找到对应值则返回null对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = new uri.URI("https://www.com?param1=value1&param2=value2");
console.info(uriInstance.getQueryValue("param1")); // value1
let uriInstance1 = new uri.URI('https://www.zyy.ss?sa%3D=po%7E');
console.info(uriInstance1.getQueryValue('sa=')) // po~
console.info(uriInstance1.getQueryValue('abc')) // null
```

#### addQueryValue12+

addQueryValue(key:string, value:string): URI

在当前URI对象上添加查询参数后返回新的URI对象，保持原有URI对象不变。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 需要添加查询参数的名称。 |
| value | string | 是 | 需要添加查询参数的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| URI | 返回添加查询部分后的URI对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = new uri.URI("https://www.test.com");
const newRoute = uriInstance.addQueryValue("param1", "hello world");
console.info(newRoute.toString()); // https://www.test.com?param1=hello%20world
```

#### addSegment12+

addSegment(pathSegment:string): URI

对指定字段进行编码，并将其追加到当前URI对象的path中，创建并返回新的URI对象，保持原有URI对象不变。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathSegment | string | 是 | 需要追加到路径部分的字段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| URI | 返回已追加字段的URI对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = new uri.URI("http://www.test.com");
const newRoute = uriInstance.addSegment("my image.jpg");
console.info(newRoute.toString()); // http://www.test.com/my%20image.jpg
```

#### addEncodedSegment12+

addEncodedSegment(pathSegment:string): URI

将已编码的字段追加到当前URI的path字段中，创建新URI对象并返回，保持原有URI对象不变。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathSegment | string | 是 | 需要追加到路径部分的编码字段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| URI | 返回已追加字段的URI对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = new uri.URI("http://www.test.com");
const newRoute = uriInstance.addEncodedSegment("my%20image.jpg");
console.info(newRoute.toString()); // http://www.test.com/my%20image.jpg
```

#### getQueryNames12+

getQueryNames(): string[]

获取URI查询部分中所有不重复的键。查询参数出现在问号“?”之后，由键值对组成，键和值用等号“=”连接，键值对间用与号“&”分隔。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回URI查询部分中所有不重复的已解码参数名集合。 |

**示例：**

```ets
const uriInstance = new uri.URI("https://www.test.com?param1=value1&param2=value2");
const paramNames = uriInstance.getQueryNames();
console.info(paramNames.toString()); // param1,param2
```

#### getQueryValues12+

getQueryValues(key:string): string[]

获取URI中查询参数指定键的所有值。如果查询参数已编码，需先解码键再获取值。

查询参数是出现在问号“?”之后的部分，由键值对组成，键和值用等号“=”连接，键值对间用与号“&”分隔。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 指定键的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回此URI中查询参数内指定键对应所有值的集合，若没有找到则返回一个空字符串数组[]。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = new uri.URI("https://www.test.com/search?query=name&query=my");
console.info(uriInstance.getQueryValues("query").toString()); // name,my
console.info(JSON.stringify(uriInstance.getQueryValues("abc"))); // []
```

#### getBooleanQueryValue12+

getBooleanQueryValue(key:string,defaultValue:boolean): boolean

根据指定键名，搜索此URI查询字符串并返回其对应的布尔类型值。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的查询参数的名称。 |
| defaultValue | boolean | 是 | 设置查询参数中未包含指定键时返回的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果指定的查询参数不存在，则返回defaultValue的值；查询参数对应第一个值为“false”或者“0”返回false，否则返回true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = new uri.URI("https://www.test.com/search?active=true");
console.info(`${uriInstance.getBooleanQueryValue("active", false)}`); // true
const uriInstance1 = new uri.URI("https://www.test.com/search");
console.info(`${uriInstance1.getBooleanQueryValue("active", false)}`); // false
const uriInstance2 = new uri.URI("https://www.test.com/search?active=aa&active=false");
console.info(`${uriInstance2.getBooleanQueryValue("active", false)}`); // true
const uriInstance3 = new uri.URI("https://www.test.com/search?active=0");
console.info(`${uriInstance3.getBooleanQueryValue("active", true)}`); // false
const uriInstance4 = new uri.URI("https://www.test.com/search");
console.info(`${uriInstance4.getBooleanQueryValue("active", true)}`); // true
```

#### clearQuery12+

clearQuery(): URI

清除URI路径查询部分，并创建一个新的URI对象返回，同时保持原有URI对象不变。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| URI | 返回一个已被清除查询部分的URI对象。 |

**示例：**

```ets
const uriInstance = new uri.URI("https://www.test.com?param1=value1");
console.info(uriInstance.clearQuery().toString()); // https://www.test.com
```

#### getLastSegment12+

getLastSegment(): string

获取此URI路径的最后一个段。每个段代表路径中的一个部分，通常通过“/”来进行分隔。对于以斜杠结尾的或者没有路径的部分不计入段。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回此URI路径中的最后一个段，如果路径为空则返回null。 |

**示例：**

```ets
const uriInstance = new uri.URI("content://com.test.provider/files/image.jpg");
console.info(uriInstance.getLastSegment()); // image.jpg
```

#### getSegment12+

getSegment(): string[]

获取此URI中已解码的所有路径段。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回此URI中已解码的所有路径段，各段前后均不含 “/”。 |

**示例：**

```ets
const uriInstance = new uri.URI("http://www.test.com/path/to/image.jpg");
console.info(uriInstance.getSegment().toString()); // path,to,image.jpg
```

#### createFromParts12+

createFromParts(scheme: string, ssp: string, fragment: string): URI

根据提供的协议、方案以及片段创建一个新的URI对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 是 | 此URI协议部分。该参数需符合URI协议标准。 |
| ssp | string | 是 | 此URI的方案特定部分，即位于协议分隔符“:”和片段分隔符“#”之间的所有内容，这部分将被编码。 |
| fragment | string | 是 | 此URI的片段部分，即“#”符号后面的内容，如果未定义则为空，这部分也将被编码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| URI | 返回由给定协议、协议特定部分和片段创建的URI对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
const uriInstance = uri.URI.createFromParts("mailto", "no body", "top");
console.info(uriInstance.toString()); // mailto:no%20body#top
```

#### equals(deprecated)

equals(other: URI): boolean

判断此URI是否与其他URI对象相等。


从API version 8开始支持，从API version 9开始废弃，建议使用[equalsTo9+](#ZH-CN_TOPIC_0000002522080702__equalsto9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | URI | 是 | 需要比较的URI对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示相等，否则返回false。 |

**示例：**

```ets
const uriInstance = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
const uriInstance1 = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
uriInstance.equals(uriInstance1); // true
```