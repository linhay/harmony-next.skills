# Class (CursorController)

提供光标样式设置的能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 12开始支持。

-

以下API需先使用UIContext中的[getCursorController()](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcursorcontroller12)方法获取CursorController实例，再通过此实例调用对应方法。

#### restoreDefault12+

restoreDefault(): void

恢复默认的光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

当光标移出绿框时，通过CursorController的restoreDefault方法恢复默认光标样式。

```ets
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Green).position({x: 150 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.EAST);
          } else {
            console.info("restoreDefault");
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
```

#### setCursor12+

setCursor(value: [PointerStyle](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__pointerstyle12)): void

更改当前的鼠标光标样式。

该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PointerStyle](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__pointerstyle12) | 是 | 光标样式。 |

**示例：**

当光标进入蓝框时，通过CursorController的setCursor方法修改光标样式为[PointerStyle](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__pointerstyle12).WEST。

```ets
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Blue).position({x: 100 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.WEST);
          } else {
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364597.webp)