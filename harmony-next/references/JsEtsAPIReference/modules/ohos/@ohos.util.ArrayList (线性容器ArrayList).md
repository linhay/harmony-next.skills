# @ohos.util.ArrayList (线性容器ArrayList)

ArrayList是一种线性数据结构，底层基于数组实现。ArrayList会根据实际需要动态调整容量，每次扩容增加50%。

ArrayList和[LinkedList](@ohos.util.LinkedList (线性容器LinkedList).md)相比，ArrayList的随机访问效率更高。但由于ArrayList的增删操作可能需要对数组内其他元素进行移动，LinkedList的增加和删除操作效率更高。

**推荐使用场景：** 当需要频繁读取集合中的元素时，推荐使用ArrayList。

文档中使用了泛型，涉及以下泛型标记符：

- T：Type，类

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

#### 导入模块

```ets
import { ArrayList } from '@kit.ArkTS';
```

#### ArrayList

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否ArrayList的元素个数。

#### constructor

constructor()

ArrayList的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200012The ArrayList's constructor cannot be directly invoked.

**示例：**

```ets
let arrayList = new ArrayList<string | number>();
```

#### add

add(element: T): boolean

在ArrayList尾部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是待插入的元素。

**返回值：**

类型说明boolean插入成功返回true，失败返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The add method cannot be bound.

**示例：**

```ets
class C1 {
  name: string = ""
  age: string = ""
}
let arrayList = new ArrayList<string | number | boolean | Array<number> | C1>();
arrayList.add("a");
arrayList.add(1);
let b = [1, 2, 3];
arrayList.add(b);
let c : C1 = {name: "Dylan", age: "13"}
let result1 = arrayList.add(c);
let result2 = arrayList.add(false);
console.info("result1:", result1);  // result1: true
console.info("result2:", result2);  // result2: true
console.info("length:", arrayList.length);  // length: 5
```

#### insert

insert(element: T, index: number): void

在长度范围内指定位置index插入元素element。如果index超出范围，则插入失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是被插入的元素。indexnumber是被插入的位置索引。需要小于等于int32_max即2147483647。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of index is out of range.10200011The insert method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number | string | boolean>();
arrayList.insert("A", 0);
arrayList.insert(0, 1);
arrayList.insert(true, 2);
console.info("length:", arrayList.length);  // length: 3
```

#### has

has(element: T): boolean

判断此ArrayList中是否包含该指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明boolean返回true表示包含指定元素，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The has method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<string>();
arrayList.add("squirrel");
let result: boolean = arrayList.has("squirrel");
console.info("result:", result);  // result: true
```

#### getIndexOf

getIndexOf(element: T): number

返回指定元素第一次出现的下标，查找失败返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明number返回指定元素第一次出现时的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The getIndexOf method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.getIndexOf(2);
console.info("result = ", result); // result = 0
```

#### getLastIndexOf

getLastIndexOf(element: T): number

返回指定元素最后一次出现的下标，查找失败返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明number返回指定元素最后一次出现时的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The getLastIndexOf method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.getLastIndexOf(2);
console.info("result = ", result); // result = 5
```

#### removeByIndex

removeByIndex(index: number): T

根据元素的下标值查找元素，返回元素后将其删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定元素的下标值。需要小于等于int32_max即2147483647。

**返回值：**

类型说明T返回删除的元素。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of "index" is out of range.10200011The removeByIndex method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.removeByIndex(2);
console.info("result = ", result); // result = 5
```

#### remove

remove(element: T): boolean

删除查找到的第一个指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明boolean删除成功返回true，失败返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The remove method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.remove(2);
console.info("result = ", result); // result =  true
```

#### removeByRange

removeByRange(fromIndex: number, toIndex: number): void

删除指定范围内的元素，区间包含fromIndex，但不包含toIndex，即左闭右开区间[fromIndex, toIndex)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明fromIndexnumber是起始下标。toIndexnumber是终止下标。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of fromIndex or toIndex is out of range.10200011The removeByRange method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.removeByRange(2, 4);
```

#### replaceAllElements

replaceAllElements(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => T,

thisArg?: Object): void

用户操作ArrayList中的元素，用操作后的元素替换原元素并返回操作后的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackFn被调用时用作this值，默认值为当前实例对象。

callbackFn的参数说明：

参数名类型必填说明valueT是当前遍历到的元素。indexnumber否当前遍历到的下标值，默认值为0。arrlistArrayList<T>否当前调用replaceAllElements方法的实例对象，默认值为当前实例对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The replaceAllElements method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.replaceAllElements((value: number): number => {
  // 用户操作逻辑根据实际场景进行添加。
  return value;
});
```

#### forEach

forEach(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => void,

thisArg?: Object): void

在遍历ArrayList实例对象的过程中，对每个元素执行回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackFn被调用时用作this值，默认值为当前实例对象。

callbackFn的参数说明：

参数名类型必填说明valueT是当前遍历到的元素。indexnumber否当前遍历到的下标值，默认值为0。arrlistArrayList<T>否当前调用forEach方法的实例对象，默认值为当前实例对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The forEach method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.forEach((value: number, index?: number) => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

#### sort

sort(comparator?: (firstValue: T, secondValue: T) => number): void

根据指定比较器所定义的顺序，对ArrayList中的元素进行排序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明comparatorfunction否回调函数，默认为升序排序的回调函数。

comparator的参数说明：

参数名类型必填说明firstValueT是前一项元素。secondValueT是后一项元素。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.10200011The sort method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.sort((a: number, b: number) => a - b);
arrayList.sort((a: number, b: number) => b - a);
arrayList.sort();
```

#### subArrayList

subArrayList(fromIndex: number, toIndex: number): ArrayList<T>

根据下标截取ArrayList中的一段元素，并返回这一段ArrayList实例，区间包含fromIndex，但不包含toIndex，即左闭右开区间[fromIndex, toIndex)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明fromIndexnumber是起始下标。toIndexnumber是终止下标。

**返回值：**

类型说明ArrayList<T>返回ArrayList对象实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of fromIndex or toIndex is out of range.10200011The subArrayList method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: ArrayList<number> = arrayList.subArrayList(2, 4);
console.info("result = ", result.length); // result = 2
```

#### clear

clear(): void

清除ArrayList中的所有元素，并把length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The clear method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.clear();
```

#### clone

clone(): ArrayList<T>

克隆一个与ArrayList相同的实例，并返回克隆后的实例。修改克隆后的实例并不会影响原实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明ArrayList<T>返回ArrayList对象实例。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The clone method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result:  ArrayList<number> = arrayList.clone();
console.info("result = ", result.length); // result = 4
```

#### getCapacity

getCapacity(): number

获取当前实例的容量大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number获取当前实例的容量大小。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The getCapacity method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: number = arrayList.getCapacity();
console.info("result = ", result); // result = 10
```

#### convertToArray

convertToArray(): Array<T>

把当前ArrayList实例转换成数组，并返回转换后的数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明Array<T>返回数组类型。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The convertToArray method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: Array<number> = arrayList.convertToArray();
console.info("result = ", result); // result =  2,4,5,4
```

#### isEmpty

isEmpty(): boolean

判断该ArrayList是否为空。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean为空返回true，不为空返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The isEmpty method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.isEmpty();
console.info("result = ", result); // result =  false
```

#### [index: number]12+

[index: number]: T

获取指定索引值对应位置的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是元素的位置索引。需要小于等于int32_max即2147483647。

**返回值：**

类型说明T容器中对应索引值为index的元素。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error.10200001The value of index is out of range.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: number = arrayList[2];
console.info("result = ", result); // result =  5
```

#### increaseCapacityTo

increaseCapacityTo(newCapacity: number): void

如果传入的新容量大于或等于ArrayList中的元素个数，将容量变更为新容量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明newCapacitynumber是新容量。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The increaseCapacityTo method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.increaseCapacityTo(2);
arrayList.increaseCapacityTo(8);
console.info("result = ", arrayList.length); // result = 4
```

#### trimToCurrentLength

trimToCurrentLength(): void

释放ArrayList中预留的空间，把容量调整为当前的元素个数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The trimToCurrentLength method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.trimToCurrentLength();
console.info("result = ", arrayList.length); // result = 4
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，每一项都是一个JavaScript对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<T>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);

// 使用方法一：
for (let value of arrayList) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
let iter = arrayList[Symbol.iterator]();
let temp: IteratorResult<number> = iter.next();
while(!temp.done) {
  console.info("value:", temp.value);
  temp = iter.next();
}
// value: 2
// value: 4
// value: 5
// value: 4
```