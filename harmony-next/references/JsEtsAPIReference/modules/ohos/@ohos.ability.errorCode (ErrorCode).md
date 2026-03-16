# @ohos.ability.errorCode (ErrorCode)

ErrorCode定义启动Ability时返回的错误码，包括无效的参数、权限拒绝等。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { ErrorCode } from '@kit.AbilityKit';
```

#### ErrorCode

定义启动Ability时返回的错误码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明NO_ERROR0没有异常。INVALID_PARAMETER-1无效的参数。ABILITY_NOT_FOUND-2找不到Ability。PERMISSION_DENY-3权限拒绝。