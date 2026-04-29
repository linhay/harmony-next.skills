# fileManagerService

fileManagerService模块提供删除文件到回收站、获取文件图标及解析文件快捷方式的能力。

起始版本： 5.0.5(17)

**导入模块**

```ets
import { fileManagerService } from '@kit.FileManagerServiceKit';
```

**fileManagerService.deleteToTrash**

deleteToTrash(uri: string): Promise<string>

以异步方法删除文件到回收站，返回删除后路径。使用Promise异步回调。

   ![image](public_sys-resources/caution_3.0-zh-cn.webp)

此接口参数uri的具体使用方式参见用户文件uri介绍中的[文档类URI的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri)。

系统能力：SystemCapability.FileManagement.FileManagerService.Core

起始版本： 5.0.5(17)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待删除文件的uri |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 文件删除到回收站后的uri。使用Promise异步回调。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1014000001 | Operation not permitted. |
| 1014000002 | No such file or directory. |
| 1014000003 | No space left on device. |
| 1014000004 | System inner fail. |

示例代码：

```ets
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function deleteFile() {
  // 以内置存储目录为例
  // 示例代码targetUri表示Download目录下文件
  // 开发者应根据自己实际获取的uri进行开发，并确保对该文件有读写权限
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  try {
    let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
    console.info("trashUri: " + trashUri);
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
```

**fileManagerService.getFileIconSync**

getFileIconSync(fileType: string): string | Resource

根据文件类型获取文件图标。

需要权限：ohos.permission.GET_FILE_ICON

系统能力：SystemCapability.FileManagement.FileManagerService.Core

起始版本： 5.0.5(17)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileType | string | 是 | 文件类型对应的UTD-ID，详见图标格式说明 |

返回值：

| 类型 | 说明 |
| --- | --- |
| string | Resource | 文件图标的Base64编码或资源对象 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 1014000004 | System inner fail. |

示例代码：

```ets
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      this.fileIcon = fileManagerService.getFileIconSync(typeId);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // 以txt格式为例
            this.getFileIconByFileExtension('.txt');
          })
      }
    .height('100%')
    .width('100%')
  }
```

**fileManagerService.getFileIcon**

getFileIcon(fileType: string): Promise<string | Resource>

根据文件类型获取文件图标。使用Promise异步回调。

需要权限：ohos.permission.GET_FILE_ICON

系统能力：SystemCapability.FileManagement.FileManagerService.Core

起始版本： 5.0.5(17)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileType | string | 是 | 文件类型对应的UTD-ID，详见图标格式说明 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string | Resource> | 文件图标的Base64编码或资源对象。使用Promise异步回调。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 1014000004 | System inner fail. |

示例代码：

```ets
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      console.info('getFileIconByFileExtension');
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      fileManagerService.getFileIcon(typeId).then((retIcon: string | Resource) => {
        this.fileIcon = retIcon;
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // 以txt格式为例
            this.getFileIconByFileExtension('.txt');
          })
      }
    .height('100%')
    .width('100%')
  }
```

**fileManagerService.parseShortcut**

parseShortcut(linkUri: string): Promise<string>

根据快捷方式文件的URI解析出对应原文件的URI。使用Promise异步回调。

系统能力：SystemCapability.FileManagement.FileManagerService.Core

起始版本：6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| linkUri | string | 是 | 快捷方式文件的URI，调用方对该文件需要有读权限。具体使用方式参见用户文件URI介绍中的文档类URI的使用方式，快捷方式文件URI的后缀必须为“.hlink”。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 对应原文件的URI。使用Promise异步回调。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1014000002 | No such file or directory. |
| 1014000005 | Invalid shortcut file. |

示例代码：

```ets
import fileManagerService from '@hms.filemanagement.fileManagerService';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State linkUri: string = '';
  @State parseResult: string = '';
  private scroller: Scroller = new Scroller();

  build() {
    Stack() {
      Column() {
        List({ scroller: this.scroller }) {
          ListItem() {
            Column() {
              Text("解析快捷方式")
                .fontSize('30fp')
                .fontWeight(FontWeight.Bold)
                .margin({ top: 20 })
                .alignRules({
                  center: { anchor: '__container__', align: VerticalAlign.Center },
                  middle: { anchor: '__container__', align: HorizontalAlign.Center }
                })
              TextInput({
                placeholder: '请输入要解析快捷方式URI（例如：file://docs/storage/Users/currentUser/Documents/1.jpg.hlink）'
              })
                .width('90%')
                .margin({ top: 20 })
                .alignRules({
                  center: { anchor: '__container__', align: VerticalAlign.Center },
                  middle: { anchor: '__container__', align: HorizontalAlign.Center }
                })
                .onChange((value: string) => {
                  this.linkUri = value;
                })
              Button("解析快捷方式", { type: ButtonType.Normal })
                .backgroundColor(0x317aff)
                .width('90%')
                .height(40)
                .margin({ top: 20 })
                .onClick(async () => {
                  const linkUri: string = this.linkUri;
                  let targetUri: string = '';
                  try {
                    targetUri = await fileManagerService.parseShortcut(linkUri);
                    console.info('parseShortcut success, linkUri:' + linkUri + ', targetUri:' + targetUri);
                    this.parseResult = '解析快捷方式成功，目标原文件URI：' + targetUri;
                  } catch (err) {
                    let error: BusinessError = err as BusinessError;
                    console.error('parseShortcut failed, errCode:' + error.code + ', errMessage:' + error.message);
                    this.parseResult = 'errCode:' + error.code + ', errMessage:' + error.message;
                  }
                })
              Row() {
                Text('解析结果：')
                  .textAlign(TextAlign.Start)
                  .margin({ top: 20 })
                  .fontSize('25fp')
                Text(this.parseResult)
                  .textAlign(TextAlign.Start)
                  .margin({ top: 20 })
                  .fontSize('25fp')
              }
          .width('100%')
        }
        .height('100%')
        .width('100%')
        .padding({left: 10, right: 10})
      }
    .align(Alignment.BottomEnd)
  }
```