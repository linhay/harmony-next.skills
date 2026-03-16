# ArkTSUtils.ASON

为支持将JSON字符串解析为共享数据，即[Sendable支持的数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable支持的数据类型)，ArkTS语言基础库新增了ASON工具。ASON工具支持解析JSON字符串并生成共享数据，用于跨并发实例引用传递，同时也支持将共享数据转换为JSON字符串。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

#### 导入模块

```ets
import { ArkTSUtils } from '@kit.ArkTS'
```

#### ISendable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

类型说明[lang.ISendable](../../modules/other/@arkts.lang (ArkTS语言基础能力).md#ZH-CN_TOPIC_0000002497444768__langisendable)所有Sendable类型的父类型。

#### Transformer

type Transformer = (this: ISendable, key: string, value: ISendable | undefined | null) => ISendable | undefined | null

用于转换结果函数的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明this[ISendable](#ZH-CN_TOPIC_0000002529444715__isendable)是在解析的键值对所属的对象。keystring是属性名。value[ISendable](#ZH-CN_TOPIC_0000002529444715__isendable) | undefined | null是在解析的键值对的值。

**返回值：**

类型说明[ISendable](#ZH-CN_TOPIC_0000002529444715__isendable) | undefined | null返回转换结果后的ISendable对象或undefined或null。

#### BigIntMode

定义处理BigInt的模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称值说明DEFAULT0不支持BigInt。PARSE_AS_BIGINT1当整数小于-(2^53-1)或大于(2^53-1)时，解析为BigInt。ALWAYS_PARSE_AS_BIGINT2所有整数都解析为BigInt。

#### ParseReturnType

定义解析结果的返回类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称值说明OBJECT0

返回 SendableObject 对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MAP13+1

返回 SendableMap 对象。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

#### ParseOptions

解析的选项，可定义处理BigInt的模式和解析结果的返回类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明bigIntMode[BigIntMode](#ZH-CN_TOPIC_0000002529444715__bigintmode)否否定义处理BigInt的模式。parseReturnType[ParseReturnType](#ZH-CN_TOPIC_0000002529444715__parsereturntype)否否定义解析结果的返回类型。

#### parse

parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null

用于解析JSON字符串生成ISendable数据或null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明textstring是有效的JSON字符串。reviver[Transformer](#ZH-CN_TOPIC_0000002529444715__transformer)否转换函数，传入该参数，可以用来修改解析生成的原始值。默认值是undefined。目前只支持传入undefined。options[ParseOptions](#ZH-CN_TOPIC_0000002529444715__parseoptions)否解析的配置，传入该参数，可以用来控制解析生成的结果类型。默认值是undefined。

**返回值：**

类型说明[ISendable](#ZH-CN_TOPIC_0000002529444715__isendable) | null返回ISendable数据或null。入参为null时，返回null。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Invalid JSON string.

**示例：**

```ets
import { ArkTSUtils, collections, lang} from '@kit.ArkTS';

type ISendable = lang.ISendable;
let jsonText = '{"name": "John", "age": 30, "city": "ChongQing"}';
let obj = ArkTSUtils.ASON.parse(jsonText) as ISendable;
console.info((obj as object)?.["name"]);
// 期望输出: 'John'
console.info((obj as object)?.["age"]);
// 期望输出: 30
console.info((obj as object)?.["city"]);
// 期望输出: 'ChongQing'

let options: ArkTSUtils.ASON.ParseOptions = {
  bigIntMode: ArkTSUtils.ASON.BigIntMode.PARSE_AS_BIGINT,
  parseReturnType: ArkTSUtils.ASON.ParseReturnType.OBJECT,
}
let numberText = '{"largeNumber":112233445566778899}';
let numberObj = ArkTSUtils.ASON.parse(numberText,undefined,options) as ISendable;

console.info((numberObj as object)?.["largeNumber"]);
// 期望输出: 112233445566778899

let options2: ArkTSUtils.ASON.ParseOptions = {
    bigIntMode: ArkTSUtils.ASON.BigIntMode.PARSE_AS_BIGINT,
    parseReturnType: ArkTSUtils.ASON.ParseReturnType.MAP,
  }
let mapText = '{"largeNumber":112233445566778899}';
let map  = ArkTSUtils.ASON.parse(mapText,undefined,options2);
console.info("map is " + map);
// 期望输出: map is [object SendableMap]
console.info("largeNumber is " + (map as collections.Map<string,bigint>).get("largeNumber"));
// 期望输出: largeNumber is 112233445566778899
```

#### stringify

stringify(value: Object | null | undefined): string

该方法将ArkTS对象数据转换为JSON字符串，额外支持Map和Set相关类型。

从API 18开始参数修改为Object类型，API 18之前参数只支持ISendable类型（除[Int8Array](../../types/classes/Class (Int8Array).md)、[Uint8Array](../../types/classes/Class (Uint8Array).md)、[Int16Array](../../types/classes/Class (Int16Array).md)、[Uint16Array](../../types/classes/Class (Uint16Array).md)、[Int32Array](../../types/classes/Class (Int32Array).md)、[Uint32Array](../../types/classes/Class (Uint32Array).md)、[Uint8ClampedArray](../../types/classes/Class (Uint8ClampedArray).md)、[Float32Array](../../types/classes/Class (Float32Array).md)外）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject | null | undefined是ArkTS对象数据。

**返回值：**

类型说明string转换后的JSON字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Invalid ArkTS value.

**示例：**

```ets
import { ArkTSUtils, collections, HashMap, HashSet } from '@kit.ArkTS';

let hashMap = new HashMap<string,string>();
hashMap.set("ha","a");
hashMap.set("sh","b");
hashMap.set("map","c");
let str1 = ArkTSUtils.ASON.stringify(hashMap);
console.info(str1);
//期望输出：'{"sh":"b","ha":"a","map":"c"}'
let hashSet = new HashSet<string>();
hashSet.add("ha");
hashSet.add("sh");
hashSet.add("set");
let str2 = ArkTSUtils.ASON.stringify(hashSet);
console.info(str2);
//期望输出：'["set","sh","ha"]'
let map = new Map<string,string>();
map.set("m","a");
map.set("a","b");
map.set("p","c");
let str3 = ArkTSUtils.ASON.stringify(map);
console.info(str3);
//期望输出：'{"m":"a","a":"b","p":"c"}'
let set = new Set<string>();
set.add("s");
set.add("e");
set.add("t");
let str4 = ArkTSUtils.ASON.stringify(set);
console.info(str4);
//期望输出：'["s","e","t"]'
let sendableMap = new collections.Map<string,string>();
sendableMap.set("send","a");
sendableMap.set("able","b");
sendableMap.set("map","c");
let str5 = ArkTSUtils.ASON.stringify(sendableMap);
console.info(str5);
//期望输出：'{"send":"a","able":"b","map":"c"}'
let sendableSet = new collections.Set<string>();
sendableSet.add("send");
sendableSet.add("able");
sendableSet.add("set");
let str6 = ArkTSUtils.ASON.stringify(sendableSet);
console.info(str6);
//期望输出：'["send","able","set"]'
```