# Interface (MediaAssetDataHandler)

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### onDataPrepared11+

onDataPrepared(data: T, map?: Map<string, string>): void

媒体资源就绪通知，系统在资源准备就绪时回调此方法。若资源准备出错，回调的data为undefined。资源请求与回调一一对应。

T支持ArrayBuffer，[ImageSource](Interface (ImageSource).md)，[MovingPhoto](Interface (MovingPhoto).md)和boolean四种数据类型。其中，ArrayBuffer表示图片/视频资源数据，[ImageSource](Interface (ImageSource).md)表示图片源，[MovingPhoto](Interface (MovingPhoto).md)表示动态照片对象，boolean表示图片/视频资源是否成功写入应用沙箱。

map支持返回的信息：

| map键名 | 值说明 |
| --- | --- |
| 'quality' | 图片质量。高质量为'high'，低质量为'low'。 |

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 已就绪的图片资源数据。泛型，支持ArrayBuffer, ImageSource, MovingPhoto和boolean四种数据类型。 |
| map12+ | Map<string, string> | 否 | 用于获取图片资源的额外信息，如图片质量。当前仅支持'quality'。 |

**示例：**

```ets
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
  onDataPrepared = (data: image.ImageSource, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对ImageSource的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
  onDataPrepared = (data: ArrayBuffer, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对ArrayBuffer的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map['quality']);
}

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  onDataPrepared = (data: photoAccessHelper.MovingPhoto, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对MovingPhoto的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }
```