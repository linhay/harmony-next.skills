# @ohos.util.Stack (线性容器Stack)

Stack基于数组的数据结构实现，特点是先进后出，只能在一端进行数据的插入和删除。

Stack和[Queue](@ohos.util.Queue (线性容器Queue).md)相比，Queue基于循环队列实现，只能在一端删除另一端插入，而Stack都在一端操作。

**推荐使用场景：** 一般符合先进后出的场景可以使用Stack。

文档中使用了泛型，涉及以下泛型标记符：

- T：Type，类

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

#### 导入模块

```ets
import { Stack } from '@kit.ArkTS';
```

#### Stack

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否Stack的元素个数。

#### constructor

constructor()

Stack的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200012The Stack's constructor cannot be directly invoked.

**示例：**

```ets
let stack = new Stack<number | string | Object>();
```

#### push

push(item: T): T

在栈顶插入元素，并返回该元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明itemT是添加进去的元素。

**返回值：**

类型说明T返回被添加进去的元素。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The push method cannot be bound.

**示例：**

```ets
class C1 {
  name: string = ""
  age: string = ""
}
let stack = new Stack<number | string | C1>();
let result = stack.push("a");
let result1 = stack.push(1);
let c : C1  = {name : "Dylan", age : "13"};
let result2 = stack.push(c);
console.info("length:", stack.length);  // length: 3
```

#### pop

pop(): T

删除栈顶元素并返回，栈为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回栈顶元素，栈为空时返回undefined。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The pop method cannot be bound.

**示例：**

```ets
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
stack.push(4);
let result = stack.pop();
console.info("result = " + result); // result = 4
```

#### peek

peek(): T

返回栈顶元素，栈为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明T返回栈顶元素，栈为空时返回undefined。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The peek method cannot be bound.

**示例：**

```ets
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
let result = stack.peek();
console.info("result:", result);  // result: 2
```

#### locate

locate(element: T): number

查找指定元素首次出现的下标值，查找失败则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementT是指定元素。

**返回值：**

类型说明number对应元素下标值，查找失败则返回-1。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The locate method cannot be bound.

**示例：**

```ets
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
let result = stack.locate(5);
console.info("result:", result);  // result: 2
```

#### forEach

forEach(callbackFn: (value: T, index?: number, stack?: Stack<T>) => void,

thisArg?: Object): void

在遍历Stack实例对象中每一个元素的过程中，对每个元素执行回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFnfunction是回调函数。thisArgObject否callbackFn被调用时用作this值，默认值为当前实例对象。

callbackFn的参数说明：

参数名类型必填说明valueT是当前遍历到的元素。indexnumber否当前遍历到的下标值，默认值为0。stackStack<T>否当前调用forEach方法的实例对象，默认值为当前实例对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200011The forEach method cannot be bound.

**示例：**

```ets
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);
stack.forEach((value : number, index: number) :void => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

#### isEmpty

isEmpty(): boolean

判断栈是否为空。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean为空返回true，不为空返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息10200011The isEmpty method cannot be bound.

**示例：**

```ets
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);
let result = stack.isEmpty();
console.info("result:", result);  // result: false
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
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);

// 使用方法一：
for (let value of stack) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
let iter = stack[Symbol.iterator]();
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