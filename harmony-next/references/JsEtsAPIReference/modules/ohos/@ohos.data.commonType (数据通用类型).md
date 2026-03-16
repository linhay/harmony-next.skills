# @ohos.data.commonType (数据通用类型)

数据通用类型（commonType）是数据管理中通用的数据类型。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { commonType } from '@kit.ArkData';
```

#### AssetStatus

描述资产附件的状态枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

名称值说明ASSET_NORMAL1表示资产状态正常。ASSET_INSERT2表示资产需要插入到云端。ASSET_UPDATE3表示资产需要更新到云端。ASSET_DELETE4表示资产需要在云端删除。ASSET_ABNORMAL5表示资产状态异常。ASSET_DOWNLOADING6表示资产正在下载到本地设备。

#### Asset

记录资产附件（文件、图片、视频等类型文件）的相关信息，相关示例见[在跨端迁移中使用分布式数据对象迁移数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-sync-of-distributed-data-object#在跨端迁移中使用分布式数据对象迁移数据)的示例代码。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

名称类型只读可选说明namestring否否资产的名称。uristring否否资产的uri，在系统里的绝对路径。pathstring否否资产在应用沙箱里的路径。createTimestring否否资产被创建出来的时间。modifyTimestring否否资产最后一次被修改的时间。sizestring否否资产占用空间的大小。确保在全链路中保持统一、一致的存储格式与取值逻辑。建议所有系统节点均采用标准化处理方式（单位为字节（Byte），取值为非负整数）。status[AssetStatus](#ZH-CN_TOPIC_0000002497604678__assetstatus)否是资产的状态，默认值为ASSET_NORMAL。

#### Assets

type Assets = Array<Asset>

表示[Asset](#ZH-CN_TOPIC_0000002497604678__asset)类型的数组。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

类型说明Array<[Asset](#ZH-CN_TOPIC_0000002497604678__asset)>表示Asset类型的数组。

#### ValueType

type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets

用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

类型说明null表示值类型为空。number表示值类型为数字。string表示值类型为字符串。boolean表示值类型为布尔值。Uint8Array表示值类型为Uint8类型的数组。Asset表示值类型为附件[Asset](#ZH-CN_TOPIC_0000002497604678__asset)。Assets表示值类型为附件数组[Assets](#ZH-CN_TOPIC_0000002497604678__assets)。

#### ValuesBucket

type ValuesBucket = Record<string, ValueType>

用于存储键值对的类型。该类型不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

类型说明Record<string, [ValueType](#ZH-CN_TOPIC_0000002497604678__valuetype)>表示键值对类型。键的类型为string，值的类型为[ValueType](#ZH-CN_TOPIC_0000002497604678__valuetype)。