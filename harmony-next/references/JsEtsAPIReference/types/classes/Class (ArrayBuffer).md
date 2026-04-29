# Class (ArrayBuffer)

ArkTS TypedArray（[Int8Array](Class (Int8Array).md)、[Uint8Array](Class (Uint8Array).md)、[Int16Array](Class (Int16Array).md)、[Uint16Array](Class (Uint16Array).md)、[Int32Array](Class (Int32Array).md)、[Uint32Array](Class (Uint32Array).md)、[Uint8ClampedArray](Class (Uint8ClampedArray).md)、[Float32Array](Class (Float32Array).md)）的底层数据结构。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

**装饰器类型：**@Sendable

#### 导入模块

```ets
import { collections } from '@kit.ArkTS';
```

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| byteLength | number | 是 | 否 | buffer所占的字节数。 |

#### constructor

constructor(byteLength: number)

构造函数，用于创建一个指定长度的ArkTS ArrayBuffer对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteLength | number | 是 | buffer所占的字节数， 最大值不能超过2147483647。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[语言基础类库错误码]([语言基础类库错误码](../../errors/语言基础类库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The ArrayBuffer's constructor cannot be directly invoked. |

**示例：**

```ets
let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(10);
console.info("byteLength: " + arrayBuffer.byteLength); // byteLength: 10
```

#### slice

slice(begin: number, end?: number): ArrayBuffer

返回一个新的ArkTS ArrayBuffer对象，其包含原ArkTS ArrayBuffer指定范围的内容。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 是 | 开始索引，如果begin < 0，则会从begin + arrayBuffer.byteLength位置开始。 |
| end | number | 否 | 结束索引（不包括该元素），如果end < 0，则会到end + arrayBuffer.byteLength位置结束。默认为原ArkTS ArrayBuffer的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 新的ArkTS ArrayBuffer对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The slice method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```ets
let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(10);
let slicedBuffer: collections.ArrayBuffer = arrayBuffer.slice(0, 4);
console.info("byteLength: " + slicedBuffer.byteLength); // byteLength: 4
```