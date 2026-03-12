# AbilityInfo

Ability信息，可以通过[bundleManager.getBundleInfoForSelf](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)获取Ability信息，其中参数[bundleFlags](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundleflag)至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ABILITY。

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

#### AbilityInfo

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明bundleNamestring是否

应用Bundle名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

moduleNamestring是否

Ability所属的模块名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

namestring是否

Ability名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

labelstring是否

Ability对用户显示的名称的资源描述符，对应[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中abilities下配置的label字段。

**说明：** 从API version 20开始，如果是通过[bundleManager.getAbilityInfo](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetabilityinfo20)获取Ability信息，该字段为Ability对用户显示的名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

labelIdnumber是否

Ability的标签资源id，是编译构建时根据应用配置abilities下的label自动生成的资源id。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

descriptionstring是否

Ability的描述，对应[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中abilities下配置的description字段，用于描述当前ability提供的页面内容和功能作用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

descriptionIdnumber是否

Ability的描述资源id，是编译构建时根据应用配置abilities下的description自动生成的资源id。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

iconstring是否

Ability的图标资源描述符，对应[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中abilities下配置的icon字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

iconIdnumber是否

Ability的图标资源id，是编译构建时根据应用配置abilities下的icon自动生成的资源id。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

processstring是否

Ability的进程名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

exportedboolean是否

判断Ability是否可以被其他应用拉起，取值为true表示Ability可以被其他应用拉起，取值为false表示Ability不可以被其他应用拉起。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

type[bundleManager.AbilityType](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__abilitytype)是否

Ability类型。

**模型约束：** 此接口仅可在FA模型下使用。

orientation[bundleManager.DisplayOrientation](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__displayorientation)是否

Ability的显示模式。来源于[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中abilities标签下配置的orientation字段，如果module.json5配置文件中orientation配置枚举，orientation属性有值且非0，取值详情参考[显示模式枚举](zh-cn_topic_0000002497444634.md#ZH-CN_TOPIC_0000002497444634__displayorientation)；如果配置文件中配置的是资源索引，orientation属性值为0。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

launchType[bundleManager.LaunchType](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__launchtype)是否

Ability的启动模式，在启动的时候是否以多实例启动，详情参考[启动模式枚举](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__launchtype) 。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

permissionsArray<string>是否

被其他应用拉起/访问时，其他应用需要申请的权限集合，只有当前AbilityInfo的exported为true，即当前Ability可以被其他应用拉起时，才会查看其他应用是否存在拉起/访问的权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

readPermissionstring是否

读取Ability数据所需的权限。

**模型约束：** 此接口仅可在FA模型下使用。

writePermissionstring是否

向Ability写数据所需的权限。

**模型约束：** 此接口仅可在FA模型下使用。

uristring是否

获取Ability的统一资源标识符（URI）。

**模型约束：** 此接口仅可在FA模型下使用。

deviceTypesArray<string>是否

Ability支持的设备类型，来源于modudle.json5配置的[deviceTypes](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#devicetypes标签)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

applicationInfo[ApplicationInfo](ApplicationInfo.md)是否

应用程序的配置信息，通过调用[getBundleInfoForSelf](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_APPLICATION获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

metadataArray<[Metadata](Metadata.md)>是否

Ability的元信息。可以配置成系统定义的参数，使用系统提供的能力，例如[快捷方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#shortcuts标签)、[窗口元数据配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-config-m)等。也可以自定义配置参数，通过调用[getBundleInfoForSelf](zh-cn_topic_0000002497444634.html#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_METADATA获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

enabledboolean是否

Ability是否可用，可用表示可以拉起或者查询，不可用时调用[getAbilityInfo](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetabilityinfo20)查询ability需要携带GET_ABILITY_INFO_WITH_DISABLE的AbilityFlag，取值为true表示Ability可用，取值为false表示Ability不可用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

supportWindowModesArray<[bundleManager.SupportWindowMode](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__supportwindowmode)>是否

Ability支持的窗口模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

windowSize[WindowSize](#ZH-CN_TOPIC_0000002497604632__windowsize)是否

Ability窗口尺寸。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

excludeFromDock12+boolean是否

判断Ability是否可以在dock区域隐藏图标，取值为true表示可以隐藏，取值为false不可以隐藏。

**说明：** 该字段不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

skills12+Array<[Skill](Skill.md)>是否

Ability的Skills信息，标识UIAbility组件或者ExtensionAbility组件能够接收的[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/want-overview)的特征。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

appIndex12+number是否应用包的分身索引标识，仅在[分身应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone)中生效。orientationId14+number是否

Ability的显示模式资源id。来源于[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中abilities标签下的orientation字段，如果module.json5配置文件中orientation配置枚举，orientationId属性值为0；如果配置文件中配置的是资源索引，orientationId属性值为非0，为编译构建时生成的资源id索引。当orientationId不为0时表示当前显示模式为自定义配置，需要使用orientationId去资源管理获取对应的资源，当orientationId为0时表示未配置资源。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

#### WindowSize

描述窗口尺寸。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明maxWindowRationumber是否表示自由窗口状态下窗口的最大宽高比；取值范围0-1，例如：0.12。minWindowRationumber是否表示自由窗口状态下窗口的最小宽高比；取值范围0-1，例如：0.5。maxWindowWidthnumber是否表示自由窗口状态下窗口的最大宽度，宽度单位为vp。minWindowWidthnumber是否表示自由窗口状态下窗口的最小宽度，宽度单位为vp。maxWindowHeightnumber是否表示自由窗口状态下窗口的最大高度，高度单位为vp。minWindowHeightnumber是否表示自由窗口状态下窗口的最小高度，高度单位为vp。