# @ohos.data.uniformDataStruct (标准化数据结构)

本模块为统一数据管理框架（Unified Data Management Framework，UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景提供了部分标准化数据类型[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)对应的数据结构，方便不同应用间进行数据交互，减少数据类型适配的工作量。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { uniformDataStruct } from '@kit.ArkData';
```

#### PlainText

纯文本类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'general.plain-text'是否统一数据类型标识，标识为纯文本类型数据，固定为“general.plain-text”，数据类型描述信息见[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)。textContentstring否否纯文本内容。abstractstring否是纯文本摘要，非必填字段，默认值为空字符串。detailsRecord<string, string>否是

是一个字典类型对象，key和value都是string类型，用于描述文本内容详细属性。例如，可生成一个details内容为

{

"title":"标题",

"content":"内容"

}

的数据对象，用于描述一篇文章的详细属性。非必填字段，默认值为空字典对象。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let plainTextDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let plainText : uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent : 'This is plainText textContent example',
  abstract : 'this is abstract',
  details : plainTextDetails
}
console.info('plainText.uniformDataType: ' + plainText.uniformDataType);
if(plainText.details != undefined){
  let plainTextDetailsObj : Record<string, string> = plainText.details;
  for(let kv of Object.entries(plainTextDetailsObj)) {
    console.info('plainText.details.attr: ' + kv[0] + ', value:' + kv[1]);
  }
}
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
```

#### Hyperlink

超链接类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'general.hyperlink'是否统一数据类型标识为超链接类型数据，固定为“general.hyperlink”，数据类型描述信息见[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)。urlstring否否链接url。descriptionstring否是链接内容描述，非必填字段，默认值为空字符串。detailsRecord<string, string>否是

是一个字典类型对象，key和value都是string类型，用于描述Hyperlink的详细属性内容。例如，可生成一个details内容为

{

"title":"标题",

"content":"内容"

}

的数据对象。非必填字段，默认值为空字典对象。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let hyperlinkDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of this hyperlink',
  details : hyperlinkDetails
}
console.info('hyperlink.uniformDataType: ' + hyperlink.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
```

#### HTML

HTML类型数据，用于描述超文本标记语言数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'general.html'是否统一数据类型标识为html类型数据，固定为“general.html”，数据类型描述信息见[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)。htmlContentstring否否html格式内容。plainContentstring否是去除html标签后的纯文本内容，非必填字段，默认值为空字符串。detailsRecord<string, string>否是

是一个字典类型对象，key和value都是string类型，用于描述HTML的详细属性内容。例如，可生成一个details内容为

{

"title":"标题",

"content":"内容"

}

的数据对象。非必填字段，默认值为空字典对象。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let htmlObjDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let htmlObj : uniformDataStruct.HTML = {
  uniformDataType :'general.html',
  htmlContent : '<div><p>标题</p></div>',
  plainContent : 'this is plainContent',
  details : htmlObjDetails
}
console.info('htmlObj.uniformDataType: ' + htmlObj.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HTML, htmlObj);
```

#### OpenHarmonyAppItem

系统定义的桌面图标类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'openharmony.app-item'是否统一数据类型标识为桌面图标类型数据，固定为“openharmony.app-item”，数据类型描述信息见[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)。appIdstring否否图标对应的应用id。appNamestring否否图标对应的应用名。appIconIdstring否否图标的图片id。appLabelIdstring否否图标名称对应的标签id。bundleNamestring否否图标对应的应用bundle名。abilityNamestring否否图标对应的应用ability名。detailsRecord<string, number | string | Uint8Array>否是是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let appItemDetails : Record<string, number | string | Uint8Array> = {
  'appItemKey1': 123,
  'appItemKey2': 'appItemValue',
  'appItemKey3': u8Array
}
let appItem : uniformDataStruct.OpenHarmonyAppItem = {
  uniformDataType:'openharmony.app-item',
  appId : 'MyAppId',
  appName : 'MyAppName',
  appIconId : 'MyAppIconId',
  appLabelId : 'MyAppLabelId',
  bundleName : 'MyBundleName',
  abilityName : 'MyAbilityName',
  details : appItemDetails
}
console.info('appItem.uniformDataType: ' + appItem.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_APP_ITEM, appItem);
```

#### ContentForm14+

内容卡片类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'general.content-form'是否统一数据类型标识为内容卡片类型数据，固定为“general.content-form”。titlestring否否内容卡片的标题。thumbDataUint8Array否是内容卡片对应的图片数据。descriptionstring否是内容卡片中的描述信息。appIconUint8Array否是内容卡片中的应用图标数据。appNamestring否是内容卡片中应用的应用名。linkUristring否是内容卡片对应的跳转超链接。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let thumbDataU8Array = new Uint8Array([1, 2, 3, 4, 5]);
let appIconU8Array = new Uint8Array([6, 7, 8, 9, 10]);
let contentForm : uniformDataStruct.ContentForm = {
  uniformDataType : 'general.content-form',
  title : 'MyTitle',
  thumbData : thumbDataU8Array,
  description : 'MyDescription',
  appName : 'MyAppName',
  linkUri : 'MyLinkUri',
  appIcon : appIconU8Array
}
console.info('contentForm.uniformDataType: ' + contentForm.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.CONTENT_FORM, contentForm);
```

#### Form15+

系统定义的卡片类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'openharmony.form'是否统一数据类型标识为卡片类型数据，固定为“openharmony.form”，数据类型描述信息见[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)。formIdnumber否否卡片id。formNamestring否否卡片名。bundleNamestring否否卡片所属的bundle名。abilityNamestring否否卡片对应的ability名。modulestring否否卡片所属的module名。detailsRecord<string, number | string | Uint8Array>否是是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let formDetails : Record<string, number | string | Uint8Array> = {
  'formKey1': 123,
  'formKey2': 'formValue',
  'formKey3': u8Array
}
let form : uniformDataStruct.Form = {
  uniformDataType : 'openharmony.form',
  formId : 1,
  formName : 'formName',
  bundleName : 'com.xx.app',
  abilityName : 'abilityName',
  module : 'module',
  details : formDetails
}
console.info('form.uniformDataType: ' + form.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
```

#### FileUri15+

文件地址类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'general.file-uri'是否统一数据类型标识为文件地址类型数据，固定为“general.file-uri”，数据类型描述信息见[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)。oriUristring否否文件路径。fileTypestring否否文件类型（必须是UTD类型，详情参考[UTD预置列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list)）。fileType最大长度限制为1024个字节。detailsRecord<string, number | string | Uint8Array>否是是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let fileUriDetails : Record<string, number | string | Uint8Array> = {
  'fileUriKey1': 123,
  'fileUriKey2': 'fileUriValue',
  'fileUriKey3': u8Array
}
let fileUri : uniformDataStruct.FileUri = {
  uniformDataType : 'general.file-uri',
  oriUri : 'www.xx.com',
  fileType : 'general.image',
  details : fileUriDetails
}
console.info('fileUri.uniformDataType: ' + fileUri.uniformDataType);
// 当使用FileUri类型的标准化数据结构构造record时，推荐入参中的type值设为uniformTypeDescriptor.UniformDataType.FILE_URI
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
```

#### PixelMap15+

系统定义的像素图类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明uniformDataType'openharmony.pixel-map'是否统一数据类型标识为像素图类型数据，固定为“openharmony.pixel-map”，数据类型描述信息见[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md#ZH-CN_TOPIC_0000002497444710__uniformdatatype)。pixelMapimage.PixelMap否否像素图二进制数据。detailsRecord<string, number | string | Uint8Array>否是是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。

**示例：**

```ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let arrayBuffer = new ArrayBuffer(4*200*200);
let opt : image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 }, alphaType: 3 };
let pixelMapDetails : Record<string, number | string | Uint8Array> = {
  'pixelMapKey1': 123,
  'pixelMapKey2': 'pixelMapValue',
  'pixelMapKey3': u8Array
}
let pixelMap : uniformDataStruct.PixelMap = {
  uniformDataType : 'openharmony.pixel-map',
  pixelMap : image.createPixelMapSync(arrayBuffer, opt),
  details : pixelMapDetails
}
console.info('pixelMap.uniformDataType: ' + pixelMap.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
```