# @system.file (文件存储)

- 模块维护策略：

  - 对于Lite Wearable设备类型，该模块长期维护，正常使用。
  - 对于支持该模块的其他设备类型，该模块从API Version 10开始不再维护，推荐使用新接口[@ohos.file.fs](../ohos/@ohos.file.fs (文件管理).md)。

- 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import file from '@system.file';
```

#### file.move

move(Object): void

将指定文件移动到其他指定位置。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.moveFile](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsmovefile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明srcUristring是要移动的文件的uri。字符串最大长度为128，且不能包含“"*+,:;<=>?[]|\x7F”等特殊符号。dstUristring是文件要移动到的位置的uri。字符串最大长度为128，且不能包含“"*+,:;<=>?[]|\x7F”等特殊符号。successFunction否接口调用成功的回调函数，返回文件要移动到的位置的uri。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O错误。301文件或目录不存在。

**示例：**

```ets
export default {
  move() {
    file.move({
      srcUri: 'internal://app/myfiles1',
      dstUri: 'internal://app/myfiles2',
      success: function(uri) {
        console.log('call success callback success');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.copy

copy(Object): void

将指定文件拷贝并存储到指定位置。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.copyFile](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fscopyfile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明srcUristring是要拷贝的文件的uri。dstUristring是

文件要拷贝到的位置的uri。

不支持用应用资源路径或tmp类型的uri。

successFunction否接口调用成功的回调函数，返回文件要拷贝到的位置的uri。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O错误。301文件或目录不存在。

**示例：**

```ets
export default {
  copy() {
    file.copy({
      srcUri: 'internal://app/file.txt',
      dstUri: 'internal://app/file_copy.txt',
      success: function(uri) {
        console.log('call success callback success');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.list

list(Object): void

获取指定路径下全部文件的列表。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.listFile](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fslistfile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是目录uri。字符串最大长度为128，且不能包含“"*+,:;<=>?[]|\x7F”等特殊符号。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

success返回值：

参数名类型说明fileListArray<FileInfo>

获取的文件列表，其中每个文件的信息的格式为：

{

uri:'file1',

lastModifiedTime:1589965924479,

length:10240,

type: 'file'

}

**表1** FileInfo

参数名类型说明uristring文件的 uri。lastModifiedTimenumber文件上一次保存时的时间戳，显示从1970/01/01 00:00:00 GMT到当前时间的毫秒数。lengthnumber文件的大小，单位为字节。typestring

文件的类型，可选值为：

- dir：目录；

- file：文件。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O错误。301文件或目录不存在。

**示例：**

```ets
export default {
  list() {
    file.list({
      uri: 'internal://app/pic',
      success: function(data) {
        console.log(JSON.stringify(data.fileList));
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.get

get(Object): void

获取指定本地文件的信息。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.stat](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsstat)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是文件的uri。recursiveboolean否是否进行递归获取子目录文件列表，true为进行该操作，缺省为false。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

success返回值：

参数名类型说明uristring文件的uri。lengthnumber文件字节长。lastModifiedTimenumber文件保存时的时间戳，从1970/01/01 00:00:00到当前时间的毫秒数。typestring

文件类型，可选值为：

- dir：目录；

- file：文件。

subFilesArray文件列表。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O错误。301文件或目录不存在。

**示例：**

```ets
export default {
  get() {
    file.get({
      uri: 'internal://app/file',
      success: function(data) {
        console.log(data.uri);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.delete

delete(Object): void

删除本地文件。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.unlink](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsunlink)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是删除文件的uri，不能是应用资源路径。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202参数错误。300I/O错误。301文件或目录不存在。

**示例：**

```ets
export default {
  delete() {
    file.delete({
      uri: 'internal://app/my_file',
      success: function() {
        console.log('call delete success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.writeText

writeText(Object): void

写文本内容到指定文件。仅支持文本文档读写。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.write](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fswrite)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是本地文件uri，如果文件不存在会创建文件。textstring是写入的字符串。encodingstring否编码格式，默认为UTF-8。appendboolean否是否追加模式，默认为false。true为追加，false为不追加。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202参数错误。300I/O错误。

**示例：**

```ets
export default {
  writeText() {
    file.writeText({
      uri: 'internal://app/test.txt',
      text: 'Text that just for test.',
      success: function() {
        console.log('call writeText success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.writeArrayBuffer

writeArrayBuffer(Object): void

写Buffer内容到指定文件。仅支持文本文档读写。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.write](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fswrite)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是本地文件uri，如果文件不存在会创建文件。bufferUint8Array是写入的Buffer。positionnumber否文件开始写入数据的位置的偏移量，默认为0。appendboolean否是否追加模式，默认为false。当设置为true时，position参数无效。true为追加，false为不追加。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O错误。

**示例：**

```ets
export default {
  writeArrayBuffer() {
    file.writeArrayBuffer({
      uri: 'internal://app/test',
      buffer: new Uint8Array(8), //buffer为Uint8Array类型
      success: function() {
        console.log('call writeArrayBuffer success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.readText

readText(Object): void

从指定文件中读取文本内容。仅支持文本文档读写。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.readText](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsreadtext)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是本地文件uri。encodingstring否编码格式，缺省为UTF-8。positionnumber否读取的起始位置，默认值为文件的起始位置。lengthnumber否读取的长度，默认值为4096。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

success返回值：

参数名类型说明textstring读取到的文本内容。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O错误。301文件或目录不存在。302要读取的文件内容超过4KB。

**示例：**

```ets
export default {
  readText() {
    file.readText({
      uri: 'internal://app/text.txt',
      success: function(data) {
        console.log('call readText success: ' + data.text);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.readArrayBuffer

readArrayBuffer(Object): void

从指定文件中读取Buffer内容。仅支持文本文档读写。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.read](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsread)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是本地文件uri。positionnumber否读取的起始位置，缺省为文件的起始位置。lengthnumber否需要读取的长度，缺省则读取到文件结尾。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

success返回值：

参数名类型说明bufferUint8Array读取到的文件内容。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O错误。301文件或目录不存在。

**示例：**

```ets
export default {
  readArrayBuffer() {
    file.readArrayBuffer({
      uri: 'internal://app/test',
      position: 10,
      length: 200,
      success: function(data) {
        console.log('call readArrayBuffer success: ' + data.buffer);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.access

access(Object): void

判断指定文件或目录是否存在。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.access](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsaccess)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是目录或文件uri。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O 错误。301文件或目录不存在。

**示例：**

```ets
export default {
  access() {
    file.access({
      uri: 'internal://app/test',
      success: function() {
        console.log('call access success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.mkdir

mkdir(Object): void

创建指定目录。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.mkdir](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsmkdir)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是目录的uri路径。recursiveboolean否是否递归创建该目录的上级目录，缺省为false。true为递归创建，false是不递归创建。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O 错误。

**示例：**

```ets
export default {
  mkdir() {
    file.mkdir({
      uri: 'internal://app/test_directory',
      success: function() {
        console.log('call mkdir success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.rmdir

rmdir(Object): void

删除指定目录。

除Lite Wearable外，从API version 10开始废弃，请使用[fs.rmdir](../ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsrmdir)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

参数名类型必填说明uristring是目录的uri路径。recursiveboolean否是否递归删除子文件和子目录，缺省为false。true为递归删除，false为不递归删除。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回错误代码：

错误码说明202出现参数错误。300出现I/O 错误。301文件或目录不存在。

**示例：**

```ets
export default {
  rmdir() {
    file.rmdir({
      uri: 'internal://app/test_directory',
      success: function() {
        console.log('call rmdir success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```