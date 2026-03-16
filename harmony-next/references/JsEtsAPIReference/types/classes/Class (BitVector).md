# Class (BitVector)

BitVector是一种线性数据结构，底层基于数组实现。BitVector中存储元素为bit值，能存储和处理bit级别的操作。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

**装饰器类型：**@Sendable

#### 导入模块

```ets
import { collections } from '@kit.ArkTS';
```

#### 属性

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明lengthnumber是否BitVector的元素个数。

#### constructor

constructor(length: number)

BitVector的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明lengthnumber是初始化BitVector的长度。

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
```

#### push

push(element:number): boolean

在BitVector尾部插入元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementnumber是待插入的元素，0表示0，其余值表示1。

**返回值：**

类型说明boolean插入成功返回true，失败返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200011The push method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
```

#### pop

pop(): number

弹出BitVector尾部的元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number弹出BitVector尾部的元素，其值为对应bit值。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The pop method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
let res = bitVector.pop(); // bitVector: [0, 1, 0, 1]
console.info("bitVector pop:", res); // 0
```

#### has

has(element: number, fromIndex: number, toIndex: number): boolean

判断范围内是否包含特定bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementnumber是待判断的bit值，0表示0，其余值表示1。fromIndexnumber是范围起始索引，包含本索引值。fromIndex<0或者fromIndex>=toIndex时，则会抛出错误。toIndexnumber是范围终止索引，包含本索引值。toIndex<0或者toIndex>=length时，则会抛出错误。

**返回值：**

类型说明boolean包含特定bit值返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of fromIndex or toIndex is out of range.10200011The has method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
let res0: boolean = bitVector.has(0, 1, 4);
console.info("bitVector has 0:", res0); // true
```

#### setBitsByRange

setBitsByRange(element: number, fromIndex: number, toIndex: number): void

将BitVector中指定范围的元素均设为特定bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementnumber是待设置的bit值，0表示0，其余表示1。fromIndexnumber是范围起始索引，包含本索引值。fromIndex<0或者fromIndex>=toIndex时，则会抛出错误。toIndexnumber是范围终止索引，不包含本索引值。toIndex<0或者toIndex>=length时，则会抛出错误。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200001The value of fromIndex or toIndex is out of range.10200011The setBitsByRange method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
bitVector.setBitsByRange(1, 1, 3); // bitVector: [0, 1, 1, 1, 0]
```

#### setAllBits

setAllBits(element: number): void

将BitVector中所有元素均设为特定bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementnumber是待设置的元素，0表示0，其余值表示1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200011The setAllBits method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
bitVector.setAllBits(1); // bitVector: [1, 1, 1, 1, 1]
```

#### getBitsByRange

getBitsByRange(fromIndex: number, toIndex: number): BitVector

获取指定范围内的bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明fromIndexnumber是范围起始索引，包含本索引值。fromIndex<0或者fromIndex>=toIndex时，则会抛出错误。toIndexnumber是范围终止索引，不包含本索引值。toIndex<0或者toIndex>=length时，则会抛出错误。

**返回值：**

类型说明BitVector指定范围内的bit值组成的BitVector。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200001The value of fromIndex or toIndex is out of range.10200011The getBitsByRange method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
let bitVector2 = bitVector.getBitsByRange(1, 3); // bitVector2: [1, 0]
console.info("bitVector2 length:", bitVector2.length); // 2
```

#### resize

resize(size: number): void

改变BitVector的长度。

若size大于原BitVector的长度，则扩充原BitVector的长度，多出的部分其元素设置为0；

若size小于等于原BitVector的长度，则将原BitVector按size长度大小裁剪。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明sizenumber是需要改变的长度。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200011The resize method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
bitVector.resize(10); // bitVector: [0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
console.info("bitVector get bit vector's length:", bitVector.length); // 10
bitVector.resize(3); // bitVector: [0, 1, 0]
console.info("bitVector get bit vector's length:", bitVector.length); // 3
```

#### getBitCountByRange

getBitCountByRange(element: number, fromIndex: number, toIndex: number): number

统计指定范围内获取指定bit值的数量。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementnumber是待统计的bit值，0表示0，其余值表示1。fromIndexnumber是范围起始索引，包含本索引值。fromIndex<0或者fromIndex>=toIndex时，则会抛出错误。toIndexnumber是范围终止索引，不包含本索引值。toIndex<0或者toIndex>=length时，则会抛出错误。

**返回值：**

类型说明number统计指定范围内获取指定bit值的数量。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200001The value of fromIndex or toIndex is out of range.10200011The getBitCountByRange method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
let res: number = bitVector.getBitCountByRange(1, 1, 4);
console.info("bitVector getBitCountByRange:", res); // 2
```

#### getIndexOf

getIndexOf(element: number, fromIndex: number, toIndex: number): number

返回指定bit值首次出现时的索引值，查找失败返回-1。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementnumber是待统计的bit值，0表示0，其余值表示1。fromIndexnumber是范围起始索引，包含本索引值。fromIndex<0或者fromIndex>=toIndex时，则会抛出错误。toIndexnumber是范围终止索引，不包含本索引值。toIndex<0或者toIndex>=length时，则会抛出错误。

**返回值：**

类型说明number返回指定bit值首次出现时的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200001The value of fromIndex or toIndex is out of range.10200011The getIndexOf method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
let res: number = bitVector.getIndexOf(0, 1, 4);
console.info("bitVector getIndexOf:", res); // 2
```

#### getLastIndexOf

getLastIndexOf(element: number, fromIndex: number, toIndex: number): number

返回指定bit值最后一次出现时的下标值，查找失败返回-1。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明elementnumber是待统计的bit值，0表示0，其余值表示1。fromIndexnumber是范围起始索引，包含本索引值。fromIndex<0或者fromIndex>=toIndex时，则会抛出错误。toIndexnumber是范围终止索引，不包含本索引值。toIndex<0或者toIndex>=length时，则会抛出错误。

**返回值：**

类型说明number返回指定bit值最后一次出现时的下标值，查找失败返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200001The value of fromIndex or toIndex is out of range.10200011The getLastIndexOf method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
let res: number = bitVector.getLastIndexOf(0, 1, 4);
console.info("bitVector getLastIndexOf:", res); // 2
```

#### flipBitByIndex

flipBitByIndex(index: number): void

翻转BitVector指定索引处的bit值，0翻转为1，1翻转为0。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是指定索引。index<0或者index>=length时，则会抛出错误。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200001The value of index is out of range.10200011The flipBitByIndex method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
bitVector.flipBitByIndex(3); // bitVector: [0, 1, 0, 0, 0]
```

#### flipBitsByRange

flipBitsByRange(fromIndex: number, toIndex: number): void

翻转BitVector指定范围内的bit值，0翻转为1，1翻转为0。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明fromIndexnumber是范围起始索引，包含本索引值。fromIndex<0或者fromIndex>=toIndex时，则会抛出错误。toIndexnumber是范围终止索引，不包含本索引值。toIndex<0或者toIndex>=length时，则会抛出错误。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.10200001The value of fromIndex or toIndex is out of range.10200011The flipBitsByRange method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
bitVector.flipBitsByRange(1, 4); // bitVector: [0, 0, 1, 0, 0]
```

#### values

values(): IterableIterator<number>

返回一个新的迭代器对象，该对象包含BitVector中每个元素的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<number>返回一个BitVector迭代器对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The values method cannot be bound.10200201Concurrent modification error.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
let iter: IterableIterator<number> = bitVector.values();
let temp: IteratorResult<number> = iter.next();
while (!temp.done) {
  console.info(JSON.stringify(temp.value));
  temp = iter.next();
} // 依次输出 0,1,0,1,0
```

#### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<number>

返回一个迭代器，迭代器的每一项都是一个 JavaScript 对象，并返回该对象。

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<number>返回一个迭代器。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200011The Symbol.iterator method cannot be bound.

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);

for (let item of bitVector) {
  console.info("value: " + item);
}
```

#### [index: number]

[index: number]: number

返回BitVector指定索引位置的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明indexnumber是所需代码单元的从零开始的索引。

**返回值：**

类型说明number返回number数据类型。

**示例：**

```ets
let bitVector: collections.BitVector = new collections.BitVector(0);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0);
bitVector.push(1);
bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
console.info("BitVector Element Index at 1: " + bitVector[1]);
```