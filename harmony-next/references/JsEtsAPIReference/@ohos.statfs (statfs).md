# @ohos.statfs (statfs)

该模块提供文件系统相关存储信息的功能，向应用程序提供获取文件系统总字节数、空闲字节数的JS接口。

- 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块从API version 9开始废弃，建议使用[@ohos.file.statvfs](@ohos.file.statvfs (文件系统空间统计).md)替代。

#### 导入模块

```ets
import statfs from '@ohos.statfs';
```

#### Statfs.getFreeBytes

getFreeBytes(path:string):Promise<number>

异步方法获取指定文件系统空闲字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是需要查询的文件系统的文件路径

**返回值：**

类型说明Promise<number>返回空闲字节数

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let path = "/dev";
statfs.getFreeBytes(path).then((number: number) => {
  console.info("getFreeBytes promise successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getFreeBytes failed with error:" + JSON.stringify(err));
});
```

#### Statfs.getFreeBytes

getFreeBytes(path:string, callback:AsyncCallback<number>): void

异步方法获取指定文件系统空闲字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是需要查询的文件系统的文件路径callbackAsyncCallback<number>是异步获取空闲字节数之后的回调

**示例：**

```ets
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getFreeBytes(path, (err: BusinessError, freeBytes:Number) => {
    if (err) {
        console.error('getFreeBytes callback failed');
    } else {
        console.info('getFreeBytes callback success' + freeBytes);
    }
});
```

#### Statfs.getTotalBytes

getTotalBytes(path: string): Promise<number>

异步方法获取指定文件系统总字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是需要查询的文件系统的文件路径

**返回值：**

类型说明Promise<number>返回总字节数

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let path = "/dev";
statfs.getTotalBytes(path).then((number: number) => {
  console.info("getTotalBytes promise successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getTotalBytes failed with error:" + JSON.stringify(err));
});
```

#### Statfs.getTotalBytes

getTotalBytes(path: string, callback: AsyncCallback<number>): void

异步方法获取指定文件系统总字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

参数名类型必填说明pathstring是需要查询的文件系统的文件路径callbackAsyncCallback<number>是异步获取总字节数之后的回调

**示例：**

```ets
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalBytes(path, (err: BusinessError, totalBytes:Number) => {
    if (err) {
        console.error('getTotalBytes callback failed');
    } else {
        console.info('getTotalBytes callback success' + totalBytes);
    }
});
```