# @ohos.document (文件交互)

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口从API version 9开始废弃。不建议使用以下接口，调用以下接口将抛出异常。

#### 导入模块

```ets
import document from '@ohos.document';
```

#### document.choose(deprecated)

choose(types?: string[]): Promise<string>

通过文件管理器选择文件，异步返回文件URI，使用promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明typesstring[]否限定文件选择的类型

**返回值：**

类型说明Promise<string>异步返回文件URI（注：当前返回错误码）

**示例：**

```ets
let types: Array<string> = [];
document.choose(types);
```

#### document.choose(deprecated)

choose(callback:AsyncCallback<string>): void

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是异步获取对应文件URI（注：当前返回错误码）

**示例：**

```ets
let uri: string = "";
document.choose((err: TypeError, uri: string) => {
  //do something with uri
});
```

#### document.choose(deprecated)

choose(types:string[], callback:AsyncCallback<string>): void

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明typesstring[]是限定选择文件的类型callbackAsyncCallback<string>是异步获取对应文件URI（注：当前返回错误码）

**示例：**

```ets
let types: Array<string> = [];
let uri: string = "";
document.choose(types, (err: TypeError, uri: string) => {
  //do something with uri
});
```

#### document.show(deprecated)

show(uri:string, type:string):Promise<void>

异步打开URI对应的文件，使用promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明uristring是待打开的文件URItypestring是待打开文件的类型

**返回值：**

类型说明Promise<void>Promise回调返回void表示成功打开文件（注：当前返回错误码）

**示例：**

```ets
let type: string = "";
let uri: string = "";
document.show(uri, type);
```

#### document.show(deprecated)

show(uri:string, type:string, callback:AsyncCallback<void>): void

异步打开URI对应的文件，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

参数名类型必填说明uristring是待打开的文件URItypestring是待打开文件的类型callbackAsyncCallback<void>是异步打开uri对应文件（注：当前返回错误码）

**示例：**

```ets
let type: string = "";
let uri: string = "";
document.show(uri, type, (err: TypeError) => {
  //do something
});
```