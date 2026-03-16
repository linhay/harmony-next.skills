# @ohos.file.picker (选择器)

该模块接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

选择器(Picker)是一个封装DocumentViewPicker、AudioViewPicker、PhotoViewPicker的API模块，具有选择与保存的能力。应用可以选择使用以下API来实现文件的选择和保存的功能。该类接口，需要应用在界面UIAbility中调用，否则无法拉起FilePicker应用、AudioPicker应用或PhotoPicker应用。

调用本模块接口返回的URI数组，URI中的中文及非数字字母的特殊字符会被编码为对应的ASCII码并拼接到URI中。

#### 导入模块

```ets
import  { picker } from '@kit.CoreFileKit';
```

#### DocumentViewPicker

文件选择器对象，用来支撑选择和保存各种格式文档。在使用前，需要先创建DocumentViewPicker实例。

**系统能力**：SystemCapability.FileManagement.UserFileService

#### constructor12+

constructor(context: Context)

创建DocumentViewPicker对象，推荐使用该构造函数，获取context参考[getHostContext](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__gethostcontext12)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明contextContext是应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
            let documentPicker = new picker.DocumentViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### constructor12+

constructor()

创建DocumentViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**示例：**

```ets
let documentPicker = new picker.DocumentViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

#### constructor13+

constructor(context: Context, window: window.Window)

应用自行创建窗口中，可用通过该构造函数创建DocumentViewPicker对象。一般场景推荐使用constructor(context: Context)方法创建DocumentViewPicker对象。

从API version 19开始，2in1和Tablet设备支持该方法。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明contextContext是应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)。window[window.Window](../../types/interfaces/Interface (Window).md)是应用创建的窗口实例。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
import { window } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
            let windowClass: window.Window | undefined = undefined;
            windowClass = window.findWindow('test'); // 请确保window已创建，此处的'test'为window创建时的name参数
            let documentPicker = new picker.DocumentViewPicker(context, windowClass);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### select

select(option?: DocumentSelectOptions): Promise<Array<string>>

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。接口采用Promise异步返回形式，传入可选参数DocumentSelectOptions对象，返回选择文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[DocumentSelectOptions](#ZH-CN_TOPIC_0000002497445278__documentselectoptions)否documentPicker选择选项。若无此参数，则默认拉起documentPicker主界面。

**返回值：**

类型说明Promise<Array<string>>

Promise对象。返回documentPicker选择后的结果集。

**注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example07(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### select

select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。接口采用callback异步返回形式，传入参数DocumentSelectOptions对象，返回选择文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[DocumentSelectOptions](#ZH-CN_TOPIC_0000002497445278__documentselectoptions)是documentPicker选择选项。callbackAsyncCallback<Array<string>>是

callback 返回documentPicker选择后的结果集。

**注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example08(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions, (err: BusinessError, documentSelectResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### select

select(callback: AsyncCallback<Array<string>>): void

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。接口采用callback异步返回形式，返回选择文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是

callback 返回documentPicker选择后的结果集。

**注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example09(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select((err: BusinessError, documentSelectResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### save

save(option?: DocumentSaveOptions): Promise<Array<string>>

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。接口采用Promise异步返回形式，传入可选参数DocumentSaveOptions对象，返回保存文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[DocumentSaveOptions](#ZH-CN_TOPIC_0000002497445278__documentsaveoptions)否documentPicker保存选项。若无此参数，则拉起documentPicker界面后需用户自行输入保存的文件名。

**返回值：**

类型说明Promise<Array<string>>

Promise对象。返回documentPicker保存后的结果集。

**注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example10(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = ['DocumentViewPicker01.txt'];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    }).catch((err: BusinessError) => {
      console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### save

save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。接口采用callback异步返回形式，传入参数DocumentSaveOptions对象，返回保存文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[DocumentSaveOptions](#ZH-CN_TOPIC_0000002497445278__documentsaveoptions)是documentPicker保存选项。callbackAsyncCallback<Array<string>>是

callback 返回documentPicker保存后的结果集。

**注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example11(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = ['DocumentViewPicker02.txt'];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions, (err: BusinessError, documentSaveResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### save

save(callback: AsyncCallback<Array<string>>): void

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。接口采用callback异步返回形式，返回保存文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是

callback 返回documentPicker保存后的结果集。

**注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example12(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save((err: BusinessError, documentSaveResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### getSelectedIndex14+

getSelectedIndex(): number

获取保存成功后的文件后缀类型的下标。

该方法只在调用 [save()](#ZH-CN_TOPIC_0000002497445278__save)时使用生效，其他场景下不适用。

该方法需要配置参数[DocumentSaveOptions.fileSuffixChoices](#ZH-CN_TOPIC_0000002497445278__documentsaveoptions)。

该方法返回的是所选后缀类型的下标(number)。所选的后缀类型是开发者所传的参数[DocumentSaveOptions.fileSuffixChoices](#ZH-CN_TOPIC_0000002497445278__documentsaveoptions)里的某个后缀类型。如果没有传参，并且调用了getSelectedIndex()方法，返回值为-1。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection

**返回值：**

类型说明number返回所选后缀类型在[DocumentSaveOptions.fileSuffixChoices](#ZH-CN_TOPIC_0000002497445278__documentsaveoptions)里的下标(number)。默认返回-1。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function exampleIndex(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    //保存文件的名字
    documentSaveOptions.newFileNames = ['DocumentViewPicker01'];
    //保存文件的后缀类型
    documentSaveOptions.fileSuffixChoices = ['txt', 'mp4', 'pdf'];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
      if (documentSaveOptions.fileSuffixChoices != undefined && documentSaveResult != undefined) {
        //获取保存文件的后缀类型的下标
        let index = documentPicker.getSelectedIndex();
        //获取保存文件的后缀类型。
        let selectedsuffix = documentSaveOptions.fileSuffixChoices[index];
        console.info ('DocumentViewPicker.save selectedsuffix is ' + selectedsuffix);
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    }).catch((err: BusinessError) => {
      console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### AudioViewPicker

音频选择器对象，用来支撑选择和保存音频类文件等用户场景。在使用前，需要先创建AudioViewPicker实例。

**系统能力**：SystemCapability.FileManagement.UserFileService

#### constructor12+

constructor(context: Context)

创建AudioViewPicker对象，推荐使用该构造函数，获取context参考[getHostContext](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__gethostcontext12)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明contextContext是应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
            let audioPicker = new picker.AudioViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### constructor12+

constructor()

创建AudioViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**示例：**

```ets
let audioPicker = new picker.AudioViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

#### select

select(option?: AudioSelectOptions): Promise<Array<string>>

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。接口采用Promise异步返回形式，传入可选参数AudioSelectOptions对象，返回选择音频文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[AudioSelectOptions](#ZH-CN_TOPIC_0000002497445278__audioselectoptions)否audioPicker音频选择选项。若无此参数，则默认拉起audioPicker主界面。

**返回值：**

类型说明Promise<Array<string>>

Promise对象。返回audioPicker选择音频后的结果集。

**注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[媒体类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri介绍)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example13(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSelectOptions = new picker.AudioSelectOptions();
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### select

select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。接口采用callback异步返回形式，传入参数AudioSelectOptions对象，返回选择音频文件的URI数组。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[AudioSelectOptions](#ZH-CN_TOPIC_0000002497445278__audioselectoptions)是audioPicker音频选择选项。callbackAsyncCallback<Array<string>>是

callback 返回audioPicker选择音频后的结果集。

**注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[媒体类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri介绍)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example14(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSelectOptions = new picker.AudioSelectOptions();
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions, (err: BusinessError, audioSelectResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### select

select(callback: AsyncCallback<Array<string>>): void

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。接口采用callback异步返回形式，返回选择音频文件的URI数组。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是

callback 返回audioPicker选择音频后的结果集。

**注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[媒体类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri介绍)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example15(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select((err: BusinessError, audioSelectResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### save

save(option?: AudioSaveOptions): Promise<Array<string>>

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中），用户可以保存一个或多个音频文件。接口采用Promise异步返回形式，传入可选参数AudioSaveOptions对象，返回保存音频文件的URI数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[AudioSaveOptions](#ZH-CN_TOPIC_0000002497445278__audiosaveoptions)否audioPicker保存音频文件选项。若无此参数，则拉起audioPicker界面后需用户自行输入保存的文件名。

**返回值：**

类型说明Promise<Array<string>>

Promise对象。返回audioPicker保存音频文件后的结果集。

**注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example16(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSaveOptions = new picker.AudioSaveOptions();
    audioSaveOptions.newFileNames = ['AudioViewPicker01.mp3'];
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions).then((audioSaveResult: Array<string>) => {
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult))
    }).catch((err: BusinessError) => {
      console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### save

save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中），用户可以保存一个或多个音频文件。接口采用callback异步返回形式，传入参数AudioSaveOptions对象，返回保存音频文件的URI数组。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[AudioSaveOptions](#ZH-CN_TOPIC_0000002497445278__audiosaveoptions)是audioPicker保存音频文件选项。callbackAsyncCallback<Array<string>>是

callback 返回audioPicker保存音频文件后的结果集。

**注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example17(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSaveOptions = new picker.AudioSaveOptions();
    audioSaveOptions.newFileNames = ['AudioViewPicker02.mp3'];
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions, (err: BusinessError, audioSaveResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### save

save(callback: AsyncCallback<Array<string>>): void

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中），用户可以保存一个或多个音频文件。接口采用callback异步返回形式，返回保存音频文件的URI数组。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是

callback 返回audioPicker保存音频文件后的结果集。

**注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example18(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save((err: BusinessError, audioSaveResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
        console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

#### DocumentSelectMode11+

枚举，picker选择的文档类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection

名称值说明FILE0文件类型（默认类型）。FOLDER1文件夹类型。MIXED2文件和文件夹混合类型。

#### DocumentSelectOptions

文档选择选项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称类型只读可选说明maxSelectNumber10+number否是

选择文件最大个数。

API version 20及之前的版本，单次选择最大文件个数上限为500个，默认值是500。选择目录仅对具有该系统能力的设备开放，且目录选择的最大个数为1。

API version 21及之后的版本取消限制。受系统能力限制，选择文件数量过大可能会出现功能异常或处理性能较差等情况，建议单次选择文件个数不超过1万个。

**系统能力**：SystemCapability.FileManagement.UserFileService

defaultFilePathUri10+string否是指定选择的文件或者目录的URI。默认为空（效果为拉起最近打开页）。fileSuffixFilters10+Array<string>否是

选择文件的后缀类型。传入字符串数组，每一项代表一个后缀选项，每一项内部用"|"分为两部分，第一部分为描述，第二部分为过滤后缀。没有"|"则没有描述，该项整体是一个过滤后缀。每项过滤后缀可以存在多个后缀名，则每一个后缀名之间用英文逗号进行分隔，传入数组长度不能超过100，例如：['图片(.png, .jpg)|.png,.jpg', '文档|.txt', '视频|.mp4', '.pdf']。

默认不过滤，即显示所有文件。此外2in1设备支持通配符方式['所有文件(*.*)|.*']（说明：从API version 17开始，手机支持该配置），表示为显示所有文件。

仅对具有该系统能力的设备开放。**系统能力**：SystemCapability.FileManagement.UserFileService

selectMode11+[DocumentSelectMode](#ZH-CN_TOPIC_0000002497445278__documentselectmode11)否是

Picker选择的文档类型，默认值是FILE(文件类型)。

**系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection

authMode12+boolean否是

拉起授权Picker，默认为false（非授权模式）。当authMode为true时为授权模式，defaultFilePathUri必填，表明待授权URI。

**设备行为差异**：该参数在2in1设备中可正常使用，在其他设备中无效果。

**系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection

multiAuthMode15+boolean否是

支持批量授权模式，默认为false（非批量授权模式）。当multiAuthMode为true时为批量授权模式。当multiAuthMode为true时，只有multiUriArray参数生效，其他参数不生效。

**设备行为差异**：该参数在Phone设备中可正常使用，在其他设备中无效果。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

multiUriArray15+Array<string>否是

传入需要批量授权的URI数组（仅支持文件，文件夹不生效）。配合multiAuthMode使用。当multiAuthMode为false时，配置该参数不生效。默认为空（效果为拉起批量授权页面后展示的文件为空）。

**设备行为差异**：该参数在Phone设备中可正常使用，在其他设备中无效果。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

mergeMode15+[MergeTypeMode](#ZH-CN_TOPIC_0000002497445278__mergetypemode15)否是

开启聚合视图模式，支持拉起文件管理应用的聚合视图。默认为DEFAULT，表示该参数不生效，非聚合视图。当该参数置为非DEFAULT时，其他参数不生效。

API version 22及之后的版本当该参数置为非DEFAULT时，仅fileSuffixFilters参数生效，其他参数不生效。

**设备行为差异**：该参数在Phone设备中可正常使用，在其他设备中无效果。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

isEncryptionSupported19+boolean否是

是否支持加密（仅支持文件，文件夹不生效），默认为false。该参数为true时，在Picker界面可以选择对文件进行加密。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

#### DocumentPickerMode12+

枚举，picker保存的模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称值说明DEFAULT0标准模式。DOWNLOAD1

下载模式。

**注意**： DOWNLOAD模式创建的目录仅用于保存文件，目录之间无访问隔离，不建议保存应用敏感数据。

#### MergeTypeMode15+

枚举，文件聚合类型。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**设备行为差异**：该接口在Phone设备中可正常调用，在其他设备中无效果。

名称值说明DEFAULT0默认模式，表示该参数不生效。AUDIO1音频文件模式。VIDEO2视频文件模式。DOCUMENT3文档文件模式。PICTURE4图片文件模式。

#### DocumentSaveOptions

文档保存选项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称类型只读可选说明newFileNamesArray<string>否是拉起documentPicker进行保存的文件名。若无此参数，则默认需要用户自行输入。defaultFilePathUri10+string否是指定保存的文件或者目录的URI。默认为空。fileSuffixChoices10+Array<string>否是保存文件的后缀类型。传入字符串数组，每一项代表一个后缀选项，每一项内部用"|"分为两部分，第一部分为描述，第二部分为要保存的后缀。没有"|"则没有描述，该项整体是一个保存的后缀。默认没有后缀类型。pickerMode12+[DocumentPickerMode](#ZH-CN_TOPIC_0000002497445278__documentpickermode12)否是拉起picker的类型, 默认为DEFAULT。当pickerMode设置为DOWNLOAD时，用户配置的参数newFileNames、defaultFilePathUri和fileSuffixChoices将不会生效。

#### AudioSelectOptions

音频选择选项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称类型只读可选说明maxSelectNumber12+number否是选择文件最大个数，默认值为1，上限为500个，有效值范围1-500。

#### AudioSaveOptions

音频保存选项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称类型只读可选说明newFileNamesArray<string>否是拉起audioPicker进行保存音频资源的文件名。若无此参数，则默认需要用户自行输入。

#### PhotoViewPicker(deprecated)

图库选择器对象，用来支撑选择图片/视频和保存图片/视频等用户场景。选择文件推荐使用[PhotoAccessHelper的PhotoViewPicker](../../types/classes/Class (PhotoViewPicker).md)。在使用前，需要先创建PhotoViewPicker实例。

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker](../../types/classes/Class (PhotoViewPicker).md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

#### constructor(deprecated)

constructor(context: Context)

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明contextContext是应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)。

创建PhotoViewPicker对象，推荐使用该构造函数，获取context参考[getHostContext](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__gethostcontext12)。

从API version 12开始支持，从API version 18开始废弃。建议使用[photoAccessHelper.PhotoViewPicker](../../types/classes/Class (PhotoViewPicker).md)替代。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
            let photoPicker = new picker.PhotoViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### constructor(deprecated)

constructor()

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

创建PhotoViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

从API version 12开始支持，从API version 18开始废弃。建议使用[photoAccessHelper.PhotoViewPicker](../../types/classes/Class (PhotoViewPicker).md)替代。

**示例：**

```ets
let photoPicker = new picker.PhotoViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

#### select(deprecated)

select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用Promise异步返回形式，传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker#select](../../types/classes/Class (PhotoViewPicker).md#ZH-CN_TOPIC_0000002529445913__select)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[PhotoSelectOptions](#ZH-CN_TOPIC_0000002497445278__photoselectoptionsdeprecated)否photoPicker选择选项。若无此参数，则默认选择媒体文件类型为图片和视频类型。选择媒体文件数量的默认最大值为50。

**返回值：**

类型说明Promise<[PhotoSelectResult](#ZH-CN_TOPIC_0000002497445278__photoselectresultdeprecated)>

Promise对象。返回photoPicker选择后的结果集。

**注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用[photoAccessHelper.getAssets接口](../../types/interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用，具体使用方式参见用户文件uri介绍中的[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example01(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions).then((photoSelectResult: picker.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    }).catch((err: BusinessError) => {
      console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

#### select(deprecated)

select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker#select](../../types/classes/Class (PhotoViewPicker).md#ZH-CN_TOPIC_0000002529445913__select-1)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[PhotoSelectOptions](#ZH-CN_TOPIC_0000002497445278__photoselectoptionsdeprecated)是photoPicker选择选项。callbackAsyncCallback<[PhotoSelectResult](#ZH-CN_TOPIC_0000002497445278__photoselectresultdeprecated)>是

callback 返回photoPicker选择后的结果集。

**注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用[photoAccessHelper.getAssets接口](../../types/interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用，具体使用方式参见用户文件uri介绍中的[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example02(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

#### select(deprecated)

select(callback: AsyncCallback<PhotoSelectResult>): void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，返回PhotoSelectResult对象。

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker#select](../../types/classes/Class (PhotoViewPicker).md#ZH-CN_TOPIC_0000002529445913__select-2)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明callbackAsyncCallback<[PhotoSelectResult](#ZH-CN_TOPIC_0000002497445278__photoselectresultdeprecated)>是

callback 返回photoPicker选择后的结果集。

**注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用[photoAccessHelper.getAssets接口](../../types/interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用，具体使用方式参见用户文件uri介绍中的[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example03(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select((err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

#### save(deprecated)

save(option?: PhotoSaveOptions): Promise<Array<string>>

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用Promise异步返回形式，传入可选参数PhotoSaveOptions对象，返回保存文件的uri数组。

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButton](../../topics/components/SaveButton.md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[PhotoSaveOptions](#ZH-CN_TOPIC_0000002497445278__photosaveoptionsdeprecated)否photoPicker保存图片或视频文件选项。若无此参数，则拉起photoPicker界面后需用户自行输入保存的文件名。

**返回值：**

类型说明Promise<Array<string>>

Promise对象。返回photoPicker保存图片或视频文件后的结果集。

**注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example04(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = ['PhotoViewPicker01.jpg', 'PhotoViewPicker01.mp4'];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions).then((photoSaveResult: Array<string>) => {
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    }).catch((err: BusinessError) => {
      console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
      console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

#### save(deprecated)

save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSaveOptions对象，返回保存文件的uri数组。

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButton](../../topics/components/SaveButton.md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明option[PhotoSaveOptions](#ZH-CN_TOPIC_0000002497445278__photosaveoptionsdeprecated)是photoPicker保存图片或视频文件选项。callbackAsyncCallback<Array<string>>是

callback 返回photoPicker保存图片或视频文件后的结果集。

**注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example05(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = ['PhotoViewPicker02.jpg','PhotoViewPicker02.mp4'];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions, (err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

#### save(deprecated)

save(callback: AsyncCallback<Array<string>>): void

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式，返回保存文件的uri数组。

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButton](../../topics/components/SaveButton.md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是

callback 返回photoPicker保存图片或视频文件后的结果集。

**注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的[文档类uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri的使用方式)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example06(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save((err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

#### PhotoViewMIMETypes(deprecated)

枚举，可选择的媒体文件类型。

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewMIMETypes](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称值说明IMAGE_TYPE'image/*'

图片类型。

**说明**：从API version 9开始支持，从API version 18开始废弃。

VIDEO_TYPE'video/*'

视频类型。

**说明**：从API version 9开始支持，从API version 18开始废弃。

IMAGE_VIDEO_TYPE'*/*'

图片和视频类型。

**说明**：从API version 9开始支持，从API version 18开始废弃。

#### PhotoSelectOptions(deprecated)

图库选择选项。

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoSelectOptions](../../types/classes/Classes (其他).md#ZH-CN_TOPIC_0000002497605950__photoselectoptions)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称类型只读可选说明MIMEType[PhotoViewMIMETypes](#ZH-CN_TOPIC_0000002497445278__photoviewmimetypesdeprecated)否是

可选择的媒体文件类型。若无此参数，则默认为图片和视频类型。

**说明**：从API version 9开始支持，从API version 18开始废弃。

maxSelectNumbernumber否是

选择媒体文件数量的最大值，默认值为50，最大值为500。

**说明**：从API version 9开始支持，从API version 18开始废弃。

#### PhotoSelectResult(deprecated)

返回图库选择后的结果集。

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoSelectResult](../../types/classes/Classes (其他).md#ZH-CN_TOPIC_0000002497605950__photoselectresult)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称类型只读可选说明photoUrisArray<string>否否

返回图库选择后的媒体文件的uri数组。此uri数组只能通过临时授权的方式调用[photoAccessHelper.getAssets接口](../../types/interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用，具体使用方式参见用户文件uri介绍中的[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**说明**：从API version 9开始支持，从API version 18开始废弃。

isOriginalPhotoboolean否否

返回图库选择后的媒体文件是否为原图。true为原图；false不是原图。

**说明**：从API version 9开始支持，从API version 18开始废弃。

#### PhotoSaveOptions(deprecated)

图片或视频的保存选项。

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButtonOptions](../../topics/components/SaveButton.md#ZH-CN_TOPIC_0000002497604940__savebuttonoptions)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

名称类型只读可选说明newFileNamesArray<string>否是

拉起photoPicker进行保存图片或视频资源的文件名。若无此参数，则默认需要用户自行输入。

**说明**：从API version 9开始支持，从API version 18开始废弃。