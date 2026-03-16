# @ohos.util (util工具函数)

该模块主要提供常用的工具函数，实现字符串编解码（[TextEncoder](#ZH-CN_TOPIC_0000002497604754__textencoder)，[TextDecoder](#ZH-CN_TOPIC_0000002497604754__textdecoder)）、有理数运算（[RationalNumber8+](#ZH-CN_TOPIC_0000002497604754__rationalnumber8)）、缓冲区管理（[LRUCache9+](#ZH-CN_TOPIC_0000002497604754__lrucache9)）、范围判断（[ScopeHelper9+](#ZH-CN_TOPIC_0000002497604754__scopehelper9)）、Base64编解码（[Base64Helper9+](#ZH-CN_TOPIC_0000002497604754__base64helper9)）、内置对象类型检查（[types8+](#ZH-CN_TOPIC_0000002497604754__types8)）、对方法进行插桩和替换（[Aspect11+](#ZH-CN_TOPIC_0000002497604754__aspect11)）等功能。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { util } from '@kit.ArkTS';
```

#### util.format9+

format(format: string, ...args: Object[]): string

使用样式化字符串将输入内容按特定格式输出。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明formatstring是格式化字符串，可以包含零个或多个占位符，用于指定要插入的参数的位置和格式。...argsObject[]否替换format参数中占位符的数据，此参数缺失时，默认返回第一个参数。

**返回值：**

类型说明string格式化后的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**格式说明符：**

格式说明符说明%s将参数转换为字符串，用于除Object，BigInt和-0之外的所有值。%d将参数作为十进制整数进行格式化输出，用于除Symbol和BigInt之外的所有值。%i将字符串转换为十进制整数，用于除BigInt和Symbol之外的所有值。%f将字符串转换为浮点数，用于除BigInt和Symbol之外的所有值。%j将JavaScript对象转换为JSON字符串进行格式化输出。%o用于将JavaScript对象进行格式化输出，将对象转换为字符串表示，但不包含对象的原型链信息。%O用于将JavaScript对象进行格式化输出，将对象转换为字符串表示。%c只在浏览器环境中有效。其余环境不会产生样式效果。%%转义百分号的特殊格式化占位符。

**示例：**

```ets
import { util } from '@kit.ArkTS';

interface utilAddressType {
  city: string;
  country: string;
}
interface utilPersonType {
  name: string;
  age: number;
  address: utilAddressType;
}

let name = 'John';
let age = 20;
let formattedString = util.format('My name is %s and I am %s years old', name, age);
console.info(formattedString);
// 输出结果：My name is John and I am 20 years old
let num = 10.5;
formattedString = util.format('The number is %d', num);
console.info(formattedString);
// 输出结果：The number is 10.5
num = 100.5;
formattedString = util.format('The number is %i', num);
console.info(formattedString);
// 输出结果：The number is 100
const pi = 3.141592653;
formattedString = util.format('The value of pi is %f', pi);
console.info(formattedString);
// 输出结果：The value of pi is 3.141592653
const obj: Record<string,number | string> = { "name": 'John', "age": 20 };
formattedString = util.format('The object is %j', obj);
console.info(formattedString);
// 输出结果：The object is {"name":"John","age":20}
const person: utilPersonType = {
  name: 'John',
  age: 20,
  address: {
    city: 'New York',
    country: 'USA'
  }
};
console.info(util.format('Formatted object using %%O: %O', person));
console.info(util.format('Formatted object using %%o: %o', person));
/*
输出结果：
Formatted object using %O: { name: 'John',
  age: 20,
  address:
  { city: 'New York',
    country: 'USA' } }
Formatted object using %o: { name: 'John',
  age: 20,
  address:
  { city: 'New York',
    country: 'USA' } }
*/
const percentage = 80;
let arg = 'homework';
formattedString = util.format('John finished %d%% of the %s', percentage, arg);
console.info(formattedString);
// 输出结果：John finished 80% of the homework
```

#### util.errnoToString9+

errnoToString(errno: number): string

获取系统错误码对应的详细信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明errnonumber是系统发生错误产生的错误码。

**返回值：**

类型说明string错误码对应的详细信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let errnum = -1; // -1 : a system error number
let result = util.errnoToString(errnum);
console.info("result = " + result);
// 输出结果：result = operation not permitted
```

**部分错误码及信息示例：**

错误码信息-1operation not permitted-2no such file or directory-3no such process-4interrupted system call-5i/o error-11resource temporarily unavailable-12not enough memory-13permission denied-100network is down

#### util.callbackWrapper

callbackWrapper(original: Function): (err: Object, value: Object)=>void

对异步函数进行回调化处理，回调中第一个参数是拒绝原因（如果Promise已解决，则为null），第二个参数是已解决的值。

该接口要求参数original必须是异步函数类型。如果传入的参数不是异步函数，不会进行拦截，但是会输出错误信息："callbackWrapper: The type of Parameter must be AsyncFunction"。

该接口用于将返回Promise的async函数转换为错误优先回调风格的函数，调用此接口返回的函数接收一个回调函数作为第二个入参，调用此方法时会先执行original函数。当original的Promise返回resolve时，入参的回调函数的第一个参数为null，第二个参数为resolve的值。当original的Promise返回reject时，入参的回调函数的第一个参数为错误对象，第二个参数为null。当original为无入参的函数时，此接口返回的函数第一个入参需传入一个无效的占位参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明originalFunction是异步函数。

**返回值：**

类型说明(err: Object, value: Object)=>void返回一个回调函数，该函数第一个参数err是拒绝原因（如果 Promise 已解决，则为 null），第二个参数value是已解决的值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
async function fn(input: string) {
  return input;
}
let cb = util.callbackWrapper(fn);
cb('hello world', (err : Object, ret : string) => {
  if (err) throw new Error;
  console.info(ret);
});
// 输出结果：hello world
```

#### util.promisify9+

promisify(original: (err: Object, value: Object) => void): Function

接收一个采用“错误优先”回调模式的函数，即以(err, value) => callback作为最后一个参数，并返回其Promise函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明original(err: Object, value: Object) => void是回调函数中第一个参数err是拒绝原因（如果 Promise 已解决，则为 null），第二个参数value是已解决的值。

**返回值：**

类型说明Function返回一个 Promise 的函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
async function fn() {
  return 'hello world';
}
const addCall = util.promisify(util.callbackWrapper(fn));
(async () => {
  try {
    let res: string = await addCall();
    console.info(res);
    // 输出结果：hello world
  } catch (err) {
    console.info(err);
  }
})();
```

#### util.generateRandomUUID9+

generateRandomUUID(entropyCache?: boolean): string

使用加密安全随机数生成器生成随机的RFC 4122版本4的string类型UUID。为了提升性能，此接口会默认使用缓存，即入参为true，最多可缓存128个随机的UUID。当缓存中128个UUID用尽后，会重新生成，以保证UUID的随机性。如需禁用缓存，请将入参设置为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明entropyCacheboolean否是否使用已缓存的UUID，true表示使用缓存的UUID，false表示不使用缓存的UUID，默认true。

**返回值：**

类型说明string表示此UUID的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
let uuid = util.generateRandomUUID(true);
console.info("RFC 4122 Version 4 UUID:" + uuid);
// 输出随机生成的UUID
```

#### util.generateRandomBinaryUUID9+

generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array

使用加密安全随机数生成器生成随机的RFC 4122版本4的UUID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明entropyCacheboolean否是否使用已缓存的UUID，true表示使用缓存的UUID，false表示不使用缓存的UUID，默认true。

**返回值：**

类型说明Uint8Array表示此UUID的Uint8Array值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
let uuid = util.generateRandomBinaryUUID(true);
console.info(JSON.stringify(uuid));
// 输出随机生成的UUID
```

#### util.parseUUID9+

parseUUID(uuid: string): Uint8Array

将generateRandomUUID生成的string类型UUID转换为generateRandomBinaryUUID生成的UUID，符合RFC 4122版本规范。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明uuidstring是UUID字符串。

**返回值：**

类型说明Uint8Array返回表示此UUID的Uint8Array，如果解析失败，则抛出SyntaxError。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.10200002Invalid uuid string.

**示例：**

```ets
let uuid = util.parseUUID("84bdf796-66cc-4655-9b89-d6218d100f9c");
console.info("uuid = " + uuid);
// 输出结果：uuid = 132,189,247,150,102,204,70,85,155,137,214,33,141,16,15,156
```

#### util.printf(deprecated)

printf(format: string, ...args: Object[]): string

通过式样化字符串对输入的内容按特定格式输出。

从API version 7开始支持，从API version 9开始废弃，建议使用[util.format9+](#ZH-CN_TOPIC_0000002497604754__utilformat9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明formatstring是式样化字符串。...argsObject[]否替换式样化字符串通配符的数据，此参数缺失时，默认返回第一个参数。

**返回值：**

类型说明string按特定格式式样化后的字符串。

**示例：**

```ets
let res = util.printf("%s", "hello world!");
console.info(res);
// 输出结果：hello world!
```

#### util.getErrorString(deprecated)

getErrorString(errno: number): string

获取系统错误码对应的详细信息。

从API version 7开始支持，从API version 9开始废弃，建议使用[util.errnoToString9+](#ZH-CN_TOPIC_0000002497604754__utilerrnotostring9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明errnonumber是系统发生错误产生的错误码。

**返回值：**

类型说明string错误码对应的详细信息。

**示例：**

```ets
let errnum = -1; // -1 : a system error number
let result = util.getErrorString(errnum);
console.info("result = " + result);
// 输出结果：result = operation not permitted
```

#### util.promiseWrapper(deprecated)

promiseWrapper(original: (err: Object, value: Object) => void): Object

接收一个采用“错误优先”回调模式的函数，即以(err, value) => callback作为最后一个参数，并返回其Promise函数。

从API version 7开始支持，从API version 9开始废弃，此接口不可用，建议使用[util.promisify9+](#ZH-CN_TOPIC_0000002497604754__utilpromisify9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明original(err: Object, value: Object) => void是异步函数。

**返回值：**

类型说明Object返回promise函数，采用遵循常见的错误优先的回调风格的函数（也就是将(err, value) => ...回调作为最后一个参数）。

#### util.getHash12+

getHash(object: object): number

获取对象的Hash值。

首次获取时，则计算Hash值并保存到对象的Hash域（返回随机的Hash值）；后续获取时，直接从Hash域中返回Hash值（同一对象多次返回值保持不变）。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明objectobject是需要获取Hash值的对象。

**返回值：**

类型说明numberHash值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
interface Person {
  name: string,
  age: number
}
let obj: Person = { name: 'Jack', age: 20 };
let result1 = util.getHash(obj);
console.info('result1 is ' + result1);
let result2 = util.getHash(obj);
console.info('result2 is ' + result2);
// 输出结果：result1 与 result2 的值相等，且为随机的Hash值。
```

#### util.getMainThreadStackTrace20+

getMainThreadStackTrace(): string

获取主线程的栈追踪信息，最多返回64层调用帧。

该接口可能对主线程性能产生影响，建议仅在必要时使用，如日志记录、错误分析或调试场景。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string主线程的栈追踪信息。若主线程未处于执行JS代码状态，则返回空字符串。

**示例：**

```ets
let stack = util.getMainThreadStackTrace();
console.info(stack);
// 输出当前主线程的栈追踪信息。
```

#### TextDecoderOptions11+

解码相关选项参数，包含两个属性fatal和ignoreBOM。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明fatalboolean否是是否显示致命错误，true表示显示致命错误，false表示不显示致命错误，默认值是false。ignoreBOMboolean否是是否忽略BOM标记，true表示忽略待解码数据的BOM标记，false表示会对BOM标记解码，默认值是false。

#### DecodeToStringOptions12+

用于配置decodeToString方法在解码字节流时的行为参数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明streamboolean否是输入末尾出现的不完整字节序列是否需要追加在下次调用decodeToString的参数中处理。设置为true，则不完整的字节序列会存储在内部缓存区直到下次调用该函数，false则会在当前调用时直接解码。默认为false。

#### DecodeWithStreamOptions11+

解码是否跟随附加数据块相关选项参数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明streamboolean否是在随后的decodeWithStream()调用中是否跟随附加数据块。如果以块的形式处理数据，则设置为true；如果处理最后的数据未分块，则设置为false。默认为false。

#### Aspect11+

Aspect类用于封装提供切面能力（Aspect Oriented Programming，简写AOP）的接口，这些接口可用于对类方法进行前后插桩或替换实现。

#### addBefore11+

static addBefore(targetClass: Object, methodName: string, isStatic: boolean, before: Function): void

在指定的类对象的原方法执行前插入一个函数。执行addBefore接口后，先运行插入的函数逻辑，再执行指定类对象的原方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明targetClassObject是指定的类对象。methodNamestring是指定的原方法名，不支持read-only方法。isStaticboolean是指定的原方法是否为静态方法。true表示静态方法，false表示实例方法。beforeFunction是要插入的函数对象。函数有参数，则第一个参数是this对象（若isStatic为true，则为类对象即targetClass；若isStatic为false，则为调用方法的实例对象），其余参数是原方法的参数。函数也可以无参数，无参时不做处理。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class MyClass {
  msg: string = 'msg000';
  foo(arg: string): string {
    console.info('foo arg is ' + arg);
    return this.msg;
  }

  static data: string = 'data000';
  static bar(arg: string): string {
    console.info('bar arg is ' + arg);
    return MyClass.data;
  }
}

let asp = new MyClass();
let result = asp.foo('123');
// 输出结果：foo arg is 123
console.info('result is ' + result);
// 输出结果：result is msg000
console.info('asp.msg is ' + asp.msg);
// 输出结果：asp.msg is msg000

util.Aspect.addBefore(MyClass, 'foo', false, (instance: MyClass, arg: string) => {
  console.info('arg is ' + arg);
  instance.msg = 'msg111';
  console.info('msg is changed to ' + instance.msg);
});

result = asp.foo('123');
// 输出结果：arg is 123
// 输出结果：msg is changed to msg111
// 输出结果：foo arg is 123
console.info('result is ' + result);
// 输出结果：result is msg111
console.info('asp.msg is ' + asp.msg);
// 输出结果：asp.msg is msg111

let res = MyClass.bar('456');
// 输出结果：bar arg is 456
console.info('res is ' + res);
// 输出结果：res is data000
console.info('MyClass.data is ' + MyClass.data);
// 输出结果：MyClass.data is data000

util.Aspect.addBefore(MyClass, 'bar', true, (target: Object, arg: string) => {
  console.info('arg is ' + arg);
  let newVal = 'data111';
  Reflect.set(target, 'data', newVal);
  console.info('data is changed to ' + newVal);
});

res = MyClass.bar('456');
// 输出结果：arg is 456
// 输出结果：data is changed to data111
// 输出结果：bar arg is 456
console.info('res is ' + res);
// 输出结果：res is data111
console.info('MyClass.data is ' + MyClass.data);
// 输出结果：MyClass.data is data111
```

#### addAfter11+

static addAfter(targetClass: Object, methodName: string, isStatic: boolean, after: Function): void

在指定的类方法执行后插入一段逻辑。最终返回插入函数执行后的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明targetClassObject是指定的类对象。methodNamestring是指定的原方法名，不支持read-only方法。isStaticboolean是指定的原方法是否为静态方法。true表示静态方法，false表示实例方法。afterFunction是要插入的函数。函数有参数时，则第一个参数是this对象（若isStatic为true，则为类对象即targetClass；若isStatic为false，则为调用方法的实例对象），第二个参数是原方法的返回值（如果原方法没有返回值，则为undefined），其余参数是原方法的参数。函数也可以无参，无参时不做处理。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class MyClass {
  msg: string = 'msg000';
  foo(arg: string): string {
    console.info('foo arg is ' + arg);
    return this.msg;
  }
}

let asp = new MyClass();
let result = asp.foo('123');
// 输出结果：foo arg is 123
console.info('result is ' + result);
// 输出结果：result is msg000
console.info('asp.msg is ' + asp.msg);
// 输出结果：asp.msg is msg000

util.Aspect.addAfter(MyClass, 'foo', false, (instance: MyClass, ret: string, arg: string): string => {
  console.info('arg is ' + arg);
  console.info('ret is ' + ret);
  instance.msg = 'msg111';
  console.info('msg is changed to ' + instance.msg);
  return 'msg222';
});

result = asp.foo('123');
// 输出结果：foo arg is 123
// 输出结果：arg is 123
// 输出结果：ret is msg000
// 输出结果：msg is changed to msg111
console.info('result is ' + result);
// 输出结果：result is msg222
console.info('asp.msg is ' + asp.msg);
// 输出结果：asp.msg is msg111

// 前后插桩的例子
class AroundTest {
  foo(arg: string) {
    console.info('execute foo with arg ' + arg);
  }
}
util.Aspect.addBefore(AroundTest, 'foo', false, () => {
  console.info('execute before');
});
util.Aspect.addAfter(AroundTest, 'foo', false, () => {
  console.info('execute after');
});

(new AroundTest()).foo('hello');
// 输出结果：execute before
// 输出结果：execute foo with arg hello
// 输出结果：execute after
```

#### replace11+

static replace(targetClass: Object, methodName: string, isStatic: boolean, instead: Function) : void

将指定类的原方法替换为另一个函数。replace接口执行完成后，调用指定的类方法时，仅执行替换后的逻辑。最终返回替换函数执行完毕的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明targetClassObject是指定的类对象。methodNamestring是指定的原方法名，不支持read-only方法。isStaticboolean是指定的原方法是否为静态方法。true表示静态方法，false表示实例方法。insteadFunction是要用来替换原方法的函数。函数有参数时，则第一个参数是this对象（若isStatic为true，则为类对象即targetClass；若isStatic为false，则为调用方法的实例对象），其余参数是原方法的参数。函数也可以无参，无参时不做处理。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class MyClass {
  msg: string = 'msg000';
  foo(arg: string): string {
    console.info('foo arg is ' + arg);
    return this.msg;
  }
}

let asp = new MyClass();
let result = asp.foo('123');
// 输出结果：foo arg is 123
console.info('result is ' + result);
// 输出结果：result is msg000
console.info('asp.msg is ' + asp.msg);
// 输出结果：asp.msg is msg000

util.Aspect.replace(MyClass, 'foo', false, (instance: MyClass, arg: string): string => {
  console.info('execute instead');
  console.info('arg is ' + arg);
  instance.msg = 'msg111';
  console.info('msg is changed to ' + instance.msg);
  return 'msg222';
});

result = asp.foo('123');
// 输出结果：execute instead
// 输出结果：arg is 123
// 输出结果：msg is changed to msg111
console.info('result is ' + result);
// 输出结果：result is msg222
console.info('asp.msg is ' + asp.msg);
// 输出结果：asp.msg is msg111
```

#### TextDecoder

TextDecoder用于将字节数组解码为字符串，支持utf-8、utf-16le/be、iso-8859和windows-1251等不同的编码格式。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

名称类型只读可选说明encodingstring是否

编码格式。

- 支持格式：utf-8、ibm866、iso-8859-2、iso-8859-3、iso-8859-4、iso-8859-5、iso-8859-6、iso-8859-7、iso-8859-8、iso-8859-8-i、iso-8859-10、iso-8859-13、iso-8859-14、iso-8859-15、koi8-r、koi8-u、macintosh、windows-874、windows-1250、windows-1251、windows-1252、windows-1253、windows-1254、windows-1255、windows-1256、windows-1257、windows-1258、x-mac-cyrillic、gbk、gb18030、big5、euc-jp、iso-2022-jp、shift_jis、euc-kr、utf-16be、utf-16le、gb2312、iso-8859-1。

fatalboolean是否是否显示致命错误，true表示显示，false表示不显示。ignoreBOMboolean是否是否忽略BOM（byte order marker）标记，默认值为false，表示解码结果包含BOM标记。

#### constructor9+

constructor()

TextDecoder的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let textDecoder = new util.TextDecoder();
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// 输出结果：retStr = utf-8
```

#### create9+

static create(encoding?: string, options?: TextDecoderOptions): TextDecoder

替代有参构造函数的功能。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否编码格式，默认值是'utf-8'。options[TextDecoderOptions](#ZH-CN_TOPIC_0000002497604754__textdecoderoptions11)否解码相关选项参数，存在两个属性fatal和ignoreBOM。

**返回值：**

类型说明[TextDecoder](#ZH-CN_TOPIC_0000002497604754__textdecoder)返回一个TextDecoder对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// 输出结果：retStr = utf-8
```

#### decodeToString12+

decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string

将输入参数解码后输出对应文本。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明inputUint8Array是需要解码的数组。options[DecodeToStringOptions](#ZH-CN_TOPIC_0000002497604754__decodetostringoptions12)否解码相关选项参数。默认undefined。

**返回值：**

类型说明string解码后的数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let decodeToStringOptions: util.DecodeToStringOptions = {
  stream: false
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let uint8 = new Uint8Array([0xEF, 0xBB, 0xBF, 0x61, 0x62, 0x63]);
let retStr = textDecoder.decodeToString(uint8, decodeToStringOptions);
console.info("retStr = " + retStr);
// 输出结果：retStr = abc
```

#### decodeWithStream(deprecated)

decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string

将输入参数解码后输出对应文本。当input是一个空数组时，返回undefined。

从API version 9开始支持，从API version 12开始废弃，建议使用[decodeToString12+](#ZH-CN_TOPIC_0000002497604754__decodetostring12)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明inputUint8Array是符合格式需要解码的数组。options[DecodeWithStreamOptions](#ZH-CN_TOPIC_0000002497604754__decodewithstreamoptions11)否解码相关选项参数。

**返回值：**

类型说明string解码后的数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let decodeWithStreamOptions: util.DecodeWithStreamOptions = {
  stream: false
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let uint8 = new Uint8Array(6);
uint8[0] = 0xEF;
uint8[1] = 0xBB;
uint8[2] = 0xBF;
uint8[3] = 0x61;
uint8[4] = 0x62;
uint8[5] = 0x63;
console.info("input num:");
let retStr = textDecoder.decodeWithStream(uint8, decodeWithStreamOptions);
console.info("retStr = " + retStr);
// 输出结果：retStr = abc
```

#### constructor(deprecated)

constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })

TextDecoder的构造函数。

从API version 7开始支持，从API version 9开始废弃，建议使用[create9+](#ZH-CN_TOPIC_0000002497604754__create9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否编码格式，默认值是'utf-8'。options{ fatal?: boolean; ignoreBOM?: boolean }否解码相关选项参数，存在两个属性fatal和ignoreBOM。

**表1** options

名称参数类型必填说明fatalboolean否是否显示致命错误，true表示显示致命错误，false表示不显示致命错误，默认值是false。ignoreBOMboolean否是否忽略BOM标记，true表示忽略待解码数据的BOM标记，false表示会对BOM标记解码，默认值是false。

**示例：**

```ets
let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
```

#### decode(deprecated)

decode(input: Uint8Array, options?: { stream?: false }): string

通过输入参数解码后输出对应文本。

从API version 7开始支持，从API version 9开始废弃，建议使用[decodeToString12+](#ZH-CN_TOPIC_0000002497604754__decodetostring12)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明inputUint8Array是符合格式需要解码的数组。options{ stream?: false }否解码相关选项参数。

**表2** options

名称参数类型必填说明streamboolean否在随后的decode()调用中是否跟随附加数据块。如果以块的形式处理数据，则设置为true；如果处理数据未分块，则设置为false。默认为false。

**返回值：**

类型说明string解码后的数据。

**示例：**

```ets
let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
let uint8 = new Uint8Array(6);
uint8[0] = 0xEF;
uint8[1] = 0xBB;
uint8[2] = 0xBF;
uint8[3] = 0x61;
uint8[4] = 0x62;
uint8[5] = 0x63;
console.info("input num:");
let retStr = textDecoder.decode(uint8, {stream: false});
console.info("retStr = " + retStr);
// 输出结果：retStr = abc
```

#### EncodeIntoUint8ArrayInfo11+

编码后的信息，包含读取的字符数和写入的字节数。

#### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明readnumber是否已读取的字符数。writtennumber是否已写入的字节数。

#### TextEncoder

TextEncoder将字符串编码为字节数组，支持多种编码格式。

在使用TextEncoder进行编码时，需要注意不同编码格式下字符所占的字节数不同。务必明确指定编码格式，以确保编码结果正确。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

名称类型只读可选说明encodingstring是否

编码格式。

- 支持格式：utf-8、gb2312、gb18030、ibm866、iso-8859-1、iso-8859-2、iso-8859-3、iso-8859-4、iso-8859-5、iso-8859-6、iso-8859-7、iso-8859-8、iso-8859-8-i、iso-8859-10、iso-8859-13、iso-8859-14、iso-8859-15、koi8-r、koi8-u、macintosh、windows-874、windows-1250、windows-1251、windows-1252、windows-1253、windows-1254、windows-1255、windows-1256、windows-1257、windows-1258、gbk、big5、euc-jp、iso-2022-jp、shift_jis、euc-kr、x-mac-cyrillic、utf-16be、utf-16le。

- 默认值是：'utf-8'。

#### constructor

constructor()

TextEncoder的构造函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let textEncoder = new util.TextEncoder();
```

#### constructor9+

constructor(encoding?: string)

TextEncoder的构造函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否编码格式，默认值为'utf-8'。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
let textEncoder = new util.TextEncoder("utf-8");
```

#### create12+

static create(encoding?: string): TextEncoder

创建TextEncoder对象的方法。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否编码格式，默认值为'utf-8'。

**返回值：**

类型说明[TextEncoder](#ZH-CN_TOPIC_0000002497604754__textencoder)返回一个TextEncoder对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
let textEncoder = util.TextEncoder.create("utf-8");
```

#### encodeInto9+

encodeInto(input?: string): Uint8Array

将输入参数编码后输出Uint8Array对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明inputstring否需要编码的字符串，默认值是空字符串。当入参是空字符串时，返回undefined。

**返回值：**

类型说明Uint8Array返回编码后的Uint8Array对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
let textEncoder = new util.TextEncoder();
let result = textEncoder.encodeInto("\uD800¥¥");
console.info("result = " + result);
// 输出结果: result = 237,160,128,194,165,194,165
```

#### encodeIntoUint8Array9+

encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo

对字符串进行编码，将结果存储到dest数组。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明inputstring是需要编码的字符串。destUint8Array是Uint8Array对象实例，用于将生成的utf-8编码文本放入其中。

**返回值：**

类型说明[EncodeIntoUint8ArrayInfo](#ZH-CN_TOPIC_0000002497604754__encodeintouint8arrayinfo11)返回一个对象，read表示已编码的字符数，written表示编码字符所占用的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let textEncoder = new util.TextEncoder();
let buffer = new ArrayBuffer(4);
let uint8 = new Uint8Array(buffer);
let result = textEncoder.encodeIntoUint8Array('abcd', uint8);
console.info("uint8 = " + uint8);
// 输出结果: uint8 = 97,98,99,100
console.info("result.read = " + result.read);
// 输出结果: result.read = 4
console.info("result.written = " + result.written);
// 输出结果: result.written = 4
```

#### encodeInto(deprecated)

encodeInto(input: string, dest: Uint8Array): { read: number; written: number }

将生成的utf-8编码文本写入dest数组。

从API version 7开始支持，从API version 9开始废弃，建议使用[encodeIntoUint8Array9+](#ZH-CN_TOPIC_0000002497604754__encodeintouint8array9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明inputstring是需要编码的字符串。destUint8Array是Uint8Array对象实例，用于将生成的utf-8编码文本放入其中。

**返回值：**

类型说明{ read: number; written: number }返回一个对象，read表示已编码的字符数，written表示编码字符所占用的字节数。

**示例：**

```ets
let textEncoder = new util.TextEncoder();
let buffer = new ArrayBuffer(4);
let uint8 = new Uint8Array(buffer);
let result = textEncoder.encodeInto('abcd', uint8);
console.info("uint8 = " + uint8);
// 输出结果: uint8 = 97,98,99,100
```

#### encode(deprecated)

encode(input?: string): Uint8Array

将输入参数编码后输出对应文本。

从API version 7开始支持，从API version 9开始废弃，建议使用[encodeInto9+](#ZH-CN_TOPIC_0000002497604754__encodeinto9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明inputstring否需要编码的字符串，默认值是空字符串。

**返回值：**

类型说明Uint8Array返回编码后的文本。

**示例：**

```ets
let textEncoder = new util.TextEncoder();
let result = textEncoder.encode("\uD800¥¥");
console.info("result = " + result);
// 输出结果: result = 237,160,128,194,165,194,165
```

#### RationalNumber8+

RationalNumber主要用于有理数的比较，并提供获取分子和分母的方法。使用toString()方法可以将有理数转换为字符串形式，使用该类可以方便地进行有理数的各种操作。

#### constructor9+

constructor()

RationalNumber的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let rationalNumber = new util.RationalNumber();
```

#### parseRationalNumber9+

static parseRationalNumber(numerator: number,denominator: number): RationalNumber

创建具有给定分子和分母的RationalNumber实例。

该接口要求参数numerator和denominator必须是整数类型。如果传入的参数是小数类型，不会进行拦截，但是会输出错误信息："parseRationalNumber: The type of Parameter must be integer"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明numeratornumber是分子，整数类型。取值范围：-Number.MAX_VALUE <= numerator <= Number.MAX_VALUE。denominatornumber是分母，整数类型。取值范围：-Number.MAX_VALUE <= denominator <= Number.MAX_VALUE。

**返回值：**

类型说明[RationalNumber](#ZH-CN_TOPIC_0000002497604754__rationalnumber8)RationalNumber对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
```

#### createRationalFromString8+

static createRationalFromString(rationalString: string): RationalNumber

使用给定的字符串创建RationalNumber对象。

该接口要求参数rationalString是字符串格式。如果传入的参数是小数类型字符串格式，不会进行拦截，但是会输出错误信息："createRationalFromString: The type of Parameter must be integer string"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明rationalStringstring是字符串格式。

**返回值：**

类型说明[RationalNumber](#ZH-CN_TOPIC_0000002497604754__rationalnumber8)​RationalNumber对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401The type of rationalString must be string.

**示例：**

```ets
let rational = util.RationalNumber.createRationalFromString("3/4");
```

#### compare9+

compare(another: RationalNumber): number​

将当前RationalNumber对象与目标RationalNumber对象进行比较，并返回比较结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明another[RationalNumber](#ZH-CN_TOPIC_0000002497604754__rationalnumber8)是其他的有理数对象。

**返回值：**

类型说明number两个对象相等时返回0；给定对象小于当前对象时返回1；给定对象大于当前对象时返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.compare(rational);
console.info("result = " + result);
// 输出结果：result = -1
```

#### valueOf8+

valueOf(): number

获取当前RationalNumber对象的整数或浮点数值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回整数或者浮点数的值。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.valueOf();
console.info("result = " + result);
// 输出结果：result = 0.5
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.valueOf();
console.info("result = " + result);
// 输出结果：result = 0.5
```

#### equals8+

equals(obj: Object): boolean

比较当前的RationalNumber对象与给定对象是否相等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明objObject是其他类型对象。

**返回值：**

类型说明boolean如果给定对象与当前对象相同，则返回true；否则返回false。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.equals(rational);
console.info("result = " + result);
// 输出结果：result = false
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.equals(rational);
console.info("result = " + result);
// 输出结果：result = false
```

#### getCommonFactor9+

static getCommonFactor(number1: number, number2: number): number

获取两个整数的最大公约数。

该接口要求参数number1和number2必须是整数类型。如果传入的参数是小数类型，不会进行拦截，但是会输出错误信息："getCommonFactor: The type of Parameter must be integer"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明number1number是整数类型。-Number.MAX_VALUE <= number1 <= Number.MAX_VALUE。number2number是整数类型。-Number.MAX_VALUE <= number2 <= Number.MAX_VALUE。

**返回值：**

类型说明number返回两个给定数字的最大公约数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let result = util.RationalNumber.getCommonFactor(4,6);
console.info("result = " + result);
// 输出结果：result = 2
```

#### getNumerator8+

getNumerator(): number

获取当前RationalNumber对象的分子。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回RationalNumber对象的分子。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.getNumerator();
console.info("result = " + result);
// 输出结果：result = 1
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.getNumerator();
console.info("result = " + result);
// 输出结果：result = 1
```

#### getDenominator8+

getDenominator(): number

获取当前RationalNumber对象的分母。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回RationalNumber对象的分母。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.getDenominator();
console.info("result = " + result);
// 输出结果：result = 2
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2)
let result = rationalNumber.getDenominator();
console.info("result = " + result);
// 输出结果：result = 2
```

#### isZero8+

isZero():boolean

检查当前RationalNumber对象是否为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean如果当前对象的值为0，则返回true；否则返回false。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isZero();
console.info("result = " + result);
// 输出结果：result = false
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isZero();
console.info("result = " + result);
// 输出结果：result = false
```

#### isNaN8+

isNaN(): boolean

检查当前RationalNumber对象是否表示非数字(NaN)值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean如果分母和分子都为0，则返回true；否则返回false。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isNaN();
console.info("result = " + result);
// 输出结果：result = false
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isNaN();
console.info("result = " + result);
// 输出结果：result = false
```

#### isFinite8+

isFinite():boolean

检查RationalNumber对象是否表示一个有限值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean如果分母不为0，则返回true；否则返回false。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isFinite();
console.info("result = " + result);
// 输出结果：result = true
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isFinite();
console.info("result = " + result);
// 输出结果：result = true
```

#### toString8+

toString(): string

获取RationalNumber对象的字符串表示形式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回Numerator/Denominator格式的字符串，例如3/5，如果分子为0，则返回0/1。如果分母为0，则返回Infinity。如果分子和分母都为0，则返回NaN。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// 输出结果：result = 1/2
```

API 9及以上建议使用以下写法：

```ets
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// 输出结果：result = 1/2
```

#### constructor(deprecated)

constructor(numerator: number,denominator: number)

RationalNumber的构造函数。

从API version 8开始支持，从API version 9开始废弃，建议使用[parseRationalNumber9+](#ZH-CN_TOPIC_0000002497604754__parserationalnumber9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明numeratornumber是分子，整数类型。denominatornumber是分母，整数类型。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
```

#### compareTo(deprecated)

compareTo(another: RationalNumber): number​

比较当前的RationalNumber对象与给定的对象。

从API version 8开始支持，从API version 9开始废弃，建议使用[compare9+](#ZH-CN_TOPIC_0000002497604754__compare9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明anotherRationalNumber是其他的有理数对象。

**返回值：**

类型说明number如果两个对象相等，则返回0；如果给定对象小于当前对象，则返回1；如果给定对象大于当前对象，则返回-1。

**示例：**

```ets
let rationalNumber = new util.RationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.compareTo(rational);
console.info("result = " + result);
// 输出结果：result = -1
```

#### getCommonDivisor(deprecated)

static getCommonDivisor(number1: number,number2: number): number

获取两个指定整数的最大公约数。

从API version 8开始支持，从API version 9开始废弃，建议使用[getCommonFactor9+](#ZH-CN_TOPIC_0000002497604754__getcommonfactor9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明number1number是整数类型。number2number是整数类型。

**返回值：**

类型说明number返回两个给定数字的最大公约数。

#### LRUCache9+

LRUCache用于在缓存空间不足时，将近期最少使用的数据替换为新数据。此设计基于资源访问的考虑：近期访问的数据，可能在不久的将来会再次访问。因此最少访问的数据被认为价值最低，应当优先从缓存中移除。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

名称类型只读可选说明lengthnumber是否当前缓冲区中值的总数。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(1, 8);
let result = pro.length;
console.info('result = ' + result);
// 输出结果：result = 2
```

#### constructor9+

constructor(capacity?: number)

默认构造函数用于创建一个新的LRUCache实例，默认容量为64。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明capacitynumber否指示要为缓冲区自定义的容量，不传默认值为64，最大值不能超过2147483647。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
```

#### updateCapacity9+

updateCapacity(newCapacity: number): void

更新缓冲区容量为指定值，如果newCapacity小于或等于0，则抛出异常。当缓冲区中值的总数大于指定容量时，会执行删除操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明newCapacitynumber是指示要为缓冲区自定义的容量，最大值不能超过2147483647。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.updateCapacity(100);
```

#### toString9+

toString(): string

返回对象的字符串表示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回对象的字符串表示形式。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
pro.get(3);
console.info(pro.toString());
// 输出结果：LRUCache[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% ]
// maxSize: 缓存区最大值 hits: 查询值匹配成功的次数 misses: 查询值匹配失败的次数 hitRate: 查询值匹配率
```

#### getCapacity9+

getCapacity(): number

获取当前缓冲区的容量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回当前缓冲区的容量。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
let result = pro.getCapacity();
console.info('result = ' + result);
// 输出结果：result = 64
```

#### clear9+

clear(): void

清除当前缓冲区中的键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.length;
pro.clear();
let res = pro.length;
console.info('result = ' + result);
console.info('res = ' + res);
// 输出结果：result = 1
// 输出结果：res = 0
```

#### getCreateCount9+

getCreateCount(): number

获取对象创建的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回创建对象的次数。

**示例：**

```ets
// 创建新类ChildLRUCache继承LRUCache，重写createDefault方法，返回一个非undefined的值。
class ChildLRUCache extends util.LRUCache<number, number> {
  constructor() {
    super();
  }

  createDefault(key: number): number {
    return key;
  }
}
let lru = new ChildLRUCache();
lru.put(2, 10);
lru.get(3);
lru.get(5);
let res = lru.getCreateCount();
console.info('res = ' + res);
// 输出结果：res = 2
```

#### getMissCount9+

getMissCount(): number

获取查询值不匹配的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回查询值不匹配的次数。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
let result = pro.getMissCount();
console.info('result = ' + result);
// 输出结果：result = 0
```

#### getRemovalCount9+

getRemovalCount(): number

获取缓冲区键值对的回收次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回缓冲区键值对回收的次数。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.updateCapacity(2);
pro.put(50, 22);
let result = pro.getRemovalCount();
console.info('result = ' + result);
// 输出结果：result = 0
```

#### getMatchCount9+

getMatchCount(): number

获取查询值匹配成功的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回查询值匹配成功的次数。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
let result = pro.getMatchCount();
console.info('result = ' + result);
// 输出结果：result = 1
```

#### getPutCount9+

getPutCount(): number

获取将值添加到缓冲区的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回将值添加到缓冲区的次数。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.getPutCount();
console.info('result = ' + result);
// 输出结果：result = 1
```

#### isEmpty9+

isEmpty(): boolean

检查缓冲区是否为空。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean如果缓冲区不包含任何值，则返回true。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.isEmpty();
console.info('result = ' + result);
// 输出结果：result = false
```

#### get9+

get(key: K): V | undefined

返回键对应的值。当键不在缓冲区中时，通过[createDefault9+](#ZH-CN_TOPIC_0000002497604754__createdefault9)接口创建，若createDefault创建的值不为undefined时，此时会调用[afterRemoval9+](#ZH-CN_TOPIC_0000002497604754__afterremoval9)接口，返回createDefault创建的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是要查询的键。

**返回值：**

类型说明V | undefined如果指定的键存在于缓冲区中，则返回与键关联的值；否则返回createDefault创建的值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result  = pro.get(2);
console.info('result = ' + result);
// 输出结果：result = 10
```

#### put9+

put(key: K,value: V): V

将键值对添加到缓冲区，返回与添加的键关联的值。当缓冲区中值的总数超过容量时，执行删除操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是要添加的键。valueV是指示与要添加的键关联的值。

**返回值：**

类型说明V返回与添加的键关联的值。如果键或值为空，则抛出此异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
let result = pro.put(2, 10);
console.info('result = ' + result);
// 输出结果：result = 10
```

#### values9+

values(): V[]

获取当前缓冲区中所有值，从最近最少访问到最近访问的顺序列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明V[]返回当前缓冲区中所有值的列表，顺序为从最近最少访问（Least Recent）到最近访问（Most Recent）。

**示例：**

```ets
let pro = new util.LRUCache<number, string>();
pro.put(1, 'A');
pro.put(2, "B");
pro.put(3, 'C');
pro.put(4, 'D')
pro.put(5, 'E')
pro.put(6, 'F')
let result = pro.values();
console.info('result = ' + result);
// 输出结果：result = A,B,C,D,E,F
pro.get(1);
pro.get(2);
result = pro.values();
console.info('result = ' + result);
// 输出结果：result = C,D,E,F,A,B
```

#### keys9+

keys(): K[]

获取当前缓冲区中所有键，从最近最少访问到最近访问的顺序列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明K[]返回当前缓冲区中所有键的列表，顺序为从最近最少访问（Least Recent）到最近访问（Most Recent）。

**示例：**

```ets
let pro = new util.LRUCache<number, string>();
pro.put(1, 'A');
pro.put(2, "B");
pro.put(3, 'C');
pro.put(4, 'D')
pro.put(5, 'E')
pro.put(6, 'F')
let result = pro.keys();
console.info('result = ' + result);
// 输出结果：result = 1,2,3,4,5,6
pro.get(5);
pro.get(3);
result = pro.keys();
console.info('result = ' + result);
// 输出结果：result = 1,2,4,6,5,3
```

#### remove9+

remove(key: K): V | undefined

从当前缓冲区中删除指定的键及其关联的值，并返回键关联的值。如果指定的键不存在，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是要删除的键值。

**返回值：**

类型说明V | undefined返回一个包含已删除键值对的Optional对象；如果key不存在，则返回undefined，如果key为null，则抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.remove(20);
console.info('result = ' + result);
// 输出结果：result = undefined
```

#### afterRemoval9+

afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void

删除值后执行后续操作，这些操作由开发者自行实现。本接口会在删除操作时被调用，如[get9+](#ZH-CN_TOPIC_0000002497604754__get9)、[put9+](#ZH-CN_TOPIC_0000002497604754__put9)、[remove9+](#ZH-CN_TOPIC_0000002497604754__remove9)、[clear9+](#ZH-CN_TOPIC_0000002497604754__clear9)、[updateCapacity9+](#ZH-CN_TOPIC_0000002497604754__updatecapacity9)接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明isEvictboolean是当因容量不足而调用该方法时，参数值设置为true，其他情况设置为false。keyK是表示删除的键。valueV是表示删除的值。newValueV是如果已调用put方法并且要添加的键已经存在，则参数值是关联的新值。其他情况下参数值为空。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class ChildLRUCache<K, V> extends util.LRUCache<K, V> {
  constructor(capacity?: number) {
    super(capacity);
  }

  afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void {
    if (isEvict === true) {
      console.info('key = ' + key);
      // 输出结果：key = 1
      console.info('value = ' + value);
      // 输出结果：value = 1
      console.info('newValue = ' + newValue);
      // 输出结果：newValue = null
    }
  }
}
let lru = new ChildLRUCache<number, number>(2);
lru.put(1, 1);
lru.put(2, 2);
lru.put(3, 3);
```

#### contains9+

contains(key: K): boolean

检查当前缓冲区是否包含指定的键。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是要检查的键。

**返回值：**

类型说明boolean如果缓冲区包含指定的键，则返回 true。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.contains(2);
console.info('result = ' + result);
// 输出结果：result = true
```

#### createDefault9+

createDefault(key: K): V

如果在缓冲区未匹配到键，则执行后续操作，参数表示未匹配的键，返回与键关联的值，默认返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是表示未匹配的键。

**返回值：**

类型说明V返回与键关联的值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
let result = pro.createDefault(50);
console.info('result = ' + result);
// 输出结果：result = undefined
```

#### entries9+

entries(): IterableIterator<[K, V]>

返回一个迭代器对象，用于按插入顺序遍历当前对象中的所有键值对（[key, value]）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个可迭代数组。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(3, 15);
let pair = pro.entries();
for (let value of pair) {
  console.info(value[0]+ ', '+ value[1]);
}
// 输出结果：
// 2, 10
// 3, 15
```

#### [Symbol.iterator]9+

[Symbol.iterator](): IterableIterator<[K, V]>

返回键值对形式的二维数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个键值对形式的二维数组。

**示例：**

```ets
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(3, 15);

for (let value of pro) {
  console.info(value[0]+ ', '+ value[1]);
}
// 输出结果：
// 2, 10
// 3, 15
```

#### ScopeComparable8+

ScopeComparable类型的值需要实现compareTo方法，确保传入的数据具有可比性。

**系统能力：** SystemCapability.Utils.Lang

#### compareTo8+

compareTo(other: ScopeComparable): boolean

比较两个值的大小，返回一个布尔值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明other[ScopeComparable](#ZH-CN_TOPIC_0000002497604754__scopecomparable8)是表示要比较的值。

**返回值：**

类型说明boolean调用compareTo的值大于等于传入的值返回true，否则返回false。

**示例：**

构造新类，实现compareTo方法。后续示例代码中，均以此Temperature类为例。

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}
```

#### ScopeType8+

type ScopeType = ScopeComparable | number

表示范围中的值的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

类型说明number表示值的类型为数字。[ScopeComparable](#ZH-CN_TOPIC_0000002497604754__scopecomparable8)表示值的类型为ScopeComparable。

#### ScopeHelper9+

ScopeHelper接口用于描述一个字段的有效范围。构造函数用于创建具有指定下限和上限的对象，并要求这些对象必须具有可比性。

#### constructor9+

constructor(lowerObj: ScopeType, upperObj: ScopeType)

创建指定下限和上限的作用域实例，返回一个ScopeHelper对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lowerObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是指定作用域实例的下限。upperObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是指定作用域实例的上限。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}
let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
console.info("range = " + range);
// 输出结果：range = [30, 40]
```

#### toString9+

toString(): string

该字符串化方法返回当前范围的字符串表示形式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回当前范围的字符串表示形式。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### intersect9+

intersect(range: ScopeHelper): ScopeHelper

获取给定范围和当前范围的交集。当交集为空集时，抛出异常。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明range[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)是传入给定范围。

**返回值：**

类型说明[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)返回给定范围和当前范围的交集。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
let result = range.intersect(rangeFir);
console.info("result = " + result);
// 输出结果：result = [35, 39]
```

#### intersect9+

intersect(lowerObj:ScopeType,upperObj:ScopeType):ScopeHelper

获取当前范围与指定下限和上限范围的交集。当交集为空集时，抛出异常。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lowerObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的下限。upperObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的上限。

**返回值：**

类型说明[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)返回当前范围与给定下限和上限范围的交集。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.intersect(tempMiDF, tempMidS);
console.info("result = " + result);
// 输出结果：result = [35, 39]
```

#### getUpper9+

getUpper(): ScopeType

获取当前范围的上限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)返回当前范围的上限值。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.getUpper();
console.info("result = " + result);
// 输出结果：result = 40
```

#### getLower9+

getLower(): ScopeType

获取当前范围的下限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)返回当前范围的下限值。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.getLower();
console.info("result = " + result);
// 输出结果：result = 30
```

#### expand9+

expand(lowerObj: ScopeType,upperObj: ScopeType): ScopeHelper

创建并返回当前范围与给定下限和上限的并集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lowerObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的下限。upperObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的上限。

**返回值：**

类型说明[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)返回当前范围和给定下限和上限的并集。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.expand(tempMiDF, tempMidS);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### expand9+

expand(range: ScopeHelper): ScopeHelper

创建并返回当前范围和给定范围的并集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明range[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)是传入一个给定范围。

**返回值：**

类型说明[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)返回包括当前范围和给定范围的并集。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
let result = range.expand(rangeFir);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### expand9+

expand(value: ScopeType): ScopeHelper

创建并返回当前范围和给定值的并集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明value[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是传入一个给定值。

**返回值：**

类型说明[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)返回包括当前范围和给定值的并集。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.expand(tempMiDF);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### contains9+

contains(value: ScopeType): boolean

检查给定value是否在当前范围内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明value[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是传入一个给定值。

**返回值：**

类型说明boolean如果给定值包含在当前范围内返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// 输出结果：result = true
```

#### contains9+

contains(range: ScopeHelper): boolean

检查给定range是否在当前范围内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明range[ScopeHelper](#ZH-CN_TOPIC_0000002497604754__scopehelper9)是传入一个给定范围。

**返回值：**

类型说明boolean如果给定范围在当前范围内则返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.ScopeHelper(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// 输出结果：result = false
```

#### clamp9+

clamp(value: ScopeType): ScopeType

将值限定到当前范围内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明value[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是传入的给定值。

**返回值：**

类型说明[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)如果传入的value小于下限，返回lowerObj；如果大于上限值，返回upperObj；如果在当前范围内，返回value。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.clamp(tempMiDF);
console.info("result = " + result);
// 输出结果：result = 35
```

#### Base64Helper9+

Base64Helper类提供Base64编解码和Base64URL编解码功能。Base64编码表包含A-Z、a-z、0-9这62个字符，以及"+"和"/"这两个特殊字符。在编码时，将原始数据按3个字节一组进行划分，得到若干个6位的数字，然后使用Base64编码表中对应的字符来表示这些数字。如果最后剩余1或2个字节，则需要使用"="字符进行补齐。Base64URL编码表包含A-Z、a-z、0-9以及"-"和"_"64个字符，Base64URL编码结果不含"="。

#### constructor9+

constructor()

Base64Helper的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**示例：**

```ets
let base64 = new util.Base64Helper();
```

#### encodeSync9+

encodeSync(src: Uint8Array, options?: Type): Uint8Array

通过输入参数编码后输出Uint8Array对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是待编码的Uint8Array对象。options12+[Type](#ZH-CN_TOPIC_0000002497604754__type10)否

从API version 12开始支持该参数，表示对应的编码格式。

此参数可选，可选值为：util.Type.BASIC和util.Type.BASIC_URL_SAFE，默认值为：util.Type.BASIC。

util.Type.BASIC表示Base64编码。

util.Type.BASIC_URL_SAFE表示Base64URL编码。

**返回值：**

类型说明Uint8Array返回编码后的Uint8Array对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let base64Helper = new util.Base64Helper();
let array = new Uint8Array([115,49,51]);
let result = base64Helper.encodeSync(array);
console.info("result = " + result);
// 输出结果：result = 99,122,69,122
```

#### encodeToStringSync9+

encodeToStringSync(src: Uint8Array, options?: Type): string

将输入的Uint8Array字节数组进行Base64编码，返回一个字符串结果。该方法支持多种编码格式，包括标准Base64编码、MIME格式的Base64编码（带有换行符）、URL安全格式的Base64编码等。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是待编码Uint8Array对象。options10+[Type](#ZH-CN_TOPIC_0000002497604754__type10)否

从API version 10开始支持该参数，表示对应的编码格式。

此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC_URL_SAFE 和util.Type.MIME_URL_SAFE，默认值为：util.Type.BASIC。

- 当参数取值为util.Type.BASIC，表示Base64编码，返回值没有回车符、换行符。

- 当参数取值为util.Type.MIME，表示使用Base64编码。如果返回值超过76个字符，则会在每76个字符处进行换行，并以'\r\n'结束每行。如果返回值少于76个字符，则会抛出异常。

- 当参数取值为util.Type.BASIC_URL_SAFE，表示Base64URL编码，返回值没有回车符、换行符。

- 当参数取值为util.Type.MIME_URL_SAFE，表示Base64URL编码，返回值每一行不超过76个字符，而且每行以'\r\n'符结束。

**返回值：**

类型说明string返回编码后的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
// MIME编码
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.MIME);
console.info("result = " + result);
/*
输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
*/

// BASIC编码
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.BASIC);
console.info("result = " + result);
/*
输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
*/

// MIME_URL_SAFE编码
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.BASIC_URL_SAFE);
console.info("result = " + result);
/*
输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
*/
// MIME_URL_SAFE编码
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.MIME_URL_SAFE);
console.info("result = " + result);
/*
输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
*/
```

#### decodeSync9+

decodeSync(src: Uint8Array | string, options?: Type): Uint8Array

将输入参数解码后输出对应Uint8Array对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array | string是待解码的Uint8Array对象或者字符串。options10+[Type](#ZH-CN_TOPIC_0000002497604754__type10)否

从API version 10开始支持该参数，表示对应的解码格式。

此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC_URL_SAFE和util.Type.MIME_URL_SAFE，默认值为：util.Type.BASIC。

- 当参数取值为util.Type.BASIC，表示Base64解码。

- 当参数取值为util.Type.MIME，表示Base64解码，src入参包含回车符、换行符。

- 当参数取值为util.Type.BASIC_URL_SAFE，表示Base64URL解码。

- 当参数取值为util.Type.MIME_URL_SAFE，表示Base64URL解码，src入参包含回车符、换行符。

**返回值：**

类型说明Uint8Array返回解码后新分配的Uint8Array对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let base64Helper = new util.Base64Helper();
let buff = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\r\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\r\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\r\n';
let result = base64Helper.decodeSync(buff, util.Type.MIME);
console.info("result = " + result);
/*
输出结果：result = 77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
*/
```

#### encode9+

encode(src: Uint8Array, options?: Type): Promise<Uint8Array>

将输入参数异步编码后输出对应Uint8Array对象。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是待编码Uint8Array对象。options12+[Type](#ZH-CN_TOPIC_0000002497604754__type10)否

从API version 12开始支持该参数，表示对应的编码格式。

此参数可选，可选值为：util.Type.BASIC和util.Type.BASIC_URL_SAFE，默认值为：util.Type.BASIC。

util.Type.BASIC表示Base64编码。

util.Type.BASIC_URL_SAFE表示Base64URL编码。

**返回值：**

类型说明Promise<Uint8Array>Promise对象，返回异步编码后新分配的Uint8Array对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let base64Helper = new util.Base64Helper();
let array = new Uint8Array([115,49,51]);
base64Helper.encode(array).then((val) => {
  console.info(val.toString());
  // 输出结果：99,122,69,122
})
```

#### encodeToString9+

encodeToString(src: Uint8Array, options?: Type): Promise<string>

将输入参数异步编码后输出对应文本。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是异步编码输入Uint8Array对象。options10+[Type](#ZH-CN_TOPIC_0000002497604754__type10)否

从API version 10开始支持该参数，表示对应的编码格式。

此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC_URL_SAFE和util.Type.MIME_URL_SAFE，默认值为：util.Type.BASIC。

- 当参数取值为util.Type.BASIC，表示Base64编码，返回值没有回车符、换行符。

- 当参数取值为util.Type.MIME，表示Base64编码，返回值每一行不超过76个字符，而且每行以'\r\n'符结束。

- 当参数取值为util.Type.BASIC_URL_SAFE，表示Base64URL编码，返回值没有回车符、换行符。

- 当参数取值为util.Type.MIME_URL_SAFE，表示Base64URL编码，返回值每一行不超过76个字符，而且每行以'\r\n'符结束。

**返回值：**

类型说明Promise<string>返回异步编码后的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let base64Helper = new util.Base64Helper();
let array = new Uint8Array([77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101]);
base64Helper.encodeToString(array, util.Type.MIME).then((val) => {
  console.info(val);
  /*
  输出结果：TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
  aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
  aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
  */

})
```

#### decode9+

decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>

将输入参数异步解码后输出对应Uint8Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array | string是异步解码输入Uint8Array对象或者字符串。options10+[Type](#ZH-CN_TOPIC_0000002497604754__type10)否

从API version 10开始支持该参数，表示对应的解码格式。

此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC_URL_SAFE和util.Type.MIME_URL_SAFE，默认值为：util.Type.BASIC。

- 当参数取值为util.Type.BASIC时，表示Base64解码。

- 当参数取值为util.Type.MIME时，表示Base64解码，src入参包含回车符、换行符。

- 当参数取值为util.Type.BASIC_URL_SAFE，表示Base64URL解码。

- 当参数取值为util.Type.MIME_URL_SAFE，表示Base64URL解码，src入参包含回车符、换行符。

**返回值：**

类型说明Promise<Uint8Array>返回异步解码后新分配的Uint8Array对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let base64Helper = new util.Base64Helper();
let array = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\r\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\r\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\r\n';
base64Helper.decode(array, util.Type.MIME).then((val) => {
  console.info(val.toString());
  /*
  输出结果：77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
  */
})
```

#### StringDecoder12+

提供将二进制流解码为字符串的能力。支持的编码类型包括：utf-8、iso-8859-2、koi8-r、macintosh、windows-1250、windows-1251、gbk、gb18030、big5、utf-16be、utf-16le等。

#### constructor12+

constructor(encoding?: string)

StringDecoder的构造函数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否输入数据的编码类型。默认值：'utf-8'。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let decoder = new util.StringDecoder();
```

#### write12+

write(chunk: string | Uint8Array): string

返回一个解码后的字符串，确保Uint8Array末尾的任何不完整的多字节字符从返回的字符串中被过滤，并保存在一个内部的buffer中用于下次调用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array是需要解码的字符串。会根据输入的编码类型进行解码，参数为Uint8Array时正常解码，参数为string时会将参数直接返回。

**返回值：**

类型说明string返回解码后的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let decoder = new util.StringDecoder('utf-8');
let input =  new Uint8Array([0xE4, 0xBD, 0xA0, 0xE5, 0xA5, 0xBD]);
const decoded = decoder.write(input);
console.info("decoded:", decoded);
// 输出结果：decoded: 你好
```

#### end12+

end(chunk?: string | Uint8Array): string

结束解码过程，以字符串形式返回存储在内部缓冲区中的所有剩余输入。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array否需要解码的字符串。默认为undefined。

**返回值：**

类型说明string返回解码后的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let decoder = new util.StringDecoder('utf-8');
let input = new Uint8Array([0xE4, 0xBD, 0xA0, 0xE5, 0xA5, 0xBD]);
const writeString = decoder.write(input.slice(0, 5));
const endString = decoder.end(input.slice(5));
console.info("writeString:", writeString);
// 输出结果：writeString: 你
console.info("endString:", endString);
// 输出结果：endString: 好
```

#### Type10+

Base64编码格式枚举。

**系统能力：** SystemCapability.Utils.Lang

名称值说明BASIC0表示BASIC编码格式。**元服务API**：从API version 11开始，该接口支持在元服务中使用。MIME1表示MIME编码格式。**元服务API**：从API version 11开始，该接口支持在元服务中使用。BASIC_URL_SAFE12+2

表示BASIC_URL_SAFE编码格式。

从API version 12开始支持此枚举。**元服务API**：从API version 12开始，该接口支持在元服务中使用。

MIME_URL_SAFE12+3

表示MIME_URL_SAFE编码格式。

从API version 12开始支持此枚举。**元服务API**：从API version 12开始，该接口支持在元服务中使用。

#### types8+

types为不同类型的内置对象提供类型检查，可以避免由于类型错误导致的异常。该模块包含了多个工具函数，用于判断JS对象是否属于各种类型，例如：ArrayBuffer、Map、Set等。

#### constructor8+

constructor()

Types的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let type = new util.types();
```

#### isAnyArrayBuffer8+

isAnyArrayBuffer(value: Object): boolean

检查value是否为ArrayBuffer或SharedArrayBuffer类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是ArrayBuffer或SharedArrayBuffer类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isAnyArrayBuffer(new ArrayBuffer(0));
console.info("result = " + result);
// 输出结果：result = true
```

#### isArrayBufferView8+

isArrayBufferView(value: Object): boolean

检查value是否为ArrayBufferView类型。

ArrayBufferView类型包括：Int8Array、Int16Array、Int32Array、Uint8Array、Uint8ClampedArray、Uint32Array、Float32Array、Float64Array、DataView。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是ArrayBufferView类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isArrayBufferView(new Int8Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isArgumentsObject8+

isArgumentsObject(value: Object): boolean

检查value是否为arguments对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是arguments对象则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
function foo() {
    let result = type.isArgumentsObject(arguments);
    console.info("result = " + result);
}
let f = foo();
// 输出结果：result = true
```

#### isArrayBuffer8+

isArrayBuffer(value: Object): boolean

检查value是否为ArrayBuffer类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是ArrayBuffer类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isArrayBuffer(new ArrayBuffer(0));
console.info("result = " + result);
// 输出结果：result = true
```

#### isAsyncFunction8+

isAsyncFunction(value: Object): boolean

检查value是否为异步函数类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是异步函数则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isAsyncFunction(async () => {});
console.info("result = " + result);
// 输出结果：result = true
```

#### isBooleanObject(deprecated)

isBooleanObject(value: Object): boolean

检查value是否为Boolean对象。

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Boolean对象则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isBooleanObject(new Boolean(true));
console.info("result = " + result);
// 输出结果：result = true
```

#### isBoxedPrimitive(deprecated)

isBoxedPrimitive(value: Object): boolean

检查value是否为Boolean、Number、String或Symbol对象类型。

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Boolean、Number、String或Symbol对象则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isBoxedPrimitive(new Boolean(false));
console.info("result = " + result);
// 输出结果：result = true
```

#### isDataView8+

isDataView(value: Object): boolean

检查value是否为DataView类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是DataView类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
const ab = new ArrayBuffer(20);
let result = type.isDataView(new DataView(ab));
console.info("result = " + result);
// 输出结果：result = true
```

#### isDate8+

isDate(value: Object): boolean

检查value是否为Date类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Date类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isDate(new Date());
console.info("result = " + result);
// 输出结果：result = true
```

#### isExternal8+

isExternal(value: Object): boolean

检查value是否为native External类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是native External类型则返回true，否则返回false。

**示例：**

```ets
// /entry/src/main/cpp/napi_init.cpp
#include "napi/native_api.h"
#include <js_native_api.h>
#include <stdlib.h>

napi_value result;
static napi_value Testexternal(napi_env env, napi_callback_info info) {
    int* raw = (int*) malloc(1024);
    napi_status status = napi_create_external(env, (void*) raw, NULL, NULL, &result);
    if (status != napi_ok) {
        napi_throw_error(env, NULL, "create external failed");
        return NULL;
    }
    return result;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        {"testexternal", nullptr, Testexternal, nullptr, nullptr, nullptr, napi_default, nullptr},
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
// 此处已省略模块注册的代码, 你可能需要自行注册Testexternal方法
...
```

```ets
import testNapi from 'libentry.so';

let type = new util.types();
const data = testNapi.testexternal();
let result = type.isExternal(data);

let result01 = type.isExternal(true);
console.info("result = " + result);
console.info("result01 = " + result01);
// 输出结果：result = true
// 输出结果：result01 = false
```

#### isFloat32Array8+

isFloat32Array(value: Object): boolean

检查value是否为Float32Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Float32Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isFloat32Array(new Float32Array());
console.info("result = " + result);
// 输出结果：result = true
```

#### isFloat64Array8+

isFloat64Array(value: Object): boolean

检查value是否为Float64Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Float64Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isFloat64Array(new Float64Array());
console.info("result = " + result);
// 输出结果：result = true
```

#### isGeneratorFunction8+

isGeneratorFunction(value: Object): boolean

检查value是否是为generator函数类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是generator函数类型则返回true，否则返回false。

**示例：**

```ets
// /entry/src/main/ets/pages/test.ts
export function* foo() {}
```

```ets
import { foo } from './test'

let type = new util.types();
let result = type.isGeneratorFunction(foo);
console.info("result = " + result);
// 输出结果：result = true
```

#### isGeneratorObject8+

isGeneratorObject(value: Object): boolean

检查value是否为generator对象类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是generator对象则返回true，否则返回false。

**示例：**

```ets
// /entry/src/main/ets/pages/test.ts
function* foo() {}
export const generator = foo();
```

```ets
import { generator } from './test'

let type = new util.types();
let result = type.isGeneratorObject(generator);
console.info("result = " + result);
// 输出结果：result = true
```

#### isInt8Array8+

isInt8Array(value: Object): boolean

检查value是否为Int8Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Int8Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isInt8Array(new Int8Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isInt16Array8+

isInt16Array(value: Object): boolean

检查value是否为Int16Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Int16Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isInt16Array(new Int16Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isInt32Array8+

isInt32Array(value: Object): boolean

检查value是否为Int32Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Int32Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isInt32Array(new Int32Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isMap8+

isMap(value: Object): boolean

检查value是否为Map类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Map类型返回则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isMap(new Map());
console.info("result = " + result);
// 输出结果：result = true
```

#### isMapIterator8+

isMapIterator(value: Object): boolean

检查value是否为Map的Iterator类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Map的Iterator类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
const map : Map<number,number> = new Map();
let result = type.isMapIterator(map.keys());
console.info("result = " + result);
// 输出结果：result = true
```

#### isNativeError8+

isNativeError(value: Object): boolean

检查value是否为Error类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Error类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isNativeError(new TypeError());
console.info("result = " + result);
// 输出结果：result = true
```

#### isNumberObject(deprecated)

isNumberObject(value: Object): boolean

检查value是否为Number对象类型。

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Number对象类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isNumberObject(new Number(0));
console.info("result = " + result);
// 输出结果：result = true
```

#### isPromise8+

isPromise(value: Object): boolean

检查value是否为Promise类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Promise类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isPromise(Promise.resolve(1));
console.info("result = " + result);
// 输出结果：result = true
```

#### isProxy8+

isProxy(value: Object): boolean

检查value是否为Proxy类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Proxy类型则返回true，否则返回false。

**示例：**

```ets
class Target{
}
let type = new util.types();
const target : Target = {};
const proxy = new Proxy(target, target);
let result = type.isProxy(proxy);
console.info("result = " + result);
// 输出结果：result = true
```

#### isRegExp8+

isRegExp(value: Object): boolean

检查value是否为RegExp类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是RegExp类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isRegExp(new RegExp('abc'));
console.info("result = " + result);
// 输出结果：result = true
```

#### isSet8+

isSet(value: Object): boolean

检查value是否为Set类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Set类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let set : Set<number> = new Set();
let result = type.isSet(set);
console.info("result = " + result);
// 输出结果：result = true
```

#### isSetIterator8+

isSetIterator(value: Object): boolean

检查value是否为Set的Iterator类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Set的Iterator类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
const set : Set<number> = new Set();
let result = type.isSetIterator(set.keys());
console.info("result = " + result);
// 输出结果：result = true
```

#### isStringObject(deprecated)

isStringObject(value: Object): boolean

检查value是否为String对象类型。

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是String对象类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isStringObject(new String('foo'));
console.info("result = " + result);
// 输出结果：result = true
```

#### isSymbolObject(deprecated)

isSymbolObject(value: Object): boolean

检查value是否为Symbol对象类型。

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Symbol对象类型为则返回true，否则返回false。

**示例：**

```ets
// /entry/src/main/ets/pages/test.ts
export const symbols = Symbol('foo');
```

```ets
import { symbols } from './test'

let type = new util.types();
let result = type.isSymbolObject(Object(symbols));
console.info("result = " + result);
// 输出结果：result = true
```

#### isTypedArray8+

isTypedArray(value: Object): boolean

检查value是否为TypedArray类型。

TypedArray类型，包括Int8Array、Int16Array、Int32Array、Uint8Array、Uint8ClampedArray、Uint16Array、Uint32Array、Float32Array、Float64Array、BigInt64Array、BigUint64Array。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是TypedArray包含的类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isTypedArray(new Float64Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isUint8Array8+

isUint8Array(value: Object): boolean

检查value是否为Uint8Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Uint8Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isUint8Array(new Uint8Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isUint8ClampedArray8+

isUint8ClampedArray(value: Object): boolean

检查value是否为Uint8ClampedArray数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Uint8ClampedArray数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isUint8ClampedArray(new Uint8ClampedArray([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isUint16Array8+

isUint16Array(value: Object): boolean

检查value是否为Uint16Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Uint16Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isUint16Array(new Uint16Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isUint32Array8+

isUint32Array(value: Object): boolean

检查value是否为Uint32Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Uint32Array数组类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isUint32Array(new Uint32Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isWeakMap8+

isWeakMap(value: Object): boolean

检查value是否为WeakMap类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是WeakMap类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let value : WeakMap<object, number> = new WeakMap();
let result = type.isWeakMap(value);
console.info("result = " + result);
// 输出结果：result = true
```

#### isWeakSet8+

isWeakSet(value: Object): boolean

检查value是否为WeakSet类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是WeakSet类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isWeakSet(new WeakSet());
console.info("result = " + result);
// 输出结果：result = true
```

#### isBigInt64Array8+

isBigInt64Array(value: Object): boolean

检查value是否为BigInt64Array类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是BigInt64Array类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isBigInt64Array(new BigInt64Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isBigUint64Array8+

isBigUint64Array(value: Object): boolean

检查value是否为BigUint64Array类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是BigUint64Array类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isBigUint64Array(new BigUint64Array([]));
console.info("result = " + result);
// 输出结果：result = true
```

#### isModuleNamespaceObject8+

isModuleNamespaceObject(value: Object): boolean

检查value是否为Module Namespace Object类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是Module Namespace Object类型则返回true，否则返回false。

**示例：**

```ets
// /entry/src/main/ets/pages/test.ts
export function func() {
  console.info("hello world");
}
```

```ets
import * as nameSpace from './test';

let type = new util.types();
let result = type.isModuleNamespaceObject(nameSpace);
console.info("result = " + result);
// 输出结果：result = true
```

#### isSharedArrayBuffer8+

isSharedArrayBuffer(value: Object): boolean

检查value是否为SharedArrayBuffer类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject是待检测对象。

**返回值：**

类型说明boolean如果是SharedArrayBuffer类型则返回true，否则返回false。

**示例：**

```ets
let type = new util.types();
let result = type.isSharedArrayBuffer(new SharedArrayBuffer(0));
console.info("result = " + result);
// 输出结果：result = true
```

#### AutoFinalizer<T>22+

AutoFinalizer是一个接口类，用于在ArkTS对象释放时提供回调。通过实现回调接口，开发者可自定义对象被回收时自动触发的资源清理逻辑。

AutoFinalizer<T>需要和AutoFinalizerCleaner<T>一起使用，只实现该接口类没有任何功能。

#### onFinalization22+

onFinalization(heldValue: T): void

开发者需要实现该接口，定义对象被回收时自动触发的资源清理回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明heldValueT是当监听的对象被回收时，该值会被传递给onFinalization回调方法。

#### AutoFinalizerCleaner<T>22+

AutoFinalizerCleaner是用于关联对象生命周期与资源清理逻辑的工具类。主要的作用是将实现了AutoFinalizer<T>接口的对象与特定值绑定，当对象被回收时自动触发资源清理回调。

#### register<T>22+

static register<T>(obj: AutoFinalizer<T>, heldValue: T): void

将AutoFinalizer接口的对象与输入值关联，当对象被回收时触发资源清理的回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明obj[AutoFinalizer<T>](#ZH-CN_TOPIC_0000002497604754__autofinalizert22)是实现了AutoFinalizer接口的对象，其onFinalization方法会在该对象被回收时调用。heldValueT是当监听的对象被回收时，该值会被传递给obj.onFinalization方法。

**示例：**

```ets
class DeviceManageViewModel implements util.AutoFinalizer<string> {
  constructor(heldValue: string) {
    util.AutoFinalizerCleaner.register(this, heldValue);
  }

  onFinalization(heldValue: string) {
    console.info("onFinalization: ", heldValue);
    // 等待触发垃圾回收，触发后会输出结果：onFinalization: test
  }
}

const device = new DeviceManageViewModel("test");
```

#### LruBuffer(deprecated)

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache9+](#ZH-CN_TOPIC_0000002497604754__lrucache9)替代。

#### 属性

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

名称类型只读可选说明lengthnumber是否当前缓冲区中值的总数。

**示例：**

```ets
let pro : util.LruBuffer<number,number>= new util.LruBuffer();
pro.put(2,10);
pro.put(1,8);
let result = pro.length;
console.info("result = " + result);
// 输出结果：result = 2
```

#### constructor(deprecated)

constructor(capacity?: number)

构造函数用于创建一个新的LruBuffer实例，默认容量为64。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.constructor9+](#ZH-CN_TOPIC_0000002497604754__constructor9-3)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明capacitynumber否指示要为缓冲区自定义的容量，默认值为64。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
```

#### updateCapacity(deprecated)

updateCapacity(newCapacity: number): void

将缓冲区容量更新为指定容量，如果newCapacity小于或等于0，则抛出异常。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.updateCapacity9+](#ZH-CN_TOPIC_0000002497604754__updatecapacity9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明newCapacitynumber是指示要为缓冲区自定义的容量。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.updateCapacity(100);
```

#### toString(deprecated)

toString(): string

返回对象的字符串表示形式。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.toString9+](#ZH-CN_TOPIC_0000002497604754__tostring9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回对象的字符串表示形式。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
pro.remove(20);
let result = pro.toString();
console.info("result = " + result);
// 输出结果：result = Lrubuffer[ maxSize = 64, hits = 1, misses = 0, hitRate = 100% ]
```

#### getCapacity(deprecated)

getCapacity(): number

获取当前缓冲区的容量。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getCapacity9+](#ZH-CN_TOPIC_0000002497604754__getcapacity9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回当前缓冲区的容量。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.getCapacity();
console.info("result = " + result);
// 输出结果：result = 64
```

#### clear(deprecated)

clear(): void

清除当前缓冲区中的键值对，后续调用afterRemoval()方法执行操作。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.clear9+](#ZH-CN_TOPIC_0000002497604754__clear9)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.length;
pro.clear();
```

#### getCreateCount(deprecated)

getCreateCount(): number

获取createDefault()返回值的次数。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getCreateCount9+](#ZH-CN_TOPIC_0000002497604754__getcreatecount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回createDefault()返回值的次数。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(1,8);
let result = pro.getCreateCount();
console.info("result = " + result);
// 输出结果：result = 0
```

#### getMissCount(deprecated)

getMissCount(): number

获取查询值不匹配的次数。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getMissCount9+](#ZH-CN_TOPIC_0000002497604754__getmisscount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回查询值不匹配的次数。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
let result = pro.getMissCount();
console.info("result = " + result);
// 输出结果：result = 0
```

#### getRemovalCount(deprecated)

getRemovalCount(): number

获取从缓冲区中逐出值的次数。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getRemovalCount9+](#ZH-CN_TOPIC_0000002497604754__getremovalcount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回从缓冲区中驱逐的次数。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.updateCapacity(2);
pro.put(50,22);
let result = pro.getRemovalCount();
console.info("result = " + result);
// 输出结果：result = 0
```

#### getMatchCount(deprecated)

getMatchCount(): number

获取查询值匹配成功的次数。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getMatchCount9+](#ZH-CN_TOPIC_0000002497604754__getmatchcount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回查询值匹配成功的次数。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
let result = pro.getMatchCount();
console.info("result = " + result);
// 输出结果：result = 1
```

#### getPutCount(deprecated)

getPutCount(): number

获取将值添加到缓冲区的次数。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getPutCount9+](#ZH-CN_TOPIC_0000002497604754__getputcount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回将值添加到缓冲区的次数。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.getPutCount();
console.info("result = " + result);
// 输出结果：result = 1
```

#### isEmpty(deprecated)

isEmpty(): boolean

检查当前缓冲区是否为空。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.isEmpty9+](#ZH-CN_TOPIC_0000002497604754__isempty9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean如果当前缓冲区不包含任何值，则返回true。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.isEmpty();
console.info("result = " + result);
// 输出结果：result = false
```

#### get(deprecated)

get(key: K): V | undefined

表示要查询的键。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.get9+](#ZH-CN_TOPIC_0000002497604754__get9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是要查询的键。

**返回值：**

类型说明V | undefined如果指定的键存在于缓冲区中，则返回与键关联的值；否则返回undefined。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result  = pro.get(2);
console.info("result = " + result);
// 输出结果：result = 10
```

#### put(deprecated)

put(key: K,value: V): V

将键值对添加到缓冲区。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.put9+](#ZH-CN_TOPIC_0000002497604754__put9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是要添加的密钥。valueV是指示与要添加的键关联的值。

**返回值：**

类型说明V返回与添加的键关联的值；如果要添加的键已经存在，则返回原始值，如果键或值为空，则抛出此异常。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.put(2,10);
console.info("result = " + result);
// 输出结果：result = 10
```

#### values(deprecated)

values(): V[]

获取当前缓冲区中所有值从最近访问到最近最少访问的顺序列表。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.values9+](#ZH-CN_TOPIC_0000002497604754__values9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明V []按从最近访问到最近最少访问的顺序返回当前缓冲区中所有值的列表。

**示例：**

```ets
let pro : util.LruBuffer<number|string,number|string> = new util.LruBuffer();
pro.put(2,10);
pro.put(2,"anhu");
pro.put("afaf","grfb");
let result = pro.values();
console.info("result = " + result);
// 输出结果：result = anhu,grfb
```

#### keys(deprecated)

keys(): K[]

获取当前缓冲区中所有键从最近访问到最近最少访问的升序列表。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.keys9+](#ZH-CN_TOPIC_0000002497604754__keys9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明K []按升序返回当前缓冲区中所有键的列表，从最近访问到最近最少访问。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.keys();
console.info("result = " + result);
// 输出结果：result = 2
```

#### remove(deprecated)

remove(key: K): V | undefined

删除当前缓冲区中指定的键及其关联的值。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.remove9+](#ZH-CN_TOPIC_0000002497604754__remove9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是要删除的密钥。

**返回值：**

类型说明V | undefined返回一个包含已删除键值对的Optional对象；如果key不存在，则返回一个空的Optional对象，如果key为null，则抛出异常。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.remove(20);
console.info("result = " + result);
// 输出结果：result = undefined
```

#### afterRemoval(deprecated)

afterRemoval(isEvict: boolean,key: K,value: V,newValue: V): void

删除值后执行后续操作。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.afterRemoval9+](#ZH-CN_TOPIC_0000002497604754__afterremoval9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明isEvictboolean是因容量不足而调用该方法时，参数值为true，其他情况为false。keyK是表示删除的键。valueV是表示删除的值。newValueV是如果已调用put方法并且要添加的键已经存在，则参数值是关联的新值。其他情况下参数值为空。

**示例：**

```ets
class ChildLruBuffer<K, V> extends util.LruBuffer<K, V> {
  constructor(capacity?: number) {
    super(capacity);
  }

  afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void {
    if (isEvict === true) {
      console.info('key: ' + key);
      // 输出结果：key: 11
      console.info('value: ' + value);
      // 输出结果：value: 1
      console.info('newValue: ' + newValue);
      // 输出结果：newValue: null
    }
  }
}
let lru: ChildLruBuffer<number, number> = new ChildLruBuffer(2);
lru.put(11, 1);
lru.put(22, 2);
lru.put(33, 3);
```

#### contains(deprecated)

contains(key: K): boolean

检查当前缓冲区是否包含指定的键。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.contains9+](#ZH-CN_TOPIC_0000002497604754__contains9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是表示要检查的键。

**返回值：**

类型说明boolean如果缓冲区包含指定的键，则返回 true。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.contains(20);
console.info('result = ' + result);
// 输出结果：result = false
```

#### createDefault(deprecated)

createDefault(key: K): V

如果未计算特定键的值，则执行后续操作，参数表示丢失的键，返回与键关联的值。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.createDefault9+](#ZH-CN_TOPIC_0000002497604754__createdefault9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是表示丢失的键。

**返回值：**

类型说明V返回与键关联的值。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.createDefault(50);
```

#### entries(deprecated)

entries(): IterableIterator<[K, V]>

允许迭代包含在这个对象中的所有键值对。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.entries9+](#ZH-CN_TOPIC_0000002497604754__entries9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个可迭代数组。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.entries();
```

#### [Symbol.iterator](deprecated)

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个键值对形式的二维数组。

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.[Symbol.iterator]9+](#ZH-CN_TOPIC_0000002497604754__symboliterator9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个键值对形式的二维数组。

**示例：**

```ets
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro[Symbol.iterator]();
```

#### Scope(deprecated)

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper9+](#ZH-CN_TOPIC_0000002497604754__scopehelper9)替代。

#### constructor(deprecated)

constructor(lowerObj: ScopeType, upperObj: ScopeType)

创建指定下限和上限的作用域实例，并返回一个Scope对象。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.constructor9+](#ZH-CN_TOPIC_0000002497604754__constructor9-4)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lowerObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是指定作用域实例的下限。upperObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是指定作用域实例的上限。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
console.info("range = " + range);
// 输出结果：range = [30, 40]
```

#### toString(deprecated)

toString(): string

该字符串化方法返回一个包含当前范围的字符串表示形式。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.toString9+](#ZH-CN_TOPIC_0000002497604754__tostring9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回包含当前范围对象的字符串表示形式。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### intersect(deprecated)

intersect(range: Scope): Scope

获取给定范围和当前范围的交集。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.intersect9+](#ZH-CN_TOPIC_0000002497604754__intersect9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明range[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)是传入一个给定范围。

**返回值：**

类型说明[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)返回给定范围和当前范围的交集。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let rangeFir = new util.Scope(tempMiDF, tempMidS);
let result = range.intersect(rangeFir );
console.info("result = " + result);
  // 输出结果：result = [35, 39]
```

#### intersect(deprecated)

intersect(lowerObj:ScopeType,upperObj:ScopeType):Scope

获取当前范围与给定下限和上限范围的交集。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.intersect9+](#ZH-CN_TOPIC_0000002497604754__intersect9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lowerObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的下限。upperObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的上限。

**返回值：**

类型说明[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)返回当前范围与给定下限和上限范围的交集。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.Scope(tempLower, tempUpper);
let result = range.intersect(tempMiDF, tempMidS);
console.info("result = " + result);
// 输出结果：result = [35, 39]
```

#### getUpper(deprecated)

getUpper(): ScopeType

获取当前范围的上限。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.getUpper9+](#ZH-CN_TOPIC_0000002497604754__getupper9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)返回当前范围的上限值。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let result = range.getUpper();
console.info("result = " + result);
// 输出结果：result = 40
```

#### getLower(deprecated)

getLower(): ScopeType

获取当前范围的下限。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.getLower9+](#ZH-CN_TOPIC_0000002497604754__getlower9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)返回当前范围的下限值。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let result = range.getLower();
console.info("result = " + result);
// 输出结果：result = 30
```

#### expand(deprecated)

expand(lowerObj: ScopeType,upperObj: ScopeType): Scope

创建并返回包括当前范围和给定下限和上限的并集。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.expand9+](#ZH-CN_TOPIC_0000002497604754__expand9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lowerObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的下限。upperObj[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是给定范围的上限。

**返回值：**

类型说明[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)返回当前范围和给定下限和上限的并集。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.Scope(tempLower, tempUpper);
let result = range.expand(tempMiDF, tempMidS);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### expand(deprecated)

expand(range: Scope): Scope

创建并返回包括当前范围和给定范围的并集。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.expand9+](#ZH-CN_TOPIC_0000002497604754__expand9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明range[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)是传入一个给定范围。

**返回值：**

类型说明[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)返回包括当前范围和给定范围的并集。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.Scope(tempLower, tempUpper);
let rangeFir = new util.Scope(tempMiDF, tempMidS);
let result = range.expand(rangeFir);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### expand(deprecated)

expand(value: ScopeType): Scope

创建并返回包括当前范围和给定值的并集。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.expand9+](#ZH-CN_TOPIC_0000002497604754__expand9-2)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明value[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是传入一个给定值。

**返回值：**

类型说明[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)返回包括当前范围和给定值的并集。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.Scope(tempLower, tempUpper);
let result = range.expand(tempMiDF);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

#### contains(deprecated)

contains(value: ScopeType): boolean

检查给定value是否包含在当前范围内。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.contains9+](#ZH-CN_TOPIC_0000002497604754__contains9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明value[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是传入一个给定值。

**返回值：**

类型说明boolean如果给定值包含在当前范围内返回true，否则返回false。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.Scope(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// 输出结果：result = true
```

#### contains(deprecated)

contains(range: Scope): boolean

检查给定range是否在当前范围内。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.contains9+](#ZH-CN_TOPIC_0000002497604754__contains9-2)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明range[Scope](#ZH-CN_TOPIC_0000002497604754__scopedeprecated)是传入一个给定范围。

**返回值：**

类型说明boolean如果给定范围包含在当前范围内返回true，否则返回false。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.Scope(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// 输出结果：result = false
```

#### clamp(deprecated)

clamp(value: ScopeType): ScopeType

将给定值限定到当前范围内。

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.clamp9+](#ZH-CN_TOPIC_0000002497604754__clamp9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明value[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)是传入的给定值。

**返回值：**

类型说明[ScopeType](#ZH-CN_TOPIC_0000002497604754__scopetype8)如果传入的value小于下限，则返回lowerObj；如果大于上限值则返回upperObj；如果在当前范围内，则返回value。

**示例：**

```ets
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.Scope(tempLower, tempUpper);
let result = range.clamp(tempMiDF);
console.info("result = " + result);
// 输出结果：result = 35
```

#### Base64(deprecated)

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper9+](#ZH-CN_TOPIC_0000002497604754__base64helper9)替代。

#### constructor(deprecated)

constructor()

Base64的构造函数。

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.constructor9+](#ZH-CN_TOPIC_0000002497604754__constructor9-5)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let base64 = new  util.Base64();
```

#### encodeSync(deprecated)

encodeSync(src: Uint8Array): Uint8Array

将输入的Uint8Array字节数组进行Base64编码，返回编码后的Uint8Array数组。

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encodeSync9+](#ZH-CN_TOPIC_0000002497604754__encodesync9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是编码输入Uint8数组。

**返回值：**

类型说明Uint8Array返回编码后新分配的Uint8数组。

**示例：**

```ets
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
let result = base64.encodeSync(array);
console.info("result = " + result);
// 输出结果：result = 99,122,69,122
```

#### encodeToStringSync(deprecated)

encodeToStringSync(src: Uint8Array): string

将输入的Uint8Array字节数组进行Base64编码，返回编码后的字符串结果。

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encodeToStringSync9+](#ZH-CN_TOPIC_0000002497604754__encodetostringsync9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是编码输入Uint8数组。

**返回值：**

类型说明string返回编码后的字符串。

**示例：**

```ets
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
let result = base64.encodeToStringSync(array);
console.info("result = " + result);
// 输出结果：result = czEz
```

#### decodeSync(deprecated)

decodeSync(src: Uint8Array | string): Uint8Array

通过输入参数解码后输出对应文本。

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.decodeSync9+](#ZH-CN_TOPIC_0000002497604754__decodesync9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array | string是解码输入Uint8数组或者字符串。

**返回值：**

类型说明Uint8Array返回解码后新分配的Uint8数组。

**示例：**

```ets
let base64 = new util.Base64();
let buff = 'czEz';
let result = base64.decodeSync(buff);
console.info("result = " + result);
// 输出结果：result = 115,49,51
```

#### encode(deprecated)

encode(src: Uint8Array): Promise<Uint8Array>

通过输入参数异步编码后输出对应文本。

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encode9+](#ZH-CN_TOPIC_0000002497604754__encode9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是异步编码输入Uint8数组。

**返回值：**

类型说明Promise<Uint8Array>返回异步编码后新分配的Uint8数组。

**示例：**

```ets
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
base64.encode(array).then((val) => {
  console.info(val.toString());
  // 输出结果：99,122,69,122
})
```

#### encodeToString(deprecated)

encodeToString(src: Uint8Array): Promise<string>

通过输入参数异步编码后输出对应文本。

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encodeToString9+](#ZH-CN_TOPIC_0000002497604754__encodetostring9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array是异步编码输入Uint8数组。

**返回值：**

类型说明Promise<string>返回异步编码后的字符串。

**示例：**

```ets
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
base64.encodeToString(array).then((val) => {
    console.info(val);
    // 输出结果：czEz
})
```

#### decode(deprecated)

decode(src: Uint8Array | string): Promise<Uint8Array>

将输入参数异步解码后输出对应文本。

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.decode9+](#ZH-CN_TOPIC_0000002497604754__decode9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明srcUint8Array | string是异步解码输入Uint8数组或者字符串。

**返回值：**

类型说明Promise<Uint8Array>返回异步解码后新分配的Uint8数组。

**示例：**

```ets
let base64 = new util.Base64();
let array = new Uint8Array([99,122,69,122]);
base64.decode(array).then((val) => {
  console.info(val.toString());
  // 输出结果：115,49,51
})
```