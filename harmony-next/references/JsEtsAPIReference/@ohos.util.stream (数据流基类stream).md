# @ohos.util.stream (数据流基类stream)

本模块提供基本流类型的处理能力，支持数据分块读取或写入，避免一次性加载整个数据到内存。

包括可写流（[Writable](#ZH-CN_TOPIC_0000002497444782__writable)）、可读流（[Readable](#ZH-CN_TOPIC_0000002497444782__readable)）、双工流（[Duplex](#ZH-CN_TOPIC_0000002497444782__duplex)）和转换流（[Transform](#ZH-CN_TOPIC_0000002497444782__transform)）。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { stream  } from '@kit.ArkTS';
```

#### Writable

可写入数据的流。可写流允许将数据写入到目标中，这个目标可以是文件、HTTP 响应、标准输出、另一个流等。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明writableObjectModeboolean是否指定可写流是否以对象模式工作。true表示流被配置为对象模式，false表示流处于非对象模式。当前版本只支持原始数据（字符串和Uint8Array），返回值为false。writableHighWatermarknumber是否定义可写流缓冲区数据量的水位线大小。当前版本不支持开发者自定义修改水位线大小。调用[write()](#ZH-CN_TOPIC_0000002497444782__write)写入数据后，若缓冲区数据量达到该值，[write()](#ZH-CN_TOPIC_0000002497444782__write)会返回false。默认值为16 * 1024字节。writableboolean是否表示可写流是否处于可写状态。true表示流当前是可写的，false表示流当前不再接受写入操作。writableLengthnumber是否表示可写流缓冲区中待写入的字节数。writableCorkednumber是否表示可写流cork状态计数。值大于0时，可写流处于强制写入缓冲区状态；值为0时，该状态解除。使用[cork()](#ZH-CN_TOPIC_0000002497444782__cork)方法时计数加一，使用[uncork()](#ZH-CN_TOPIC_0000002497444782__uncork)方法时计数减一，使用[end()](#ZH-CN_TOPIC_0000002497444782__end)方法时计数清零。writableEndedboolean是否表示当前可写流的[end()](#ZH-CN_TOPIC_0000002497444782__end)是否被调用，该状态不代表数据已经全部写入。true表示[end()](#ZH-CN_TOPIC_0000002497444782__end)已被调用，false表示[end()](#ZH-CN_TOPIC_0000002497444782__end)未被调用。writableFinishedboolean是否表示当前可写流是否处于写入完成状态。true表示当前流已处于写入完成状态，false表示当前流的写入操作可能还在进行中。

#### constructor

constructor()

Writable的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let writableStream = new stream.Writable();
```

#### write

write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean

将数据写入流的缓冲区中。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array否需要写入的数据。当前版本不支持null、undefined和空字符串。encodingstring否字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。callbackFunction否回调函数。默认不调用。

**返回值：**

类型说明boolean可写流的缓冲区中是否还有空间。true表示缓冲区还有空间，false表示流的内部缓冲区数据量已达到设定水位线，不建议继续写入，如果连续调用写入函数，数据仍会被添加到缓冲区中，直到内存溢出为止。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200035The doWrite method has not been implemented.10200036The stream has been ended.10200037The callback is invoked multiple times consecutively.

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Writable chunk is", chunk); // Writable chunk is test
    callback();
  }
}

let writableStream = new TestWritable();
writableStream.write('test', 'utf8');
```

#### end

end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable

结束可写流的写入操作。如果属性writableCorked的值大于0，会置零该值并输出缓冲区剩余数据。如果传入chunk参数，则根据实际运行情况，通过write或者doWrite将其作为最后一块数据写入。其中通过doWrite写入时，encoding参数的合法性检查依赖doWrite。end单独使用（不使用write）并传入chunk参数的情况下，必然通过doWrite写入。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array否需要写入的数据。默认为undefined。encodingstring否字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。callbackFunction否回调函数。

**返回值：**

类型说明[Writable](#ZH-CN_TOPIC_0000002497444782__writable)返回当前可写流对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200035The doWrite method has not been implemented.

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Writable chunk is", chunk);
    callback();
  }
  // Writable chunk is test
  // Writable chunk is finish
}

let writableStream = new TestWritable();
writableStream.write('test', 'utf8');
writableStream.end('finish', 'utf8', () => {
  console.info("Writable is end"); // Writable is end
});
```

#### setDefaultEncoding

setDefaultEncoding(encoding?: string): boolean

设置可写流的默认字符编码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否设置默认字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。

**返回值：**

类型说明boolean返回是否设置成功。true表示成功，false表示失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
let result = writableStream.setDefaultEncoding('utf8');
console.info("Writable is result", result); // Writable is result true
```

#### cork

cork(): boolean

使后续写入的数据强制写入缓冲区，优化连续写入操作的性能。使用后属性writableCorked的值会加一。建议和[uncork()](#ZH-CN_TOPIC_0000002497444782__uncork)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回设置cork状态是否成功。true表示成功，false表示失败。

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
let result = writableStream.cork();
console.info("Writable cork result", result); // Writable cork result true
```

#### uncork

uncork(): boolean

解除cork状态，解除后刷新缓冲区数据并写入目标位置。使用后属性writableCorked的值会减一，如果该值降为0，则解除cork状态，否则流依然处于cork状态。建议和[cork()](#ZH-CN_TOPIC_0000002497444782__cork)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回解除cork状态是否成功。true表示成功，false表示失败。

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
writableStream.cork();
writableStream.write('data1', 'utf8');
writableStream.write('data2', 'utf8');
writableStream.uncork();
writableStream.end();
writableStream.on('finish', () => {
  console.info("all Data is End"); // all Data is End
});
```

#### on

on(event: string, callback: Callback<emitter.EventData>): void

注册事件处理函数来监听可写流上的不同事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明eventstring是

事件回调类型，支持的事件包括：'close' | 'drain' |'error' | 'finish' 。

- 'close'：完成[end()](#ZH-CN_TOPIC_0000002497444782__end)调用，结束写入操作，触发该事件。

- 'drain'：在可写流缓冲区中数据清空时触发该事件。

- 'error'：在可写流发生异常时触发该事件。

- 'finish'：在数据缓冲区全部写入到目标后触发该事件。

callbackCallback<[emitter.EventData](@ohos.events.emitter (Emitter).md#ZH-CN_TOPIC_0000002529285503__eventdata)>是回调函数，返回事件传输的数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback(new Error());
  }
}

let callbackCalled = false;
let writable = new TestWritable();
writable.on('error', () => {
  console.info("Writable event test", callbackCalled.toString()); // Writable event test false
});
writable.write('hello', 'utf8', () => {
});
```

#### off

off(event: string, callback?: Callback<emitter.EventData>): void

移除通过[on](#ZH-CN_TOPIC_0000002497444782__on)注册的事件处理函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明eventstring是

事件回调类型，支持的事件包括：'close' | 'drain' |'error' | 'finish' 。

- 'close'：完成[end()](#ZH-CN_TOPIC_0000002497444782__end)调用，结束写入操作，触发该事件。

- 'drain'：在可写流缓冲区中数据清空时触发该事件。

- 'error'：在可写流发生异常时触发该事件。

- 'finish'：在数据缓冲区全部写入到目标后触发该事件。

callbackCallback<[emitter.EventData](@ohos.events.emitter (Emitter).md#ZH-CN_TOPIC_0000002529285503__eventdata)>否回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
 }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
let testListenerCalled = false;
let testListener = () => {
  testListenerCalled = true;
};
writableStream.on('finish', testListener);
writableStream.off('finish');
writableStream.write('test');
writableStream.end();
setTimeout(() => {
  console.info("Writable off test", testListenerCalled.toString()); // Writable off test false
}, 0);
```

#### doInitialize

doInitialize(callback: Function): void

用户实现这个函数。该函数在可写流初始化阶段被调用，无需用户调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class MyWritable extends stream.Writable {
  doInitialize(callback: Function) {
    super.doInitialize(callback);
    console.info("Writable doInitialize"); // Writable doInitialize
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    super.doWrite(chunk, encoding, callback);
  }
}

new MyWritable();
```

#### doWrite

doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void

提供一个数据写出接口供开发者实现，该接口函数会在数据被成功写出时自动调用，无需手动触发。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array是要写出的数据。encodingstring是字符编码类型。当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Writable chunk is", chunk); // Writable chunk is data
    callback();
  }
}

let writableStream = new TestWritable();
writableStream.write('data', 'utf8');
```

#### doWritev

doWritev(chunks: string[] | Uint8Array[], callback: Function): void

提供一个数据批量写出接口供使用者实现，该接口函数会在数据被成功写出时自动调用，无需用户手动触发。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunksstring[] | Uint8Array[]是被批量写出的数据数组。callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWritev(chunks: string[] | Uint8Array[], callback: Function) {
    console.info("Writable chunk", chunks);
    callback();
  }
  // Writable chunk data1
  // Writable chunk data2
}

let writableStream = new TestWritable();
writableStream.write('data1', 'utf8');
writableStream.write('data2', 'utf8');
writableStream.uncork();
writableStream.end();
```

#### ReadableOptions

Readable构造函数的选项信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明encodingstring否是

指定数据的编码格式，如果传入非法字符串，将会在Readable构造函数中抛出异常。

- 支持格式：utf-8、UTF-8、GBK、GB2312、gb2312、GB18030、gb18030、ibm866、iso-8859-2、iso-8859-3、iso-8859-4、iso-8859-5、iso-8859-6、iso-8859-7、iso-8859-8、iso-8859-8-i、iso-8859-10、iso-8859-13、iso-8859-14、iso-8859-15、koi8-r、koi8-u、macintosh、windows-874、windows-1250、windows-1251、windows-1252、windows-1253、windows-1254、windows-1255、windows-1256、windows-1257、windows-1258、gbk、big5、euc-jp、iso-2022-jp、shift_jis、euc-kr、x-mac-cyrillic、utf-16be、utf-16le。

- 默认值是：'utf-8'。

#### Readable

表示可读取数据的流。可读流用于从数据源（如文件、网络套接字等）读取数据。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明readableObjectModeboolean是否用于指定可读流是否以对象模式工作。true表示流被配置为对象模式，false表示流处于非对象模式。当前版本只支持原始数据（字符串和Uint8Array），返回值为false。readableboolean是否表示可读流是否处于可读状态。true表示流处于可读状态，false表示流中没有更多数据可供读取。readableHighWatermarknumber是否定义缓冲区的最大数据量。默认值为16 * 1024字节。readableFlowingboolean | null是否表示当前可读流的状态。true表示流处于流动模式，false表示流处于非流动模式。默认值是true。readableLengthnumber是否表示缓冲区的当前字节数。readableEncodingstring | null是否被解码成字符串时所使用的字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。readableEndedboolean是否表示当前可读流是否已经结束。true表示流已经没有更多数据可读且已结束，false表示流尚未结束，仍有数据可读或等待读取。

#### constructor

constructor()

Readable的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let readableStream = new stream.Readable();
```

#### constructor

constructor(options: ReadableOptions)

Readable的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明options[ReadableOptions](#ZH-CN_TOPIC_0000002497444782__readableoptions)是Readable构造函数的选项信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let option : stream.ReadableOptions = {
  encoding : 'utf-8'
};
let readableStream = new stream.Readable(option);
```

#### read

read(size?: number): string | null

从可读流缓冲区读取数据，并返回读取到的数据，如果未读取到数据，则返回null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明sizenumber否读取数据的字节数。默认为undefined。

**返回值：**

类型说明string | null可读流读取出的数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200038The doRead method has not been implemented.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.push('test');
readableStream.pause();
let dataChunk = readableStream.read();
console.info('Readable data is', dataChunk); // Readable data is test
```

#### resume

resume(): Readable

将流的读取模式从暂停切换到流动模式，可用接口isPaused判断是否已切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明[Readable](#ZH-CN_TOPIC_0000002497444782__readable)当前可读流本身。

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.resume();
console.info("Readable test resume", !readableStream.isPaused()); // 切换流动模式成功时，此处日志将打印"Readable test resume true"
```

#### pause

pause(): Readable

将流的读取模式从流动切换到暂停模式，可用接口isPaused判断是否已切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明[Readable](#ZH-CN_TOPIC_0000002497444782__readable)当前可读流本身。

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.pause();
console.info("Readable test pause", readableStream.isPaused()); // Readable test pause true
```

#### setEncoding

setEncoding(encoding?: string): boolean

设置可读流的字符编码。

当缓冲区有数据时，不允许设置字符编码，返回值为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否需要设置的字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。

**返回值：**

类型说明boolean返回是否设置成功。true表示设置成功，false表示设置失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
let result = readableStream.setEncoding('utf8');
console.info("Readable result", result); // Readable result true
```

#### isPaused

isPaused(): boolean

检查流是否处于暂停模式，调用[pause()](#ZH-CN_TOPIC_0000002497444782__pause)后，返回值为true；调用[resume()](#ZH-CN_TOPIC_0000002497444782__resume)后，返回值为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回流是否处于暂停模式。true表示流处于暂停模式，false表示流未处于暂停模式。

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused false
readableStream.pause();
console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused true
```

#### pipe

pipe(destination: Writable, options?: Object): Writable

将一个可读流与一个可写流连接起来，实现数据的自动传输。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明destination[Writable](#ZH-CN_TOPIC_0000002497444782__writable)是接收数据的可写流。optionsObject否预留字段，暂不支持使用。

**返回值：**

类型说明[Writable](#ZH-CN_TOPIC_0000002497444782__writable)返回当前可写流对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    this.push('test');
    this.push(null);
  }
}

class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Readable test pipe", chunk); // Readable test pipe test
    callback();
  }
}

let readable = new TestReadable();
let writable = new TestWritable();
readable.pipe(writable);
```

#### unpipe

unpipe(destination?: Writable): Readable

从可写流中移除所有或指定的已连接的可读流。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明destination[Writable](#ZH-CN_TOPIC_0000002497444782__writable)否从当前可写流中移除指定的这个可读流。默认为undefined。

**返回值：**

类型说明[Readable](#ZH-CN_TOPIC_0000002497444782__readable)返回当前可读流对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    this.push('test');
    this.push(null);
  }
}

class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let readable = new TestReadable();
let writable = new TestWritable();
readable.pipe(writable);
readable.unpipe(writable);
readable.on('data', () => {
  console.info("Readable test unpipe data event triggered");
});
// unpipe成功断开连接之后，data事件将不会触发，不会打印"Readable test unpipe data event triggered"
```

#### on

on(event: string, callback: Callback<emitter.EventData>): void

注册事件处理函数来监听可读流上的不同事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明eventstring是

事件回调类型，支持的事件包括：'close' | 'data' |'end' | 'error'|'readable'|'pause'|'resume' 。

- 'close'：完成[push()](#ZH-CN_TOPIC_0000002497444782__push)调用，传入null值，触发该事件。

- 'data'：当流传递给消费者一个数据块时触发该事件。

- 'end'：完成[push()](#ZH-CN_TOPIC_0000002497444782__push)调用，传入null值，触发该事件。

- 'error'：流发生异常时触发。

- 'readable'：当有可从流中读取的数据时触发该事件。

- 'pause'：完成[pause()](#ZH-CN_TOPIC_0000002497444782__pause)调用，触发该事件。

- 'resume'：完成[resume()](#ZH-CN_TOPIC_0000002497444782__resume)调用，触发该事件。

callbackCallback<[emitter.EventData](@ohos.events.emitter (Emitter).md#ZH-CN_TOPIC_0000002529285503__eventdata)>是回调函数，返回事件数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    throw new Error('Simulated error');
  }
}

let readable = new TestReadable();
readable.push('test');
readable.on('error', () => {
  console.info("error event called"); // error event called
});
```

#### off

off(event: string, callback?: Callback<emitter.EventData>): void

移除通过[on](#ZH-CN_TOPIC_0000002497444782__on)注册的事件处理函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明eventstring是

事件回调类型，支持的事件包括：'close' | 'data' |'end' | 'error'|'readable'|'pause'|'resume' 。

- 'close'：完成[push()](#ZH-CN_TOPIC_0000002497444782__push)调用，传入null值，触发该事件。

- 'data'：当流传递给消费者一个数据块时触发该事件。

- 'end'：完成[push()](#ZH-CN_TOPIC_0000002497444782__push)调用，传入null值，触发该事件。

- 'error'：流发生异常时触发。

- 'readable'：当有可从流中读取的数据时触发该事件。

- 'pause'：完成[pause()](#ZH-CN_TOPIC_0000002497444782__pause)调用，触发该事件。

- 'resume'：完成[resume()](#ZH-CN_TOPIC_0000002497444782__resume)调用，触发该事件。

callbackCallback<[emitter.EventData](@ohos.events.emitter (Emitter).md#ZH-CN_TOPIC_0000002529285503__eventdata)>否回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readable = new TestReadable();

function read() {
  console.info("read() called");
}

readable.setEncoding('utf8');
readable.on('readable', read);
readable.off('readable');
readable.push('test');
// off注销对readable事件的监听后，read函数不会被调用，"read() called"也不会被打印
```

#### doInitialize

doInitialize(callback: Function): void

使用者实现这个函数，这个函数在可读流第一次使用[on](#ZH-CN_TOPIC_0000002497444782__on-1)监听时被调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class MyReadable extends stream.Readable {
  doInitialize(callback: Function) {
    super.doInitialize(callback);
    console.info("Readable doInitialize"); // Readable doInitialize
}

  doRead(size: number) {
  }
}

let myReadable = new MyReadable();
myReadable.on('data', () => {
});
```

#### doRead

doRead(size: number): void

数据读取接口，需要在子类中被实现。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明sizenumber是读取数据的字节数。 取值范围：0 <= size <= Number.MAX_VALUE。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    console.info("doRead called"); // doRead called
  }
}

let readable = new TestReadable();
readable.on('data', () => {
});
```

#### push

push(chunk: Uint8Array | string | null, encoding?: string): boolean

将数据推送到可读流缓冲区中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkUint8Array | string | null是读取的数据。encodingstring否数据的编码格式。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。

**返回值：**

类型说明boolean可读流的缓冲区中是否还有空间。true表示缓冲区还有空间，false表示流的内部缓冲区已满。输入null时，固定返回false表示推送结束，没有数据块可推送。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readable = new TestReadable();
let testData = 'Hello world';
readable.push(testData);
console.info("Readable push test", readable.readableLength); // Readable push test 11
```

#### Duplex

双工流是一个同时支持可读和可写能力的流。双工流允许数据在两个方向上进行传输，既可以读取数据，又可以写入数据。

Duplex类继承[Readable](#ZH-CN_TOPIC_0000002497444782__readable)，支持Readable中所有的方法。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明writableObjectModeboolean是否用于指定双工流的写模式是否以对象模式工作。true表示流的写模式被配置为对象模式，false表示流的写模式处于非对象模式。当前版本只支持原始数据（字符串和Uint8Array），返回值为false。writableHighWatermarknumber是否定义双工流的写模式下缓冲区数据量的水位线大小。当前版本不支持开发者自定义修改设置水位线大小。调用[write()](#ZH-CN_TOPIC_0000002497444782__write-1)写入后，若缓冲区数据量达到该值，[write()](#ZH-CN_TOPIC_0000002497444782__write-1)会返回false。默认值为16 * 1024字节。writableboolean是否表示双工流是否处于可写状态。true表示当前流是可写的，false表示流当前不再接受写入操作。writableLengthnumber是否表示双工流缓冲区中待写入的字节数。writableCorkednumber是否表示双工流cork状态计数。值大于0时，双工流处于强制写入缓冲区状态，值为0时，该状态解除。使用[cork()](#ZH-CN_TOPIC_0000002497444782__cork-1)方法时计数加一，使用[uncork()](#ZH-CN_TOPIC_0000002497444782__uncork-1)方法时计数减一，使用[end()](#ZH-CN_TOPIC_0000002497444782__end-1)方法时计数清零。writableEndedboolean是否表示当前双工流的[end()](#ZH-CN_TOPIC_0000002497444782__end-1)是否被调用，该状态不代表数据已经全部写入。true表示[end()](#ZH-CN_TOPIC_0000002497444782__end-1)已被调用，false表示[end()](#ZH-CN_TOPIC_0000002497444782__end-1)未被调用。writableFinishedboolean是否表示当前双工流是否处于写入完成状态。true表示当前流已处于写入完成状态，false表示当前流的写入操作可能还在进行中。

#### constructor

constructor()

Duplex的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let duplex = new stream.Duplex();
```

#### write

write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean

将数据写入流的缓冲区中。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array否需要写入的数据。当前版本不支持null、undefined和空字符串。encodingstring否字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。callbackFunction否回调函数。默认不调用。

**返回值：**

类型说明boolean可写流的缓冲区中是否还有空间。true表示缓冲区还有空间，false表示流的内部缓冲区数据量已达到设定水位线，不建议继续写入。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200036The stream has been ended.10200037The callback is invoked multiple times consecutively.10200039The doTransform method has not been implemented for a class that inherits from Transform.

**示例：**

```ets
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("duplexStream chunk is", chunk); // duplexStream chunk is test
    callback();
  }
}

let duplexStream = new TestDuplex();
let result = duplexStream.write('test', 'utf8');
console.info("duplexStream result", result); // duplexStream result true
```

#### end

end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable

结束双工流的写入操作。如果属性writableCorked的值大于0，会置零该值并输出缓冲区剩余数据。如果传入chunk参数，则根据实际运行情况，通过write或者doWrite将其作为最后一块数据写入。其中通过doWrite写入时，encoding参数的合法性检查依赖doWrite。end单独使用（不使用write）并传入chunk参数的情况下，必然通过doWrite写入。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array否需要写入的数据。默认为undefined。encodingstring否字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。callbackFunction否回调函数。默认不调用。

**返回值：**

类型说明[Writable](#ZH-CN_TOPIC_0000002497444782__writable)返回可写流对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200039The doTransform method has not been implemented for a class that inherits from Transform.

**示例：**

```ets
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
  console.info("Duplex chunk is", chunk); // Duplex chunk is test
  callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.end('test', 'utf8', () => {
  console.info("Duplex is end"); // Duplex is end
});
```

#### setDefaultEncoding

setDefaultEncoding(encoding?: string): boolean

设置双工流的默认字符编码，确保在读取数据时正确解析字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明encodingstring否需要设置的默认字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。

**返回值：**

类型说明boolean返回是否设置成功。true表示设置成功，false表示设置失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let duplexStream = new TestDuplex();
let result = duplexStream.setDefaultEncoding('utf8');
console.info("duplexStream is result", result); // duplexStream is result true
```

#### cork

cork(): boolean

将写入的数据强制写入缓冲区暂存，用来优化连续写入操作的性能。使用后属性writableCorked的值会加一。建议和[uncork()](#ZH-CN_TOPIC_0000002497444782__uncork-1)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回设置cork状态是否成功。true表示设置成功，false表示设置失败。

**示例：**

```ets
let duplexStream = new stream.Duplex();
let result = duplexStream.cork();
console.info("duplexStream cork result", result); // duplexStream cork result true
```

#### uncork

uncork(): boolean

解除cork状态，解除后将缓冲区中的数据全部刷新，并将其写入目标位置。使用后属性writableCorked的值会减一，如果该值降为0，则解除cork状态，否则流依然处于cork状态。建议和[cork()](#ZH-CN_TOPIC_0000002497444782__cork-1)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回解除cork状态是否成功。true表示成功，false表示失败。

**示例：**

```ets
let dataWritten = '';
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    dataWritten += chunk;
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.cork();
duplexStream.write('a');
duplexStream.write('b');
duplexStream.uncork();
console.info("Duplex test uncork", dataWritten); // Duplex test uncork ab
```

#### doWrite

doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void

数据写出接口是一个由使用者实现的函数，在数据被写出时自动调用，而不需要用户手动调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring | Uint8Array是要写出的数据。encodingstring是字符编码类型。当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("duplexStream chunk is", chunk); // duplexStream chunk is data
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.write('data', 'utf8');
```

#### doWritev

doWritev(chunks: string[] | Uint8Array[], callback: Function): void

数据分批写出接口是一个由使用者实现的函数，在数据被写出时自动调用，而不需要用户手动调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunksstring[] | Uint8Array[]是被批量写出的数据数组。callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }

  doWritev(chunks: string[] | Uint8Array[], callback: Function) {
    console.info("duplexStream chunk", chunks[0]); // duplexStream chunk data1
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.cork();
duplexStream.write('data1', 'utf8');
duplexStream.write('data2', 'utf8');
duplexStream.uncork();
duplexStream.end();
```

#### Transform

转换流是一个特殊的双工流，支持可读和可写能力的流，可以对数据进行转换并输出结果。Transform类继承[Duplex](#ZH-CN_TOPIC_0000002497444782__duplex)，支持Duplex中所有的方法。

#### constructor

constructor()

Transform的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let transform = new stream.Transform();
```

#### doTransform

doTransform(chunk: string, encoding: string, callback: Function): void

对输入的数据块进行转换或处理，并通过回调函数通知操作完成。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明chunkstring是需要写入的数据。encodingstring是字符编码类型。当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestTransform extends stream.Transform {
  constructor() {
    super();
  }

  doTransform(chunk: string, encoding: string, callback: Function) {
    let stringChunk = chunk.toString().toUpperCase();
    console.info("Transform test doTransform", stringChunk); // Transform test doTransform HELLO
    this.push(stringChunk);
    callback();
  }
}

let tr = new TestTransform();
tr.write("hello");
```

#### doFlush

doFlush(callback: Function): void

该函数会在流结束时被调用，用于处理剩余的数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明callbackFunction是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
class TestTransform extends stream.Transform {
  constructor() {
    super();
  }

  doTransform(chunk: string, encoding: string, callback: Function) {
    callback();
  }

  doFlush(callback: Function) {
    callback(null, 'test');
  }
}

let transform = new TestTransform();
transform.end('my test');
transform.on('data', (data) => {
  console.info("data is", data.data); // data is test
});
```