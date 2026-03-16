# AbilityDelegatorArgs

AbilityDelegatorArgs模块提供在应用程序执行测试用例期间，获取测试用例参数AbilityDelegatorArgs对象的能力。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)中使用。

#### 导入模块

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

#### 使用说明

通过AbilityDelegatorRegistry中[getArguments](../../modules/ohos/@ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry).md#ZH-CN_TOPIC_0000002497605688__abilitydelegatorregistrygetarguments)方法获取。

#### AbilityDelegatorArgs

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明bundleNamestring否否当前被测试应用的包名。parametersRecord<string, string>否否当前启动单元测试的参数。testCaseNamesstring否否测试用例名称。testRunnerClassNamestring否否执行测试用例的测试执行器名称。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let args: abilityDelegatorRegistry.AbilityDelegatorArgs = abilityDelegatorRegistry.getArguments();
```