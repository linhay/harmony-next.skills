# @ohos.file.fs (文件管理)

该模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
```

#### 使用说明

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
  }
}
```

获取沙箱路径的方式及其接口用法也可参考：[应用上下文Context-获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取应用文件路径)。

将指向资源的字符串称为URI。对于只支持沙箱路径作为入参的接口，可以使用构造fileUri对象并获取其沙箱路径的属性的方式将URI转换为沙箱路径，然后使用文件接口。URI定义解及其转换方式请参考：[文件URI](@ohos.file.fileuri (文件URI).md)。

#### fs.stat

stat(file: string | number): Promise<Stat>

获取文件或目录详细属性信息，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | number是

文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。

**说明**：从API version 22开始，支持传入URI。

**返回值：**

类型说明Promise<[Stat](#ZH-CN_TOPIC_0000002529445221__stat)>Promise对象。返回文件或目录的具体信息。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.stat(filePath).then((stat: fs.Stat) => {
  console.info("get file info succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("get file info failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.stat

stat(file: string | number, callback: AsyncCallback<Stat>): void

获取文件或目录的详细属性信息，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | number是

文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。

**说明**：从API version 22开始，支持传入URI。

callbackAsyncCallback<[Stat](#ZH-CN_TOPIC_0000002529445221__stat)>是异步获取文件或目录的信息之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
fs.stat(pathDir, (err: BusinessError, stat: fs.Stat) => {
  if (err) {
    console.error("get file info failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("get file info succeed, the size of file is " + stat.size);
  }
});
```

#### fs.statSync

statSync(file: string | number): Stat

以同步方法获取文件或目录详细属性信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | number是

文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。

**说明**：从API version 22开始，支持传入URI。

**返回值：**

类型说明[Stat](#ZH-CN_TOPIC_0000002529445221__stat)表示文件或目录的具体信息。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let stat = fs.statSync(pathDir);
console.info("get file info succeed, the size of file is " + stat.size);
```

#### fs.access

access(path: string, mode?: AccessModeType): Promise<boolean>

检查文件或目录是否存在，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录应用沙箱路径。mode12+[AccessModeType](#ZH-CN_TOPIC_0000002529445221__accessmodetype12)否文件或目录校验的权限。不填该参数则默认校验文件是否存在。

**返回值：**

类型说明Promise<boolean>Promise对象。返回布尔值。返回true，表示文件存在；返回false，表示文件不存在。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.access(filePath).then((res: boolean) => {
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
}).catch((err: BusinessError) => {
  console.error("access failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.access12+

access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>

检查文件或目录是否在本地，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录应用沙箱路径。mode12+[AccessModeType](#ZH-CN_TOPIC_0000002529445221__accessmodetype12)是文件或目录校验的权限。flag12+[AccessFlagType](#ZH-CN_TOPIC_0000002529445221__accessflagtype12)是文件或目录校验的位置。

**返回值：**

类型说明Promise<boolean>Promise对象。返回布尔值。返回true，表示文件或目录在本地且校验权限存在；返回false，表示文件或目录不存在或者文件或目录在云端或其他分布式设备上。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.access(filePath, fs.AccessModeType.EXIST, fs.AccessFlagType.LOCAL).then((res: boolean) => {
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
}).catch((err: BusinessError) => {
  console.error("access failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.access

access(path: string, callback: AsyncCallback<boolean>): void

检查文件或目录是否存在，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录应用沙箱路径。callbackAsyncCallback<boolean>是异步检查文件或目录是否存在的回调。如果存在，回调返回true；否则返回false。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.access(filePath, (err: BusinessError, res: boolean) => {
  if (err) {
    console.error("access failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (res) {
      console.info("file exists");
    } else {
      console.info("file not exists");
    }
  }
});
```

#### fs.accessSync

accessSync(path: string, mode?: AccessModeType): boolean

以同步方法检查文件或目录是否存在，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录应用沙箱路径。mode12+[AccessModeType](#ZH-CN_TOPIC_0000002529445221__accessmodetype12)否文件或目录校验的权限。不填该参数则默认校验文件或目录是否存在。

**返回值：**

类型说明boolean返回true，表示文件存在；返回false，表示文件不存在。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
try {
  let res = fs.accessSync(filePath);
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error message: " + err.message + ", error code: " + err.code);
}
```

#### fs.accessSync12+

accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean

以同步方法检查文件或目录是否在本地，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件应用沙箱路径。mode12+[AccessModeType](#ZH-CN_TOPIC_0000002529445221__accessmodetype12)是文件或目录校验的权限。flag12+[AccessFlagType](#ZH-CN_TOPIC_0000002529445221__accessflagtype12)是文件或目录校验的位置。

**返回值：**

类型说明boolean返回true，表示文件在本地且校验权限存在；返回false，表示文件不存在或者文件在云端或其他分布式设备上。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
try {
  let res = fs.accessSync(filePath, fs.AccessModeType.EXIST, fs.AccessFlagType.LOCAL);
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error message: " + err.message + ", error code: " + err.code);
}
```

#### fs.close

close(file: number | File): Promise<void>

关闭文件或目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filenumber | [File](#ZH-CN_TOPIC_0000002529445221__file)是已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.close(file).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.close

close(file: number | File, callback: AsyncCallback<void>): void

关闭文件或目录，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filenumber | [File](#ZH-CN_TOPIC_0000002529445221__file)是已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。callbackAsyncCallback<void>是异步关闭文件或目录之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.close(file, (err: BusinessError) => {
  if (err) {
    console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close file succeed");
  }
});
```

#### fs.closeSync

closeSync(file: number | File): void

以同步方法关闭文件或目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filenumber | [File](#ZH-CN_TOPIC_0000002529445221__file)是已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.closeSync(file);
```

#### fs.copy11+

copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>

拷贝文件或目录，使用promise异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcUristring是待复制文件或目录的URI。destUristring是目标文件或目录的URI。options[CopyOptions](#ZH-CN_TOPIC_0000002529445221__copyoptions11)否options中提供拷贝进度回调。不填该参数则无拷贝进度回调。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
  console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let copyOption: fs.CopyOptions = {
  "progressListener" : progressListener
}
try {
  fs.copy(srcDirUriLocal, dstDirUriLocal, copyOption).then(()=>{
    console.info("Succeeded in copying.");
  }).catch((err: BusinessError)=>{
    console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
  })
} catch(err) {
  console.error(`Failed to copy.Code: ${err.code}, message: ${err.message}`);
}
```

#### fs.copy11+

copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcUristring是待复制文件或目录的URI。destUristring是目标文件或目录的URI。callbackAsyncCallback<void>是异步拷贝之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  fs.copy(srcDirUriLocal, dstDirUriLocal, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
}
```

#### fs.copy11+

copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcUristring是待复制文件或目录的URI。destUristring是目标文件或目录的URI。options[CopyOptions](#ZH-CN_TOPIC_0000002529445221__copyoptions11)是拷贝进度回调。callbackAsyncCallback<void>是异步拷贝之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
    console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
  };
  let copyOption: fs.CopyOptions = {
    "progressListener" : progressListener
  }
  fs.copy(srcDirUriLocal, dstDirUriLocal, copyOption, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
}
```

#### fs.copyFile

copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>

复制文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring | number是待复制文件的路径或待复制文件的文件描述符。deststring | number是目标文件路径或目标文件的文件描述符。modenumber否

mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFile(srcPath, dstPath, 0).then(() => {
  console.info("copy file succeed");
}).catch((err: BusinessError) => {
  console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.copyFile

copyFile(src: string | number, dest: string | number, mode: number, callback: AsyncCallback<void>): void

复制文件，可设置覆盖文件的方式，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring | number是待复制文件的路径或待复制文件的文件描述符。deststring | number是目标文件路径或目标文件的文件描述符。modenumber是

mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

callbackAsyncCallback<void>是异步复制文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFile(srcPath, dstPath, 0, (err: BusinessError) => {
  if (err) {
    console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy file succeed");
  }
});
```

#### fs.copyFile

copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void

复制文件，覆盖方式为完全覆盖目标文件，未覆盖部分将被裁切。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring | number是待复制文件的路径或待复制文件的文件描述符。deststring | number是目标文件路径或目标文件的文件描述符。callbackAsyncCallback<void>是异步复制文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFile(srcPath, dstPath, (err: BusinessError) => {
  if (err) {
    console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy file succeed");
  }
});
```

#### fs.copyFileSync

copyFileSync(src: string | number, dest: string | number, mode?: number): void

以同步方法复制文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring | number是待复制文件的路径或待复制文件的文件描述符。deststring | number是目标文件路径或目标文件的文件描述符。modenumber否

mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFileSync(srcPath, dstPath);
```

#### fs.copyDir10+

copyDir(src: string, dest: string, mode?: number): Promise<void>

复制源目录至目标路径下，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。modenumber否

复制模式，默认值为0。

- mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>形式提供。

- mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fs.copyDir(srcPath, destPath, 0).then(() => {
  console.info("copy directory succeed");
}).catch((err: BusinessError) => {
  console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.copyDir10+

copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

复制源目录至目标路径下，可设置复制模式。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。modenumber是

复制模式，默认值为0。

- mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>形式提供。

- mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

callbackAsyncCallback<void, Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>>是异步复制目录之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fs.copyDir(srcPath, destPath, 0, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("copy directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy directory succeed");
  }
});
```

#### fs.copyDir10+

copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

复制源目录至目标路径下，使用callback异步回调。

如果目标目录下有与源目录名冲突的目录，且冲突目录下有同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>形式提供。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。callbackAsyncCallback<void, Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>>是异步复制目录之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fs.copyDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("copy directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy directory succeed");
  }
});
```

#### fs.copyDirSync10+

copyDirSync(src: string, dest: string, mode?: number): void

以同步方法复制源目录至目标路径下。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。modenumber否

复制模式，默认值为0。

- mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>形式提供。

- mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
try {
  fs.copyDirSync(srcPath, destPath, 0);
  console.info("copy directory succeed");
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
}
```

#### fs.dup10+

dup(fd: number): File

复制文件描述符，并返回对应的File对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是文件描述符。

**返回值：**

类型说明[File](#ZH-CN_TOPIC_0000002529445221__file)打开的File对象。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file1 = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let fd: number = file1.fd;
let file2 = fs.dup(fd);
console.info("The name of the file2 is " + file2.name);
fs.closeSync(file1);
fs.closeSync(file2);
```

#### fs.connectDfs12+

connectDfs(networkId: string, listeners: DfsListeners): Promise<void>

业务调用connectDfs接口，触发建链。如果对端设备出现异常，业务执行回调DfsListeners内[onStatus](#ZH-CN_TOPIC_0000002529445221__onstatus12)通知应用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明networkIdstring是设备的网络Id。通过[distributedDeviceManager](@ohos.distributedDeviceManager (设备管理).md)接口调用[deviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002529285429__devicebasicinfo)获得。listeners[DfsListeners](#ZH-CN_TOPIC_0000002529445221__fsdfslisteners12)是分布式文件系统状态监听器。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Success to get available device list`);
  let networkId = deviceInfoList[0].networkId;
  let listeners: fs.DfsListeners = {
    onStatus(networkId, status) {
      console.info('onStatus');
    }
  };
  fs.connectDfs(networkId, listeners).then(() => {
    console.info("Success to connectDfs");
  }).catch((err: BusinessError) => {
    console.error(`Failed to connectDfs. Code: ${err.code}, message: ${err.message}`);
  });
}
```

#### fs.disconnectDfs12+

disconnectDfs(networkId: string): Promise<void>

业务调用disconnectDfs接口，传入networkId参数，触发断链。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明networkIdstring是设备的网络Id。通过[distributedDeviceManager](@ohos.distributedDeviceManager (设备管理).md)接口调用[deviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002529285429__devicebasicinfo)获得。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Success to get available device list`);
  let networkId = deviceInfoList[0].networkId;
  fs.disconnectDfs(networkId).then(() => {
    console.info("Success to disconnect dfs");
  }).catch((err: BusinessError) => {
    console.error(`Failed to disconnect dfs. Code: ${err.code}, message: ${err.message}`);
  })
}
```

#### fs.setxattr12+

setxattr(path: string, key: string, value: string): Promise<void>

设置文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录的应用沙箱路径。keystring是扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。valuestring是扩展属性的value。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

fs.setxattr(filePath, attrKey, attrValue).then(() => {
  console.info("Set extended attribute successfully.");
}).catch((err: BusinessError) => {
  console.error("Failed to set extended attribute with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.setxattrSync12+

setxattrSync(path: string, key: string, value: string): void

设置文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录的应用沙箱路径。keystring是扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。valuestring是扩展属性的value。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

try {
  fs.setxattrSync(filePath, attrKey, attrValue);
  console.info("Set extended attribute successfully.");
} catch (err) {
  console.error("Failed to set extended attribute with error message: " + err.message + ", error code: " + err.code);
}
```

#### fs.getxattr12+

getxattr(path: string, key: string): Promise<string>

获取文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录的应用沙箱路径。keystring是扩展属性的key。

**返回值：**

类型说明Promise<string>Promise对象。返回扩展属性的value。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

fs.getxattr(filePath, attrKey).then((attrValue: string) => {
  console.info("Get extended attribute succeed, the value is: " + attrValue);
}).catch((err: BusinessError) => {
  console.error("Failed to get extended attribute with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.getxattrSync12+

getxattrSync(path: string, key: string): string

使用同步接口获取文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录的应用沙箱路径。keystring是扩展属性的key。

**返回值：**

类型说明string返回扩展属性的value。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

try {
  let attrValue = fs.getxattrSync(filePath, attrKey);
  console.info("Get extended attribute succeed, the value is: " + attrValue);
} catch (err) {
  console.error("Failed to get extended attribute with error message: " + err.message + ", error code: " + err.code);
}
```

#### fs.mkdir

mkdir(path: string): Promise<void>

创建目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((err: BusinessError) => {
  console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.mkdir11+

mkdir(path: string, recursion: boolean): Promise<void>

创建目录，使用promise异步回调。当recursion指定为true时，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。recursionboolean是是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fs.mkdir(dirPath, true).then(() => {
  console.info("mkdir succeed");
}).catch((err: BusinessError) => {
  console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.mkdir

mkdir(path: string, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。callbackAsyncCallback<void>是异步创建目录操作完成之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.mkdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdir succeed");
  }
});
```

#### fs.mkdir11+

mkdir(path: string, recursion: boolean, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。当recursion指定为true，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。recursionboolean是是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。callbackAsyncCallback<void>是异步创建目录操作完成之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fs.mkdir(dirPath, true, (err: BusinessError) => {
  if (err) {
    console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdir succeed");
  }
});
```

#### fs.mkdirSync

mkdirSync(path: string): void

以同步方法创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let dirPath = pathDir + "/testDir";
fs.mkdirSync(dirPath);
```

#### fs.mkdirSync11+

mkdirSync(path: string, recursion: boolean): void

以同步方法创建目录。当recursion指定为true，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。recursionboolean是是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fs.mkdirSync(dirPath, true);
```

#### fs.open

open(path: string, mode?: number): Promise<File>

打开文件或目录，使用promise异步回调。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录的应用沙箱路径或文件URI。modenumber否

打开文件或目录的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，必须指定如下选项中的一个，默认以只读方式打开：

- OpenMode.READ_ONLY(0o0)：只读打开。

- OpenMode.WRITE_ONLY(0o1)：只写打开。

- OpenMode.READ_WRITE(0o2)：读写打开。

可以追加以下功能选项，以按位或的方式组合，默认情况下不追加任何额外选项。

- OpenMode.CREATE(0o100)：如果文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO方式打开文件。

**返回值：**

类型说明Promise<[File](#ZH-CN_TOPIC_0000002529445221__file)>Promise对象。返回File对象。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.open(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE).then((file: fs.File) => {
  console.info("file fd: " + file.fd);
  fs.closeSync(file);
}).catch((err: BusinessError) => {
  console.error("open file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.open

open(path: string, mode: number, callback: AsyncCallback<File>): void

打开文件或目录，可设置打开文件的选项。使用callback异步回调。

支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录的应用沙箱路径或URI。modenumber是

打开文件或目录的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，必须指定如下选项中的一个，默认以只读方式打开：

- OpenMode.READ_ONLY(0o0)：只读打开。

- OpenMode.WRITE_ONLY(0o1)：只写打开。

- OpenMode.READ_WRITE(0o2)：读写打开。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。

callbackAsyncCallback<[File](#ZH-CN_TOPIC_0000002529445221__file)>是异步打开文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.open(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE, (err: BusinessError, file: fs.File) => {
  if (err) {
    console.error("open failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("file fd: " + file.fd);
    fs.closeSync(file);
  }
});
```

#### fs.open

open(path: string, callback: AsyncCallback<File>): void

打开文件或目录，使用callback异步回调。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件或目录的应用沙箱路径或URI。callbackAsyncCallback<[File](#ZH-CN_TOPIC_0000002529445221__file)>是异步打开文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.open(filePath, (err: BusinessError, file: fs.File) => {
  if (err) {
    console.error("open failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("file fd: " + file.fd);
    fs.closeSync(file);
  }
});
```

#### fs.openSync

openSync(path: string, mode?: number): File

以同步方法打开文件或目录。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是打开文件或目录的应用沙箱路径或URI。modenumber否

打开文件或目录的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，必须指定如下选项中的一个，默认以只读方式打开：

- OpenMode.READ_ONLY(0o0)：只读打开。

- OpenMode.WRITE_ONLY(0o1)：只写打开。

- OpenMode.READ_WRITE(0o2)：读写打开。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。

**返回值：**

类型说明[File](#ZH-CN_TOPIC_0000002529445221__file)打开的File对象。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
console.info("file fd: " + file.fd);
fs.closeSync(file);
```

#### fs.read

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

读取文件数据，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。bufferArrayBuffer是用于保存读取到的文件数据的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度。

**返回值：**

类型说明Promise<number>Promise对象。返回实际读取的数据长度（单位：字节）。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fs.read(file.fd, arrayBuffer).then((readLen: number) => {
  console.info("read file data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error("read file data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

#### fs.read

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从文件读取数据，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。bufferArrayBuffer是用于保存读取到的文件数据的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度。

callbackAsyncCallback<number>是异步读取数据之后的回调。返回实际读取的数据长度，单位字节。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fs.read(file.fd, arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read file data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`The content of file: ${buf.toString()}`);
  }
  fs.closeSync(file);
});
```

#### fs.readSync

readSync(fd: number, buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。bufferArrayBuffer是用于保存读取到的文件数据的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度。

**返回值：**

类型说明number返回实际读取的数据长度（单位：字节）。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let buf = new ArrayBuffer(4096);
fs.readSync(file.fd, buf);
fs.closeSync(file);
```

#### fs.rmdir

rmdir(path: string): Promise<void>

删除目录及其所有子目录和文件，使用promise异步回调。

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.rmdir(dirPath).then(() => {
  console.info("rmdir succeed");
}).catch((err: BusinessError) => {
  console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.rmdir

rmdir(path: string, callback: AsyncCallback<void>): void

删除目录及其所有子目录和文件，使用callback异步回调。

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。callbackAsyncCallback<void>是异步删除目录之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.rmdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("rmdir succeed");
  }
});
```

#### fs.rmdirSync

rmdirSync(path: string): void

以同步方法删除目录及其所有子目录和文件。

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlinkSync接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let dirPath = pathDir + "/testDir";
fs.rmdirSync(dirPath);
```

#### fs.unlink

unlink(path: string): Promise<void>

删除单个文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的应用沙箱路径。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.unlink(filePath).then(() => {
  console.info("remove file succeed");
}).catch((err: BusinessError) => {
  console.error("remove file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.unlink

unlink(path: string, callback: AsyncCallback<void>): void

删除文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的应用沙箱路径。callbackAsyncCallback<void>是异步删除文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.unlink(filePath, (err: BusinessError) => {
  if (err) {
    console.error("remove file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("remove file succeed");
  }
});
```

#### fs.unlinkSync

unlinkSync(path: string): void

以同步方法删除文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的应用沙箱路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
fs.unlinkSync(filePath);
```

#### fs.write

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- offset，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写入。

- length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。

**返回值：**

类型说明Promise<number>Promise对象。返回实际写入的数据长度（单位：字节）。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
fs.write(file.fd, str).then((writeLen: number) => {
  console.info("write data to file succeed and size is:" + writeLen);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

#### fs.write

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- offset，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。

- length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。

callbackAsyncCallback<number>是异步将数据写入完成后执行的回调函数。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
fs.write(file.fd, str, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error("write data to file failed with error message:" + err.message + ", error code: " + err.code);
  } else {
    console.info("write data to file succeed and size is:" + writeLen);
  }
  fs.closeSync(file);
});
```

#### fs.writeSync

writeSync(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- offset，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。

- length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。

**返回值：**

类型说明number返回实际写入的数据长度（单位：字节）。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
let writeLen = fs.writeSync(file.fd, str);
console.info("write data to file succeed and size is:" + writeLen);
fs.closeSync(file);
```

#### fs.truncate

truncate(file: string | number, len?: number): Promise<void>

截断文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | number是文件的应用沙箱路径或已打开的文件描述符fd。lennumber否文件截断后的长度（单位：字节）。默认为0。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let len: number = 5;
fs.truncate(filePath, len).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.truncate

truncate(file: string | number, len?: number, callback: AsyncCallback<void>): void

截断文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | number是文件的应用沙箱路径或已打开的文件描述符fd。lennumber否文件截断后的长度，以字节为单位。默认为0。callbackAsyncCallback<void>是回调函数，本调用无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let len: number = 5;
fs.truncate(filePath, len, (err: BusinessError) => {
  if (err) {
    console.error("truncate failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("truncate succeed");
  }
});
```

#### fs.truncateSync

truncateSync(file: string | number, len?: number): void

以同步方法截断文件内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | number是文件的应用沙箱路径或已打开的文件描述符fd。lennumber否文件截断后的长度（单位：字节）。默认为0。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let len: number = 5;
fs.truncateSync(filePath, len);
```

#### fs.readLines11+

readLines(filePath: string, options?: Options): Promise<ReaderIterator>

逐行读取文件文本内容，使用promise异步回调。只支持读取utf-8格式文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filePathstring是文件的应用沙箱路径。options[Options](#ZH-CN_TOPIC_0000002529445221__options11)否

可选项。支持以下选项：

- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

**返回值：**

类型说明Promise<[ReaderIterator](#ZH-CN_TOPIC_0000002529445221__readeriterator11)>Promise对象。返回文件读取迭代器。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fs.readLines(filePath, options).then((readerIterator: fs.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info("content: " + it.value);
  }
}).catch((err: BusinessError) => {
  console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.readLines11+

readLines(filePath: string, options?: Options, callback: AsyncCallback<ReaderIterator>): void

逐行读取文件文本内容，使用callback异步回调，只支持读取utf-8格式文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filePathstring是文件的应用沙箱路径。options[Options](#ZH-CN_TOPIC_0000002529445221__options11)否

可选项。支持以下选项：

- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

callbackAsyncCallback<[ReaderIterator](#ZH-CN_TOPIC_0000002529445221__readeriterator11)>是逐行读取文件文本内容回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fs.readLines(filePath, options, (err: BusinessError, readerIterator: fs.ReaderIterator) => {
  if (err) {
    console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
      console.info("content: " + it.value);
    }
  }
});
```

#### fs.readLinesSync11+

readLinesSync(filePath: string, options?: Options): ReaderIterator

以同步方式逐行读取文件的文本内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filePathstring是文件的应用沙箱路径。options[Options](#ZH-CN_TOPIC_0000002529445221__options11)否

可选项。支持以下选项：

- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

**返回值：**

类型说明[ReaderIterator](#ZH-CN_TOPIC_0000002529445221__readeriterator11)返回文件读取迭代器。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
let readerIterator = fs.readLinesSync(filePath, options);
for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
  console.info("content: " + it.value);
}
```

#### ReaderIterator11+

文件读取迭代器。在调用ReaderIterator的方法前，需要先通过readLines方法（同步或异步）来构建一个ReaderIterator实例。

#### next11+

next(): ReaderIteratorResult

获取迭代器下一项内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明[ReaderIteratorResult](#ZH-CN_TOPIC_0000002529445221__readeriteratorresult11)文件读取迭代器返回结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

如果ReaderIterator读取的当前行的编码方式不是'utf-8'，接口返回错误码13900037。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fs.readLines(filePath, options).then((readerIterator: fs.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info("content: " + it.value);
  }
}).catch((err: BusinessError) => {
  console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### ReaderIteratorResult11+

文件读取迭代器返回结果，支持ReaderIterator接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型说明doneboolean迭代器是否已完成迭代。true：已完成迭代；false：未完成迭代。valuestring逐行读取的文件文本内容。

#### fs.readText

readText(filePath: string, options?: ReadTextOptions): Promise<string>

基于文本方式读取文件（即直接读取文件的文本内容），使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filePathstring是文件的应用沙箱路径。options[ReadTextOptions](#ZH-CN_TOPIC_0000002529445221__readtextoptions11)否

支持如下选项：

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读取。

- length，number类型，表示期望读取数据的长度。可选，默认文件长度。

- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

**返回值：**

类型说明Promise<string>Promise对象。返回读取文件的内容。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.readText(filePath).then((str: string) => {
  console.info("readText succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("readText failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.readText

readText(filePath: string, options?: ReadTextOptions, callback: AsyncCallback<string>): void

基于文本方式读取文件内容，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filePathstring是文件的应用沙箱路径。options[ReadTextOptions](#ZH-CN_TOPIC_0000002529445221__readtextoptions11)否

支持如下选项：

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读取。

- length，number类型，表示期望读取数据的长度。可选，默认文件长度。

- encoding，string类型，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

callbackAsyncCallback<string>是回调函数，返回读取文件的内容。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadTextOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stat = fs.statSync(filePath);
let readTextOption: ReadTextOptions = {
    offset: 1,
    length: stat.size,
    encoding: 'utf-8'
};
fs.readText(filePath, readTextOption, (err: BusinessError, str: string) => {
  if (err) {
    console.error("readText failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("readText succeed:" + str);
  }
});
```

#### fs.readTextSync

readTextSync(filePath: string, options?: ReadTextOptions): string

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filePathstring是文件的应用沙箱路径。options[ReadTextOptions](#ZH-CN_TOPIC_0000002529445221__readtextoptions11)否

支持如下选项：

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读取。

- length，number类型，表示期望读取数据的长度。可选，默认文件长度。

- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

**返回值：**

类型说明string返回读取文件的内容。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs, ReadTextOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let readTextOptions: ReadTextOptions = {
  offset: 1,
  length: 0,
  encoding: 'utf-8'
};
let stat = fs.statSync(filePath);
readTextOptions.length = stat.size;
let str = fs.readTextSync(filePath, readTextOptions);
console.info("readText succeed:" + str);
```

#### fs.lstat

lstat(path: string): Promise<Stat>

获取链接文件信息，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是

文件的应用沙箱路径path或URI。

**说明**：从API version 22开始，支持传入URI。

**返回值：**

类型说明Promise<[Stat](#ZH-CN_TOPIC_0000002529445221__stat)>Promise对象。返回Stat对象，表示文件的具体信息，详情见Stat。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/linkToFile";
fs.lstat(filePath).then((stat: fs.Stat) => {
  console.info("lstat succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("lstat failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.lstat

lstat(path: string, callback: AsyncCallback<Stat>): void

获取链接文件信息，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是

文件的应用沙箱路径path或URI。

**说明**：从API version 22开始，支持传入URI。

callbackAsyncCallback<[Stat](#ZH-CN_TOPIC_0000002529445221__stat)>是异步获取文件具体信息之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/linkToFile";
fs.lstat(filePath, (err: BusinessError, stat: fs.Stat) => {
  if (err) {
    console.error("lstat failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("lstat succeed, the size of file is " + stat.size);
  }
});
```

#### fs.lstatSync

lstatSync(path: string): Stat

以同步方法获取链接文件信息。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是

文件的应用沙箱路径path或URI。

**说明**：从API version 22开始，支持传入URI。

**返回值：**

类型说明[Stat](#ZH-CN_TOPIC_0000002529445221__stat)表示文件的具体信息。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/linkToFile";
let fileStat = fs.lstatSync(filePath);
console.info("lstat succeed, the size of file is " + fileStat.size);
```

#### fs.rename

rename(oldPath: string, newPath: string): Promise<void>

重命名文件或目录，使用promise异步回调。

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明oldPathstring是文件的应用沙箱原路径。newPathstring是文件的应用沙箱新路径。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fs.rename(srcFile, dstFile).then(() => {
  console.info("rename succeed");
}).catch((err: BusinessError) => {
  console.error("rename failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.rename

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

重命名文件或目录，使用callback异步回调。

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明oldPathstring是文件的应用沙箱原路径。newPathstring是文件的应用沙箱新路径。callbackAsyncCallback<void>是异步重命名文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fs.rename(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error("rename failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("rename succeed");
  }
});
```

#### fs.renameSync

renameSync(oldPath: string, newPath: string): void

以同步方法重命名文件或目录。

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明oldPathstring是文件的应用沙箱原路径。newPathstring是文件的应用沙箱新路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fs.renameSync(srcFile, dstFile);
```

#### fs.fsync

fsync(fd: number): Promise<void>

将文件系统缓存数据写入磁盘，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fsync(file.fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

#### fs.fsync

fsync(fd: number, callback: AsyncCallback<void>): void

将文件系统缓存数据写入磁盘，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。callbackAsyncCallback<void>是异步将文件数据同步之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fsync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error("fsync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("fsync succeed");
  }
  fs.closeSync(file);
});
```

#### fs.fsyncSync

fsyncSync(fd: number): void

以同步方法将文件系统缓存数据写入磁盘。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fsyncSync(file.fd);
fs.closeSync(file);
```

#### fs.fdatasync

fdatasync(fd: number): Promise<void>

实现文件内容数据同步，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdatasync(file.fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

#### fs.fdatasync

fdatasync(fd: number, callback: AsyncCallback<void>): void

实现文件内容数据同步，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。callbackAsyncCallback<void>是异步将文件内容数据同步之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdatasync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error("fdatasync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("fdatasync succeed");
  }
  fs.closeSync(file);
});
```

#### fs.fdatasyncSync

fdatasyncSync(fd: number): void

以同步方法实现文件内容的数据同步。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdatasyncSync(file.fd);
fs.closeSync(file);
```

#### fs.symlink

symlink(target: string, srcPath: string): Promise<void>

基于文件路径创建符号链接，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明targetstring是要链接的目标文件的应用沙箱路径。srcPathstring是符号链接文件的应用沙箱路径。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fs.symlink(srcFile, dstFile).then(() => {
  console.info("symlink succeed");
}).catch((err: BusinessError) => {
  console.error("symlink failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.symlink

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

基于文件路径创建符号链接，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明targetstring是要链接的目标文件的应用沙箱路径。srcPathstring是符号链接文件的应用沙箱路径。callbackAsyncCallback<void>是异步创建符号链接信息之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fs.symlink(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error("symlink failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("symlink succeed");
  }
});
```

#### fs.symlinkSync

symlinkSync(target: string, srcPath: string): void

以同步的方法基于文件路径创建符号链接。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明targetstring是要链接的目标文件的应用沙箱路径。srcPathstring是符号链接文件的应用沙箱路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fs.symlinkSync(srcFile, dstFile);
```

#### fs.listFile

listFile(path: string, options?: ListFileOptions): Promise<string[]>

默认列出当前目录下所有文件名和目录名。支持过滤。使用promise异步回调。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。options[ListFileOptions](#ZH-CN_TOPIC_0000002529445221__listfileoptions11)否文件过滤选项。默认不进行过滤。

**返回值：**

类型说明Promise<string[]>Promise对象。返回文件名数组。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
}
fs.listFile(pathDir, listFileOption).then((filenames: Array<string>) => {
  console.info("listFile succeed");
  for (let i = 0; i < filenames.length; i++) {
    console.info("fileName: %s", filenames[i]);
  }
}).catch((err: BusinessError) => {
  console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.listFile

listFile(path: string, options?: ListFileOptions, callback: AsyncCallback<string[]>): void

默认列出当前目录下所有文件名和目录名。支持过滤。使用callback异步回调。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。options[ListFileOptions](#ZH-CN_TOPIC_0000002529445221__listfileoptions11)否文件过滤选项。默认不进行过滤。callbackAsyncCallback<string[]>是异步列出文件名数组之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
};
fs.listFile(pathDir, listFileOption, (err: BusinessError, filenames: Array<string>) => {
  if (err) {
    console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("listFile succeed");
    for (let i = 0; i < filenames.length; i++) {
      console.info("filename: %s", filenames[i]);
    }
  }
});
```

#### fs.listFileSync

listFileSync(path: string, options?: ListFileOptions): string[]

默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是目录的应用沙箱路径。options[ListFileOptions](#ZH-CN_TOPIC_0000002529445221__listfileoptions11)否文件过滤选项。默认不进行过滤。

**返回值：**

类型说明string[]返回文件名数组。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs, Filter, ListFileOptions} from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
};
let filenames = fs.listFileSync(pathDir, listFileOption);
console.info("listFile succeed");
for (let i = 0; i < filenames.length; i++) {
  console.info("filename: %s", filenames[i]);
}
```

#### fs.lseek11+

lseek(fd: number, offset: number, whence?: WhenceType): number

调整文件偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是文件描述符。offsetnumber是相对偏移位置，单位为字节。whence[WhenceType](#ZH-CN_TOPIC_0000002529445221__whencetype11)否偏移指针相对位置类型。不指定则默认为文件起始位置处。

**返回值：**

类型说明number当前文件偏移指针位置（相对于文件头的偏移量，单位为字节）。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
console.info('The current offset is at ' + fs.lseek(file.fd, 5, fs.WhenceType.SEEK_SET));
fs.closeSync(file);
```

#### fs.moveDir10+

moveDir(src: string, dest: string, mode?: number): Promise<void>

移动源目录至目标路径下，使用promise异步回调。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。modenumber否

移动模式，默认值为0。

- mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的非空目录，则抛出异常。

- mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>形式提供。

- mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

- mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下的所有原始文件将被删除。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fs.moveDir(srcPath, destPath, 1).then(() => {
  console.info("move directory succeed");
}).catch((err: BusinessError) => {
  console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.moveDir10+

moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

移动源目录至目标路径下，支持设置移动模式。使用callback异步回调。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。modenumber是

移动模式，默认值为0。

- mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。

- mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>形式提供。

- mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

- mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。

callbackAsyncCallback<void, Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>>是异步移动目录之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fs.moveDir(srcPath, destPath, 1, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move directory succeed");
  }
});
```

#### fs.moveDir10+

moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

移动源目录至目标路径下。使用callback异步回调。

移动模式为目录级别抛异常。当目标目录下存在与源目录名冲突的目录，则抛出异常。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。callbackAsyncCallback<void, Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>>是异步移动目录之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fs.moveDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move directory succeed");
  }
});
```

#### fs.moveDirSync10+

moveDirSync(src: string, dest: string, mode?: number): void

以同步方法移动源目录至目标路径下。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源目录的应用沙箱路径。deststring是目标目录的应用沙箱路径。modenumber否

移动模式，默认值为0。

- mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。

- mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#ZH-CN_TOPIC_0000002529445221__conflictfiles10)>形式提供。

- mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

- mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
try {
  fs.moveDirSync(srcPath, destPath, 1);
  console.info("move directory succeed");
} catch (error) {
  let err: BusinessError<Array<ConflictFiles>> = error as BusinessError<Array<ConflictFiles>>;
  if (err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  }
}
```

#### fs.moveFile

moveFile(src: string, dest: string, mode?: number): Promise<void>

移动文件，使用promise异步回调。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源文件的应用沙箱路径。deststring是目标文件的应用沙箱路径。modenumber否移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, 0).then(() => {
  console.info("move file succeed");
}).catch((err: BusinessError) => {
  console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.moveFile

moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void

移动文件，支持设置移动模式。使用callback异步回调。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源文件的应用沙箱路径。deststring是目标文件的应用沙箱路径。modenumber是移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。callbackAsyncCallback<void>是异步移动文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, 0, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});
```

#### fs.moveFile

moveFile(src: string, dest: string, callback: AsyncCallback<void>): void

移动文件。如果移动位置存在同名文件，将强制覆盖。使用callback异步回调。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源文件的应用沙箱路径。deststring是目标文件的应用沙箱路径。callbackAsyncCallback<void>是异步移动文件之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});
```

#### fs.moveFileSync

moveFileSync(src: string, dest: string, mode?: number): void

以同步方式移动文件。

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明srcstring是源文件的应用沙箱路径。deststring是目标文件的应用沙箱路径。modenumber否移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFileSync(srcPath, destPath, 0);
console.info("move file succeed");
```

#### fs.mkdtemp

mkdtemp(prefix: string): Promise<string>

创建临时目录，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明prefixstring是指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。

**返回值：**

类型说明Promise<string>Promise对象。返回生成的唯一目录路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
fs.mkdtemp(pathDir + "/XXXXXX").then((dir: string) => {
  console.info("mkdtemp succeed:" + dir);
}).catch((err: BusinessError) => {
  console.error("mkdtemp failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.mkdtemp

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

创建临时目录，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明prefixstring是指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。callbackAsyncCallback<string>是异步创建临时目录之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
fs.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  if (err) {
    console.error("mkdtemp failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdtemp succeed");
  }
});
```

#### fs.mkdtempSync

mkdtempSync(prefix: string): string

以同步的方法创建临时目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明prefixstring是指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。

**返回值：**

类型说明string产生的唯一目录路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let res = fs.mkdtempSync(pathDir + "/XXXXXX");
```

#### fs.utimes11+

utimes(path: string, mtime: number): void

更改文件上次修改该文件的时间。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的应用沙箱路径。mtimenumber是待更新的时间戳。自1970年1月1日起至目标时间的毫秒数。仅支持更改上次修改该文件的时间属性。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.writeSync(file.fd, 'test data');
fs.closeSync(file);
fs.utimes(filePath, new Date().getTime());
```

#### fs.createRandomAccessFile10+

createRandomAccessFile(file: string | File, mode?: number): Promise<RandomAccessFile>

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | [File](#ZH-CN_TOPIC_0000002529445221__file)是文件的应用沙箱路径或已打开的File对象。modenumber否

创建文件RandomAccessFile对象的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

- OpenMode.READ_ONLY(0o0)：只读创建。

- OpenMode.WRITE_ONLY(0o1)：只写创建。

- OpenMode.READ_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path未指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

**返回值：**

类型说明Promise<[RandomAccessFile](#ZH-CN_TOPIC_0000002529445221__randomaccessfile10)>Promise对象。返回RandomAccessFile对象的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.createRandomAccessFile(file).then((randomAccessFile: fs.RandomAccessFile) => {
  console.info("randomAccessFile fd: " + randomAccessFile.fd);
  randomAccessFile.close();
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

#### fs.createRandomAccessFile10+

createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void

基于文件路径或文件对象，以只读方式创建RandomAccessFile对象，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | [File](#ZH-CN_TOPIC_0000002529445221__file)是文件的应用沙箱路径或已打开的File对象。callbackAsyncCallback<[RandomAccessFile](#ZH-CN_TOPIC_0000002529445221__randomaccessfile10)>是异步创建RandomAccessFile对象之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.createRandomAccessFile(file, (err: BusinessError, randomAccessFile: fs.RandomAccessFile) => {
  if (err) {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  }
  fs.closeSync(file);
});
```

#### fs.createRandomAccessFile10+

createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void

基于文件路径或文件对象创建RandomAccessFile对象，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | [File](#ZH-CN_TOPIC_0000002529445221__file)是文件的应用沙箱路径或已打开的File对象。modenumber是

创建文件RandomAccessFile对象的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

- OpenMode.READ_ONLY(0o0)：只读创建。

- OpenMode.WRITE_ONLY(0o1)：只写创建。

- OpenMode.READ_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

callbackAsyncCallback<[RandomAccessFile](#ZH-CN_TOPIC_0000002529445221__randomaccessfile10)>是异步创建RandomAccessFile对象之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.createRandomAccessFile(file, fs.OpenMode.READ_ONLY, (err: BusinessError, randomAccessFile: fs.RandomAccessFile) => {
  if (err) {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  }
  fs.closeSync(file);
});
```

#### fs.createRandomAccessFile12+

createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | [File](#ZH-CN_TOPIC_0000002529445221__file)是文件的应用沙箱路径或已打开的File对象。modenumber否

创建文件RandomAccessFile对象的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

- OpenMode.READ_ONLY(0o0)：只读创建。

- OpenMode.WRITE_ONLY(0o1)：只写创建。

- OpenMode.READ_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

options[RandomAccessFileOptions](#ZH-CN_TOPIC_0000002529445221__randomaccessfileoptions12)否

支持如下选项：

- start，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

- end，number类型，表示期望读取结束的位置。可选，默认文件末尾。

此选项仅对[getreadstream](#ZH-CN_TOPIC_0000002529445221__getreadstream12)及[getwritestream](#ZH-CN_TOPIC_0000002529445221__getwritestream12)获取的文件流对象生效。

**返回值：**

类型说明Promise<[RandomAccessFile](#ZH-CN_TOPIC_0000002529445221__randomaccessfile10)>Promise对象。返回RandomAccessFile对象的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.createRandomAccessFile(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE, { start: 10, end: 100 })
  .then((randomAccessFile: fs.RandomAccessFile) => {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  })
  .catch((err: BusinessError) => {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  });
```

#### fs.createRandomAccessFileSync10+

createRandomAccessFileSync(file: string | File, mode?: number): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | [File](#ZH-CN_TOPIC_0000002529445221__file)是文件的应用沙箱路径或已打开的File对象。modenumber否

创建文件RandomAccessFile对象的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

- OpenMode.READ_ONLY(0o0)：只读创建。

- OpenMode.WRITE_ONLY(0o1)：只写创建。

- OpenMode.READ_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

**返回值：**

类型说明[RandomAccessFile](#ZH-CN_TOPIC_0000002529445221__randomaccessfile10)返回RandomAccessFile对象。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
randomAccessFile.close();
```

#### fs.createRandomAccessFileSync12+

createRandomAccessFileSync(file: string | File, mode?: number,

options?: RandomAccessFileOptions): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filestring | [File](#ZH-CN_TOPIC_0000002529445221__file)是文件的应用沙箱路径或已打开的File对象。modenumber否

创建文件RandomAccessFile对象的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

- OpenMode.READ_ONLY(0o0)：只读创建。

- OpenMode.WRITE_ONLY(0o1)：只写创建。

- OpenMode.READ_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

options[RandomAccessFileOptions](#ZH-CN_TOPIC_0000002529445221__randomaccessfileoptions12)否

支持如下选项：

- start，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

- end，number类型，表示期望读取结束的位置。可选，默认文件末尾。

此选项仅对[getreadstream](#ZH-CN_TOPIC_0000002529445221__getreadstream12)及[getwritestream](#ZH-CN_TOPIC_0000002529445221__getwritestream12)获取的文件流对象生效。

**返回值：**

类型说明[RandomAccessFile](#ZH-CN_TOPIC_0000002529445221__randomaccessfile10)返回RandomAccessFile对象。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE,
  { start: 10, end: 100 });
randomAccessFile.close();
```

#### fs.createStream

createStream(path: string, mode: string): Promise<Stream>

基于文件路径创建文件流，使用promise异步回调。需要配合[Stream](#ZH-CN_TOPIC_0000002529445221__stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的应用沙箱路径。modestring是

- r：打开只读文件，该文件必须存在。

- r+：打开可读写的文件，该文件必须存在。

- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

**返回值：**

类型说明Promise<[Stream](#ZH-CN_TOPIC_0000002529445221__stream)>Promise对象。返回文件流的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.createStream(filePath, "a+").then((stream: fs.Stream) => {
  stream.closeSync();
  console.info("createStream succeed");
}).catch((err: BusinessError) => {
  console.error("createStream failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fs.createStream

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

基于文件路径创建文件流，使用callback异步回调。需要配合[Stream](#ZH-CN_TOPIC_0000002529445221__stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的应用沙箱路径。modestring是

- r：打开只读文件，该文件必须存在。

- r+：打开可读写的文件，该文件必须存在。

- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

callbackAsyncCallback<[Stream](#ZH-CN_TOPIC_0000002529445221__stream)>是异步打开文件流之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.createStream(filePath, "r+", (err: BusinessError, stream: fs.Stream) => {
  if (err) {
    console.error("create stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    stream.closeSync();
    console.info("createStream succeed");
  }
})
```

#### fs.createStreamSync

createStreamSync(path: string, mode: string): Stream

以同步方法基于文件路径创建文件流。需要配合[Stream](#ZH-CN_TOPIC_0000002529445221__stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的应用沙箱路径。modestring是

- r：打开只读文件，该文件必须存在。

- r+：打开可读写的文件，该文件必须存在。

- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

**返回值：**

类型说明[Stream](#ZH-CN_TOPIC_0000002529445221__stream)返回文件流的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
console.info("createStream succeed");
stream.closeSync();
```

#### fs.fdopenStream

fdopenStream(fd: number, mode: string): Promise<Stream>

基于文件描述符打开文件流，使用promise异步回调。需要配合[Stream](#ZH-CN_TOPIC_0000002529445221__stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。modestring是

- r：打开只读文件，该文件必须存在。

- r+：打开可读写的文件，该文件必须存在。

- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

**返回值：**

类型说明Promise<[Stream](#ZH-CN_TOPIC_0000002529445221__stream)>Promise对象。返回文件流的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdopenStream(file.fd, "r+").then((stream: fs.Stream) => {
  console.info("openStream succeed");
  stream.closeSync();
}).catch((err: BusinessError) => {
  console.error("openStream failed with error message: " + err.message + ", error code: " + err.code);
  // 文件流打开失败后，文件描述符需要手动关闭
  fs.closeSync(file);
});
```

使用文件描述符创建的文件流时，文件描述符的生命周期将由文件流对象管理。调用文件流的close()函数后，初始的文件描述符也会被关闭。

#### fs.fdopenStream

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

基于文件描述符打开文件流，使用callback异步回调。需要配合[Stream](#ZH-CN_TOPIC_0000002529445221__stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。modestring是

- r：打开只读文件，该文件必须存在。

- r+：打开可读写的文件，该文件必须存在。

- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

callbackAsyncCallback<[Stream](#ZH-CN_TOPIC_0000002529445221__stream)>是异步打开文件流之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
fs.fdopenStream(file.fd, "r+", (err: BusinessError, stream: fs.Stream) => {
  if (err) {
    console.error("fdopen stream failed with error message: " + err.message + ", error code: " + err.code);
    // 文件流打开失败后，文件描述符需要手动关闭
    fs.closeSync(file);
  } else {
    console.info("fdopen stream succeed");
    stream.closeSync();
  }
});
```

使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。

#### fs.fdopenStreamSync

fdopenStreamSync(fd: number, mode: string): Stream

以同步方法基于文件描述符打开文件流。需要配合[Stream](#ZH-CN_TOPIC_0000002529445221__stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明fdnumber是已打开的文件描述符。modestring是

- r：打开只读文件，该文件必须存在。

- r+：打开可读写的文件，该文件必须存在。

- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

**返回值：**

类型说明[Stream](#ZH-CN_TOPIC_0000002529445221__stream)返回文件流的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY | fs.OpenMode.CREATE);
let stream = fs.fdopenStreamSync(file.fd, "r+");
stream.closeSync();
```

使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。

#### fs.createReadStream12+

createReadStream(path: string, options?: ReadStreamOptions ): ReadStream

以同步方法打开文件可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件路径。options[ReadStreamOptions](#ZH-CN_TOPIC_0000002529445221__readstreamoptions12)否

支持如下选项：

- start，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

- end，number类型，表示期望读取结束的位置。可选，默认文件末尾。

**返回值：**

类型说明[ReadStream](#ZH-CN_TOPIC_0000002529445221__readstream12)文件可读流。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
// 创建文件可读流
const rs = fs.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fs.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});
```

#### fs.createWriteStream12+

createWriteStream(path: string, options?: WriteStreamOptions): WriteStream

以同步方法打开文件可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件路径。options[WriteStreamOptions](#ZH-CN_TOPIC_0000002529445221__writestreamoptions12)否

支持如下选项：

- start，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。

- mode，number 类型，创建文件可写流的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，可选，默认以只写方式创建。

**返回值：**

类型说明[WriteStream](#ZH-CN_TOPIC_0000002529445221__writestream12)文件可写流。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
// 创建文件可读流
const rs = fs.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fs.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});
```

#### AtomicFile15+

AtomicFile是一个用于对文件进行原子读写操作的类。

在写操作时，通过写入临时文件，并在写入成功后将其重命名到原始文件位置来确保写入文件的完整性；而在写入失败时删除临时文件，不修改原始文件内容。

使用者可以自行调用finishWrite或failWrite来完成文件内容的写入或回滚。

**系统能力**：SystemCapability.FileManagement.File.FileIO

#### constructor15+

constructor(path: string)

对于给定路径的文件创建一个AtomicFile类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是文件的沙箱路径。

#### getBaseFile15+

getBaseFile(): File

通过AtomicFile对象获取文件对象。

文件描述符fd需要由用户调用close方法关闭。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明[File](#ZH-CN_TOPIC_0000002529445221__file)打开的File对象。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)和[通用错误码](通用错误码.md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let atomicFile = new fs.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = atomicFile.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    atomicFile.finishWrite();
    let File = atomicFile.getBaseFile();
    console.info('AtomicFile getBaseFile File.fd is: ' + File.fd + ' path: ' + File.path + ' name: ' + File.name);
  })
} catch (err) {
  console.error(`Failed to get baseFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### openRead15+

openRead(): ReadStream

创建一个读文件流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明[ReadStream](#ZH-CN_TOPIC_0000002529445221__readstream12)文件可读流。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)和[通用错误码](通用错误码.md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let readStream = file.openRead();
      readStream.on('readable', () => {
        const data = readStream.read();
        if (!data) {
          console.error('AtomicFile read data is null.');
          return;
        }
        console.info('AtomicFile read data is: ' + data);
      });
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### readFully15+

readFully(): ArrayBuffer

读取文件全部内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明ArrayBuffer文件的全部内容。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)和[通用错误码](通用错误码.md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';
import { util, buffer } from '@kit.ArkTS';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      console.info('AtomicFile readFully str is: ' + str);
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### startWrite15+

startWrite(): WriteStream

对文件开始新的写入操作。将返回一个WriteStream，用于在其中写入新的文件数据。

当文件不存在时新建文件。

在写入文件完成后，写入成功需要调用finishWrite()，写入失败需要调用failWrite()。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明[WriteStream](#ZH-CN_TOPIC_0000002529445221__writestream12)文件可写流。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)和[通用错误码](通用错误码.md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    console.info('AtomicFile write finished!');
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### finishWrite15+

finishWrite(): void

在完成对startWrite返回流的写入操作时调用，表示文件写入成功。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)和[通用错误码](通用错误码.md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### failWrite15+

failWrite(): void

文件写入失败后调用，将执行文件回滚操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)和[通用错误码](通用错误码.md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let file = new fs.AtomicFile(`${pathDir}/write.txt`);
try {
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    console.info('AtomicFile write succeed!');
  })
} catch (err) {
  file.failWrite();
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### delete15+

delete(): void

删除AtomicFile类，会删除原始文件和临时文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)和[通用错误码](通用错误码.md)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';
import { util } from '@kit.ArkTS';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      console.info('AtomicFile readFully str is: ' + str);
      file.delete();
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### fs.createWatcher10+

createWatcher(path: string, events: number, listener: WatchEventListener): Watcher

创建Watcher对象，监听文件或目录变动。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是监听文件或目录的沙箱路径。eventsnumber是

监听变动的事件集，多个事件通过或(|)的方式进行集合。

- 0x1: IN_ACCESS， 文件被访问。

- 0x2: IN_MODIFY，文件内容被修改。

- 0x4: IN_ATTRIB，文件元数据被修改。

- 0x8: IN_CLOSE_WRITE，文件在打开时进行了写操作，然后被关闭。

- 0x10: IN_CLOSE_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。

- 0x20: IN_OPEN，文件或目录被打开。

- 0x40: IN_MOVED_FROM，监听目录中文件被移动走。

- 0x80: IN_MOVED_TO，监听目录中文件被移动过来。

- 0x100: IN_CREATE，监听目录中文件或子目录被创建。

- 0x200: IN_DELETE，监听目录中文件或子目录被删除。

- 0x400: IN_DELETE_SELF，监听的目录被删除，删除后监听停止。

- 0x800: IN_MOVE_SELF，监听的文件或目录被移动，移动后监听继续。

- 0xfff: IN_ALL_EVENTS，监听以上所有事件。

listener[WatchEventListener](#ZH-CN_TOPIC_0000002529445221__watcheventlistener10)是监听事件发生后的回调。监听事件每发生一次，回调一次。

**返回值：**

类型说明[Watcher](#ZH-CN_TOPIC_0000002529445221__watcher10)返回Watcher对象。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { fileIo as fs, WatchEvent } from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let watcher = fs.createWatcher(filePath, 0x2 | 0x10, (watchEvent: WatchEvent) => {
  if (watchEvent.event == 0x2) {
    console.info(watchEvent.fileName + 'was modified');
  } else if (watchEvent.event == 0x10) {
    console.info(watchEvent.fileName + 'was closed');
  }
});
watcher.start();
fs.writeSync(file.fd, 'test');
fs.closeSync(file);
watcher.stop();
```

#### WatchEventListener10+

(event: WatchEvent): void

事件监听类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明event[WatchEvent](#ZH-CN_TOPIC_0000002529445221__watchevent10)是回调的事件类。

#### WatchEvent10+

事件类

#### 属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明fileNamestring是否发生监听事件对应文件的沙箱路径，该沙箱路径包含文件名称。eventnumber是否

监听变动的事件集，多个事件通过或(|)的方式进行集合。

- 0x1: IN_ACCESS， 文件被访问。

- 0x2: IN_MODIFY，文件内容被修改。

- 0x4: IN_ATTRIB，文件元数据被修改。

- 0x8: IN_CLOSE_WRITE，文件在打开时进行了写操作，然后被关闭。

- 0x10: IN_CLOSE_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。

- 0x20: IN_OPEN，文件或目录被打开。

- 0x40: IN_MOVED_FROM，监听目录中文件被移动走。

- 0x80: IN_MOVED_TO，监听目录中文件被移动过来。

- 0x100: IN_CREATE，监听目录中文件或子目录被创建。

- 0x200: IN_DELETE，监听目录中文件或子目录被删除。

- 0x400: IN_DELETE_SELF，监听的目录被删除，删除后监听停止。

- 0x800: IN_MOVE_SELF，监听的文件或目录被移动，移动后监听继续。

- 0xfff: IN_ALL_EVENTS，监听以上所有事件。

cookienumber是否绑定相关事件的cookie。当前仅支持事件IN_MOVED_FROM与IN_MOVED_TO，同一个文件的移动事件IN_MOVED_FROM和IN_MOVED_TO具有相同的cookie值。

#### Progress11+

拷贝进度回调数据

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明processedSizenumber是否已拷贝的数据大小。totalSizenumber是否待拷贝的数据总大小。

#### TaskSignal12+

拷贝中断信号。

**系统能力**：SystemCapability.FileManagement.File.FileIO

#### cancel12+

cancel(): void

取消拷贝任务。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { fileUri } from '@kit.CoreFileKit';
import common from '@ohos.app.ability.common';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";
let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);
let copySignal = new fs.TaskSignal;
let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
  console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
  if (progress.processedSize / progress.totalSize > 0.5) {
    copySignal.cancel();
    console.info("copy cancel.");
  }
};
let options: fs.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}

try {
  fs.copy(srcDirUriLocal, dstDirUriLocal, options, (err: BusinessError) => {
    if (err) {
      console.error("copy fail, err: ", err.message);
      return;
    }
    console.info("copy success.");
  })
} catch (err) {
  console.error("copyFileWithCancel failed, err: ", err.message);
}
```

#### onCancel12+

onCancel(): Promise<string>

取消拷贝事件监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明Promise<string>Promise对象。最后一个拷贝的文件路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { TaskSignal } from '@ohos.file.fs';
let copySignal: fs.TaskSignal = new TaskSignal();
copySignal.onCancel();
```

#### CopyOptions11+

拷贝进度回调监听

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明progressListener[ProgressListener](#ZH-CN_TOPIC_0000002529445221__progresslistener11)否是拷贝进度监听。copySignal[TaskSignal](#ZH-CN_TOPIC_0000002529445221__tasksignal12)否是取消拷贝信号。

#### ProgressListener11+

拷贝进度监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

类型说明(progress: [Progress](#ZH-CN_TOPIC_0000002529445221__progress11)) => void拷贝进度监听

**示例：**

```ets
import { TaskSignal } from '@kit.CoreFileKit';
let copySignal: fs.TaskSignal = new TaskSignal();
let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
  console.info(`processedSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let copyOption: fs.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}
```

#### Stat

文件具体信息，在调用Stat的方法前，需要先通过[stat()](#ZH-CN_TOPIC_0000002529445221__fsstat)方法（同步或异步）构建一个Stat实例。

#### 属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明inobigint是否标识该文件。通常同设备上的不同文件的INO不同。modenumber是否

表示文件权限，各特征位的含义如下：

**说明**：以下值为八进制，取得的返回值为十进制，请换算后查看。

- 0o400：用户读。对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。

- 0o200：用户写。对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。

- 0o100：用户执行。对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。

- 0o040：用户组读。对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。

- 0o020：用户组写。对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。

- 0o010：用户组执行。对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。

- 0o004：其他读。对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。

- 0o002：其他写。对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。

- 0o001：其他执行。对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

uidnumber是否文件所有者的ID。gidnumber是否文件所有组的ID。sizenumber是否

文件的大小，以字节为单位。仅对普通文件有效。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

atimenumber是否

上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。

**注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

mtimenumber是否

上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

ctimenumber是否最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。atimeNs15+bigint是是

上次访问该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。

**注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。

mtimeNs15+bigint是是上次修改该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。ctimeNs15+bigint是是最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的纳秒数。location11+[LocationType](#ZH-CN_TOPIC_0000002529445221__locationtype11)是否文件的位置，表示该文件是本地文件或者云端文件。

Stat中部分属性仅支持普通文件获取，开发者可通过[isFile()](#ZH-CN_TOPIC_0000002529445221__isfile)接口判断文件是否为普通文件。

#### isBlockDevice

isBlockDevice(): boolean

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明boolean表示文件是否是块特殊设备。true：是块特殊设备；false：不是块特殊设备。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isBLockDevice = fs.statSync(filePath).isBlockDevice();
```

#### isCharacterDevice

isCharacterDevice(): boolean

判断文件是否为字符特殊文件。字符特殊设备支持随机访问，且访问时无缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明boolean表示文件是否是字符特殊设备。true：是字符特殊设备；false：不是字符特殊设备。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isCharacterDevice = fs.statSync(filePath).isCharacterDevice();
```

#### isDirectory

isDirectory(): boolean

判断文件是否为目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明boolean表示文件是否是目录。true：是目录；false：不是目录。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let dirPath = pathDir + "/test";
let isDirectory = fs.statSync(dirPath).isDirectory();
```

#### isFIFO

isFIFO(): boolean

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明boolean表示文件是否是 FIFO。true：是FIFO；false：不是FIFO。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isFIFO = fs.statSync(filePath).isFIFO();
```

#### isFile

isFile(): boolean

用于判断文件是否是普通文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明boolean表示文件是否是普通文件。true：是普通文件；false：不是普通文件。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isFile = fs.statSync(filePath).isFile();
```

#### isSocket

isSocket(): boolean

判断文件是否是套接字。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明boolean表示文件是否是套接字。true：是套接字；false：不是套接字。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isSocket = fs.statSync(filePath).isSocket();
```

#### isSymbolicLink

isSymbolicLink(): boolean

判断文件是否为符号链接。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明boolean表示文件是否是符号链接。true：是符号链接；false：不是符号链接。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let isSymbolicLink = fs.statSync(filePath).isSymbolicLink();
```

#### Stream

文件流，在调用Stream的方法前，需要先通过[fs.createStream](#ZH-CN_TOPIC_0000002529445221__fscreatestream)方法或者[fs.fdopenStream](#ZH-CN_TOPIC_0000002529445221__fsfdopenstream)（同步或异步）来构建一个Stream实例。

#### close

close(): Promise<void>

关闭文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### close

close(callback: AsyncCallback<void>): void

异步关闭文件流，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是异步关闭文件流之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.close((err: BusinessError) => {
  if (err) {
    console.error("close stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close stream succeed");
  }
});
```

#### closeSync

closeSync(): void

同步关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.closeSync();
```

#### flush

flush(): Promise<void>

刷新文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明Promise<void>Promise对象。返回表示异步刷新文件流的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flush().then(() => {
  console.info("flush succeed");
  stream.close();
}).catch((err: BusinessError) => {
  console.error("flush failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### flush

flush(callback: AsyncCallback<void>): void

异步刷新文件流，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是异步刷新文件流后的回调函数。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flush((err: BusinessError) => {
  if (err) {
    console.error("flush stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("flush succeed");
    stream.close();
  }
});
```

#### flushSync

flushSync(): void

同步刷新文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flushSync();
stream.close();
```

#### write

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入流文件，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- length，number类型，表示期望写入数据的长度。默认缓冲区长度。

- offset，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

**返回值：**

类型说明Promise<number>Promise对象。返回实际写入的长度。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption).then((number: number) => {
  console.info("write succeed and size is:" + number);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("write failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### write

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入流文件，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度。

- offset，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

callbackAsyncCallback<number>是异步写入完成后执行的回调函数。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  stream.close();
});
```

#### writeSync

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入流文件。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度。

- offset，number类型，表示期望写入文件的位置。可选，默认从当前位置开始写。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

**返回值：**

类型说明number实际写入的长度。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath,"r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let num = stream.writeSync("hello, world", writeOption);
stream.close();
```

#### read

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

从流文件读取数据，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer是用于读取文件的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度。

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

**返回值：**

类型说明Promise<number>Promise对象。返回读取的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption).then((readLen: number) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`The content of file: ${buf.toString()}`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("read data failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### read

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从流文件读取数据，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer是用于读取文件的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度。

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读取。

callbackAsyncCallback<number>是异步读取完成后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`The content of file: ${buf.toString()}`);
    stream.close();
  }
});
```

#### readSync

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从流文件读取数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer是用于读取文件的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度。

- offset，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读。

**返回值：**

类型说明number实际读取的长度。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
let buf = new ArrayBuffer(4096);
let num = stream.readSync(buf, readOption);
stream.close();
```

#### File

由open接口打开的File对象。

#### 属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明fdnumber是否

打开的文件描述符。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

path10+string是否文件路径。name10+string是否文件名。

#### getParent11+

getParent(): string

获取File对象对应文件父目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明string返回父目录路径。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
console.info('The parent path is: ' + file.getParent());
fs.closeSync(file);
```

#### lock

lock(exclusive?: boolean): Promise<void>

对文件阻塞式施加共享锁或独占锁，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明exclusiveboolean否是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。

**返回值：**

类型说明Promise<void>Promise对象。无返回值。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
file.lock(true).then(() => {
  console.info("lock file succeed");
}).catch((err: BusinessError) => {
  console.error("lock file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

#### lock

lock(exclusive?: boolean, callback: AsyncCallback<void>): void

对文件阻塞式施加共享锁或独占锁，使Callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明exclusiveboolean否是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。callbackAsyncCallback<void>是异步文件上锁之后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
file.lock(true, (err: BusinessError) => {
  if (err) {
    console.error("lock file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("lock file succeed");
  }
  fs.closeSync(file);
});
```

#### tryLock

tryLock(exclusive?: boolean): void

文件非阻塞式施加共享锁或独占锁。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明exclusiveboolean否是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
file.tryLock(true);
console.info("lock file succeed");
fs.closeSync(file);
```

#### unlock

unlock(): void

以同步方式解锁文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
file.tryLock(true);
file.unlock();
console.info("unlock file succeed");
fs.closeSync(file);
```

#### fs.DfsListeners12+

事件监听类。创建DFSListener对象，用于监听分布式文件系统状态。

**系统能力**：SystemCapability.FileManagement.File.FileIO

#### onStatus12+

onStatus(networkId: string, status: number): void;

事件回调类。参数由[connectDfs](#ZH-CN_TOPIC_0000002529445221__fsconnectdfs12)传入。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明networkIdstring是设备的网络Id。statusnumber是

分布式文件系统的状态码（以connectDfs回调onStatus的特定错误码作为入参）。触发场景为connectDfs调用过程中出现对端设备异常，对应错误码为：

- [13900046](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__13900046-软件造成连接中断)：软件造成连接中断。

#### RandomAccessFile10+

随机读写文件流。在调用RandomAccessFile的方法前，需要先通过createRandomAccessFile()方法（同步或异步）来构建一个RandomAccessFile实例。

#### 属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明fdnumber是否打开的文件描述符。filePointernumber是否RandomAccessFile对象的偏移指针。

#### setFilePointer10+

setFilePointer(filePointer:number): void

设置文件偏移指针。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明filePointernumber是RandomAccessFile对象的偏移指针。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
randomAccessFile.setFilePointer(1);
randomAccessFile.close();
```

#### close10+

close(): void

以同步方式关闭RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
randomAccessFile.close();
```

#### write10+

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入文件，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- length，number类型，表示期望写入数据的长度。默认缓冲区长度。

- offset，number类型，表示期望写入文件位置（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

**返回值：**

类型说明Promise<number>Promise对象。返回实际写入的长度。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: 5,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: number) => {
  console.info("randomAccessFile bytesWritten: " + bytesWritten);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fs.closeSync(file);
});
```

#### write10+

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- length，number类型，表示期望写入数据的长度。可选，默认为缓冲区长度。

- offset，number类型，表示期望写入文件位置（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

callbackAsyncCallback<number>是异步写入完成后执行的回调函数。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: bufferLength,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  randomAccessFile.close();
  fs.closeSync(file);
});
```

#### writeSync10+

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer | string是待写入文件的数据，可来自缓冲区或字符串。options[WriteOptions](#ZH-CN_TOPIC_0000002529445221__writeoptions11)否

支持如下选项：

- length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度。

- offset，number类型，表示期望写入文件位置（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

**返回值：**

类型说明number实际写入的长度。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let bytesWritten = randomAccessFile.writeSync("hello, world", writeOption);
randomAccessFile.close();
```

#### read10+

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

从文件读取数据，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer是用于读取文件的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- length，number类型，表示期望读取数据的长度。可选，默认为缓冲区长度。

- offset，number类型，表示期望读取文件位置（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。

**返回值：**

类型说明Promise<number>Promise对象。返回读取的结果。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.read(arrayBuffer, readOption).then((readLength: number) => {
  console.info("randomAccessFile readLength: " + readLength);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fs.closeSync(file);
});
```

#### read10+

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从文件读取数据，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer是用于读取文件的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- length，number类型，表示读取数据的长度。可选，默认为缓冲区长度。

- offset，number类型，表示读取文件位置（基于当前filePointer加上offset的位置）。可选，默认从filePointer开始读。

callbackAsyncCallback<number>是异步读取完成后的回调。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let length: number = 20;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (readLength) {
      console.info("read succeed and size is:" + readLength);
    }
  }
  randomAccessFile.close();
  fs.closeSync(file);
});
```

#### readSync10+

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明bufferArrayBuffer是用于读取文件的缓冲区。options[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)否

支持如下选项：

- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度。

- offset，number类型，表示期望读取文件位置（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。

**返回值：**

类型说明number实际读取的长度。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let length: number = 4096;
let arrayBuffer = new ArrayBuffer(length);
let readLength = randomAccessFile.readSync(arrayBuffer);
randomAccessFile.close();
fs.closeSync(file);
```

#### getReadStream12+

getReadStream(): ReadStream

获取当前 RandomAccessFile 的一个 ReadStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明[ReadStream](#ZH-CN_TOPIC_0000002529445221__readstream12)文件可读流。

**示例：**

```ets
const filePath = pathDir + "/test.txt";
const randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
const rs = randomAccessFile.getReadStream();
rs.close();
randomAccessFile.close();
```

#### getWriteStream12+

getWriteStream(): WriteStream

获取当前 RandomAccessFile 的一个 WriteStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

类型说明[WriteStream](#ZH-CN_TOPIC_0000002529445221__writestream12)文件可写流。

**示例：**

```ets
const filePath = pathDir + "/test.txt";
const randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
const ws = randomAccessFile.getWriteStream();
ws.close();
randomAccessFile.close();
```

#### Watcher10+

文件目录变化监听对象。由createWatcher接口获得。

#### start10+

start(): void

开启监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let watcher = fs.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

#### stop10+

stop(): void

停止监听并移除Watcher对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
let filePath = pathDir + "/test.txt";
let watcher = fs.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

#### OpenMode

open接口flags参数常量。文件打开标签。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型值说明READ_ONLYnumber0o0

只读打开。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

WRITE_ONLYnumber0o1

只写打开。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

READ_WRITEnumber0o2

读写打开。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

CREATEnumber0o100

若文件不存在，则创建文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

TRUNCnumber0o1000

如果文件存在且以只写或读写的方式打开，则将其长度裁剪为零。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

APPENDnumber0o2000

以追加方式打开，后续写将追加到文件末尾。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

NONBLOCKnumber0o4000如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。DIRnumber0o200000如果path不指向目录，则出错。NOFOLLOWnumber0o400000如果path指向符号链接，则出错。SYNCnumber0o4010000以同步IO的方式打开文件。

#### Filter10+

文件过滤配置项，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明suffixArray<string>否是文件后缀名完全匹配，各个关键词OR关系。displayNameArray<string>否是文件名模糊匹配，各个关键词OR关系。当前仅支持通配符*。mimeTypeArray<string>否是mime类型完全匹配，各个关键词OR关系。预留字段，暂不支持使用。fileSizeOvernumber否是文件大小匹配，大于指定大小的文件。lastModifiedAfternumber否是文件最近修改时间匹配，在指定时间点及之后的文件。excludeMediaboolean否是是否排除Media中已有的文件。true：排除Media中已有的文件；false：不排除Media中已有的文件。

#### ConflictFiles10+

冲突文件信息，支持copyDir及moveDir接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型说明srcFilestring源冲突文件路径。destFilestring目标冲突文件路径。

#### Options11+

可选项类型，支持readLines接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型说明encodingstring文件编码方式。可选项。

#### WhenceType11+

枚举，文件偏移指针相对偏移位置类型，支持lseek接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称值说明SEEK_SET0文件起始位置处。SEEK_CUR1当前文件偏移指针位置处。SEEK_END2文件末尾位置处。

#### LocationType11+

枚举，文件位置，表示该文件是否在本地或者云端存在。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称值说明LOCAL1文件在本地存在。CLOUD2文件在云端存在。

#### AccessModeType12+

枚举，表示需要校验的具体权限。若不填，默认校验文件是否存在。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称值说明EXIST0文件是否存在。WRITE2文件是否具有写入权限。READ4文件是否具有读取权限。READ_WRITE6文件是否具有读写权限。

#### AccessFlagType12+

枚举，表示需要校验的文件位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称值说明LOCAL0文件是否在本地。

#### ReadOptions11+

可选项类型，支持read接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明offsetnumber否是期望读取文件位置，单位为字节（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。lengthnumber否是期望读取数据的长度，单位为字节。可选，默认缓冲区长度。

#### ReadTextOptions11+

可选项类型，支持readText接口使用，ReadTextOptions继承至[ReadOptions](#ZH-CN_TOPIC_0000002529445221__readoptions11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明offsetnumber否是期望读取文件的位置，单位为字节。可选，默认从当前位置开始读取。lengthnumber否是期望读取数据的长度，单位为字节。可选，默认文件长度。encodingstring否是

当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

#### WriteOptions11+

可选项类型，支持write接口使用，WriteOptions继承至[Options](#ZH-CN_TOPIC_0000002529445221__options11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明offsetnumber否是

期望写入文件位置，单位为字节（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

lengthnumber否是

期望写入数据的长度，单位为字节。可选，默认缓冲区长度。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

encodingstring否是当数据是string类型时有效，表示数据的编码方式。默认 'utf-8'。仅支持 'utf-8'。

#### ListFileOptions11+

可选项类型，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明recursionboolean否是是否递归子目录下文件名。可选，默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及目录名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。listNumnumber否是列出文件名数量。可选，当设置0时，列出所有文件，默认为0。filter[Filter](#ZH-CN_TOPIC_0000002529445221__filter10)否是文件过滤配置项。 可选，设置过滤条件。

#### ReadStream12+

文件可读流，需要先通过[fs.createReadStream](#ZH-CN_TOPIC_0000002529445221__fscreatereadstream12)方法来构建一个ReadStream实例。ReadStream继承自数据流基类[stream](zh-cn_topic_0000002497444782.html#ZH-CN_TOPIC_0000002497444782__readable)。

**规格**：ReadStream读到的数据为解码后的字符串，其编码格式当前仅支持'utf-8'。

名称类型只读可选说明bytesReadnumber是否可读流已经读取的字节数。pathstring是否当前可读流对应的文件路径。

#### seek12+

seek(offset: number, whence?: WhenceType): number

调整可读流偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明offsetnumber是相对偏移位置，单位为字节。whence[WhenceType](#ZH-CN_TOPIC_0000002529445221__whencetype11)否偏移指针相对位置类型。默认值：SEEK_SET，文件起始位置处。

**返回值：**

类型说明number当前可读流偏移指针位置（相对于文件头的偏移量，单位为字节）。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
const filePath = pathDir + "/test.txt";
const rs = fs.createReadStream(filePath);
const curOff = rs.seek(5, fs.WhenceType.SEEK_SET);
console.info(`current offset is ${curOff}`);
rs.close();
```

#### close12+

close(): void

关闭可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
const filePath = pathDir + "/test.txt";
const rs = fs.createReadStream(filePath);
rs.close();
```

#### WriteStream12+

文件可写流，需要先通过[fs.createWriteStream](#ZH-CN_TOPIC_0000002529445221__fscreatewritestream12)方法来构建一个WriteStream实例。WriteStream继承自数据流基类[stream](zh-cn_topic_0000002497444782.html#ZH-CN_TOPIC_0000002497444782__writable)。

#### 属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明bytesWrittennumber是否可写流已经写入的字节数。pathstring是否当前可写流对应的文件路径。

#### Seek12+

seek(offset: number, whence?: WhenceType): number;

调整可写流的偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明offsetnumber是相对偏移位置，单位为字节。whence[WhenceType](#ZH-CN_TOPIC_0000002529445221__whencetype11)否偏移指针相对位置类型。默认值：SEEK_SET，文件起始位置处。

**返回值：**

类型说明number当前可写流偏移指针位置（相对于文件头的偏移量，单位为字节）。

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
const filePath = pathDir + "/test.txt";
const ws = fs.createWriteStream(filePath);
const curOff = ws.seek(5, fs.WhenceType.SEEK_SET);
console.info(`current offset is ${curOff}`);
ws.close();
```

#### close12+

close(): void

关闭可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](文件管理错误码.md#ZH-CN_TOPIC_0000002529445241__基础文件io错误码)。

**示例：**

```ets
const filePath = pathDir + "/test.txt";
const ws = fs.createWriteStream(filePath);
ws.close();
```

#### RandomAccessFileOptions12+

可选项类型，支持 createRandomAccessFile 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明startnumber否是表示期望读取文件的位置，单位为字节。可选，默认从当前位置开始读。endnumber否是表示期望读取结束的位置，单位为字节。可选，默认文件末尾。

#### ReadStreamOptions12+

可选项类型，支持 createReadStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明startnumber否是表示期望读取文件的位置，单位为字节。可选，默认从当前位置开始读。endnumber否是表示期望读取结束的位置，单位为字节。可选，默认文件末尾。

#### WriteStreamOptions12+

可选项类型，支持 createWriteStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

名称类型只读可选说明startnumber否是表示期望写入文件的位置，单位为字节。可选，默认从当前位置开始写。modenumber否是

创建文件可写流的[选项](#ZH-CN_TOPIC_0000002529445221__openmode)，必须指定如下选项中的一个，默认只写方式创建：

- OpenMode.READ_ONLY(0o0)：只读。

- OpenMode.WRITE_ONLY(0o1)：只写。

- OpenMode.READ_WRITE(0o2)：读写。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

- OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。