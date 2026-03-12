# @ohos.util.LightWeightMap (非线性容器LightWeightMap)

LightWeightMap可用于存储具有关联关系的key-value键值对集合，存储元素中key值唯一，每个key对应一个value。

LightWeightMap依据泛型定义，采用轻量级结构，初始默认容量大小为8，每次扩容大小为原始容量的两倍。

集合中key值的查找依赖于hash算法，通过一个数组存储hash值，然后映射到其他数组中的key值及value值。

LightWeightMap和[HashMap](@ohos.util.HashMap (非线性容器HashMap).md)都是用来存储键值对的集合，但LightWeightMap占用内存更小。

**推荐使用场景：** 当需要存取key-value键值对时，推荐使用占用内存更小的LightWeightMap。

文档中使用了泛型，涉及以下泛型标记符：

-

K：Key，键

- V：Value，值

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

#### 规格限制

当LightWeightMap存入的key为number类型且值大于INT32_MAX或小于INT32_MIN时，针对LightWeightMap的操作，其结果可能与预期不一致。

这是因为，当key为number类型且值大于INT32_MAX或小于INT32_MIN时，存储结构会发生改变。

例如在以下示例针对key的计算中，1758783600000大于INT32_MAX，此时会通过TaggedDouble存储；1758783600小于INT32_MIN，此时会通过TaggedInt存储。由于以上存储方式的差异，当对其进行hash算法即会计算出不同的hash值，从而导致映射结果不同，产生与预期不一致的现象。

```ets
let mp = new LightWeightMap<number, number>();
let key = 1758783600000 / 1000;  // 1758783600000 > INT32_MAX
mp.set(key, 1001);
console.info("result:", mp.hasKey(1758783600));  // result: false
console.info("result:", mp.hasKey(key));  // result: true
```

#### 导入模块

```ets
import { LightWeightMap } from '@kit.ArkTS';
```

#### LightWeightMap

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否LightWeightMap的元素个数。

#### constructor

constructor()

LightWeightMap的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200012The LightWeightMap's constructor cannot be directly invoked.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
```

#### isEmpty

isEmpty(): boolean

判断LightWeightMap是否为空。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean为空返回true，不为空返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The isEmpty method cannot be bound.

**示例：**

```ets
const lightWeightMap = new LightWeightMap<string, number>();
let result = lightWeightMap.isEmpty();
console.info("result:", result);  // result: true
```

#### hasAll

hasAll(map: LightWeightMap<K, V>): boolean

判断LightWeightMap中是否包含指定map中的所有元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明mapLightWeightMap<K, V>是比较对象。

**返回值：**

类型说明boolean包含所有元素返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The hasAll method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let map = new LightWeightMap<string, number>();
map.set("sparrow", 356);
let result = lightWeightMap.hasAll(map);
console.info("result = ", result); // result = true
```

#### hasKey

hasKey(key: K): boolean

判断LightWeightMap中是否包含指定key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是指定key。

**返回值：**

类型说明boolean包含指定key返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The hasKey method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
let result = lightWeightMap.hasKey("squirrel");
console.info("result:", result);  // result: true
```

#### hasValue

hasValue(value: V): boolean

判断LightWeightMap中是否包含指定value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueV是指定元素。

**返回值：**

类型说明boolean包含指定元素返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The hasValue method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
let result = lightWeightMap.hasValue(123);
console.info("result:", result);  // result: true
```

#### increaseCapacityTo

increaseCapacityTo(minimumCapacity: number): void

将当前LightWeightMap扩容至指定容量。如果传入的容量值大于或等于当前LightWeightMap中的元素个数，将容量变更为新容量，小于则不会变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明minimumCapacitynumber是需要容纳的元素数量。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The increaseCapacityTo method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.increaseCapacityTo(10);
```

#### get

get(key: K): V

获取指定key所对应的value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是指定key。

**返回值：**

类型说明V返回key映射的value值。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The get method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.get("sparrow");
console.info("result:", result);  // result: 356
```

#### getIndexOfKey

getIndexOfKey(key: K): number

查找key元素首次出现的下标值，如果未找到返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是被查找的元素。

**返回值：**

类型说明number返回key元素首次出现的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The getIndexOfKey method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getIndexOfKey("sparrow");
console.info("result:", result);  // result: 0
```

#### getIndexOfValue

getIndexOfValue(value: V): number

查找value元素首次出现的下标值，如果未找到则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueV是被查找的元素。

**返回值：**

类型说明number返回value元素首次出现的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The getIndexOfValue method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getIndexOfValue(123);
console.info("result:", result);  // result: 1
```

#### getKeyAt

getKeyAt(index: number): K

查找指定下标的元素键值对中key值，如果未找到则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是所查找的下标。需要小于等于int32_max即2147483647。

**返回值：**

类型说明K返回该下标对应的元素键值对中key值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of index is out of range.10200011The getKeyAt method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getKeyAt(1);
console.info("result:", result);  // result: squirrel
```

#### setAll

setAll(map: LightWeightMap<K, V>): void

将一个LightWeightMap中的所有元素组添加到另一个LightWeightMap中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明mapLightWeightMap<K, V>是提供添加元素的LightWeightMap。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The setAll method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let map = new LightWeightMap<string, number>();
map.setAll(lightWeightMap);   // 将lightWeightMap中所有的元素添加到map中
let result = map.get("sparrow");
console.info("result:", result);  // result: 356
```

#### set

set(key: K, value: V): Object

向LightWeightMap中添加或更新一组数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是添加或更新成员数据的键名。valueV是添加或更新成员数据的值。

**返回值：**

类型说明Object返回添加或更新数据后的LightWeightMap。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The set method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
let result = lightWeightMap.set("squirrel", 123);
console.info("result:", result);  // result: squirrel:123
```

#### remove

remove(key: K): V

删除指定key映射的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明keyK是指定key。

**返回值：**

类型说明V返回删除元素的值。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The remove method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.remove("sparrow");
console.info("result:", result);  // result: 356
```

#### removeAt

removeAt(index: number): boolean

删除指定下标对应的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定下标。需要小于等于int32_max即2147483647。

**返回值：**

类型说明boolean成功删除元素返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The removeAt method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.removeAt(1);
console.info("result:", result);  // result: true
```

#### setValueAt

setValueAt(index: number, newValue: V): boolean

替换指定下标对应键值对中的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定下标。需要小于等于int32_max即2147483647。newValueV是替换键值对中的值。

**返回值：**

类型说明boolean成功替换返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of index is out of range.10200011The setValueAt method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
lightWeightMap.setValueAt(1, 3546);
console.info("result:", lightWeightMap.get("squirrel"));  // result: 3546
```

#### getValueAt

getValueAt(index: number): V

获取指定下标对应键值对中的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定下标。需要小于等于int32_max即2147483647。

**返回值：**

类型说明V返回指定下标对应键值对中的值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of index is out of range.10200011The getValueAt method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getValueAt(1);
console.info("result:", result);  // result: 123
```

#### clear

clear(): void

清除LightWeightMap中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The clear method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
lightWeightMap.clear();
let result = lightWeightMap.isEmpty();
console.info("result:", result);  // result: true
```

#### keys

keys(): IterableIterator<K>

返回包含此映射中所有的键的新迭代器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<K>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The keys method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let keys = lightWeightMap.keys();
for (let key of keys) {
  console.info("key:", key);
}
// key: sparrow
// key: squirrel
```

#### values

values(): IterableIterator<V>

返回包含此映射中所有键值的新迭代器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<V>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The values method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let values = lightWeightMap.values();
for (let value of values) {
  console.info("value:", value);
}
// value: 356
// value: 123
```

#### forEach

forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object): void

通过回调函数来遍历实例对象上的元素及其下标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackFn被调用时用作this值，默认值为当前实例对象。

callbackFn的参数说明：

参数名类型必填说明valueV否当前遍历到的元素键值对的值，默认值为首个键值对的值。keyK否当前遍历到的元素键值对的键，默认值为首个键值对的键。mapLightWeightMap<K, V>否当前调用forEach方法的实例对象，默认值为当前实例对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The forEach method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("sparrow", 123);
lightWeightMap.set("gull", 357);
lightWeightMap.forEach((value: number, key: string) => {
  console.info("value:" + value, "key:" + key);
});
// value:123 key:sparrow
// value:357 key:gull
```

```ets
// 不建议在forEach中使用set、setValueAt、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let lightWeightMap = new LightWeightMap<string, number>();
for(let i = 0; i < 10; i++) {
  lightWeightMap.set("sparrow" + i, 123);
}
for(let i = 0; i < 10; i++) {
  lightWeightMap.remove("sparrow" + i);
}
```

#### entries

entries(): IterableIterator<[K, V]>

返回包含此映射中所有键值对的新迭代器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The entries method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let iter = lightWeightMap.entries();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:" + temp.value[0]);
  console.info("value:" + temp.value[1]);
  temp = iter.next();
}
```

```ets
// 不建议在entries中使用set、setValueAt、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let lightWeightMap = new LightWeightMap<string, number>();
for(let i = 0; i < 10; i++) {
  lightWeightMap.set("sparrow" + i, 123);
}
for(let i = 0; i < 10; i++) {
  lightWeightMap.remove("sparrow" + i);
}
```

#### toString

toString(): String

将此映射中包含的键值对拼接成字符串并返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明String返回一个字符串。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The toString method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.toString();
console.info("result:", result);  // result: sparrow:356,squirrel:123
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[K, V]>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);

// 使用方法一：
for (let item of lightWeightMap) {
  console.info("key:", item[0]);
  console.info("value:", item[1]);
}
// key: sparrow
// value: 356
// key: squirrel
// value: 123

// 使用方法二：
let iter = lightWeightMap[Symbol.iterator]();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:", temp.value[0]);
  console.info("value:", temp.value[1]);
  temp = iter.next();
}
// key: sparrow
// value: 356
// key: squirrel
// value: 123
```

```ets
// 不建议在Symbol.iterator中使用set、setValueAt、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let lightWeightMap = new LightWeightMap<string, number>();
for(let i = 0; i < 10; i++) {
  lightWeightMap.set("sparrow" + i, 123);
}
for(let i = 0; i < 10; i++) {
  lightWeightMap.remove("sparrow" + i);
}
```