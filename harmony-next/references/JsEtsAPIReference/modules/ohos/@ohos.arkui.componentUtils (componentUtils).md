# @ohos.arkui.componentUtils (componentUtils)

提供获取组件绘制区域坐标和大小的能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](../../types/classes/Class (UIContext).md)说明。

#### 导入模块

```ets
import { componentUtils } from '@kit.ArkUI';
```

#### componentUtils.getRectangleById(deprecated)

getRectangleById(id: string): ComponentInfo

根据组件ID获取组件实例对象，通过组件实例对象将获取的坐标位置和大小同步返回给开发者。

-

从API version 18开始废弃，建议使用[UIContext](../../types/classes/Class (UIContext).md)中的[getComponentUtils](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getcomponentutils)获取[ComponentUtils](../../types/classes/Class (ComponentUtils).md)实例，再通过此实例调用替代方法[getRectangleById](../../types/classes/Class (ComponentUtils).md#ZH-CN_TOPIC_0000002529284767__getrectanglebyid)。

-

从API version 10开始，可以通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getComponentUtils](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getcomponentutils)方法获取当前UI上下文关联的[ComponentUtils](../../types/classes/Class (ComponentUtils).md)对象。在目标组件布局完成后，通过该接口能够获取组件坐标和尺寸信息。建议在[布局回调](@ohos.arkui.inspector (布局回调).md)中使用该接口。如果组件动态创建但未挂树，则无法通过该接口获取正常的组件信息。因为组件在未挂树的情况下，一般未经过UI框架正常的测量与布局，此时请确保组件正常挂树后再尝试获取组件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明idstring是指定组件id。

**返回值：**

类型说明[ComponentInfo](#ZH-CN_TOPIC_0000002529284761__componentinfo)组件大小、位置、平移缩放旋转及仿射矩阵属性信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息100001UI execution context not found.

**示例：**

```ets
import { componentUtils } from '@kit.ArkUI';
let modePosition:componentUtils.ComponentInfo = componentUtils.getRectangleById("onClick");
```

#### ComponentInfo

组件大小、位置、平移缩放旋转及仿射矩阵属性信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明size[Size](#ZH-CN_TOPIC_0000002529284761__size)否否组件大小。localOffset[Offset](#ZH-CN_TOPIC_0000002529284761__offset)否否组件相对于父组件信息。windowOffset[Offset](#ZH-CN_TOPIC_0000002529284761__offset)否否组件相对于窗口信息。screenOffset[Offset](#ZH-CN_TOPIC_0000002529284761__offset)否否组件相对于屏幕信息。translate[TranslateResult](#ZH-CN_TOPIC_0000002529284761__translateresult)否否组件平移信息。scale[ScaleResult](#ZH-CN_TOPIC_0000002529284761__scaleresult)否否组件缩放信息。rotate[RotateResult](#ZH-CN_TOPIC_0000002529284761__rotateresult)否否组件旋转信息。transform[Matrix4Result](#ZH-CN_TOPIC_0000002529284761__matrix4result)否否仿射矩阵信息，根据入参创建的四阶矩阵对象。

#### Size

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明widthnumber否否

组件宽度。

单位: px

heightnumber否否

组件高度。

单位: px

#### Offset

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否否

x点坐标。

单位: px

ynumber否否

y点坐标。

单位: px

#### TranslateResult

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否否

x轴平移距离。

单位: px

ynumber否否

y轴平移距离。

单位: px

znumber否否

z轴平移距离。

单位: px

#### ScaleResult

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否否

x轴缩放倍数。

单位: px

ynumber否否

y轴缩放倍数。

单位: px

znumber否否

z轴缩放倍数。

单位: px

centerXnumber否否

变换中心点x轴坐标。

单位: px

centerYnumber否否

变换中心点y轴坐标。

单位: px

#### RotateResult

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否否

旋转轴向量x坐标。

单位: px

ynumber否否

旋转轴向量y坐标。

单位: px

znumber否否

旋转轴向量z坐标。

单位: px

anglenumber否否

旋转角度。

单位: px

centerXnumber否否

变换中心点x轴坐标。

单位: px

centerYnumber否否

变换中心点y轴坐标。

单位: px

#### Matrix4Result

type Matrix4Result = [number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number]

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明

[number,number,number,number,

number,number,number,number,

number,number,number,number,

number,number,number,number]

取值范围为长度为16（4*4）的number数组， 详情见四阶矩阵说明。

单位: px

**四阶矩阵说明：**

参数名类型必填说明m00number是x轴缩放值，单位矩阵默认为1。m01number是第2个值，xyz轴旋转会影响这个值。m02number是第3个值，xyz轴旋转会影响这个值。m03number是无实际意义。m10number是第5个值，xyz轴旋转会影响这个值。m11number是y轴缩放值，单位矩阵默认为1。m12number是第7个值，xyz轴旋转会影响这个值。m13number是无实际意义。m20number是第9个值，xyz轴旋转会影响这个值。m21number是第10个值，xyz轴旋转会影响这个值。m22number是z轴缩放值，单位矩阵默认为1。m23number是无实际意义。m30number是x轴平移值，单位px，单位矩阵默认为0。m31number是y轴平移值，单位px，单位矩阵默认为0。m32number是z轴平移值，单位px，单位矩阵默认为0。m33number是齐次坐标下生效，产生透视投影效果。

**示例：**

推荐通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[getComponentUtils](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getcomponentutils)方法获取当前UI上下文关联的ComponentUtils对象。

```ets
import { matrix4, componentUtils } from '@kit.ArkUI';

@Entry
@Component
struct Utils {
  @State x: number = 120;
  @State y: number = 10;
  @State z: number = 100;
  @State value: string = '';
  private matrix1 = matrix4.identity().translate({ x: this.x, y: this.y, z: this.z });

  build() {
    Column() {
      // $r("app.media.img")需要替换为开发者所需的图像资源文件
      Image($r("app.media.img"))
        .transform(this.matrix1)
        .translate({ x: 20, y: 20, z: 20 })
        .scale({ x: 0.5, y: 0.5, z: 1 })
        .rotate({
          x: 1,
          y: 1,
          z: 1,
          centerX: '50%',
          centerY: '50%',
          angle: 300
        })
        .width(300)
        .height(100)
        .key("image_01")
      Button('getRectangleById')
      .onClick(() => {
        this.value = JSON.stringify(this.getUIContext().getComponentUtils().getRectangleById("image_01")) // 建议使用this.getUIContext().getComponentUtils()接口
      }).margin(10).id('onClick')
      Text(this.value)
        .margin(20)
        .width(300)
        .height(300)
        .borderWidth(2)
    }.margin({left: 50})
  }
}
```