# ElementName

ElementName信息，通过接口[Context.getElementName](Context (FA模型的上下文基类).md)获取。


本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-ElementName](ElementName.md)替代。

**ElementName(deprecated)**


从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-ElementName](ElementName.md#ZH-CN_TOPIC_0000002522240582__elementname-1)替代。

ElementName信息，标识Ability的基本信息，通过接口[Context.getElementName](Context (FA模型的上下文基类).md)获取。

系统能力： SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 设备id值。 |
| bundleName | string | 否 | 否 | 应用Bundle的名称。 |
| abilityName | string | 否 | 否 | Ability的名称。 |
| uri | string | 否 | 是 | 资源标识符。 |
| shortName | string | 否 | 是 | Ability的短名称。 |