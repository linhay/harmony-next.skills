[]()[]()

# Class (Font)

注册自定义字体的信息。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 10开始支持。

-

以下API需先使用UIContext中的[getFont()](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)方法获取到Font对象，再通过该对象调用对应方法。

-

推荐使用字体引擎的[loadFontSync](../../modules/ohos/@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__loadfontsync)接口注册自定义字体。

[]()[]()

#### registerFont

registerFont(options: font.FontOptions): void

在字体管理中注册自定义字体。

该接口为异步接口，不支持并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[font.FontOptions](../../modules/ohos/@ohos.font (注册自定义字体).md#ZH-CN_TOPIC_0000002497444810__fontoptions)是

注册的自定义字体信息。

**说明：**

设置注册字体文件的路径，读取系统沙箱路径内的资源时，建议使用file://路径前缀的字符串，需要确保沙箱目录路径下的文件存在并且有可读权限。

**示例：**

```ets
// xxx.ets
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();

  aboutToAppear() {
    this.font.registerFont({
      familyName: 'medium',
      familySrc: '/font/medium.ttf' // font文件夹与pages目录同级
    })
  }

  build() {
    Column() {
      Text(this.message)
        .align(Alignment.Center)
        .fontSize(20)
        .fontFamily('medium') // medium：注册自定义字体的名字（$r('app.string.mediumFamilyName')、'mediumRawFile'等已注册字体也能正常使用）
    }.width('100%')
  }
}
```

[]()[]()

#### getSystemFontList

getSystemFontList(): Array<string>

获取系统支持的字体名称列表。

该接口仅在PC/2in1设备上生效，在其他设备上返回空数组。

推荐使用[getSystemFontFullNamesByType](../../modules/ohos/@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__textgetsystemfontfullnamesbytype14)接口获取系统最新支持的字体列表数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array<string>系统的字体名列表。

**示例：**

```ets
// xxx.ets
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();
  fontList: Array<string> = new Array<string>();

  build() {
    Column() {
      Button("getSystemFontList")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontList = this.font.getSystemFontList();
          console.info('getSystemFontList', JSON.stringify(this.fontList))
        })
    }.width('100%')
  }
}
```

[]()[]()

#### getFontByName

getFontByName(fontName: string): font.FontInfo

根据传入的系统字体名称获取系统字体的相关信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fontNamestring是系统的字体名。

**返回值：**

类型说明[font.FontInfo](../../modules/ohos/@ohos.font (注册自定义字体).md#ZH-CN_TOPIC_0000002497444810__fontinfo10)

字体的详细信息。

如果查询不到字体，返回undefined。

**示例：**

```ets
// xxx.ets
import { Font, font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();
  fontInfo: font.FontInfo = this.font.getFontByName('');

  build() {
    Column() {
      Button("getFontByName")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontInfo = this.font.getFontByName('HarmonyOS Sans Italic');
          console.info("getFontByName(): path = " + this.fontInfo.path);
          console.info("getFontByName(): postScriptName = " + this.fontInfo.postScriptName);
          console.info("getFontByName(): fullName = " + this.fontInfo.fullName);
          console.info("getFontByName(): family = " + this.fontInfo.family);
          console.info("getFontByName(): subfamily = " + this.fontInfo.subfamily);
          console.info("getFontByName(): weight = " + this.fontInfo.weight);
          console.info("getFontByName(): width = " + this.fontInfo.width);
          console.info("getFontByName(): italic = " + this.fontInfo.italic);
          console.info("getFontByName(): monoSpace = " + this.fontInfo.monoSpace);
          console.info("getFontByName(): symbolic = " + this.fontInfo.symbolic);
        })
    }.width('100%')
  }
}
```