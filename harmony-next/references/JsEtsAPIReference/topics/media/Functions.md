# Functions

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

**photoAccessHelper.getPhotoAccessHelper**

getPhotoAccessHelper(context: Context): PhotoAccessHelper

获取相册管理模块的实例，用于访问和修改相册中的媒体文件。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入Ability实例的上下文。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| PhotoAccessHelper | 相册管理模块的实例。 |

错误码：

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

示例：

```ets
// 此处获取的phAccessHelper实例为全局对象，后续使用到phAccessHelper的地方默认为使用此处获取的对象，如未添加此段代码报phAccessHelper未定义的错误请自行添加。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button("example").onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      }).width('100%')
    }
    .height('90%')
  }
```