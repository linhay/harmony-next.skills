# Class (Uint32Array)

一种线性数据结构，底层基于[ArkTS ArrayBuffer](Class (ArrayBuffer).md)实现。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

**装饰器类型：**@Sendable

#### 导入模块

```ets
import { collections } from '@kit.ArkTS';
```

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称类型只读可选说明bufferArrayBuffer是否ArkTS Uint32Array底层使用的buffer。byteLengthnumber是否ArkTS Uint32Array的所占的字节数。byteOffsetnumber是否ArkTS Uint32Array距离其ArrayBuffer起始位置的偏移。lengthnumber是否ArkTS Uint32Array元素个数。BYTES_PER_ELEMENTnumber是否ArkTS Uint32Array中每个元素所占用的字节数。

#### constructor

constructor()

构造函数，用于创建一个空ArkTS Uint32Array对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200012The Uint32Array's constructor cannot be directly invoked.

**示例：**

```ets
let uint32Array: collections.Uint32Array = new collections.Uint32Array();
```

#### constructor

constructor(length: number)

构造函数，用于创建一个指定长度的ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lengthnumber是用于指定ArkTS Uint32Array的长度。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The Uint32Array's constructor cannot be directly invoked.

**示例：**

```ets
// 以长度参数构造对象
let uint32Array: collections.Uint32Array = new collections.Uint32Array(12);
```

#### constructor

constructor(elements: Iterable<number>)

构造函数，以Iterable创建一个ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementsIterable<number>是可迭代数字集合，用于构造ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The Uint32Array's constructor cannot be directly invoked.

**示例：**

```ets
// 从一个Iterable构造对象
let set: Set<number> = new Set<number>([1, 2, 3]);
let array: collections.Uint32Array = new collections.Uint32Array(set);
// Uint32Array [1, 2, 3]
```

#### constructor

constructor(array: ArrayLike<number> | ArrayBuffer)

构造函数，以ArrayLike或ArkTS ArrayBuffer创建一个ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明arrayArrayLike<number> | ArrayBuffer是用于构造ArkTS Uint32Array的对象。当参数类型是ArrayBuffer时buffer所占的字节数须是4的整数倍。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The Uint32Array's constructor cannot be directly invoked.

**示例：**

```ets
// 例1 从一个ArrayLike构造对象
let arrayLike = [1, 3, 5];
let array: collections.Uint32Array = new collections.Uint32Array(arrayLike);
```

```ets
// 例2 从一个ArrayBuffer构造对象
let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(12);
let array: collections.Uint32Array = new collections.Uint32Array(arrayBuffer);
```

```ets
// 例3 从另一ArkTS Uint32Array构造对象
let arrayLike = [1, 3, 5];
// uint32Array1 [1, 3, 5]
let uint32Array1: collections.Uint32Array = new collections.Uint32Array(arrayLike);
// uint32Array2 [1, 3, 5]
let uint32Array2: collections.Uint32Array = new collections.Uint32Array(uint32Array1);
```

#### constructor

constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)

构造函数，以ArrayBuffer创建一个ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明bufferArrayBuffer是用于构造ArkTS Uint32Array的ArrayBuffer对象。buffer所占的字节数须是4的整数倍。byteOffsetnumber否指定buffer的字节偏移，从0开始，默认为0。lengthnumber否指定ArkTS Uint32Array的长度，默认为0。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The Uint32Array's constructor cannot be directly invoked.

**示例：**

```ets
let uint32Array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5, 6]);
console.info("byteLength: " + uint32Array.buffer.byteLength); // byteLength: 24
// 从uint32Array对应buffer第4个字节开始，长度为5
let uint32Array1: collections.Uint32Array = new collections.Uint32Array(uint32Array.buffer, 4, 5);
console.info("[" + uint32Array1 + "]"); // [2, 3, 4, 5, 6]
```

#### from

static from(arrayLike: ArrayLike<number>): Uint32Array

从一个ArrayLike或者可迭代对象中创建一个ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明arrayLikeArrayLike<number>是用于构造ArkTS Uint32Array的ArrayLike对象。

**返回值：**

类型说明Uint32Array新创建的ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
let arrayLike = [1, 3, 5];
let array: collections.Uint32Array = collections.Uint32Array.from(arrayLike); // array [1, 3, 5]
```

#### from

static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint32Array

从一个ArrayLike中创建一个ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明arrayLikeArrayLike<T>是用于构造ArrayLike对象。mapFn[TypedArrayFromMapFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayfrommapfn)<T, number>是映射函数。

**返回值：**

类型说明Uint32Array新创建的ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
// 例1 从一个对象创建
let array: collections.Uint32Array = collections.Uint32Array.from<number>(
  { length: 5 }, (v: Object, k: number) => k);
// Uint32Array [0, 1, 2, 3, 4]
```

```ets
// 例2 从一个字符数组创建
let array: collections.Uint32Array = collections.Uint32Array.from<string>(
  ["1", "3", "5"], (v: string, k: number) => parseInt(v));
// Uint32Array [1, 3, 5]
```

```ets
// 例3 从一个字符串创建
let array: collections.Uint32Array = collections.Uint32Array.from<string>(
  "12345", (v: string, k: number) => parseInt(v));
// Uint32Array [1, 2, 3, 4, 5]
```

#### from

static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint32Array

从一个可迭代对象中创建一个ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明arrayLikeIterable<number>是用于构造的可迭代对象。mapFn[TypedArrayFromMapFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayfrommapfn)<number, number>否映射函数。如果省略，则不对元素进行加工处理。

**返回值：**

类型说明Uint32Array新创建的ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
// 例1 不指定映射函数
let set: Set<number> = new Set<number>([1, 2, 3]);
let array: collections.Uint32Array = collections.Uint32Array.from(set);
// Uint32Array [1, 2, 3]
```

```ets
// 例2 指定映射函数
let set: Set<number> = new Set<number>([1, 2, 3]);
let array: collections.Uint32Array = collections.Uint32Array.from(
  set, (v: number, k: number) => v + k);
// Uint32Array [1, 3, 5]
```

#### of18+

static of(...items: number[]): Uint32Array

通过可变数量的参数创建一个新的ArkTS Uint32Array对象，参数个数可以是0个、1个或者多个。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明itemsnumber[]否用于创建数组的元素，参数个数可以是0个、1个或者多个。

**返回值：**

类型说明Uint32Array新的ArkTS Uint32Array实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error: Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.

**示例：**

```ets
let arr: collections.Uint32Array = collections.Uint32Array.of(1, 2, 3, 4);
console.info(arr.toString()); // 预期输出：1,2,3,4
```

#### toString18+

toString(): string

ArkTS Uint32Array转换为字符串。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string一个包含数组所有元素的字符串。

**错误码：**

以下错误码详细介绍请参考[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The toString method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array = new collections.Uint32Array([1, 2, 3, 4, 5]);
let stringArray = array.toString();
console.info(stringArray); // 预期输出：1,2,3,4,5
```

#### toLocaleString18+

toLocaleString(): string

根据当前应用的系统地区获取符合当前文化习惯的数字表示形式，让每个元素调用自己的toLocaleString方法把数字转换为字符串，然后使用逗号将每个元素的结果字符串按照顺序拼接成字符串。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string一个包含数组所有元素的字符串。

**错误码：**

以下错误码详细介绍请参考[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The toLocaleString method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
// 当前应用所在系统为法国地区
let array = new collections.Uint32Array([1000, 2000, 3000]);
let stringArray = array.toLocaleString();
console.info(stringArray); // 预期输出：1,000, 2,000, 3,000
```

#### copyWithin

copyWithin(target: number, start: number, end?: number): Uint32Array

从ArkTS Uint32Array指定范围内的元素依次拷贝到目标位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明targetnumber是目标起始位置的下标，如果target < 0，则会从target + array.length位置开始。startnumber是源起始位置下标，如果start < 0，则会从start + Uint32Array.length位置开始。endnumber否源终止位置下标（不包含end位置的元素），如果end < 0，则会从end + Uint32Array.length位置终止。默认为ArkTS Uint32Array的长度。

**返回值：**

类型说明Uint32Array修改后的Uint32Array。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The copyWithin method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5, 6, 7, 8]);
let copied: collections.Uint32Array = array.copyWithin(3, 1, 3);
// Uint32Array [1, 2, 3, 2, 3, 6, 7, 8]
```

#### some

some(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean

测试ArkTS Uint32Array中的是否存在元素满足指定条件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明predicate[TypedArrayPredicateFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarraypredicatefn)<number, Uint32Array>是用于测试的断言函数。

**返回值：**

类型说明boolean如果存在元素满足指定条件返回true，否则返回false。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The some method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let arrayLike = [10, 20, 30, 40, 50];
let uint32Array: collections.Uint32Array = new collections.Uint32Array(arrayLike);
uint32Array.some((element: number) => element < 1); // false
```

#### every

every(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean

测试ArkTS Uint32Array中的所有元素是否满足指定条件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明predicate[TypedArrayPredicateFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarraypredicatefn)<number, Uint32Array>是用于测试的断言函数。

**返回值：**

类型说明boolean如果所有元素都满足指定条件则返回true，否则返回false。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The every method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let arrayLike = [10, 20, 30, 40, 50];
let uint32Array: collections.Uint32Array = new collections.Uint32Array(arrayLike);
uint32Array.every((element: number) => element > 1);  // true
```

#### fill

fill(value: number, start?: number, end?: number): Uint32Array

使用特定值填充ArkTS Uint32Array指定范围的全部元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是待填充的值。startnumber否开始填充的索引，如果start < 0，则会从start + Uint32Array.length位置开始。默认值为0。endnumber否结束填充的索引（不包括该元素），如果end < 0，则会到end + Uint32Array.length位置结束。默认为ArkTS Uint32Array的长度。

**返回值：**

类型说明Uint32Array填充后的Uint32Array。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The fill method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let arrayLike = [1, 2, 3];
new collections.Uint32Array(arrayLike).fill(4); // Uint32Array [4, 4, 4]
new collections.Uint32Array(arrayLike).fill(4, 1); // Uint32Array [1, 4, 4]
new collections.Uint32Array(arrayLike).fill(4, 1, 2); // Uint32Array [1, 4, 3]
```

#### filter

filter(predicate: TypedArrayPredicateFn<number, Uint32Array>): Uint32Array

返回一个新ArkTS Uint32Array，其包含满足指定条件的所有元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明predicate[TypedArrayPredicateFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarraypredicatefn)<number, Uint32Array>是用于元素过滤的断言函数。

**返回值：**

类型说明Uint32Array过滤后的ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The filter method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([0, 1, 2, 3, 4]);
let filtered: collections.Uint32Array = array.filter((element: number) => element % 2 == 0);
// Uint32Array [0, 2, 4]
```

#### find

find(predicate: TypedArrayPredicateFn<number, Uint32Array>): number | undefined

返回ArkTS Uint32Array中第一个满足指定条件的元素的值，如果所有元素都不满足，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明predicate[TypedArrayPredicateFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarraypredicatefn)<number, Uint32Array>是用于元素查找的断言函数。

**返回值：**

类型说明number | undefined第一个满足条件的元素的值；如果所有元素都不满足条件，则返回undefined。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The find method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([0, 1, 2, 3, 4]);
array.find((element: number) => element > 2); // 3
array.find((element: number) => element > 4); // undefined
```

#### findIndex

findIndex(predicate: TypedArrayPredicateFn<number, Uint32Array>): number

返回ArkTS Uint32Array中第一个满足指定条件的元素索引，如果所有元素都不满足，则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明predicate[TypedArrayPredicateFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarraypredicatefn)<number, Uint32Array>是用于元素查找的断言函数。

**返回值：**

类型说明number第一个满足条件的元素索引；如果所有元素都不满足条件，则返回-1。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The findIndex method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
const array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let foundIndex: number = array.findIndex((element: number) => element % 2 === 0); // 1
```

#### forEach

forEach(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): void

对ArkTS Uint32Array中的每个元素执行提供的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn[TypedArrayForEachCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayforeachcallback)<number, Uint32Array>是用于对每个元素执行的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The forEach method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let uint32Array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3]);
uint32Array.forEach((value: number, index: number, array: collections.Uint32Array) => {
  console.info(`Element ${value} at index ${index}`);
});
```

#### indexOf

indexOf(searchElement: number, fromIndex?: number): number

返回在ArkTS Uint32Array中给定元素的第一个索引，如果不存在，则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明searchElementnumber是待索引的值。fromIndexnumber否搜索的起始下标。默认值为0。如果下标大于等于ArkTS Uint32Array的长度，则返回-1。如果提供的下标值是负数，则被当做距离数组尾部的偏移，从前到后搜索。

**返回值：**

类型说明number数组中元素的第一个索引；没有找到，则返回-1。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The indexOf method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([3, 5, 9]);
array.indexOf(3); // 0
array.indexOf(7); // -1
array.indexOf(9, 2); // 2
array.indexOf(9, -2); // 2
```

#### lastIndexOf18+

lastIndexOf(searchElement: number, fromIndex?: number): number

返回ArkTS Uint32Array实例中最后一次出现searchElement的索引，如果对象不包含，则为-1。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明searchElementnumber是待索引的值。fromIndexnumber否搜索的起始下标。默认值为0。如果下标大于等于ArkTS Uint32Array的长度，则返回-1。如果提供的下标值是负数，则被当做距离数组尾部的偏移，从后到前搜索。

**返回值：**

类型说明number数组中给定元素的最后一个索引；没有找到，则返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The lastIndexOf method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([3, 5, 9]);
console.info(array.lastIndexOf(3) + ''); // 预期输出：0
console.info(array.lastIndexOf(7) + ''); // 预期输出：-1
console.info(array.lastIndexOf(9, 2) + ''); // 预期输出：2
console.info(array.lastIndexOf(9, -2) + ''); // 预期输出：-1
```

#### join

join(separator?: string): string

将ArkTS Uint32Array的所有元素拼接成一个字符串，元素之间使用指定的分隔符分隔。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明separatorstring否分隔字符串。如果省略，则使用逗号分隔。

**返回值：**

类型说明string包含所有元素拼接成的字符串。如果ArkTS Uint32Array为空，则返回空字符串。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The join method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let joined: string = array.join('-'); // "1-2-3-4-5"
```

#### map

map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array

对ArkTS Uint32Array中的每个元素应用指定的回调函数，并使用结果创建一个新的ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn[TypedArrayMapCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarraymapcallback)<number, Uint32Array>是回调函数。

**返回值：**

类型说明Uint32Array新ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The map method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([25, 36, 49]);
const mapped: collections.Uint32Array = array.map(Math.sqrt); // Uint32Array [5, 6 ,7]
```

#### reduce

reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number

对ArkTS Uint32Array中的每个元素执行归约函数，并返回最终的归约结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn[TypedArrayReduceCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayreducecallback)<number, number, Uint32Array>是归约函数。

**返回值：**

类型说明number由归约函数返回的结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The reduce method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let reducedValue: number = array.reduce((accumulator: number, value: number) => accumulator + value);
// reducedValue == 15
```

#### reduceRight18+

reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number

反向遍历ArkTS Uint32Array，对ArkTS Uint32Array中的每个元素执行归约函数，并返回最终的归约结果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn[TypedArrayReduceCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayreducecallback)<number, number, Uint32Array>是归约函数。

**返回值：**

类型说明number由归约函数返回的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.10200011The reduceRight method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let reducedValue: number = array.reduceRight((accumulator: number, value: number) => accumulator + value);
console.info(reducedValue + ''); // 预期输出： 15
```

#### reduce

reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>, initialValue: number): number

对ArkTS Uint32Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn[TypedArrayReduceCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayreducecallback)<number, number, Uint32Array>是归约函数。initialValuenumber是初始值。

**返回值：**

类型说明number由归约函数返回的结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The reduce method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let reducedValue: number = array.reduce((accumulator: number, value: number) => accumulator + value, 1);
// reducedValue == 16
```

#### reduceRight18+

reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U

反向遍历ArkTS Uint32Array，对ArkTS Uint32Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn[TypedArrayReduceCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayreducecallback)<U, number, Uint32Array>是归约函数。initialValueU是初始值。

**返回值：**

类型说明U由归约函数返回的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.10200011The reduceRight method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let reducedValue: number = array.reduceRight((accumulator: number, value: number) => accumulator + value, 1);
console.info(reducedValue + ''); // 预期输出： 16
```

#### reduce

reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U

对ArkTS Uint32Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn[TypedArrayReduceCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarrayreducecallback)<U, number, Uint32Array>是归约函数。initialValueU是初始值。

**返回值：**

类型说明U由归约函数返回的结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The reduce method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let reducedValue: string = array.reduce<string>((accumulator: string, value: number) => accumulator + value, "initialValue");
// reducedValue == initialValue12345
```

#### reverse

reverse(): Uint32Array

反转ArkTS Uint32Array。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明Uint32Array反转后的ArkTS Uint32Array对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The reverse method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let reversed: collections.Uint32Array = array.reverse(); // Uint32Array [5, 4, 3, 2, 1]
```

#### set

set(array: ArrayLike<number>, offset?: number): void

将传入的ArrayLike元素依次写入到指定的起始位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明arrayArrayLike<number>是用于设置的ArrayLike对象。offsetnumber否写入的起始位置。默认为0。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The set method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let buffer: collections.ArrayBuffer = new collections.ArrayBuffer(32);
let array: collections.Uint32Array = new collections.Uint32Array(buffer);
array.set([1, 2, 3], 3); // Uint32Array [0, 0, 0, 1, 2, 3, 0, 0]
```

#### slice

slice(start?: number, end?: number): Uint32Array

返回一个新的ArkTS Uint32Array对象，其包含原ArkTS Uint32Array指定范围的内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明startnumber否开始索引，如果start < 0，则会从start + Uint32Array.length位置开始。默认为0。endnumber否结束索引（不包括该元素），如果end < 0，则会到end + Uint32Array.length位置结束。默认为ArkTS Uint32Array的长度。

**返回值：**

类型说明Uint32Array新的ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The slice method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
array.slice(); // Uint32Array [1, 2, 3, 4, 5]
array.slice(1, 3); // Uint32Array [2, 3]
array.slice(-2); // Uint32Array [4, 5]
```

#### sort

sort(compareFn?: TypedArrayCompareFn<number>): Uint32Array

对ArkTS Uint32Array进行排序，并返回排序后的ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明compareFn[TypedArrayCompareFn](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497604746__typedarraycomparefn)<number>否用于确定元素顺序的函数。默认使用升序排序。

**返回值：**

类型说明Uint32Array排序后的ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The sort method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 3, 5, 4, 2]);
array.sort(); // Uint32Array [1, 2, 3, 4, 5]
array.sort((a: number, b: number) => a - b); // Uint32Array [1, 2, 3, 4, 5]
array.sort((a: number, b: number) => b - a); // Uint32Array [5, 4, 3, 2, 1]
```

#### subarray

subarray(begin?: number, end?: number): Uint32Array

从指定的位置截取数组，返回一个新的、基于相同ArkTS ArrayBuffer的ArkTS Uint32Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明beginnumber否开始索引，如果begin < 0，则会从begin + Uint32Array.length位置开始。默认值为0。endnumber否结束索引（不包括该元素），如果end < 0，则会到end + Uint32Array.length位置结束。默认为ArkTS Uint32Array的长度。

**返回值：**

类型说明Uint32Array新的ArkTS Uint32Array对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The subarray method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let subArray: collections.Uint32Array = array.subarray(); // Uint32Array [1, 2, 3, 4, 5]
subArray.set([10, 20, 30]); // Uint32Array [10, 20, 30, 4, 5]
```

#### at

at(index: number): number | undefined

返回指定下标的元素，如果不存在，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是要返回的Array元素的索引（从零开始），取值为整数。如果index < 0，则会访问index + Uint32Array.length位置的元素。

**返回值：**

类型说明number | undefined指定下标的元素；如果不存在，则返回undefined。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The at method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
console.info("element: " + array.at(2));  // element: 3
console.info("element: " + array.at(-1)); // element: 5
console.info("element: " + array.at(6));  // element: undefined
```

#### includes

includes(searchElement: number, fromIndex?: number): boolean

判断ArkTS Uint32Array是否包含特定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明searchElementnumber是待搜索的元素。fromIndexnumber否开始搜索的索引，如果fromIndex < 0，则会从fromIndex + Uint32Array.length位置开始。默认值为0。

**返回值：**

类型说明boolean如果ArkTS Uint32Array包含指定的元素，则返回true；否则返回false。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The includes method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3]);
console.info("includes: " + array.includes(2));    // includes: true
console.info("includes: " + array.includes(4));    // includes: false
console.info("includes: " + array.includes(3, 3)); // includes: false
```

#### entries

entries(): IterableIterator<[number, number]>

返回一个新的迭代器对象，该对象包含ArkTS Uint32Array中每个元素的键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[number, number]>新的迭代器对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The entries method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([11, 22, 33]);
let iterator: IterableIterator<[number, number]> = array.entries();
console.info("value: " + iterator.next().value); // value: 0,11
console.info("value: " + iterator.next().value); // value: 1,22
console.info("value: " + iterator.next().value); // value: 2,33
```

#### keys

keys(): IterableIterator<number>

返回一个新的迭代器对象，该对象包含ArkTS Uint32Array中每个元素的键（下标）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<number>新的迭代器对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The keys method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let iterator: IterableIterator<number> = array.keys();
for (const key of iterator) {
  console.info("" + key); // 依次输出 0,1,2,3,4
}
```

#### values

values(): IterableIterator<number>

返回一个新的迭代器对象，该对象包含ArkTS Uint32Array中每个元素的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<number>新的迭代器对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The values method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5]);
let iterator: IterableIterator<number> = array.values();
for (const value of iterator) {
  console.info("" + value); // 依次输出 1,2,3,4,5
}
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<number>

返回一个迭代器，迭代器的每一项都是一个 JavaScript 对象，并返回该对象。

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<number>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let uint32Array: collections.Uint32Array = collections.Uint32Array.from([1, 2, 3, 4, 5, 6]);

for (let item of uint32Array) {
  console.info(`value : ${item}`);
}
```

#### [index: number]

[index: number]: number

返回Uint32Array指定索引位置的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是所需代码单元的从零开始的索引。

**返回值：**

类型说明number返回number数据类型。

**示例：**

```ets
let uint32Array = collections.Uint32Array.from([1, 2, 4]);
console.info("Element at index 1: ", uint32Array[1]);
```