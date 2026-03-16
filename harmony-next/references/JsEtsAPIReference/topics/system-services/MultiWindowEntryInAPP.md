# MultiWindowEntryInAPP

依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：

- 双折叠：展开态。
- 三折叠：双屏态，三屏态的横屏态。
- 平板：横屏态。

对于不支持的设备形态，该组件不可交互，不响应点击事件。

MultiWindowEntryInAPP组件承载单应用多窗口并行逻辑的实现，应用开发者结合本应用业务特点，通过MultiWindowEntryInAPP实现一个应用多个窗口任务并行场景的开发。

**设备行为差异：**该组件在Phone、Tablet设备及上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { MultiWindowEntryInAPP, MultiWindowEntryInAPPParams, MultiWindowEntryInAPPAttribute, MultiWindowEntryInAPPIconOptions, MultiWindowEntryInAPPSubtitleOptions } from '@kit.UIDesignKit';
```

#### 子组件

无

#### 接口

MultiWindowEntryInAPP(params: MultiWindowEntryInAPPParams)

创建应用内多窗组件接口。

**系统能力****：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在Phone、Tablet设备及上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：**6.0.0(20)

参数名

类型

必填

说明

params

[MultiWindowEntryInAPPParams](#section1967092315545)

是

应用内多窗组件参数。

#### MultiWindowEntryInAPPParams

MultiWindowEntryInAPP组件参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在Phone、Tablet设备及上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

want

[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)

否

否

要启动窗口的参数，有以下要求：

1. 必填字段：abilityName, moduleName和bundleName；

2. 应用限制：所有指定的名称（abilityName, moduleName 和bundleName）必须属于当前应用；

3. 跨应用限制：多窗口功能不支持跨应用的能力。

isShowSubtitle

boolean

否

是

是否显示组件文本标题。

true：显示默认文本标题。

false：不显示默认文本标题。

默认值：false。

multiWindowEntryInAPPStyle

[MultiWindowEntryInAPPStyle](#section126113816421)

否

是

组件风格参数。

#### MultiWindowEntryInAPPStyle

MultiWindowEntryInAPP组件风格参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在Phone、Tablet设备及上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

iconOptions

[MultiWindowEntryInAPPIconOptions](#section754554610522)

否

是

组件图标参数。

subtitleOptions

[MultiWindowEntryInAPPSubtitleOptions](#section15788112816535)

否

是

组件文本标题参数。

#### MultiWindowEntryInAPPIconOptions

MultiWindowEntryInAPP组件图标参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在Phone、Tablet设备及上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

iconColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

组件图标颜色。

默认值：$r('sys.color.font_primary')。

iconWeight

number | [FontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontweight) | string

否

是

组件图标粗细。

默认值：400。

 说明：

- number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。
- string类型仅支持number类型取值的字符串形式，例如“400”，以及“Bold”、“Bolder”、“Lighter”、“Regular” 、“Medium”分别对应FontWeight中相应的枚举值。

iconSize

number | string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)

否

是

组件图标尺寸。

默认值：24*24 vp。

 说明：

暂不支持百分比。

backgroundColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

组件背景颜色。

默认值：$r('sys.color.comp_background_tertiary')。

#### MultiWindowEntryInAPPSubtitleOptions

MultiWindowEntryInAPP组件标题文本参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在Phone、Tablet设备及上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

modifier

[TextModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

组件文本标题修改器。

#### 属性

支持大部分[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

width、height、size属性暂不支持百分比。

该组件暂不支持accessibilityDescription、accessibilityText属性。

#### 事件

支持大部分[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

该组件暂不支持onClick事件，如要监听点击请使用onTouch事件。

#### 示例

集成应用内多窗组件，用户点击按钮后可与应用内的其他UIAbility组成分屏或进入全景多窗。

```ets
import {
  MultiWindowEntryInAPP,
  MultiWindowEntryInAPPAttribute,
} from '@kit.UIDesignKit';
import { Want } from '@kit.AbilityKit';
import { TextModifier }  from '@kit.ArkUI';

@Entry
@Component
struct MultiWindowEntryInAPPTest {
  @State textModifier: TextModifier = new TextModifier();
  private want: Want = {
    // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
    bundleName: "com.example.myapplication",
    moduleName: "entry",
    abilityName: "FuncAbility",
  };

  build() {
    Row() {
      MultiWindowEntryInAPP({
        want: this.want, isShowSubtitle: true, multiWindowEntryInAPPStyle: {
          iconOptions: {
            iconSize: 24,
            iconColor: $r('sys.color.font_primary'),
            iconWeight: FontWeight.Normal,
            backgroundColor: $r('sys.color.comp_background_tertiary')
          },
          subtitleOptions: {
            modifier: this.textModifier.fontColor(Color.Black)
          }
        }
      })
        .size({ width: 48, height: 48 })
        .position({ x: 400, y: 30 })
    }
  }
}
```