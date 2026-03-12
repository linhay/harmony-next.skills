# @ohos.zlib (Zip模块)

本模块提供压缩解压缩文件的能力。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { zlib } from '@kit.BasicServicesKit';
```

#### zlib.zipFile(deprecated)

zipFile(inFile: string, outFile: string, options: Options): Promise<void>

压缩接口，压缩完成后返回执行结果，使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[zlib.compressFile](#ZH-CN_TOPIC_0000002529285501__zlibcompressfile9)。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilestring是指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。outFilestring是指定压缩结果的文件路径（文件的扩展名zip）。options[Options](#ZH-CN_TOPIC_0000002529285501__options)是压缩的可选参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

zlib.zipFile(inFile, outFile, options).then((data: void) => {
  console.info('zipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
});
```

#### zlib.unzipFile(deprecated)

unzipFile(inFile:string, outFile:string, options: Options): Promise<void>

解压文件，解压完成后返回执行结果，使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[zlib.decompressFile](#ZH-CN_TOPIC_0000002529285501__zlibdecompressfile9)。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回-1错误码。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilestring是指定的待解压缩文件的文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。outFilestring是指定的解压文件路径。options[Options](#ZH-CN_TOPIC_0000002529285501__options)是解压的可选参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFile = '/data/storage/el2/base/temp/xxx';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

zlib.unzipFile(inFile, outFile, options).then((data: void) => {
  console.info('unzipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
})
```

#### zlib.compressFile9+

compressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void

压缩文件，压缩的结果，使用callback异步回调返回。成功返回null，失败返回错误码。

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilestring是指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。待压缩的文件夹不可为空，否则使用[decompressFile](#ZH-CN_TOPIC_0000002529285501__zlibdecompressfile9)对压缩后的文件解压时会报错。outFilestring是指定的压缩结果的文件路径。多个线程同时压缩文件时，outFile不能相同。options[Options](#ZH-CN_TOPIC_0000002529285501__options)是压缩的配置参数。callbackAsyncCallback<void>是异步获取压缩结果之后的回调。成功返回null，失败返回错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.900001The input source file is invalid.900002The input destination file is invalid.

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

try {
  zlib.compressFile(inFile, outFile, options, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(`compressFile errData is errCode:${errData.code}  message:${errData.message}`);
    } else {
      console.info(`compressFile success.`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`compressFile errData is errCode:${code}  message:${message}`);
}
```

#### zlib.compressFile9+

compressFile(inFile: string, outFile: string, options: Options): Promise<void>

压缩文件，压缩的结果，使用Promise异步回调。成功时返回null，失败时返回错误码。

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilestring是指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。待压缩的文件夹不可为空，否则使用[decompressFile](#ZH-CN_TOPIC_0000002529285501__zlibdecompressfile9)对压缩后的文件解压时会报错。outFilestring是指定的压缩结果的文件路径。多个线程同时压缩文件时，outFile不能相同。options[Options](#ZH-CN_TOPIC_0000002529285501__options)是压缩的配置参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.900001The input source file is invalid.900002The input destination file is invalid.

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

try {
  zlib.compressFile(inFile, outFile, options).then((data: void) => {
    console.info('compressFile success. data: ' + JSON.stringify(data));
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```

#### zlib.decompressFile9+

decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void

解压文件，解压的结果，使用callback异步回调返回。成功时返回null，失败时返回错误码。

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilestring是指定的待解压缩文件的文件路径，文件后缀需要以.zip结尾。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。outFilestring是指定的解压后的文件夹路径，文件夹目录路径需要在系统中存在，不存在则会解压失败。路径必须为沙箱路径，沙箱路径可以通过context获取，具体方法可参考[application/context（Stage模型）](Context (Stage模型的上下文基类).md)或 [app/context（FA模型）](Context (FA模型的上下文基类).md)。如果待解压的文件或文件夹在解压后的路径下已经存在，则会直接覆盖同名文件或同名文件夹中的同名文件。多个线程同时解压文件时，outFile不能相同。options[Options](#ZH-CN_TOPIC_0000002529285501__options)是解压的配置参数。callbackAsyncCallback<void>是异步获取解压结果之后的回调。成功返回null，失败返回错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.900001The input source file is invalid.900002The input destination file is invalid.900003The input source file is not in ZIP format or is damaged.

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  parallel: zlib.ParallelStrategy.PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION
};

try {
  zlib.decompressFile(inFile, outFileDir, options, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(`decompressFile errData is errCode:${errData.code}  message:${errData.message}`);
    } else {
      console.info(`decompressFile success.`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`decompressFile errData is errCode:${code}  message:${message}`);
}
```

#### zlib.decompressFile9+

decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>

解压文件，解压的结果，使用Promise异步回调，成功时返回null，失败时返回错误码。

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilestring是指定的待解压缩文件的文件路径，文件后缀需要以.zip结尾。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。outFilestring是指定的解压后的文件夹路径，文件夹目录路径需要在系统中存在，不存在则会解压失败。路径必须为沙箱路径，沙箱路径可以通过context获取，具体方法可参考[application/context（Stage模型）](Context (Stage模型的上下文基类).md)或 [app/context（FA模型）](Context (FA模型的上下文基类).md)。如果待解压的文件或文件夹在解压后的路径下已经存在，则会直接覆盖同名文件或同名文件夹中的同名文件。多个线程同时解压文件时，outFile不能相同。options[Options](#ZH-CN_TOPIC_0000002529285501__options)否解压时的配置参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.900001The input source file is invalid.900002The input destination file is invalid.900003The input source file is not in ZIP format or is damaged.

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION
};

try {
  zlib.decompressFile(inFile, outFileDir, options).then((data: void) => {
    console.info('decompressFile success. data: ' + JSON.stringify(data));
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```

#### zlib.decompressFile10+

decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void

解压文件，解压的结果，使用callback异步回调返回。成功时返回null，失败时返回错误码。

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilestring是指定的待解压缩文件的文件路径，文件后缀需要以.zip结尾。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。outFilestring是指定的解压后的文件夹路径，文件夹目录路径需要在系统中存在，不存在则会解压失败。路径必须为沙箱路径，沙箱路径可以通过context获取，具体方法可参考[application/context（Stage模型）](Context (Stage模型的上下文基类).md)或 [app/context（FA模型）](Context (FA模型的上下文基类).md)。如果待解压的文件或文件夹在解压后的路径下已经存在，则会直接覆盖同名文件或同名文件夹中的同名文件。多个线程同时解压文件时，outFile不能相同。callbackAsyncCallback<void>是异步获取解压结果之后的回调。成功返回null，失败返回错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.900001The input source file is invalid.900002The input destination file is invalid.900003The input source file is not in ZIP format or is damaged.

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';

try {
  zlib.decompressFile(inFile, outFileDir, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(`decompressFile failed. code is ${errData.code}, message is ${errData.message}`);
    } else {
      console.info(`decompressFile success.`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`decompressFile failed. code is ${code}, message is ${message}`);
}
```

#### zlib.getOriginalSize12+

getOriginalSize(compressedFile: string): Promise<number>

获取压缩文件的原始大小，使用Promise异步回调。成功时返回压缩文件的原始大小，失败时返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明compressedFilestring是指定的压缩文件的文件路径，只支持zip格式压缩文件。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。

**返回值：**

类型说明Promise<number>Promise对象，返回压缩文件的原始大小，单位字节。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401The parameter check failed. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.900001The input source file is invalid.900003The input source file is not in ZIP format or is damaged.

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp，也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let compressedFile = '/data/storage/el2/base/temp/test.zip';

try {
  zlib.getOriginalSize(compressedFile).then((data: number) => {
    console.info(`getOriginalSize success. getOriginalSize: ${data}`);
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```

#### zlib.compressFiles12+

compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>

压缩指定的多个文件，使用Promise异步回调。成功时返回null，失败时返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inFilesArray<string>是指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](Context (FA模型的上下文基类).md)，[Stage模型](Context (Stage模型的上下文基类).md)。待压缩的文件夹不可为空，否则使用[decompressFile](#ZH-CN_TOPIC_0000002529285501__zlibdecompressfile9)对压缩后的文件解压时会报错。outFilestring是指定的压缩结果的文件路径。多个线程同时压缩文件时，outFile不能相同。options[Options](#ZH-CN_TOPIC_0000002529285501__options)是压缩的配置参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.900001The input source file is invalid.900002The input destination file is invalid.

**示例：**

```ets
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp，也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let pathDir = 'data/storage/el2/base/temp/xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

try {
  zlib.compressFiles([inFile, pathDir], outFile, options).then((data: void) => {
    console.info('compressFiles success. data: ' + JSON.stringify(data));
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```

#### zlib.createChecksum12+

createChecksum(): Promise<Checksum>

创建校验对象，使用Promise异步回调。成功时返回Checksum对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[Checksum](#ZH-CN_TOPIC_0000002529285501__checksum12)>Promise对象。返回校验对象实例。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

zlib.createChecksum().then((data) => {
  console.info('createChecksum success');
})
```

#### zlib.createChecksumSync12+

createChecksumSync(): Checksum

创建校验对象。成功时返回Checksum对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明[Checksum](#ZH-CN_TOPIC_0000002529285501__checksum12)校验对象实例。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()
```

#### Checksum12+

校验对象。

#### adler3212+

adler32(adler: number, buf: ArrayBuffer): Promise<number>

计算Adler-32校验和，使用Promise异步回调。成功时返回计算后的Adler-32校验和，失败时返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明adlernumber是Adler-32校验和的初始值。bufArrayBuffer是计算校验和数据缓冲区。

**返回值：**

类型说明Promise<number>Promise对象。返回计算后的Adler-32校验和。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data[i] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.adler32(0, arrayBufferIn).then(data => {
  console.info('adler32 success', data);
})
```

#### adler32Combine12+

adler32Combine(adler1: number, adler2: number, len2: number): Promise<number>

将两个Adler-32校验和合并，使用Promise异步回调。成功时返回合并后的Adler-32校验和，失败时返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明adler1number是第一个要合并的Adler-32校验和。adler2number是第二个要合并的Adler-32校验和。len2number是第二个Adler-32校验和的数据块的长度。

**返回值：**

类型说明Promise<number>Promise对象。返回合并后的Adler-32校验和。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(12);
  let data = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    data[i] = str.charCodeAt(i);
  }
  let checksum = zlib.createChecksumSync()
  let adler1 = 0;
  let adler2 = 1;
  await checksum.adler32(0, arrayBufferIn).then(data => {
    console.info('adler32 success', data);
    adler1 = data;
  })
  await checksum.adler32(1, arrayBufferIn).then(data => {
    console.info('adler32 success', data);
    adler2 = data;
  })
  await checksum.adler32Combine(adler1, adler2, 12).then((data) => {
    console.info('adler32Combine success', data);
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### crc3212+

crc32(crc: number, buf: ArrayBuffer): Promise<number>

更新CRC-32校验，使用Promise异步回调。成功时返回更新后的CRC-32校验，失败时返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明crcnumber是CRC-32校验的初始值。bufArrayBuffer是计算校验数据缓冲区。

**返回值：**

类型说明Promise<number>Promise对象。返回更新后的CRC-32校验。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data[i] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.crc32(0, arrayBufferIn).then((data) => {
  console.info('crc32 success', data);
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### crc32Combine12+

crc32Combine(crc1: number, crc2: number, len2: number): Promise<number>

将两个CRC-32校验合并，使用Promise异步回调。成功时返回合并后的CRC-32校验，失败时返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明crc1number是第一个要合并的CRC-32校验。crc2number是第二个要合并的CRC-32校验。len2number是第二个CRC-32校验的数据块的长度。

**返回值：**

类型说明Promise<number>Promise对象。返回合并后的CRC-32校验。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(12);
  let data = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    data[i] = str.charCodeAt(i);
  }
  let checksum = zlib.createChecksumSync()
  let crc1 = 0;
  let crc2 = 1;
  await checksum.crc32(0, arrayBufferIn).then(data => {
    console.info('crc32 success', data);
    crc1 = data;
  })
  await checksum.crc32(1, arrayBufferIn).then(data => {
    console.info('crc32 success', data);
    crc2 = data;
  })
  await checksum.crc32Combine(crc1, crc2, 12).then((data) => {
    console.info('crc32Combine success', data);
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### crc6412+

crc64(crc: number, buf: ArrayBuffer): Promise<number>

更新CRC-64校验，使用Promise异步回调。成功时返回更新后的CRC-64校验，失败时返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明crcnumber是CRC-64校验的初始值。bufArrayBuffer是计算校验数据缓冲区。

**返回值：**

类型说明Promise<number>Promise对象。返回更新后的CRC-64校验。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data[i] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.crc64(0, arrayBufferIn).then((data) => {
  console.info('crc64 success', data);
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### getCrcTable12+

getCrcTable(): Promise<Array<number>>

输出CRC-32校验表，使用Promise异步回调。成功时返回CRC-32校验表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<Array<number>>Promise对象。返回CRC-32校验表。

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()

checksum.getCrcTable().then((data) => {
  console.info('getCrcTable success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### getCrc64Table12+

getCrc64Table(): Promise<Array<number>>

输出CRC-64校验表，使用Promise异步回调。成功时返回CRC-64校验表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<Array<number>>Promise对象。返回CRC-64校验表。

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()

checksum.getCrc64Table().then((data) => {
  console.info('getCrc64Table success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### zlib.createZip12+

createZip(): Promise<Zip>

创建压缩解压缩对象实例，使用Promise异步回调，成功时返回压缩解压缩对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[Zip](#ZH-CN_TOPIC_0000002529285501__zip12)>Promise对象。返回压缩解压缩对象实例。

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

zlib.createZip().then(data => {
  console.info('createZip success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### zlib.createZipSync12+

createZipSync(): Zip

创建压缩解压缩对象实例，成功时返回压缩解压缩对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明[Zip](#ZH-CN_TOPIC_0000002529285501__zip12)返回压缩解压缩对象实例。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();
```

#### Zip12+

压缩解压缩对象实例，支持以zlib、deflate、gzip格式对数据进行压缩与解压。

#### getZStream12+

getZStream(): Promise<ZStream>

输出流，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[ZStream](#ZH-CN_TOPIC_0000002529285501__zstream12)>Promise对象。返回ZStream流。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();

zip.getZStream().then(data => {
  console.info('getZStream success');
})
```

#### zlibVersion12+

zlibVersion(): Promise<string>

获取当前链接的zlib库的版本信息，使用Promise异步回调。成功时返回当前zlib库的版本信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<string>Promise对象。返回当前zlib库的版本信息。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();

zip.zlibVersion().then((data) => {
  console.info('zlibVersion success')
})
```

#### zlibCompileFlags12+

zlibCompileFlags(): Promise<number>

返回指示编译时选项的标志，使用Promise异步回调。成功时返回指示编译时选项的标志。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<number>Promise对象。返回指示编译时选项的标志。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();

zip.zlibCompileFlags().then((data) => {
  console.info('zlibCompileFlags success')
})
```

#### compress12+

compress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>

将源缓冲区压缩到目标缓冲区，使用Promise异步回调。成功时返回结果状态和目标缓冲区的总大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明destArrayBuffer是目标缓冲区。sourceArrayBuffer是源数据缓冲区。sourceLennumber否源数据长度。默认值为0。

**返回值：**

类型说明Promise<[ZipOutputInfo](#ZH-CN_TOPIC_0000002529285501__zipoutputinfo12)>Promise对象。返回结果状态和目标缓冲区的总大小。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800007The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray[i] = str.charCodeAt(i)
}

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.compress(arrayBufferOut, arrayBufferIn, 20).then((data) => {
  console.info('compress success:');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### compress212+

compress2(dest: ArrayBuffer, source: ArrayBuffer, level: CompressLevel, sourceLen?: number): Promise<ZipOutputInfo>

将源缓冲区压缩到目标缓冲区，使用Promise异步回调。成功时返回结果状态和目标缓冲区的总大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明destArrayBuffer是目标缓冲区。sourceArrayBuffer是源数据缓冲区。levelCompressLevel是参考[CompressLevel枚举定义](#ZH-CN_TOPIC_0000002529285501__compresslevel)。sourceLennumber否源数据长度。默认值为0。

**返回值：**

类型说明Promise<[ZipOutputInfo](#ZH-CN_TOPIC_0000002529285501__zipoutputinfo12)>Promise对象。返回结果状态和目标缓冲区的总大小。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800007The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray[i] = str.charCodeAt(i)
}

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.compress2(arrayBufferOut, arrayBufferIn, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
  console.info('compress2 success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### uncompress12+

uncompress(dest:ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>

将压缩后的数据解压缩为原始的未压缩形式，使用Promise异步回调。成功时返回结果状态和目标缓冲区的总大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明destArrayBuffer是目标缓冲区。sourceArrayBuffer是源数据缓冲区。sourceLennumber否源数据长度。默认值为0。

**返回值：**

类型说明Promise<[ZipOutputInfo](#ZH-CN_TOPIC_0000002529285501__zipoutputinfo12)>Promise对象。返回结果状态和目标缓冲区的总大小。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800005The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed.17800007The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.compress(arrayBufferOut, arrayBufferIn, 12).then((data) => {
    console.info('compress success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.uncompress(arrayBufferIn, arrayBufferOut, 20).then((data) => {
    console.info('uncompress success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### uncompress212+

uncompress2(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<DecompressionOutputInfo>

将压缩后的数据解压缩为原始的未压缩形式，使用Promise异步回调。成功时返回结果状态、目标缓冲区的总大小和源数据长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明destArrayBuffer是目标缓冲区。sourceArrayBuffer是源数据缓冲区。sourceLennumber否源数据长度。默认值为0。

**返回值：**

类型说明Promise<[DecompressionOutputInfo](#ZH-CN_TOPIC_0000002529285501__decompressionoutputinfo12)>Promise对象。返回结果状态、目标缓冲区的总大小和源数据长度。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800005The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed.17800007The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.compress2(arrayBufferOut, arrayBufferIn, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('compress2 success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.uncompress2(arrayBufferIn, arrayBufferOut, 20).then((data) => {
    console.info('uncompress2 success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### compressBound12+

compressBound(sourceLen: number): Promise<number>

计算返回压缩大小的上限，使用Promise异步回调。成功时返回压缩大小的上限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明sourceLennumber是源数据长度。

**返回值：**

类型说明Promise<number>Promise对象。返回压缩大小的上限。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray[i] = str.charCodeAt(i)
}

let zip = zlib.createZipSync();

zip.compressBound(str.length).then((data) => {
  console.info('compressBound success')
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### inflateValidate12+

inflateValidate(strm: ZStream, check: number): Promise<ReturnStatus>

验证压缩流结构内部的校验和，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。checknumber是预期的校验和。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateValidate({ availableIn: 1 }, 1).then(data => {
    console.info('inflateValidate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateSyncPoint12+

inflateSyncPoint(strm: ZStream): Promise<ReturnStatus>

查找当前解压缩流的同步点，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateSyncPoint({ availableIn: 1 }).then(data => {
    console.info('inflateSyncPoint success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateSync12+

inflateSync(strm: ZStream): Promise<ReturnStatus>

跳过无效的压缩数据，直到找到一个可能的完整刷新点为止，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800005The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed.17800007The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello, hello!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.deflateInit({}, zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflate({ nextIn: arrayBufferIn, availableIn: 3, nextOut: arrayBufferOut, availableOut: 100 }, zlib.CompressFlushMode.FULL_FLUSH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflate({ availableIn: 11 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateEnd({}).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  try {
    await zip.inflateInit({ nextIn: arrayBufferOut, availableIn: 2 }).then(data => {
      console.info('inflateInit2 success')
    })
  } catch (errData) {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  }
  await zip.inflate({ nextOut: arrayBufferIn, availableOut: 28 }, zlib.CompressFlushMode.NO_FLUSH).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateSync({ availableIn: 26 }).then(data => {
    console.info('inflateSync success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateResetKeep12+

inflateResetKeep(strm: ZStream): Promise<ReturnStatus>

重置解压缩流的状态，以保留分配的霍夫曼解码树和预设字典，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateResetKeep({ availableIn: 1 }).then(data => {
    console.info('inflateResetKeep success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateSetDictionary12+

inflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>

使用给定的字典数据初始化当前解压缩流的字典内容，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。dictionaryArrayBuffer是字典数据。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800005The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello, hello!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  let dictionary = 'hello'
  let dictionarybuf = new ArrayBuffer(dictionary.length);
  let dictionarybufdata = new Uint8Array(dictionarybuf);
  for (let i = 0, j = dictionary.length; i < j; i++) {
    dictionarybufdata[i] = str.charCodeAt(i);
  }
  await zip.deflateInit({}, zlib.CompressLevel.COMPRESS_LEVEL_BEST_COMPRESSION).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflateSetDictionary({}, dictionarybuf).then((data) => {
    console.info('deflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflate({ nextIn: arrayBufferIn, availableIn: 14, nextOut: arrayBufferOut, availableOut: 100 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflateEnd({}).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  try {
    await zip.inflateInit({ nextIn: arrayBufferOut, availableIn: 100 }).then(data => {
      console.info('inflateInit success')
    })
  } catch (errData) {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  }
  await zip.inflate({ nextOut: arrayBufferIn, availableOut: 28 }, zlib.CompressFlushMode.NO_FLUSH).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.inflateSetDictionary({}, dictionarybuf).then((data) => {
    console.info('inflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
}
```

#### inflateReset212+

inflateReset2(strm: ZStream, windowBits: number): Promise<ReturnStatus>

重置指定解压缩流的状态并更新窗口大小配置，以重新开始新的解压操作。不会释放或重新分配内部缓冲区。使用Promise异步回调，成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。windowBitsnumber是

控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：

zlib格式：[1, 15]。

gzip格式：大于15。

raw deflate格式：[-15, -1]。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateReset2({ availableOut: 8 }, 15).then(data => {
    console.info('inflateReset2 success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateReset12+

inflateReset(strm: ZStream): Promise<ReturnStatus>

重置指定解压缩流的状态，使其恢复到初始化状态以重新开始新的解压操作。不会释放或重新分配内部缓冲区。使用Promise异步回调，成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateReset({ availableIn: 1, availableOut: 8 }).then(data => {
    console.info('inflateReset success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflatePrime12+

inflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>

在指定解压缩流中设置初始比特数和比特值，用于在解压流开始时预填充比特缓冲区，以正确处理流起始位置的数据。使用Promise异步回调，成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。bitsnumber是指定要写入比特缓冲区的比特数。valuenumber是用于填充比特缓冲区的比特值。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflatePrime({ nextOut: arrayBufferOut }, 5, 2).then(data => {
    console.info('inflatePrime success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateMark12+

inflateMark(strm: ZStream): Promise<number>

用于标记输入数据中的位置以供随机访问，使用Promise异步回调。成功时返回位置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<number>Promise对象。返回位置信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateMark({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }).then(data => {
    console.info('inflateMark success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateInit212+

inflateInit2(strm: ZStream, windowBits: number): Promise<ReturnStatus>

初始化解压缩流并设置指定的 windowBits 参数，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。windowBitsnumber是

控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：

zlib格式：[1, 15]。

gzip格式：大于15。

raw deflate格式：[-15, -1]。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray[i] = str.charCodeAt(i)
}

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
).then(data => {
  console.info('inflateInit2 success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### inflateInit12+

inflateInit(strm: ZStream): Promise<ReturnStatus>

初始化解压缩流，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray[i] = str.charCodeAt(i)
}

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
).then(data => {
  console.info('inflateInit success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

#### inflateGetHeader12+

inflateGetHeader(strm: ZStream, header: GzHeader): Promise<ReturnStatus>

用于在解压缩数据前设置gzip文件头部信息，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。header[GzHeader](#ZH-CN_TOPIC_0000002529285501__gzheader12)是从压缩数据流中提取的gzip头信息。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
  ).then(data => {
    console.info('inflateInit2 success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateGetHeader({ availableIn: 1, availableOut: 1 }, { isText: true, os: 1, time: 1, xflags: 1, extra: arrayBufferIn, extraLen: 12, name: arrayBufferIn, comment: arrayBufferOut, hcrc: true, done: true }).then(data => {
    console.info('inflateGetHeader success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateGetDictionary12+

inflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>

获取当前解压缩流中使用的解压缩字典内容及其长度，使用Promise异步回调。成功时返回结果状态和字典的长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。dictionaryArrayBuffer是接收解压缩字典的实际内容。

**返回值：**

类型说明Promise<[DictionaryOutputInfo](#ZH-CN_TOPIC_0000002529285501__dictionaryoutputinfo12)>Promise对象。返回结果状态和字典的长度。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
  ).then(data => {
    console.info('inflateInit2 success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateGetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('inflateGetDictionary success:')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateEnd12+

inflateEnd(strm: ZStream): Promise<ReturnStatus>

解压流的所有动态分配的数据结构都被释放，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflate({ availableIn: 8, availableOut: 8 }, 0).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateCopy12+

inflateCopy(source: Zip): Promise<ReturnStatus>

复制解压流，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明sourceZip是参考[Zip定义](#ZH-CN_TOPIC_0000002529285501__zip12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  let destZip = zlib.createZipSync();
  await destZip.inflateCopy(zip).then((data) => {
    console.info('inflateCopy success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateCodesUsed12+

inflateCodesUsed(strm: ZStream): Promise<number>

当前解压缩流中使用的霍夫曼编码树的数量，使用Promise异步回调。成功时返回已使用的霍夫曼编码树的数量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<number>Promise对象。返回已使用的霍夫曼编码树的数量。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateCodesUsed({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 8 }).then(data => {
    console.info('inflateCodesUsed success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### inflateBackInit12+

inflateBackInit(strm: ZStream, windowBits: number, window: ArrayBuffer): Promise<ReturnStatus>

使用inflateBack()函数前初始化内部流状态以进行解压缩，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。windowBitsnumber是

控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：

zlib格式：[1, 15]。

gzip格式：大于15。

raw deflate格式：[-15, -1]。

windowArrayBuffer是预设的窗口缓冲区。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

参考[inflateBack](#ZH-CN_TOPIC_0000002529285501__inflateback12)中的示例代码。

#### inflateBackEnd12+

inflateBackEnd(strm: ZStream): Promise<ReturnStatus>

inflateBackInit()函数分配的所有内存都被释放，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

参考[inflateBack](#ZH-CN_TOPIC_0000002529285501__inflateback12)中的示例代码。

#### inflateBack12+

inflateBack(strm: ZStream, backIn: InflateBackInputCallback, inDesc: object, backOut: InflateBackOutputCallback, outDesc: object): Promise<ReturnStatus>

实现原始解压缩，采用回调接口来处理输入和输出，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。backInInflateBackInputCallback是一种函数，用于从末尾解压缩数据，以从输入源读取原始压缩数据。inDescobject是通用对象。backOutInflateBackOutputCallback是将解压缩的数据写入目标输出。outDescobject是通用对象。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let readIn: (inDesc: object) => ArrayBuffer = (inDesc: object): ArrayBuffer => {
    console.info("inDesc = ", JSON.stringify(inDesc));
    let buffer = new ArrayBuffer(26)
    let array = new Uint8Array(buffer);
    array.set([31, 139, 8, 0, 0, 0, 0, 0, 0, 10, 243, 72, 205, 201, 201, 231, 2, 0, 22, 53, 150, 49, 6, 0, 0, 0]);
    return buffer;
  }

  let writeOut: (outDesc: object, buffer: ArrayBuffer, length: number) => number = (outDesc: object, buffer: ArrayBuffer, length: number): number => {
    console.info("outDesc = ", outDesc);
    console.info("buffer = ", buffer);
    console.info("length = ", length);
    let array = new Uint8Array(buffer);
    let dataString = "";
    for (let i = 0; i < length; i++) {
      dataString += String.fromCharCode(array[i]);
    }
    console.info('writeOut ', dataString);
    return 0;
  }

  let have = 0;
  let first = 1;
  let arrayBuffer = new ArrayBuffer(26);
  let next = new Uint8Array(arrayBuffer);
  let last = 0;
  let index = 0;
  let flags = 0;
  let NEXT2: () => number = (): number => {
    let o6: object = new Object()
    if (!have) {
      arrayBuffer = readIn(o6)
      next = new Uint8Array(arrayBuffer);
      console.info('readIn next = ', next.length)
      have = next.length;
    }
    if (have) {
      have--;
      last = next[index];
      index++;
    }
    else {
      last = -1;
    }
    return last;
  }

  let inflateBackTest: () => void = (async () => {
    try {
      have = 0;
      first = 1;
      arrayBuffer = new ArrayBuffer(26);
      next = new Uint8Array(arrayBuffer);
      last = 0;
      index = 0;
      flags = 0;
      let sr = zlib.createZipSync();
      let buffer = new ArrayBuffer(1024)
      await sr.inflateBackInit({}, 15, buffer).then((result) => {
        console.info('inflateBackInit Call result res', result)
      })
      let ret = 0;
      for (; ;) {
        if (NEXT2() == -1) {
          ret = 0;
          console.info('inflateBackTest Call result NEXT2() == -1')
          break;
        }
        console.info('have =  last = ', have, last)
        if (last != 31 || NEXT2() != 139 ) {
          ret = first ? -3 : -1;
          console.info('inflateBackTest Call result last != 31 || (NEXT2() != 139 && last != 157)')
          break;
        }
        first = 0;
        ret = -5;
        if (NEXT2() != 8) {
          if (last < 0) {
            console.info('inflateBackTest Call result 1 last == -1')
            break;
          }
        }
        flags = NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        if (last < 0) {
          console.info('inflateBackTest Call result 2 last == -1')
          break;
        }
        console.info('index =  have = ', next[index], have)
        let newArrayBuffer = new ArrayBuffer(have);
        let newNext = new Uint8Array(newArrayBuffer);
        for (let i = 0; i < have; i++) {
          newNext[i] = next[26 - have + i];
        }
        console.info('newArrayBuffer.length = ', newArrayBuffer.byteLength)
        console.info('newNext.length = ', newNext.length)
        let zStream: zlib.ZStream = {
          nextIn: newArrayBuffer,
          availableIn: have,
        };
        await sr.inflateBack(
          zStream,
          readIn,
          { fileName: 'test.gz' },
          writeOut,
          { fileName: 'test.gz' }).then((result) => {
            ret = result;
            console.info('inflateBack Call result res', result)
          })
        if (ret == 1) {
          console.info('inflateBackTest Call result success')
          break;
        }
      }
      await sr.inflateBackEnd({}).then((result) => {
        console.info('inflateBackEnd Call result res', result)
      })
    }
    catch (errData) {
      console.error(`errData is message:${errData}`);
    }
  })
  inflateBackTest();
}
```

#### InflateBackInputCallback12+

type InflateBackInputCallback = (inDesc: object) => ArrayBuffer

用于输入数据的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明inDescobject是用户定义数据对象。

**返回值：**

类型说明ArrayBuffer从输入数据源成功读取的内容缓冲区。

#### InflateBackOutputCallback12+

type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: number) => number

用于输出数据的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明outDescobject是用户定义数据对象。bufArrayBuffer是用于存储要写入的数据。lengthnumber是写入输出缓冲区的长度。

**返回值：**

类型说明number输出缓冲区的字节数。

#### inflate12+

inflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>

解压数据，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。flushCompressFlushMode是参考[CompressFlushMode定义](#ZH-CN_TOPIC_0000002529285501__compressflushmode12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800005The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflateEnd({ nextOut: arrayBufferOut }).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflate({ availableIn: 8, availableOut: 8 }, 0).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateInit12+

deflateInit(strm: ZStream, level: CompressLevel): Promise<ReturnStatus>

初始化压缩流并设置指定压缩级别，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。levelCompressLevel是参考[CompressLevel枚举定义](#ZH-CN_TOPIC_0000002529285501__compresslevel)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
}
```

#### deflateInit212+

deflateInit2(strm: ZStream, level: CompressLevel, method: CompressMethod, windowBits: number, memLevel: MemLevel, strategy: CompressStrategy): Promise<ReturnStatus>

初始化压缩流并设置压缩级别、压缩方法、窗口大小、内存级别和压缩策略，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。levelCompressLevel是参考[CompressLevel枚举定义](#ZH-CN_TOPIC_0000002529285501__compresslevel)。methodCompressMethod是参考[CompressMethod枚举定义](#ZH-CN_TOPIC_0000002529285501__compressmethod12)。windowBitsnumber是

控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：

zlib格式：[1, 15]。

gzip格式：大于15。

raw deflate格式：[-15, -1]。

memLevelMemLevel是参考[MemLevel枚举定义](#ZH-CN_TOPIC_0000002529285501__memlevel)。strategyCompressStrategy是参考[CompressStrategy枚举定义](#ZH-CN_TOPIC_0000002529285501__compressstrategy)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync()
  await zip.deflateInit2(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED, zlib.CompressMethod.DEFLATED, 28,
    zlib.MemLevel.MEM_LEVEL_DEFAULT, zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY).then((data) => {
      console.info('deflateInit2 success');
    }).catch((errData: BusinessError) => {
      console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
    })
}
```

#### deflate12+

deflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>

压缩数据，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。flushCompressFlushMode是参考[CompressFlushMode定义](#ZH-CN_TOPIC_0000002529285501__compressflushmode12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800007The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
}
```

#### deflateEnd12+

deflateEnd(strm: ZStream): Promise<ReturnStatus>

压缩流的所有动态分配的数据结构都被释放，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
  await zip.deflateEnd({ nextOut: arrayBufferOut }).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateBound12+

deflateBound(strm: ZStream, sourceLength: number): Promise<number>

计算压缩大小的上限，使用Promise异步回调。成功时返回压缩大小的上限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。sourceLengthnumber是源数据长度。

**返回值：**

类型说明Promise<number>Promise对象。返回压缩大小的上限。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateBound({ nextOut: arrayBufferOut }, 12).then((data) => {
    console.info('deflateBound success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateSetHeader12+

deflateSetHeader(strm: ZStream, head: GzHeader): Promise<ReturnStatus>

当deflateInit2()请求gzip流时，提供gzip标头信息，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。head[GzHeader](#ZH-CN_TOPIC_0000002529285501__gzheader12)是从压缩数据流中提取的gzip头信息。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync()
  await zip.deflateInit2(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED, zlib.CompressMethod.DEFLATED, 28,
    zlib.MemLevel.MEM_LEVEL_DEFAULT, zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY).then((data) => {
      console.info('deflateInit2 success');
    }).catch((errData: BusinessError) => {
      console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
    })
  await zip.deflateSetHeader({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, { isText: true, os: 1, time: 1, xflags: 1, extra: arrayBufferIn, extraLen: 12, name: arrayBufferIn, comment: arrayBufferOut, hcrc: true, done: true }).then((data) => {
    console.info('deflateSetHeader success');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
  })
}
```

#### deflateCopy12+

deflateCopy(source: Zip): Promise<ReturnStatus>

复制压缩流，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明sourceZip是参考[Zip定义](#ZH-CN_TOPIC_0000002529285501__zip12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateCopy(zip).then((data) => {
    console.info('deflateCopy success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateSetDictionary12+

deflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>

从给定的字节序列初始化压缩字典，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。dictionaryArrayBuffer是字典数据。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateSetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('deflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateGetDictionary12+

deflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>

获取当前压缩流中使用的解压缩字典内容及其长度，使用Promise异步回调。成功时返回结果状态和字典的长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。dictionaryArrayBuffer是接收压缩字典的实际内容。

**返回值：**

类型说明Promise<[DictionaryOutputInfo](#ZH-CN_TOPIC_0000002529285501__dictionaryoutputinfo12)>Promise对象。返回结果状态和字典的长度。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateSetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('deflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateGetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('deflateGetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateTune12+

deflateTune(strm: ZStream, goodLength: number, maxLazy: number, niceLength: number, maxChain: number): Promise<ReturnStatus>

微调deflate的内部压缩参数，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。goodLengthnumber是匹配的长度阈值。maxLazynumber是压缩算法在构建哈夫曼树时的延迟匹配策略，取值范围为0到4的整数。1到4，值越大，算法越‘懒’，匹配过程越慢，但可能生成更优的压缩结果。0：禁用懒惰匹配，算法会尽快构建哈夫曼树，压缩速度快，但压缩率低。niceLengthnumber是适合的延迟长度阈值。maxChainnumber是最大链条长度。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateTune({ nextOut: arrayBufferOut }, 2, 2, 2, 2).then((data) => {
    console.info('deflateTune success:')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateReset12+

deflateReset(strm: ZStream): Promise<ReturnStatus>

这个函数相当于先调用deflateEnd再调用deflateInit，但是并不会释放和重新分配内部解压缩状态，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateReset({ nextOut: arrayBufferOut }).then((data) => {
    console.info('deflateReset success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateResetKeep12+

deflateResetKeep(strm: ZStream): Promise<ReturnStatus>

重置初始化的deflate压缩流，但保留其设置的压缩参数和字典，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateResetKeep({ nextOut: arrayBufferOut }).then((data) => {
    console.info('deflateResetKeep success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflatePending12+

deflatePending(strm: ZStream): Promise<DeflatePendingOutputInfo>

返回已生成但尚未在可用输出中提供的输出的字节数和位数，使用Promise异步回调。成功时返回结果状态、输出位数和输出字节数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。

**返回值：**

类型说明Promise<[DeflatePendingOutputInfo](#ZH-CN_TOPIC_0000002529285501__deflatependingoutputinfo12)>Promise对象。返回结果状态、输出位数和输出字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflatePending({ nextOut: arrayBufferOut }).then((data) => {
    console.info('deflatePending success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflateParams12+

deflateParams(strm: ZStream, level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>

动态更新压缩级别和压缩策略，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。levelCompressLevel是参考[CompressLevel枚举定义](#ZH-CN_TOPIC_0000002529285501__compresslevel)。strategyCompressStrategy是参考[CompressStrategy枚举定义](#ZH-CN_TOPIC_0000002529285501__compressstrategy)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync()
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflateParams(zStream, zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION, zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY).then((data) => {
    console.info('deflateParams success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### deflatePrime12+

deflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>

在压缩流中插入位和值，使用Promise异步回调。成功时返回结果状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strmZStream是参考[ZStream定义](#ZH-CN_TOPIC_0000002529285501__zstream12)。bitsnumber是要插入的位数，取值范围在0~16。valuenumber是与位数相对应的位值。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象。返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
  await zip.deflatePrime({ nextOut: arrayBufferOut }, 5, 2).then((data) => {
    console.info('deflatePrime success')
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

#### Options

Options用于指定在压缩或解压Zip文件时的选项。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明level[CompressLevel](#ZH-CN_TOPIC_0000002529285501__compresslevel)否是

压缩或解压时指定的压缩等级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

memLevel[MemLevel](#ZH-CN_TOPIC_0000002529285501__memlevel)否是

压缩时指定的使用内存等级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

strategy[CompressStrategy](#ZH-CN_TOPIC_0000002529285501__compressstrategy)否是

压缩时指定的压缩策略。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

parallel18+[ParallelStrategy](#ZH-CN_TOPIC_0000002529285501__parallelstrategy18)否是

压缩或解压时指定的串行或并行策略。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

pathSeparatorStrategy21+[PathSeparatorStrategy](#ZH-CN_TOPIC_0000002529285501__pathseparatorstrategy21)否是

解压时指定的压缩包内文件路径中分隔符的处理策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

#### CompressLevel

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明COMPRESS_LEVEL_NO_COMPRESSION0压缩率为0压缩等级。COMPRESS_LEVEL_BEST_SPEED1最佳速度压缩等级。COMPRESS_LEVEL_BEST_COMPRESSION9最佳压缩等级。COMPRESS_LEVEL_DEFAULT_COMPRESSION-1默认压缩等级。

#### MemLevel

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明MEM_LEVEL_MIN1zlib接口在压缩过程中最小使用内存。MEM_LEVEL_MAX9zlib接口在压缩过程中最大使用内存。MEM_LEVEL_DEFAULT8zlib接口在压缩过程中默认使用内存。

#### CompressStrategy

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明COMPRESS_STRATEGY_DEFAULT_STRATEGY0常规数据策略。COMPRESS_STRATEGY_FILTERED1过滤器产生的数据压缩策略。COMPRESS_STRATEGY_HUFFMAN_ONLY2霍夫曼编码格式压缩策略。COMPRESS_STRATEGY_RLE3游标编码压缩策略。COMPRESS_STRATEGY_FIXED4固定的压缩策略。

#### ParallelStrategy18+

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明PARALLEL_STRATEGY_SEQUENTIAL0默认值，串行压缩/解压策略。PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION1并行解压策略。

#### PathSeparatorStrategy21+

PathSeparatorStrategy作为[Options](#ZH-CN_TOPIC_0000002529285501__options)的一个属性，用于指定解压时目标压缩包内文件路径中分隔符的处理策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明PATH_SEPARATOR_STRATEGY_DEFAULT0默认值，压缩包内文件路径中的分隔符不做处理。PATH_SEPARATOR_STRATEGY_REPLACE_BACKSLASH1压缩包内文件路径中的反斜杠'\'替换为斜杠'/'。

#### ErrorCode(deprecated)

本模块首批接口从API version 7 开始支持。

从API Version 9开始，该模块不再维护。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明ERROR_CODE_OK0函数调用成功。ERROR_CODE_ERRNO-1函数调用失败。

#### CompressFlushMode12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明NO_FLUSH0默认值，表示正常操作。PARTIAL_FLUSH1在流中生成部分刷新点。SYNC_FLUSH2在保持压缩流状态的同时强制输出所有压缩数据。FULL_FLUSH3重置压缩状态。FINISH4压缩或解压缩过程结束。BLOCK5允许更精确的控制。TREES6实施过程中有特殊目的。

#### CompressMethod12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明DEFLATED8压缩方法。

#### ReturnStatus12+

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明OK0

函数调用成功。该接口支持在元服务中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_END1

函数调用成功，表示已处理了整个数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

NEED_DICT2

函数调用成功，表示需要预设字典才能继续解压缩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### ZStream12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明nextInArrayBuffer否是需要压缩的输入字节。availableInnumber否是nextIn可用的字节数。totalInnumber否是到目前为止读取的输入字节总数。nextOutArrayBuffer否是压缩后的输出字节。availableOutnumber否是nextOut的剩余可用字节数。totalOutnumber否是到目前为止输出字节总数。dataTypenumber否是关于数据类型的最佳猜测：deflate的二进制或文本，或inflate的解码状态。adlernumber否是未压缩数据的Adler-32或CRC-32值。

#### ZipOutputInfo12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明statusReturnStatus否否参考[ReturnStatus枚举定义](#ZH-CN_TOPIC_0000002529285501__returnstatus12)。destLennumber否否目标缓冲区的总长度。

#### DictionaryOutputInfo12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明statusReturnStatus否否参考[ReturnStatus枚举定义](#ZH-CN_TOPIC_0000002529285501__returnstatus12)。dictionaryLengthnumber否否字典的长度。

#### DecompressionOutputInfo12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明statusReturnStatus否否参考[ReturnStatus枚举定义](#ZH-CN_TOPIC_0000002529285501__returnstatus12)。destLengthnumber否否目标缓冲区的长度。sourceLengthnumber否否源缓冲区的长度。

#### DeflatePendingOutputInfo12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明statusReturnStatus否否参考[ReturnStatus枚举定义](#ZH-CN_TOPIC_0000002529285501__returnstatus12)。pendingnumber否否已生成的输出字节数。bitsnumber否否已生成的输出位数。

#### GzHeader12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明isTextboolean否是如果压缩数据被认为是文本，则为True。osnumber否是操作系统。timenumber否是修改时间。xflagsnumber否是额外标志。extraArrayBuffer否是额外字段。extraLennumber否是额外字段的长度。nameArrayBuffer否是文件名。commentArrayBuffer否是注释。hcrcboolean否是如果存在crc标头，则为True。doneboolean否是读取gzip标头后为True。

#### zlib.createGZip12+

createGZip(): Promise<GZip>

创建GZip对象，使用Promise异步回调。成功时返回Gzip对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[GZip](#ZH-CN_TOPIC_0000002529285501__gzip12)>Promise对象。返回GZip对象实例。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

zlib.createGZip().then((data) => {
  console.info('createGZip success');
})
```

#### zlib.createGZipSync12+

createGZipSync(): GZip

创建GZip对象。成功时返回GZip对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明[GZip](#ZH-CN_TOPIC_0000002529285501__gzip12)GZip对象实例。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';

let gzip = zlib.createGZipSync();
```

#### GZip12+

Gzip相关接口。

#### gzdopen12+

gzdopen(fd: number, mode: string): Promise<void>

将gzFile与文件描述符fd相关联，打开文件，用于进行读取并解压缩，或者压缩并写入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明fdnumber是文件描述符。通常情况下，通过系统调用“open”或其他方法获得的。modestring是用于指定访问模式。

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800002No such file or access mode error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzdopenDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzdopen");
  let path = pathDir + "/gzdopen/test.gz";
  let file = fs.openSync(path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  let gzip = zlib.createGZipSync();
  await gzip.gzdopen(file.fd, "wb");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzdopenDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzbuffer12+

gzbuffer(size: number):Promise<number>

为当前库函数设置内部缓冲区尺寸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明sizenumber是需要设置的内部缓冲区尺寸。

**返回值：**

类型说明Promise<number>Promise对象，成功时，返回0。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { zlib } from '@kit.BasicServicesKit';

async function gzbufferDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzbuffer");
  let path = pathDir + "/gzbuffer/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let result = await gzip.gzbuffer(648);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzbufferDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzopen12+

gzopen(path: string, mode: string): Promise<void>

打开位于指定路径的gzip(.gz)文件，用于进行读取并解压缩，或者压缩并写入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明pathstring是需要打开的文件路径。modestring是指定文件打开方法。

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800002No such file or access mode error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzopenDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzopen");
  let path = pathDir + "/gzopen/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzopenDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzeof12+

gzeof(): Promise<number>

检查gzip压缩文件的读取位置是否已到达文件的末尾。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<number>Promise对象，如果在读取时设置了文件的文件结束指示符，则返回1。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzeofDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzeof");
  let path = pathDir + "/gzeof/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View[i] = i;
  }
  let writeNum = await gzip.gzwrite(writeBufferWithData, 16)
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBufferWithData = new ArrayBuffer(20);
  let readNum = await gzip.gzread(readBufferWithData);
  let eofNum = await gzip.gzeof();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzeofDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzdirect12+

gzdirect(): Promise<number>

检查指定的gzip文件句柄文件是否直接访问原始未压缩数据，重新分配缓冲区。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<number>Promise对象，如果直接访问原始未压缩数据，则返回1。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzdirectDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzdirect");
  let path = pathDir + "/gzdirect/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let directNum = await gzip.gzdirect();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzdirectDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzclose12+

gzclose(): Promise<ReturnStatus>

清除文件的所有挂起输出，如有必要，关闭文件和释放（解）压缩状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象，返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800006Memory allocation failed.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzcloseDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzclose");
  let path = pathDir + "/gzclose/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzcloseDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzclearerr12+

gzclearerr(): Promise<void>

清除文件的错误和文件结束标志。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<void>Promise对象，无返回值。

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzclearerrDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzclearerr");
  let path = pathDir + "/gzclearerr/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View[i] = i;
  }
  let writeNum = await gzip.gzwrite(writeBufferWithData, 16)
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBufferWithData = new ArrayBuffer(20);
  let readNum = await gzip.gzread(readBufferWithData);
  let eofNum = await gzip.gzeof();
  await gzip.gzclearerr();
  let eofNumClear = await gzip.gzeof();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzclearerrDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzerror12+

gzerror(): Promise<GzErrorOutputInfo>

文件上发生的最后一个错误的错误消息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[GzErrorOutputInfo](#ZH-CN_TOPIC_0000002529285501__gzerroroutputinfo12)>Promise对象，返回结果状态和出现的最后一个状态的状态消息。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzerrorDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzerror");
  let path = pathDir + "/gzerror/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View[i] = i;
  }
  try {
    await gzip.gzwrite(writeBufferWithData, -1);
  } catch (errData) {
    await gzip.gzerror().then((GzErrorOutputInfo) => {
      console.info('errCode', GzErrorOutputInfo.status);
      console.info('errMsg', GzErrorOutputInfo.statusMsg);
    })
  }
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzerrorDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzgetc12+

gzgetc(): Promise<number>

从文件中读取并解压缩一个字节。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<number>Promise对象，返回读取字符的ASCII值。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzgetcDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzgetc");
  let path = pathDir + "/gzgetc/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzputc(1);
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let result = await gzip.gzgetc();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzgetcDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzflush12+

gzflush(flush: CompressFlushMode): Promise<ReturnStatus>

将所有挂起的输出刷新到文件中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明flushCompressFlushMode是控制刷新操作的行为，参考[CompressFlushMode枚举](#ZH-CN_TOPIC_0000002529285501__compressflushmode12)的定义。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象，返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzflushDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzflush");
  let path = pathDir + "/gzflush/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let flushNum = await gzip.gzflush(zlib.CompressFlushMode.NO_FLUSH);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzflushDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzfwrite12+

gzfwrite(buf: ArrayBuffer, size: number, nitems: number): Promise<number>

将大小为size，数量为nitems的数据块从buf压缩并写入文件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明bufArrayBuffer是要将数据写入的缓冲区。sizenumber是单个数据块中的字节数。nitemsnumber是要写入的数据块数。

**返回值：**

类型说明Promise<number>Promise对象，返回写入大小为size的完整数据块的数目。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzfwriteDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzfwrite");
  let path = pathDir + "/gzfwrite/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let bufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(bufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View[i] = i;
  }
  let result = await gzip.gzfwrite(bufferWithData, 8, 2)
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzfwriteDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzfread12+

gzfread(buf: ArrayBuffer, size: number, nitems: number): Promise<number>

从gzip压缩文件中解压缩并读取数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明bufArrayBuffer是用于存储读取结果的目标缓冲区。sizenumber是单个数据块中的字节数。nitemsnumber是要写入的数据块数。

**返回值：**

类型说明Promise<number>Promise对象，返回读取大小为size的完整数据块的数目。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzfreadDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzfread");
  let path = pathDir + "/gzfread/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBuffer = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBuffer);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View[i] = i;
  }
  await gzip.gzfwrite(writeBuffer, 8, 2);
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBuffer = new ArrayBuffer(16);
  let result = await gzip.gzfread(readBuffer, 8, 2);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzfreadDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzclosew12+

gzclosew(): Promise<ReturnStatus>

与gzclose()功能相同，仅适用于写入或追加时。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象，返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800006Memory allocation failed.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzclosewDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzclosew");
  let path = pathDir + "/gzclosew/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclosew();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzclosewDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzcloser12+

gzcloser(): Promise<ReturnStatus>

与gzclose()功能相同，仅适用于读取时。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象，返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzcloserDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzcloser");
  let path = pathDir + "/gzcloser/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  await gzip.gzcloser();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzcloserDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzwrite12+

gzwrite(buf: ArrayBuffer, len: number): Promise<number>

将buf中的len长度的未压缩字节进行压缩并将其写入文件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明bufArrayBuffer是对象指向要写入的数据缓冲区。lennumber是未压缩字节长度。

**返回值：**

类型说明Promise<number>Promise对象，返回写入的未压缩字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzwriteDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzwrite");
  let path = pathDir + "/gzwrite/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let bufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(bufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View[i] = i;
  }
  let result = await gzip.gzwrite(bufferWithData, 16);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzwriteDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzungetc12+

gzungetc(c: number): Promise<number>

将c推回到流中，以便在下次读取文件时将作为第一个字符读取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明cnumber是回退到输入流之前的字符。

**返回值：**

类型说明Promise<number>Promise对象，返回推送的字符。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzungetcDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzungetc");
  let path = pathDir + "/gzungetc/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  await gzip.gzread(new ArrayBuffer(1));
  let result = await gzip.gzungetc(1);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzungetcDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gztell12+

gztell(): Promise<number>

返回文件中下一个gzread或gzwrite的起始位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<number>Promise对象，返回文件种下一个gzread或gzwrite的起始位置。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gztellDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gztell");
  let path = pathDir + "/gztell/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gztell();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gztellDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzsetparams12+

gzsetparams(level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>

动态更新文件的压缩级别和压缩策略。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明levelCompressLevel是压缩级别，参考[CompressLevel枚举定义](#ZH-CN_TOPIC_0000002529285501__compresslevel)。strategyCompressStrategy是压缩策略，参考[CompressStrategy枚举定义](#ZH-CN_TOPIC_0000002529285501__compressstrategy)。

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象，返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzsetparamsDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzsetparams");
  let path = pathDir + "/gzsetparams/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzsetparams(zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
    zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzsetparamsDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzseek12+

gzseek(offset: number, whence: OffsetReferencePoint): Promise<number>

将起始位置设置为相对于文件中下一个gzread或gzwrite的偏移位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明offsetnumber是目标偏移位置。whenceOffsetReferencePoint是定义偏移的参考点，参考[OffsetReferencePoint枚举定义](#ZH-CN_TOPIC_0000002529285501__offsetreferencepoint12)。

**返回值：**

类型说明Promise<number>Promise对象，返回从未压缩流开始以字节为单位测量的结果偏移位置。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzseekDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzseek");
  let path = pathDir + "/gzseek/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzseek(2, zlib.OffsetReferencePoint.SEEK_CUR);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzseekDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzrewind12+

gzrewind(): Promise<ReturnStatus>

将文件指针重新定位到文件的开头，此功能仅用于读取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<[ReturnStatus](#ZH-CN_TOPIC_0000002529285501__returnstatus12)>Promise对象，返回结果状态。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzrewindDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzrewind");
  let path = pathDir + "/gzrewind/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let result = await gzip.gzrewind();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzrewindDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzread12+

gzread(buf: ArrayBuffer): Promise<number>

从文件中读取最多len个未压缩字节并将其解压缩到buf中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明bufArrayBuffer是目标偏移位置。

**返回值：**

类型说明Promise<number>Promise对象，返回实际读取的未压缩字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzreadDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzread");
  let path = pathDir + "/gzread/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBuffer = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBuffer);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View[i] = i;
  }
  await gzip.gzwrite(writeBuffer, 16);
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBuffer = new ArrayBuffer(16);
  let result = await gzip.gzread(readBuffer);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzreadDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzputs12+

gzputs(str: string): Promise<number>

压缩给定的以null结尾的字符串并将其写入文件，不包括终止的null字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明strstring是格式化描述符和纯文本。

**返回值：**

类型说明Promise<number>Promise对象，返回写入的字符数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzputsDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzputs");
  let path = pathDir + "/gzputs/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzputs("hello");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzputsDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzputc12+

gzputc(char: number): Promise<number>

将转换为无符号字符的c压缩并写入文件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明charnumber是写入字符ASCII。

**返回值：**

类型说明Promise<number>Promise对象，返回已写入的值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzputcDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzputc");
  let path = pathDir + "/gzputc/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzputc(0);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzputcDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzprintf12+

gzprintf(format: string, ...args: Array<string | number>): Promise<number>

在字符串格式的控制下，将参数转换和格式化后，压缩并写入文件，如fprintf中所示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明formatstring是格式化描述符和纯文本。...argsArray<string | number>否可变参数列表。

**返回值：**

类型说明Promise<number>Promise对象，返回实际写入的未压缩字节数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800004Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzprintfDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzprintf");
  let path = pathDir + "/gzprintf/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzprintf("name is %s, age is %d", "Tom", 23);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzprintfDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzoffset12+

gzoffset(): Promise<number>

返回文件的当前压缩（实际）读或写偏移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

类型说明Promise<number>Promise对象，返回文件的当前压缩（实际）读或写偏移量。

**错误码：**

以下错误码的详细介绍请参见[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzoffsetDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzoffset");
  let path = pathDir + "/gzoffset/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzoffset();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzoffsetDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### gzgets12+

gzgets(buf: ArrayBuffer): Promise<string>

从文件中读取字节并将其解压缩到buf中，直到读取len-1字符，或者直到读取换行符并将其传输到buf，或者遇到文件结束条件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

参数名类型必填说明bufArrayBuffer是存储读取的行数据。

**返回值：**

类型说明Promise<string>Promise对象，返回以null结尾的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.zlib错误码](zlib子系统错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter types;

3. Parameter verification failed.

17800009Internal structure error.

**示例：**

```ets
import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzgetsDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzgets");
  let path = pathDir + "/gzgets/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzputs("hello");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let bufferWithData = new ArrayBuffer(16);
  let result = await gzip.gzgets(bufferWithData);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzgetsDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### GzErrorOutputInfo12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称类型只读可选说明statusReturnStatus否否返回zlib文件状态码，参考ReturnStatus的定义。statusMsgstring否否zlib文件上发生的最后一个状态的状态消息。

#### OffsetReferencePoint12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

名称值说明SEEK_SET0从文件开头查找。SEEK_CUR1从当前位置查找。