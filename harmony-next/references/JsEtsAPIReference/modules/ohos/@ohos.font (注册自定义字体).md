# @ohos.font (注册自定义字体)

本模块提供注册自定义字体。

-

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](../../types/classes/Class (UIContext).md)说明。

-

推荐使用字体引擎的[loadFontSync](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__loadfontsync)接口注册自定义字体。

#### 导入模块

```ets
import { font } from '@kit.ArkUI';
```

#### font.registerFont(deprecated)

registerFont(options: FontOptions): void

在字体管理中注册自定义字体。

该接口为异步接口，不支持并发调用。

-

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)获取[Font](../../types/classes/Class (Font).md)实例，再通过此实例调用替代方法[registerFont](../../types/classes/Class (Font).md#ZH-CN_TOPIC_0000002497604778__registerfont)。

-

从API version 10开始，可以通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)方法获取当前UI上下文关联的[Font](../../types/classes/Class (Font).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[FontOptions](#ZH-CN_TOPIC_0000002497444810__fontoptions)是注册的自定义字体信息。

#### FontOptions

注册的自定义字体信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明familyNamestring | [Resource](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)10+否否设置注册的字体名称。familySrcstring | [Resource](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)10+否否

设置注册字体文件的路径。

**说明：**

读取系统沙箱路径内的资源时，建议使用file://路径前缀的字符串，需要确保沙箱目录路径下的文件存在并且有可读权限。

直接使用font可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，推荐通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)方法获取当前UI上下文关联的[Font](../../types/classes/Class (Font).md)对象。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct FontExample {
  @State message: string = 'Hello World';
  // iconFont示例，假设0000为指定icon的Unicode，实际需要开发者从注册的iconFont的ttf文件里面获取Unicode
  @State unicode: string = '\u0000';
  @State codePoint: string = String.fromCharCode(0x0000);
  private uiContext: UIContext = this.getUIContext();

  aboutToAppear() {
    // familyName和familySrc都支持系统Resource
    this.uiContext.getFont().registerFont({
      // 建议使用 this.getUIContext().getFont().registerFont()接口
      // 'app.string.font_name'和'app.string.font_src'仅作示例，请替换为实际使用资源字符串
      familyName: $r('app.string.font_name'),
      familySrc: $r('app.string.font_src')
    })

    // familySrc支持RawFile
    this.uiContext.getFont().registerFont({
      familyName: 'mediumRawFile',
      familySrc: $rawfile('font/medium.ttf')// 'font/medium.ttf'仅作示例，请替换为实际使用资源字体文件
    })

    // 注册iconFont
    this.uiContext.getFont().registerFont({
      familyName: 'iconFont',
      familySrc: '/font/iconFont.ttf'
    })

    // familyName和familySrc都支持string
    this.uiContext.getFont().registerFont({
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

      // 使用iconFont的两种方式
      Text(this.unicode)
        .align(Alignment.Center)
        .fontSize(20)
        .fontFamily('iconFont')
      Text(this.codePoint)
        .align(Alignment.Center)
        .fontSize(20)
        .fontFamily('iconFont')
    }.width('100%')
  }
}
```

应用若需全局使用自定义字体，请在EntryAbility.ets文件的[onWindowStageCreate](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onwindowstagecreate)生命周期中，通过[windowStage.loadContent](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__loadcontent9)回调注册。

在HSP工程中，不推荐采用相对路径的方式注册自定义字体，详见[通过$r访问HSP中的资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/in-app-hsp)。

#### font.getSystemFontList(deprecated)

getSystemFontList(): Array<string>

获取风格字体列表。

该接口仅在PC/2in1设备上生效，在其他设备上返回空数组。

推荐使用[getSystemFontFullNamesByType](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__textgetsystemfontfullnamesbytype14)接口获取系统最新支持的字体列表数据。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)获取[Font](../../types/classes/Class (Font).md)实例，再通过此实例调用替代方法[getSystemFontList](../../types/classes/Class (Font).md#ZH-CN_TOPIC_0000002497604778__getsystemfontlist)。

从API version 10开始，可以通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)方法获取当前UI上下文关联的[Font](../../types/classes/Class (Font).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array<string>系统的字体名列表。

直接使用font可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，推荐通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)方法获取当前UI上下文关联的[Font](../../types/classes/Class (Font).md)对象。

**示例：**

```ets
// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  fontList: Array<string> = new Array<string>();

  build() {
    Column() {
      Button("getSystemFontList")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontList = font.getSystemFontList(); // 建议使用 this.getUIContext().getFont().getSystemFontList()接口
        })
    }.width('100%')
  }
}
```

#### font.getFontByName(deprecated)

getFontByName(fontName: string): FontInfo

根据传入的系统字体名称获取系统字体的相关信息。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)获取[Font](../../types/classes/Class (Font).md)实例，再通过此实例调用替代方法[getFontByName](../../types/classes/Class (Font).md#ZH-CN_TOPIC_0000002497604778__getfontbyname)。

从API version 10开始，可以通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)方法获取当前UI上下文关联的[Font](../../types/classes/Class (Font).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fontNamestring是系统的字体名。

**返回值：**

类型说明FontInfo字体的详细信息。

#### FontInfo10+

字体的详细信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明pathstring否否系统字体的文件路径。postScriptNamestring否否系统字体的postScript名称。fullNamestring否否系统字体的名称。familystring否否系统字体的字体家族。subfamilystring否否系统字体的子字体家族。weightnumber否否

系统字体的字重。

取值范围：[100,900]，取值间隔为100，分别对应[FontWeight](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__fontweight)枚举中的值。

默认值：100

widthnumber否否

系统字体的宽度。

取值范围：[1,9]，取值间隔为1，分别对应[FontWidth](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__fontwidth)枚举中的值。

italicboolean否否

系统字体是否倾斜。

默认值：false

值为true，表示斜体字体，值为false，表示非斜体字体。

monoSpaceboolean否否

系统字体是否等宽。

默认值：false

值为true，表示等宽字体，值为false，表示非等宽字体。

symbolicboolean否否

系统字体是否支持符号字体。

默认值：false

值为true，表示支持符号字体，值为false，表示不支持符号字体。

**示例：**

直接使用font可能导致实例不明确的问题，推荐通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getFont](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getfont)方法获取当前UI上下文关联的[Font](../../types/classes/Class (Font).md)对象。

```ets
// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  fontList: Array<string> = new Array<string>();
  uiFont = this.getUIContext().getFont();
  fontInfo: font.FontInfo = this.uiFont.getFontByName(''); // 建议使用 this.getUIContext().getFont().getFontByName()接口

  build() {
    Column() {
      Button("getFontByName")
        .onClick(() => {
          this.fontInfo =
            this.uiFont.getFontByName('HarmonyOS Sans Italic');
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

#### font.getUIFontConfig11+

getUIFontConfig() : UIFontConfig

获取系统的UI字体配置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[UIFontConfig](#ZH-CN_TOPIC_0000002497444810__uifontconfig11)系统的UI字体配置信息。

#### UIFontConfig11+

系统的UI字体配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明fontDirArray<string>否否系统字体文件所在的路径。genericArray<[UIFontGenericInfo](#ZH-CN_TOPIC_0000002497444810__uifontgenericinfo11)>否否系统所支持的通用字体集列表。fallbackGroupsArray<[UIFontFallbackGroupInfo](#ZH-CN_TOPIC_0000002497444810__uifontfallbackgroupinfo11)>否否备用字体集。

#### UIFontGenericInfo11+

系统所支持的通用字体集列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明familystring否否字体集名，字体文件中指定的"family"值。aliasArray<[UIFontAliasInfo](#ZH-CN_TOPIC_0000002497444810__uifontaliasinfo11)>否否别名列表。adjustArray<[UIFontAdjustInfo](#ZH-CN_TOPIC_0000002497444810__uifontadjustinfo11)>否否字体原本的weight值对应需显示的值。

#### UIFontFallbackGroupInfo11+

备用字体集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明fontSetNamestring否否备用字体集所对应的字体集名称。fallbackArray<[UIFontFallbackInfo](#ZH-CN_TOPIC_0000002497444810__uifontfallbackinfo11)>否否表示以下列表为该字体集的备用字体，如果fontSetName为""，表示可以作为所有字体集的备用字体。

#### UIFontAliasInfo11+

别名列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明namestring否否别名名称。weightnumber否否

当weight>0时表示此字体集只包含所指定weight的字体，当weight=0时，表示此字体集包含所有字体。

可返回的值有0、100、400、700、900。

#### UIFontAdjustInfo11+

字体原本的weight值和显示实际值的映射列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明weightnumber否否

字体原本的weight值。

可返回的值有50、80、100、200。

tonumber否否

字体在应用中显示的weight值。

可返回的值有100、400、700、900。

#### UIFontFallbackInfo11+

该字体集的备用字体。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明languagestring否否字体集所支持的语言类型，语言格式为bcp47。familystring否否字体集名，字体文件中指定的"family"值。

**示例：**

```ets
// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  build() {
    Column() {
      Button("getUIFontConfig")
        .width('60%')
        .height('6%')
        .margin(50)
        .onClick(() => {
          let fontConfig = font.getUIFontConfig();
          console.info("font-dir -----------" + String(fontConfig.fontDir.length));
          for (let i = 0; i < fontConfig.fontDir.length; i++) {
            console.info(fontConfig.fontDir[i]);
          }
          console.info("generic-------------" + String(fontConfig.generic.length));
          for (let i = 0; i < fontConfig.generic.length; i++) {
            console.info("family:" + fontConfig.generic[i].family);
            for (let j = 0; j < fontConfig.generic[i].alias.length; j++) {
              console.info(fontConfig.generic[i].alias[j].name + " " + fontConfig.generic[i].alias[j].weight);
            }
            for (let j = 0; j < fontConfig.generic[i].adjust.length; j++) {
              console.info(fontConfig.generic[i].adjust[j].weight + " " + fontConfig.generic[i].adjust[j].to);
            }
          }
          console.info("fallback------------" + String(fontConfig.fallbackGroups.length));
          for (let i = 0; i < fontConfig.fallbackGroups.length; i++) {
            console.info("fontSetName:" + fontConfig.fallbackGroups[i].fontSetName);
            for (let j = 0; j < fontConfig.fallbackGroups[i].fallback.length; j++) {
              console.info("language:" + fontConfig.fallbackGroups[i].fallback[j].language + " family:" +
              fontConfig.fallbackGroups[i].fallback[j].family);
            }
          }
        })
    }.width('100%')
  }
}
```