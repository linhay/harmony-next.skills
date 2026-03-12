# @ohos.data.UdmfComponents(内容卡片)

针对[ContentForm](@ohos.data.uniformDataStruct (标准化数据结构).md#ZH-CN_TOPIC_0000002497604688__contentform14)标准数据结构的内容卡片，支持设置标题（必选）、描述、应用图标、应用名称、跳转链接、内容图片。用户点击卡片时，执行传入的回调事件函数，若设置的跳转链接不为空，则跳转到指定的页面。

该组件从API Version 20开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import { ContentFormCard, FormType } from '@kit.ArkData';
```

#### 子组件

无

#### ContentFormCard

ContentFormCard({contentFormData: uniformDataStruct.ContentForm, formType: FormType, formWidth?: number, formHeight?: number, handleOnClick?: Function})

内容卡片控件，用于在应用内展示标题、描述、内容图片、应用信息等。

**装饰器类型：**@Component

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

名称类型必填装饰器类型说明contentFormData[uniformDataStruct.ContentForm](@ohos.data.uniformDataStruct (标准化数据结构).md#ZH-CN_TOPIC_0000002497604688__contentform14)是-内容卡片数据。formType[FormType](#ZH-CN_TOPIC_0000002497444716__formtype)是@Prop内容卡片类型，影响内容卡片的大小。formWidthnumber否@Prop卡片宽度，其范围在设置的内容卡片类型默认宽度的0.8 ~ 1.2倍之间，当formType为TYPE_SMALL时，其范围在设置的内容卡片类型默认宽度的0.4 ~ 1.2倍之间。formHeightnumber否@Prop卡片高度，当contentFormData中的title为空字符串时，卡片高度为传入的值，否则其范围在设置的内容卡片类型默认宽度的0.8 ~ 1.2倍之间，当formType为TYPE_SMALL时，其范围在设置的内容卡片类型默认宽度的0.4 ~ 1.2倍之间。handleOnClickFunction否-点击事件回调函数。

#### FormType

内容卡片类型枚举，提供了大、中、小三种尺寸。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

名称值说明TYPE_BIG0表示 4 x 4 的尺寸。默认卡片宽度为200，默认高度为200。TYPE_MID1表示 4 x 2 的尺寸。默认卡片宽度为200，默认高度为100。TYPE_SMALL2表示 2 x 1 的尺寸。默认卡片宽度为137， 默认高度为83。

#### 示例

```ets
import { uniformDataStruct } from '@kit.ArkData'

@Entry
@Component
struct Index {
  @State contentForm: uniformDataStruct.ContentForm = {
    uniformDataType: 'general.content-form',
    title: ''
  };
  @State startToShow: boolean = false;

  aboutToAppear(): void {
    this.initData();
  }

  async initData() {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return;
    }
    try {
      let appIcon = await context.resourceManager.getMediaContent($r('app.media.startIcon').id);
      let thumbImage = await context.resourceManager.getMediaContent($r('app.media.foreground').id);
      this.contentForm = {
        uniformDataType: 'general.content-form',
        title: "Content form title",
        thumbData: appIcon,
        description: "Content form description",
        appIcon: thumbImage,
        appName: "com.test.demo"
      };
    } catch (err) {
      console.error("Init data error");
    }
  }

  build() {
    Column() {
      Button('show card')
        .onClick(() => {
          this.startToShow = true;
        })
      if (this.startToShow) {
        ContentFormCard({
          contentFormData: this.contentForm,
          formType: FormType.TYPE_SMALL,
          formWidth: 110,
          formHeight: 50,
          handleOnClick: () => {
            console.info("Clicked card");
          }
        })
      }
    }
  }
}
```