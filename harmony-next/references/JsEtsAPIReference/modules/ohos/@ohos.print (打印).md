# @ohos.print (打印)

该模块为基本打印的操作API，提供调用基础打印功能的接口。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { print } from '@kit.BasicServicesKit';
```

#### PrintTask

打印任务完成后的事件监听回调接口类。

#### on

on(type: 'block', callback: Callback<void>): void

注册打印任务阻塞的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听， 监听字段：block， 表示打印任务阻塞。 |
callbackCallback<void>是回调函数，通知调用方打印任务阻塞。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码]([打印服务错误码](../../errors/打印服务错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.on('block', () => {
        console.info('print state is block');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### on

on(type: 'succeed', callback: Callback<void>): void

注册打印任务成功的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听， 监听字段：succeed， 表示打印任务成功。 |
callbackCallback<void>是回调函数，通知调用方打印任务成功。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.on('succeed', () => {
        console.info('print state is succeed');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### on

on(type: 'fail', callback: Callback<void>): void

注册打印任务失败的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听， 监听字段：fail， 表示打印任务失败。 |
callbackCallback<void>是回调函数，通知调用方打印任务失败。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.on('fail', () => {
        console.info('print state is fail');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### on

on(type: 'cancel', callback: Callback<void>): void

注册打印任务被取消的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听， 监听字段：cancel， 表示打印任务被取消。 |
callbackCallback<void>是回调函数，通知调用方打印任务被取消。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.on('cancel', () => {
        console.info('print state is cancel');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### off

off(type: 'block', callback?: Callback<void>): void

取消打印任务阻塞的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听， 监听字段：block， 表示打印任务阻塞。 |
callbackCallback<void>否回调函数，取消指定的打印任务阻塞事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.off('block', () => {
        console.info('unregister state block');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### off

off(type: 'succeed', callback?: Callback<void>): void

取消打印任务成功的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听， 监听字段：succeed， 表示打印任务成功。 |
callbackCallback<void>否回调函数，取消指定的打印任务成功事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.off('succeed', () => {
        console.info('unregister state succeed');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### off

off(type: 'fail', callback?: Callback<void>): void

取消打印任务失败的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听， 监听字段：fail， 表示打印任务失败。 |
callbackCallback<void>否回调函数，取消指定的打印任务失败事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.off('fail', () => {
        console.info('unregister state fail');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### off

off(type: 'cancel', callback?: Callback<void>): void

取消打印任务被取消的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听， 监听字段：cancel， 表示打印任务被取消。 |
callbackCallback<void>否回调函数，取消指定的打印任务被取消事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.off('cancel', () => {
        console.info('unregister state cancel');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### PrintDocumentAdapter11+

第三方应用程序实现此接口来渲染要打印的文件。

#### onStartLayoutWrite11+

onStartLayoutWrite(jobId: string, oldAttrs: PrintAttributes, newAttrs: PrintAttributes, fd: number, writeResultCallback: (jobId: string, writeResult: PrintFileCreationState) => void): void

打印服务会通过本接口将一个空的pdf文件的文件描述符传给三方应用，由三方应用使用新的打印参数更新待打印文件，更新文件完成后通过本接口的回调方法writeResultCallback通知打印服务。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| oldAttrs | PrintAttributes | 是 | 表示旧打印参数。 |
| newAttrs | PrintAttributes | 是 | 表示新打印参数。 |
| fd | number | 是 | 表示打印文件传给接口调用方的pdf文件的文件描述符。 |
| writeResultCallback | (jobId: string, writeResult: PrintFileCreationState) => void | 是 | 表示三方应用使用新的打印参数更新待打印文件完成后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';

class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
    onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
        writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
        writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
    };
    onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
        if (state == print.PrintDocumentAdapterState.PREVIEW_DESTROY) {
            console.info('PREVIEW_DESTROY');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_SUCCEED) {
            console.info('PRINT_TASK_SUCCEED');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_FAIL) {
            console.info('PRINT_TASK_FAIL');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_CANCEL) {
            console.info('PRINT_TASK_CANCEL');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_BLOCK) {
            console.info('PRINT_TASK_BLOCK');
        }
```

#### onJobStateChanged11+

onJobStateChanged(jobId: string, state: PrintDocumentAdapterState): void

实现这个接口来监听打印任务状态的改变。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| state | PrintDocumentAdapterState | 是 | 表示打印任务更改为该状态。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
    onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
        writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
        writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
    };
    onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
        if (state == print.PrintDocumentAdapterState.PREVIEW_DESTROY) {
            console.info('PREVIEW_DESTROY');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_SUCCEED) {
            console.info('PRINT_TASK_SUCCEED');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_FAIL) {
            console.info('PRINT_TASK_FAIL');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_CANCEL) {
            console.info('PRINT_TASK_CANCEL');
        } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_BLOCK) {
            console.info('PRINT_TASK_BLOCK');
        }
```

#### print.print10+

print(files: Array<string>, callback: AsyncCallback<PrintTask>): void

打印接口，传入文件进行打印，使用callback异步回调。拉起系统打印预览界面，需要使用[print](#ZH-CN_TOPIC_0000002522081596__printprint11-1)接口，传入context。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |
| callback | AsyncCallback<PrintTask> | 是 | 异步获取打印完成之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

//传入文件的uri
let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)], (err: BusinessError, printTask: print.PrintTask) => {
    if (err) {
        console.error('print err ' + JSON.stringify(err));
    } else {
        printTask.on('succeed', () => {
            console.info('print state is succeed');
        })
        // ...
    }
})
```

#### print.print10+

print(files: Array<string>): Promise<PrintTask>

打印接口，传入文件进行打印，使用Promise异步回调。拉起系统打印预览界面，需要使用[print](#ZH-CN_TOPIC_0000002522081596__printprint11-1)接口，传入context。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PrintTask> | 打印完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

//传入文件的uri
let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.on('succeed', () => {
        console.info('print state is succeed');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})
```

#### print.print11+

print(files: Array<string>, context: Context, callback: AsyncCallback<PrintTask>): void

打印接口，传入文件进行打印，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，当前支持的文件类型：".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", ".xml"。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |
| callback | AsyncCallback<PrintTask> | 是 | 异步获取打印完成之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button("打印").width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context, (err: BusinessError, printTask: print.PrintTask) => {
                        if (err) {
                            console.error('print err ' + JSON.stringify(err));
                        } else {
                            printTask.on('succeed', () => {
                                console.info('print state is succeed');
                            })
                            // ...
                        }
                    })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
```

#### print.print11+

print(files: Array<string>, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，当前支持的文件类型：".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", ".xml"。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PrintTask> | 打印完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button("打印").width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.on('succeed', () => {
                            console.info('print state is succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error('print err ' + JSON.stringify(error));
                    })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
```

#### print.print11+

print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，三方应用需要更新打印文件，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobName | string | 是 | 表示待打印文件名称，例如：test.pdf。打印侧会通过onStartLayoutWrite接口将空的pdf文件的fd传给接口调用方，由调用方使用新的打印参数更新待打印文件。 |
| printAdapter | PrintDocumentAdapter | 是 | 表示三方应用实现的PrintDocumentAdapter接口实例。 |
| printAttributes | PrintAttributes | 是 | 表示打印参数。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PrintTask> | 打印完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button("打印").width('90%').height(50).onClick(() => {
                    let jobName : string = "jobName";
                    let printAdapter : print.PrintDocumentAdapter | null = null;
                    let printAttributes : print.PrintAttributes = {
                        copyNumber: 1,
                        pageRange: {
                            startPage: 0,
                            endPage: 5,
                            pages: []
                        },
                        pageSize: print.PrintPageType.PAGE_ISO_A3,
                        directionMode: print.PrintDirectionMode.DIRECTION_MODE_AUTO,
                        colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
                        duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE
                    }
                    let context = this.getUIContext().getHostContext();

                    print.print(jobName, printAdapter, printAttributes, context).then((printTask: print.PrintTask) => {
                        printTask.on('succeed', () => {
                            console.info('print state is succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error('print err ' + JSON.stringify(error));
                    })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
```

#### PrintAttributes11+

定义打印参数的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| copyNumber | number | 否 | 是 | 表示文件打印份数。默认值为1。 |
| pageRange | PrintPageRange | 否 | 是 | 表示待打印文件的页面范围。 |
| pageSize | PrintPageSize | PrintPageType | 否 | 是 | 表示待打印文件的纸张类型。 |
| directionMode | PrintDirectionMode | 否 | 是 | 表示待打印文件的方向。 |
| colorMode | PrintColorMode | 否 | 是 | 表示待打印文件的色彩模式。 |
| duplexMode | PrintDuplexMode | 否 | 是 | 表示待打印文件的单双面模式。 |

#### PrintPageRange11+

定义打印范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startPage | number | 否 | 是 | 表示起始页。默认值为1。 |
| endPage | number | 否 | 是 | 表示结束页。默认值为待打印文件的最大页数。 |
| pages | Array<number> | 否 | 是 | 表示待打印的页面范围的集合。默认值为空。 |

#### PrintPageSize11+

定义打印页面尺寸的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示纸张类型ID。 |
| name | string | 否 | 否 | 表示纸张类型名称。 |
| width | number | 否 | 否 | 表示页面宽度，单位：毫米。 |
| height | number | 否 | 否 | 表示页面高度，单位：毫米。 |

#### PrintDirectionMode11+

打印纸张方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIRECTION_MODE_AUTO | 0 | 表示自动选择纸张方向。 |
| DIRECTION_MODE_PORTRAIT | 1 | 表示纵向打印。 |
| DIRECTION_MODE_LANDSCAPE | 2 | 表示横向打印。 |

#### PrintColorMode11+

打印色彩模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR_MODE_MONOCHROME | 0 | 表示黑白打印。 |
| COLOR_MODE_COLOR | 1 | 表示彩色打印。 |

#### PrintDuplexMode11+

打印单双面模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DUPLEX_MODE_NONE | 0 | 表示单面打印。 |
| DUPLEX_MODE_LONG_EDGE | 1 | 表示双面打印沿长边翻转。 |
| DUPLEX_MODE_SHORT_EDGE | 2 | 表示双面打印沿短边翻转。 |

#### PrintPageType11+

打印纸张类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAGE_ISO_A3 | 0 | 表示A3。 |
| PAGE_ISO_A4 | 1 | 表示A4。 |
| PAGE_ISO_A5 | 2 | 表示A5。 |
| PAGE_JIS_B5 | 3 | 表示B5。 |
| PAGE_ISO_C5 | 4 | 表示C5。 |
| PAGE_ISO_DL | 5 | 表示DL。 |
| PAGE_LETTER | 6 | 表示Letter。 |
| PAGE_LEGAL | 7 | 表示Legal。 |
| PAGE_PHOTO_4X6 | 8 | 表示4x6相纸。 |
| PAGE_PHOTO_5X7 | 9 | 表示5x7相纸。 |
| PAGE_INT_DL_ENVELOPE | 10 | 表示INT DL ENVELOPE。 |
| PAGE_B_TABLOID | 11 | 表示B Tabloid。 |

#### PrintDocumentAdapterState11+

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PREVIEW_DESTROY | 0 | 表示预览失败。 |
| PRINT_TASK_SUCCEED | 1 | 表示打印任务成功。 |
| PRINT_TASK_FAIL | 2 | 表示打印任务失败。 |
| PRINT_TASK_CANCEL | 3 | 表示打印任务取消。 |
| PRINT_TASK_BLOCK | 4 | 表示打印任务阻塞。 |

#### PrintFileCreationState11+

打印文件创建状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINT_FILE_CREATED | 0 | 表示打印文件创建成功。 |
| PRINT_FILE_CREATION_FAILED | 1 | 表示打印文件创建失败。 |
| PRINT_FILE_CREATED_UNRENDERED | 2 | 表示打印文件创建成功但未渲染。 |

#### PrinterState14+

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINTER_ADDED | 0 | 表示新打印机到达。 |
| PRINTER_REMOVED | 1 | 表示打印机丢失。 |
| PRINTER_CAPABILITY_UPDATED | 2 | 表示打印机更新。 |
| PRINTER_CONNECTED | 3 | 表示打印机已连接。 |
| PRINTER_DISCONNECTED | 4 | 表示打印机已断开连接。 |
| PRINTER_RUNNING | 5 | 表示打印机正在运行。 |

#### PrintJobState14+

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINT_JOB_PREPARE | 0 | 表示打印任务的初始状态。 |
| PRINT_JOB_QUEUED | 1 | 表示打印任务传送到打印机。 |
| PRINT_JOB_RUNNING | 2 | 表示执行打印任务。 |
| PRINT_JOB_BLOCKED | 3 | 表示打印任务已被阻止。 |
| PRINT_JOB_COMPLETED | 4 | 表示打印任务完成。 |

#### PrintJobSubState14+

打印任务子状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINT_JOB_COMPLETED_SUCCESS | 0 | 表示打印任务成功。 |
| PRINT_JOB_COMPLETED_FAILED | 1 | 表示打印任务失败。 |
| PRINT_JOB_COMPLETED_CANCELLED | 2 | 表示打印任务已取消。 |
| PRINT_JOB_COMPLETED_FILE_CORRUPTED | 3 | 表示打印文件已损坏。 |
| PRINT_JOB_BLOCK_OFFLINE | 4 | 表示打印处于离线状态。 |
| PRINT_JOB_BLOCK_BUSY | 5 | 表示打印被其他进程占用。 |
| PRINT_JOB_BLOCK_CANCELLED | 6 | 表示打印任务已取消。 |
| PRINT_JOB_BLOCK_OUT_OF_PAPER | 7 | 表示打印纸张用完。 |
| PRINT_JOB_BLOCK_OUT_OF_INK | 8 | 表示打印墨水用完。 |
| PRINT_JOB_BLOCK_OUT_OF_TONER | 9 | 表示打印墨粉用完。 |
| PRINT_JOB_BLOCK_JAMMED | 10 | 表示打印卡纸。 |
| PRINT_JOB_BLOCK_DOOR_OPEN | 11 | 表示打印盖开启。 |
| PRINT_JOB_BLOCK_SERVICE_REQUEST | 12 | 表示打印服务请求。 |
| PRINT_JOB_BLOCK_LOW_ON_INK | 13 | 表示打印墨水不足。 |
| PRINT_JOB_BLOCK_LOW_ON_TONER | 14 | 表示打印墨粉不足。 |
| PRINT_JOB_BLOCK_REALLY_LOW_ON_INK | 15 | 表示打印墨水量非常低。 |
| PRINT_JOB_BLOCK_BAD_CERTIFICATE | 16 | 表示打印证书有误。 |
| PRINT_JOB_BLOCK_DRIVER_EXCEPTION20+ | 17 | 表示打印驱动异常。 |
| PRINT_JOB_BLOCK_ACCOUNT_ERROR | 18 | 表示打印账户时出错。 |
| PRINT_JOB_BLOCK_PRINT_PERMISSION_ERROR | 19 | 表示打印许可异常。 |
| PRINT_JOB_BLOCK_PRINT_COLOR_PERMISSION_ERROR | 20 | 表示彩色打印权限异常。 |
| PRINT_JOB_BLOCK_NETWORK_ERROR | 21 | 表示设备未连接到网络。 |
| PRINT_JOB_BLOCK_SERVER_CONNECTION_ERROR | 22 | 表示无法连接服务器。 |
| PRINT_JOB_BLOCK_LARGE_FILE_ERROR | 23 | 表示打印大文件异常。 |
| PRINT_JOB_BLOCK_FILE_PARSING_ERROR | 24 | 表示文件分析异常。 |
| PRINT_JOB_BLOCK_SLOW_FILE_CONVERSION | 25 | 表示文件转换太慢。 |
| PRINT_JOB_RUNNING_UPLOADING_FILES | 26 | 表示正在上传文件。 |
| PRINT_JOB_RUNNING_CONVERTING_FILES | 27 | 表示正在转换文件。 |
| PRINT_JOB_BLOCK_FILE_UPLOADING_ERROR18+ | 30 | 表示文件上传失败。 |
| PRINT_JOB_BLOCK_DRIVER_MISSING20+ | 34 | 表示打印驱动缺失。 |
| PRINT_JOB_BLOCK_INTERRUPT20+ | 35 | 表示打印任务中断。 |
| PRINT_JOB_BLOCK_PRINTER_UNAVAILABLE20+ | 98 | 表示打印机不可用。 |
| PRINT_JOB_BLOCK_UNKNOWN | 99 | 表示打印未知问题。 |

#### PrintErrorCode14+

打印错误代码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| E_PRINT_NONE | 0 | 表示没有错误。 |
| E_PRINT_NO_PERMISSION | 201 | 表示没有许可。 |
| E_PRINT_INVALID_PARAMETER | 401 | 表示无效的参数。 |
| E_PRINT_GENERIC_FAILURE | 13100001 | 表示一般打印失败。 |
| E_PRINT_RPC_FAILURE | 13100002 | 表示RPC失败。 |
| E_PRINT_SERVER_FAILURE | 13100003 | 表示打印服务失败。 |
| E_PRINT_INVALID_EXTENSION | 13100004 | 表示打印扩展无效。 |
| E_PRINT_INVALID_PRINTER | 13100005 | 表示打印机无效。 |
| E_PRINT_INVALID_PRINT_JOB | 13100006 | 表示打印任务无效。 |
| E_PRINT_FILE_IO | 13100007 | 表示文件输入/输出错误。 |
| E_PRINT_TOO_MANY_FILES18+ | 13100010 | 表示文件数量超过上限，当前上限99个。 |

#### ApplicationEvent14+

打印应用事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APPLICATION_CREATED | 0 | 表示打印应用被拉起的事件。 |
| APPLICATION_CLOSED_FOR_STARTED | 1 | 表示由于点击打印而关闭打印应用的事件。 |
| APPLICATION_CLOSED_FOR_CANCELED | 2 | 表示由于点击取消而关闭打印应用的事件。 |

#### print.addPrinterToDiscovery14+

addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>

添加打印机到系统打印机发现列表，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerInformation | PrinterInformation | 是 | 表示新发现的打印机。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 添加打印机到系统打印机发现列表完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId',
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOps'
};
print.addPrinterToDiscovery(printerInformation).then(() => {
    console.info('addPrinterToDiscovery success');
}).catch((error: BusinessError) => {
    console.error('addPrinterToDiscovery error : ' + JSON.stringify(error));
})
```

#### print.updatePrinterInDiscovery14+

updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>

更新打印机能力到系统打印机发现列表，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerInformation | PrinterInformation | 是 | 表示待更新能力的打印机。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 更新打印机能力到系统打印机发现列表完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testPageSize : print.PrintPageSize = {
    id : 'ISO_A4',
    name : 'iso_a4_210x297mm',
    width : 8268,
    height : 11692
};

let testCapability : print.PrinterCapabilities = {
    supportedPageSizes : [testPageSize],
    supportedColorModes : [print.PrintColorMode.COLOR_MODE_MONOCHROME],
    supportedDuplexModes : [print.PrintDuplexMode.DUPLEX_MODE_NONE],
    supportedMediaTypes : ['stationery'],
    supportedQualities : [print.PrintQuality.QUALITY_NORMAL],
    supportedOrientations : [print.PrintOrientationMode.ORIENTATION_MODE_PORTRAIT],
    options : 'testOptions'
};

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId',
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    capability : testCapability,
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOptions'
};
print.updatePrinterInDiscovery(printerInformation).then(() => {
    console.info('updatePrinterInDiscovery success');
}).catch((error: BusinessError) => {
    console.error('updatePrinterInDiscovery error : ' + JSON.stringify(error));
})
```

#### print.removePrinterFromDiscovery14+

removePrinterFromDiscovery(printerId: string): Promise<void>

从系统打印机发现列表里移除打印机，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示待移除的打印机。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 从系统打印机发现列表里移除打印机完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = 'testPrinterId';
print.removePrinterFromDiscovery(printerId).then(() => {
    console.info('removePrinterFromDiscovery success');
}).catch((error: BusinessError) => {
    console.error('removePrinterFromDiscovery error : ' + JSON.stringify(error));
})
```

#### print.getPrinterInformationById14+

getPrinterInformationById(printerId: string): Promise<PrinterInformation>

根据打印机id获取打印机信息，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示待获取信息的打印机id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PrinterInformation> | 根据打印机id获取的对应打印机信息。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = 'testPrinterId';
print.getPrinterInformationById(printerId).then((printerInformation : print.PrinterInformation) => {
    console.info('getPrinterInformationById data : ' + JSON.stringify(printerInformation));
}).catch((error: BusinessError) => {
    console.error('getPrinterInformationById error : ' + JSON.stringify(error));
})
```

#### PrinterInformation14+

定义打印机信息的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| printerId | string | 否 | 否 | 表示打印机ID。 |
| printerName | string | 否 | 否 | 表示打印机名称。 |
| printerStatus | PrinterStatus | 否 | 否 | 表示当前打印机状态。 |
| description | string | 否 | 是 | 表示打印机说明。 |
| capability | PrinterCapabilities | 否 | 是 | 表示打印机能力。 |
| uri | string | 否 | 是 | 表示打印机uri。 |
| printerMake | string | 否 | 是 | 表示打印机型号。 |
| preferences18+ | PrinterPreferences | 否 | 是 | 表示打印机首选项。 |
| alias18+ | string | 否 | 是 | 表示打印机别名。 |
| options | string | 否 | 是 | 表示打印机详细信息。 |

#### PrinterCapabilities14+

定义打印机能力的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedPageSizes | Array<PrintPageSize> | 否 | 否 | 表示打印机支持的纸张尺寸列表。 |
| supportedColorModes | Array<PrintColorMode> | 否 | 否 | 表示打印机支持的色彩模式列表。 |
| supportedDuplexModes | Array<PrintDuplexMode> | 否 | 否 | 表示打印机支持的单双面模式列表。 |
| supportedMediaTypes | Array<string> | 否 | 是 | 表示打印机支持的纸张类型列表。 |
| supportedQualities | Array<PrintQuality> | 否 | 是 | 表示打印机支持的打印质量列表。 |
| supportedOrientations | Array<PrintOrientationMode> | 否 | 是 | 表示打印机支持的打印方向列表。 |
| options | string | 否 | 是 | 表示打印机能力详细信息。 |

#### PrintQuality14+

打印质量的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| QUALITY_DRAFT | 3 | 表示经济的打印质量。 |
| QUALITY_NORMAL | 4 | 表示标准的打印质量。 |
| QUALITY_HIGH | 5 | 表示最佳的打印质量。 |

#### PrintOrientationMode14+

打印方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORIENTATION_MODE_PORTRAIT | 0 | 表示纵向打印。 |
| ORIENTATION_MODE_LANDSCAPE | 1 | 表示横向打印。 |
| ORIENTATION_MODE_REVERSE_LANDSCAPE | 2 | 表示横向翻转打印。 |
| ORIENTATION_MODE_REVERSE_PORTRAIT | 3 | 表示纵向翻转打印。 |
| ORIENTATION_MODE_NONE | 4 | 表示自适应方向打印。 |

#### PrinterStatus14+

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINTER_IDLE | 0 | 表示打印机空闲状态。 |
| PRINTER_BUSY | 1 | 表示打印机忙碌状态。 |
| PRINTER_UNAVAILABLE | 2 | 表示打印机脱机状态。 |

#### PrinterPreferences18+

定义打印机首选项的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultDuplexMode | PrintDuplexMode | 否 | 是 | 表示默认单双面模式。 |
| defaultPrintQuality | PrintQuality | 否 | 是 | 表示默认打印质量。 |
| defaultMediaType | string | 否 | 是 | 表示默认纸张类型。 |
| defaultPageSizeId | string | 否 | 是 | 表示默认纸张尺寸的ID，其范围包含国际标准化组织定义的标准纸张尺寸，如ISO_A4，和系统中定义的非标准的纸张尺寸，如Custom.178x254mm，表示这种纸张尺寸为178毫米 x 254毫米。 |
| defaultOrientation | PrintOrientationMode | 否 | 是 | 表示默认打印方向。 |
| borderless | boolean | 否 | 是 | 表示是否无边距打印，true表示无边距，false表示有边距。默认值为false。 |
| options | string | 否 | 是 | 表示打印机首选项中不在以上字段中的其他字段，查询打印机或者从打印机驱动获取，以json格式存储在string中。 |

#### PrinterEvent18+

打印机相关事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINTER_EVENT_ADDED | 0 | 表示打印机添加事件。 |
| PRINTER_EVENT_DELETED | 1 | 表示打印机删除事件。 |
| PRINTER_EVENT_STATE_CHANGED | 2 | 表示打印机状态变化事件。 |
| PRINTER_EVENT_INFO_CHANGED | 3 | 表示打印机信息变化事件。 |
| PRINTER_EVENT_PREFERENCE_CHANGED | 4 | 表示打印机首选项变化事件。 |
| PRINTER_EVENT_LAST_USED_PRINTER_CHANGED | 5 | 表示上次使用的打印机的变化事件。 |

#### DefaultPrinterType18+

默认打印类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT_PRINTER_TYPE_SET_BY_USER | 0 | 表示将用户手动设置的默认打印机作为当前默认打印机。 |
| DEFAULT_PRINTER_TYPE_LAST_USED_PRINTER | 1 | 表示自动将上次使用的打印机作为当前默认打印机。 |

#### print.getAddedPrinters18+

getAddedPrinters(): Promise<Array<string>>

获取系统中已添加的打印机列表，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | 获取系统中已添加的打印机列表的完成结果回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.getAddedPrinters().then((printers: string[]) => {
    console.info('getAddedPrinters success ' + JSON.stringify(printers));
    // ...
}).catch((error: BusinessError) => {
    console.error('failed to getAddedPrinters because ' + JSON.stringify(error));
})
```

#### PrinterChangeCallback18+

type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void

将打印机事件和打印机信息作为参数的回调方法。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | PrinterEvent | 是 | 表示打印机事件。 |
| printerInformation | PrinterInformation | 是 | 表示打印机信息。 |

#### print.on18+

on(type: 'printerChange', callback: PrinterChangeCallback): void

注册打印机变动事件回调，使用callback回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'printerChange' | 是 | 表示打印机变动事件。 |
| callback | PrinterChangeCallback | 是 | 打印机变动之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';

// Trigger this callback when a added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);
```

#### print.off18+

off(type: 'printerChange', callback?: PrinterChangeCallback): void

取消注册打印机变动事件回调，使用callback回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'printerChange' | 是 | 表示打印机变动事件。 |
| callback | PrinterChangeCallback | 否 | 表示取消注册打印机变动事件后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';

// Trigger this callback when a added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);
print.off('printerChange');
```

#### print.startDiscoverPrinter20+

startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备包含指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extensionList | Array<string> | 是 | 要加载的打印扩展能力列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |
| callback | AsyncCallback<void> | 是 | 异步开始发现打印机之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 加载所有打印扩展能力
let extensionList: string[] = [];
// 通过指定自己应用的包名，在发现时加载自己的打印扩展能力
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList, (err: BusinessError) => {
    if (err) {
        console.error('failed to start Discover Printer because : ' + JSON.stringify(err));
    } else {
        console.info('start Discover Printer success');
    }
})
```

#### print.startDiscoverPrinter20+

startDiscoverPrinter(extensionList: Array<string>): Promise<void>

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备包含指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extensionList | Array<string> | 是 | 要加载的打印扩展能力列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 开始发现打印机的完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 加载所有打印扩展能力
let extensionList: string[] = [];
// 通过指定自己应用的包名，在发现时加载自己的打印扩展能力
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList).then(() => {
    console.info('start Discovery success');
}).catch((error: BusinessError) => {
    console.error('failed to start Discovery because : ' + JSON.stringify(error));
})
```

#### print.stopDiscoverPrinter20+

stopDiscoverPrinter(callback: AsyncCallback<void>): void

停止发现打印机，使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 停止发现打印机的异步回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter((err: BusinessError) => {
    if (err) {
        console.error('failed to stop Discover Printer because : ' + JSON.stringify(err));
    } else {
        console.info('stop Discover Printer success');
    }
})
```

#### print.stopDiscoverPrinter20+

stopDiscoverPrinter(): Promise<void>

停止发现打印机，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 停止发现打印机的完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter().then(() => {
    console.info('stop Discovery success');
}).catch((error: BusinessError) => {
    console.error('failed to stop Discovery because : ' + JSON.stringify(error));
})
```

#### print.connectPrinter20+

connectPrinter(printerId: string, callback: AsyncCallback<void>): void

通过打印机ID连接打印机，使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 打印机ID。 |
| callback | AsyncCallback<void> | 是 | 通过打印机ID异步连接打印机的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId: string = 'printerId_32';
print.connectPrinter(printerId, (err: BusinessError) => {
    if (err) {
        console.error('failed to connect Printer because : ' + JSON.stringify(err));
    } else {
        console.info('start connect Printer success');
    }
})
```

#### print.connectPrinter20+

connectPrinter(printerId: string): Promise<void>

通过打印机ID连接打印机，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 打印机ID |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 通过打印机ID连接打印机完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](打印服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId: string = 'printerId_32';
print.connectPrinter(printerId).then(() => {
    console.info('start connect Printer success');
}).catch((error: BusinessError) => {
    console.error('failed to connect Printer because : ' + JSON.stringify(error));
})
```

**startPrint23+**

startPrint(job: PrintJobData): Promise<void>

打印接口，传入文件或者二进制数据进行打印，使用Promise异步回调。

需要权限： ohos.permission.PRINT

系统能力： SystemCapability.Print.PrintFramework

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| job | PrintJobData | 是 | 打印任务数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

示例：

```ets
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import fs from "@ohos.file.fs";

let tempPath = '/data/stroage/el2/base/haps/entry/files/note.jpg';
let file: fs.File;
file = fs.openSync(tempPath, 4);

let printJobData: print.printJobData = {
    printerId: "printerId",
    jobName: "jobName",
    documentFormat: print.PrintDocumentFormat.DOCUMENT_FORMAT_AUTO,
    docFlavor: print.DocFlavor.FILE_DESCRIPTOR,
    copyNumber: 1,
    isLandscape: 0,
    colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
    dulpexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE,
    pageSize: {id: "ISO_A4", name: "ISO_A4", width:8268, height: 11692},
    fdList: [file.fd],
}
print.startPrint(printJobData).then(() => {
    console.info('start print success');
}).catch((error: BusinessError) => {
    console.error('failed to print because : ' + JSON.stringify(error));
})
```

**PrintDocumentFormat23+**

打印数据格式的枚举。

系统能力： SystemCapability.Print.PrintFramework

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOCUMENT_FORMAT_AUTO | 0 | 表示自动检测格式。 |
| DOCUMENT_FORMAT_JPEG | 1 | 表示Jpeg格式。 |
| DOCUMENT_FORMAT_PDF | 2 | 表示PDF格式。 |
| DOCUMENT_FORMAT_POSTSCRIPT | 3 | 表示PostScript格式。 |
| DOCUMENT_FORMAT_TEXT | 4 | 表示文本格式。 |
| DOCUMENT_FORMAT_RAW | 5 | 表示RAW格式。 |

**DocFlavor23+**

打印数据来源形式的枚举。

系统能力： SystemCapability.Print.PrintFramework

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILE_DESCRIPTOR | 0 | 表示文件数据。 |
| BYTES | 1 | 表示二进制数据。 |

**printJobData23+**

定义打印任务的接口。

系统能力： SystemCapability.Print.PrintFramework

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| printerId | string | 否 | 否 | 表示打印机ID。 |
| jobName | string | 否 | 否 | 表示打印任务名称。 |
| documentFormat | PrintDocumentFormat | 否 | 否 | 表示打印数据格式。 |
| docFlavor | DocFlavor | 否 | 否 | 表示打印数据来源形式。 |
| copyNumber | number | 否 | 否 | 表示文件列表副本数。 |
| isLandscape | boolean | 否 | 否 | 表示是否横向打印。true表示横向打印，false表示纵向打印。默认值为false。 |
| colorMode | PrintColorMode | 否 | 否 | 表示色彩模式。 |
| duplexMode | PrintDuplexMode | 否 | 否 | 表示单双面打印模式。 |
| pageSize | PrintPageSize | 否 | 否 | 表示选定的页面尺寸。 |
| jobId | string | 否 | 是 | 表示打印任务的唯一标识符。 |
| fdList | Array<number> | 否 | 是 | 表示待打印文件fd列表。 |
| binaryData | Uint8Array | 否 | 是 | 表示待打印二进制数据。 |
| printQuality | PrintQuality | 否 | 是 | 表示打印质量。 |
| mediaType | string | 否 | 是 | 表示打印纸张类型。 |
| isBorderless | boolean | 否 | 是 | 表示是否无边框打印。true表示无边框打印，false表示有边框打印。默认值为true。 |
| isAutoRotate | boolean | 否 | 是 | 表示是否自动旋转页面。true表示自动旋转页面，false表示不自动旋转页面。默认值为true。 |
| isReverse | boolean | 否 | 是 | 表示是否逆序打印。true表示逆序打印，false表示顺序打印。默认值为false。 |
| isCollate | boolean | 否 | 是 | 表示打印顺序方式。true表示逐页打印，false表示逐份打印。默认值为true。 |
| isSequential | boolean | 否 | 是 | 表示是否按照页面顺序打印。 |
| options | string | 否 | 是 | 表示以JSON格式字符串化的对象。 |