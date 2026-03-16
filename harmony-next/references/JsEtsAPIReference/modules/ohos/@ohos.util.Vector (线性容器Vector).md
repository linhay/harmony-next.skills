# @ohos.util.Vector (线性容器Vector)

Vector是一种线性数据结构，底层基于数组实现。当Vector的内存用尽时，会自动分配更大的连续内存区，将原先的元素复制到新的内存区，并释放旧的内存区。使用Vector能够高效快速地访问元素。

Vector和[ArrayList](@ohos.util.ArrayList (线性容器ArrayList).md)相似，都是基于数组实现，但Vector提供了更多操作数组的接口。它们都可以动态调整容量，但Vector每次扩容增加1倍，ArrayList只扩容0.5倍。

**推荐使用场景：** 当数据量大时，一般使用Vector来存取数据。

文档中存在泛型的使用，涉及以下泛型标记符：

- T：Type，类

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

API version 9开始，该接口不再维护，推荐使用接口['@ohos.util.ArrayList'](@ohos.util.ArrayList (线性容器ArrayList).md)。

#### 导入模块

```ets
import { Vector } from '@kit.ArkTS';
```

#### Vector

#### 属性

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否Vector的元素个数。

#### constructor

constructor()

Vector的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let vector : Vector<string | number | Array<number>> = new Vector();
```

#### add

add(element: T): boolean

在Vector中尾部插入元素。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是添加进去的元素。

**返回值：**

类型说明boolean插入成功返回true，失败返回false。

**示例：**

```ets
class C1 {
  name: string = ""
  age: string = ""
}
let vector : Vector<string | number | C1 | Array<number>> = new Vector();
let result = vector.add("a");
let result1 = vector.add(1);
let b = [1, 2, 3];
let result2 = vector.add(b);
let c: C1 = {name : "Jack", age : "13"};
let result3 = vector.add(c);
```

#### insert

insert(element: T, index: number): void

在长度范围内任意插入指定元素，并将其后续元素向右移动。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是被插入的元素。indexnumber是被插入的位置索引。

**示例：**

```ets
let vector : Vector<string | number | Object | Array<number>> = new Vector();
vector.insert("A", 0);
vector.insert(0, 1);
vector.insert(true, 2);
```

#### has

has(element: T): boolean

判断此Vector中是否含有该指定元素。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定的元素。

**返回值：**

类型说明boolean是否包含指定元素，true表示包含该元素，false表示不包含。

**示例：**

```ets
let vector : Vector<string> = new Vector();
let result = vector.has("squirrel");
vector.add("squirrel");
let result1 = vector.has("squirrel");
```

#### getIndexOf

getIndexOf(element: T): number

返回指定元素第一次出现时的下标值，查找失败返回-1。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定的元素。

**返回值：**

类型说明number返回指定元素第一次出现时的下标值，查找失败返回-1。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(2);
vector.add(1);
vector.add(2);
vector.add(4);
let result = vector.getIndexOf(2);
```

#### getLastIndexOf

getLastIndexOf(element: T): number

返回指定元素最后一次出现时的下标值，查找失败返回-1。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明number返回指定元素最后一次出现时的下标值，查找失败返回-1。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(2);
vector.add(1);
vector.add(2);
vector.add(4);
let result = vector.getLastIndexOf(2);
```

#### removeByIndex

removeByIndex(index: number): T

根据元素的下标值查找元素，返回元素后将其删除，并将其后续元素向左移动。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定元素的下标值。

**返回值：**

类型说明T返回被删除的元素。数组为空时返回undefined，下标越界时抛出异常。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(2);
vector.add(4);
let result = vector.removeByIndex(2);
```

#### remove

remove(element: T): boolean

删除查找到的第一个指定的元素。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明boolean删除成功返回true，否则返回false。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.remove(2);
```

#### removeByRange

removeByRange(fromIndex: number, toIndex: number): void

从一段范围内删除元素，包括起始值但不包括终止值。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明fromIndexnumber是起始下标。toIndexnumber是终止下标。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.removeByRange(2,4);
```

#### replaceAllElements

replaceAllElements(callbackFn: (value: T, index?: number, vector?: Vector<T>) => T,

thisArg?: Object): void

用户操作Vector中的元素，用操作后的元素替换原元素并返回操作后的元素。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackfn被调用时用作this值，默认值为当前实例对象。

callbackfn的参数说明：

参数名类型必填说明valueT是当前遍历到的元素。indexnumber否当前遍历到的下标值，默认值为0。vectorVector<T>否当前调用replaceAllElements方法的实例对象，默认值为当前实例对象。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.replaceAllElements((value : number) : number => {
  // 用户操作逻辑根据实际场景进行添加。
  return value;
});
```

#### forEach

forEach(callbackFn: (value: T, index?: number, vector?: Vector<T>) => void,

thisArg?: Object): void

通过回调函数来遍历Vector实例对象上的元素以及元素对应的下标。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackfn被调用时用作this值，默认值为当前实例对象。

callbackfn的参数说明：

参数名类型必填说明valueT是当前遍历到的元素。indexnumber否当前遍历到的下标值，默认值为0。vectorVector<T>否当前调用forEach方法的实例对象，默认值为当前实例对象。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.forEach((value : number, index ?: number) : void => {
  console.info("value:" + value, "index:" + index);
});
```

#### sort

sort(comparator?: (firstValue: T, secondValue: T) => number): void

对Vector中的元素进行一个排序操作。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明comparatorfunction否回调函数，默认值为当前实例对象。

comparator的参数说明：

参数名类型必填说明firstValueT是前一项元素。secondValueT是后一项元素。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.sort((a: number, b: number) => a - b);
vector.sort((a: number, b: number) => b - a);
vector.sort();
```

#### subVector

subVector(fromIndex: number, toIndex: number): Vector<T>

根据下标截取Vector中的一段元素，并返回这一段vector实例，包括起始值但不包括终止值。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明fromIndexnumber是起始下标。toIndexnumber是终止下标。

**返回值：**

类型说明Vector<T>返回Vector对象实例。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.add(6);
vector.add(8);
let result = vector.subVector(0,4);
let result1 = vector.subVector(2,4);
```

#### clear

clear(): void

清除Vector中的所有元素，并把length置为0。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.clear();
```

#### clone

clone(): Vector<T>

克隆一个与Vector相同的实例，并返回克隆后的实例。修改克隆后的实例并不会影响原实例。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明Vector<T>返回Vector对象实例。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.clone();
```

#### getCapacity

getCapacity(): number

获取当前实例的容量大小。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回Vector的容量大小。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.getCapacity();
```

#### convertToArray

convertToArray(): Array<T>

把当前Vector实例转换成数组，并返回转换后的数组。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明Array<T>返回数组类型。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.convertToArray();
```

#### isEmpty

isEmpty(): boolean

判断该Vector是否为空。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean为空返回true，否则返回false。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.isEmpty();
```

#### increaseCapacityTo

increaseCapacityTo(newCapacity: number): void

如果传入的新容量大于或等于Vector中的元素个数，将容量变更为新容量。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明newCapacitynumber是新容量。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.increaseCapacityTo(2);
vector.increaseCapacityTo(12);
```

#### trimToCurrentLength

trimToCurrentLength(): void

把容量限制为当前的length大小。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.trimToCurrentLength();
```

#### toString

toString(): string

用","将Vector实例中的元素按顺序拼接成字符串。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明string返回对应的字符串。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.toString();
```

#### copyToArray

copyToArray(array: Array<T>): void

将Vector实例中的元素按照下标复制到指定数组。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明arrayArray<T>是指定数组。

#### getFirstElement

getFirstElement(): T

获取实例中的第一个元素。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回第一个元素。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.getFirstElement();
```

#### getLastElement

getLastElement(): T

获取Vector实例中的最后一个元素。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回最后一个元素。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.getLastElement();
```

#### getLastIndexFrom

getLastIndexFrom(element: T, index: number): number

从指定索引向后搜索，返回该元素的下标索引。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是要查找的元素。indexnumber是从指定索引开始搜索。

**返回值：**

类型说明number返回该元素的下标，如果查找失败，则返回-1。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.getLastIndexFrom(4,3);
```

#### getIndexFrom

getIndexFrom(element: T, index: number): number

从指定索引向前搜索，返回该元素的下标索引。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是要查找的元素。indexnumber是从指定索引开始搜索。

**返回值：**

类型说明number返回该元素的下标，如果查找失败，则返回 -1。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.getIndexFrom(4, 3);
```

#### setLength

setLength(newSize: number): void

设置Vector实例的元素个数。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明newSizenumber是设置的新长度。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
vector.setLength(8);
vector.setLength(2);
```

#### get

get(index: number): T

根据下标值获取Vector实例中的元素。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是查找的下标值。

**返回值：**

类型说明T返回获取到的元素。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
let result = vector.get(2);
```

#### set

set(index: number, element: T): T

将此Vector中指定位置的元素替换为指定元素。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是查找的下标值。elementT是用来替换的元素。

**返回值：**

类型说明T返回替换后的元素。

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，迭代器的每一项都是一个 JavaScript 对象，并返回该对象。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<T>返回一个迭代器。

**示例：**

```ets
let vector : Vector<number> = new Vector();
vector.add(2);
vector.add(4);
vector.add(5);
vector.add(4);
// 使用方法一：
let nums: Array<number> =  vector.convertToArray()
for (let item of nums) {
  console.info("value:" + item);
}

// 使用方法二：
let iter = vector[Symbol.iterator]();
let temp: IteratorResult<number> = iter.next().value;
while(temp != undefined) {
  console.info("value:" + temp);
  temp = iter.next().value;
}
```