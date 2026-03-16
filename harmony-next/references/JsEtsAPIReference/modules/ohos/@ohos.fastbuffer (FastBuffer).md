# @ohos.fastbuffer (FastBuffer)

FastBuffer对象是更高效的Buffer容器，用于表示固定长度的字节序列，是专门存放二进制数据的缓存区。

FastBuffer通过from构造时，仅支持FastBuffer、Uint8Array、string、Array、ArrayBuffer类型的参数。

需要高性能处理大型二进制数据（如图片、文件传输、网络通信等）时，推荐使用FastBuffer。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

#### 导入模块

```ets
import { fastbuffer } from '@kit.ArkTS';
```

#### BufferEncoding

type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex'

表示支持的编码格式类型。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

类型说明'ascii'表示ascii格式。'utf8'表示utf8格式。'utf-8'表示utf8格式。'utf16le'表示utf16小端序格式。'ucs2'utf16le格式的别名。'ucs-2'utf16le格式的别名。'base64'表示base64格式。'base64url'表示base64url格式。'latin1'iso-8859-1的别名，向下兼容ascii格式。'binary'表示二进制格式。'hex'表示十六进制格式。

#### fastbuffer.alloc

alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer

创建指定字节长度的FastBuffer对象并初始化。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明sizenumber是指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32_MAX。fillstring | FastBuffer | number否填充至新缓存区的值，默认值：0。encoding[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)否编码格式（当fill为string时，才有意义）。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)返回一个FastBuffer对象。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.alloc(5);
let buf2 = fastbuffer.alloc(5, 'a');
let buf3 = fastbuffer.alloc(11, 'aGVsbG8gd29ybGQ=', 'base64');
console.info(buf2.toString());
// 输出结果：aaaaa
console.info(buf3.toString());
// 输出结果：hello world
```

#### fastbuffer.allocUninitializedFromPool

allocUninitializedFromPool(size: number): FastBuffer

从缓冲池中创建指定大小未初始化的FastBuffer对象，需要使用[fill](#ZH-CN_TOPIC_0000002529444717__fill)函数来初始化FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明sizenumber是指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32_MAX。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)未初始化的Buffer实例。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(10);
buf.fill(0);
// "buf":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

#### fastbuffer.allocUninitialized

allocUninitialized(size: number): FastBuffer

创建指定大小未初始化的FastBuffer对象，需要使用[fill](#ZH-CN_TOPIC_0000002529444717__fill)函数来初始化FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明sizenumber是指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32_MAX。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)未初始化的FastBuffer实例。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitialized(10);
buf.fill(0);
// "buf":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

#### fastbuffer.byteLength

byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number

根据不同的编码格式，返回指定字符串的字节数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuestring | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer是指定字符串。encoding[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)否编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。

**返回值：**

类型说明number返回指定字符串的字节数。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let str = 'hello world';
console.info(`${str}: ${str.length} characters, ${fastbuffer.byteLength(str, 'utf-8')} bytes`);
// 输出结果：hello world: 11 characters, 11 bytes

str = '\u00bd + \u00bc = \u00be';
console.info(`${str}: ${str.length} characters, ${fastbuffer.byteLength(str, 'utf-8')} bytes`);
// 输出结果：½ + ¼ = ¾: 9 characters, 12 bytes
```

#### fastbuffer.compare

compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1

返回两个FastBuffer对象的比较结果，通常用于对FastBuffer对象数组进行排序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明buf1[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer) | Uint8Array是待比较的第一个对象。buf2[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer) | Uint8Array是待比较的第二个对象。

**返回值：**

类型说明-1 | 0 | 1

如果buf1与buf2相同，则返回0。

如果排序时buf1位于buf2之后，则返回1。

如果排序时buf1位于buf2之前，则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('1234');
let buf2 = fastbuffer.from('0123');
let res = fastbuffer.compare(buf1, buf2);

console.info(Number(res).toString());
// 输出结果：1
```

#### fastbuffer.concat

concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer

将数组中指定字节长度的内容复制到新的FastBuffer对象中并返回拼接后的FastBuffer对象。

当数组中所有对象的长度总和大于totalLength时，返回结果的长度将被截断为totalLength。

当数组中所有对象的长度总和小于totalLength时，返回结果的多余部分将会被填充为0。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明list[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)[] | Uint8Array[]是实例数组。totalLengthnumber否需要复制的总字节长度，默认值为0。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)返回新的FastBuffer对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001Range error. Possible causes: The value of the parameter is not within the specified range.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from("1234");
let buf2 = fastbuffer.from("abcd");
let buf = fastbuffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// 输出结果：3132333461626364
```

#### fastbuffer.from

from(array: number[]): FastBuffer

根据指定数组创建新的FastBuffer对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明arraynumber[]是指定数组。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)新的FastBuffer对象。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72]);
console.info(buf.toString('hex'));
// 输出结果：627566666572
```

#### fastbuffer.from

from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer

创建与arrayBuffer共享内存的指定长度的FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明arrayBufferArrayBuffer | SharedArrayBuffer是实例对象。byteOffsetnumber否字节偏移量，默认值：0。lengthnumber否字节长度， 默认值:（arrayBuffer.byteLength - byteOffset）。取值范围：0 <= length <= arrayBuffer.byteLength - byteOffset

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)返回一个FastBuffer对象，该对象与入参对象arrayBuffer共享相同的内存区域。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001Range error. Possible causes: The value of the parameter is not within the specified range.10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let ab = new ArrayBuffer(10);
let buf = fastbuffer.from(ab, 0, 2);
console.info(buf.length.toString());
// 输出结果：2
```

#### fastbuffer.from

from(buffer: FastBuffer | Uint8Array): FastBuffer

当入参为FastBuffer对象时，创建新的FastBuffer对象并复制入参FastBuffer对象的数据，然后返回新对象。

当入参为Uint8Array对象时，基于Uint8Array对象的内存创建新的FastBuffer对象并返回，保持数据的内存关联。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明buffer[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer) | Uint8Array是对象数据。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)返回新的FastBuffer对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

// 以FastBuffer对象类型进行创建新的FastBuffer对象
let buf1 = fastbuffer.from('buffer');
let buf2 = fastbuffer.from(buf1);
console.info(buf2.toString());
// 输出结果：buffer

// 以Uint8Array对象类型进行创建FastBuffer对象，保持对象间内存共享
let uint8Array = new Uint8Array(10);
let buf3 = fastbuffer.from(uint8Array);
buf3.fill(1)
console.info("uint8Array:", uint8Array)
// 输出结果：1,1,1,1,1,1,1,1,1,1
```

#### fastbuffer.from

from(value: string, encoding?: BufferEncoding): FastBuffer

根据指定编码格式的字符串，创建新的FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuestring是字符串。encoding[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)否编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)返回新的FastBuffer对象。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('this is a test');
let buf2 = fastbuffer.from('7468697320697320612074c3a97374', 'hex');

console.info(buf1.toString());
// 输出结果：this is a test
console.info(buf2.toString());
// 输出结果：this is a tést
```

#### fastbuffer.isBuffer

isBuffer(obj: Object): boolean

判断obj是否为FastBuffer。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明objObject是判断对象。

**返回值：**

类型说明boolean如果obj是FastBuffer，则返回true，否则返回false。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let result = fastbuffer.isBuffer(fastbuffer.alloc(10)); // 10: fastbuffer size
console.info("result = " + result);
// 输出结果：result = true
let result1 = fastbuffer.isBuffer(fastbuffer.from('foo'));
console.info("result1 = " + result1);
// 输出结果：result1 = true
let result2 = fastbuffer.isBuffer('a string');
console.info("result2 = " + result2);
// 输出结果：result2 = false
let result3 = fastbuffer.isBuffer([]);
console.info("result3 = " + result3);
// 输出结果：result3 = false
let result4 = fastbuffer.isBuffer(new Uint8Array(1024));
console.info("result4 = " + result4);
// 输出结果：result4 = false
```

#### fastbuffer.isEncoding

isEncoding(encoding: string): boolean

判断encoding是否为支持的编码格式。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring是编码格式。

**返回值：**

类型说明boolean是支持的编码格式返回true，反之则返回false。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

console.info(fastbuffer.isEncoding('utf-8').toString());
// 输出结果：true
console.info(fastbuffer.isEncoding('hex').toString());
// 输出结果：true
console.info(fastbuffer.isEncoding('utf/8').toString());
// 输出结果：false
console.info(fastbuffer.isEncoding('').toString());
// 输出结果：false
```

#### fastbuffer.transcode

transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer

将FastBuffer或Uint8Array对象从fromEnc编码转换为toEnc编码。

fastbuffer.transcode支持的编码：'ascii' | 'utf8' | 'utf16le'| 'ucs2' | 'latin1'| 'binary'。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明source[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer) | Uint8Array是实例对象。fromEncstring是当前编码。 支持的格式范围为[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)。toEncstring是目标编码。 支持的格式范围为[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)将当前编码转换成目标编码，并返回一个新的FastBuffer对象。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let newBuf = fastbuffer.transcode(fastbuffer.from('buffer'), 'utf-8', 'ascii');
console.info("newBuf = " + newBuf.toString('ascii'));
// 输出结果：newBuf = buffer
```

#### FastBuffer

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

名称类型只读可选说明lengthnumber是否FastBuffer对象的字节长度。bufferArrayBuffer是否ArrayBuffer对象。byteOffsetnumber是否当前Buffer所在内存池的偏移量。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from("1236");
console.info(JSON.stringify(buf.length));
// 输出结果：4
let arrayBuffer = buf.buffer;
console.info(JSON.stringify(new Uint8Array(arrayBuffer)));
// 输出结果：{"0":49,"1":50,"2":51,"3":54}
console.info(JSON.stringify(buf.byteOffset));
// 输出结果：0
```

#### compare

compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1

比较当前对象this与目标对象target，并返回比较结果。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明target[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer) | Uint8Array是要比较的实例对象。targetStartnumber否target实例中开始的偏移量。默认值：0。 0 <= targetStart <= target.length。targetEndnumber否target实例中结束的偏移量（不包含结束位置）。默认值：目标对象的字节长度。取值范围：0 <= targetEnd <= target.length。sourceStartnumber否this实例中开始的偏移量。默认值：0。取值范围：0 <= sourceStart <= this.length。sourceEndnumber否this实例中结束的偏移量（不包含结束位置）。默认值：当前对象的字节长度。取值范围：0 <= sourceEnd <= this.length。

**返回值：**

类型说明-1 | 0 | 1

返回比较结果。

-1：当前排列在目标前；

0：当前与目标相同；

1：当前排列在目标后。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001Range error. Possible causes: The value of the parameter is not within the specified range.10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
let buf2 = fastbuffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
// 输出结果：0
console.info(buf1.compare(buf2, 0, 6, 4).toString());
// 输出结果：-1
console.info(buf1.compare(buf2, 5, 6, 5).toString());
// 输出结果：1
```

#### copy

copy(target: FastBuffer| Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number

将this实例中指定位置的数据复制到target的指定位置上，并返回复制的字节总长度。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明target[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer) | Uint8Array是要复制到的Buffer或Uint8Array实例。targetStartnumber否target实例中开始写入的偏移量。默认值：0。取值范围：0 <= targetStart <= UINT32_MAX。sourceStartnumber否this实例中开始复制的偏移量。默认值: 0。取值范围：0 <= sourceStart <= UINT32_MAX。sourceEndnumber否this实例中结束复制的偏移量（不包含结束位置）。默认值：当前对象的字节长度。取值范围：0 <= sourceEnd <= this.length。

**返回值：**

类型说明number复制的字节总长度。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001Range error. Possible causes: The value of the parameter is not within the specified range.10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.allocUninitializedFromPool(26);
let buf2 = fastbuffer.allocUninitializedFromPool(26).fill('!');

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}

buf1.copy(buf2, 8, 16, 20);
console.info(buf2.toString('ascii', 0, 25));
// 输出结果：!!!!!!!!qrst!!!!!!!!!!!!!
```

#### entries

entries(): IterableIterator<[number, number]>

返回一个包含key值和value值的迭代器。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<[number, number]>包含key和value的迭代器，同时两者皆为number类型。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('buffer');
let pair = buf.entries();
let next: IteratorResult<Object[]> = pair.next();
while (!next.done) {
  console.info("fastbuffer: " + next.value);
  /*
  输出结果：buffer: 0,98
           fastbuffer: 1,117
           fastbuffer: 2,102
           fastbuffer: 3,102
           fastbuffer: 4,101
           fastbuffer: 5,114
  */
  next = pair.next();
}
```

#### equals

equals(otherBuffer: Uint8Array | FastBuffer): boolean

逐字节比较this和otherBuffer是否相等。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明otherBufferUint8Array | FastBuffer是比较的目标对象。

**返回值：**

类型说明boolean若this和otherBuffer逐字节相等则返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('ABC');
let buf2 = fastbuffer.from('414243', 'hex');
let buf3 = fastbuffer.from('ABCD');

console.info(buf1.equals(buf2).toString());
// 输出结果：true
console.info(buf1.equals(buf3).toString());
// 输出结果：false
```

#### fill

fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer

使用value填充当前对象指定位置的数据，默认为循环填充，并返回填充后的FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuestring | FastBuffer | Uint8Array | number是用于填充的值。offsetnumber否起始偏移量。默认值：0。取值范围：0 <= offset <= this.length。endnumber否结束偏移量（不包含结束位置）。 默认值：当前对象的字节长度。取值范围：0 <= end <= this.length。encoding[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)否字符编码格式（value为string才有意义）。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。

**返回值：**

类型说明[FastBuffer](#ZH-CN_TOPIC_0000002529444717__fastbuffer)返回填充后的FastBuffer对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001Range error. Possible causes: The value of the parameter is not within the specified range.10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let b = fastbuffer.allocUninitializedFromPool(50).fill('h');
console.info(b.toString());
// 输出结果：hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
```

#### includes

includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean

检查FastBuffer对象是否包含value值。

若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。

当byteOffset大于等于this.length时，返回false。当byteOffset小于等于-this.length，查找整个FastBuffer中是否存在value。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuestring | number | FastBuffer | Uint8Array是要搜索的内容。byteOffsetnumber否字节偏移量。若为正数，则从0开始计算偏移量；若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。默认值：0。encoding[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)否字符编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。

**返回值：**

类型说明boolean若FastBuffer对象包含value值时返回true，否则为false。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('this is a buffer');
console.info(buf.includes('this').toString());
// 输出结果：true
console.info(buf.includes('be').toString());
// 输出结果：false
```

#### indexOf

indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number

返回当前对象中首次出现value的索引，如果不包含value，则返回-1。

若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。

当byteOffset大于等于this.length时，返回-1。当byteOffset小于等于-this.length，返回整个FastBuffer中首次出现value的索引。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuestring | number | FastBuffer | Uint8Array是要查找的内容。byteOffsetnumber否字节偏移量。若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。默认值：0。encoding[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)否字符编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。

**返回值：**

类型说明number返回第一次出现的位置。

**示例**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('this is a buffer');
console.info(buf.indexOf('this').toString());
// 输出结果：0
console.info(buf.indexOf('is').toString());
// 输出结果：2
```

#### keys

keys(): IterableIterator<number>

返回一个包含key值的迭代器。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<number>返回一个包含key值的迭代器。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('buffer');
let keys = buf.keys();
for (const key of keys) {
  console.info(key.toString());
}
/*
输出结果：0
        1
        2
        3
        4
        5
*/
```

#### values

values(): IterableIterator<number>

返回一个包含value的迭代器。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明IterableIterator<number>迭代器。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('buffer');
let pair = buf1.values()
let next:IteratorResult<number> = pair.next()
while (!next.done) {
  console.info(next.value.toString());
  /*
  输出结果：98
           117
           102
           102
           101
           114
  */
  next = pair.next();
}
```

#### lastIndexOf

lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number

返回当前对象中最后一次出现value的索引，如果对象不包含value，则返回-1。

若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。

当byteOffset大于等于this.length时，返回整个FastBuffer中最后一次出现value的索引。当byteOffset小于等于-this.length时，返回-1。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuestring | number | FastBuffer | Uint8Array是要搜索的内容。byteOffsetnumber否字节偏移量。若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。默认值：this.length - 1。encoding[BufferEncoding](#ZH-CN_TOPIC_0000002529444717__bufferencoding)否字符编码格式。默认值：'utf8'。

**返回值：**

类型说明number最后一次出现value值的索引。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('this buffer is a buffer');
console.info(buf.lastIndexOf('this').toString());
// 输出结果：0
console.info(buf.lastIndexOf('buffer').toString());
// 输出结果：17
```

#### readBigInt64BE

readBigInt64BE(offset?: number): bigint

从指定的offset处读取有符号的大端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。

**返回值：**

类型说明bigint读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigInt64BE(0).toString());
// 输出结果：7161960797921896816
```

#### readBigInt64LE

readBigInt64LE(offset?: number): bigint

从指定的offset处读取有符号的小端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。

**返回值：**

类型说明bigint读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigInt64LE(0).toString());
// 输出结果：8100120198111388771
```

#### readBigUInt64BE

readBigUInt64BE(offset?: number): bigint

从指定的offset处读取无符号的大端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。

**返回值：**

类型说明bigint读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64BE(0).toString());
// 输出结果：7161960797921896816
```

#### readBigUInt64LE

readBigUInt64LE(offset?: number): bigint

从指定的offset处读取无符号的小端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。

**返回值：**

类型说明bigint读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64LE(0).toString());
// 输出结果：8100120198111388771
```

#### readDoubleBE

readDoubleBE(offset?: number): number

从指定的offset处读取64位大端序双精度值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleBE(0).toString());
// 输出结果：8.20788039913184e-304
```

#### readDoubleLE

readDoubleLE(offset?: number): number

从指定的offset处读取64位小端序双精度值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleLE(0).toString());
// 输出结果：5.447603722011605e-270
```

#### readFloatBE

readFloatBE(offset?: number): number

从指定的offset处读取32位大端序浮点数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatBE(0).toString());
// 输出结果：2.387939260590663e-38
```

#### readFloatLE

readFloatLE(offset?: number): number

从指定的offset处读取32位小端序浮点数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatLE(0).toString());
// 输出结果：1.539989614439558e-36
```

#### readInt8

readInt8(offset?: number): number

从指定的offset处读取有符号的8位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 1，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([-1, 5]);
console.info(buf.readInt8(0).toString());
// 输出结果：-1
console.info(buf.readInt8(1).toString());
// 输出结果：5
```

#### readInt16BE

readInt16BE(offset?: number): number

从指定的offset处读取有符号的大端序16位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 5]);
console.info(buf.readInt16BE(0).toString());
// 输出结果：5
```

#### readInt16LE

readInt16LE(offset?: number): number

从指定的offset处读取有符号的小端序16位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 5]);
console.info(buf.readInt16LE(0).toString());
// 输出结果：1280
```

#### readInt32BE

readInt32BE(offset?: number): number

从指定的offset处读取有符号的大端序32位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 0, 0, 5]);
console.info(buf.readInt32BE(0).toString());
// 输出结果：5
```

#### readInt32LE

readInt32LE(offset?: number): number

从指定的offset处读取有符号的小端序32位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 0, 0, 5]);
console.info(buf.readInt32LE(0).toString());
// 输出结果：83886080
```

#### readIntBE

readIntBE(offset: number, byteLength: number): number

从指定的offset处读取byteLength个字节，并将结果解释为支持最高48位精度的大端序、二进制补码有符号值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber是偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。byteLengthnumber是读取的字节数。取值范围：1 <= byteLength <= 6。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from("ab");
let num = buf.readIntBE(0, 1);
console.info(num.toString());
// 输出结果：97
```

#### readIntLE

readIntLE(offset: number, byteLength: number): number

从指定的offset处读取byteLength个字节，并将结果解释为支持最高48位精度的小端序、二进制补码有符号值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber是偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。byteLengthnumber是读取的字节数。取值范围：1 <= byteLength <= 6。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readIntLE(0, 6).toString(16));
// 输出结果：-546f87a9cbee
```

#### readUInt8

readUInt8(offset?: number): number

从offset处读取8位无符号整型数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 1，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, -2]);
console.info(buf.readUInt8(0).toString());
// 输出结果：1
console.info(buf.readUInt8(1).toString());
// 输出结果：254
```

#### readUInt16BE

readUInt16BE(offset?: number): number

从指定的offset处读取无符号的大端序16位整数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16BE(0).toString(16));
// 输出结果：1234
console.info(buf.readUInt16BE(1).toString(16));
// 输出结果：3456
```

#### readUInt16LE

readUInt16LE(offset?: number): number

从指定的offset处的buf读取无符号的小端序16位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16LE(0).toString(16));
// 输出结果：3412
console.info(buf.readUInt16LE(1).toString(16));
// 输出结果：5634
```

#### readUInt32BE

readUInt32BE(offset?: number): number

从指定的offset处的buf读取无符号的大端序32位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32BE(0).toString(16));
// 输出结果：12345678
```

#### readUInt32LE

readUInt32LE(offset?: number): number

从指定的offset处的buf读取无符号的小端序32位整数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明offsetnumber否偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。

**返回值：**

类型说明number读取出的内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset].

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32LE(0).toString(16));
// 输出结果：78563412
```

#### readUIntBE

readUIntBE(offset: number, byteLength: number): number

从指定的offset处的buf读取byteLength个字节，并将结果解释为支持最高48位精度的无符号大端序整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber是偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。byteLengthnumber是要读取的字节数。读取的字节数。取值范围：1 <= byteLength <= 6。

**返回值：**

类型说明number读取出的内容。当offset为小数时，返回undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntBE(0, 6).toString(16));
// 输出结果：1234567890ab
```

#### readUIntLE

readUIntLE(offset: number, byteLength: number): number

从指定的offset处的buf读取byteLength个字节，并将结果解释为支持最高48位精度的无符号小端序整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明offsetnumber是偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。byteLengthnumber是读取的字节数。取值范围：1 <= byteLength <= 6。

**返回值：**

类型说明number读取出的内容。当offset为小数时，返回undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntLE(0, 6).toString(16));
// 输出结果：ab9078563412
```

#### subarray

subarray(start?: number, end?: number): FastBuffer

截取当前对象指定位置的数据并返回。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明startnumber否截取开始位置。默认值：0。endnumber否截取结束位置（不包含结束位置）。默认值：当前对象的字节长度。取值范围：start <= end <= this.length

**返回值：**

类型说明FastBuffer返回新的FastBuffer对象。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.allocUninitializedFromPool(26);

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
const buf2 = buf1.subarray(0, 3);
console.info(buf2.toString('ascii', 0, buf2.length));
// 输出结果: abc
```

#### swap16

swap16(): FastBuffer

将当前对象转换为无符号的16位整数数组，并交换字节顺序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明FastBuffer交换之后的FastBuffer对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200009The fastbuffer size must be a multiple of 16-bits.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// 输出结果：0102030405060708
buf1.swap16();
console.info(buf1.toString('hex'));
// 输出结果：0201040306050807
```

#### swap32

swap32(): FastBuffer

将当前对象转换为无符号的32位整数数组，并交换字节顺序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明FastBuffer交换之后的FastBuffer对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200009The fastbuffer size must be a multiple of 32-bits.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// 输出结果：0102030405060708
buf1.swap32();
console.info(buf1.toString('hex'));
// 输出结果：0403020108070605
```

#### swap64

swap64(): FastBuffer

将当前对象转换为无符号的64位整数数组，并交换字节顺序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明FastBuffer交换之后的FastBuffer对象。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200009The fastbuffer size must be a multiple of 64-bits.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// 输出结果：0102030405060708
buf1.swap64();
console.info(buf1.toString('hex'));
// 输出结果：0807060504030201
```

#### toJSON

toJSON(): Object

将Buffer转为JSON并返回。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明ObjectJSON对象。

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
let obj = buf1.toJSON();
console.info(JSON.stringify(obj));
// 输出结果: {"type":"FastBuffer","data":[1,2,3,4,5]}
```

#### toString

toString(encoding?: string, start?: number, end?: number): string

将当前对象中指定位置的数据转成指定编码格式的字符串并返回。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否字符编码格式。默认值：'utf8'。startnumber否开始位置。默认值：0。endnumber否结束位置。默认值：Buffer.length。

**返回值：**

类型说明string字符串。当start >= this.length或start > end时返回空字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.allocUninitializedFromPool(26);
for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
console.info(buf1.toString('utf-8'));
// 输出结果: abcdefghijklmnopqrstuvwxyz
```

#### write

write(str: string, offset?: number, length?: number, encoding?: string): number

在FastBuffer对象的offset偏移处写入指定编码的字符串，写入的字节长度为length。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明strstring是要写入Buffer的字符串。offsetnumber否偏移量。默认值：0。lengthnumber否最大字节长度。默认值：(this.length - offset)。encodingstring否字符编码。默认值：'utf8'。

**返回值：**

类型说明number写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001Range error. Possible causes: The value of the parameter is not within the specified range.10200068The underlying ArrayBuffer is null or detach.

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.alloc(256);
let len = buf.write('\u00bd + \u00bc = \u00be', 0);
console.info(`${len} bytes: ${buf.toString('utf-8', 0, len)}`);
// 输出结果: 12 bytes: ½ + ¼ = ¾

let buffer1 = fastbuffer.alloc(10);
let length = buffer1.write('abcd', 8);
console.info("length = " + length);
// 输出结果：length = 2
```

#### writeBigInt64BE

writeBigInt64BE(value: bigint, offset?: number): number

在FastBuffer对象的offset偏移处写入有符号的大端序64位BigInt型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuebigint是写入Buffer的数据。取值范围：-INT64_MAX <= value <= INT64_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64BE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// 输出结果：result = 8
```

#### writeBigInt64LE

writeBigInt64LE(value: bigint, offset?: number): number

在FastBuffer对象的offset偏移处写入有符号的小端序64位BigInt型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuebigint是写入Buffer的数据。取值范围：-INT64_MAX <= value <= INT64_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64LE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// 输出结果：result = 8
```

#### writeBigUInt64BE

writeBigUInt64BE(value: bigint, offset?: number): number

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

在FastBuffer对象的offset偏移处写入无符号的大端序64位BigUInt型数据。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuebigint是写入Buffer的数据。取值范围：0 <= value <= UINT64_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// 输出结果：result = 8
```

#### writeBigUInt64LE

writeBigUInt64LE(value: bigint, offset?: number): number

在FastBuffer对象的offset偏移处写入无符号的小端序64位BigUInt型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuebigint是写入Buffer的数据。取值范围：0 <= value <= UINT64_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64LE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// 输出结果：result = 8
```

#### writeDoubleBE

writeDoubleBE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的64位双浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-DOUBLE_MAX <= value <= DOUBLE_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleBE(123.456, 0);
console.info("result = " + result);
// 输出结果：result = 8
```

#### writeDoubleLE

writeDoubleLE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的64位双浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-DOUBLE_MAX <= value <= DOUBLE_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleLE(123.456, 0);
console.info("result = " + result);
// 输出结果：result = 8
```

#### writeFloatBE

writeFloatBE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的32位浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-FLOAT_MAX <= value <= FLOAT_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeFloatBE(3.1415, 0);
console.info("result = " + result);
// 输出结果：result = 4
```

#### writeFloatLE

writeFloatLE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的32位浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-FLOAT_MAX <= value <= FLOAT_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeFloatLE(3.1415, 0);
console.info("result = " + result);
// 输出结果：result = 4
```

#### writeInt8

writeInt8(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入8位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-INT8_MAX <= value <= INT8_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 1。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(2);
let result = buf.writeInt8(2, 0);
console.info("result = " + result);
// 输出结果：result = 1
let result1 = buf.writeInt8(-2, 1);
console.info("result1 = " + result1);
// 输出结果：result1 = 2
```

#### writeInt16BE

writeInt16BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的16位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-INT16_MAX <= value <= INT16_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 2。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(2);
let result = buf.writeInt16BE(0x0102, 0);
console.info("result = " + result);
// 输出结果：result = 2
```

#### writeInt16LE

writeInt16LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的16位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-INT16_MAX <= value <= INT16_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 2。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(2);
let result = buf.writeInt16LE(0x0304, 0);
console.info("result = " + result);
// 输出结果：result = 2
```

#### writeInt32BE

writeInt32BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的32位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-INT32_MAX <= value <= INT32_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeInt32BE(0x01020304, 0);
console.info("result = " + result);
// 输出结果：result = 4
```

#### writeInt32LE

writeInt32LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的32位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：-INT32_MAX <= value <= INT32_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeInt32LE(0x05060708, 0);
console.info("result = " + result);
// 输出结果：result = 4
```

#### writeIntBE

writeIntBE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入大端序的有符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围取决于byteLength。offsetnumber是偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。byteLengthnumber是要写入的字节数。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
```

#### writeIntLE

writeIntLE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入小端序的有符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围取决于byteLength。offsetnumber是偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。byteLengthnumber是要写入的字节数。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
```

#### writeUInt8

writeUInt8(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入8位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：0 <= value <= UINT8_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 1。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt8(0x3, 0);
console.info("result = " + result);
// 输出结果：result = 1
let result1 = buf.writeUInt8(0x4, 1);
console.info("result1 = " + result1);
// 输出结果：result1 = 2
let result2 = buf.writeUInt8(0x23, 2);
console.info("result2 = " + result2);
// 输出结果：result2 = 3
let result3 = buf.writeUInt8(0x42, 3);
console.info("result3 = " + result3);
// 输出结果：result3 = 4
```

#### writeUInt16BE

writeUInt16BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的16位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：0 <= value <= UINT16_MAX。offsetnumber否偏移量。默认值为0。取值范围：0 <= offset <= this.length - 2。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt16BE(0xdead, 0);
console.info("result = " + result);
// 输出结果：result = 2
let result1 = buf.writeUInt16BE(0xbeef, 2);
console.info("result1 = " + result1);
// 输出结果：result1 = 4
```

#### writeUInt16LE

writeUInt16LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的16位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：0 <= value <= UINT16_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 2。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt16LE(0xdead, 0);
console.info("result = " + result);
// 输出结果：result = 2
let result1 = buf.writeUInt16LE(0xbeef, 2);
console.info("result1 = " + result1);
// 输出结果：result1 = 4
```

#### writeUInt32BE

writeUInt32BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的32位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围：0 <= value <= UINT32_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32BE(0xfeedface, 0);
console.info("result = " + result);
// 输出结果：result = 4
```

#### writeUInt32LE

writeUInt32LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的32位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入FastBuffer对象的数据。取值范围：0 <= value <= UINT32_MAX。offsetnumber否偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32LE(0xfeedface, 0);
console.info("result = " + result);
// 输出结果：result = 4
```

#### writeUIntBE

writeUIntBE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入大端序的无符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围取决于byteLength。offsetnumber是偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。byteLengthnumber是要写入的字节数。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeUIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
```

#### writeUIntLE

writeUIntLE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入小端序的无符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valuenumber是写入Buffer的数据。取值范围取决于byteLength。offsetnumber是偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。byteLengthnumber是要写入的字节数。

**返回值：**

类型说明number偏移量offset加上写入的字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200001The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]

**示例：**

```ets
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeUIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
```