# cloudDatabase (云数据库模块)

本模块提供使用云数据库进行数据写入、查询、删除等操作的能力。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
```

#### zone

zone(zone: string): DatabaseZone

通过zone名称初始化云数据库实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

zone

string

是

zone的名称。

**返回值****：**

类型

说明

[DatabaseZone](#section18912210182513)

云数据库处理数据的实例。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';

let databaseZone = cloudDatabase.zone("storageArea");
```

#### DatabaseZone

云数据库处理数据的实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

#### query

query<T extends DatabaseObject>(condition: DatabaseQuery<T>): Promise<T[]>

通过条件查询数据。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

condition

[DatabaseQuery](#section76501736191415)<T>

是

提供丰富的查询条件。

**返回值****：**

类型

说明

Promise<T[]>

Promise对象，返回查询结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
// 在代码工程中创建BookInfo.ets文件
import { cloudDatabase } from '@kit.CloudFoundationKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject
class BookInfo extends cloudDatabase.DatabaseObject{
  public naturalbase_ClassName(): string {
    return 'BookInfo';
  }
  public key_string: string | undefined;
  public key_boolean: boolean | undefined;
  public key_byte: number | undefined;
  public key_short: number | undefined;
  public key_integer: number | undefined;
  public key_long: number | undefined;
  public key_float: number | undefined;
  public key_double: number | undefined;
  public key_text: string | undefined;
  public key_date: Date | undefined;
  public key_byte_array: Uint8Array | undefined;
}

export { BookInfo };
```

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // 在云数据库代码工程中引入BookInfo.ets文件，xx是文件的路径

try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let condition = new cloudDatabase.DatabaseQuery(BookInfo);
  condition.equalTo('key_string', 'string_123');
  let bookInfoArray = await databaseZone.query(condition);
  hilog.info(0x0000, 'testTag', `Succeeded in querying data, result: ${JSON.stringify(bookInfoArray)}`);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query data, code: ${err.code}, message: ${err.message}`);
}
```

#### query

query<T extends DatabaseObject>(condition: DatabaseQuery<T>, callback: AsyncCallback<T[]>): void

通过条件查询数据。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

condition

[DatabaseQuery](#section76501736191415)<T>

是

提供丰富的查询条件。

callback

AsyncCallback<T[]>

是

回调函数。当查询数据成功，err为undefined，data为查询到的结果数组；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('key_string', 'string_123');
databaseZone.query(condition, (err: BusinessError, bookInfoArray) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to query data, code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in querying data, result: ${JSON.stringify(bookInfoArray)}`);
  }
});
```

#### calculateQuery

calculateQuery<T extends DatabaseObject>(condition: DatabaseQuery<T>, fieldName: string, calculate: QueryCalculate): Promise<number>

从数据库中查询符合条件的数据，并对指定字段进行算术计算。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

condition

[DatabaseQuery](#section76501736191415)<T>

是

提供丰富的查询条件。

fieldName

string

是

指定查询对象中要计算的字段名称。

calculate

[QueryCalculate](#section530095545712)

是

云数据库查询算术计算的类型。

**返回值****：**

类型

说明

Promise<number>

Promise对象。返回查询字段名称算术运算结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let condition = new cloudDatabase.DatabaseQuery(BookInfo);
  condition.lessThan('key_integer', 100);
  let count = await databaseZone.calculateQuery(condition, 'key_integer', cloudDatabase.QueryCalculate.AVERAGE);
  hilog.info(0x0000, 'testTag', `Succeeded in calculating queried data, result: ${count}`);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to calculate queried data, code: ${err.code}, message: ${err.message}`);
}
```

#### calculateQuery

calculateQuery<T extends DatabaseObject>(condition: DatabaseQuery<T>, fieldName: string, calculate: QueryCalculate, callback: AsyncCallback<number>): void

从数据库中查询符合条件的数据，并对指定字段进行算术计算。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

condition

[DatabaseQuery](#section76501736191415)<T>

是

提供丰富的查询条件。

fieldName

string

是

指定查询对象中要计算的字段名称。

calculate

[QueryCalculate](#section530095545712)

是

云数据库查询算术计算的类型。

callback

AsyncCallback<number>

是

回调函数。返回查询字段名称算术运算结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key_integer', 100);
databaseZone.calculateQuery(condition, 'key_integer', cloudDatabase.QueryCalculate.AVERAGE,
  (err: BusinessError, num) => {
    if (err) {
      hilog.error(0x0000, 'testTag', `Failed to calculate queried data, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag', `Succeeded in calculating queried data, result: ${num}`);
    }
  });
```

#### upsert

upsert<T extends DatabaseObject>(objectList: T[] | T): Promise<number>

向数据库更新数据。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

objectList

T[] | T

是

一个或多个对象。

**返回值****：**

类型

说明

Promise<number>

Promise对象。返回更新成功的数据数量。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let book = new BookInfo();
  book.key_string = 'string_12';
  book.key_integer = 90;
  let book1 = new BookInfo();
  book1.key_string = 'string_1234';
  book1.key_integer = 101;
  let num = await databaseZone.upsert([book, book1]);
  hilog.info(0x0000, 'testTag', `Succeeded in upserting data, result: ${num}`);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to upsert data, code: ${err.code}, message: ${err.message}`);
}
```

#### upsert

upsert<T extends DatabaseObject>(objectList: T[] | T, callback: AsyncCallback<number>): void

向数据库更新数据。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

objectList

T[] | T

是

一个或多个对象。

callback

AsyncCallback<number>

是

回调函数。返回更新成功的数据数量。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let book = new BookInfo();
book.key_string = 'string_12';
book.key_integer = 90;
let book1 = new BookInfo();
book1.key_string = 'string_1234';
book1.key_integer = 101;
databaseZone.upsert([book, book1], (err: BusinessError, num) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to upsert data, code: ${err.code}, message: ${err.message}`);
  } else {
    hilog.info(0x0000, 'testTag', `Succeeded in upserting data, result: ${num}`);
  }
});
```

#### delete

delete<T extends DatabaseObject>(objectList: T[] | T): Promise<number>

在数据库中删除一条或者多条数据。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

objectList

T[] | T

是

一个或多个对象。

**返回值****：**

类型

说明

Promise<number>

Promise对象。返回删除成功的数据数量。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let condition = new cloudDatabase.DatabaseQuery(BookInfo);
  condition.lessThan('key_integer', 100);
  let bookArray = await databaseZone.query(condition);
  let deleteNum = await databaseZone.delete(bookArray);
  hilog.info(0x0000, 'testTag', `Succeeded in deleting a book, result: ${deleteNum}`);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to delete a book, code: ${err.code}, message: ${err.message}`);
}
```

#### delete

delete<T extends DatabaseObject>(objectList: T[] | T, callback: AsyncCallback<number>): void

在数据库中删除一条或者多条数据。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：**ohos.permission.INTERNET

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

objectList

T[] | T

是

一个或多个对象。

callback

AsyncCallback<number>

是

回调函数。返回删除成功的数据数量。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

201

No Internet permission.

401

Parameter error.

1008230001

Network connection error.

1008230002

Schema config error.

1008230003

Natural object error.

1008230009

Client internal error.

1008231001

Server error.

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key_integer', 100);
try {
  let bookArray = await databaseZone.query(condition);
  databaseZone.delete(bookArray, (err: BusinessError, num) => {
    if (err) {
      hilog.error(0x0000, 'testTag', `Failed to delete a book, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag', `Succeeded in deleting a book, result: ${num}`);
    }
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### DatabaseObject

数据库数据类型基类，在云端生成表结构时继承。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

#### naturalbase_ClassName

naturalbase_ClassName(): string

数据类型基类名称。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**返回值****：**

类型

说明

string

返回数据类型基类名称，需要与创建的对象类型名称一致。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
class BookInfo extends cloudDatabase.DatabaseObject{
  public naturalbase_ClassName(): string {
    return "BookInfo";
  }
}

export { BookInfo };
```

#### FieldType

type FieldType = string | number | boolean | Uint8Array | Date

云数据库支持的数据类型。取值类型为下表类型中的并集/交集。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

类型

说明

string

表示值类型为字符，可取任意值。

number

表示值类型为数字，可取任意值。

boolean

表示值类型为布尔类型，可取true或者false。

Uint8Array

表示值类型为8位无符号整型数组，可取任意值。

Date

表示值类型为日期，值固定格式为“YYYY-MM-DD”。

#### QueryCalculate

枚举， 查询算术计算类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

名称

值

说明

AVERAGE

0

计算平均数。

SUM

1

计算总和。

MAXIMUM

2

计算最大值。

MINIMUM

3

计算最小值。

COUNT

4

计算记录总数。

#### DatabaseQuery

DatabaseQuery<T extends DatabaseObject>

提供丰富的谓词查询来构建查询条件。根据谓词查询方法构造自己的DatabaseQuery对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

#### constructor

constructor(entityClass: new () => T)

构造查询实体类信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

entityClass

new () => T

是

数据对象的实体类。

#### equalTo

equalTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中某个字段的值等于指定值的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('key_string', 'string_123');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### notEqualTo

notEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中某个字段的值不等于指定值的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.notEqualTo('key_string', 'string_123');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### beginsWith

beginsWith(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中string类型字段值以指定子串开头的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.beginsWith('key_string', 'key');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### endsWith

endsWith(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中string类型字段值以指定子串结尾的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.endsWith('key_string', 'string');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### contains

contains(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中字符串类型字段值包含指定子字符串的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.contains('key_string', 'string');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### greaterThan

greaterThan(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值大于指定值的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.greaterThan('key_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### greaterThanOrEqualTo

greaterThanOrEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值大于或等于指定值的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.greaterThanOrEqualTo('key_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### lessThan

lessThan(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值小于指定值的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### lessThanOrEqualTo

lessThanOrEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值小于或等于指定值的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

value

[FieldType](#section15219172491013)

是

云数据库中支持的数据类型的值。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThanOrEqualTo('key_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### in

in(fieldName: string, values: FieldType[]): DatabaseQuery<T>

添加实体类字段值包含在指定数组中的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

values

[FieldType](#section15219172491013)[]

是

云数据库中支持的数据类型的值的数组。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.in('key_integer', [100, 200]);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### isNull

isNull(fieldName: string): DatabaseQuery<T>

添加实体类某字段值为空的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.isNull('key_date');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### isNotNull

isNotNull(fieldName: string): DatabaseQuery<T>

添加实体类某字段值不为空的查询条件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.isNotNull('key_date');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### orderByAsc

orderByAsc(fieldName: string): DatabaseQuery<T>

按指定字段升序对查询结果进行排序。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.orderByAsc('key_integer');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### orderByDesc

orderByDesc(fieldName: string): DatabaseQuery<T>

按指定字段降序对查询结果进行排序。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

fieldName

string

是

实体类中的字段名。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.orderByDesc('key_integer');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### orderByRandom

orderByRandom(): DatabaseQuery<T>

调用此方法可以将查询结果按随机顺序展示。

使用orderByRandom()对数据进行排序时，建议与limit()配合使用。否则，当该对象类型的数据记录数量过多时，可能会影响查询效率，导致查询超时或失败。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**6.0.1(21)

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.orderByRandom().limit(10);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### limit

limit(count: number, offset?: number): DatabaseQuery<T>

指定返回的查询结果集中的数据记录条数。如果不设置offset，则默认从首个对象开始获取前count个对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**参数****：**

参数名

类型

必填

说明

count

number

是

限制可以获得的数据记录数量。

offset

number

否

指定数据记录的起始位置。

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key_integer', 100);
condition.limit(4, 1);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### beginGroup

beginGroup(): DatabaseQuery<T>

调用此方法是为了放置左括号“(”附加到任何查询条件并将右括号“)”与相同的查询连接起来组合使用。

- beginGroup()和endGroup()必须成对出现，并且必须与其他查询条件一起使用。
- 在beginGroup()和endGroup()之间，必须存在以下查询条件中的一个或多个：

equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()。

- beginGroup()不能直接用在and()和or()之前。即不支持beginGroup().and()、beginGroup().and().endGroup()、beginGroup().or()和beginGroup().or().endGroup()。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.beginGroup().equalTo('string_string', 'string_123').endGroup();
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### endGroup

endGroup(): DatabaseQuery<T>

调用此方法是为了放置右括号“)”附加到任何查询条件并将左括号“(”与相同的查询连接起来组合使用。

- beginGroup()和endGroup()必须成对出现，并且必须与其他查询条件一起使用。
- 在beginGroup()和endGroup()之间，必须存在以下查询条件中的一个或多个：

equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()。

- endGroup()不能直接用在and()和or()之前。即不支持and().endGroup()、beginGroup().and().endGroup()、or().endGroup()和beginGroup().or().endGroup()。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.beginGroup().equalTo('string_string', 'string_123').endGroup();
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### or

or(): DatabaseQuery<T>

使用or运算组合两个条件并返回两个查询结果的并集。

- or()只能与其他查询条件一起使用。
- 当和equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()一起使用时，返回两个查询结果的交集。
- 当or()与and()一起使用时，or()前面不能直接跟and()，即不支持and().or()。
- 与beginGroup()和endGroup()结合使用时：

  - 支持多层嵌套，beginGroup()和endGroup()必须成对出现。
  - beginGroup()不能在or()之前使用，endGroup()不能在or()之后使用。
  - 即不支持beginGroup().or()、beginGroup().or().endGroup()和or().endGroup()。
  - 不能与orderByAsc()、orderByDesc()或limit()一起使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('string_string', 'string_123').or().lessThan('key_integer', 50);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```

#### and

and(): DatabaseQuery<T>

使用and运算组合两个条件并返回两个查询结果的交集。

- and()只能与其他查询条件一起使用。
- 当和equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()一起使用时，返回两个查询结果的交集。
- 当and()与or()一起使用时，and()后面不能直接跟or()，即不支持and().or()。
- 与beginGroup()和endGroup()结合使用时：

  - 支持多层嵌套，beginGroup()和endGroup()必须成对出现。
  - beginGroup()不能在and()之前使用，endGroup()不能在and()之后使用。
  - 即不支持beginGroup().and()、beginGroup().and().endGroup()和and().endGroup()。
  - 不能与orderByAsc()、orderByDesc()或limit()一起使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API****：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：**5.0.0(12)

**返回值****：**

类型

说明

[DatabaseQuery](#section76501736191415)<T>

DatabaseQuery对象。

**示例****：**

```ets
import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
import { hilog } from '@kit.PerformanceAnalysisKit';

// 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('string_string', 'string_123').and().lessThan('key_integer', 50);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
}
```