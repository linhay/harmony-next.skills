# fileManagerService

fileManagerService模块提供删除文件到回收站及获取文件图标的能力。

**起始版本：**5.0.5(17)

#### 导入模块

```ets
import { fileManagerService } from '@kit.FileManagerServiceKit';
```

#### fileManagerService.deleteToTrash

deleteToTrash(uri: string): Promise<string>

以异步方法删除文件到回收站，返回删除后路径。使用Promise异步回调。

**注意**：此接口参数uri的具体使用方式参见用户文件uri介绍中的[文档类URI的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#文档类uri)。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：**5.0.5(17)

**参数：**

参数名

类型

必填

说明

uri

string

是

待删除文件的uri

**返回值：**

类型

说明

Promise<string>

文件删除到回收站后的uri。使用Promise异步回调。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1014000001

Operation not permitted.

1014000002

No such file or directory.

1014000003

No space left on device.

1014000004

System inner fail.

**示例代码：**

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
}
```

#### fileManagerService.getFileIconSync

getFileIconSync(fileType: string): string | Resource

根据文件类型获取文件图标。

**需要权限**：ohos.permission.GET_FILE_ICON

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：**5.0.5(17)

**参数：**

参数名

类型

必填

说明

fileType

string

是

文件类型对应的UTD-ID，详见[图标格式说明](图标格式说明.md)

**返回值：**

类型

说明

string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)

文件图标的Base64编码或资源对象

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

1014000004

System inner fail.

**示例代码：**

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
    }
    .height('100%')
    .width('100%')
  }
}
```

#### fileManagerService.getFileIcon

getFileIcon(fileType: string): Promise<string | Resource>

根据文件类型获取文件图标。使用Promise异步回调。

**需要权限**：ohos.permission.GET_FILE_ICON

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：**5.0.5(17)

**参数：**

参数名

类型

必填

说明

fileType

string

是

文件类型对应的UTD-ID，详见[图标格式说明](图标格式说明.md)

**返回值：**

类型

说明

Promise<string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)>

文件图标的Base64编码或资源对象。使用Promise异步回调。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

1014000004

System inner fail.

**示例代码：**

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
    }
    .height('100%')
    .width('100%')
  }
}
```