# @ohos.util.LinkedList (线性容器LinkedList)

LinkedList底层通过双向链表实现，每个节点都包含对前一个元素和后一个元素的引用。查询元素时，可以从头或从尾部遍历，插入和删除效率高，查询效率低。LinkedList允许元素为null。

LinkedList和[List](@ohos.util.List (线性容器List).md)相比，LinkedList是双向链表，可以快速地在头尾进行增删，而List是单向链表，无法双向操作。

LinkedList和[ArrayList](@ohos.util.ArrayList (线性容器ArrayList).md)相比，LinkedList插入数据效率高于ArrayList，而ArrayList查询效率高于LinkedList。

在LinkedList中使用[index]的方式获取元素可能导致未定义结果，推荐使用get()方法。

**推荐使用场景：** 当需要频繁的插入删除元素且需要使用双向链表时，推荐使用LinkedList。

文档中使用了泛型，涉及以下泛型标记符：

- T： Type，类

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

#### 导入模块

```ets
import { LinkedList } from '@kit.ArkTS';
```

#### LinkedList

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否LinkedList的元素个数。

#### constructor

constructor()

LinkedList的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200012The LinkedList's constructor cannot be directly invoked.

**示例：**

```ets
let linkedList = new LinkedList<string | number | boolean | object>();
```

#### add

add(element: T): boolean

在LinkedList尾部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是待插入的元素。

**返回值：**

类型说明boolean插入成功返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The add method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<string | number | boolean | object>();
let result = linkedList.add("a");
let result1 = linkedList.add(1);
let b = [1, 2, 3];
let result2 = linkedList.add(b);
class C {
  name: string = ''
  age: string = ''
}
let c: C = {name : "Dylan", age : "13"};
let result3 = linkedList.add(c);
let result4 = linkedList.add(false);
console.info("result = ", result4) // result =  true
```

#### addFirst

addFirst(element: T): void

在LinkedList头部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是待插入的元素。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The addFirst method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<string | number | boolean | object>();
linkedList.addFirst("a");
linkedList.addFirst(1);
let b = [1, 2, 3];
linkedList.addFirst(b);
class C {
  name: string = ''
  age: string = ''
}
let c: C = {name : "Dylan", age : "13"};
linkedList.addFirst(c);
linkedList.addFirst(false);
let result = linkedList.get(2);
console.info("result:", result);  // result: 1,2,3
```

#### insert

insert(index: number, element: T): void

在长度范围内任意位置插入指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是插入位置索引。需要小于等于int32_max即2147483647。elementT是插入元素。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of index is out of range.10200011The insert method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<string | number | boolean | object>();
linkedList.insert(0, "A");
linkedList.insert(1, 0);
linkedList.insert(2, true);
let result = linkedList.get(1);
console.info("result:", result);  // result: 0
```

#### has

has(element: T): boolean

判断LinkedList中是否包含指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明boolean包含指定元素返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The has method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<string>();
linkedList.add("squirrel");
let result = linkedList.has("squirrel");
console.info("result:", result);  // result: true
```

#### get

get(index: number): T

根据下标获取LinkedList中的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定的下标值。需要小于等于int32_max即2147483647。

**返回值：**

类型说明T根据下标查找到的元素，元素不存在返回undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The get method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(1);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.get(2);
console.info("result:", result);  // result: 5
```

#### getLastIndexOf

getLastIndexOf(element: T): number

查找指定元素最后一次出现时的下标值，查找失败返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明number返回指定元素最后一次出现时的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The getLastIndexOf method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(1);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.getLastIndexOf(2);
console.info("result:", result);  // result: 5
```

#### getIndexOf

getIndexOf(element: T): number

查找指定元素第一次出现时的下标值，查找失败返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明number返回指定元素第一次出现时的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The getIndexOf method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(1);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.getIndexOf(2);
console.info("result:", result);  // result: 0
```

#### removeByIndex

removeByIndex(index: number): T

根据元素的下标值查找元素，并将其删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定元素的下标值。需要小于等于int32_max即2147483647。

**返回值：**

类型说明T返回删除的元素，如果元素为空返回undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of index is out of range.10200011The removeByIndex method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.removeByIndex(2);
console.info("result:", result);  // result: 5
```

#### removeFirst

removeFirst(): T

删除并返回LinkedList的第一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回删除的元素。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200010Container is empty.10200011The removeFirst method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.removeFirst();
console.info("result:", result);  // result: 2
```

#### removeLast

removeLast(): T

删除并返回LinkedList的最后一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回删除的元素。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200010Container is empty.10200011The removeLast method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(2);
linkedList.add(4);
let result = linkedList.removeLast();
console.info("result:", result);  // result: 4
```

#### remove

remove(element: T): boolean

删除查找到的第一个指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明boolean删除成功返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The remove method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.remove(2);
console.info("result:", result);  // result: true
```

#### removeFirstFound

removeFirstFound(element: T): boolean

删除第一次出现的指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明boolean删除成功返回true，删除失败或不存在该元素时返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200010Container is empty.10200011The removeFirstFound method cannot be bound.10200017The element does not exist in this container.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.removeFirstFound(4);
console.info("result:", result);  // result: true
```

#### removeLastFound

removeLastFound(element: T): boolean

删除最后一次出现的指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明boolean删除成功返回true，删除失败或不存在该元素时返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200010Container is empty.10200011The removeLastFound method cannot be bound.10200017The element does not exist in this container.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.removeLastFound(4);
console.info("result:", result);  // result: true
```

#### clone

clone(): LinkedList<T>

克隆一个与LinkedList相同的实例并返回。修改克隆后的实例并不会影响原实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明LinkedList<T>返回LinkedList对象实例。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The clone method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.clone();
console.info("result:", result.has(4));  // result: true
```

#### forEach

forEach(callbackFn: (value: T, index?: number, LinkedList?: LinkedList<T>) => void,

thisArg?: Object): void

通过回调函数来遍历LinkedList实例对象上的元素以及其下标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackFn被调用时用作this值，默认值为当前实例对象。

callbackFn的参数说明：

参数名类型必填说明valueT是当前遍历到的元素。indexnumber否当前遍历到的下标值，默认值为0。LinkedListLinkedList<T>否当前调用forEach方法的实例对象，默认值为当前实例对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The forEach method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
linkedList.forEach((value: number, index: number) => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

#### clear

clear(): void

清除LinkedList中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The clear method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
linkedList.clear();
let result = linkedList.has(2);
console.info("result:", result);  // result: false
```

#### set

set(index: number, element: T): T

替换LinkedList指定位置的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是查找的下标值。需要小于等于int32_max即2147483647。elementT是用来替换的元素。

**返回值：**

类型说明T返回替换后的元素，如果元素为空则返回undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200001The value of index is out of range.10200011The set method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number | string>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.set(2, "b");
console.info("result:", result);  // result: b
```

#### convertToArray

convertToArray(): Array<T>

将当前LinkedList实例转换成数组并返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明Array<T>返回转换后的数组。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The convertToArray method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.convertToArray();
console.info("result:", result);  // result: 2,4,5,4
```

#### getFirst

getFirst(): T

获取LinkedList实例中的第一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回对应元素，若元素为空则返回undefined。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The getFirst method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.getFirst();
console.info("result:", result);  // result: 2
```

#### getLast

getLast(): T

获取LinkedList实例中的最后一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回对应元素，若元素为空则返回undefined。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The getLast method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);
let result = linkedList.getLast();
console.info("result:", result);  // result: 4
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<T>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let linkedList = new LinkedList<number>();
linkedList.add(2);
linkedList.add(4);
linkedList.add(5);
linkedList.add(4);

// 使用方法一：
for (let item of linkedList) {
  console.info("value:", item);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
let iter = linkedList[Symbol.iterator]();
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