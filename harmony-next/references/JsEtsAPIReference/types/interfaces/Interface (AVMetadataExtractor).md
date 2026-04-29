# Interface (AVMetadataExtractor)

元数据获取类，用于从媒体资源中获取元数据、缩略图。在调用AVMetadataExtractor的方法前，需要先通过[media.createAVMetadataExtractor](Functions.md#ZH-CN_TOPIC_0000002522082030__mediacreateavmetadataextractor11)构建一个AVMetadataExtractor实例。

获取音频或视频元数据、视频缩略图的demo可参考：[使用AVMetadataExtractor提取音视频元数据信息(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avmetadataextractor)。


- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { media } from '@kit.MediaKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fdSrc11+ | AVFileDescriptor | 否 | 是 | 媒体文件描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。 使用示例： 假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }。 说明： 将资源句柄（fd）传递给AVMetadataExtractor实例之后，不允许通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致音视频元数据获取异常。 |
| dataSrc11+ | AVDataSrcDescriptor | 否 | 是 | 流式媒体资源描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。 当应用从远端获取音视频媒体文件，在应用未下载完整音视频资源时，可以设置dataSrc提前获取该资源的元数据。 |

#### setUrlSource20+

setUrlSource(url: string, headers?: Record<string, string>): void

网络点播资源地址描述，通过该接口设置数据源。只支持获取网络[fetchMetadata](#ZH-CN_TOPIC_0000002522242026__fetchmetadata11)（元数据）和[fetchFrameByTime](#ZH-CN_TOPIC_0000002522242026__fetchframebytime20)（缩略图），在获取之前，必须设置媒体资源URL。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 媒体资源URL。 1. 支持的视频格式包括：mp4、mpeg-ts、mkv。 2. 支持的音频格式包括：m4a、aac、mp3、ogg、wav、flac、amr。 支持路径示例： 1. http网络播放：http\://xx。 2. https网络播放：https\://xx。 说明： 不支持设置hls/dash、直播资源。 |
headersRecord<string, string>否支持访问网络资源HttpHeader自定义。默认为空。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;

media.createAVMetadataExtractor(async (error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
    let url = "http://xx";
    let headers: Record<string, string> = {
      "User-Agent": "User-Agent-Value"
    };
    avMetadataExtractor.setUrlSource(url, headers);
  } else {
    console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
  }
});
```

#### fetchFrameByTime20+

fetchFrameByTime(timeUs: number, options: [AVImageQueryOptions](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avimagequeryoptions12), param: PixelMapParams): Promise<image.PixelMap>

获取视频缩略图。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeUs | number | 是 | 需要获取的缩略图在视频中的时间点，单位为微秒（us）。 |
| options | [AVImageQueryOptions](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avimagequeryoptions12) | 是 | 需要获取的缩略图时间点与视频帧的对应关系。 |
| param | PixelMapParams | 是 | 需要获取的缩略图的格式参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | Promise对象，返回视频缩略图对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |
| 5400108 | Parameter check failed. Returned by promise. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;
let pixelMap: image.PixelMap | undefined = undefined;

// 初始化入参。
let timeUs: number = 0;
let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_PREVIOUS_SYNC;
let param: media.PixelMapParams = {
  width: 300,
  height: 300
};
// 获取缩略图。
media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
    avMetadataExtractor.fetchFrameByTime(timeUs, queryOption, param).then((pixelMap: image.PixelMap) => {
      pixelMap = pixelMap;
    }).catch((error: BusinessError) => {
      console.error(`Failed to fetch FrameByTime, error message:${error.message}`);
    });
  } else {
    console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
  }
});
```

**fetchFramesByTimes23+**

fetchFramesByTimes(timesUs: number[], queryOption: [AVImageQueryOptions](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avimagequeryoptions12), param: PixelMapParams, callback: OnFrameFetched): void

批量获取视频缩略图。使用Callback异步回调。


- 先对给定的视频资源进行解码，随后依据提供的参数options和param，从timesUs数组中的每个时间点提取图像帧。

- 当每一次图像提取完成时，系统将调用回调函数并传递提取结果。请注意，回调函数的执行顺序会与timesUs数组中时间点的先后顺序不一致。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timesUs | number[] | 是 | 需要获取的所有缩略图在视频中的时间点集合。 时间单位为微秒（μs），数组长度取值范围为(0, 4096]。 |
| queryOption | [AVImageQueryOptions](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avimagequeryoptions12) | 是 | 需要获取的缩略图时间点与视频帧的对应关系。 |
| param | PixelMapParams | 是 | 需要获取的缩略图的格式参数。 |
| callback | OnFrameFetched | 是 | 需要返回的缩略图信息及可能的异常类型。 异常类型请参考具体返回的错误码信息。 |

错误码：

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by callback. |
| 5400104 | Fetch timeout. Returned by callback. |
| 5400106 | Unsupported format. Returned by callback. |
| 5400105 | Service died. |
| 5400108 | Parameter check failed. e.g. The size of timesUs is larger than 4096. |
| 5411012 | Http cleartext not permitted. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

// 初始化入参。
let timesUs: number[] = [0];
let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_PREVIOUS_SYNC;
let param: media.PixelMapParams = {
  width: 300,
  height: 300
};
// 获取缩略图。
let avMetadataExtractor = await media.createAVMetadataExtractor();
if (avMetadataExtractor !== null) {
  console.info('Succeeded in creating AVMetadataExtractor');
  avMetadataExtractor.fetchFramesByTimes (timesUs, queryOption, param, async (frameInfo: media.FrameInfo, err: BusinessError) => {
    if (err) {
      console.info(`fetchFramesByTimes callback failed, error = ${JSON.stringify(err)}`);
      return;
    }
    if (frameInfo != undefined && frameInfo.image != undefined) {
      let pixelMap = frameInfo.image;
    }});
}
```

**cancelAllFetchFrames23+**

cancelAllFetchFrames(): void

取消正在进行的批量获取缩略图任务（已完成部分不受影响）。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

示例：

```ets
import { media } from '@kit.MediaKit';

let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;

media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
    avMetadataExtractor.cancelAllFetchFrames();
  } else {
    console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
  }
});
```

#### fetchMetadata11+

fetchMetadata(callback: AsyncCallback<AVMetadata>): void

获取媒体元数据。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<AVMetadata> | 是 | 回调函数。异步返回音视频元数据对象（AVMetadata）。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by callback. |
| 5400106 | Unsupported format. Returned by callback. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.fetchMetadata((error: BusinessError, metadata: media.AVMetadata) => {
    if (error) {
      console.error(`Failed to fetch Metadata, err = ${JSON.stringify(error)}`);
      return;
    }
    console.info(`Succeeded in fetching Metadata, genre: ${metadata.genre}`);
  });
}
```

#### fetchMetadata11+

fetchMetadata(): Promise<AVMetadata>

获取媒体元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AVMetadata> | Promise对象。异步返回音视频元数据对象（AVMetadata）。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.fetchMetadata().then((metadata: media.AVMetadata) => {
    console.info(`Succeeded in fetching Metadata, genre: ${metadata.genre}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to fetch Metadata, error message:${error.message}`);
  });
}
```

#### fetchAlbumCover11+

fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void

获取音频专辑封面。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<image.PixelMap> | 是 | 回调函数。异步返回专辑封面。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400106 | Unsupported format. Returned by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  let pixel_map: image.PixelMap | undefined = undefined;

  avMetadataExtractor.fetchAlbumCover((error: BusinessError, pixelMap: image.PixelMap) => {
    if (error) {
      console.error(`Failed to fetch AlbumCover, error = ${JSON.stringify(error)}`);
      return;
    }
    pixel_map = pixelMap;
  });
}
```

#### fetchAlbumCover11+

fetchAlbumCover(): Promise<image.PixelMap>

获取专辑封面。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | Promise对象。异步返回专辑封面。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  let pixel_map: image.PixelMap | undefined = undefined;

  avMetadataExtractor.fetchAlbumCover().then((pixelMap: image.PixelMap) => {
    pixel_map = pixelMap;
  }).catch((error: BusinessError) => {
    console.error(`Failed to fetch AlbumCover, error message:${error.message}`);
  });
}
```

#### release11+

release(callback: AsyncCallback<void>): void

释放资源。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放资源成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release((error: BusinessError) => {
    if (error) {
      console.error(`Failed to release, err = ${JSON.stringify(error)}`);
      return;
    }
    console.info(`Succeeded in releasing.`);
  });
}
```

#### release11+

release(): Promise<void>

释放资源。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异步方式释放资源release方法的Promise返回值。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release().then(() => {
    console.info(`Succeeded in releasing.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to release, error message:${error.message}`);
  });
}
```