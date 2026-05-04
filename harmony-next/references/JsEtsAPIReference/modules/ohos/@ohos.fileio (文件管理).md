# @ohos.fileio (文件管理)

该模块提供文件存储管理能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块从API version 9开始废弃，建议使用[@ohos.file.fs](@ohos.file.fs (文件管理).md)替代。

#### 导入模块

```ets
import fileio from '@ohos.fileio';
```

#### 使用说明

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```ets
 import UIAbility from '@ohos.app.ability.UIAbility';
 import window from '@ohos.window';

 export default class EntryAbility extends UIAbility {
   onWindowStageCreate(windowStage: window.WindowStage) {
     let context = this.context;
     let pathDir = context.filesDir;
   }
```

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：[应用上下文Context-获取应用文件路径](../../guides/应用上下文Context.md#获取应用文件路径)

#### fileio.stat

stat(path: string): Promise<Stat>

获取文件信息，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.stat](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__stat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Stat> | Promise对象。返回文件的具体信息。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "test.txt";
fileio.stat(filePath).then((stat: fileio.Stat) => {
  console.info("getFileInfo succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("getFileInfo failed with error:" + err);
});
```

#### fileio.stat

stat(path: string, callback: AsyncCallback<Stat>): void

获取文件信息，使用callback异步回调。


从API version 9开始废弃，请使用[fs.stat](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsstat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |
| callback | AsyncCallback<Stat> | 是 | 异步获取文件的信息之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
fileio.stat(pathDir, (err: BusinessError, stat: fileio.Stat) => {
  // example code in Stat
});
```

#### fileio.statSync

statSync(path: string): Stat

以同步方法获取文件的信息。


从API version 9开始废弃，请使用[fs.statSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsstatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stat | 表示文件的具体信息。 |

**示例：**

```ets
let stat = fileio.statSync(pathDir);
// example code in Stat
```

#### fileio.opendir

opendir(path: string): Promise<Dir>

打开文件目录，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Dir> | Promise对象。返回Dir对象。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + "/testDir";
fileio.opendir(dirPath).then((dir: fileio.Dir) => {
  console.info("opendir succeed");
}).catch((err: BusinessError) => {
  console.error("opendir failed with error:" + err);
});
```

#### fileio.opendir

opendir(path: string, callback: AsyncCallback<Dir>): void

打开文件目录，使用callback异步回调。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |
| callback | AsyncCallback<Dir> | 是 | 异步打开文件目录之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
fileio.opendir(pathDir, (err: BusinessError, dir: fileio.Dir) => {
  // example code in Dir struct
  // use read/readSync/close
});
```

#### fileio.opendirSync

opendirSync(path: string): Dir

以同步方法打开文件目录。


从API version 9开始废弃，请使用[fs.listFileSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Dir | 返回Dir对象。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
// example code in Dir struct
// use read/readSync/close
```

#### fileio.access

access(path: string, mode?: number): Promise<void>

检查当前进程是否可访问某文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.access](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsaccess)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。 确认当前进程是否具有对应权限： - 0：确认文件是否存在。 - 1：确认当前进程是否具有可执行权限。 - 2：确认当前进程是否具有写权限。 - 4：确认当前进程是否具有读权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath).then(() => {
  console.info("access succeed");
}).catch((err: BusinessError) => {
  console.error("access failed with error:" + err);
});
```

#### fileio.access

access(path: string, mode?: number, callback: AsyncCallback<void>): void

检查当前进程是否可访问某文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.access](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsaccess-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。 确认当前进程是否具有对应权限： - 0：确认文件是否存在。 - 1：确认当前进程是否具有可执行权限。 - 2：确认当前进程是否具有写权限。 - 4：确认当前进程是否具有读权限。 |
callbackAsyncCallback<void>是异步检查当前进程是否可访问某文件之后的回调。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath, (err: BusinessError) => {
  // do something
});
```

#### fileio.accessSync

accessSync(path: string, mode?: number): void

以同步方法检查当前进程是否可访问某文件。


从API version 9开始废弃，请使用[fs.accessSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsaccesssync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。 确认当前进程是否具有对应权限： - 0：确认文件是否存在。 - 1：确认当前进程是否具有可执行权限。 - 2：确认当前进程是否具有写权限。 - 4：确认当前进程是否具有读权限。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
try {
  fileio.accessSync(filePath);
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error:" + err);
}
```

#### fileio.close7+

close(fd: number): Promise<void>

关闭文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.close](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsclose)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error:" + err);
});
```

#### fileio.close7+

close(fd: number, callback: AsyncCallback<void>): void

关闭文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.close](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsclose-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步关闭文件之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.closeSync

closeSync(fd: number): void

以同步方法关闭文件。


从API version 9开始废弃，请使用[fs.closeSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsclosesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.closeSync(fd);
```

#### fileio.copyFile

copyFile(src: string|number, dest: string|number, mode?: number): Promise<void>

复制文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.copyFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fscopyfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。 0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath).then(() => {
  console.info("copyFile succeed");
}).catch((err: BusinessError) => {
  console.error("copyFile failed with error:" + err);
});
```

#### fileio.copyFile

copyFile(src: string|number, dest: string|number, mode: number, callback: AsyncCallback<void>): void

复制文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.copyFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fscopyfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。 0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |
callbackAsyncCallback<void>是异步复制文件之后的回调。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath, (err: BusinessError) => {
  // do something
});
```

#### fileio.copyFileSync

copyFileSync(src: string|number, dest: string|number, mode?: number): void

以同步方法复制文件。


从API version 9开始废弃，请使用[fs.copyFileSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fscopyfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。 0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |

**示例：**

```ets
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFileSync(srcPath, dstPath);
```

#### fileio.mkdir

mkdir(path: string, mode?: number): Promise<void>

创建目录，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.mkdir](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsmkdir)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。 - 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((error: BusinessError) => {
  console.error("mkdir failed with error:" + error);
});
```

#### fileio.mkdir

mkdir(path: string, mode: number, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。


从API version 9开始废弃，请使用[fs.mkdir](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsmkdir-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。 - 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |
callbackAsyncCallback<void>是异步创建目录操作完成之后的回调。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath, (err: BusinessError) => {
  console.info("mkdir succeed");
});
```

#### fileio.mkdirSync

mkdirSync(path: string, mode?: number): void

以同步方法创建目录。


从API version 9开始废弃，请使用[fs.mkdirSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsmkdirsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。 - 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |

**示例：**

```ets
let dirPath = pathDir + '/testDir';
fileio.mkdirSync(dirPath);
```

#### fileio.open7+

open(path: string, flags?: number, mode?: number): Promise<number>

打开文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.open](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsopen)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开： - 0o0：只读打开。 - 0o1：只写打开。 - 0o2：读写打开。 同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项： - 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。 - 0o200：如果追加了0o100选项，且文件已经存在，则出错。 - 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。 - 0o2000：以追加方式打开，后续写将追加到文件末尾。 - 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - 0o200000：如果path不指向目录，则出错。 - 0o400000：如果path指向符号链接，则出错。 - 0o4010000：以同步IO的方式打开文件。 |
| mode | number | 否 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。 - 0o660：所有者具有读、写权限，所有用户组具有读、写权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回打开文件的文件描述符。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.open(filePath, 0o1, 0o0200).then((number: number) => {
  console.info("open file succeed");
}).catch((err: BusinessError) => {
  console.error("open file failed with error:" + err);
});
```

#### fileio.open7+

open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void

打开文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.open](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsopen-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开： - 0o0：只读打开。 - 0o1：只写打开。 - 0o2：读写打开。 同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项： - 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。 - 0o200：如果追加了0o100选项，且文件已经存在，则出错。 - 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。 - 0o2000：以追加方式打开，后续写将追加到文件末尾。 - 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - 0o200000：如果path不指向目录，则出错。 - 0o400000：如果path指向符号链接，则出错。 - 0o4010000：以同步IO的方式打开文件。 |
| mode | number | 否 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。 - 0o660：所有者具有读、写权限，所有用户组具有读、写权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |
callbackAsyncCallback<number>是异步打开文件之后的回调。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.open(filePath, 0, (err: BusinessError, fd: number) => {
  // do something
});
```

#### fileio.openSync

openSync(path: string, flags?: number, mode?: number): number

以同步方法打开文件。


从API version 9开始废弃，请使用[fs.openSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsopensync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开： - 0o0：只读打开。 - 0o1：只写打开。 - 0o2：读写打开。 同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项： - 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。 - 0o200：如果追加了0o100选项，且文件已经存在，则出错。 - 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。 - 0o2000：以追加方式打开，后续写将追加到文件末尾。 - 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - 0o200000：如果path不指向目录，则出错。 - 0o400000：如果path指向符号链接，则出错。 - 0o4010000：以同步IO的方式打开文件。 |
| mode | number | 否 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。 - 0o660：所有者具有读、写权限，所有用户组具有读、写权限。 - 0o640：所有者具有读、写权限，所有用户组具有读权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 创建出的文件权限受umask影响，umask随进程启动确定，其修改当前不开放。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 打开文件的文件描述符。 |

#### fileio.read

read(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): Promise<ReadOut>

从文件读取数据，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.read](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsread)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移。可选，默认为0。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ReadOut> | Promise对象。返回读取的结果。 |

#### fileio.read

read(fd: number, buffer: ArrayBuffer, options: { offset?: number; length?: number; position?: number; }, callback: AsyncCallback<ReadOut>): void

从文件读取数据，使用callback异步回调。


从API version 9开始废弃，请使用[fs.read](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsread-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移。可选，默认为0。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。 约束：offset+length<=buffer.size。 |
| callback | AsyncCallback<ReadOut> | 是 | 异步读取数据之后的回调。 |

#### fileio.readSync

readSync(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): number

以同步方法从文件读取数据。


从API version 9开始废弃，请使用[fs.readSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsreadsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移。可选，默认为0。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o2);
let buf = new ArrayBuffer(4096);
let num = fileio.readSync(fd, buf);
```

#### fileio.rmdir7+

rmdir(path: string): Promise<void>

删除目录，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.rmdir](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsrmdir)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.rmdir(dirPath).then(() => {
  console.info("rmdir succeed");
}).catch((err: BusinessError) => {
  console.error("rmdir failed with error:" + err);
});
```

#### fileio.rmdir7+

rmdir(path: string, callback: AsyncCallback<void>): void

删除目录，使用callback异步回调。


从API version 9开始废弃，请使用[fs.rmdir](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsrmdir-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除目录之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.rmdir(dirPath, (err: BusinessError) => {
  // do something
  console.info("rmdir succeed");
});
```

#### fileio.rmdirSync7+

rmdirSync(path: string): void

以同步方法删除目录。


从API version 9开始废弃，请使用[fs.rmdirSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsrmdirsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |

**示例：**

```ets
let dirPath = pathDir + '/testDir';
fileio.rmdirSync(dirPath);
```

#### fileio.unlink

unlink(path: string): Promise<void>

删除文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.unlink](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsunlink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.unlink(filePath).then(() => {
  console.info("remove file succeed");
}).catch((error: BusinessError) => {
  console.error("remove file failed with error:" + error);
});
```

#### fileio.unlink

unlink(path: string, callback: AsyncCallback<void>): void

删除文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.unlink](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsunlink-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除文件之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.unlink(filePath, (err: BusinessError) => {
  console.info("remove file succeed");
});
```

#### fileio.unlinkSync

unlinkSync(path: string): void

以同步方法删除文件。


从API version 9开始废弃，请使用[fs.unlinkSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsunlinksync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
fileio.unlinkSync(filePath);
```

#### fileio.write

write(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

将数据写入文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.write](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fswrite)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移。可选，默认为0。 - length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际写入的长度。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world").then((number: number) => {
  console.info("write data to file succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error:" + err);
});
```

#### fileio.write

write(fd: number, buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.write](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fswrite-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移。可选，默认为0。 - length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 约束：offset+length<=buffer.size。 |
callbackAsyncCallback<number>是异步将数据写入完成后执行的回调函数。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world", (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    console.info("write data to file succeed and size is:" + bytesWritten);
  }
});
```

#### fileio.writeSync

writeSync(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

以同步方法将数据写入文件。


从API version 9开始废弃，请使用[fs.writeSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fswritesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移。可选，默认为0。 - length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
let num = fileio.writeSync(fd, "hello, world");
```

#### fileio.hash

hash(path: string, algorithm: string): Promise<string>

计算文件的哈希值，使用Promise异步回调。


从API version 9开始废弃，请使用[hash.write](@ohos.file.hash (文件哈希处理).md#ZH-CN_TOPIC_0000002553201183__hashhash)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回文件的哈希值。表示为十六进制数字串，所有字母均大写。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256").then((str: string) => {
  console.info("calculate file hash succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("calculate file hash failed with error:" + err);
});
```

#### fileio.hash

hash(path: string, algorithm: string, callback: AsyncCallback<string>): void

计算文件的哈希值，使用callback异步回调。


从API version 9开始废弃，请使用[hash.write](@ohos.file.hash (文件哈希处理).md#ZH-CN_TOPIC_0000002553201183__hashhash-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |
| callback | AsyncCallback<string> | 是 | 异步计算文件哈希操作之后的回调函数（其中给定文件哈希值表示为十六进制数字串，所有字母均大写）。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256", (err: BusinessError, hashStr: string) => {
  if (hashStr) {
    console.info("calculate file hash succeed:" + hashStr);
  }
});
```

#### fileio.chmod7+

chmod(path: string, mode: number): Promise<void>

改变文件权限，使用Promise异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 改变文件权限，可给定如下权限，以按位或的方式追加权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.chmod(filePath, 0o700).then(() => {
  console.info("chmod succeed");
}).catch((err: BusinessError) => {
  console.error("chmod failed with error:" + err);
});
```

#### fileio.chmod7+

chmod(path: string, mode: number, callback: AsyncCallback<void>): void

改变文件权限，使用callback异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 改变文件权限，可给定如下权限，以按位或的方式追加权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |
callbackAsyncCallback<void>是异步改变文件权限之后的回调。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.chmod(filePath, 0o700, (err: BusinessError) => {
  // do something
});
```

#### fileio.chmodSync7+

chmodSync(path: string, mode: number): void

以同步方法改变文件权限。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 改变文件权限，可给定如下权限，以按位或的方式追加权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
fileio.chmodSync(filePath, 0o700);
```

#### fileio.fstat7+

fstat(fd: number): Promise<Stat>

基于文件描述符获取文件状态信息，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.stat](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsstat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Stat> | Promise对象。返回表示文件状态的具体信息。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fstat(fd).then((stat: fileio.Stat) => {
  console.info("fstat succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("fstat failed with error:" + err);
});
```

#### fileio.fstat7+

fstat(fd: number, callback: AsyncCallback<Stat>): void

基于文件描述符获取文件状态信息，使用callback异步回调。


从API version 9开始废弃，请使用[fs.stat](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsstat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |
| callback | AsyncCallback<Stat> | 是 | 异步获取文件状态信息之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fstat(fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.fstatSync7+

fstatSync(fd: number): Stat

以同步方法基于文件描述符获取文件状态信息。


从API version 9开始废弃，请使用[fs.statSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsstatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stat | 表示文件状态的具体信息。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.fstatSync(fd);
```

#### fileio.ftruncate7+

ftruncate(fd: number, len?: number): Promise<void>

基于文件描述符截断文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.truncate](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fstruncate)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.ftruncate(fd, 5).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error:" + err);
});
```

#### fileio.ftruncate7+

ftruncate(fd: number, len?: number, callback: AsyncCallback<void>): void

基于文件描述符截断文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.truncate](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fstruncate-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，以字节为单位。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let len = 5;
fileio.ftruncate(fd, 5, (err: BusinessError) => {
  // do something
});
```

#### fileio.ftruncateSync7+

ftruncateSync(fd: number, len?: number): void

以同步方法基于文件描述符截断文件。


从API version 9开始废弃，请使用[fs.truncateSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fstruncatesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，以字节为单位。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let len = 5;
fileio.ftruncateSync(fd, len);
```

#### fileio.truncate7+

truncate(path: string, len?: number): Promise<void>

基于文件路径截断文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.truncate](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fstruncate)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncate(filePath, len).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error:" + err);
});
```

#### fileio.truncate7+

truncate(path: string, len?: number, callback: AsyncCallback<void>): void

基于文件路径截断文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.truncate](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fstruncate-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，以字节为单位。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncate(filePath, len, (err: BusinessError) => {
  // do something
});
```

#### fileio.truncateSync7+

truncateSync(path: string, len?: number): void

以同步方法基于文件路径截断文件。


从API version 9开始废弃，请使用[fs.truncateSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fstruncatesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，以字节为单位。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncateSync(filePath, len);
```

#### fileio.readText7+

readText(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): Promise<string>

基于文本方式读取文件（即直接读取文件的文本内容），使用Promise异步回调。


从API version 9开始废弃，请使用[fs.readText](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsreadtext)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 支持如下选项： - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读取。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回读取文件的内容。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.readText(filePath).then((str: string) => {
  console.info("readText succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("readText failed with error:" + err);
});
```

#### fileio.readText7+

readText(filePath: string, options: { position?: number; length?: number; encoding?: string; }, callback: AsyncCallback<string>): void

基于文本方式读取文件（即直接读取文件的文本内容），使用callback异步回调。


从API version 9开始废弃，请使用[fs.readText](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsreadtext-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 支持如下选项： - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读取。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - encoding，string类型，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |
callbackAsyncCallback<string>是回调函数，返回读取文件的内容。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
class Option {
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.position = 1;
option.encoding = 'utf-8';
fileio.readText(filePath, option, (err: BusinessError, str: string) => {
  // do something
});
```

#### fileio.readTextSync7+

readTextSync(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): string

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。


从API version 9开始废弃，请使用[fs.readTextSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsreadtextsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 支持如下选项： - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读取。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回读取文件的内容。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
class Option {
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.position = 1;
option.length = 3;
let str = fileio.readTextSync(filePath, option);
```

#### fileio.lstat7+

lstat(path: string): Promise<Stat>

获取链接信息，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.lstat](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslstat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Stat> | promise对象，返回文件对象，表示文件的具体信息，详情见stat。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.lstat(filePath).then((stat: fileio.Stat) => {
  console.info("get link status succeed, the size of file is" + stat.size);
}).catch((err: BusinessError) => {
  console.error("get link status failed with error:" + err);
});
```

#### fileio.lstat7+

lstat(path: string, callback: AsyncCallback<Stat>): void

获取链接信息，使用callback异步回调。


从API version 9开始废弃，请使用[fs.lstat](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslstat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标文件的应用沙箱路径。 |
| callback | AsyncCallback<Stat> | 是 | 回调函数，返回文件的具体信息。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.lstat(filePath, (err: BusinessError, stat: fileio.Stat) => {
  // do something
});
```

#### fileio.lstatSync7+

lstatSync(path: string): Stat

以同步方法获取链接信息。


从API version 9开始废弃，请使用[fs.lstatSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslstatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stat | 表示文件的具体信息。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let stat = fileio.lstatSync(filePath);
```

#### fileio.rename7+

rename(oldPath: string, newPath: string): Promise<void>

重命名文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.rename](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsrename)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile).then(() => {
  console.info("rename succeed");
}).catch((err: BusinessError) => {
  console.error("rename failed with error:" + err);
});
```

#### fileio.rename7+

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

重命名文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.rename](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsrename-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步重命名文件之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile, (err: BusinessError) => {
});
```

#### fileio.renameSync7+

renameSync(oldPath: string, newPath: string): void

以同步方法重命名文件。


从API version 9开始废弃，请使用[fs.renameSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsrenamesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |

**示例：**

```ets
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.renameSync(srcFile, dstFile);
```

#### fileio.fsync7+

fsync(fd: number): Promise<void>

同步文件数据，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.fsync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error:" + err);
});
```

#### fileio.fsync7+

fsync(fd: number, callback: AsyncCallback<void>): void

同步文件数据，使用callback异步回调。


从API version 9开始废弃，请使用[fs.fsync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfsync-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件数据同步之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.fsyncSync7+

fsyncSync(fd: number): void

以同步方法同步文件数据。


从API version 9开始废弃，请使用[fs.fsyncSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfsyncsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsyncSync(fd);
```

#### fileio.fdatasync7+

fdatasync(fd: number): Promise<void>

实现文件内容数据同步，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.fdatasync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfdatasync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdatasync(fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error:" + err);
});
```

#### fileio.fdatasync7+

fdatasync(fd: number, callback: AsyncCallback<void>): void

实现文件内容数据同步，使用callback异步回调。


从API version 9开始废弃，请使用[fs.fdatasync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfdatasync-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件内容数据同步之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdatasync (fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.fdatasyncSync7+

fdatasyncSync(fd: number): void

以同步方法实现文件内容数据同步。


从API version 9开始废弃，请使用[fs.fdatasyncSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfdatasyncsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.fdatasyncSync(fd);
```

#### fileio.symlink7+

symlink(target: string, srcPath: string): Promise<void>

基于文件路径创建符号链接，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.symlink](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fssymlink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile).then(() => {
  console.info("symlink succeed");
}).catch((err: BusinessError) => {
  console.error("symlink failed with error:" + err);
});
```

#### fileio.symlink7+

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

基于文件路径创建符号链接，使用callback异步回调。


从API version 9开始废弃，请使用[fs.symlink](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fssymlink-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步创建符号链接信息之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile, (err: BusinessError) => {
  // do something
});
```

#### fileio.symlinkSync7+

symlinkSync(target: string, srcPath: string): void

以同步的方法基于文件路径创建符号链接。


从API version 9开始废弃，请使用[fs.symlinkSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fssymlinksync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**示例：**

```ets
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlinkSync(srcFile, dstFile);
```

#### fileio.chown7+

chown(path: string, uid: number, gid: number): Promise<void>

基于文件路径改变文件所有者，使用Promise异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID（UserID）。 |
| gid | number | 是 | 新的GID（GroupID）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.chown(filePath, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});
```

#### fileio.chown7+

chown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件路径改变文件所有者，使用callback异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath)
fileio.chown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
  // do something
});
```

#### fileio.chownSync7+

chownSync(path: string, uid: number, gid: number): void

以同步的方法基于文件路径改变文件所有者。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath)
fileio.chownSync(filePath, stat.uid, stat.gid);
```

#### fileio.mkdtemp7+

mkdtemp(prefix: string): Promise<string>

创建临时目录，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.mkdtemp](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsmkdtemp)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回生成的唯一目录路径。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX").then((pathDir: string) => {
  console.info("mkdtemp succeed:" + pathDir);
}).catch((err: BusinessError) => {
  console.error("mkdtemp failed with error:" + err);
});
```

#### fileio.mkdtemp7+

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

创建临时目录，使用callback异步回调。


从API version 9开始废弃，请使用[fs.mkdtemp](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsmkdtemp-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |
| callback | AsyncCallback<string> | 是 | 异步创建临时目录之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  // do something
});
```

#### fileio.mkdtempSync7+

mkdtempSync(prefix: string): string

以同步的方法创建临时目录。


从API version 9开始废弃，请使用[fs.mkdtempSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsmkdtempsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 产生的唯一目录路径。 |

**示例：**

```ets
let res = fileio.mkdtempSync(pathDir + "/XXXXXX");
```

#### fileio.fchmod7+

fchmod(fd: number, mode: number): Promise<void>

基于文件描述符改变文件权限，使用Promise异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmod(fd, mode).then(() => {
  console.info("chmod succeed");
}).catch((err: BusinessError) => {
  console.error("chmod failed with error:" + err);
});
```

#### fileio.fchmod7+

fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void

基于文件描述符改变文件权限，使用callback异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |
callbackAsyncCallback<void>是异步改变文件权限之后的回调。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmod(fd, mode, (err: BusinessError) => {
  // do something
});
```

#### fileio.fchmodSync7+

fchmodSync(fd: number, mode: number): void

以同步方法基于文件描述符改变文件权限。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。 - 0o700：所有者具有读、写及可执行权限。 - 0o400：所有者具有读权限。 - 0o200：所有者具有写权限。 - 0o100：所有者具有可执行权限。 - 0o070：所有用户组具有读、写及可执行权限。 - 0o040：所有用户组具有读权限。 - 0o020：所有用户组具有写权限。 - 0o010：所有用户组具有可执行权限。 - 0o007：其余用户具有读、写及可执行权限。 - 0o004：其余用户具有读权限。 - 0o002：其余用户具有写权限。 - 0o001：其余用户具有可执行权限。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmodSync(fd, mode);
```

#### fileio.createStream7+

createStream(path: string, mode: string): Promise<Stream>

基于文件路径打开文件流，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.createStream](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fscreatestream)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Stream> | Promise对象。返回文件流的结果。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.createStream(filePath, "r+").then((stream: fileio.Stream) => {
  console.info("createStream succeed");
}).catch((err: BusinessError) => {
  console.error("createStream failed with error:" + err);
});
```

#### fileio.createStream7+

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

基于文件路径打开文件流，使用callback异步回调。


从API version 9开始废弃，请使用[fs.createStream](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fscreatestream-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback<Stream> | 是 | 异步打开文件流之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.createStream(filePath, "r+", (err: BusinessError, stream: fileio.Stream) => {
  // do something
});
```

#### fileio.createStreamSync7+

createStreamSync(path: string, mode: string): Stream

以同步方法基于文件路径打开文件流。


从API version 9开始废弃，请使用[fs.createStreamSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fscreatestreamsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stream | 返回文件流的结果。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
```

#### fileio.fdopenStream7+

fdopenStream(fd: number, mode: string): Promise<Stream>

基于文件描述符打开文件流，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.fdopenStream](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfdopenstream)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Stream> | Promise对象。返回文件流的结果。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdopenStream(fd, "r+").then((stream: fileio.Stream) => {
  console.info("openStream succeed");
}).catch((err: BusinessError) => {
  console.error("openStream failed with error:" + err);
});
```

#### fileio.fdopenStream7+

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

基于文件描述符打开文件流，使用callback异步回调。


从API version 9开始废弃，请使用[fs.fdopenStream](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfdopenstream-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback<Stream> | 是 | 异步打开文件流之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdopenStream(fd, "r+", (err: BusinessError, stream: fileio.Stream) => {
  // do something
});
```

#### fileio.fdopenStreamSync7+

fdopenStreamSync(fd: number, mode: string): Stream

以同步方法基于文件描述符打开文件流。


从API version 9开始废弃，请使用[fs.fdopenStreamSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fsfdopenstreamsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stream | 返回文件流的结果。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let ss = fileio.fdopenStreamSync(fd, "r+");
```

#### fileio.fchown7+

fchown(fd: number, uid: number, gid: number): Promise<void>

基于文件描述符改变文件所有者，使用Promise异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchown(fd, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});
```

#### fileio.fchown7+

fchown(fd: number, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件描述符改变文件所有者，使用callback异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchown(fd, stat.uid, stat.gid, (err: BusinessError) => {
  // do something
});
```

#### fileio.fchownSync7+

fchownSync(fd: number, uid: number, gid: number): void

以同步方法基于文件描述符改变文件所有者。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchownSync(fd, stat.uid, stat.gid);
```

#### fileio.lchown7+

lchown(path: string, uid: number, gid: number): Promise<void>

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是符号链接所指向的实际文件，使用Promise异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchown(filePath, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});
```

#### fileio.lchown7+

lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件，使用callback异步回调。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
  // do something
});
```

#### fileio.lchownSync7+

lchownSync(path: string, uid: number, gid: number): void

以同步方法基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchownSync(filePath, stat.uid, stat.gid);
```

#### fileio.createWatcher7+

createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher

监听文件或者目录的变化，使用callback异步回调。

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filename | string | 是 | 待监视文件的应用沙箱路径。 |
| events | number | 是 | - 1: 监听文件或者目录是否发生重命名。 - 2：监听文件或者目录内容的是否修改。 - 3：两者都有。 |
callbackAsyncCallback<number>是每发生变化一次，调用一次此函数。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Watcher | Promise对象。返回文件变化监听的实例。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
```

#### Readout

仅用于read方法，获取文件的读取结果。

从API version 9开始废弃。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

| 名称 | 类型 | 只读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| bytesRead | number | 是 | 是 | 实际读取长度。 |
| offset | number | 是 | 是 | 读取数据相对于缓冲区首地址的偏移。 |
| buffer | ArrayBuffer | 是 | 是 | 保存读取数据的缓冲区。 |

#### Stat

文件具体信息，在调用Stat的方法前，需要先通过[stat()](#ZH-CN_TOPIC_0000002522081224__fileiostat)方法（同步或异步）来构建一个Stat实例。


从API version 9开始废弃，请使用[fs.Stat](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__stat)替代。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

#### 属性

| 名称 | 类型 | 只读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| dev | number | 是 | 否 | 标识包含该文件的主设备号。 |
| ino | number | 是 | 否 | 标识该文件。通常同设备上的不同文件的INO不同。 |
| mode | number | 是 | 否 | 表示文件类型及权限，其首 4 位表示文件类型，后 12 位表示权限。各特征位的含义如下： - 0o170000：可用于获取文件类型的掩码。 - 0o140000：文件是套接字。 - 0o120000：文件是符号链接。 - 0o100000：文件是一般文件。 - 0o060000：文件属于块设备。 - 0o040000：文件是目录。 - 0o020000：文件是字符设备。 - 0o010000：文件是命名管道，即FIFO。 - 0o0700：可用于获取用户权限的掩码。 - 0o0400：用户读，对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。 - 0o0200：用户写，对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。 - 0o0100：用户执行，对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。 - 0o0070：可用于获取用户组权限的掩码。 - 0o0040：用户组读，对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。 - 0o0020：用户组写，对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。 - 0o0010：用户组执行，对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。 - 0o0007：可用于获取其他用户权限的掩码。 - 0o0004：其他读，对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。 - 0o0002：其他写，对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。 - 0o0001：其他执行，对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。 |
| nlink | number | 是 | 否 | 文件的硬链接数。 |
| uid | number | 是 | 否 | 文件所有者的ID。 |
| gid | number | 是 | 否 | 文件所有组的ID。 |
| rdev | number | 是 | 否 | 标识包含该文件的从设备号。 |
| size | number | 是 | 否 | 文件的大小，以字节为单位。仅对普通文件有效。 |
| blocks | number | 是 | 否 | 文件占用的块数，计算时块大小按512B计算。 |
| atime | number | 是 | 否 | 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| mtime | number | 是 | 否 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| ctime | number | 是 | 否 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。 |

#### isBlockDevice

isBlockDevice(): boolean

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。


从API version 9开始废弃，请使用[fs.Stat.isBlockDevice](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__isblockdevice)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是块特殊设备。true为是，false为不是。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isBLockDevice = fileio.statSync(filePath).isBlockDevice();
```

#### isCharacterDevice

isCharacterDevice(): boolean

用于判断文件是否是字符特殊文件。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。


从API version 9开始废弃，请使用[fs.Stat.isCharacterDevice](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__ischaracterdevice)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是字符特殊设备。true为是，false为不是。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isCharacterDevice = fileio.statSync(filePath).isCharacterDevice();
```

#### isDirectory

isDirectory(): boolean

用于判断文件是否是目录。


从API version 9开始废弃，请使用[fs.Stat.isDirectory](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__isdirectory)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是目录。true为是，false为不是。 |

**示例：**

```ets
let dirPath = pathDir + "/test";
let isDirectory = fileio.statSync(dirPath).isDirectory();
```

#### isFIFO

isFIFO(): boolean

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。


从API version 9开始废弃，请使用[fs.Stat.isFIFO](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__isfifo)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是 FIFO。true为是，false为不是。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isFIFO = fileio.statSync(filePath).isFIFO();
```

#### isFile

isFile(): boolean

用于判断文件是否是普通文件。


从API version 9开始废弃，请使用[fs.Stat.isFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__isfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是普通文件。true为是，false为不是。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isFile = fileio.statSync(filePath).isFile();
```

#### isSocket

isSocket(): boolean

用于判断文件是否是套接字。


从API version 9开始废弃，请使用[fs.Stat.isSocket](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__issocket)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是套接字。true为是，false为不是。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isSocket = fileio.statSync(filePath).isSocket();
```

#### isSymbolicLink

isSymbolicLink(): boolean

用于判断文件是否是符号链接。


从API version 9开始废弃，请使用[fs.Stat.isSymbolicLink](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__issymboliclink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是符号链接。true为是，false为不是。 |

**示例：**

```ets
let filePath = pathDir + "/test";
let isSymbolicLink = fileio.statSync(filePath).isSymbolicLink();
```

#### Watcher7+

Watcher是文件变化监听的实例，调用Watcher.stop()方法（同步或异步）来停止文件监听。

从API version 10开始废弃。

#### stop7+

stop(): Promise<void>

关闭watcher监听，使用Promise异步回调。

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
watcher.stop().then(() => {
  console.info("close watcher succeed");
});
```

#### stop7+

stop(callback: AsyncCallback<void>): void

关闭watcher监听，使用callback异步回调。

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 以异步方法关闭watcher监听之后的回调。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
watcher.stop(() => {
  console.info("close watcher succeed");
})
```

#### Stream

文件流，在调用Stream的方法前，需要先通过createStream()方法（同步或异步）来构建一个Stream实例。


从API version 9开始废弃，请使用[fs.Stream](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__stream)替代。

#### close7+

close(): Promise<void>

关闭文件流，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.Stream.close](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__close)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。返回表示异步关闭文件流的结果。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error:" + err);
});
```

#### close7+

close(callback: AsyncCallback<void>): void

异步关闭文件流，使用callback异步回调。


从API version 9开始废弃，请使用[fs.Stream.close](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__close-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 异步关闭文件流之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close((err: BusinessError) => {
  // do something
});
```

#### closeSync

closeSync(): void

同步关闭文件流。


从API version 9开始废弃，请使用[fs.Stream.closeSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__closesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.closeSync();
```

#### flush7+

flush(): Promise<void>

刷新文件流，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.Stream.flush](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__flush)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。返回表示异步刷新文件流的结果。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush().then(() => {
  console.info("flush succeed");
}).catch((err: BusinessError) => {
  console.error("flush failed with error:" + err);
});
```

#### flush7+

flush(callback: AsyncCallback<void>): void

异步刷新文件流，使用callback异步回调。


从API version 9开始废弃，请使用[fs.Stream.flush](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__flush-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 异步刷新文件流后的回调函数。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush((err: BusinessError) => {
  // do something
});
```

#### flushSync7+

flushSync(): void

同步刷新文件流。


从API version 9开始废弃，请使用[fs.Stream.flushSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__flushsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flushSync();
```

#### write7+

write(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

将数据写入流文件，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.Stream.write](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__write)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移。可选，默认为0。 - length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际写入的长度。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option).then((number: number) => {
  console.info("write succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write failed with error:" + err);
});
```

#### write7+

write(buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

将数据写入流文件，使用callback异步回调。


从API version 9开始废弃，请使用[fs.Stream.write](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__write-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移。可选，默认为0。 - length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 约束：offset+length<=buffer.size。 |
callbackAsyncCallback<number>是异步写入完成后执行的回调函数。

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option, (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    // do something
    console.info("write succeed and size is:" + bytesWritten);
  }
});
```

#### writeSync7+

writeSync(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

以同步方法将数据写入流文件。


从API version 9开始废弃，请使用[fs.Stream.writeSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__writesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移。可选，默认为0。 - length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath,"r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let num = ss.writeSync("hello, world", option);
```

#### read7+

read(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): Promise<ReadOut>

从流文件读取数据，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.Stream.read](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__read)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移。可选，默认为0。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ReadOut> | Promise对象。返回读取的结果。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option).then((readResult: fileio.ReadOut) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
  console.info(`The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error("read data failed with error:" + err);
});
```

#### read7+

read(buffer: ArrayBuffer, options: { position?: number; offset?: number; length?: number; }, callback: AsyncCallback<ReadOut>): void

从流文件读取数据，使用callback异步回调。


从API version 9开始废弃，请使用[fs.Stream.read](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__read-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移。可选，默认为0。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。 约束：offset+length<=buffer.size。 |
| callback | AsyncCallback<ReadOut> | 是 | 异步从流文件读取数据之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option, (err: BusinessError, readResult: fileio.ReadOut) => {
  if (readResult.bytesRead) {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
    console.info(`The content of file: ${buf.toString()}`);
  }
});
```

#### readSync7+

readSync(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): number

以同步方法从流文件读取数据。


从API version 9开始废弃，请使用[fs.Stream.readSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__readsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 支持如下选项： - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移。可选，默认为0。 - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度。 - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。 约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度。 |

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let buf = new ArrayBuffer(4096)
let num = ss.readSync(buf, option);
```

#### Dir

管理目录，在调用Dir的方法前，需要先通过opendir方法（同步或异步）来构建一个Dir实例。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile)替代。

#### read

read(): Promise<Dirent>

读取下一个目录项，使用Promise异步回调。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Dirent> | Promise对象。返回表示异步读取目录项的结果。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
dir.read().then((dirent: fileio.Dirent) => {
  console.info("read succeed, the name of dirent is " + dirent.name);
}).catch((err: BusinessError) => {
  console.error("read failed with error:" + err);
});
```

#### read

read(callback: AsyncCallback<Dirent>): void

读取下一个目录项，使用callback异步回调。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Dirent> | 是 | 异步读取下一个目录项之后的回调。 |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
dir.read((err: BusinessError, dirent: fileio.Dirent) => {
  if (dirent) {
    // do something
    console.info("read succeed, the name of file is " + dirent.name);
  }
});
```

#### readSync

readSync(): Dirent

同步读取下一个目录项。


从API version 9开始废弃，请使用[fs.listFileSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Dirent | 表示一个目录项。 |

**示例：**

```ets
let dirent = dir.readSync();
```

#### close7+

close(): Promise<void>

异步关闭目录，使用promise形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ets
import { BusinessError } from '@ohos.base';
dir.close().then(() => {
  console.info("close dir successfully");
});
```

#### close7+

close(callback: AsyncCallback<void>): void

异步关闭目录，使用callback形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ets
import { BusinessError } from '@ohos.base';
dir.close((err: BusinessError) => {
  console.info("close dir successfully");
});
```

#### closeSync

closeSync(): void

用于关闭目录。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。


从API version 9开始废弃，请使用[fs.listFileSync](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ets
dir.closeSync();
```

#### Dirent

在调用Dirent的方法前，需要先通过[dir.read()](#ZH-CN_TOPIC_0000002522081224__read)方法（同步或异步）来构建一个Dirent实例。


从API version 9开始废弃，请使用[fs.listFile](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002522241216__fslistfile)替代。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

#### 属性

| 名称 | 类型 | 只读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 目录项的名称。 |

#### isBlockDevice

isBlockDevice(): boolean

用于判断当前目录项是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是块特殊设备。true为是，false为不是。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
let isBLockDevice = dir.readSync().isBlockDevice();
```

#### isCharacterDevice

isCharacterDevice(): boolean

用于判断当前目录项是否是字符特殊设备。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是字符特殊设备。true为是，false为不是。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
let isCharacterDevice = dir.readSync().isCharacterDevice();
```

#### isDirectory

isDirectory(): boolean

用于判断当前目录项是否是目录。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是目录。true为是，false为不是。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
let isDirectory = dir.readSync().isDirectory();
```

#### isFIFO

isFIFO(): boolean

用于判断当前目录项是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是FIFO。true为是，false为不是。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
let isFIFO = dir.readSync().isFIFO();
```

#### isFile

isFile(): boolean

用于判断当前目录项是否是普通文件。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是普通文件。true为是，false为不是。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
let isFile = dir.readSync().isFile();
```

#### isSocket

isSocket(): boolean

用于判断当前目录项是否是套接字。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是套接字。true为是，false为不是。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
let isSocket = dir.readSync().isSocket();
```

#### isSymbolicLink

isSymbolicLink(): boolean

用于判断当前目录项是否是符号链接。

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是符号链接。true为是，false为不是。 |

**示例：**

```ets
let dir = fileio.opendirSync(pathDir);
let isSymbolicLink = dir.readSync().isSymbolicLink();
```