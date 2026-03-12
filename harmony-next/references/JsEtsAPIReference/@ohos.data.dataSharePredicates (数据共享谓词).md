# @ohos.data.dataSharePredicates (数据共享谓词)

**谓词(DataSharePredicates)** 是开发者通过DataShare查询数据库中的数据所使用的筛选条件，经常被应用在更新数据、删除数据和查询数据中。

谓词的接口函数与数据库的筛选条件一一对应，开发者在使用前需了解数据库相关知识。

谓词(DataSharePredicates)的使用场景如下：

- 用于在媒体文件管理服务作为检索条件使用，参考[相册管理模块检索条件](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285945__fetchoptions)。此种场景下，开发者无需关注数据库类型。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { dataSharePredicates } from '@kit.ArkData';
```

#### DataSharePredicates

提供用于不同实现不同查询方法的数据共享谓词。该类型不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

#### equalTo10+

equalTo(field: string, value: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值等于指定值的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明fieldstring是

数据库表中的列名。

field为undefined或者null时，此次调用接口配置的谓词无效。

value[ValueType](@ohos.data.ValuesBucket (数据集).md#ZH-CN_TOPIC_0000002529284681__valuetype)是

指示要与谓词匹配的值。

value为undefined或者null时，此次调用接口配置的谓词无效。

**返回值：**

类型说明[DataSharePredicates](#ZH-CN_TOPIC_0000002529444645__datasharepredicates)返回与指定字段匹配的谓词。

**示例：**

```ets
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose");
```

#### and10+

and(): DataSharePredicates

该接口用于将和条件添加到谓词中。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**返回值：**

类型说明[DataSharePredicates](#ZH-CN_TOPIC_0000002529444645__datasharepredicates)返回带有和条件的谓词。

**示例：**

```ets
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "lisi")
    .and()
    .equalTo("SALARY", 200.5);
```

#### orderByAsc10+

orderByAsc(field: string): DataSharePredicates

该接口用于配置谓词以匹配其值按升序排序的列。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明fieldstring是

数据库表中的列名。

field为undefined或者null时，此次调用接口配置的谓词无效。

**返回值：**

类型说明[DataSharePredicates](#ZH-CN_TOPIC_0000002529444645__datasharepredicates)返回与指定字段匹配的谓词。

**示例：**

```ets
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByAsc("AGE");
```

#### orderByDesc10+

orderByDesc(field: string): DataSharePredicates

该接口用于配置谓词以匹配其值按降序排序的列。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明fieldstring是

数据库表中的列名。

field为undefined或者null时，此次调用接口配置的谓词无效。

**返回值：**

类型说明[DataSharePredicates](#ZH-CN_TOPIC_0000002529444645__datasharepredicates)返回与指定字段匹配的谓词。

**示例：**

```ets
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByDesc("AGE");
```

#### limit10+

limit(total: number, offset: number): DataSharePredicates

该接口用于配置谓词以指定结果数和起始位置。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明totalnumber是

最大数据记录数。

当使用键值型数据库且total为undefined或null时，会限制最大记录数为0。

当使用关系型数据库且total为undefined或null时，不会限制最大记录数。

当使用键值型数据库时，取值范围参考[键值型数据库limit接口](@ohos.data.distributedKVStore (分布式键值数据库).md#ZH-CN_TOPIC_0000002497444702__limit)中的total参数说明。

当使用关系型数据库时，取值范围参考[关系型数据库limitAs接口](Class (RdbPredicates).md#ZH-CN_TOPIC_0000002529444651__limitas)中的value参数说明。

offsetnumber是

指定查询结果的起始位置。

当offset为undefined或null时，起始位置为结果集的最前端。

当使用键值型数据库时，取值范围参考[键值型数据库limit接口](@ohos.data.distributedKVStore (分布式键值数据库).md#ZH-CN_TOPIC_0000002497444702__limit)中的offset参数说明。

当使用关系型数据库时，取值范围参考[关系型数据库offsetAs接口](Class (RdbPredicates).md#ZH-CN_TOPIC_0000002529444651__offsetas)中的rowOffset参数说明。

**返回值：**

类型说明[DataSharePredicates](#ZH-CN_TOPIC_0000002529444645__datasharepredicates)返回与指定字段匹配的谓词。

**示例：**

```ets
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose").limit(10, 3);
```

#### in10+

in(field: string, value: Array<ValueType>): DataSharePredicates

该接口用于配置谓词以匹配值在指定范围内的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明fieldstring是

数据库表中的列名。

field为undefined或者null时，此次调用接口配置的谓词无效。

valueArray<[ValueType](@ohos.data.ValuesBucket (数据集).md#ZH-CN_TOPIC_0000002529284681__valuetype)>是以ValueType型数组形式指定的要匹配的值。

**返回值：**

类型说明[DataSharePredicates](#ZH-CN_TOPIC_0000002529444645__datasharepredicates)返回与指定字段匹配的谓词。

**示例：**

```ets
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.in("AGE", [18, 20]);
```