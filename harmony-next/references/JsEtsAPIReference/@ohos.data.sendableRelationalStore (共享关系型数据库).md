# @ohos.data.sendableRelationalStore (共享关系型数据库)

该模块针对关系型数据库（Relational Database，RDB）提供了sendable支持。支持从查询结果集中获取sendable类型ValuesBucket用于并发实例间传递。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 使用场景

在使用[taskpool](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction)进行多线程计算时，因为对跨线程传递的数据类型限制，关系型数据库常规的ValuesBucket、Asset、Assets数据存储容器不能直接用于跨线程传递。

本模块提供了相应的类型转换工具函数，以便在常规数据存储容器和支持跨线程传递的数据存储容器之间进行类型转换，用于跨线程传递。

#### 导入模块

```ets
import { sendableRelationalStore } from '@kit.ArkData';
```

#### sendableRelationalStore.toSendableValuesBucket

toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket

将不能用于跨线程传递的键值对数据，转换为可用于跨线程传递的键值对数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明valuesBucket[NonSendableBucket](#ZH-CN_TOPIC_0000002529284679__nonsendablebucket)是不可跨线程传递的ValuesBucket数据。

**返回值**：

类型说明[ValuesBucket](#ZH-CN_TOPIC_0000002529284679__valuesbucket)可用于跨线程传递的ValuesBucket数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.

**示例：**

```ets
const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const asset2: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const u8 = new Uint8Array([1, 2, 3]);
const valuesBucket: sendableRelationalStore.NonSendableBucket = {
  age: 18,
  name: "hangman",
  salary: 100.5,
  passed: true,
  data1: asset1,
  blobType: u8,
  bigValue: BigInt("15822401018187971961171"),
  data2: [asset1, asset2]
};

const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket(valuesBucket);
```

#### sendableRelationalStore.fromSendableValuesBucket

fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket

将可用于跨线程传递的键值对数据，转换为不能用于跨线程传递的键值对数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明valuesBucket[ValuesBucket](#ZH-CN_TOPIC_0000002529284679__valuesbucket)是可用于跨线程传递的ValuesBucket数据。

**返回值**：

类型说明[NonSendableBucket](#ZH-CN_TOPIC_0000002529284679__nonsendablebucket)不可跨线程传递的ValuesBucket数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.

**示例：**

```ets
const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const asset2: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const u8 = new Uint8Array([1, 2, 3]);

const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket({
  age: 18,
  name: "hangman",
  salary: 100.5,
  passed: true,
  data1: asset1,
  blobType: u8,
  bigValue: BigInt("15822401018187971961171"),
  data2: [asset1, asset2]
});
const nonSendableBucket = sendableRelationalStore.fromSendableValuesBucket(sendableValuesBucket);
```

#### sendableRelationalStore.toSendableAsset

toSendableAsset(asset: NonSendableAsset): Asset

将不可跨线程传递的附件数据，转换为可跨线程传递的附件数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明asset[NonSendableAsset](#ZH-CN_TOPIC_0000002529284679__nonsendablebucket)是不可跨线程传递的Asset数据。

**返回值**：

类型说明[Asset](#ZH-CN_TOPIC_0000002529284679__asset)可跨线程传递的Asset数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.

**示例：**

```ets
const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
```

#### sendableRelationalStore.fromSendableAsset

fromSendableAsset(asset: Asset): NonSendableAsset

将可跨线程传递的附件数据，转换为不可跨线程传递的附件数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明asset[Asset](#ZH-CN_TOPIC_0000002529284679__asset)是可跨线程传递的Asset数据。

**返回值**：

类型说明[NonSendableAsset](#ZH-CN_TOPIC_0000002529284679__nonsendablebucket)不可跨线程传递的Asset数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.

**示例：**

```ets
const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
const normalAsset = sendableRelationalStore.fromSendableAsset(sendableAsset);
```

#### sendableRelationalStore.fromSendableValues20+

fromSendableValues(values: collections.Array<ValueType>): NonSendableValues

将可跨线程传递的数组数据，转换为不可跨线程传递的数组数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明valuescollections.Array<[ValueType](Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>是可跨线程传递的数组数据。

**返回值**：

类型说明[NonSendableValues](#ZH-CN_TOPIC_0000002529284679__nonsendablevalues20)不可跨线程传递的数组数据。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

**错误码ID****错误信息**14800000Inner error.

**示例：**

```ets
import { sendableRelationalStore } from '@kit.ArkData';
import { collections } from '@kit.ArkTS';
const array = new collections.Array<sendableRelationalStore.ValueType>();
array.push("a");
array.push("b");
array.push(1);
array.push(2);
const values = sendableRelationalStore.fromSendableValues(array);
```

#### sendableRelationalStore.toSendableValues20+

toSendableValues(values: NonSendableValues): collections.Array<ValueType>

将不可跨线程传递的数组数据，转换为可跨线程传递的数组数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明values[NonSendableValues](#ZH-CN_TOPIC_0000002529284679__nonsendablevalues20)是不可跨线程传递的数组数据。

**返回值**：

类型说明collections.Array<[ValueType](Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>可跨线程传递的数组数据。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

**错误码ID****错误信息**14800000Inner error.

**示例：**

```ets
import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
const array: relationalStore.ValueType[] = [];
array.push(1);
array.push(2);
array.push("aaaaaa")
const values = sendableRelationalStore.toSendableValues(array);
```

#### Asset

记录资产附件（文件、图片、视频等类型文件）的相关信息。用于支持资产数据跨线程传递，继承自[lang.ISendable](@arkts.lang (ArkTS语言基础能力).md#ZH-CN_TOPIC_0000002497444768__langisendable)。资产类型的相关接口暂不支持Datashare。使用[sendableRelationalStore.toSendableAsset](#ZH-CN_TOPIC_0000002529284679__sendablerelationalstoretosendableasset)方法创建。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明namestring否否资产的名称。uristring否否资产的uri，在系统里的绝对路径。pathstring否否资产在应用沙箱里的路径。createTimestring否否资产被创建出来的时间。modifyTimestring否否资产最后一次被修改的时间。sizestring否否资产占用空间的大小。statusnumber否是资产的状态，取值与[relationalStore.AssetStatus](Enums.md#ZH-CN_TOPIC_0000002497604686__assetstatus10)枚举值保持一致，默认值为relationalStore.AssetStatus.ASSET_NORMAL。

#### Assets

type Assets = collections.Array<Asset>

表示[Asset](#ZH-CN_TOPIC_0000002529284679__asset)类型数据的集合。用于支持Asset数据集合跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

类型说明[collections.Array](Class (Array).md)<[Asset](#ZH-CN_TOPIC_0000002529284679__asset)>用于并发场景的Asset附件数据集合。

#### ValueType

type ValueType = null | number | string | boolean | collections.Uint8Array | Asset | Assets | collections.Float32Array | bigint

用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

类型说明null表示值类型为空。number表示值类型为数字。string表示值类型为字符串。boolean表示值类型为布尔值。[collections.Uint8Array](Class (Uint8Array).md)表示值类型为Uint8类型的数组。[Asset](#ZH-CN_TOPIC_0000002529284679__asset)

表示值类型为附件Asset。

当字段类型是Asset时，在创建表的sql语句中，类型应当为：ASSET。

[Assets](#ZH-CN_TOPIC_0000002529284679__assets)

表示值类型为附件数据集合Assets。

当字段类型是Assets时，在创建表的sql语句中，类型应当为：ASSETS。

[collections.Float32Array](Class (Float32Array).md)

表示值类型为浮点数组。

当字段类型是collections.Float32Array时，在创建表的sql语句中，类型应当为：floatvector(128)。

bigint

表示值类型为任意长度的整数。

当字段类型是bigint时，在创建表的sql语句中，类型应当为：UNLIMITED INT，详见[通过关系型数据库实现数据持久化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-rdb-store)。

**说明：**

bigint类型字段不能比较大小，不适用以下谓词操作：between、notBetween、greaterThan、lessThan、greaterThanOrEqualTo、lessThanOrEqualTo、orderByAsc、orderByDesc。

bigint类型字段的数据写入时，需通过BigInt()方法或在数据尾部添加'n'的方式明确为bigint类型，如'let data = BigInt(1234)'或'let data = 1234n'。

bigint字段如果写入number类型的数据，则查询该数据的返回类型为number，而非bigint。

#### ValuesBucket

type ValuesBucket = collections.Map<string, ValueType>

表示[ValueType](#ZH-CN_TOPIC_0000002529284679__valuetype)数据的键值对存储，用于支持ValueType数据跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

类型说明[collections.Map](Class (Map).md)<string, [ValueType](#ZH-CN_TOPIC_0000002529284679__valuetype)>并发场景的键值对数据存储，其中，键的类型为string，值的类型为ValueType。

#### NonSendableBucket

type NonSendableBucket = relationalStore.ValuesBucket

用于存储键值对的类型。不支持跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

类型说明[relationalStore.ValuesBucket](Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)非并发场景的键值对数据存储。

#### NonSendableValues20+

type NonSendableValues = Array<relationalStore.ValueType>

表示[ValueType](Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)数据数组存储。不支持跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

类型说明Array<[relationalStore.ValueType](Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>非并发场景的数组数据存储，值的类型为ValueType。

#### NonSendableAsset

type NonSendableAsset = relationalStore.Asset

记录资产附件（文件、图片、视频等类型文件）的相关信息。不支持跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

类型说明[relationalStore.Asset](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284677__asset10)非并发场景的资产附件数据存储。

#### 跨线程传递使用示例

调用taskpool执行数据插入时，主线程调用toSendableValuesBucket方法将数据转为跨线程传递类型，传入taskpool处理。

调用taskpool执行数据查询时，调用ResultSet的getSendableRow方法，获取可跨线程传递的数据行返回主线程，主线程中调用fromSendableValuesBucket方法，转为常规ValuesBucket执行后续处理。

```ets
// Index.ets
import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
import { taskpool } from '@kit.ArkTS';

@Concurrent
async function insert(context: Context, dataItem: sendableRelationalStore.ValuesBucket) {
  const CONFIG: relationalStore.StoreConfig = {
    name: "Store.db",
    securityLevel: relationalStore.SecurityLevel.S3,
  };

  let store = await relationalStore.getRdbStore(context, CONFIG);
  console.info(`Get store successfully!`);

  const CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS test (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
    "name TEXT NOT NULL, " +
    "age INTEGER, " +
    "salary REAL, " +
    "blobType BLOB)";
  await store.executeSql(CREATE_TABLE_SQL);
  console.info(`Create table test successfully!`);

  // 数据插入
  const rowId = await store.insertSync("test", dataItem);
  await store.close();
  return rowId;
}

@Concurrent
async function queryByName(context: Context, name: string) {
  const CONFIG: relationalStore.StoreConfig = {
    name: "Store.db",
    securityLevel: relationalStore.SecurityLevel.S3,
  };

  let store = await relationalStore.getRdbStore(context, CONFIG);
  console.info(`Get store successfully!`);

  const predicates = new relationalStore.RdbPredicates("test");
  predicates.equalTo("name", name);

  const resultSet = await store.query(predicates);
  if (resultSet.rowCount > 0 && resultSet.goToFirstRow()) {
    // 获取可用于跨线程传递的ValuesBucket返回查询结果
    return resultSet.getSendableRow();
  }
  return null;
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(async () => {
          let context: Context = this.getUIContext().getHostContext() as Context;

          const item: relationalStore.ValuesBucket = {
            name: "zhangsan",
            age: 20,
            salary: 5000
          }
          // 调用toSendableValuesBucket转换数据，用于跨线程传递。
          const sendableItem = sendableRelationalStore.toSendableValuesBucket(item);
          const insertRowId = await taskpool.execute(insert, context, sendableItem) as number;
          console.info(`Insert data success, row id is: ${insertRowId}`);

          const rowData = await taskpool.execute(queryByName, context, "zhangsan");
          if (rowData) {
            const row =
              sendableRelationalStore.fromSendableValuesBucket(rowData as sendableRelationalStore.ValuesBucket);
            console.info(`Query success, name is ${row['name']}, age is ${row['age']}.`);
          } else {
            console.error(`Query failed.`)
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```