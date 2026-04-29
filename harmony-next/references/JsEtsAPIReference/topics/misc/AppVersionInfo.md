# AppVersionInfo

应用版本信息，可以通过[getAppVersionInfo](Context (FA模型的上下文基类).md#ZH-CN_TOPIC_0000002522240552__contextgetappversioninfo7)获取当前应用的版本信息。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

**导入模块**

```ets
import featureAbility from '@ohos.ability.featureAbility';
```

**属性**

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appName | string | 是 | 否 | 应用名称。 |
| versionCode | number | 是 | 否 | 应用版本编码。 |
| versionName | string | 是 | 否 | 应用版本名称。 |