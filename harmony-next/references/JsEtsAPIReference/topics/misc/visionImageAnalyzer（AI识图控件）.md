# visionImageAnalyzer（AI识图控件）

AI识图是通过聚合OCR（Optical Character Recognition）、主体分割、实体识别、多目标识别等AI能力，提供场景化的文本识别、主体分割、识图搜索功能。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用接口需捕获异常。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';
```

**Menu**

AI识图菜单。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 菜单内容。 |
| action | Callback<string | Subject[]> | 否 | 否 | 菜单结果回调，包含文字选中结果和抠图结果。 |

**Rect**

矩形数据结构。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 是 | 矩形的左方位置。取值范围在图片的左边界到右边界之间。单位：vp。 |
| top | number | 否 | 是 | 矩形的上方位置。取值范围在图片的上边界到下边界之间。单位：vp。 |
| right | number | 否 | 是 | 矩形的右方位置。取值范围在图片的左边界到右边界之间。单位：vp。 |
| bottom | number | 否 | 是 | 矩形的下方位置。取值范围在图片的上边界到下边界之间。单位：vp。 |

**Subject**

主体识别结果。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 主体id。取值范围：[0，6]。 |
| image | PixelMap | 否 | 否 | 主体识别的图片。 |
| boundingBox | Rect | 否 | 否 | 主体识别图片结果的外接矩形框。 |
| maskData | Int32Array | 否 | 是 | 基于原图大小的一维数组，表示主体掩码。0-255取值范围。0代表背景，255代表主体，中间值代表是否是显著性主体的概率。 起始版本：5.1.0(18)。 说明： maskData参数数据可能较大，通过JSON.stringify()方法解析打印日志会比较耗时，可能会影响接口性能，请按需打印。 |

**SelectedStatus**

识图对象选中状态的枚举值。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECTED | 0 | 选中状态。 |
| UNSELECTED | 1 | 未选中状态。 |

**ImageAnalyzerVisibility**

AI识图控件可见状态的枚举值。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOWN | 0 | AI识图控件的可见状态。 |
| HIDDEN | 1 | AI识图控件的不可见状态。 |

**AIButtonStatus**

AIButton状态的枚举值。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECTED | 0 | AIButton选中状态。 |
| UNSELECTED | 1 | AIButton未选中状态。 |
| HIDDEN | 2 | AIButton隐藏状态。 |

**ObjectSearchPanelVisibility**

图片搜索界面可见状态的枚举值。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOW | 0 | 图片搜索界面的可见状态。 |
| HIDE | 1 | 图片搜索界面的不可见状态。 |

**ImageAnalyzerUIStatus**

图片分析界面状态的枚举值。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INITIAL | 0 | 初始化状态。 |
| AI_BUTTON_SELECTED | 1 | AIButton选中状态。 |
| TEXT_SELECTED | 2 | 文字选中状态。 |
| SUBJECT_SELECTED | 3 | 主体选中状态。 |
| OBJECT_SEARCH | 4 | 视觉搜索状态。 |

**VisionImageAnalyzerController**

这是视觉图像控制器，用于控制交互。继承自[ImageAnalyzerController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageanalyzercontroller12)类。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

**setImageAnalyzerVisibility**

setImageAnalyzerVisibility(visibility: ImageAnalyzerVisibility): void

设置AI识图控件的可见性。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visibility | ImageAnalyzerVisibility | 是 | AI识图控件的可见性。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setImageAnalyzerVisibility(visionImageAnalyzer.ImageAnalyzerVisibility.HIDDEN)
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
          types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
          aiController: this.visionImageAnalyzerController
        })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**setAIButtonPosition**

setAIButtonPosition(position: Rect): void

设置AIButton的位置。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | Rect | 是 | AIButton区域距离AI识图控件四边的位置（vp）。默认展示在右下角 。 当传入部分参数时，优先按照传入的参数匹配，如果位置参数异常，使用默认位置展示。 同时设置top及bottom参数，调setAIButtonPosition接口仅top参数生效。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    let position: visionImageAnalyzer.Rect = {
      bottom: 300
    }
    this.visionImageAnalyzerController.setAIButtonPosition(position)
    this.visionImageAnalyzerController.setAIButtonVisibility(true)
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.6'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**setAIButtonVisibility**

setAIButtonVisibility(visible: boolean): void

设置AIButton的可见性。配置AIButton属性可见后，会对图片进行预分析，当图片中存在文本且文本区域大于图片区域的5%时AIButton才会显示。开启AIButton会触发图片的预分析从而导致一定的功耗开销，建议评估场景，对图片中文本内容较为关注的场景下按需开启，带给消费者良好的图片浏览体验的同时降低不必要的功耗开销。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | AIButton的可见性。true表示可见，false表示不可见。 默认为false，隐藏AIButton。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setAIButtonVisibility(true)
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
          types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
          aiController: this.visionImageAnalyzerController
        })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**setCustomTextMenuItems**

setCustomTextMenuItems(menus: Menu[]): void

设置自定义的文字分析菜单项。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menus | Menu[] | 是 | 选中文字时，支持在文字菜单上增加自定义菜单项，回调中包含当前选中的文字结果。 最多只展示三个，超过三个时取前三个。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.setCustomTextMenuItems([
      {
        value: "menu2",
        action: (param: string | visionImageAnalyzer.Subject[]) => {
          console.info("DEMO_TAG", "text menu clicked")
        }
    ]
    )
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**startSubjectAnalyzer**

startSubjectAnalyzer(): void

开启主体识别，前提需确保当前设备支持主体识别功能。可通过监听 “subjectAnalysis”事件回调获取主体, 注意在等待返回主体时增加超时处理，避免因未识别到主体而一直处于等待状态。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes();
    if (supportTypes.includes(ImageAnalyzerType.SUBJECT)) {
       this.visionImageAnalyzerController.startSubjectAnalyzer()
    }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**setCustomSubjectMenuItems**

setCustomSubjectMenuItems(menus: Menu[]): void

设置自定义的主体分析菜单项。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menus | Menu[] | 是 | 选中主体时，支持在主体菜单上增加自定义菜单项，回调中包含当前选中的主体结果。 最多只展示三个，超过部分取前三个。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setCustomSubjectMenuItems([
      {
        value: "menu2",
        action: (param: string | visionImageAnalyzer.Subject[]) => {
          console.info("DEMO_TAG", "subject menu clicked")
        }
    ]
    )
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**setSelectedSubjects**

setSelectedSubjects(subjectIds: number[]): void

根据主体id列表设置选中的主体。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subjectIds | number[] | 是 | 要选中的主体id列表。通过getSubject获取，只有图片识别结果中包含的主体id才有效。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct SingleImageTest2 {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
      if(subjects.length > 0) {
        this.visionImageAnalyzerController.setSelectedSubjects([subjects[0].id])
      }
    })
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**getSelectedSubjects**

getSelectedSubjects(): Promise<Subject[] | null>

获取当前选中的主体。使用Promise异步回调。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Subject[] | null> | Promise对象，返回当前选中的主体。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  getSelectedSubjects() {
    void this.visionImageAnalyzerController.getSelectedSubjects().then((subjects: visionImageAnalyzer.Subject[] | null) => {
      console.info("DEMO_TAG", `getSelectedSubjects result: ${JSON.stringify(subjects)}`)
    })
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**getSubject**

getSubject(point: visionBase.Point): Promise<Subject | null>

根据点位获取对应位置的主体。使用Promise异步回调。调用此接口前需先调用[startSubjectAnalyzer](#ZH-CN_TOPIC_0000002522242600__startsubjectanalyzer)开启主体识别。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | visionBase.Point | 是 | 相对于图片左上角位置点位（px）。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Subject | null> | Promise对象，point点位所在的主体。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';
import { visionBase } from '@kit.CoreVisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()
  getSelectedSubjects() {
    let searchPoint: visionBase.Point = { x: 100, y: 100 }
    void this.visionImageAnalyzerController.getSubject(searchPoint).then((subjects: visionImageAnalyzer.Subject | null) => {
      console.info("DEMO_TAG", `getSubject result: ${JSON.stringify(subjects)}`)
    })
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**getSubjectsImage**

getSubjectsImage(subjectIds: number[]): Promise<PixelMap | null>

根据主体id获取对应主体组装成的图像。使用Promise异步回调。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subjectIds | number[] | 是 | 主体id列表。通过getSubject获取。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<PixelMap | null> | Promise对象，对应id列表组装成的图片。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  getSubjectsImage() {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
      if(subjects.length > 0) {
        let ids: number[] = [subjects[0].id]
        this.visionImageAnalyzerController.getSubjectsImage(ids).then((image: PixelMap | null) => {
          console.info('Image data obtained successfully: ', image);
        }).catch((error: Error) => {
          console.error('Failed to obtain image data: ', error);
        })
      }
    })
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**getImageAnalyzerUIStatus**

getImageAnalyzerUIStatus(): Promise<ImageAnalyzerUIStatus>

获取当前图片分析UI状态。使用Promise异步回调。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.2(14)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ImageAnalyzerUIStatus> | Promise对象，当前图片分析UI状态。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setAIButtonVisibility(true);
    this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (objectSearchPanelVisibility: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
      this.visionImageAnalyzerController.getImageAnalyzerUIStatus().then((status: visionImageAnalyzer.ImageAnalyzerUIStatus) => {
        console.info('Image data obtained successfully: ', status);
      }).catch((error: Error) => {
        console.error('Failed to obtain image data: ', error);
      })
  }
  build() {
    Stack() {
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('60%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)

      Button('获取当前图片分析UI状态', { stateEffect: true, type: ButtonType.Capsule })
        .width('80%')
        .height(40)
        .onClick(() => {
          this.visionImageAnalyzerController.getImageAnalyzerUIStatus()
            .then((status: visionImageAnalyzer.ImageAnalyzerUIStatus) => {
              console.info('Image data obtained successfully: ', status);
            })
            .catch((error: Error) => {
              console.error('Failed to obtain image data: ', error);
            })
        .id('getImageAnalyzerUIStatus')
        .width('40%')
    }.width('100%').height('100%')
  }
```

**startObjectSearch**

startObjectSearch(): Promise<boolean>

开启视觉搜索。使用Promise异步回调。

系统能力： SystemCapability.AI.VisionImageAnalyzer

设备行为差异： 该接口在PC/2in1上无效果，在其他设备类型中可正常调用。

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回是否开启视觉搜索。true表示开启视觉搜索，false表示关闭视觉搜索。在文字选择或主体识别状态时拉起会返回false。 说明： 视觉搜索若在Swiper容器切换图场景下无法生效，则需要在图片切换的onAnimationStart中置空一下当前选中图片的index，再由onAnimationEnd时将当前选中index置成当前index，以此实现overlay跟随图片变动而变动。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  startObjectSearch() {
    this.visionImageAnalyzerController.startObjectSearch()
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**stopObjectSearch**

stopObjectSearch(): void

关闭视觉搜索功能。 如果当前在视觉搜索交互状态，则不支持关闭。

系统能力： SystemCapability.AI.VisionImageAnalyzer

设备行为差异： 该接口在PC/2in1上无效果，在其他设备类型中可正常调用。

起始版本： 5.0.0(12)

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  stopObjectSearch() {
    this.visionImageAnalyzerController.stopObjectSearch()
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**setSubjectMenuVisibility**

setSubjectMenuVisibility(visible: boolean): void

设置图像分割菜单状态。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.1(13)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 设置图像分割菜单状态。 true：显示图像分割菜单；false：隐藏图像分割菜单。 默认是true。 |

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  setSubjectMenuVisibility(visible: boolean) {
    this.visionImageAnalyzerController.setSubjectMenuVisibility(visible)
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'aiButtonStatusChange')**

on(type: 'aiButtonStatusChange', callback: Callback<AIButtonStatus>): void

监听AIButton展示状态。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"aiButtonStatusChange"。监听AIButton展示状态。 |
| callback | Callback<AIButtonStatus> | 是 | callback回调函数。接收AIButton展示状态。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('aiButtonStatusChange', (aiButtonState: visionImageAnalyzer.AIButtonStatus) => {
      console.info("DEMO_TAG", `aiButtonStatusChange result: ${JSON.stringify(aiButtonState)}`)
    })
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'aiButtonStatusChange')**

off(type: 'aiButtonStatusChange', callback?: Callback<AIButtonStatus>): void

取消监听AIButton展示状态。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"aiButtonStatusChange"。取消监听AIButton展示状态。 |
| callback | Callback<AIButtonStatus> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('aiButtonStatusChange', (aiButtonState: visionImageAnalyzer.AIButtonStatus) => {
      console.info("DEMO_TAG", `aiButtonStatusChange result: ${JSON.stringify(aiButtonState)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('aiButtonStatusChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'imageAnalyzerVisibilityChange')**

on(type: 'imageAnalyzerVisibilityChange', callback: Callback<ImageAnalyzerVisibility>): void

监听AI识图控件可见状态。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"imageAnalyzerVisibilityChange"。监听AI识图控件可见状态。 |
| callback | Callback<ImageAnalyzerVisibility> | 是 | callback回调函数。接收AI识图控件可见状态。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
      console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'imageAnalyzerVisibilityChange')**

off(type: 'imageAnalyzerVisibilityChange', callback?: Callback<ImageAnalyzerVisibility>): void

取消AI识图控件可见状态的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"imageAnalyzerVisibilityChange"。取消AI识图控件可见状态的监听。 |
| callback | Callback<ImageAnalyzerVisibility> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
      console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'textAnalysis')**

on(type: 'textAnalysis', callback: Callback<string>): void

监听文字分析结果。默认在首次长按图片文本时触发文本分析，PC/2in1是在图片首次加载时触发文本分析。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"textAnalysis"。监听文字分析结果。 |
| callback | Callback<string> | 是 | callback回调函数。接收文字分析结果。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
      console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('textAnalysis')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'textAnalysis')**

off(type: 'textAnalysis', callback?: Callback<string>): void

取消文字分析结果的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"textAnalysis"。取消文字分析结果的监听。 |
| callback | Callback<string> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
      console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('textAnalysis')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'selectedTextChange')**

on(type: 'selectedTextChange', callback: Callback<string>): void

监听文字选中结果。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedTextChange"。监听文字选中结果。 |
| callback | Callback<string> | 是 | callback回调函数。接收文字选中结果。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
      console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedTextChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'selectedTextChange')**

off(type: 'selectedTextChange', callback?: Callback<string>): void

取消文字选中结果的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedTextChange"。取消文字选中结果的监听。 |
| callback | Callback<string> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
      console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedTextChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'subjectAnalysis')**

on(type: 'subjectAnalysis', callback: Callback<Subject[]>): void

监听主体分析结果，返回所有主体信息。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"subjectAnalysis"。监听主体分析结果， 返回所有主体信息。 |
| callback | Callback<Subject[]> | 是 | callback回调函数。接收主体分析结果， 返回所有主体信息。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('subjectAnalysis')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'subjectAnalysis')**

off(type: 'subjectAnalysis', callback?: Callback<Subject[]>): void

取消主体分析结果的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"subjectAnalysis"。取消主体分析结果的监听。 |
| callback | Callback<Subject[]> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('subjectAnalysis')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'selectedSubjectsChange')**

on(type: 'selectedSubjectsChange', callback: Callback<Subject[]>): void

监听选中的主体。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedSubjectsChange"。监听选中的主体。 |
| callback | Callback<Subject[]> | 是 | callback回调函数。接收选中的主体信息。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedSubjectsChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'selectedSubjectsChange')**

off(type: 'selectedSubjectsChange', callback?: Callback<Subject[]>): void

取消对选中主体的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedSubjectsChange"。取消对选中主体的监听。 |
| callback | Callback<Subject[]> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedSubjectsChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'objectSearchPanelVisibilityChange')**

on(type: 'objectSearchPanelVisibilityChange', callback: Callback<ObjectSearchPanelVisibility>): void

监听图片搜索事件。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.1(13)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"objectSearchPanelVisibilityChange"。监听图片搜索事件。 |
| callback | Callback<ObjectSearchPanelVisibility> | 是 | callback回调函数。接收图片搜索事件信息。 |

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (status: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
      console.info("DEMO_TAG", `objectSearchPanelVisibilityChange result: ${JSON.stringify(status)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('objectSearchPanelVisibilityChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'objectSearchPanelVisibilityChange')**

off(type: 'objectSearchPanelVisibilityChange', callback?: Callback<ObjectSearchPanelVisibility>): void

取消图片搜索事件的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.1(13)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"objectSearchPanelVisibilityChange"。取消监听图片搜索事件。 |
| callback | Callback<ObjectSearchPanelVisibility> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (status: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
      console.info("DEMO_TAG", `objectSearchPanelVisibilityChange result: ${JSON.stringify(status)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('objectSearchPanelVisibilityChange')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'cursorMoveInText')**

on(type: 'cursorMoveInText', callback: Callback<void>): void

监听光标移入图片内文字区域事件。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveInText"。监听光标移入图片内文字区域事件。 |
| callback | Callback<void> | 是 | callback回调函数。接收光标移入图片内文字区域事件信息。 |

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveInText', () => {
      console.info("DEMO_TAG", `cursorMoveInText on`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveInText')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'cursorMoveInText')**

off(type: 'cursorMoveInText', callback?: Callback<void>): void

取消光标移入图片内文字区域事件的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveInText"。取消监听光标移入图片内文字区域事件。 |
| callback | Callback<void> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveInText', () => {
      console.info("DEMO_TAG", `cursorMoveInText on`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveInText')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'cursorMoveOutText')**

on(type: 'cursorMoveOutText', callback: Callback<void>): void

监听光标移出图片内文字区域事件。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveOutText"。监听光标移出图片内文字区域事件。 |
| callback | Callback<void> | 是 | callback回调函数。接收光标移出图片内文字区域事件信息。 |

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveOutText', () => {
      console.info("DEMO_TAG", `cursorMoveOutText on`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveOutText')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'cursorMoveOutText')**

off(type: 'cursorMoveOutText', callback?: Callback<void>): void

取消光标移出图片内文字区域事件的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveOutText"。取消监听光标移出图片内文字区域事件。 |
| callback | Callback<void> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveOutText', () => {
      console.info("DEMO_TAG", `cursorMoveOutText on`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveOutText')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**on(type: 'analyzerFailed')**

on(type: 'analyzerFailed', callback: ErrorCallback): void

监听AI识图的异常场景。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"analyzerFailed"。监听AI识图异常场景。 |
| callback | ErrorCallback | 是 | callback回调函数。接收AI识图异常场景信息。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1013700002 | The service is abnormal. |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
      console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('analyzerFailed')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```

**off(type: 'analyzerFailed')**

off(type: 'analyzerFailed', callback?: ErrorCallback): void

取消AI识图异常场景的监听。

系统能力： SystemCapability.AI.VisionImageAnalyzer

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"analyzerFailed"。取消AI识图异常场景的监听。 |
| callback | ErrorCallback | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1013700002 | The service is abnormal. |

示例：

```ets
import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
      console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('analyzerFailed')
  }
  build() {
    Stack() {
      // 此处图片需单独配置，添加到src/main/resources/base/media路径下
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
```