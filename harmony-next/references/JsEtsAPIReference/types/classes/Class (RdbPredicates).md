# Class (RdbPredicates)

表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。谓词间支持多语句拼接，拼接时默认使用and()连接。不支持Sendable跨线程传递。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { relationalStore } from '@kit.ArkData';
```

#### constructor

constructor(name: string)

构造函数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明namestring是数据库表名。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
```

#### inDevices

inDevices(devices: Array<string>): RdbPredicates

同步分布式数据库时连接到组网内指定的远程设备。

其中devices通过调用[deviceManager.getAvailableDeviceListSync](../../modules/ohos/@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002529285429__getavailabledevicelistsync)方法得到。

数据库同步时调用Sync接口，需要在入参谓词中调用inDevices接口选择设备。如果不调用inDevices接口即默认连接组网内所有的设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明devicesArray<string>是指定的组网内的远程设备ID。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceIds: Array<string> = [];

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    deviceIds[i] = devices[i].networkId!;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.inDevices(deviceIds);
```

#### inAllDevices

inAllDevices(): RdbPredicates

同步分布式数据库时连接到组网内所有的远程设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.inAllDevices();
```

#### equalTo

equalTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值为value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。value[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中值为"Lisa"的字段
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
```

#### notEqualTo

notEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值不为value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。value[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中值不为"Lisa"的字段
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notEqualTo("NAME", "Lisa");
```

#### beginWrap

beginWrap(): RdbPredicates

向谓词添加左括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回带有左括号的Rdb谓词。

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .beginWrap()
  .equalTo("AGE", 18)
  .or()
  .equalTo("SALARY", 200.5)
  .endWrap();
```

#### endWrap

endWrap(): RdbPredicates

向谓词添加右括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回带有右括号的Rdb谓词。

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .beginWrap()
  .equalTo("AGE", 18)
  .or()
  .equalTo("SALARY", 200.5)
  .endWrap();
```

#### or

or(): RdbPredicates

将或条件添加到谓词中。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回带有或条件的Rdb谓词。

**示例：**

```ets
// 匹配数据表的"NAME"列中值为"Lisa"或"Rose"的字段
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .or()
  .equalTo("NAME", "Rose");
```

#### and

and(): RdbPredicates

向谓词添加和条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回带有和条件的Rdb谓词。

**示例：**

```ets
// 匹配数据表的"NAME"列中值为"Lisa"且"SALARY"列中值为"200.5"的字段
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .and()
  .equalTo("SALARY", 200.5);
```

#### contains

contains(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中包含value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valuestring是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中包含"os"的字段，如"Rose"
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.contains("NAME", "os");
```

#### beginsWith

beginsWith(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中以value开头的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valuestring是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中以"Li"开头的字段，如"Lisa"
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.beginsWith("NAME", "Li");
```

#### endsWith

endsWith(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中以value结尾的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valuestring是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中以"se"结尾的字段，如"Rose"
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.endsWith("NAME", "se");
```

#### isNull

isNull(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.isNull("NAME");
```

#### isNotNull

isNotNull(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值不为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.isNotNull("NAME");
```

#### like

like(field: string, value: string): RdbPredicates

配置模糊查询条件，指定field列的模糊匹配条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valuestring是指定模糊匹配条件，通常配合通配符使用，%表示任意长度任意字符，_表示单个字符。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 查询NAME列中包含"os"子串的数据，例如会匹配"Rose"。
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.like("NAME", "%os%");
```

#### glob

glob(field: string, value: string): RdbPredicates

配置谓词匹配数据字段为string的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valuestring是

指示要与谓词匹配的值。

支持通配符，*表示0个、1个或多个数字或字符，?表示1个数字或字符。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中类型为string且值为"?h*g"的字段
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.glob("NAME", "?h*g");
```

#### between

between(field: string, low: ValueType, high: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值在给定范围内的字段（包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。low[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示与谓词匹配的最小值。high[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示与谓词匹配的最大值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"AGE"列中大于等于10且小于等于50的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.between("AGE", 10, 50);
```

#### notBetween

notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值超出给定范围的字段（不包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。low[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示与谓词匹配的最小值。high[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示要与谓词匹配的最大值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"AGE"列中小于10或大于50的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notBetween("AGE", 10, 50);
```

#### greaterThan

greaterThan(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值大于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。value[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"AGE"列中大于18的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.greaterThan("AGE", 18);
```

#### lessThan

lessThan(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值小于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。value[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"AGE"列中小于20的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.lessThan("AGE", 20);
```

#### greaterThanOrEqualTo

greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值大于或者等于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。value[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"AGE"列中大于等于18的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.greaterThanOrEqualTo("AGE", 18);
```

#### lessThanOrEqualTo

lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值小于或者等于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。value[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"AGE"列中小于等于20的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.lessThanOrEqualTo("AGE", 20);
```

#### orderByAsc

orderByAsc(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值按升序排序的列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.orderByAsc("NAME");
```

#### orderByDesc

orderByDesc(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值按降序排序的列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.orderByDesc("AGE");
```

#### distinct

distinct(): RdbPredicates

配置谓词以过滤重复记录并仅保留其中一个。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回可用于过滤重复记录的谓词。

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose").distinct(); // 对NAME列值为Rose的结果集去重
```

#### limitAs

limitAs(value: number): RdbPredicates

设置谓词的最大数据记录数量。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明valuenumber是最大数据记录数，取值应为正整数，传入值小于等于0时，不会限制记录数量。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回可用于设置最大数据记录数的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose").limitAs(3);
```

#### offsetAs

offsetAs(rowOffset: number): RdbPredicates

设置谓词查询结果返回的起始位置。需要同步调用limitAs接口指定查询数量，否则将无查询结果。如需查询指定偏移位置后的所有行，limitAs接口入参需小于等于0。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明rowOffsetnumber是指定查询结果的起始位置，默认初始位置为结果集的最前端。当rowOffset为负数时，起始位置为结果集的最前端。当rowOffset超出结果集最后位置时，查询结果为空。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回具有指定返回结果起始位置的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose").limitAs(-1).offsetAs(3);
```

#### groupBy

groupBy(fields: Array<string>): RdbPredicates

配置谓词按指定列分组查询结果。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldsArray<string>是指定分组依赖的列名。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回分组查询列的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.groupBy(["AGE", "NAME"]);
```

#### indexedBy

indexedBy(field: string): RdbPredicates

配置谓词以指定索引列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是索引列的名称。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回具有指定索引列的RdbPredicates。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.indexedBy("SALARY");
```

#### in

in(field: string, value: Array<ValueType>): RdbPredicates

配置谓词条件，表示字段field的值必须在给定的value集合内。

value集合不能为空。如果传入空集，此条件将失效，导致操作针对所有数据（如全量查询、更新或删除）。请在调用前判断value是否为空集，避免误操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valueArray<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>是以ValueType型数组形式指定的要匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"AGE"列中在[18，20]中的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.in("AGE", [18, 20]);
```

#### notIn

notIn(field: string, value: Array<ValueType>): RdbPredicates

将谓词配置为匹配数据字段为ValueType且值超出给定范围的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valueArray<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>是以ValueType数组形式指定的要匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中不在["Lisa", "Rose"]中的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notIn("NAME", ["Lisa", "Rose"]);
```

#### notContains12+

notContains(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中不包含value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valuestring是指示要与谓词匹配的值。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 匹配数据表的"NAME"列中不包含"os"的字段，如列表中的"Lisa"
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notContains("NAME", "os");
```

#### notLike12+

notLike(field: string, value: string): RdbPredicates

配置模糊查询条件，指定field列**不包含**的模糊匹配条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明fieldstring是数据库表中的列名。valuestring是指定**不包含**的模糊匹配条件，通常配合通配符使用，%表示任意长度任意字符，_表示单个字符。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
// 查询NAME列中不包含"os"子串的数据，例如不会匹配"Rose"。
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notLike("NAME", "%os%");
```

#### having20+

having(conditions:string, args?: Array<ValueType>): RdbPredicates

筛选符合条件的分组数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明conditionsstring是用于过滤使用[groupBy](#ZH-CN_TOPIC_0000002529444651__groupby)获得的数据，不能为空且必须与[groupBy](#ZH-CN_TOPIC_0000002529444651__groupby)配合使用。argsArray<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>否条件中使用的参数，用来替换条件语句中的占位符，不传时默认为空数组。

**返回值**：

类型说明[RdbPredicates](Class (RdbPredicates).md)返回与指定字段匹配的谓词。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**14800001Invalid arguments. Possible causes: 1. Parameter is out of valid range; 2. Missing GROUP BY clause.

**示例1：**

```ets
// 传递完整的条件
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.groupBy(["AGE"]);
predicates.having("NAME = zhangsan");
```

**示例2：**

```ets
// 条件中使用占位符替代，args参数传入替换占位符的值
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.groupBy(["AGE"]);
predicates.having("NAME = ?", ["zhangsan"]);
```