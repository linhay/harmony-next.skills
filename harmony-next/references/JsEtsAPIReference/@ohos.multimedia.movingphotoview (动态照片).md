# @ohos.multimedia.movingphotoview (动态照片)

用于播放动态照片文件并控制其播放状态的组件。

该组件从API Version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

当前不支持在预览器中使用MovingPhotoView组件。

#### 导入模块

- MovingPhotoViewAttribute是用于配置MovingPhotoView组件属性的关键接口。API version 21及之前版本，导入MovingPhotoView组件后需要开发者手动导入MovingPhotoViewAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入MovingPhotoView组件后，会自动导入MovingPhotoViewAttribute，无需开发者手动导入。
- 如果开发者手动导入MovingPhotoViewAttribute，DevEco Studio会将其显示置灰，API version 21及之前版本删除会编译报错，从API version 22开始，删除对功能无影响。

 API version 21及之前版本：

```ets
import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
```

 API version 22及之后版本：

```ets
import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';
```

#### MovingPhotoView

- 当前不支持动态属性设置。
- 当前不支持ArkUI通用属性ComponentOptions中expandSafeArea属性设置。
- 该组件长按触发播放时组件区域放大为1.1倍。
- 该组件使用[AVPlayer](Interface (AVPlayer).md)进行播放，同时开启的AVPlayer个数不建议超过3个，超过3个可能会出现视频播放卡顿现象。

MovingPhotoView(options: MovingPhotoViewOptions)

**参数：**

参数名参数类型必填参数描述options[MovingPhotoViewOptions](#ZH-CN_TOPIC_0000002529285949__movingphotoviewoptions)是动态照片信息。

#### MovingPhotoViewOptions

名称类型只读可选说明movingPhoto[photoAccessHelper.MovingPhoto](Interface (MovingPhoto).md)否否

支持媒体库MovingPhoto数据源，具体信息详见[MovingPhoto说明](Interface (MovingPhoto).md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

controller[MovingPhotoViewController](#ZH-CN_TOPIC_0000002529285949__movingphotoviewcontroller)否是

设置动态照片控制器，可以控制动态照片的播放状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

imageAIOptions18+[ImageAIOptions](图像类型定义.md#ZH-CN_TOPIC_0000002497604902__imageaioptions12)否是

设置动态照片AI分析选项，可配置分析类型或绑定一个分析控制器。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

#### 属性

除支持[通用属性](通用属性.md)外，还支持以下属性：

#### muted

muted(isMuted: boolean)

设置是否静音。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明isMutedboolean是

是否静音。

默认值：false。

false：非静音。

true：静音。

#### objectFit

objectFit(value: ImageFit)

设置动态照片显示模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明value[ImageFit](枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagefit)是

视频显示模式。

默认值：Cover。

#### autoPlayPeriod13+

autoPlayPeriod(startTime: number, endTime: number)

设置自动播放区间，附属于autoPlay的子配置项。

在调用此方法前，需将[autoPlay](#ZH-CN_TOPIC_0000002529285949__autoplay13)设置为true，设置自动播放，否则指定的视频区间(startTime, endTime)无法生效。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明startTimenumber是

区间播放开始时间，单位：ms。

取值范围：大于等于0。

endTimenumber是

区间播放结束时间，单位：ms。

取值范围：大于startTime。

#### autoPlay13+

autoPlay(isAutoPlay: boolean)

设置自动播放，自动播放一遍视频。

动态照片加载完成后，准备播放时可以调用，播放完成后显示静态图。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明isAutoPlayboolean是

是否自动播放。

false：不自动播放。

true：自动播放。

默认值：false。

#### repeatPlay13+

repeatPlay(isRepeatPlay: boolean)

设置循环播放，重复播放视频。 repeatPlay与autoPlay及长按播放互斥，repeatPlay设置时，autoPlay和长按播放均不生效。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明isRepeatPlayboolean是

是否循环播放。

false：不循环播放。

true：循环播放。

默认值：false。

#### enableAnalyzer18+

enableAnalyzer(enabled: boolean)

设置该图片是否支持AI分析，当前支持主体识别、文字识别和对象查找等功能。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明enabledboolean是

是否开启AI分析。

false：不开启AI分析。

true：开启AI分析。

默认值：true。

#### 事件

除支持[通用事件](通用事件.md)外，还支持以下事件：

#### onComplete13+

onComplete(callback: MovingPhotoViewEventCallback)

动态照片加载完成图片时触发该事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callback[MovingPhotoViewEventCallback](#ZH-CN_TOPIC_0000002529285949__movingphotovieweventcallback)是动态照片加载完成图片的回调。

#### onStart

onStart(callback: MovingPhotoViewEventCallback)

播放时触发该事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callback[MovingPhotoViewEventCallback](#ZH-CN_TOPIC_0000002529285949__movingphotovieweventcallback)是动态照片开始播放时触发的回调。

#### onPause

onPause(callback: MovingPhotoViewEventCallback)

播放暂停时触发该事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callback[MovingPhotoViewEventCallback](#ZH-CN_TOPIC_0000002529285949__movingphotovieweventcallback)是动态照片播放暂停时触发的回调。

#### onFinish

onFinish(callback: MovingPhotoViewEventCallback)

播放结束时触发该事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callback[MovingPhotoViewEventCallback](#ZH-CN_TOPIC_0000002529285949__movingphotovieweventcallback)是动态照片播放结束时触发的回调。

#### onError

onError(callback: MovingPhotoViewEventCallback)

播放失败时触发该事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callback[MovingPhotoViewEventCallback](#ZH-CN_TOPIC_0000002529285949__movingphotovieweventcallback)是动态照片播放失败时触发的回调。

#### onStop

onStop(callback: MovingPhotoViewEventCallback)

播放停止时触发该事件(当stop()方法被调用后触发)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callback[MovingPhotoViewEventCallback](#ZH-CN_TOPIC_0000002529285949__movingphotovieweventcallback)是动态照片停止播放时触发的回调。

#### onPrepared20+

onPrepared(callback: MovingPhotoViewEventCallback)

动态照片准备播放时触发该事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callback[MovingPhotoViewEventCallback](#ZH-CN_TOPIC_0000002529285949__movingphotovieweventcallback)是动态照片准备播放时的回调。

#### MovingPhotoViewEventCallback

declare type MovingPhotoViewEventCallback = () => void

动态照片播放状态发生变化时触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

#### MovingPhotoViewController

一个MovingPhotoViewController对象可以控制一个MovingPhotoView，可用视频播放实例请参考[@ohos.multimedia.media](模块描述.md)。

#### constructor

constructor()

MovingPhotoViewController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

#### startPlayback

startPlayback()

开始播放，动态照片加载完成后，在播放准备，暂停，完成时调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

#### stopPlayback

stopPlayback()

停止播放，再次播放时从头开始播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

#### refreshMovingPhoto18+

refreshMovingPhoto()

强制刷新动态照片组件加载的视频和图片资源，会打断组件当前的行为，使用时要谨慎。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

#### 示例1：多种形式播放动态照片

```ets
// xxx.ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { emitter } from '@kit.BasicServicesKit';
import { dataSharePredicates } from '@kit.ArkData';
// API version 21及之前版本导入方式：import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
// API version 22及之后版本导入方式如下：
import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';

const PHOTO_SELECT_EVENT_ID: number = 80001

@Entry
@Component
struct MovingPhotoViewDemo {
  @State src: photoAccessHelper.MovingPhoto | undefined = undefined
  @State isMuted: boolean = false
  controller: MovingPhotoViewController = new MovingPhotoViewController()
  private uiContext: UIContext = this.getUIContext()

  aboutToAppear(): void {
    emitter.on({
      eventId: PHOTO_SELECT_EVENT_ID,
      priority: emitter.EventPriority.IMMEDIATE,
    }, (eventData: emitter.EventData) => {
      this.src = AppStorage.get<photoAccessHelper.MovingPhoto>('mv_data') as photoAccessHelper.MovingPhoto
    })
  }

  aboutToDisappear(): void {
    emitter.off(PHOTO_SELECT_EVENT_ID)
  }

  build() {
    Column() {
      Row() {
        Button('PICK')
          .margin(5)
          .onClick(async () => {
            try {
              let uris: Array<string> = []
              const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions()
              photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE
              photoSelectOptions.maxSelectNumber = 2
              const photoViewPicker = new photoAccessHelper.PhotoViewPicker()
              let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoViewPicker.select(photoSelectOptions)
              uris = photoSelectResult.photoUris
              if (uris[0]) {
                this.handlePickerResult(this.uiContext.getHostContext()!, uris[0], new MediaDataHandlerMovingPhoto())
              }
            } catch (e) {
              console.error(`pick file failed`)
            }
          })
      }
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('15%')

      Row() {
        Column() {
          MovingPhotoView({
            movingPhoto: this.src,
            controller: this.controller
          })
            .width('100%')
            .height('100%')
            .muted(this.isMuted)
            .autoPlay(true)
            .repeatPlay(false)
            .autoPlayPeriod(0, 600)
            .objectFit(ImageFit.Cover)
            .onComplete(() => {
              console.info('Completed');
            })
            .onStart(() => {
              console.info('onStart')
            })
            .onFinish(() => {
              console.info('onFinish')
            })
            .onStop(() => {
              console.info('onStop')
            })
            .onError(() => {
              console.error('onError')
            })
        }
      }
      .height('70%')

      Row() {
        Button('start')
          .onClick(() => {
            this.controller.startPlayback()
          })
          .margin(5)
        Button('stop')
          .onClick(() => {
            this.controller.stopPlayback()
          })
          .margin(5)
        Button('mute')
          .onClick(() => {
            this.isMuted = !this.isMuted
          })
          .margin(5)
      }
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('15%')
    }
  }

  async handlePickerResult(context: Context, uri: string, handler: photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto>): Promise<void> {
    let uriPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    uriPredicates.equalTo('uri', uri)
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: uriPredicates
    };
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context)
    let assetResult = await phAccessHelper.getAssets(fetchOptions)
    let asset = await assetResult.getFirstObject()
    let requestOptions: photoAccessHelper.RequestOptions = {
      deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
    }
    try {
      photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler)
    } catch (err) {
      console.error("request error: ", err)
    }
  }
}

class MediaDataHandlerMovingPhoto implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    AppStorage.setOrCreate('mv_data', movingPhoto)
    emitter.emit({
      eventId: PHOTO_SELECT_EVENT_ID,
      priority: emitter.EventPriority.IMMEDIATE,
    }, {
    })
  }
}
```

#### 示例2：在元服务中使用动态照片

```ets
// xxx.ets
// API version 21及之前版本导入方式：import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
// API version 22及之后版本导入方式如下：
import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';

let data: photoAccessHelper.MovingPhoto
async function loading(context: Context) {
  try {
    // 需要确保imageFileUri和videoFileUri对应的资源在应用沙箱存在。
    let imageFileUri = 'file://{bundleName}/data/storage/el2/base/haps/entry/files/xxx.jpg';
    let videoFileUri = 'file://{bundleName}/data/storage/el2/base/haps/entry/files/xxx.mp4';
    data = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
    console.info('load moving photo successfully');
  } catch (err) {
    console.error(`load moving photo failed with error: ${err.code}, ${err.message}`);
  }
}
@Entry
@Component
struct Index {
  controller: MovingPhotoViewController = new MovingPhotoViewController()
  private uiContext: UIContext = this.getUIContext()
  @State ImageFit: ImageFit | undefined | null = ImageFit.Contain;
  @State flag: boolean = true;
  @State autoPlayFlag: boolean = true;
  @State repeatPlayFlag: boolean = false;
  @State autoPlayPeriodStart: number = 0;
  @State autoPlayPeriodEnd: number = 500;
  aboutToAppear(): void {
    loading(this.uiContext.getHostContext()!)
  }

  build() {
    NavDestination() {
      Column() {
        Stack({ alignContent: Alignment.BottomStart }) {
          MovingPhotoView({
            movingPhoto: data,
            controller: this.controller
          })
            .width(300)
            .height(400)
            .muted(this.flag)
            .objectFit(this.ImageFit)
            .autoPlay(this.autoPlayFlag)
            .autoPlayPeriod(this.autoPlayPeriodStart, this.autoPlayPeriodEnd)
            .repeatPlay(this.repeatPlayFlag)
            .onComplete(() => {
              console.info('onComplete')
            })
            .onStart(() => {
              console.info('onStart')
            })
            .onStop(() => {
              console.info('onStop')
            })
            .onPause(() => {
              console.info('onPause')
            })
            .onFinish(() => {
              console.info('onFinish')
            })
            .onError(() => {
              console.info('onError')
            })
        }

        Row() {
          Button('Play')
            .onClick(() => {
              this.controller.startPlayback()
            })
          Button('StopPlay')
            .onClick(() => {
              this.controller.stopPlayback()
            })
          Button('refreshMovingPhoto')
            .onClick(() => {
              this.controller.refreshMovingPhoto()
            })
          Button('mute').id('MovingPhotoView_true')
            .onClick(() => {
              this.flag = false
            })
        }
      }
    }
  }
}
```

#### 示例3：图像分析功能使用

```ets
// xxx.ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { emitter } from '@kit.BasicServicesKit';
import { dataSharePredicates } from '@kit.ArkData';
import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
import { visionImageAnalyzer } from '@kit.VisionKit';
const PHOTO_SELECT_EVENT_ID: number = 80001

@Entry
@Component
struct MovingPhotoViewDemo {
  @State src: photoAccessHelper.MovingPhoto | undefined = undefined
  @State isMuted: boolean = false
  controller: MovingPhotoViewController = new MovingPhotoViewController()
  private aiController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT, ImageAnalyzerType.OBJECT_LOOKUP],
    aiController: this.aiController
  }
  private uiContext: UIContext = this.getUIContext()

  aboutToAppear(): void {
    emitter.on({
      eventId: PHOTO_SELECT_EVENT_ID,
      priority: emitter.EventPriority.IMMEDIATE,
    }, (eventData: emitter.EventData) => {
      this.src = AppStorage.get<photoAccessHelper.MovingPhoto>('mv_data') as photoAccessHelper.MovingPhoto
    })
  }

  aboutToDisappear(): void {
    emitter.off(PHOTO_SELECT_EVENT_ID)
  }

  build() {
    Column() {
      Row() {
        Button('PICK')
          .margin(5)
          .onClick(async () => {
            try {
              let uris: Array<string> = []
              const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions()
              photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE
              photoSelectOptions.maxSelectNumber = 2
              const photoViewPicker = new photoAccessHelper.PhotoViewPicker()
              let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoViewPicker.select(photoSelectOptions)
              uris = photoSelectResult.photoUris
              if (uris[0]) {
                this.handlePickerResult(this.uiContext.getHostContext()!, uris[0], new MediaDataHandlerMovingPhoto())
              }
            } catch (e) {
              console.error(`pick file failed`)
            }
          })
      }
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('15%')

      Row() {
        Column() {
          MovingPhotoView({
            movingPhoto: this.src,
            controller: this.controller,
            imageAIOptions: this.options
          })
            .width('100%')
            .height('100%')
            .muted(this.isMuted)
            .autoPlay(true)
            .repeatPlay(false)
            .autoPlayPeriod(0, 600)
            .objectFit(ImageFit.Cover)
            .enableAnalyzer(true)
            .onComplete(() => {
              console.log('Completed');
            })
            .onStart(() => {
              console.log('onStart')
            })
            .onFinish(() => {
              console.log('onFinish')
            })
            .onStop(() => {
              console.log('onStop')
            })
            .onError(() => {
              console.log('onError')
            })
        }
      }
      .height('70%')

      Row() {
        Button('start')
          .onClick(() => {
            this.controller.startPlayback()
          })
          .margin(5)
        Button('stop')
          .onClick(() => {
            this.controller.stopPlayback()
          })
          .margin(5)
        Button('mute')
          .onClick(() => {
            this.isMuted = !this.isMuted
          })
          .margin(5)
      }
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('15%')
    }
  }

  async handlePickerResult(context: Context, uri: string, handler: photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto>): Promise<void> {
    let uriPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    uriPredicates.equalTo('uri', uri)
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: uriPredicates
    };
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context)
    let assetResult = await phAccessHelper.getAssets(fetchOptions)
    let asset = await assetResult.getFirstObject()
    let requestOptions: photoAccessHelper.RequestOptions = {
      deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
    }
    try {
      photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler)
    } catch (err) {
      console.error("request error: ", err)
    }
  }
}

class MediaDataHandlerMovingPhoto implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    AppStorage.setOrCreate('mv_data', movingPhoto)
    emitter.emit({
      eventId: PHOTO_SELECT_EVENT_ID,
      priority: emitter.EventPriority.IMMEDIATE,
    }, {
    })
  }
}
```