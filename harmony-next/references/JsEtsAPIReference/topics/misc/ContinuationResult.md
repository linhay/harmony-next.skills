# ContinuationResult

流转管理入口返回的设备信息。


本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](@ohos.distributedDeviceManager (设备管理).md)替代。

本模块接口仅可在Stage模型下使用。

#### ContinuationResult(deprecated)

ContinuationManager的[on](@ohos.continuation.continuationManager (流转_协同管理).md#ZH-CN_TOPIC_0000002522080546__continuationmanagerondeviceselecteddeprecated)接口返回此对象表示流转管理入口返回的设备信息。


从API version 22开始废弃，建议使用[devicebasicinfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示设备标识。 |
| type | string | 否 | 否 | 表示设备类型。 |
| name | string | 否 | 否 | 表示设备名称。 |