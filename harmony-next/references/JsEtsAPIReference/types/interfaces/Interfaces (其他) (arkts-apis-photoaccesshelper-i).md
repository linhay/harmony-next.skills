[]()[]()

# Interfaces (其他)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

[]()[]()

#### MediaChangeRequest11+

媒体变更请求，资产变更请求和相册变更请求的父类型。

媒体变更请求必须在调用[applyChanges](Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__applychanges11)后才会生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

[]()[]()

#### CreateOptions

图片或视频的创建选项。

title参数的规格如下：

- 不应包含扩展名。
- 文件名字符串长度为1~255。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明titlestring否是

图片或者视频的标题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

subtype12+[PhotoSubtype](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__photosubtype12)否是

图片或者视频的文件子类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### FetchOptions

检索条件。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明fetchColumnsArray<string>否否

检索条件，指定列名查询。

对于照片，如果该参数为空，默认查询'uri'、'media_type'、'subtype'和'display_name'，使用[get](Interface (PhotoAsset).md#ZH-CN_TOPIC_0000002497605954__get)接口获取当前对象的其他属性时将会报错。示例：fetchColumns: ['uri', 'title']。

对于相册，如果该参数为空，默认查询'uri'和'album_name'。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

predicates[dataSharePredicates.DataSharePredicates](../../modules/ohos/@ohos.data.dataSharePredicates (数据共享谓词).md#ZH-CN_TOPIC_0000002529444645__datasharepredicates)否否

谓词查询，显示过滤条件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### RequestOptions11+

请求策略。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明deliveryMode[DeliveryMode](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__deliverymode11)否否请求资源分发模式，可以指定对于该资源的请求策略，可被配置为快速模式，高质量模式，均衡模式三种策略。compatibleMode15+[CompatibleMode](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__compatiblemode15)否是配置HDR视频资源转码模式，可指定配置为转码和不转码两种策略。默认为原视频资源内容模式即不转码。mediaAssetProgressHandler15+[MediaAssetProgressHandler](Interface (MediaAssetProgressHandler).md)否是配置HDR视频转码为SDR视频时的进度级回调。[]()[]()

#### ChangeData

监听器回调函数的返回值。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明type[NotifyType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__notifytype)否否ChangeData的通知类型。urisArray<string>否否相同[NotifyType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__notifytype)的所有uri，可以是PhotoAsset或Album。extraUrisArray<string>否否相册中变动文件的uri数组。可能为undefined，使用前需要检查是否为undefined。[]()[]()

#### TextContextInfo12+

文本信息，用于推荐图片的文本信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明textstring否是如果需要根据文本（支持250字以内的简体中文）推荐相应的图片，则配置此参数。text默认是空字符串。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let textInfo: photoAccessHelper.TextContextInfo = {
      text: '上海野生动物园的大熊猫'
    }
    let recommendOptions: photoAccessHelper.RecommendationOptions = {
      textContextInfo: textInfo
    }
    let options: photoAccessHelper.PhotoSelectOptions = {
      MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
      maxSelectNumber: 1,
      recommendationOptions: recommendOptions
    }
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(options).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```

[]()[]()

#### PhotoCreationConfig12+

保存图片/视频到媒体库的配置，包括保存的文件名等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明titlestring否是

图片或者视频的标题，不传入时由系统生成。参数规格为：

- 不应包含扩展名。

- 文件名字符串长度为1~255（资产文件名为标题+扩展名）。

- 不允许出现的非法英文字符，包括：. \ / : * ? " ' ` < > | { } [ ]

fileNameExtensionstring否否文件扩展名，例如'jpg'。photoType[PhotoType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__phototype)否否创建的文件类型[PhotoType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__phototype)，IMAGE或者VIDEO。subtype[PhotoSubtype](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__photosubtype12)否是图片或者视频的文件子类型[PhotoSubtype](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__photosubtype12)，不传入时默认为DEFAULT。[]()[]()

#### PhotoAssetChangeInfo20+

媒体资产（图片/视频）信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明uristring否否媒体文件资源uri。mediaType[PhotoType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__phototype)否否媒体资产的类型（图片/视频）。albumUristring否否媒体资产（图片/视频）所属相册的uri。[]()[]()

#### PhotoAssetChangeData20+

媒体资产（图片/视频）的具体变更数据。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明assetBeforeChange[PhotoAssetChangeInfo](#ZH-CN_TOPIC_0000002529285945__photoassetchangeinfo20) | null否否变更前的媒体资产（图片/视频）数据。如果是新增资产，assetBeforeChange为null。assetAfterChange[PhotoAssetChangeInfo](#ZH-CN_TOPIC_0000002529285945__photoassetchangeinfo20) | null否否变更后的媒体资产（图片/视频）数据。如果是删除资产，assetAfterChange为null。isContentChangedboolean否否媒体资产（图片/视频）内容是否变化。true表示文件内容发生变化，false表示文件内容未发生变化。isDeletedboolean否否媒体资产（图片/视频）是否被删除。true表示资产被彻底删除，false表示资产未被彻底删除。[]()[]()

#### PhotoAssetChangeInfos20+

媒体资产（图片/视频）的变更通知信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明type[NotifyChangeType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__notifychangetype20)否否媒体资产（图片/视频）变更的通知类型。assetChangeDatas[PhotoAssetChangeData](#ZH-CN_TOPIC_0000002529285945__photoassetchangedata20)[] | null否否变更的媒体资产（图片/视频）数组。如果需要重新查询所有媒体资产，assetChangeDatas为null。isForRecheckboolean否否

应用是否应该重新查询所有媒体资产（图片/视频）信息。true表示需要重新查询所有资产，false表示无需查询所有资产。

**注意：**

在大量资产操作或者异常通知的场景下，应用收到的isForRecheck为true，表示重新查询所有资产信息。

[]()[]()

#### AlbumChangeInfo20+

相册信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明albumType[AlbumType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__albumtype)否否相册类型。albumSubtype[AlbumSubtype](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__albumsubtype)否否相册子类型。albumNamestring否否相册名。albumUristring否否相册uri。imageCountnumber否否相册中的图片数量。videoCountnumber否否相册中的视频数量。countnumber否否相册中的资产总数，包括图片和视频。coverUristring否否相册封面资产的uri。[]()[]()

#### AlbumChangeData20+

相册的具体变更数据。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明albumBeforeChange[AlbumChangeInfo](#ZH-CN_TOPIC_0000002529285945__albumchangeinfo20) | null否否变更前的相册数据。如果是新增相册，albumBeforeChange为null。albumAfterChange[AlbumChangeInfo](#ZH-CN_TOPIC_0000002529285945__albumchangeinfo20) | null否否变更后的相册数据。如果是删除相册，albumAfterChange为null。[]()[]()

#### AlbumChangeInfos20+

相册的变更通知信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明type[NotifyChangeType](../../topics/networking/Enums (arkts-apis-photoaccesshelper-e).md#ZH-CN_TOPIC_0000002529445919__notifychangetype20)否否相册变更的通知类型。albumChangeDatas[AlbumChangeData](#ZH-CN_TOPIC_0000002529285945__albumchangedata20)[] | null否否变更的相册数组。如果需要重新查询所有相册，albumChangeDatas为null。isForRecheckboolean否否

应用是否应该重新查询所有相册信息。true表示需要重新查询所有相册，false表示无需查询所有相册。

**注意：**

在大量相册操作或者异常通知的场景下，应用收到的isForRecheck为true，表示重新查询所有相册信息。