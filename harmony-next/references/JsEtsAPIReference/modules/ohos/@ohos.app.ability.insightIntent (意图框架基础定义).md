# @ohos.app.ability.insightIntent (意图框架基础定义)

本模块提供[意图框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-overview)基础定义。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { insightIntent } from '@kit.AbilityKit';
```

#### ExecuteMode

意图执行模式。表示系统入口触发意图执行时传递的执行模式，每个意图支持的执行模式在意图开发时定义。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明UI_ABILITY_FOREGROUND0

将UIAbility在前台显示。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

UI_ABILITY_BACKGROUND1

将UIAbility在后台拉起。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

UI_EXTENSION_ABILITY2拉起UIExtensionAbility。

#### ExecuteResult

意图执行的返回结果。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明codenumber否否

意图执行返回的错误码，由开发者定义。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

resultRecord<string, Object>否是

意图执行返回的结果，通常会包含需要返回给系统入口的数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

uris18+Array<string>否是

意图执行返回的URI列表。该字段需要与flags字段配合使用，根据URI列表将flags字段的相应权限授权给系统入口。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

flags18+number否是

意图执行返回给系统入口的URI列表的授权权限。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**说明：**

该参数仅支持FLAG_AUTH_READ_URI_PERMISSION、FLAG_AUTH_WRITE_URI_PERMISSION、FLAG_AUTH_READ_URI_PERMISSION|FLAG_AUTH_WRITE_URI_PERMISSION。权限介绍见[Flags](@ohos.app.ability.wantConstant (Want常量).md#ZH-CN_TOPIC_0000002497604612__flags)。

#### IntentEntity20+

意图实体结构体定义，用于定义意图执行过程中涉及的关键信息对象，包括意图参数和意图执行结果等。

开发者通过继承该类来定义意图实体，继承类需使用[@InsightIntentEntity](@ohos.app.ability.InsightIntentDecorator (意图装饰器定义).md#ZH-CN_TOPIC_0000002497604590__insightintententity)装饰。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明entityIdstring否否

意图实体的ID。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

#### IntentResult<T>20+

意图执行的返回结果，支持[泛型类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts#泛型类和接口)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明codenumber否否

意图执行返回的错误码，由开发者定义。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

resultT否是

意图执行返回的结果，通常会包含需要返回给系统入口的数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。