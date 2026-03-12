# ContinuationResult

流转管理入口返回的设备信息。

本模块首批接口从API version 8开始支持，从API version 22开始不再维护，建议使用[分布式设备管理](@ohos.distributedDeviceManager (设备管理).md)替代。

#### ContinuationResult(deprecated)

ContinuationManager的[on](@ohos.continuation.continuationManager (流转_协同管理).md#ZH-CN_TOPIC_0000002497604644__continuationmanagerondeviceselecteddeprecated)接口返回此对象表示流转管理入口返回的设备信息。

从API version 22开始不再维护，建议使用[devicebasicinfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002529285429__devicebasicinfo)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

名称类型只读可选说明idstring否否表示设备标识。typestring否否表示设备类型。namestring否否表示设备名称。