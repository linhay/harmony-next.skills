# @ohos.graphics.uiEffect (效果级联)

本模块提供组件效果的一些基础能力，包括模糊、边缘像素扩展、提亮等。效果被分为Filter和VisualEffect大类，同类效果可以级联在一个效果大类的实例下。在实际开发中，模糊可用于背景虚化，提亮可用于亮屏显示等。

- [Filter](#ZH-CN_TOPIC_0000002497446008__filter)：用于添加指定Filter效果到组件上。
- [VisualEffect](#ZH-CN_TOPIC_0000002497446008__visualeffect)：用于添加指定VisualEffect效果到组件上。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { uiEffect } from "@kit.ArkGraphics2D";
```

#### uiEffect.createFilter

createFilter(): Filter

创建Filter实例用于给组件添加多种filter效果。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[Filter](#ZH-CN_TOPIC_0000002497446008__filter)返回Filter的头节点。

**示例：**

```ets
let filter : uiEffect.Filter = uiEffect.createFilter()
```

#### uiEffect.createEffect

createEffect(): VisualEffect

创建VisualEffect实例用于给组件添加多种effect效果。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[VisualEffect](#ZH-CN_TOPIC_0000002497446008__visualeffect)返回VisualEffect的头节点。

**示例：**

```ets
let visualEffect : uiEffect.VisualEffect = uiEffect.createEffect()
```

#### Filter

Filter效果类，用于将相应的效果添加到指定的组件上。在调用Filter的方法前，需要先通过[createFilter](#ZH-CN_TOPIC_0000002497446008__uieffectcreatefilter)创建一个Filter实例。

#### blur

blur(blurRadius: number): Filter

将模糊效果添加至组件上。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明blurRadiusnumber是

模糊半径。

取值需大于等于0，模糊半径越大，模糊效果越强。

模糊半径为0时无模糊效果。

**返回值：**

类型说明[Filter](#ZH-CN_TOPIC_0000002497446008__filter)返回挂载了模糊效果的Filter。

**示例：**

```ets
// xxx.ts
import { uiEffect } from '@kit.ArkGraphics2D';

let filter: uiEffect.Filter = uiEffect.createFilter();
filter.blur(10);

@Entry
@Component
struct UIEffectFilterExample {
    build(){
        Column({ space: 15 }) {
            Text('UIEffectFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
            Image($r('app.media.foreground'))
                .width(100)
                .height(100)
                .backgroundImage($r('app.media.background'))
                .backgroundImagePosition(Alignment.Center)
                .backgroundImageSize({ width: 90, height: 90 })
                .backgroundFilter(filter)
        }
        .height('100%')
        .width('100%')
    }
}
```

#### VisualEffect

VisualEffect效果类，用于将相应的效果添加到指定的组件上。在调用VisualEffect的方法前，需要先通过[createEffect](#ZH-CN_TOPIC_0000002497446008__uieffectcreateeffect)创建一个VisualEffect实例。