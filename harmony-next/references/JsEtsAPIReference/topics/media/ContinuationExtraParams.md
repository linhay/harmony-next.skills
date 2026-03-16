# ContinuationExtraParams

流转管理入口中设备选择模块所需的过滤参数，可以作为[startContinuationDeviceManager](../../modules/ohos/@ohos.continuation.continuationManager (流转_协同管理).md#ZH-CN_TOPIC_0000002497604644__continuationmanagerstartcontinuationdevicemanagerdeprecated)的入参。

本模块首批接口从API version 8开始支持，从API version 22开始不再维护，建议使用[分布式设备管理](../../modules/ohos/@ohos.distributedDeviceManager (设备管理).md)替代。

#### ContinuationExtraParams(deprecated)

表示流转管理入口中设备选择模块所需的过滤参数。

从API version 22开始不再维护，建议使用[devicebasicinfo](../../modules/ohos/@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002529285429__devicebasicinfo)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

名称类型只读可选说明deviceTypeArray<string>否是表示设备类型。targetBundlestring否是表示目标Bundle名称。descriptionstring否是表示设备过滤的描述。filterany否是表示设备过滤的参数。continuationMode[continuationManager.ContinuationMode](../../modules/ohos/@ohos.continuation.continuationManager (流转_协同管理).md#ZH-CN_TOPIC_0000002497604644__continuationmodedeprecated)否是表示协同的模式。authInfoRecord<string, Object>否是表示认证的信息。