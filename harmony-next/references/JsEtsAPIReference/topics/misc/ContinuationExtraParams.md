# ContinuationExtraParams

流转管理入口中设备选择模块所需的过滤参数，可以作为[startContinuationDeviceManager](@ohos.continuation.continuationManager (流转_协同管理).md#ZH-CN_TOPIC_0000002522080546__continuationmanagerstartcontinuationdevicemanagerdeprecated)的入参。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](@ohos.distributedDeviceManager (设备管理).md)替代。

本模块接口仅可在Stage模型下使用。

**ContinuationExtraParams(deprecated)**

表示流转管理入口中设备选择模块所需的过滤参数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 22开始废弃，建议使用[devicebasicinfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)代替。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

模型约束：此接口仅可在Stage模型下使用。

系统能力：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceType | Array<string> | 否 | 是 | 表示设备类型。 |
| targetBundle | string | 否 | 是 | 表示目标Bundle名称。 |
| description | string | 否 | 是 | 表示设备过滤的描述。 |
| filter | any | 否 | 是 | 表示设备过滤的参数。 |
| continuationMode | continuationManager.ContinuationMode | 否 | 是 | 表示协同的模式。 |
| authInfo | Record<string, Object> | 否 | 是 | 表示认证的信息。 |