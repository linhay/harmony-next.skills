# @Env：环境变量

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[@Env开发者指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property)。

#### @Env

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型说明Env[EnvDecorator](#ZH-CN_TOPIC_0000002529284965__envdecorator)环境变量装饰器。

**示例：**

```ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

  build() {}
}
```

#### EnvDecorator

declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator

定义@Env装饰器类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[SystemProperties](@Env：环境变量.md#ZH-CN_TOPIC_0000002529284965__systemproperties)是环境变量属性名。

**返回值：**

类型说明PropertyDecorator属性装饰器。

**错误码：**

详细介绍请参见[@Env错误码](环境变量错误码.md)。

错误码ID错误信息140000Invalid key for @Env

#### SystemProperties

定义环境变量枚举值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明BREAK_POINT'system.arkui.breakpoint'

[@Env](#ZH-CN_TOPIC_0000002529284965__env)变量参数，通过@Env(SystemProperties.BREAK_POINT)可获取[WindowSizeLayoutBreakpointInfo](zh-cn_topic_0000002529444737.html#ZH-CN_TOPIC_0000002529444737__windowsizelayoutbreakpointinfo22)实例。

当该装饰器声明在[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)或[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)中时，用于获取当前自定义组件所在窗口的尺寸布局断点信息。