# Interface (ConcatArray)

表示可以进行连接的类似数组的对象。该接口扩展了ISendable接口。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

文档中存在泛型的使用，涉及以下泛型标记符：

- T：Type，支持[Sendable支持的数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable支持的数据类型)。

#### 导入模块

```ets
import { collections } from '@kit.ArkTS';
```

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否ConcatArray的元素个数。

#### [index: number]

readonly [index: number]: T

返回ConcatArray指定索引位置的元素。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是所需代码单元的从零开始的索引，不支持修改指定索引位置的元素。

**返回值：**

类型说明TConcatArray给定的元素数据类型。

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Illegal index.10200001The value of index is out of range.

**示例：**

```ets
let concatArray : collections.ConcatArray<number> = new collections.Array<number>(1, 2, 4);
console.info("Element at index 1: ", concatArray[1]);
```

#### join

join(separator?: string): string

将ConcatArray的所有元素连接成一个字符串，元素之间可以用指定的分隔符分隔。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明separatorstring否用于分隔ConcatArray元素的字符串。如果省略，则使用逗号分隔。

**返回值：**

类型说明string包含所有ConcatArray元素连接成的字符串。如果ConcatArray为空，则返回空字符串。

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Invalid separator.

**示例：**

```ets
let concatArray : collections.ConcatArray<string> = new collections.Array<string>('a', 'b', 'c');
let joinedString = concatArray.join('-'); // 返回 "a-b-c"
```

#### slice

slice(start?: number, end?: number): ConcatArray<T>

返回一个新的ConcatArray，该ConcatArray是原始ConcatArray的切片。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明startnumber否开始索引。如果start < 0，则会从start + array.length位置开始。默认值为0。endnumber否结束索引（不包括该元素）。如果end < 0，则会到end + array.length位置结束。默认为ArkTS Array的长度。

**返回值：**

类型说明ConcatArray<T>包含原始ConcatArray切片的新ConcatArray。

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Invalid `start` or `end` parameters.

**示例：**

```ets
let concatArray : collections.ConcatArray<number> = new collections.Array<number>(1, 2, 3, 4, 5);
let slicedArray = concatArray.slice(1, 3); // 返回[2, 3]，原Array保持不变
```