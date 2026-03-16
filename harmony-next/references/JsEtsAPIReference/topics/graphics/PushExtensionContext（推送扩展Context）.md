# PushExtensionContext（推送扩展Context）

PushExtensionContext是[PushExtensionAbility](../system-services/PushExtensionAbility（推送扩展Ability）.md)的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**起始版本：**4.0.0(10)

#### 导入模块

```ets
import { PushExtensionContext } from '@kit.PushKit';
```

#### PushExtensionContext

**模型约束：**属性仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：**4.0.0(10)

本类继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)，未新增内容。