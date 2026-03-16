# Class (Set)

一种非线性数据结构。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

文档中存在泛型的使用，涉及以下泛型标记符：

- T：Type，支持[Sendable支持的数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable支持的数据类型)。

**装饰器类型：**@Sendable

#### 导入模块

```ets
import { collections } from '@kit.ArkTS';
```

#### 属性

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明sizenumber是否Set的元素个数。

#### constructor

constructor(values?: readonly T[] | null)

构造函数，用于创建ArkTS Set对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuesreadonly T[] | null否数组或其它可迭代对象。默认值为null，创建一个空Set对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The ArkTS Set's constructor cannot be directly invoked.

**示例：**

```ets
// 正例1：
const mySet = new collections.Set<number>();
```

```ets
// 正例2：
const mySet = new collections.Set<number>([1, 2, 3, 4, 5]);
```

```ets
// 反例：
@Sendable
class SharedClass {
  constructor() {
  }
}

let sObj = new SharedClass();
const mySet1: collections.Set<number|SharedClass> = new collections.Set<number|SharedClass>([1, sObj]);
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
let obj = new Object();
const mySet2: collections.Set<number|SharedClass> = new collections.Set<number|Object>([1, obj]);
```

#### constructor

constructor(iterable: Iterable<T>)

创建ArkTS Set对象的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明iterableIterable<T>是用于构造ArkTS Set的对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200012The ArkTS Set's constructor cannot be directly invoked.

**示例：**

```ets
const mapper = new Map([
  ['1', 'a'],
  ['2', 'b'],
]);
let newSet = new collections.Set<string>(mapper.values());
console.info(newSet.has('a').toString()); // 预期输出： true
console.info(newSet.has('b').toString()); // 预期输出： true
```

#### entries

entries(): IterableIterator<[T, T]>

返回一个Set迭代器对象，该对象包含了此Set中每个元素的键值对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[T, T]>返回一个Set迭代器对象，该对象包含了此Set中每个元素的键值对。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The entries method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const mySet = new collections.Set<number>([0, 1, 2, 3]);

const iterator = mySet.entries();
// Expected output: [0, 0]
console.info(iterator.next().value);
// Expected output: [1, 1]
console.info(iterator.next().value);
```

#### keys

keys(): IterableIterator<T>

返回一个Set迭代器对象，该对象包含了此Set中每个元素的键。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<T>返回一个Set迭代器对象，该对象包含了此Set中每个元素的键。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The keys method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const mySet = new collections.Set<number>([0, 1, 2, 3]);

const iterator = mySet.keys();
// Expected output: 0
console.info(iterator.next().value);
// Expected output: 1
console.info(iterator.next().value);
```

#### values

values(): IterableIterator<T>

返回一个Set迭代器对象，该对象包含了此Set中每个元素的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<T>返回一个Set迭代器对象，该对象包含了此Set中每个元素的值。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The values method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
// 例1：
const mySet = new collections.Set<number>([0, 1, 2, 3]);

const iterator = mySet.values();
// Expected output: 0
console.info(iterator.next().value);
// Expected output: 1
console.info(iterator.next().value);
```

```ets
// 例2：
const mySet = new collections.Set<number>([0, 1, 2, 3]);

const valueIter = mySet.values();
for (let value of valueIter) {
    if (value % 2 == 0) {
        mySet.delete(value);
    }
}

// Expected output: 2
console.info("size:" + mySet.size);
```

#### clear

clear(): void

删除该Set中的所有元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The clear method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const mySet = new collections.Set<number>([0, 1]);
// Expected output: 2
console.info("size:" + mySet.size);
mySet.clear();
// Expected output: 0
console.info("size:" + mySet.size);
```

#### delete

delete(value: T): boolean

删除该Set中指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueT是待删除元素的值。

**返回值：**

类型说明boolean成功删除返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The delete method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const mySet = new collections.Set<string>(["hello", "world"]);
// Expected result: true
console.info("result:" + mySet.delete("hello"));
// Expected result: false
console.info("result:" + mySet.has("hello"));
// Expected result: false
console.info("result:" + mySet.delete("hello"));
```

#### forEach

forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void

按插入顺序对该Set中的每个键/值对执行一次回调函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFn(value: T, value2: T, set: Set<T>) => void是回调函数。

callbackFn的参数说明：

参数名类型必填说明valueT否当前遍历到的元素键值对的值。value2T否当前遍历到的元素键值对的键。setSet<T>否当前set实例对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The forEach method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
// 正例：
new collections.Set<string>(['foo', 'bar', 'baz']).forEach((value1, value2, set) => {
  console.info(`s[${value1}] = ${value2}`);
});
```

```ets
// 反例：
new collections.Set<string>(['foo', 'bar', 'baz']).forEach((value1, value2, set) => {
  // Throw exception `Concurrent modification error.`
  set.delete(value1);
});
```

#### has

has(value: T): boolean

判断该Set中是否存在指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueT是待查找元素的值。

**返回值：**

类型说明boolean如果存在指定元素，则返回true；否则返回false。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200011The has method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
const mySet = new collections.Set<string>(["hello", "world"]);
// Expected output: true
console.info("result:" + mySet.has("hello"));
// Expected output: true
console.info("result:" + mySet.has("world"));
```

#### add

add(value: T): Set<T>

如果没有相同元素，则在该Set中插入一个新元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueT是待插入元素的值。

**返回值：**

类型说明Set<T>Set对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The add method cannot be bound with non-sendable.10200201Concurrent modification error.

**示例：**

```ets
// 正例：
const mySet: collections.Set<string> = new collections.Set<string>();
mySet.add("foo");
```

```ets
// 反例：
let obj = new Object();
const mySet: collections.Set<Object> = new collections.Set<Object>();
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
mySet.add(obj);
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象，并返回该对象。

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<T>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let set = new collections.Set<number>([1, 2, 3, 4, 5]);

let val: Array<number> = Array.from(set.values());
for (let item of val) {
  console.info("value: " + item);
}
```