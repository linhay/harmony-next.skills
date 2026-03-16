# Class (Map)

一种非线性数据结构。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

文档中存在泛型的使用，涉及以下泛型标记符：

- K：Key，键
- V：Value，值

K和V类型都需为[Sendable支持的数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable支持的数据类型)。

**装饰器类型：**@Sendable

#### 导入模块

```ets
import { collections } from '@kit.ArkTS';
```

#### 属性

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明sizenumber是否Map的元素个数。

#### constructor

constructor(entries?: readonly (readonly [K, V])[] | null)

构造函数，用于创建ArkTS Map对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明entriesreadonly (readonly [K, V])[] | null否键值对数组或其它可迭代对象。默认值为null，创建一个空Map对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The ArkTS Map's constructor cannot be directly invoked.

**示例：**

```ets
// 正例1：
const myMap = new collections.Map<number, number>();
```

```ets
// 正例2：
const myMap = new collections.Map<number, string>([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);
```

```ets
// 反例：
@Sendable
class SharedClass {
  constructor() {
  }
}
let sObj = new SharedClass();
const myMap1: collections.Map<number, SharedClass> = new collections.Map<number, SharedClass>([[1, sObj]]);
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
let obj = new Object();
const myMap2: collections.Map<number, Object> = new collections.Map<number, Object>([[1, obj]]);
```

#### constructor

constructor(iterable: Iterable<readonly [K, V]>)

创建ArkTS Map对象的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明iterableIterable<readonly [K, V]>是用于构造ArkTS Map的对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The ArkTS Map's constructor cannot be directly invoked.

**示例：**

```ets
const mapper = new Map([
  ['1', 'a'],
  ['2', 'b'],
]);
let newMap = new collections.Map<string, string>(mapper.entries());
console.info(newMap.get('1')); // 预期输出： a
console.info(newMap.get('2')); // 预期输出： b
```

#### entries

entries(): IterableIterator<[K, V]>

返回一个Map迭代器对象，该对象包含了此Map中的每个元素的[key, value]对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个Map迭代器对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The entries method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
// 例1：
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);

const iterator = myMap.entries();
// Expected output: 0, foo
console.info(iterator.next().value);
// Expected output: 1, bar
console.info(iterator.next().value);
```

```ets
// 例2：
const myMap: collections.Map<number, string> = new collections.Map<number, string>([
  [0, "one"],
  [1, "two"],
  [2, "three"],
  [3, "four"]
]);
const entriesIter: IterableIterator<[number, string]> = myMap.entries();
for (const entry of entriesIter) {
  if (entry[1].startsWith('t')) {
    myMap.delete(entry[0]);
  }
}
// Expected output: 2
console.info("size:" + myMap.size);
```

#### keys

keys(): IterableIterator<K>

返回一个Map迭代器对象，该对象包含了此Map中每个元素的键。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<K>返回一个Map迭代器对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The keys method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);

const iterator = myMap.keys();
// Expected output: 0
console.info(iterator.next().value);
// Expected output: 1
console.info(iterator.next().value);
```

#### values

values(): IterableIterator<V>

返回一个Map迭代器对象，该对象包含此Map中每个元素的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<V>返回一个Map迭代器对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The values method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);

const iterator = myMap.values();
// Expected output: "foo"
console.info(iterator.next().value);
// Expected output: "bar"
console.info(iterator.next().value);
```

#### clear

clear(): void

删除该Map中的所有元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The clear method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);
// Expected output: 2
console.info("size:" + myMap.size);
myMap.clear();
// Expected output: 0
console.info("size:" + myMap.size);
```

#### delete

delete(key: K): boolean

删除该Map中指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是待删除元素的键。

**返回值：**

类型说明boolean如果元素存在并已被删除，则为true；否则该元素不存在，返回false。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The delete method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const myMap = new collections.Map<string, string>([
  ["hello", "world"],
]);
// Expected result: true
console.info("result:" + myMap.delete("hello"));
// Expected result: false
console.info("result:" + myMap.has("hello"));
// Expected result: false
console.info("result:" + myMap.delete("hello"));
```

#### forEach

forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void

按插入顺序对该Map中的每个键/值对执行一次回调函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn(value: V, key: K, map: Map<K, V>) => void是回调函数。

callbackFn的参数说明：

参数名类型必填说明valueV否当前遍历到的元素键值对的值。keyK否当前遍历到的元素键值对的键。mapMap<K, V>否当前map实例对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The forEach method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
// 正例：
new collections.Map<string, number>([
  ['foo', 0],
  ['bar', 1],
  ['baz', 2],
]).forEach((value, key, map) => {
  console.info(`m[${key}] = ${value}`);
});
```

```ets
// 反例：
new collections.Map<string, number>([
  ['foo', 0],
  ['bar', 1],
  ['baz', 2],
]).forEach((value, key, map) => {
  // Throw exception `Concurrent modification error.`
  map.delete(key);
});
```

#### get

get(key: K): V | undefined

返回该Map中的指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是指定key。

**返回值：**

类型说明V | undefined与指定键相关联的元素，如果键在Map对象中找不到，则返回undefined。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The get method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const myMap = new collections.Map<string, string>([
  ["hello", "world"],
]);
// Expected output: "world"
console.info(myMap.get("hello"));
// Expected output: undefined
console.info(myMap.get("hel"));
```

#### has

has(key: K): boolean

判断该Map中是否存在指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是待查找元素的值。

**返回值：**

类型说明boolean如果存在指定元素，则返回true，否则返回false。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The has method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const myMap = new collections.Map<string, string>([
  ["hello", "world"],
]);
// Expected output: true
console.info("result:" + myMap.has("hello"));
// Expected output: false
console.info("result:" + myMap.has("world"));
```

#### set

set(key: K, value: V): Map<K, V>

向该Map添加或更新一个指定的键值对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是添加或更新指定元素的键。valueV是添加或更新指定元素的值。

**返回值：**

类型说明Map<K, V>Map对象

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The set method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
// 正例：
const myMap = new collections.Map<string, string>();
myMap.set("foo", "bar");
```

```ets
// 反例：
let obj = new Object();
const myMap: collections.Map<string, Object> = new collections.Map<string, Object>();
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
myMap.set("foo", obj);
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象，并返回该对象。

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let map = new collections.Map<number, string>([
    [0, "one"],
    [1, "two"],
    [2, "three"],
    [3, "four"]
]);

let keys = Array.from(map.keys());
for (let key of keys) {
  console.info("key:" + key);
  console.info("value:" + map.get(key));
}
```