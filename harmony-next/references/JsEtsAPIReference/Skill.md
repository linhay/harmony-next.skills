# Skill

skill标签对象，可以通过[bundleManager.getBundleInfoForSelf](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)获取skill([BundleInfo](BundleInfo.md)->[HapModuleInfo](HapModuleInfo.md)->[AbilityInfo](AbilityInfo.md)或[ExtensionAbilityInfo](ExtensionAbilityInfo.md)中)信息，其中参数bundleFlags至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_SKILL。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

#### Skill

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明actionsArray<string>是否Skill接收的[Action集合](@ohos.ability.wantConstant (wantConstant).md#ZH-CN_TOPIC_0000002529444607__action)。entitiesArray<string>是否Skill接收的[Entity集合](@ohos.ability.wantConstant (wantConstant).md#ZH-CN_TOPIC_0000002529444607__entity)。urisArray<SkillUri>是否Want匹配的Uri集合。domainVerifyboolean是否Skill接收的DomainVerify值，仅在AbilityInfo中存在，表示是否开启域名校验，取值为true表示开启域名校验，取值为false表示未开启域名校验。

#### SkillUri

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明schemestring是否标识 URI 协议名，常见的有http、https、file、ftp等。hoststring是否标识 URI 主机地址部分，仅当 scheme 存在时才生效。portnumber是否标识 URI 端口，仅当 scheme 和 host 同时存在时才生效。pathstring是否标识 URI 路径部分，仅当 scheme 和 host 同时存在时才生效。pathStartWithstring是否标识 URI 路径部分，用于前缀匹配，仅当 scheme 和 host 同时存在时才生效。pathRegexstring是否标识 URI 路径部分，用于正则匹配，仅当 scheme 和 host 同时存在时才生效。typestring是否标识与Want相匹配的数据类型，使用MIME（Multipurpose Internet Mail Extensions）类型规范和[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md)类型规范。utdstring是否标识与 Want 相匹配的 URI 的标准化数据类型，适用于分享等场景。maxFileSupportednumber是否对于指定类型的文件，标识一次能接收或打开的最大数量。取值范围：不小于0的整数。linkFeaturestring是否标识 URI 提供的[功能类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-uri-config#linkfeature标签说明)，用于实现应用间跳转，仅在AbilityInfo中存在。