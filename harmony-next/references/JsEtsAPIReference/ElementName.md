# ElementName

应用组件结构体，包含bundleName、moduleName和abilityName等。通常用于组件启动信息[AbilityRunningInfo.ability](AbilityRunningInfo.md)和组件启动回调函数[connectOptions.onConnect](ConnectOptions.md#ZH-CN_TOPIC_0000002497444638__onconnect)中。

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

#### ElementName

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明deviceIdstring否是设备ID。bundleNamestring否否应用Bundle名称。abilityNamestring否否Ability名称。uristring否是资源标识符。shortNamestring否是Ability短名称，以“.”为开头的字符串。moduleNamestring否是Ability所属的HAP的模块名称。