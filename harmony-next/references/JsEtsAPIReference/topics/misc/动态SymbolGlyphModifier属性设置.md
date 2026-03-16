# 动态SymbolGlyphModifier属性设置

开发者可使用SymbolGlyphModifier构建组件并配置属性，通过此SymbolGlyphModifier可调用所封装组件的属性和样式接口。

 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### SymbolGlyphModifier

定义SymbolGlyphModifier。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor

constructor(src?: Resource)

SymbolGlyphModifier的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明src[Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否资源信息。

#### applyNormalAttribute

applyNormalAttribute?(instance: SymbolGlyphAttribute): void

组件普通状态时的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明instance[SymbolGlyphAttribute](SymbolGlyph.md)是动态设置SymbolGlyph组件的属性。

#### 示例

该示例通过[SymbolGlyphModifier](#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier)和TextInput组件的[cancelButton](../graphics/TextInput.md#ZH-CN_TOPIC_0000002529444859__cancelbutton18)属性展示了自定义右侧symbol类型清除按钮样式的效果。

```ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State text: string = '';
  symbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .height(50)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolModifier // 从API version 18开始支持symbol类型
        })
    }.margin(10)
  }
}
```