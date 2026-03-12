# @ohos.util.Queue (线性容器Queue)

Queue的特点是先进先出，在尾部增加元素，在头部删除元素。根据循环队列的数据结构实现。

Queue和[Deque](@ohos.util.Deque (线性容器Deque).md)相比，Queue只能在一端删除一端增加，Deque可以两端增删。

**推荐使用场景：** 一般符合先进先出的场景可以使用Queue。

文档中使用了泛型，涉及以下泛型标记符：

- T：Type，类

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

#### 导入模块

```ets
import { Queue } from '@kit.ArkTS';
```

#### Queue

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否Queue的元素个数。

#### constructor

constructor()

Queue的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200012The Queue's constructor cannot be directly invoked.

**示例：**

```ets
let queue = new Queue<number | string | Object>();
```

#### add

add(element: T): boolean

在队列尾部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是要插入的元素。

**返回值：**

类型说明boolean插入成功返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The add method cannot be bound.

**示例：**

```ets
class C1 {
  name: string = ""
  age: string = ""
}
let queue = new Queue<number | string | C1 | number[]>();
let result = queue.add("a");
let result1 = queue.add(1);
let b = [1, 2, 3];
let result2 = queue.add(b);
let c : C1 = {name : "Dylan", age : "13"};
let result3 = queue.add(c);
console.info("result:", queue.length);  // result: 4
```

#### pop

pop(): T

删除头元素并返回该删除元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回删除的元素。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The pop method cannot be bound.

**示例：**

```ets
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(2);
queue.add(4);
let result = queue.pop();
console.info("result:", result);  // result: 2
```

#### getFirst

getFirst(): T

获取队列的头元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回获取的元素。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The getFirst method cannot be bound.

**示例：**

```ets
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(2);
let result = queue.getFirst();
console.info("result:", result);  // result: 2
```

#### forEach

forEach(callbackFn: (value: T, index?: number, Queue?: Queue<T>) => void,

thisArg?: Object): void

在遍历Queue实例对象中每一个元素的过程中，对每个元素执行回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackfn被调用时用作this值，默认值为当前实例对象。

callbackfn的参数说明：

参数名类型必填说明valueT是当前遍历到的元素。indexnumber否当前遍历到的下标值，默认值为0。QueueQueue<T>否当前调用forEach方法的实例对象，默认值为当前实例对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The forEach method cannot be bound.

**示例：**

```ets
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(4);
queue.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，每一项都是一个JavaScript对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<T>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(4);

// 使用方法一：
for (let value of queue) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
let iter = queue[Symbol.iterator]();
let temp: IteratorResult<number> = iter.next().value;
while(temp != undefined) {
  console.info("value: " + temp);
  temp = iter.next().value;
}
// value: 2
// value: 4
// value: 5
// value: 4
```