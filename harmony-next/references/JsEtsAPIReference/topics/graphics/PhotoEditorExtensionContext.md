# PhotoEditorExtensionContext

PhotoEditorExtensionContext是PhotoEditorExtensionAbility的上下文，继承自ExtensionContext，提供PhotoEditorExtensionAbility的相关配置信息以及保存图片接口。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

#### 导入模块

```ets
import { common } from '@kit.AbilityKit';
```

#### PhotoEditorExtensionContext.saveEditedContentWithUri

saveEditedContentWithUri(uri: string): Promise<AbilityResult>

传入编辑过的图片的uri并保存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

参数名类型必填说明uristring是编辑后图片的[uri](../../modules/ohos/@ohos.file.fileuri (文件URI).md)，格式为file://<bundleName>/<sandboxPath>。

**返回值：**

类型说明Promise<AbilityResult>Promise对象，返回AbilityResult对象，编辑过的图片uri存在want.uri中，[uri](../../modules/ohos/@ohos.file.fileuri (文件URI).md)格式为file://<bundleName>/<sandboxPath>。

**错误码：**

以下错误码详细介绍参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.29600001Internal error.29600002Image input error.29600003Image too big.

**示例：**

```ets
import { common, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG = '[ExamplePhotoEditorAbility]';

@Entry
@Component
struct Index {
  // 原始图片
  @State originalImage: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Button('RotateAndSaveImg').onClick(event => {
          hilog.info(0x0000, TAG, `Start to edit image and save.`);

          this.originalImage?.rotate(90).then(() => {
            const imagePackerApi: image.ImagePacker = image.createImagePacker();
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
            imagePackerApi.packToData(this.originalImage, packOpts).then((data: ArrayBuffer) => {
              let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
              let filePath = context.filesDir + '/edited.jpg';
              let file: fileIo.File | undefined;
              try{
                file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE
                | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
                let writeLen = fileIo.writeSync(file.fd, data);
                hilog.info(0x0000, TAG, 'write data to file succeed and size is:'
                  + writeLen);
                fileIo.closeSync(file);
                context.saveEditedContentWithUri(filePath).then
                  (data => {
                    hilog.info(0x0000, TAG,
                      `saveContentEditingWithUri result: ${JSON.stringify(data)}`);
                  });
              } catch (e) {
                hilog.info(0x0000, TAG, `writeImage failed:${e}`);
              } finally {
                fileIo.close(file);
              }
            }).catch((error: BusinessError) => {
              hilog.error(0x0000, TAG,
                'Failed to pack the image. And the error is: ' + String(error));
            })
          })
        }).margin({ top: 10 })
      }
    }
  }
}
```

#### PhotoEditorExtensionContext.saveEditedContentWithImage

saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>

传入编辑过的图片的PixMap对象并保存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

参数名类型必填说明pixeMap[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)是编辑过的图片image.PixelMap。option[image.PackingOption](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__packingoption)是设置打包参数。

**返回值：**

类型说明Promise<AbilityResult>Promise对象，返回AbilityResult对象，编辑过的图片uri存在want.uri中，[uri](../../modules/ohos/@ohos.file.fileuri (文件URI).md)格式为file://<bundleName>/<sandboxPath>。

**错误码：**

以下错误码详细介绍参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.29600001Internal error.29600002Image input error.29600003Image too big.

**示例：**

```ets
import { common, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { image } from '@kit.ImageKit';

const TAG = '[ExamplePhotoEditorAbility]';

@Entry
@Component
struct Index {
  // 原始图片
  @State originalImage: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Button('RotateAndSaveImg').onClick(event => {
          hilog.info(0x0000, TAG, `Start to edit image and save.`);

          this.originalImage?.rotate(90).then(() => {
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
            try {
              let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
              context.saveEditedContentWithImage(this.originalImage as image.PixelMap,
                packOpts).then(data => {
                  hilog.info(0x0000, TAG,
                    `saveContentEditingWithImage result: ${JSON.stringify(data)}`);
                });
            } catch (e) {
              hilog.error(0x0000, TAG, `saveContentEditingWithImage failed:${e}`);
              return;
            }
          })
        }).margin({ top: 10 })
      }
    }
  }
}
```