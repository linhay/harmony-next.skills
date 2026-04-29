# @ohos.file.RecentPhotoComponent (最近图片组件)

应用可以在布局中嵌入最近图片组件，通过此组件，应用无需申请权限，即可指定配置访问公共目录中最近的一个图片或视频文件。授予的权限仅包含只读权限。

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import {
  RecentPhotoComponent, RecentPhotoOptions, RecentPhotoCheckResultCallback, RecentPhotoInfo, RecentPhotoCheckInfoCallback,
  RecentPhotoClickCallback, PhotoSource, RecentPhotoInfo, RecentPhotoCheckInfoCallback,
} from '@kit.MediaLibraryKit';
```

#### 属性

支持[通用属性]([通用属性](../../topics/misc/通用属性.md).md)。

#### RecentPhotoComponent

RecentPhotoComponent({ recentPhotoOptions?: RecentPhotoOptions, onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback, onRecentPhotoClick: RecentPhotoClickCallback, onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback, })

RecentPhotoComponent，是最近图片组件，可用于访问按创建时间排序的公共目录下最新的一个图片或视频文件。通过此组件，应用无需申请媒体访问权限，即可根据配置项，访问公共目录下最新的一个图片或视频文件。

**装饰器类型**：@Component

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoOptions | RecentPhotoOptions | 否 | 最近图片配置参数信息。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onRecentPhotoCheckResult | RecentPhotoCheckResultCallback | 否 | 最近图片查询结果回调函数。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onRecentPhotoClick | RecentPhotoClickCallback | 是 | 选择最近图片回调函数。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onRecentPhotoCheckInfo13+ | RecentPhotoCheckInfoCallback | 否 | 最近图片查询结果回调函数，并且返回该照片的相关信息。  元服务API：从API version 13开始，该接口支持在元服务中使用。 |

#### RecentPhotoOptions

最近图片配置选项。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| period | number | 否 | 是 | 配置显示多久时间段内按创建时间排序的最新一张图片，单位为秒（s）。最长可配置时长为1天（86400s）。 当值小于等于0、大于86400或者未配置时，默认按最长时间段1天显示最近图片。当配置时间段内无符合的图片或视频时，组件不显示。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| MIMEType | [photoAccessHelper.PhotoViewMIMETypes](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes) | 否 | 是 | 最近图片控件显示的文件类型，默认为PhotoViewMIMETypes.IMAGE_VIDEO_TYPE。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| photoSource | PhotoSource | 否 | 是 | 配置最近图片视频显示内容的来源，比如拍照、截屏等。默认不限制来源。  元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| isAutoRefreshSupported20+ | boolean | 否 | 是 | 配置最近照片组件在符合要求的最近图片或视频发生变更（包括新增、删除、修改）时是否进行刷新。 当组件原显示的最近图片或视频被删除，而无符合要求的图片或视频时，则显示占位符，组件不自动退出。 默认为false，不支持自动刷新；配置为true时显示全量照片；period字段失效。  元服务API：从API version 20开始，该接口支持在元服务中使用。 |
| colorMode20+ | PickerColorMode | 否 | 是 | 支持应用配置占位符的颜色模式。 当isAutoRefreshSupported为true，且无符合要求的最近图片或视频时，显示占位符，字段生效。 默认为跟随系统深浅色模式。  元服务API：从API version 20开始，该接口支持在元服务中使用。 |

#### RecentPhotoInfo13+

最近图片相关信息。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dateTaken | number | 否 | 是 | 最近图片/视频的拍摄时间，单位为毫秒。（距1970年1月1日的毫秒数值）。 |
| identifier | string | 否 | 是 | 最近图片/视频的名称hash值，用于辅助应用区分最新图片组件将要显示的图片/视频与之前曾显示过的图片/视频是否为同一个。 |

#### RecentPhotoCheckResultCallback

type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void

最近图片查询结果回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoExists | boolean | 是 | 查询最近图片是否存在，true为存在，false为不存在，默认为true。 |

#### RecentPhotoClickCallback

type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean

选择最近图片触发的回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoInfo | BaseItemInfo | 是 | 最近图片信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 应用回调中处理最近图片的结果返回。true表示处理完成。 |

#### RecentPhotoCheckInfoCallback13+

type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void

最近图片是否存在查询结果以及最近图片相关信息的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoExists | boolean | 是 | 查询最近图片是否存在，true为存在，false为不存在，默认为true。 |
| info | RecentPhotoInfo | 是 | 最近图片相关信息。 |

#### PhotoSource

枚举，图片或者视频数据的来源类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 所有来源的图片、视频。 |
| CAMERA | 1 | 仅相机拍摄的图片、视频。 |
| SCREENSHOT | 2 | 截屏图片或者录屏视频。 |

#### 示例

```ets
// xxx.ets
import {
  photoAccessHelper,
   RecentPhotoComponent,
   RecentPhotoOptions,
   PhotoSource,
   RecentPhotoInfo,
   RecentPhotoCheckResultCallback,
   RecentPhotoClickCallback,
   RecentPhotoCheckInfoCallback,
   BaseItemInfo
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct PickerDemo {
  private recentPhotoOptions: RecentPhotoOptions = new RecentPhotoOptions();
  private recentPhotoCheckResultCallback: RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => this.onRecentPhotoCheckResult(recentPhotoExists);
  private recentPhotoClickCallback: RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo): boolean => this.onRecentPhotoClick(recentPhotoInfo);
  private recentPhotoCheckInfoCallback: RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => this.onRecentPhotoCheckInfo(recentPhotoExists, info);

  aboutToAppear() {
    this.recentPhotoOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
    this.recentPhotoOptions.period = 30;
    this.recentPhotoOptions.photoSource = PhotoSource.ALL;
  }

  private onRecentPhotoCheckResult(recentPhotoExists: boolean): void {
    // 存在符合条件的照片或视频。
    if (recentPhotoExists) {
      console.info('The photo is exist.');
  }

  private onRecentPhotoClick(recentPhotoInfo: BaseItemInfo): boolean {
    // 照片或视频返回。
    if (recentPhotoInfo) {
      console.info('The photo uri is ' + recentPhotoInfo.uri);
      return true;
    }
    return true;
  }

  private onRecentPhotoCheckInfo(recentPhotoExists: boolean, info: RecentPhotoInfo): void {
    // 是否存在符合条件的照片或视频，若存在则可以拿到该照片或视频的相关信息。
  }

  build() {
    Stack() {
      RecentPhotoComponent({
        recentPhotoOptions: this.recentPhotoOptions,
        onRecentPhotoCheckResult: this.recentPhotoCheckResultCallback,
        onRecentPhotoClick: this.recentPhotoClickCallback,
        onRecentPhotoCheckInfo: this.recentPhotoCheckInfoCallback,
      }).height('100%').width('100%')
    }
```