[]()[]()

# Enums

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

[]()[]()

#### PhotoType

枚举，媒体文件类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明IMAGE1图片。VIDEO2视频。[]()[]()

#### PhotoSubtype12+

PhotoSubtype是不同[PhotoAsset](../../types/interfaces/Interface (PhotoAsset).md)类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明DEFAULT0默认照片类型。MOVING_PHOTO3动态照片文件类型。BURST4连拍照片文件类型。[]()[]()

#### DynamicRangeType12+

枚举，媒体文件的动态范围类型。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明SDR0标准动态范围类型。HDR1高动态范围类型。[]()[]()

#### AlbumType

枚举，相册类型。例如，用户相册、系统预置相册或由应用创建的相册。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明USER0用户相册。SYSTEM1024系统预置相册。[]()[]()

#### AlbumSubtype

枚举，相册子类型，表示具体的相册类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明USER_GENERIC1用户相册。FAVORITE1025收藏夹。VIDEO1026视频相册。IMAGE12+1031图片相册。ANY2147483647任意相册。[]()[]()

#### PositionType16+

枚举，文件位置，表示文件在本地或云端。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明LOCAL1文件只存在于本端设备。CLOUD2文件只存在于云端。LOCAL_AND_CLOUD3文件存在于本端设备和云端。[]()[]()

#### PhotoKeys

枚举，图片和视频文件关键信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明URI'uri'

文件uri。

**注意：**

查询照片时，该字段仅支持使用[DataSharePredicates.equalTo](../../modules/ohos/@ohos.data.dataSharePredicates (数据共享谓词).md#ZH-CN_TOPIC_0000002529444645__equalto10)谓词。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

PHOTO_TYPE'media_type'

媒体文件类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DISPLAY_NAME'display_name'

显示名字。规格为：

- 应包含有效文件主名和图片或视频扩展名。

- 文件名字符串长度为1~255。

- 文件主名中不允许出现的非法英文字符，包括：. .. \ / : * ? " ' ` < > | { } [ ]。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

SIZE'size'

文件大小（单位：字节）。动态照片的size包括图片和视频的总大小。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DATE_ADDED'date_added'

文件创建时的Unix时间戳（单位：秒）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DATE_MODIFIED'date_modified'

文件修改时的Unix时间戳（单位：秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DURATION'duration'

持续时间（单位：毫秒）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

WIDTH'width'

图片宽度（单位：像素）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

HEIGHT'height'

图片高度（单位：像素）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DATE_TAKEN'date_taken'

拍摄时的Unix时间戳（单位：秒）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

ORIENTATION'orientation'

文件的旋转角度，单位为度。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

FAVORITE'is_favorite'

收藏。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

TITLE'title'

文件标题。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DATE_ADDED_MS12+'date_added_ms'

文件创建时的Unix时间戳（单位：毫秒）。

**注意：**

查询照片时，不支持基于该字段排序。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DATE_MODIFIED_MS12+'date_modified_ms'

文件修改时的Unix时间戳（单位：毫秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。

**注意：**

查询照片时，不支持基于该字段排序。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

PHOTO_SUBTYPE12+'subtype'

媒体文件的子类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DYNAMIC_RANGE_TYPE12+'dynamic_range_type'

媒体文件的动态范围类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

COVER_POSITION12+'cover_position'

动态照片的封面位置，具体表示封面帧所对应的视频时间戳（单位：微秒）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

BURST_KEY12+'burst_key'

一组连拍照片的唯一标识：uuid。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

LCD_SIZE12+'lcd_size'

LCD图片的宽高，值为width:height拼接而成的字符串。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

THM_SIZE12+'thm_size'

THUMB图片的宽高，值为width:height拼接而成的字符串。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DETAIL_TIME13+'detail_time'

大图浏览时间，值为拍摄时对应时区的时间的字符串，不会跟随时区变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DATE_TAKEN_MS13+'date_taken_ms'

拍摄时的Unix时间戳（单位：毫秒）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

POSITION16+'position'

文件位置类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

MEDIA_SUFFIX18+'media_suffix'文件的后缀名。OWNER_ALBUM_ID22+'owner_album_id'照片所属的相册id。ASPECT_RATIO22+'aspect_ratio'

图片和视频的宽高比。

 ​**模型约束**：此接口仅可在Stage模型下使用。

[]()[]()

#### AlbumKeys

枚举，相册关键信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明URI'uri'相册uri。ALBUM_NAME'album_name'相册名字。[]()[]()

#### ResourceType11+

枚举，写入资源的类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明IMAGE_RESOURCE1表示图片资源。VIDEO_RESOURCE2表示视频资源。[]()[]()

#### ImageFileType13+

枚举，图片保存类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明JPEG1表示jpeg图片类型。HEIF2表示heif图片类型。[]()[]()

#### NotifyType

枚举，通知事件的类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明NOTIFY_ADD0添加文件集或相册通知的类型。NOTIFY_UPDATE1文件集或相册的更新通知类型。NOTIFY_REMOVE2删除文件集或相册的通知类型。NOTIFY_ALBUM_ADD_ASSET3在相册中添加的文件集的通知类型。NOTIFY_ALBUM_REMOVE_ASSET4在相册中删除的文件集的通知类型。[]()[]()

#### DefaultChangeUri

枚举，DefaultChangeUri子类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明DEFAULT_PHOTO_URI'file://media/Photo'默认PhotoAsset的uri，与forSubUri{true}一起使用，将接收所有PhotoAsset的更改通知。DEFAULT_ALBUM_URI'file://media/PhotoAlbum'默认相册的uri，与forSubUri{true}一起使用，将接收所有相册的更改通知。[]()[]()

#### PhotoViewMIMETypes

枚举，可选择的媒体文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明IMAGE_TYPE'image/*'

图片类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

VIDEO_TYPE'video/*'

视频类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

IMAGE_VIDEO_TYPE'*/*'

图片和视频类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MOVING_PHOTO_IMAGE_TYPE12+'image/movingPhoto'

动态照片类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### RecommendationType11+

枚举，推荐的图片类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明QR_OR_BAR_CODE1

二维码或条码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

QR_CODE2

二维码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

BAR_CODE3

条码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

ID_CARD4

身份证。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

PROFILE_PICTURE5

头像。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

PASSPORT12+6

护照。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

BANK_CARD12+7

银行卡。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

DRIVER_LICENSE12+8

驾驶证。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

DRIVING_LICENSE12+9

行驶证。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

FEATURED_SINGLE_PORTRAIT12+10

推荐人像。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let recommendOptions: photoAccessHelper.RecommendationOptions = {
      recommendationType: photoAccessHelper.RecommendationType.ID_CARD
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

#### SingleSelectionMode18+

枚举，单选模式类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明BROWSER_MODE0大图预览模式。SELECT_MODE1直接选中模式。BROWSER_AND_SELECT_MODE2兼容模式，点击右下角区域为直接选中模式，点击其他区域进入大图预览模式。[]()[]()

#### FilterOperator19+

枚举，支持进行过滤的操作符。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明EQUAL_TO0等于。NOT_EQUAL_TO1不等于。MORE_THAN2大于。LESS_THAN3小于。MORE_THAN_OR_EQUAL_TO4大于等于。LESS_THAN_OR_EQUAL_TO5小于等于。BETWEEN6在指定范围内。[]()[]()

#### DeliveryMode11+

枚举，资源分发模式。

该模式适用于分段式拍照或分段式视频。如果当前设备不具备分段式能力，则以下三种分发模式无区别，直接返回请求的图片或视频资源。请求的结果通过[onDataPrepared](../../types/interfaces/Interface (MediaAssetDataHandler).md#ZH-CN_TOPIC_0000002497605952__ondataprepared11)回调返回。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明FAST_MODE0

快速模式。

针对分段式拍照或视频场景，若当前存在高质量图或视频，则立即返回高质量图或视频的请求结果回调；若当前存在低质量图或视频，则立即返回低质量图或视频的请求结果回调。

HIGH_QUALITY_MODE1

高质量模式。

针对分段式拍照或视频场景，若当前存在高质量图或视频，则立即返回高质量图或视频的请求结果回调；若当前存在低质量图或视频，则申请高质量图或视频的生成任务，待高质量图或视频生成后，返回高质量图或视频的请求结果回调。

BALANCE_MODE2

均衡模式。

- 针对分段式拍照场景，若当前存在高质量图，则立即返回高质量图的请求结果回调；若当前存在低质量图，则立即返回低质量图的请求结果回调，并申请高质量图生成任务，待高质量图生成后，再次返回高质量图的请求结果回调。

- 针对分段式视频场景，若当前存在高质量视频，则立即返回高质量视频的请求结果回调；若当前存在低质量视频，则立即返回低质量视频的请求结果回调。

[]()[]()

#### CompatibleMode15+

配置转码模式。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明ORIGINAL_FORMAT_MODE0原视频资源内容模式。COMPATIBLE_FORMAT_MODE1兼容模式，从HDR视频资源转换为SDR视频资源。[]()[]()

#### CompleteButtonText14+

配置完成按钮显示内容。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明TEXT_DONE14+0

显示“完成”。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

TEXT_SEND14+1

显示“发送”。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

TEXT_ADD14+2

显示“添加”。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

[]()[]()

#### NotifyChangeType20+

枚举，媒体资产（图片/视频）或相册变更事件的通知类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明NOTIFY_CHANGE_ADD0媒体资产（图片/视频）或相册已经创建。NOTIFY_CHANGE_UPDATE1媒体资产（图片/视频）或相册已经修改。NOTIFY_CHANGE_REMOVE2媒体资产（图片/视频）或相册已经删除。[]()[]()

#### PhotoSource20+

枚举，图片或者视频数据的来源类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明ALL0

所有来源的图片、视频。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

CAMERA1

仅相机拍摄的图片、视频。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

SCREENSHOT2

截屏图片或者录屏视频。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### MovingPhotoBadgeStateType22+

枚举，动态照片状态。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明NOT_MOVING_PHOTO0非动态照片。MOVING_PHOTO_ENABLED1打开动态照片效果。MOVING_PHOTO_DISABLED2关闭动态照片效果。[]()[]()

#### VideoMode22+

枚举，视频文件的log模式。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明DEFAULT0

默认类型。

取值为0表示当前视频非log模式或未判断类型，后续部分视频判断后字段会更新为1，因此不建议使用此字段进行查询。

LOG_VIDEO1log模式视频的文件类型。[]()[]()

#### OperationType22+

表示各类谓词的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明EQUAL_TO1等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。NOT_EQUAL_TO2不等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。GREATER_THAN3大于，取value数组的第一个元素与谓词匹配。 超出长度取第1个。LESS_THAN4小于，取value数组的第一个元素与谓词匹配。超出长度取第1个。GREATER_THAN_OR_EQUAL_TO5大于等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。LESS_THAN_OR_EQUAL_TO6小于等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。AND7逻辑'与'，相当于数据库查询语句的'and'。无需传入field和value。OR8逻辑'或'，相当于数据库查询语句的'or'。无需传入field和value。IN9匹配在指定范围内的字段，value长度限制10个。NOT_IN10匹配不在指定范围内的字段，value长度限制10个。BEGIN_WRAP11用于向谓词添加英文左括号，相当于数据库查询语句的"("，必须和英文右括号一起使用。无需传入field和value。END_WRAP12用于向谓词添加英文右括号，相当于数据库查询语句的")"，必须和英文左括号一起使用。无需传入field和value。BETWEEN13

匹配指定范围内的字段。

包含两端边界值，为左闭右闭区间。取value数组的前两个元素与谓词匹配，超出长度取前2个，分别表示左右边界。例如：[1, 2, 3, 4]中取前两个，1表示左边界，2表示右边界。

NOT_BETWEEN14

匹配超出指定范围内的字段。

不包含两端边界值，为左开右开区间。取value数组的前两个元素与谓词匹配，超出长度取前2个，分别表示左右边界。例如：[1, 2, 3, 4]中取前两个，1表示左边界，2表示右边界。