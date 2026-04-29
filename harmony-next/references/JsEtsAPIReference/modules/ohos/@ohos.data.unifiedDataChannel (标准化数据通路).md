# @ohos.data.unifiedDataChannel (标准化数据通路)

本模块为统一数据管理框架（Unified Data Management Framework，UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景提供了标准化的数据通路，提供了标准化的数据接入与读取接口。同时对文本、图片等数据类型提供了标准化定义，方便不同应用间进行数据交互，减少数据类型适配的工作量。UDMF处理数据时，不会解析用户数据的内容，存储路径安全性较低，不建议传输个人敏感数据和隐私数据。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { unifiedDataChannel } from '@kit.ArkData';
```

#### ShareOptions12+

UDMF支持的设备内使用范围类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IN_APP | 0 | 表示允许在本设备同应用内使用。 |
| CROSS_APP | 1 | 表示允许在本设备内跨应用使用。 |

#### GetDelayData12+

type GetDelayData = (type: string) => UnifiedData

对UnifiedData的延迟封装，支持延迟获取数据。当前只支持同设备剪贴板场景，后续场景待开发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 作为延迟数据类型的标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UnifiedData | 当延迟回调触发时，返回一个UnifiedData对象。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let getDelayData: unifiedDataChannel.GetDelayData = ((type: string) => {
  if (type == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
    let plainTextDetails : Record<string, string> = {
      'attr1': 'value1',
      'attr2': 'value2'
    }
    let plainText : uniformDataStruct.PlainText = {
      uniformDataType: 'general.plain-text',
      textContent : 'This is a plain text example',
      abstract : 'This is abstract',
      details : plainTextDetails
    }
    let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
    let textData = new unifiedDataChannel.UnifiedData(text);
    return textData;
  }
  return new unifiedDataChannel.UnifiedData();
});
```

#### ValueType12+

type ValueType = number | string | boolean | image.PixelMap | Want | ArrayBuffer | object | null | undefined

用于表示统一数据记录允许的数据字段类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示number的类型。 |
| string | 表示string的类型。 |
| boolean | 表示boolean的类型。 |
| image.PixelMap | 表示image.PixelMap的类型。 |
| Want | 表示Want的类型。 |
| ArrayBuffer | 表示ArrayBuffer的类型。 |
| object | 表示object的类型。 |
| null | 表示null。 |
| undefined | 表示undefined。 |

#### UnifiedDataProperties12+

定义统一数据对象中所有数据记录的属性，包含时间戳、标签、粘贴范围以及一些附加数据等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| extras | Record<string, object> | 否 | 是 | 是一个字典类型对象，用于设置其他附加属性数据。非必填字段，默认值为空字典对象。 |
| tag | string | 否 | 是 | 用户自定义标签。非必填字段，默认值为空字符串。 |
| timestamp | Date | 是 | 是 | UnifiedData的生成时间戳。默认值为1970年1月1日（UTC）。 |
| shareOptions | ShareOptions | 否 | 是 | 指示UnifiedData支持的设备内使用范围，非必填字段，默认值为CROSS_APP。 |
| getDelayData | GetDelayData | 否 | 是 | 延迟获取数据回调。当前只支持同设备剪贴板场景，后续场景待开发。非必填字段，默认值为undefined。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let properties = new unifiedDataChannel.UnifiedDataProperties();
properties.extras = {
  key: {
    title: 'MyTitle',
    content: 'MyContent'
  }
};
properties.tag = "This is a tag of properties";
properties.shareOptions = unifiedDataChannel.ShareOptions.CROSS_APP;
properties.getDelayData = ((type: string) => {
  if (type == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
    let plainTextDetails : Record<string, string> = {
      'attr1': 'value1',
      'attr2': 'value2'
    }
    let plainText : uniformDataStruct.PlainText = {
      uniformDataType: 'general.plain-text',
      textContent : 'This is a plain text example',
      abstract : 'This is abstract',
      details : plainTextDetails
    }
    let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
    let textData = new unifiedDataChannel.UnifiedData(text);
    return textData;
  }
  return new unifiedDataChannel.UnifiedData();
});
```

#### UnifiedData

表示UDMF统一数据对象，提供封装一组数据记录的方法。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties12+ | UnifiedDataProperties | 否 | 否 | 当前统一数据对象中所有数据记录的属性，包含时间戳、标签、粘贴范围以及一些附加数据等。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### constructor12+

constructor()

用于创建统一数据对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**示例：**

```ets
let unifiedData = new unifiedDataChannel.UnifiedData();
```

#### constructor

constructor(record: UnifiedRecord)

用于创建带有一条数据记录的统一数据对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| record | UnifiedRecord | 是 | 要添加到统一数据对象中的数据记录，该记录为UnifiedRecord或其子类对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);
```

#### addRecord

addRecord(record: UnifiedRecord): void

在当前统一数据对象中添加一条数据记录。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| record | UnifiedRecord | 是 | 要添加到统一数据对象中的数据记录，该记录为UnifiedRecord子类对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of the hyperlink'
}
let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
unifiedData.addRecord(link);
```

#### getRecords

getRecords(): Array<UnifiedRecord>

将当前统一数据对象中的所有数据记录取出。通过本接口取出的数据为UnifiedRecord类型，需通过[getType](#ZH-CN_TOPIC_0000002522080636__gettype)获取数据类型后转为子类再使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<UnifiedRecord> | 当前统一数据对象内所添加的记录。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of the hyperlink'
}
let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
unifiedData.addRecord(link);

let records = unifiedData.getRecords();
for (let i = 0; i < records.length; i++) {
  let record = records[i];
  let types = record.getTypes();
  if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
    let plainText = record.getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as unifiedDataChannel.PlainText;
    console.info(`textContent: ${plainText.textContent}`);
  } else if (types.includes(uniformTypeDescriptor.UniformDataType.HYPERLINK)) {
    let hyperlink = record.getEntry(uniformTypeDescriptor.UniformDataType.HYPERLINK) as unifiedDataChannel.Hyperlink;
    console.info(`linkUrl: ${hyperlink.url}`);
  }
```

#### hasType12+

hasType(type: string): boolean

检查当前统一数据对象中是否有指定的数据类型，检查范围包括使用[addEntry](#ZH-CN_TOPIC_0000002522080636__addentry15)函数添加的数据类型。

针对文件类型，若UnifiedData的类型集合中包含"general.jpeg"，在调用hasType接口判断是否包括"general.image"类型时，结果返回true（类型"general.jpeg"归属于类型"general.image"）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要查询的数据类型，见UniformDataType。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of the hyperlink'
}
let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
unifiedData.addRecord(link);

let hasPlainText = unifiedData.hasType(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT);
let hasLink = unifiedData.hasType(uniformTypeDescriptor.UniformDataType.HYPERLINK);
```

#### getTypes12+

getTypes(): Array<string>

获取当前统一数据对象所有数据记录的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | UniformDataType类型的数组，表示当前统一数据对象所有数据记录对应的数据类型。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of the hyperlink'
}
let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
unifiedData.addRecord(link);

let types = unifiedData.getTypes();
```

#### Summary

描述统一数据对象的数据摘要，包括数据类型和大小。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| summary | Record<string, number> | 否 | 否 | 是一个字典类型对象，key表示数据类型（见UniformDataType），value为统一数据对象中该类型记录大小总和（单位：Byte）。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| totalSize | number | 否 | 否 | 统一数据对象内记录总大小（单位：Byte）。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| overview22+ | Record<string, number> | 是 | 否 | 统一数据对象中所有类型与该类型数据记录大小的映射关系，其中数据大小单位为Byte。当获取到的统一数据对象为空时，此overview属性值为空。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

**示例：**

```ets
function parseSummary(summary : unifiedDataChannel.Summary) {
  let summaryRecord = summary.summary as Record<string, number>;
  if (summaryRecord) {
    for (let item of Object.entries(summaryRecord)) {
      if (item && item.length <= 1) {
        continue;
      }
      let summaryStr : string = String(item[1]);
      let info : string[] = summaryStr.split(",");
      if (info.length <= 1) {
        continue;
      }
      let key : string = info[0];
      let value : string = info[1];
    }
  let overviewRecord = summary.overview as Record<string, number>;
  let totalSize = summary.totalSize;
}
```

#### UnifiedRecord

对UDMF支持的数据内容的抽象定义，称为数据记录。一个统一数据对象内包含一条或多条数据记录，例如一条文本记录、一条图片记录、一条HTML记录等。从API version 15开始，支持往数据记录中增加同一内容的不同表现样式，数据使用方根据业务需要获取对应的样式。

#### constructor12+

constructor()

用于创建数据记录。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**示例：**

```ets
let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
```

#### constructor12+

constructor(type: string, value: ValueType)

用于创建指定类型和值的数据记录。

当参数value为[image.PixelMap](Interface (PixelMap).md)类型时，参数type必须对应为[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002522240636__uniformdatatype)中OPENHARMONY_PIXEL_MAP的值；

当参数value为[Want](@ohos.app.ability.Want (Want).md)类型时，参数type必须对应为[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002522240636__uniformdatatype)中OPENHARMONY_WANT的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要创建的数据记录的类型。 |
| value | ValueType | 是 | 要创建的数据记录的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of the hyperlink'
}
let hyperlinkRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);

let arrayBuffer = new ArrayBuffer(4 * 200 * 200);
let opt : image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 }, alphaType: 3 };
let pixelMap : uniformDataStruct.PixelMap = {
  uniformDataType : 'openharmony.pixel-map',
  pixelMap : image.createPixelMapSync(arrayBuffer, opt)
}
let pixelMapRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
```

#### getType

getType(): string

获取当前数据记录的类型。由于从统一数据对象中调用[getRecords](#ZH-CN_TOPIC_0000002522080636__getrecords)所取出的数据是UnifiedRecord对象，因此需要通过本接口查询此记录的具体类型，再将该UnifiedRecord对象转换为其子类，调用子类接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前数据记录对应的具体数据类型，见UniformDataType。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let records = unifiedData.getRecords();
if (records[0].getType() == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
  let plainText = records[0] as unifiedDataChannel.PlainText;
  console.info(`textContent: ${plainText.textContent}`);
}
```

#### getValue12+

getValue(): ValueType

获取当前数据记录的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ValueType | 当前数据记录对应的值。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, 'this is value of text');
let value = text.getValue();

let hyperlinkDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of the hyperlink',
  details : hyperlinkDetails
}
let hyperlinkRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
let hyperlinkValue = hyperlinkRecord.getValue();
```

#### addEntry15+

addEntry(type: string, value: ValueType): void

在当前数据记录中添加一条指定数据类型和内容的数据，通过该方法增加的数据类型和内容为同一内容的不同表现样式.

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要创建的数据类型，见UniformDataType。 |
| value | ValueType | 是 | 要创建的数据的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let fileUri : uniformDataStruct.FileUri = {
  uniformDataType : 'general.file-uri',
  oriUri : 'file://data/image/1.png',
  fileType : 'general.image',
  details : fileUriDetails
}
let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'file://data/image/1.png',
  description : 'This is the description of the hyperlink'
}

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);
```

#### getEntry15+

getEntry(type: string): ValueType

通过数据类型获取数据记录中的数据内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要获取数据的类型，见UniformDataType。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ValueType | 当前数据记录对应的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let fileUri : uniformDataStruct.FileUri = {
  uniformDataType : 'general.file-uri',
  oriUri : 'file://data/image/1.png',
  fileType : 'general.image',
  details : fileUriDetails
}
let formDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let form : uniformDataStruct.Form = {
  uniformDataType : 'openharmony.form',
  formId : 1,
  formName : 'form',
  bundleName : 'com.xx.app',
  abilityName : 'ability',
  module : 'module',
  details : formDetails
}

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);

let records = unifiedData.getRecords();
for (let i = 0; i < records.length; i++) {
  let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
  let fileUriRead : uniformDataStruct.FileUri = unifiedDataRecord.getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
  if (fileUriRead != undefined) {
    console.info(`oriUri: ${fileUriRead.oriUri}`);
  }
  let formRead = unifiedDataRecord.getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM) as uniformDataStruct.Form;
  if (formRead != undefined) {
    console.info(`formName: ${formRead.formName}`);
  }
```

#### getEntries15+

getEntries(): Record<string, ValueType>

获取当前数据记录中所有数据的类型和内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, ValueType> | 当前数据记录对应的类型和内容。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let fileUri : uniformDataStruct.FileUri = {
  uniformDataType : 'general.file-uri',
  oriUri : 'file://data/image/1.png',
  fileType : 'general.image',
  details : fileUriDetails
}
let formDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let form : uniformDataStruct.Form = {
  uniformDataType : 'openharmony.form',
  formId : 1,
  formName : 'form',
  bundleName : 'com.xx.app',
  abilityName : 'ability',
  module : 'module',
  details : formDetails
}

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);

let records = unifiedData.getRecords();
for (let i = 0; i < records.length; i++) {
  let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
  let entries : Record<string, unifiedDataChannel.ValueType> = unifiedDataRecord.getEntries();
  let formRead : uniformDataStruct.Form = entries[uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM] as uniformDataStruct.Form;
  if (formRead != undefined) {
    console.info(`formName: ${formRead.formName}`);
  }
  let fileUriRead : uniformDataStruct.FileUri = entries[uniformTypeDescriptor.UniformDataType.FILE_URI] as uniformDataStruct.FileUri;
  if (fileUriRead != undefined) {
    console.info(`oriUri: ${fileUriRead.oriUri}`);
  }
```

#### getTypes15+

getTypes(): Array<string>

获取数据记录中数据的所有类型集合。可通过UnifiedRecord数据记录对象调用本接口，查询出此记录中数据的所有类型集合，包括使用[addEntry](#ZH-CN_TOPIC_0000002522080636__addentry15)函数添加的数据类型。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | UniformDataType类型的数组，表示当前记录的数据类型集合。 |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let fileUri : uniformDataStruct.FileUri = {
  uniformDataType : 'general.file-uri',
  oriUri : 'file://data/image/1.png',
  fileType : 'general.image',
  details : fileUriDetails
}
let formDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let form : uniformDataStruct.Form = {
  uniformDataType : 'openharmony.form',
  formId : 1,
  formName : 'form',
  bundleName : 'com.xx.app',
  abilityName : 'ability',
  module : 'module',
  details : formDetails
}

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);

let records = unifiedData.getRecords();
for (let i = 0; i < records.length; i++) {
  let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
  let types : Array<string> = unifiedDataRecord.getTypes();
  if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM)) {
    console.info(`Types include: ${uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM}`);
  }
```

#### Text

文本类型数据，是[UnifiedRecord](#ZH-CN_TOPIC_0000002522080636__unifiedrecord)的子类，也是文本类型数据的基类，用于描述文本类数据，推荐开发者优先使用Text的子类描述数据，如[PlainText](#ZH-CN_TOPIC_0000002522080636__plaintext)、[Hyperlink](#ZH-CN_TOPIC_0000002522080636__hyperlink)、[HTML](#ZH-CN_TOPIC_0000002522080636__html)等具体子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| details | Record<string, string> | 否 | 是 | 是一个字典类型对象，key和value都是string类型，用于描述文本内容。例如，可生成一个details内容为 { "title":"标题", "content":"内容" } 的数据对象，用于描述一篇文章。非必填字段，默认值为空字典对象。 |

**示例：**

```ets
let text = new unifiedDataChannel.Text();
text.details = {
  title: 'MyTitle',
  content: 'This is content'
};
let unifiedData = new unifiedDataChannel.UnifiedData(text);
```

#### PlainText

[Text](#ZH-CN_TOPIC_0000002522080636__text)的子类，用于描述纯文本类数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textContent | string | 否 | 否 | 纯文本内容。 |
| abstract | string | 否 | 是 | 纯文本摘要，非必填字段，默认值为空字符串。 |

**示例：**

```ets
let text = new unifiedDataChannel.PlainText();
text.textContent = 'this is textContent';
text.abstract = 'This is abstract';
```

#### Hyperlink

[Text](#ZH-CN_TOPIC_0000002522080636__text)的子类，用于描述超链接类型数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 链接url。 |
| description | string | 否 | 是 | 链接内容描述，非必填字段，默认值为空字符串。 |

**示例：**

```ets
let link = new unifiedDataChannel.Hyperlink();
link.url = 'www.XXX.com';
link.description = 'This is description';
```

#### HTML

HTML类型数据，是[Text](#ZH-CN_TOPIC_0000002522080636__text)的子类，用于描述超文本标记语言数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| htmlContent | string | 否 | 否 | html格式内容。 |
| plainContent | string | 否 | 是 | 去除html标签后的纯文本内容，非必填字段，默认值为空字符串。 |

**示例：**

```ets
let html = new unifiedDataChannel.HTML();
html.htmlContent = '<div><p>标题</p></div>';
html.plainContent = 'This is plainContent';
```

#### File

File类型数据，是[UnifiedRecord](#ZH-CN_TOPIC_0000002522080636__unifiedrecord)的子类，也是文件类型数据的基类，用于描述文件类型数据，推荐开发者优先使用File的子类描述数据，如[Image](#ZH-CN_TOPIC_0000002522080636__image)、[Video](#ZH-CN_TOPIC_0000002522080636__video)、[Folder](#ZH-CN_TOPIC_0000002522080636__folder)等具体子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| details | Record<string, string> | 否 | 是 | 是一个字典类型对象，key和value都是string类型，用于描述文件相关信息。例如，可生成一个details内容为 { "name":"文件名", "type":"文件类型" } 的数据对象，用于描述一个文件。非必填字段，默认值为空字典对象。 |
| uri | string | 否 | 否 | 本地文件数据uri或网络文件uri，本地文件数据uri可通过getUriFromPath函数获取。 |

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';
import { fileUri } from '@kit.CoreFileKit'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
    let file = new unifiedDataChannel.File();
    file.details = {
        name: 'test',
        type: 'txt'
    };
    let filePath = pathDir + '/test.txt';
    file.uri = fileUri.getUriFromPath(filePath);
  }
```

#### Image

图片类型数据，是[File](#ZH-CN_TOPIC_0000002522080636__file)的子类，用于描述图片文件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageUri | string | 否 | 否 | 本地图片数据uri或网络图片uri，本地图片数据uri可通过getUriFromPath函数获取。 |

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';
import { fileUri } from '@kit.CoreFileKit'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
    let image = new unifiedDataChannel.Image();
    let filePath = pathDir + '/test.jpg';
    image.imageUri = fileUri.getUriFromPath(filePath);
  }
```

#### Video

视频类型数据，是[File](#ZH-CN_TOPIC_0000002522080636__file)的子类，用于描述视频文件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| videoUri | string | 否 | 否 | 本地视频数据uri或网络视频uri，本地视频数据uri可通过getUriFromPath函数获取。 |

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';
import { fileUri } from '@kit.CoreFileKit'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
    let video = new unifiedDataChannel.Video();
    let filePath = pathDir + '/test.mp4';
    video.videoUri =fileUri.getUriFromPath(filePath);
  }
```

#### Audio

音频类型数据，是[File](#ZH-CN_TOPIC_0000002522080636__file)的子类，用于描述音频文件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioUri | string | 否 | 否 | 本地音频数据uri或网络音频uri，本地音频数据uri可通过getUriFromPath函数获取。 |

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';
import { fileUri } from '@kit.CoreFileKit'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
    let audio = new unifiedDataChannel.Audio();
    let filePath = pathDir + '/test.mp3';
    audio.audioUri = fileUri.getUriFromPath(filePath);
  }
```

#### Folder

文件夹类型数据，是[File](#ZH-CN_TOPIC_0000002522080636__file)的子类，用于描述文件夹。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| folderUri | string | 否 | 否 | 本地文件夹数据uri或网络文件夹uri，本地文件夹数据uri可通过getUriFromPath函数获取。 |

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';
import { fileUri } from '@kit.CoreFileKit'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
    let folder = new unifiedDataChannel.Folder();
    let filePath = pathDir + '/folder';
    folder.folderUri = fileUri.getUriFromPath(filePath);
  }
```

#### SystemDefinedRecord

SystemDefinedRecord是[UnifiedRecord](#ZH-CN_TOPIC_0000002522080636__unifiedrecord)的子类，也是HarmonyOS系统特有数据类型的基类，用于描述仅在HarmonyOS系统范围内流通的特有数据类型，推荐开发者优先使用SystemDefinedRecord的子类描述数据，如[SystemDefinedForm](#ZH-CN_TOPIC_0000002522080636__systemdefinedform)、[SystemDefinedAppItem](#ZH-CN_TOPIC_0000002522080636__systemdefinedappitem)、[SystemDefinedPixelMap](#ZH-CN_TOPIC_0000002522080636__systemdefinedpixelmap)等具体子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```ets
let sdr = new unifiedDataChannel.SystemDefinedRecord();
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
sdr.details = {
    title: 'recordTitle',
    version: 1,
    content: u8Array
};
let unifiedData = new unifiedDataChannel.UnifiedData(sdr);
```

#### SystemDefinedForm

系统定义的桌面卡片类型数据，是[SystemDefinedRecord](#ZH-CN_TOPIC_0000002522080636__systemdefinedrecord)的子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | number | 否 | 否 | 卡片id。 |
| formName | string | 否 | 否 | 卡片名称。 |
| bundleName | string | 否 | 否 | 卡片所属的bundle名。 |
| abilityName | string | 否 | 否 | 卡片对应的ability名。 |
| module | string | 否 | 否 | 卡片所属的module名。 |

**示例：**

```ets
let form = new unifiedDataChannel.SystemDefinedForm();
form.formId = 123456;
form.formName = 'MyFormName';
form.bundleName = 'MyBundleName';
form.abilityName = 'MyAbilityName';
form.module = 'MyModule';
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
form.details = {
  formKey1: 123,
  formKey2: 'formValue',
  formKey3: u8Array
};
let unifiedData = new unifiedDataChannel.UnifiedData(form);
```

#### SystemDefinedAppItem

系统定义的桌面图标类型数据，是[SystemDefinedRecord](#ZH-CN_TOPIC_0000002522080636__systemdefinedrecord)的子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appId | string | 否 | 否 | 图标对应的应用id。 |
| appName | string | 否 | 否 | 图标对应的应用名。 |
| appIconId | string | 否 | 否 | 图标的图片id。 模型约束： 此接口仅可在Stage模型下使用。 |
| appLabelId | string | 否 | 否 | 图标名称对应的标签id。 模型约束： 此接口仅可在Stage模型下使用。 |
| bundleName | string | 否 | 否 | 图标对应的应用bundle名。 |
| abilityName | string | 否 | 否 | 图标对应的应用ability名。 |

**示例：**

```ets
let appItem = new unifiedDataChannel.SystemDefinedAppItem();
appItem.appId = 'MyAppId';
appItem.appName = 'MyAppName';
appItem.appIconId = 'MyAppIconId';
appItem.appLabelId = 'MyAppLabelId';
appItem.bundleName = 'MyBundleName';
appItem.abilityName = 'MyAbilityName';
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
appItem.details = {
    appItemKey1: 123,
    appItemKey2: 'appItemValue',
    appItemKey3: u8Array
};
let unifiedData = new unifiedDataChannel.UnifiedData(appItem);
```

#### SystemDefinedPixelMap

与系统侧定义的[PixelMap](Interface (PixelMap).md)数据类型对应的图片数据类型，是[SystemDefinedRecord](#ZH-CN_TOPIC_0000002522080636__systemdefinedrecord)的子类，仅保存PixelMap的二进制数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rawData | Uint8Array | 否 | 否 | PixelMap对象的二进制数据。 |

**示例：**

```ets
import { image } from '@kit.ImageKit'; // PixelMap类定义所在模块
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

const color = new ArrayBuffer(96); // 创建pixelMap对象
let opts: image.InitializationOptions = {
  editable: true, pixelFormat: 3, size: {
    height: 4, width: 6
}
image.createPixelMap(color, opts, (error, pixelMap) => {
  if (error) {
    console.error('Failed to create pixelMap.');
  } else {
    console.info('Succeeded in creating pixelMap.');
    let arrayBuf = new ArrayBuffer(pixelMap.getPixelBytesNumber());
    pixelMap.readPixelsToBuffer(arrayBuf);
    let u8Array = new Uint8Array(arrayBuf);
    let sdPixel = new unifiedDataChannel.SystemDefinedPixelMap();
    sdPixel.rawData = u8Array;
    let unifiedData = new unifiedDataChannel.UnifiedData(sdPixel);

    // 从unifiedData中读取pixelMap类型的record
    let records = unifiedData.getRecords();
    for (let i = 0; i < records.length; i++) {
      if (records[i].getType() === uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) {
        let pixelMapRecord = records[i] as unifiedDataChannel.SystemDefinedPixelMap;
        let newArrayBuf = pixelMapRecord.rawData.buffer;
        pixelMap.writeBufferToPixels(newArrayBuf).then(() => {
          console.info('Succeeded in writing data from buffer to a pixelMap');
        }).catch((error: BusinessError) => {
          console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
        })
      }
})
```

#### ApplicationDefinedRecord

ApplicationDefinedRecord是[UnifiedRecord](#ZH-CN_TOPIC_0000002522080636__unifiedrecord)的子类，也是应用自定义数据类型的基类，用于描述仅在应用生态内部流通的自定义数据类型，应用可基于此类进行自定义数据类型的扩展。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| applicationDefinedType | string | 否 | 否 | 应用自定义类型标识符，必须以'ApplicationDefined'开头。 |
| rawData | Uint8Array | 否 | 否 | 应用自定义数据类型的二进制数据。 |

**示例：**

```ets
let record = new unifiedDataChannel.ApplicationDefinedRecord();
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
record.applicationDefinedType = 'ApplicationDefinedType';
record.rawData = u8Array;
let unifiedData = new unifiedDataChannel.UnifiedData(record);
```

#### Intention

UDMF已经支持的数据通路枚举类型。其主要用途是标识各种UDMF数据通路所面向的不同业务场景。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA_HUB | 'DataHub' | 公共数据通路。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| DRAG14+ | 'Drag' | 拖拽类型数据通道。 模型约束： 此接口仅可在Stage模型下使用。 适用场景： 适用于在拖拽场景下使用UDMF来跨应用数据共享。 |
| SYSTEM_SHARE20+ | 'SystemShare' | 系统分享类型数据通道。 模型约束： 此接口仅可在Stage模型下使用。 适用场景： 适用于在系统分享场景下使用UDMF来跨应用数据共享。 |
| PICKER20+ | 'Picker' | Picker类型数据通道。 模型约束： 此接口仅可在Stage模型下使用。 适用场景： 适用于在Picker选择器场景下使用UDMF来跨应用数据共享。 |
| MENU20+ | 'Menu' | 菜单类型数据通道。 模型约束： 此接口仅可在Stage模型下使用。 适用场景： 适用于在右键菜单场景下使用UDMF来跨应用数据共享。 |

#### Visibility20+

表示数据的可见性等级枚举。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 可见性等级，所有应用可见。 模型约束： 此接口仅可在Stage模型下使用。 |
| OWN_PROCESS | 1 | 可见性等级，仅数据提供者可见。 模型约束： 此接口仅可在Stage模型下使用。 |

#### Options

UDMF提供的数据操作接口包含三个可选参数：intention、key和visibility。如果接口不需要这些参数，可以不填，具体要求请参阅该接口的参数说明。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intention | Intention | 否 | 是 | 表示数据操作相关的数据通路类型。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| key | string | 否 | 是 | UDMF中数据对象的唯一标识符，可通过insertData接口的返回值获取。 由udmf:/、intention、bundleName和groupId四部分组成，以'/'连接，比如：udmf://DataHub/com.ohos.test/0123456789。 其中udmf:/固定，DataHub为对应枚举的取值，com.ohos.test为包名，0123456789为随机生成的groupId。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| visibility20+ | Visibility | 否 | 是 | 表示数据的可见性等级。只在写入数据的时候填写才生效，若不填写默认是Visibility.ALL。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### FileConflictOptions15+

表示文件拷贝冲突时的可选策略的枚举。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERWRITE | 0 | 目标路径存在同文件名时覆盖。 |
| SKIP | 1 | 目标路径存在同文件名时跳过。 |

#### ProgressIndicator15+

表示进度条指示选项的枚举，可选择是否采用系统默认进度显示。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不采用系统默认进度显示。 |
| DEFAULT | 1 | 采用系统默认进度显示，500ms内获取数据完成将不会拉起默认进度条。 |

#### ListenerStatus15+

表示从UDMF获取数据时的状态码的枚举。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FINISHED | 0 | 表示已完成。 |
| PROCESSING | 1 | 表示正在处理中。 |
| CANCELED | 2 | 表明本次处理已被取消。 |
| INNER_ERROR | 200 | 表明发生了内部错误。 |
| INVALID_PARAMETERS | 201 | 表示 GetDataParams 包含无效参数。 |
| DATA_NOT_FOUND | 202 | 表示没有获取到数据。 |
| SYNC_FAILED | 203 | 表示同步过程中出现错误。 |
| COPY_FILE_FAILED | 204 | 表示文件拷贝过程中出现错误。 |

#### ProgressInfo15+

定义进度上报的数据。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 否 | 系统上报拖拽任务进度百分比。取值范围为[-1-100]的整数，其中-1时代表本次获取数据失败，100时表示本次获取数据完成。 |
| status | ListenerStatus | 否 | 否 | 系统上报拖拽任务的状态码。 |

#### DataProgressListener15+

type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void

定义获取进度信息和数据的监听回调函数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progressInfo | ProgressInfo | 是 | 定义进度上报的进度信息。 |
| data | UnifiedData | null | 是 | 进度达到100时获取的数据，进度未到100时返回null。 |

#### GetDataParams15+

表示从UDMF获取数据时的参数，包含目标路径、文件冲突选项、进度条类型等。

具体使用示例可见[拖拽异步获取数据](拖拽事件.md#ZH-CN_TOPIC_0000002553200729__示例3[拖拽异步获取数据](../../topics/components/拖拽事件.md#ZH-CN_TOPIC_0000002529444781__示例3拖拽异步获取数据))。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progressIndicator | ProgressIndicator | 否 | 否 | 定义进度条指示选项，可选择是否采用系统默认进度显示。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| dataProgressListener | DataProgressListener | 否 | 否 | 表示获取统一数据时的进度和数据监听器。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| destUri | string | 否 | 是 | 拷贝文件的目标路径。若不支持文件处理，则不需要设置此参数，默认为空；若支持文件处理，须设置一个已经存在的目录。若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。不填写时获取到的uri为源端路径URI，填写后获取到的uri为目标路径uri。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| fileConflictOptions | FileConflictOptions | 否 | 是 | 定义文件拷贝冲突时的选项，默认为OVERWRITE。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| acceptableInfo20+ | DataLoadInfo | 否 | 是 | 定义接收方对数据类型和数据记录数量的接收能力。延迟加载场景下，发送方可根据此信息生成并返回更合适的数据内容。默认为空，不提供接收方数据接收能力。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### DataLoadInfo20+

用于描述被加载数据的类型与数量。

- 在**数据发送方**中使用，表示实际可提供的数据范围，必须设置该字段。

- 在**数据接收方**中使用，表示期望加载的数据类型与数量，可根据需要设置该字段。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| types | Set<string> | 否 | 是 | 表示数据类型集合，默认为空集合。 |
| recordCount | number | 否 | 是 | 表示期望或可提供的最大数据记录数，默认值为0，取值范围为[0, 232-1]。超过取值范围时会按默认值处理。设置为浮点数时，仅使用整数部分。当用于拖拽时，会作为角标数量显示，最大支持231-1，超过此数值时不显示角标。作为角标数量时，优先级低于[DragPreviewOptions](../../topics/components/拖拽控制.md#ZH-CN_TOPIC_0000002497604842__dragpreviewoptions11)中的numberBadge方法。 |

#### DataLoadHandler20+

type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null

用于延迟加载数据的处理函数。支持数据发送方根据接收方传入的信息，动态生成数据，实现更灵活、精准的数据交互策略。

该处理函数为同步函数，适用于处理简单业务逻辑，若函数业务逻辑较复杂、执行时间较长（3s以上），推荐使用异步处理函数[DelayedDataLoadHandler](#ZH-CN_TOPIC_0000002522080636__delayeddataloadhandler22)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| acceptableInfo | DataLoadInfo | 否 | 表示数据接收方可以接收的数据类型和数量，默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UnifiedData | null | 当延迟处理函数触发时，返回UnifiedData或null。 |

#### DelayedDataLoadHandler22+

type DelayedDataLoadHandler = (acceptableInfo?: DataLoadInfo) => Promise<UnifiedData | null>

用于延迟加载数据的处理函数。支持数据发送方根据接收方传入的信息，动态生成数据，实现更灵活、精准的数据交互策略。

该处理函数为异步函数，返回Promise对象，不阻塞主线程，可处理复杂业务逻辑、执行长耗时任务。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| acceptableInfo | DataLoadInfo | 否 | 表示数据接收方可以接收的数据类型和数量，默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<UnifiedData | null> | 当延迟处理函数触发时，返回Promise对象。 |

#### DataLoadParams20+

用于在延迟加载场景下描述发送方的数据加载策略。

当同时传入loadHandler和delayedDataLoadHandler时，优先使用delayedDataLoadHandler，loadHandler不生效。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| loadHandler | DataLoadHandler | 否 | 否 | 表示用于延迟加载数据的处理函数。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| delayedDataLoadHandler22+ | DelayedDataLoadHandler | 否 | 是 | 表示用于延迟加载数据的异步处理函数。 元服务API： 从API version 22开始，该接口支持在元服务中使用. 模型约束： 此接口仅可在Stage模型下使用。 |
| dataLoadInfo | DataLoadInfo | 否 | 否 | 用于描述当前发送方可生成的数据类型及数量信息。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### unifiedDataChannel.insertData

insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void

将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，参数中intention字段必填，且不支持DRAG，不填时会返回401错误码；其他字段是否填写均不影响接口的使用。 |
| data | UnifiedData | 是 | 目标数据。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回写入UDMF的数据的唯一标识符key的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
}
try {
  unifiedDataChannel.insertData(options, unifiedData, (err, key) => {
    if (err === undefined) {
      console.info(`Succeeded in inserting data. key = ${key}`);
    } else {
      console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
    }
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.insertData

insertData(options: Options, data: UnifiedData): Promise<string>

将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，参数中intention字段必填，且不支持DRAG，不填时会返回401错误码；其他字段是否填写均不影响接口的使用。 |
| data | UnifiedData | 是 | 目标数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回写入UDMF的数据的唯一标识符key的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
}
try {
  unifiedDataChannel.insertData(options, unifiedData).then((key) => {
    console.info(`Succeeded in inserting data. key = ${key}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.updateData

updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void

更新已写入UDMF的公共数据通路的数据，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，参数中key字段必填，不填时会返回401错误码；intention参数仅支持DATA_HUB；其他字段是否填写均不影响接口的使用。 |
| data | UnifiedData | 是 | 目标数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);
let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
}
try {
  unifiedDataChannel.insertData(options, unifiedData).then((key) => {
    console.info(`Succeeded in inserting data. key = ${key}`);
    let updateOptions: unifiedDataChannel.Options = {
      intention: unifiedDataChannel.Intention.DATA_HUB,
      key: key
    }
    let plainTextUpdate : uniformDataStruct.PlainText = {
      uniformDataType: 'general.plain-text',
      textContent : 'This is plainText textContent for update',
      abstract : 'This is abstract for update'
    }
    let textUpdate = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextUpdate);
    let unifiedDataUpdate = new unifiedDataChannel.UnifiedData(textUpdate);
    try {
      unifiedDataChannel.updateData(updateOptions, unifiedDataUpdate, (err) => {
        if (err === undefined) {
          console.info('Succeeded in updating data.');
        } else {
          console.error(`Failed to update data. code is ${err.code}, message is ${err.message} `);
        }
      });
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      console.error(`Update data throws an exception. code is ${error.code}, message is ${error.message} `);
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.updateData

updateData(options: Options, data: UnifiedData): Promise<void>

更新已写入UDMF的公共数据通路的数据，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，参数中key字段必填，不填时会返回401错误码；intention参数仅支持DATA_HUB；其他字段是否填写均不影响接口的使用。 |
| data | UnifiedData | 是 | 目标数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is a plain text example',
  abstract : 'This is abstract'
}
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);
let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
}
try {
  unifiedDataChannel.insertData(options, unifiedData).then((key) => {
    console.info(`Succeeded in inserting data. key = ${key}`);
    let updateOptions: unifiedDataChannel.Options = {
      intention: unifiedDataChannel.Intention.DATA_HUB,
      key: key
    }
    let plainTextUpdate : uniformDataStruct.PlainText = {
      uniformDataType: 'general.plain-text',
      textContent : 'This is plainText textContent for update',
      abstract : 'This is abstract for update'
    }
    let textUpdate = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextUpdate);
    let unifiedDataUpdate = new unifiedDataChannel.UnifiedData(textUpdate);
    try {
      unifiedDataChannel.updateData(updateOptions, unifiedDataUpdate).then(() => {
        console.info('Succeeded in updating data.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to update data. code is ${err.code}, message is ${err.message} `);
      });
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      console.error(`Update data throws an exception. code is ${error.code}, message is ${error.message} `);
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.queryData

queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void

查询UDMF公共数据通路的数据，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，key和intention均为可选，且intention参数不支持DRAG，根据传入的参数做相应的校验以返回不同的值。 |
| callback | AsyncCallback<Array<UnifiedData>> | 是 | 回调函数，返回查询到的所有数据。 如果options中填入的是key，则返回key对应的数据； 如果options中填入的是intention，则返回intention下所有数据。 如intention和key均填写了，取两者查询数据的交集，与options只填入key的获取结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
};

try {
  unifiedDataChannel.queryData(options, (err, data) => {
    if (err === undefined) {
      console.info(`Succeeded in querying data. size = ${data.length}`);
      for (let i = 0; i < data.length; i++) {
        let records = data[i].getRecords();
        for (let j = 0; j < records.length; j++) {
          if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
            let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
            console.info(`${i + 1}.${text.textContent}`);
          }
    } else {
      console.error(`Failed to query data. code is ${err.code}, message is ${err.message} `);
    }
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Query data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.queryData

queryData(options: Options): Promise<Array<UnifiedData>>

查询UDMF公共数据通路的数据，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，key和intention均为可选，且intention参数不支持DRAG，根据传入的参数做相应的校验以返回不同的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<UnifiedData>> | Promise对象，返回查询到的所有数据。 如果options中填入的是key，则返回key对应的数据。 如果options中填入的是intention，则返回intention下所有数据。 如intention和key均填写了，取两者查询数据的交集，与options只填入key的获取结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let options: unifiedDataChannel.Options = {
  key: 'udmf://DataHub/com.ohos.test/0123456789'
};

try {
  unifiedDataChannel.queryData(options).then((data) => {
    console.info(`Succeeded in querying data. size = ${data.length}`);
    for (let i = 0; i < data.length; i++) {
      let records = data[i].getRecords();
      for (let j = 0; j < records.length; j++) {
        if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
          let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
          console.info(`${i + 1}.${text.textContent}`);
        }
  }).catch((err: BusinessError) => {
    console.error(`Failed to query data. code is ${err.code}, message is ${err.message} `);
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Query data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.deleteData

deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void

删除UDMF公共数据通路的数据，返回删除的数据集，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，key和intention均为可选，且intention参数仅支持DATA_HUB，根据传入的参数做相应的校验以返回不同的值。 |
| callback | AsyncCallback<Array<UnifiedData>> | 是 | 回调函数，返回删除的所有数据。 如果options中填入的是key，则删除key对应的数据并返回该数据。 如果options中填入的是intention，则删除intention下所有数据并返回删除的数据。 如intention和key均填写了，取两者数据的交集进行删除，并返回删除的数据，与options只填入key的结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
};

try {
  unifiedDataChannel.deleteData(options, (err, data) => {
    if (err === undefined) {
      console.info(`Succeeded in deleting data. size = ${data.length}`);
      for (let i = 0; i < data.length; i++) {
        let records = data[i].getRecords();
        for (let j = 0; j < records.length; j++) {
          if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
            let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
            console.info(`${i + 1}.${text.textContent}`);
          }
    } else {
      console.error(`Failed to delete data. code is ${err.code}, message is ${err.message} `);
    }
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Delete data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.deleteData

deleteData(options: Options): Promise<Array<UnifiedData>>

删除UDMF公共数据通路的数据，返回删除的数据集，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Options | 是 | 配置项参数，key和intention均为可选，且intention参数仅支持DATA_HUB，根据传入的参数做相应的校验以返回不同的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<UnifiedData>> | Promise对象，返回删除的所有数据。 如果options中填入的是key，则删除key对应的数据并返回该数据。 如果options中填入的是intention，则删除intention下所有数据并返回删除的数据。 如intention和key均填写了，取两者数据的交集进行删除，并返回删除的数据，与options只填入key的结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let options: unifiedDataChannel.Options = {
  key: 'udmf://DataHub/com.ohos.test/0123456789'
};

try {
  unifiedDataChannel.deleteData(options).then((data) => {
    console.info(`Succeeded in deleting data. size = ${data.length}`);
    for (let i = 0; i < data.length; i++) {
      let records = data[i].getRecords();
      for (let j = 0; j < records.length; j++) {
        if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
          let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
          console.info(`${i + 1}.${text.textContent}`);
        }
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete data. code is ${err.code}, message is ${err.message} `);
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Query data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.setAppShareOptions14+

setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void

设置应用内拖拽通道数据可使用的范围[ShareOptions](#ZH-CN_TOPIC_0000002522080636__shareoptions12)，目前仅支持DRAG类型数据通道的管控设置。

**需要权限:** ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intention | Intention | 是 | 表示数据操作相关的数据通路类型，目前仅支持DRAG类型数据通道。 |
| shareOptions | ShareOptions | 是 | 指示UnifiedData支持的设备内使用范围。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[统一数据管理框架错误码]([统一数据管理框架错误码](../../errors/统一数据管理框架错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION". |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 20400001 | Settings already exist. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  unifiedDataChannel.setAppShareOptions(unifiedDataChannel.Intention.DRAG, unifiedDataChannel.ShareOptions.IN_APP);
  console.info(`[UDMF]setAppShareOptions success. `);
}catch (e){
  let error: BusinessError = e as BusinessError;
  console.error(`[UDMF]setAppShareOptions throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.removeAppShareOptions14+

removeAppShareOptions(intention: Intention): void

清除[setAppShareOptions](#ZH-CN_TOPIC_0000002522080636__unifieddatachannelsetappshareoptions14)设置的管控信息。

**需要权限:** ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intention | Intention | 是 | 表示数据操作相关的数据通路类型，目前仅支持DRAG类型数据通道。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION". |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  unifiedDataChannel.removeAppShareOptions(unifiedDataChannel.Intention.DRAG);
  console.info(`[UDMF]removeAppShareOptions success. `);
}catch (e){
  let error: BusinessError = e as BusinessError;
  console.error(`[UDMF]removeAppShareOptions throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### unifiedDataChannel.convertRecordsToEntries17+

convertRecordsToEntries(data: UnifiedData): void

本接口用于将传入的data转换成多样式数据结构。若原data使用多个record去承载同一份数据的不同样式，则可以使用此接口将原data转换为多样式数据结构。

当满足以下规则时进行转换，传入的data经转换后变为多样式数据结构：

1. data中的record数量大于1;
1. data中的properties中的tag值为"records_to_entries_data_format"。

否则不会产生任何行为。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | UnifiedData | 是 | 目标数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let details : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let plainTextObj : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'The weather is very good today',
  abstract : 'The weather is very good today',
  details : details
}
let htmlObj : uniformDataStruct.HTML = {
  uniformDataType :'general.html',
  htmlContent : '<div><p>The weather is very good today</p></div>',
  plainContent : 'The weather is very good today',
  details : details
}
let plainText = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextObj);
let html = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HTML, htmlObj);
let unifiedData = new unifiedDataChannel.UnifiedData(plainText);
unifiedData.addRecord(html);
unifiedData.properties.tag = 'records_to_entries_data_format';

try {
  unifiedDataChannel.convertRecordsToEntries(unifiedData);
  let records: Array<unifiedDataChannel.UnifiedRecord> = unifiedData.getRecords();
  console.info(`Records size is ${records.length}`); // After conversion, its length must be less than 1
  if (records.length == 1) {
    let plainTextObjRead: uniformDataStruct.PlainText = records[0].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
    console.info(`TextContent is ${plainTextObjRead.textContent}`);
    let htmlObjRead: uniformDataStruct.HTML = records[0].getEntry(uniformTypeDescriptor.UniformDataType.HTML) as uniformDataStruct.HTML;
    console.info(`HtmlContent is ${htmlObjRead.htmlContent}`);
  }
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Convert data throws an exception. code is ${error.code}, message is ${error.message} `);
}
```