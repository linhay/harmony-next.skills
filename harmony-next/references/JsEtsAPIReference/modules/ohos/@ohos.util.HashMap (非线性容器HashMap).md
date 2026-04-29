# @ohos.util.HashMap (非线性容器HashMap)

HashMap底层采用数组、链表和红黑树实现，支持高效查询、插入和删除。HashMap存储内容基于key-value的键值对映射，不允许重复的key，且一个key只能对应一个value。

HashMap和[TreeMap](@ohos.util.TreeMap (非线性容器TreeMap).md)相比，HashMap依据键的hashCode存取数据，访问速度较快。而TreeMap是有序存取，效率较低。

[HashSet](@ohos.util.HashSet (非线性容器HashSet).md)基于HashMap实现。HashMap的输入参数由key、value两个值组成。在HashSet中，只对value对象进行处理。

**推荐使用场景：** 需要快速存取、删除以及插入键值对数据时，推荐使用HashMap。

文档中使用了泛型，包含以下泛型标记符：

-

K：Key，键

- V：Value，值

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

#### 导入模块

```ets
import { HashMap } from '@kit.ArkTS';
```

#### HashMap

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | HashMap的元素个数。 |

#### constructor

constructor()

HashMap的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码]([语言基础类库错误码](../../errors/语言基础类库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The HashMap's constructor cannot be directly invoked. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
```

#### isEmpty

isEmpty(): boolean

判断该HashMap是否为空。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 为空返回true，不为空返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The isEmpty method cannot be bound. |

**示例：**

```ets
const hashMap = new HashMap<string, number>();
let result = hashMap.isEmpty();
console.info("result = ", result) // result = true
```

#### hasKey

hasKey(key: K): boolean

判断此HashMap中是否包含指定key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定Key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定Key返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The hasKey method cannot be bound. |

**示例：**

```ets
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
let result = hashMap.hasKey("squirrel");
console.info("result:", result);  // result: true
```

#### hasValue

hasValue(value: V): boolean

判断此HashMap中是否包含指定value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 是 | 指定value。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定的value返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The hasValue method cannot be bound. |

**示例：**

```ets
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
let result = hashMap.hasValue(123);
console.info("result:", result);  // result: true
```

#### get

get(key: K): V

获取指定key对应的value，不存在返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 查找的指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回key映射的value值。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The get method cannot be bound. |

**示例：**

```ets
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let result = hashMap.get("sparrow");
console.info("result:", result);  // result: 356
```

#### setAll

setAll(map: HashMap<K, V>): void

将一个HashMap中的所有元素组添加到另一个hashMap中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | HashMap<K, V> | 是 | 被添加元素的hashMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The setAll method cannot be bound. |

**示例：**

```ets
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let newHashMap = new HashMap<string, number>();
newHashMap.set("newMap", 99);
hashMap.setAll(newHashMap);
let result = hashMap.hasKey("newMap");
console.info("result:", result);  // result: true
```

#### set

set(key: K, value: V): Object

向HashMap中添加或更新一组数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 添加或更新成员数据的键名。 |
| value | V | 是 | 添加或更新成员数据的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回添加或更新后的hashMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 10200011 | The set method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123)
console.info("result:", hashMap.get("squirrel"));  // result: 123
```

#### remove

remove(key: K): V

删除指定key所对应元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回删除元素的值。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let result = hashMap.remove("sparrow");
console.info("result:", result);  // result: 356
```

#### clear

clear(): void

清除HashMap中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
hashMap.clear();
let result = hashMap.isEmpty();
console.info("result:", result);  // result: true
```

#### keys

keys(): IterableIterator<K>

返回新迭代器对象，包含此映射中所有的键。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<K> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The keys method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let keys = hashMap.keys();
for (let key of keys) {
  console.info("key:" + key);
}
// key:squirrel
// key:sparrow
```

#### values

values(): IterableIterator<V>

返回新迭代器对象，包含此映射中所有键对应的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<V> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The values method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let values = hashMap.values();
for (let value of values) {
  console.info("value:", value)
}
// value: 123
// value: 356
```

#### replace

replace(key: K, newValue: V): boolean

用于替换指定键对应的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 依据key指定替换的元素。 |
| newValue | V | 是 | 替换成员数据的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功对已有数据进行替换，成功返回true，失败返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The replace method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("sparrow", 123);
let result = hashMap.replace("sparrow", 357);
console.info("result:", result);  // result: true
```

#### forEach

forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object): void

在遍历过程中对每个元素调用一次回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 回调函数。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值，默认值为当前实例对象。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 否 | 当前遍历到的元素键值对的值。 |
| key | K | 否 | 当前遍历到的元素键值对的键。 |
| map | HashMap<K, V> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("sparrow", 123);
hashMap.set("gull", 357);
hashMap.forEach((value: number, key: string) => {
  console.info("value: " + value, "key: " + key);
});
// value: 123 key: sparrow
// value: 357 key: gull
```

```ets
// 不建议在forEach中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}
```

#### entries

entries(): IterableIterator<[K, V]>

返回包含此映射中包含的键值对的新迭代器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The entries method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let iter = hashMap.entries();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:" + temp.value[0]);
  console.info("value:" + temp.value[1]);
  temp = iter.next();
}
```

```ets
// 不建议在entries中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个迭代器，迭代器的每一项都是一个 JavaScript 对象，并返回该对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```ets
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);

// 使用方法一：
for (let item of hashMap) {
  console.info("key:", item[0]);
  console.info("value:", item[1]);
}
// key: squirrel
// value: 123
// key: sparrow
// value: 356

// 使用方法二：
let iter = hashMap[Symbol.iterator]();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:", temp.value[0]);
  console.info("value:", temp.value[1]);
  temp = iter.next();
}
// key: squirrel
// value: 123
// key: sparrow
// value: 356
```

```ets
// 不建议在Symbol.iterator中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}
```