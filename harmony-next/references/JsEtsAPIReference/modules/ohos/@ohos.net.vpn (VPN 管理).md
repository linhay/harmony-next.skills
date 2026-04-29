# @ohos.net.vpn (VPN 管理)

本模块是操作系统提供的内置VPN功能，允许用户通过系统的网络设置进行VPN连接，通常提供的功能较少，而且有比较严格的限制。

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { vpn } from '@kit.NetworkKit';
```

#### LinkAddress

type LinkAddress = connection.LinkAddress

获取网络链接信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| connection.LinkAddress | 网络链路信息。 |

#### RouteInfo

type RouteInfo = connection.RouteInfo

获取网络路由信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| connection.RouteInfo | 网络路由信息。 |

#### AbilityContext

type AbilityContext = [_AbilityContext](../../topics/misc/UIAbilityContext.md)

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_AbilityContext](../../topics/misc/UIAbilityContext.md) | 需要保存状态的UIAbility所对应的context，继承自Context，提供UIAbility的相关配置信息以及操作UIAbility和ServiceExtensionAbility的方法。 |