# @ohos.pasteboard (剪贴板)

本模块提供管理系统剪贴板的能力，支持系统复制、粘贴功能。系统剪贴板支持对文本、HTML、URI、Want、PixelMap等内容的操作。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { pasteboard } from '@kit.BasicServicesKit';
```

#### 常量

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称类型值说明MAX_RECORD_NUM7+number-

API version 10之前，此常量值为512，表示单个PasteData中所能包含的最大条目数为512。当剪贴板内容中添加的条目达到数量上限512后，后续的添加操作无效。

从API version 10开始，不再限制单个PasteData中所能包含的最大条目数。

MIMETYPE_TEXT_HTML7+string'text/html'HTML内容的MIME类型定义。MIMETYPE_TEXT_WANT7+string'text/want'Want内容的MIME类型定义。MIMETYPE_TEXT_PLAIN7+string'text/plain'纯文本内容的MIME类型定义。MIMETYPE_TEXT_URI7+string'text/uri'URI内容的MIME类型定义。MIMETYPE_PIXELMAP9+string'pixelMap'PixelMap内容的MIME类型定义。

#### ValueType9+

type ValueType = string | image.PixelMap | Want | ArrayBuffer

用于表示允许的数据字段类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

类型说明string表示string的类型。image.PixelMap表示[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)的类型。Want表示[Want](@ohos.app.ability.Want (Want).md)的类型。ArrayBuffer表示ArrayBuffer的类型。

#### pasteboard.createData9+

createData(mimeType: string, value: ValueType): PasteData

构建一个指定类型的剪贴板内容对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明mimeTypestring是剪贴板数据对应的MIME类型，可以是[常量](#ZH-CN_TOPIC_0000002497445528__常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值, mimeType长度不能超过1024字节。value[ValueType](#ZH-CN_TOPIC_0000002497445528__valuetype9)是自定义数据内容。

**返回值：**

类型说明[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)剪贴板内容对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.

**示例1：**

```ets
let dataXml = new ArrayBuffer(256);
let pasteData: pasteboard.PasteData = pasteboard.createData('app/xml', dataXml);
```

**示例2：**

```ets
let dataText = 'hello';
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, dataText);
```

#### pasteboard.createData14+

createData(data: Record<string, ValueType>): PasteData

构建一个包含多个类型数据的剪贴板内容对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明data[Record](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts#对象字面量)<string, [ValueType](#ZH-CN_TOPIC_0000002497445528__valuetype9)>是

Record的key为剪贴板数据对应的MIME类型。可以是[常量](#ZH-CN_TOPIC_0000002497445528__常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型。也可以是自定义的MIME类型，可自定义此参数值，mimeType长度不能超过1024字节。

Record的value为key中指定MIME类型对应的数据。

Record中的首个key-value指定的MIME类型，会作为剪贴板内容对象中首个PasteDataRecord的默认MIME类型，非默认类型的数据在粘贴时只能使用[getData](#ZH-CN_TOPIC_0000002497445528__getdata14)接口读取。

**返回值：**

类型说明[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)剪贴板内容对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.

**示例1：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData({
    'text/plain': 'hello',
    'app/xml': new ArrayBuffer(256),
});
```

**示例2：**

```ets
let record: Record<string, pasteboard.ValueType> = {};
record[pasteboard.MIMETYPE_TEXT_PLAIN] = 'hello';
record[pasteboard.MIMETYPE_TEXT_URI] = 'dataability:///com.example.myapplication1/user.txt';
let pasteData: pasteboard.PasteData = pasteboard.createData(record);
```

#### pasteboard.createRecord9+

createRecord(mimeType: string, value: ValueType): PasteDataRecord

创建一条指定类型的数据内容条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明mimeTypestring是剪贴板数据对应的MIME类型，可以是[常量](#ZH-CN_TOPIC_0000002497445528__常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值，mimeType长度不能超过1024字节。value[ValueType](#ZH-CN_TOPIC_0000002497445528__valuetype9)是指定类型对应的数据内容。

**返回值：**

类型说明[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)一条新建的指定类型的数据内容条目。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.

**示例1：**

```ets
let dataXml = new ArrayBuffer(256);
let pasteDataRecord: pasteboard.PasteDataRecord = pasteboard.createRecord('app/xml', dataXml);
```

**示例2：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);
```

#### pasteboard.getSystemPasteboard

getSystemPasteboard(): SystemPasteboard

获取系统剪贴板对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明[SystemPasteboard](#ZH-CN_TOPIC_0000002497445528__systempasteboard)系统剪贴板对象。

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

#### ShareOption9+

可粘贴数据的范围类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称值说明INAPP0表示仅允许同应用内粘贴。LOCALDEVICE1表示允许在任何应用内粘贴。用户在“设置-多设备协同-跨设备剪贴板开关”选项中控制允许跨设备粘贴，表示允许跨设备在任何应用内粘贴。CROSSDEVICE(deprecated)2

表示允许跨设备在任何应用内粘贴。

从API version 12开始废弃，无替代接口和替代方法，后续由用户在“设置-多设备协同-跨设备剪贴板开关”选项中控制是否允许跨设备粘贴。

#### pasteboard.createHtmlData(deprecated)

createHtmlData(htmlText: string): PasteData

构建一个HTML剪贴板内容对象。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#ZH-CN_TOPIC_0000002497445528__pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明htmlTextstring是HTML内容。

**返回值：**

类型说明[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)剪贴板内容对象。

**示例：**

```ets
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let pasteData: pasteboard.PasteData = pasteboard.createHtmlData(html);
```

#### pasteboard.createWantData(deprecated)

createWantData(want: Want): PasteData

构建一个Want剪贴板内容对象。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#ZH-CN_TOPIC_0000002497445528__pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是Want内容。

**返回值：**

类型说明[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)剪贴板内容对象。

**示例：**

```ets
import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let pasteData: pasteboard.PasteData = pasteboard.createWantData(object);
```

#### pasteboard.createPlainTextData(deprecated)

createPlainTextData(text: string): PasteData

构建一个纯文本剪贴板内容对象。

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#ZH-CN_TOPIC_0000002497445528__pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明textstring是纯文本内容。

**返回值：**

类型说明[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)剪贴板内容对象。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
```

#### pasteboard.createUriData(deprecated)

createUriData(uri: string): PasteData

构建一个URI剪贴板内容对象。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#ZH-CN_TOPIC_0000002497445528__pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明uristring是URI内容。

**返回值：**

类型说明[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)剪贴板内容对象。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createUriData('dataability:///com.example.myapplication1/user.txt');
```

#### pasteboard.createHtmlTextRecord(deprecated)

createHtmlTextRecord(htmlText: string): PasteDataRecord

创建一条HTML内容的条目。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#ZH-CN_TOPIC_0000002497445528__pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明htmlTextstring是HTML内容。

**返回值：**

类型说明[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)一条新建的HTML内容条目。

**示例：**

```ets
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createHtmlTextRecord(html);
```

#### pasteboard.createWantRecord(deprecated)

createWantRecord(want: Want): PasteDataRecord

创建一条Want内容条目。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#ZH-CN_TOPIC_0000002497445528__pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是Want内容。

**返回值：**

类型说明[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)一条新建的Want内容条目。

**示例：**

```ets
import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let record: pasteboard.PasteDataRecord = pasteboard.createWantRecord(object);
```

#### pasteboard.createPlainTextRecord(deprecated)

createPlainTextRecord(text: string): PasteDataRecord

创建一条纯文本内容条目。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#ZH-CN_TOPIC_0000002497445528__pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明textstring是纯文本内容。

**返回值：**

类型说明[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)一条新建的纯文本内容条目。

**示例：**

```ets
let record: pasteboard.PasteDataRecord = pasteboard.createPlainTextRecord('hello');
```

#### pasteboard.createUriRecord(deprecated)

createUriRecord(uri: string): PasteDataRecord

创建一条URI内容的条目。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#ZH-CN_TOPIC_0000002497445528__pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明uristring是URI内容。

**返回值：**

类型说明[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)一条新建的URI内容条目。

**示例：**

```ets
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
```

#### PasteDataProperty7+

定义剪贴板中所有内容条目的属性，包含时间戳、数据类型、粘贴范围以及一些附加数据等，该属性必须通过[setProperty](#ZH-CN_TOPIC_0000002497445528__setproperty9)方法，才能设置到剪贴板中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称类型只读可选说明additions7+{[key:string]:object}否否设置其他附加属性数据。不支持动态追加属性，只能通过重新赋值的方式修改附加值，具体见相关示例setProperty， 默认为空。mimeTypes7+Array<string>是否剪贴板内容条目的数据类型，非重复的类型列表。tag7+string否否用户自定义标签，默认为空。timestamp7+number是否剪贴板数据的写入时间戳（单位：ms）。localOnly7+boolean否否配置剪贴板内容是否为“仅在本地”，默认值为false。其值会被shareOption属性覆盖，推荐使用[ShareOption](#ZH-CN_TOPIC_0000002497445528__shareoption9)属性。shareOption9+[ShareOption](#ZH-CN_TOPIC_0000002497445528__shareoption9)否否指示剪贴板数据可以粘贴到的范围，默认值为CROSSDEVICE。

#### FileConflictOptions15+

定义文件拷贝冲突时的选项。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称值说明OVERWRITE0目标路径存在同文件名时覆盖。SKIP1目标路径存在同文件名时跳过，若设置SKIP，应用获取到的粘贴数据不包含跳过文件。

#### ProgressIndicator15+

定义进度条指示选项，可选择是否采用系统默认进度显示。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称值说明NONE0不采用系统默认进度显示。DEFAULT1采用系统默认进度显示。

#### ProgressInfo15+

定义进度上报的数据结构，且仅当进度指示选项[ProgressIndicator](#ZH-CN_TOPIC_0000002497445528__progressindicator15)设置为NONE时才会上报此信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称类型只读可选说明progressnumber否否不使用系统提供的进度条时，系统上报拷贝粘贴任务进度百分比。

#### ProgressListener15+

type ProgressListener = (progress: ProgressInfo) => void

定义进度数据变化的订阅函数，当选择不使用系统默认进度显示时，可设置该项获取粘贴过程的进度。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明progress[ProgressInfo](#ZH-CN_TOPIC_0000002497445528__progressinfo15)是定义进度上报的数据结构，且仅当进度指示选项[ProgressIndicator](#ZH-CN_TOPIC_0000002497445528__progressindicator15)设置为NONE时才会上报此信息。

#### ProgressSignal15+

定义进度取消的函数，在粘贴过程中可选择取消任务，且仅当进度指示选项[ProgressIndicator](#ZH-CN_TOPIC_0000002497445528__progressindicator15)设置为NONE时此参数才有意义。

**系统能力：** SystemCapability.MiscServices.Pasteboard

#### cancel15+

cancel(): void

取消正在进行的拷贝粘贴任务。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```ets
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { fileUri} from '@kit.CoreFileKit';
@Entry
@Component
struct PasteboardTest {
 build() {
   RelativeContainer() {
     Column() {
       Column() {
         Button("Copy txt")
           .onClick(async ()=>{
              let text = "test";
              let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
              let systemPasteboard = pasteboard.getSystemPasteboard();
              await systemPasteboard.setData(pasteData);
              let signal = new pasteboard.ProgressSignal;
              let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
                console.info('progressListener success, progress:' + progress.progress);
                signal.cancel();
              };
              let destPath: string = '/data/storage/el2/base/files/';
              let destUri : string = fileUri.getUriFromPath(destPath);
              let params: pasteboard.GetDataParams = {
                destUri: destUri,
                fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
                progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
                progressListener: progressListenerInfo,
              };
              systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
                console.error('getDataWithProgress succ');
              }).catch((err: BusinessError) => {
                console.error('Failed to get PasteData. Cause: ' + err.message);
              })
          })
        }
      }
    }
  }
}
```

#### GetDataParams15+

应用在使用剪贴板提供的文件拷贝能力的情况下需要的参数，包含目标路径、文件冲突选项、进度条类型等。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称类型只读可选说明destUristring否是拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理，默认为空。fileConflictOptions[FileConflictOptions](#ZH-CN_TOPIC_0000002497445528__fileconflictoptions15)否是定义文件拷贝冲突时的选项，默认为OVERWRITE。progressIndicator[ProgressIndicator](#ZH-CN_TOPIC_0000002497445528__progressindicator15)否否定义进度条指示选项，可选择是否采用系统默认进度显示。progressListener[ProgressListener](#ZH-CN_TOPIC_0000002497445528__progresslistener15)否是定义进度数据变化的订阅函数，当选择不使用系统默认进度显示时，可设置该项获取粘贴过程的进度，默认为空。progressSignal[ProgressSignal](#ZH-CN_TOPIC_0000002497445528__progresssignal15)否是定义进度取消的函数，在粘贴过程中可选择取消任务，且仅当进度指示选项[ProgressIndicator](#ZH-CN_TOPIC_0000002497445528__progressindicator15)设置为NONE时此参数才有意义，默认为空。

#### PasteDataRecord7+

对于剪贴板中内容记录的抽象定义，称之为条目。剪贴板内容部分由一个或者多个条目构成，例如一条文本内容、一份HTML、一个URI或者一个Want。

#### 属性

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称类型只读可选说明htmlText7+string否否HTML内容。want7+[Want](@ohos.app.ability.Want (Want).md)否否Want内容。mimeType7+string否否默认数据类型。plainText7+string否否纯文本内容。uri7+string否否URI内容。pixelMap9+[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)否否PixelMap内容。data9+{[mimeType: string]: ArrayBuffer}否否自定义数据内容。

#### toPlainText9+

toPlainText(): string

将一个PasteDataRecord中的html、plain、uri内容强制转换为文本内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明string纯文本内容。

**示例：**

```ets
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, '<html>hello</html>');
let text: string = record.toPlainText();
console.info(`Succeeded in converting to text. Text: ${text}`);
```

#### addEntry14+

addEntry(type: string, value: ValueType): void

往一个PasteDataRecord中额外添加一种样式的自定义数据。此方式添加的MIME类型都不是Record的默认类型，粘贴时只能使用[getData](#ZH-CN_TOPIC_0000002497445528__getdata14)接口读取对应数据。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明typestring是剪贴板数据对应的MIME类型，可以是[常量](#ZH-CN_TOPIC_0000002497445528__常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值，mimeType长度不能超过1024字节。value[ValueType](#ZH-CN_TOPIC_0000002497445528__valuetype9)是自定义数据内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.

**示例：**

```ets
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
```

#### getValidTypes14+

getValidTypes(types: Array<string>): Array<string>

根据传入的MIME类型，返回传入的MIME类型和剪贴板中数据的MIME类型的交集。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明typesArray<string>是MIME类型列表。

**返回值：**

类型说明Array<string>传入的MIME类型和剪贴板中数据的MIME类型的交集。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.

**示例：**

```ets
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
let types: string[] = record.getValidTypes([
    pasteboard.MIMETYPE_TEXT_PLAIN,
    pasteboard.MIMETYPE_TEXT_HTML,
    pasteboard.MIMETYPE_TEXT_URI,
    pasteboard.MIMETYPE_TEXT_WANT,
    pasteboard.MIMETYPE_PIXELMAP
]);
```

#### getData14+

getData(type: string): Promise<ValueType>

从PasteDataRecord中获取指定MIME类型的自定义数据。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明typestring是MIME类型。

**返回值：**

类型说明Promise<[ValueType](#ZH-CN_TOPIC_0000002497445528__valuetype9)>

Promise对象，返回PasteDataRecord中指定MIME类型的自定义数据。

PasteDataRecord中包含多个MIME类型数据时，非PasteDataRecord的默认MIME类型的数据只能通过本接口获取。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
record.getData(pasteboard.MIMETYPE_TEXT_PLAIN).then((value: pasteboard.ValueType) => {
    let textPlainContent = value as string;
    console.info('Success to get text/plain value. value is: ' + textPlainContent);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/plain value. Cause: ' + err.message);
});
record.getData(pasteboard.MIMETYPE_TEXT_URI).then((value: pasteboard.ValueType) => {
    let uri = value as string;
    console.info('Success to get text/uri value. value is: ' + uri);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/uri value. Cause: ' + err.message);
});
```

#### convertToText(deprecated)

convertToText(callback: AsyncCallback<string>): void

将一个PasteData中的内容强制转换为文本内容，使用callback异步回调。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[toPlainText](#ZH-CN_TOPIC_0000002497445528__toplaintext9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是回调函数，当转换成功，err为undefined，data为强制转换的文本内容；否则返回错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: Incorrect parameters types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText((err: BusinessError, data: string) => {
    if (err) {
        console.error(`Failed to convert to text. Cause: ${err.message}`);
        return;
    }
    console.info(`Succeeded in converting to text. Data: ${data}`);
});
```

#### convertToText(deprecated)

convertToText(): Promise<string>

将一个PasteData中的内容强制转换为文本内容，使用Promise异步回调。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[toPlainText](#ZH-CN_TOPIC_0000002497445528__toplaintext9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<string>Promise对象，返回强制转换的文本内容。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText().then((data: string) => {
    console.info(`Succeeded in converting to text. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to convert to text. Cause: ${err.message}`);
});
```

#### PasteData

剪贴板内容对象。剪贴板内容包含一个或者多个内容条目（[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)）以及属性描述对象（[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)）。

在调用PasteData的接口前，需要先通过[createData()](#ZH-CN_TOPIC_0000002497445528__pasteboardcreatedata9)或[getData()](#ZH-CN_TOPIC_0000002497445528__getdata9)获取一个PasteData对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

#### getPrimaryText

getPrimaryText(): string

获取第一条纯文本内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明string纯文本内容。剪贴板内容对象中没有纯文本内容时，默认返回为undefined。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### getPrimaryHtml7+

getPrimaryHtml(): string

获取第一条的HTML内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明stringHTML内容。剪贴板内容对象中没有HTML内容时，默认返回为undefined。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let htmlText: string = pasteData.getPrimaryHtml();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### getPrimaryWant7+

getPrimaryWant(): Want

获取第一条的Want对象内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明[Want](@ohos.app.ability.Want (Want).md)Want对象内容。剪贴板内容对象中没有Want内容时，默认返回为undefined。

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let want: Want = pasteData.getPrimaryWant();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### getPrimaryUri7+

getPrimaryUri(): string

获取第一条的URI内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明stringURI内容。剪贴板内容对象中没有URI内容时，默认返回为undefined。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let uri: string = pasteData.getPrimaryUri();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### getPrimaryPixelMap9+

getPrimaryPixelMap(): image.PixelMap

获取第一条的PixelMap内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)PixelMap内容。剪贴板内容对象中没有PixelMap内容时，默认返回为undefined。

**示例：**

```ets
import { image } from '@kit.ImageKit';

let buffer = new ArrayBuffer(128);
let realSize: image.Size = { height: 3, width: 5 };
let opt: image.InitializationOptions = {
    size: realSize,
    pixelFormat: 3,
    editable: true,
    alphaType: 1,
    scaleMode: 1
};
image.createPixelMap(buffer, opt).then((pixelMap: image.PixelMap) => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_PIXELMAP, pixelMap);
    let PixelMap: image.PixelMap = pasteData.getPrimaryPixelMap();
});
```

#### addRecord7+

addRecord(record: PasteDataRecord): void

向当前剪贴板内容中添加一条条目，同时也会将条目类型添加到[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明record[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)是待添加的条目。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
let textRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let htmlRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, html);
pasteData.addRecord(textRecord);
pasteData.addRecord(htmlRecord);
```

#### addRecord9+

addRecord(mimeType: string, value: ValueType): void

向当前剪贴板内容中添加一条数据内容条目，同时也会将数据类型添加到[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明mimeTypestring是数据的MIME类型， 其长度不能超过1024字节。value[ValueType](#ZH-CN_TOPIC_0000002497445528__valuetype9)是数据内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
let dataXml = new ArrayBuffer(256);
pasteData.addRecord('app/xml', dataXml);
```

#### getMimeTypes7+

getMimeTypes(): Array<string>

获取剪贴板中[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的mimeTypes列表，接口调用异常时返回undefined。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Array<string>剪贴板内容条目的数据类型，非重复的类型列表。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let types: string[] = pasteData.getMimeTypes();
```

#### getPrimaryMimeType7+

getPrimaryMimeType(): string

获取剪贴板内容中首个条目的数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明string首个条目的数据类型。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let type: string = pasteData.getPrimaryMimeType();
```

#### getProperty7+

getProperty(): PasteDataProperty

获取剪贴板内容的属性描述对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)属性描述对象。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let property: pasteboard.PasteDataProperty = pasteData.getProperty();
```

#### setProperty9+

setProperty(property: PasteDataProperty): void

设置剪贴板内容的属性描述对象[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明property[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)是属性描述对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
type AdditionType = Record<string, Record<string, Object>>;

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_HTML, 'application/xml');
let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
prop.shareOption = pasteboard.ShareOption.INAPP;
// 需要注意，不支持对addition进行追加属性的操作，只能通过重新赋值的方式达到追加属性的目的。
prop.additions = { 'TestOne': { 'Test': 123 }, 'TestTwo': { 'Test': 'additions' } } as AdditionType;
prop.tag = 'TestTag';
pasteData.setProperty(prop);
```

[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的localOnly与shareOption属性互斥，最终结果以shareOption为准，shareOption会影响localOnly的值。

```ets
(async () => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
    let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
    prop.shareOption = pasteboard.ShareOption.INAPP;
    prop.localOnly = false;
    pasteData.setProperty(prop);
    const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });

    prop.shareOption = pasteboard.ShareOption.LOCALDEVICE;
    prop.localOnly = false;
    pasteData.setProperty(prop);

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });
})
```

#### getRecord9+

getRecord(index: number): PasteDataRecord

获取剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明indexnumber是指定条目的下标。

**返回值：**

类型说明[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)指定下标的条目。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900001The index is out of the record.401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);
```

#### getRecordCount7+

getRecordCount(): number

获取剪贴板内容中条目的个数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明number条目的个数。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let count: number = pasteData.getRecordCount();
```

#### getTag7+

getTag(): string

获取剪贴板内容中用户自定义的标签内容，如果没有设置用户自定义的标签内容将返回空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明string返回用户自定义的标签内容，如果没有设置用户自定义的标签内容，将返回空。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let tag: string = pasteData.getTag();
```

#### hasType9+

hasType(mimeType: string): boolean

检查剪贴板内容中是否有指定的MIME数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明mimeTypestring是待查询的数据类型。可以是[常量](#ZH-CN_TOPIC_0000002497445528__常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型。

**返回值：**

类型说明boolean有指定的数据类型返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let hasType: boolean = pasteData.hasType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

#### removeRecord9+

removeRecord(index: number): void

移除剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明indexnumber是指定的下标。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900001The index is out of the record.401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
pasteData.removeRecord(0);
```

#### replaceRecord9+

replaceRecord(index: number, record: PasteDataRecord): void

替换剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明indexnumber是指定的下标。record[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)是被替换后的条目数据内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900001The index is out of the record.401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);
```

#### pasteStart12+

pasteStart(): void

读取剪贴板数据前，通知剪贴板服务保留跨设备通道。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    pasteData.pasteStart();
    console.info(`using data: ${pasteData.getPrimaryText()}`);
    pasteData.pasteComplete();
});
```

#### pasteComplete12+

pasteComplete(): void

通知剪贴板服务数据使用已完成。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    pasteData.pasteStart();
    console.info(`using data: ${pasteData.getPrimaryText()}`);
    pasteData.pasteComplete();
});
```

#### addHtmlRecord(deprecated)

addHtmlRecord(htmlText: string): void

向当前剪贴板内容中添加一条HTML内容条目，并将MIMETYPE_TEXT_HTML添加到[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#ZH-CN_TOPIC_0000002497445528__addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明htmlTextstring是HTML内容。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
pasteData.addHtmlRecord(html);
```

#### addWantRecord(deprecated)

addWantRecord(want: Want): void

向当前剪贴板内容中添加一条Want条目，并将MIMETYPE_TEXT_WANT添加到[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#ZH-CN_TOPIC_0000002497445528__addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是Want对象内容。

**示例：**

```ets
import { Want } from '@kit.AbilityKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
pasteData.addWantRecord(object);
```

#### addTextRecord(deprecated)

addTextRecord(text: string): void

向当前剪贴板内容中添加一条纯文本条目，并将MIME_TEXT_PLAIN添加到[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#ZH-CN_TOPIC_0000002497445528__addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明textstring是纯文本内容。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addTextRecord('good');
```

#### addUriRecord(deprecated)

addUriRecord(uri: string): void

向当前剪贴板内容中添加一条URI条目，并将MIMETYPE_TEXT_URI添加到[PasteDataProperty](#ZH-CN_TOPIC_0000002497445528__pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#ZH-CN_TOPIC_0000002497445528__addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明uristring是URI内容。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addUriRecord('dataability:///com.example.myapplication1/user.txt');
```

#### getRecordAt(deprecated)

getRecordAt(index: number): PasteDataRecord

获取剪贴板内容中指定下标的条目。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[getRecord](#ZH-CN_TOPIC_0000002497445528__getrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明indexnumber是指定条目的下标。

**返回值：**

类型说明[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)指定下标的条目。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecordAt(0);
```

#### hasMimeType(deprecated)

hasMimeType(mimeType: string): boolean

检查剪贴板内容中是否有指定的数据类型。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasType](#ZH-CN_TOPIC_0000002497445528__hastype9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明mimeTypestring是待查询的数据类型。

**返回值：**

类型说明boolean有指定的数据类型返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let hasType: boolean = pasteData.hasMimeType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

#### removeRecordAt(deprecated)

removeRecordAt(index: number): boolean

移除剪贴板内容中指定下标的条目。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[removeRecord](#ZH-CN_TOPIC_0000002497445528__removerecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明indexnumber是指定的下标。

**返回值：**

类型说明boolean成功移除返回true，失败返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let isRemove: boolean = pasteData.removeRecordAt(0);
```

#### replaceRecordAt(deprecated)

replaceRecordAt(index: number, record: PasteDataRecord): boolean

替换剪贴板内容中指定下标的条目。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[replaceRecord](#ZH-CN_TOPIC_0000002497445528__replacerecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明indexnumber是指定的下标。record[PasteDataRecord](#ZH-CN_TOPIC_0000002497445528__pastedatarecord7)是替换后的条目。

**返回值：**

类型说明boolean成功替换返回true，失败返回false。

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
let isReplace: boolean = pasteData.replaceRecordAt(0, record);
```

#### SystemPasteboard

系统剪贴板对象。

在调用SystemPasteboard的接口前，需要先通过[getSystemPasteboard](#ZH-CN_TOPIC_0000002497445528__pasteboardgetsystempasteboard)获取系统剪贴板。

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

#### on('update')7+

on(type: 'update', callback: () =>void): void

订阅系统剪贴板内容变化事件，当系统剪贴板中内容变化时触发用户程序的回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明typestring是取值为'update'，表示系统剪贴板内容变化事件。callbackfunction是剪贴板中内容变化时触发的用户程序的回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.on('update', listener);
```

#### off('update')7+

off(type: 'update', callback?: () =>void): void

取消订阅系统剪贴板内容变化事件。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明typestring是取值为'update'，表示系统剪贴板内容变化事件。callbackfunction否剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有监听回调，否则表示清除指定监听回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.off('update', listener);
```

#### clearData9+

clearData(callback: AsyncCallback<void>): void

清空系统剪贴板内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当成功清空时，err为undefined；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData((err, data) => {
    if (err) {
        console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
        return;
    }
    console.info('Succeeded in clearing the pasteboard.');
});
```

#### clearData9+

clearData(): Promise<void>

清空系统剪贴板内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData().then((data: void) => {
    console.info('Succeeded in clearing the pasteboard.');
}).catch((err: BusinessError) => {
    console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
});
```

#### setData9+

setData(data: PasteData, callback: AsyncCallback<void>): void

将数据写入系统剪贴板，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明data[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)是PasteData对象。callbackAsyncCallback<void>是回调函数。当写入成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息27787277Another copy or paste operation is in progress.27787278Replication is prohibited.401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

#### setData9+

setData(data: PasteData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明data[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)是PasteData对象。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息27787277Another copy or paste operation is in progress.27787278Replication is prohibited.401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error('Failed to set PasteData. Cause: ' + err.message);
});
```

#### getData9+

getData(callback: AsyncCallback<PasteData>): void

读取系统剪贴板内容，使用callback异步回调。

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callbackAsyncCallback<[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)>是回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息27787277Another copy or paste operation is in progress.201Permission verification failed. The application does not have the permission required to call the API.401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    let text: string = pasteData.getPrimaryText();
});
```

#### getData9+

getData(): Promise<PasteData>

读取系统剪贴板内容，使用Promise异步回调。

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)>Promise对象，返回系统剪贴板数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息27787277Another copy or paste operation is in progress.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### hasData9+

hasData(callback: AsyncCallback<boolean>): void

判断系统剪贴板中是否有内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. Cause: ${err.message}`);
        return;
    }
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
});
```

#### hasData9+

hasData(): Promise<boolean>

判断系统剪贴板中是否有内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<boolean>返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData().then((data: boolean) => {
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to check the PasteData. Cause: ${err.message}`);
});
```

#### clear(deprecated)

clear(callback: AsyncCallback<void>): void

清空系统剪贴板内容，使用callback异步回调。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.clearData](#ZH-CN_TOPIC_0000002497445528__cleardata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当成功清空时，err为undefined；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear((err, data) => {
    if (err) {
        console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
        return;
    }
    console.info('Succeeded in clearing the PasteData.');
});
```

#### clear(deprecated)

clear(): Promise<void>

清空系统剪贴板内容，使用Promise异步回调。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.clearData](#ZH-CN_TOPIC_0000002497445528__cleardata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear().then((data) => {
    console.info('Succeeded in clearing the PasteData.');
}).catch((err: BusinessError) => {
    console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
});
```

#### getPasteData(deprecated)

getPasteData(callback: AsyncCallback<PasteData>): void

读取系统剪贴板内容，使用callback异步回调。

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[getData](#ZH-CN_TOPIC_0000002497445528__getdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callbackAsyncCallback<[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)>是回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    let text: string = pasteData.getPrimaryText();
});
```

#### getPasteData(deprecated)

getPasteData(): Promise<PasteData>

读取系统剪贴板内容，使用Promise异步回调。

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[getData](#ZH-CN_TOPIC_0000002497445528__getdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)>Promise对象，返回系统剪贴板数据。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### hasPasteData(deprecated)

hasPasteData(callback: AsyncCallback<boolean>): void

判断系统剪贴板中是否有内容，使用callback异步回调。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasData](#ZH-CN_TOPIC_0000002497445528__hasdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. Cause: ${err.message}`);
        return;
    }
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
});
```

#### hasPasteData(deprecated)

hasPasteData(): Promise<boolean>

判断系统剪贴板中是否有内容，使用Promise异步回调。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasData](#ZH-CN_TOPIC_0000002497445528__hasdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<boolean>返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData().then((data: boolean) => {
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to check the PasteData. Cause: ${err.message}`);
});
```

#### setPasteData(deprecated)

setPasteData(data: PasteData, callback: AsyncCallback<void>): void

将数据写入系统剪贴板，使用callback异步回调。

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[setData](#ZH-CN_TOPIC_0000002497445528__setdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明data[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)是PasteData对象。callbackAsyncCallback<void>是回调函数。当写入成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

#### setPasteData(deprecated)

setPasteData(data: PasteData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[setData](#ZH-CN_TOPIC_0000002497445528__setdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明data[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)是PasteData对象。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error('Failed to set PasteData. Cause: ' + err.message);
});
```

#### isRemoteData11+

isRemoteData(): boolean

判断剪贴板中的数据是否来自其他设备。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明boolean是来自其他设备返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900005Excessive processing time for internal data.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.isRemoteData();
    console.info(`Succeeded in checking the RemoteData. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the RemoteData. Cause:' + err.message);
};
```

#### getDataSource11+

getDataSource(): string

获取数据来源的应用名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明string数据来源的应用名称。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900005Excessive processing time for internal data.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: string = systemPasteboard.getDataSource();
    console.info(`Succeeded in getting DataSource. Result: ${result}`);
} catch (err) {
    console.error('Failed to get DataSource. Cause:' + err.message);
};
```

#### hasDataType11+

hasDataType(mimeType: string): boolean

检查剪贴板内容中是否有指定类型的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明mimeTypestring是数据类型。

**返回值：**

类型说明boolean有指定类型的数据返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.12900005Excessive processing time for internal data.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_PLAIN);
    console.info(`Succeeded in checking the DataType. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the DataType. Cause:' + err.message);
};
```

#### clearDataSync11+

clearDataSync(): void

清空系统剪贴板内容, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900005Excessive processing time for internal data.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.clearDataSync();
    console.info('Succeeded in clearing the pasteboard.');
} catch (err) {
    console.error('Failed to clear the pasteboard. Cause:' + err.message);
};
```

#### getDataSync11+

getDataSync(): PasteData

读取系统剪贴板内容, 此接口为同步接口。

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)返回系统剪贴板数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900005Excessive processing time for internal data.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: pasteboard.PasteData = systemPasteboard.getDataSync();
    console.info('Succeeded in getting PasteData.');
} catch (err) {
    console.error('Failed to get PasteData. Cause:' + err.message);
};
```

#### setDataSync11+

setDataSync(data: PasteData): void

将数据写入系统剪贴板, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明data[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)是需要写入剪贴板中的数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.12900005Excessive processing time for internal data.

**示例：**

```ets
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setDataSync(pasteData);
    console.info('Succeeded in setting PasteData.');
} catch (err) {
    console.error('Failed to set PasteData. Cause:' + err.message);
};
```

#### hasDataSync11+

hasDataSync(): boolean

判断系统剪贴板中是否有内容, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明boolean返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息12900005Excessive processing time for internal data.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataSync();
    console.info(`Succeeded in checking the PasteData. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the PasteData. Cause:' + err.message);
};
```

#### getUnifiedData12+

getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>

读取系统剪贴板内容，使用Promise异步回调。

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<[unifiedDataChannel.UnifiedData](@ohos.data.unifiedDataChannel (标准化数据通路).md#ZH-CN_TOPIC_0000002529444653__unifieddata)>Promise对象，返回系统剪贴板数据。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.27787277Another copy or paste operation is in progress.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getUnifiedData().then((data) => {
    let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
    for (let j = 0; j < records.length; j++) {
        if (records[j].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
            let text = records[j].getValue() as uniformDataStruct.PlainText;
            console.info(`${j + 1}.${text.textContent}`);
        }
    }
}).catch((err: BusinessError) => {
    console.error('Failed to get UnifiedData. Cause: ' + err.message);
});
```

#### getUnifiedDataSync12+

getUnifiedDataSync(): unifiedDataChannel.UnifiedData

读取系统剪贴板内容, 此接口为同步接口。

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明[unifiedDataChannel.UnifiedData](@ohos.data.unifiedDataChannel (标准化数据通路).md#ZH-CN_TOPIC_0000002529444653__unifieddata)返回系统剪贴板数据。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.12900005Excessive processing time for internal data.

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: unifiedDataChannel.UnifiedData = systemPasteboard.getUnifiedDataSync();
    console.info('Succeeded in getting UnifiedData.');
} catch (err) {
    console.error('Failed to get UnifiedData. Cause:' + err.message);
};
```

#### setUnifiedData12+

setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明data[unifiedDataChannel.UnifiedData](@ohos.data.unifiedDataChannel (标准化数据通路).md#ZH-CN_TOPIC_0000002529444653__unifieddata)是需要写入剪贴板中的数据。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.27787277Another copy or paste operation is in progress.27787278Replication is prohibited.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
    uniformDataType: uniformTypeDescriptor.UniformDataType.PLAIN_TEXT,
    textContent : 'PLAINTEXT_CONTENT',
    abstract : 'PLAINTEXT_ABSTRACT',
}
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let data = new unifiedDataChannel.UnifiedData();
data.addRecord(record);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setUnifiedData(data).then((data: void) => {
    console.info('Succeeded in setting UnifiedData.');
}).catch((err: BusinessError) => {
    console.error('Failed to setUnifiedData. Cause: ' + err.message);
});
```

#### setUnifiedDataSync12+

setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void

将数据写入系统剪贴板, 此接口为同步接口。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明data[unifiedDataChannel.UnifiedData](@ohos.data.unifiedDataChannel (标准化数据通路).md#ZH-CN_TOPIC_0000002529444653__unifieddata)是需要写入剪贴板中的数据。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息401Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.12900005Excessive processing time for internal data.

**示例：**

```ets
import { unifiedDataChannel } from '@kit.ArkData';

let plainTextData = new unifiedDataChannel.UnifiedData();
let plainText = new unifiedDataChannel.PlainText();
plainText.details = {
    Key: 'delayPlaintext',
    Value: 'delayPlaintext',
};
plainText.textContent = 'delayTextContent';
plainText.abstract = 'delayTextContent';
plainTextData.addRecord(plainText);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setUnifiedDataSync(plainTextData);
    console.info('Succeeded in setting UnifiedData.');
} catch (err) {
    console.error('Failed to set UnifiedData. Cause:' + err.message);
};
```

#### setAppShareOptions14+

setAppShareOptions(shareOptions: ShareOption): void

应用设置本应用剪贴板数据的可粘贴范围。

**需要权限**：ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明shareOptions[ShareOption](@ohos.pasteboard (剪贴板).md#ZH-CN_TOPIC_0000002497445528__shareoption9)是可粘贴的范围，参数只允许pasteboard.ShareOption.INAPP。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12900006Settings already exist.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.setAppShareOptions(pasteboard.ShareOption.INAPP);
  console.info('Set app share options success.');
} catch (error) {
  console.error(`Set app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```

#### removeAppShareOptions14+

removeAppShareOptions(): void

删除应用全局的可粘贴的范围。

**需要权限**：ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.removeAppShareOptions();
  console.info('Remove app share options success.');
} catch (error) {
  console.error(`Remove app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```

#### Pattern13+

剪贴板支持检测的模式类型。

**系统能力：** SystemCapability.MiscServices.Pasteboard

名称值说明URL0URL类型。NUMBER1数字类型。EMAIL_ADDRESS2邮箱地址类型。

#### detectPatterns13+

detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>

检测**本地**剪贴板中存在的[Pattern](#ZH-CN_TOPIC_0000002497445528__pattern13)模式，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明patterns[Array<Pattern>](#ZH-CN_TOPIC_0000002497445528__pattern13)是需要在剪贴板中检测的模式。

**返回值：**

类型说明Promise<Array<Pattern>>Promise对象，返回检测到的模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. 3. Parameter verification failed.

**示例：**

```ets
import { pasteboard } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let patterns: Array<pasteboard.Pattern> = [pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL_ADDRESS];

systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
    if (patterns.sort().join('')==data.sort().join('')) {
      console.info('All needed patterns detected, next get data');
      try {
        let result: pasteboard.PasteData = systemPasteboard.getDataSync();
        console.info('Succeeded in getting PasteData.');
      } catch (err) {
        console.error('Failed to get PasteData. Cause:' + err.message);
      };
    } else {
      console.info("Not all needed patterns detected, no need to get data.");
    }
});
```

#### getMimeTypes14+

getMimeTypes(): Promise<Array<string>>

读取剪贴板中存在的MIME类型，使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明Promise<Array<string>>Promise对象，返回读取到的MIME类型。

**示例：**

```ets
import { pasteboard, BusinessError } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getMimeTypes().then((data: Array<String>) => {
    console.info('Succeeded in getting mimeTypes. mimeTypes: ' + data.sort().join(','));
}).catch((err: BusinessError) => {
    console.error('Failed to get mimeTypes. Cause:' + err.message);
});
```

#### getDataWithProgress15+

getDataWithProgress(params: GetDataParams): Promise<PasteData>

获取剪贴板的内容和进度，使用Promise异步回调，不支持对文件夹的拷贝。

**需要权限**：ohos.permission.READ_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。使用[安全控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明params[GetDataParams](#ZH-CN_TOPIC_0000002497445528__getdataparams15)是应用在使用剪贴板提供的文件拷贝能力的情况下需要的参数，包含目标路径、文件冲突选项、进度条类型等。

**返回值：**

类型说明Promise<[PasteData](#ZH-CN_TOPIC_0000002497445528__pastedata)>Promise对象，返回系统剪贴板数据。

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](../../errors/剪贴板错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error.12900003Another copy or paste operation is in progress.12900007Invalid destUri or file system error.12900008Failed to start progress.12900009Progress exits abnormally.12900010System error occurred during paste execution.

**示例：**

```ets
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { fileUri} from '@kit.CoreFileKit';
@Entry
@Component
struct PasteboardTest {
 build() {
   RelativeContainer() {
     Column() {
       Column() {
         Button("Copy txt")
           .onClick(async ()=>{
              let text = "test";
              let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
              let systemPasteboard = pasteboard.getSystemPasteboard();
              await systemPasteboard.setData(pasteData);
              let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
                console.info('progressListener success, progress:' + progress.progress);
              };
              let destPath: string = '/data/storage/el2/base/files/';
              let destUri : string = fileUri.getUriFromPath(destPath);
              let params: pasteboard.GetDataParams = {
                destUri: destUri,
                fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
                progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
                progressListener: progressListenerInfo,
              };
              systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
                console.error('getDataWithProgress succ');
              }).catch((err: BusinessError) => {
                console.error('Failed to get PasteData. Cause: ' + err.message);
              })
          })
        }
      }
    }
  }
}
```

#### getChangeCount18+

getChangeCount(): number

获取剪贴板内容的变化次数。

执行成功时返回剪贴板内容的变化次数，否则返回0。

当剪贴板内容过期或调用[clearDataSync](#ZH-CN_TOPIC_0000002497445528__cleardatasync11)等接口导致剪贴板内容为空时，内容变化次数不会因此改变。

系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被视作多次更改，每次复制均会导致内容变化次数增加。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

类型说明number返回读取到的剪贴板内容变化次数。

**示例：**

```ets
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result : number = systemPasteboard.getChangeCount();
    console.info(`Succeeded in getting the ChangeCount. Result: ${result}`);
} catch (err) {
    console.error(`Failed to get the ChangeCount. Cause: ${err.message}`);
};
```

#### UpdateCallback 22+

type UpdateCallback = () => void

表示剪贴板内容变更的回调

**系统能力：** SystemCapability.MiscServices.Pasteboard

#### onRemoteUpdate(callback: UpdateCallback)22+

onRemoteUpdate(callback: UpdateCallback): void

订阅跨设备剪贴板内容变化事件，当远端设备系统剪贴板中内容变化时触发用户程序的回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callback[UpdateCallback](#ZH-CN_TOPIC_0000002497445528__updatecallback-22)是剪贴板中内容变化时触发的用户程序的回调。

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.onRemoteUpdate(listener);
```

#### offRemoteUpdate(callback?: UpdateCallback)22+

offRemoteUpdate(callback?: UpdateCallback): void

取消订阅跨设备剪贴板内容变化事件。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

参数名类型必填说明callback[UpdateCallback](#ZH-CN_TOPIC_0000002497445528__updatecallback-22)否远端设备剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有远端监听回调，否则表示清除指定远端监听回调。

**示例：**

```ets
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.offRemoteUpdate(listener);
```