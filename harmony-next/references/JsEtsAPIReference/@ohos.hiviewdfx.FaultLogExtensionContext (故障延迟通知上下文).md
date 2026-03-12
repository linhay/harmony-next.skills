# @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)

FaultLogExtensionContext是[FaultLogExtensionAbility](@ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知).md)的上下文环境，继承自[ExtensionContext](ExtensionContext.md)。

FaultLogExtensionContext模块提供访问[FaultLogExtensionAbility](@ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知).md)的资源的能力，对于扩展的ExtensionAbility，可直接将ExtensionContext作为上下文环境，或者定义一个继承自ExtensionContext的类型作为上下文环境。

- 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。

#### 使用说明

通过FaultLogExtensionAbility子类实例来获取。

```ets
import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onFaultReportReady() {
        let context = this.context; // 获取FaultLogExtensionContext
        console.info('cache dir is ' + context.cacheDir); // 访问context中的成员
    }
}
```

#### FaultLogExtensionContext

FaultLogExtensionContext是[FaultLogExtensionAbility](@ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知).md)的上下文环境。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger