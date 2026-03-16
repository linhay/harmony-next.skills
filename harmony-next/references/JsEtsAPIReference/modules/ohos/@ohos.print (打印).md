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

**参数名****类型****必填****说明**typestring是

注册监听，

监听字段：block，

表示打印任务阻塞。

callbackCallback<void>是回调函数，通知调用方打印任务阻塞。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**typestring是

注册监听，

监听字段：succeed，

表示打印任务成功。

callbackCallback<void>是回调函数，通知调用方打印任务成功。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**typestring是

注册监听，

监听字段：fail，

表示打印任务失败。

callbackCallback<void>是回调函数，通知调用方打印任务失败。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**typestring是

注册监听，

监听字段：cancel，

表示打印任务被取消。

callbackCallback<void>是回调函数，通知调用方打印任务被取消。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**typestring是

取消监听，

监听字段：block，

表示打印任务阻塞。

callbackCallback<void>否回调函数，取消指定的打印任务阻塞事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**typestring是

取消监听，

监听字段：succeed，

表示打印任务成功。

callbackCallback<void>否回调函数，取消指定的打印任务成功事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**typestring是

取消监听，

监听字段：fail，

表示打印任务失败。

callbackCallback<void>否回调函数，取消指定的打印任务失败事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**typestring是

取消监听，

监听字段：cancel，

表示打印任务被取消。

callbackCallback<void>否回调函数，取消指定的打印任务被取消事件订阅。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**jobIdstring是表示打印任务ID。oldAttrs[PrintAttributes](#ZH-CN_TOPIC_0000002529285499__printattributes11)是表示旧打印参数。newAttrs[PrintAttributes](#ZH-CN_TOPIC_0000002529285499__printattributes11)是表示新打印参数。fdnumber是表示打印文件传给接口调用方的pdf文件的文件描述符。writeResultCallback(jobId: string, writeResult: [PrintFileCreationState](#ZH-CN_TOPIC_0000002529285499__printfilecreationstate11)) => void是表示三方应用使用新的打印参数更新待打印文件完成后的回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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
    }
}
```

#### onJobStateChanged11+

onJobStateChanged(jobId: string, state: PrintDocumentAdapterState): void

实现这个接口来监听打印任务状态的改变。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

**参数名****类型****必填****说明**jobIdstring是表示打印任务ID。state[PrintDocumentAdapterState](#ZH-CN_TOPIC_0000002529285499__printdocumentadapterstate11)是表示打印任务更改为该状态。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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
    }
}
```

#### print.print10+

print(files: Array<string>, callback: AsyncCallback<PrintTask>): void

打印接口，传入文件进行打印，使用callback异步回调。拉起系统打印预览界面，需要使用[print](#ZH-CN_TOPIC_0000002529285499__printprint11-1)接口，传入context。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

**参数名****类型****必填****说明**filesArray<string>是待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。callbackAsyncCallback<[PrintTask](#ZH-CN_TOPIC_0000002529285499__printtask)>是异步获取打印完成之后的回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

打印接口，传入文件进行打印，使用Promise异步回调。拉起系统打印预览界面，需要使用[print](#ZH-CN_TOPIC_0000002529285499__printprint11-1)接口，传入context。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

**参数名****类型****必填****说明**filesArray<string>是待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。

**返回值：**

**类型****说明**Promise<[PrintTask](#ZH-CN_TOPIC_0000002529285499__printtask)>打印完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**filesArray<string>是待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。contextContext是用于拉起系统打印界面的UIAbilityContext。callbackAsyncCallback<[PrintTask](#ZH-CN_TOPIC_0000002529285499__printtask)>是异步获取打印完成之后的回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

#### print.print11+

print(files: Array<string>, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

**参数名****类型****必填****说明**filesArray<string>是待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。contextContext是用于拉起系统打印界面的UIAbilityContext。

**返回值：**

**类型****说明**Promise<[PrintTask](#ZH-CN_TOPIC_0000002529285499__printtask)>打印完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

#### print.print11+

print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，三方应用需要更新打印文件，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

**参数名****类型****必填****说明**jobNamestring是表示待打印文件名称，例如：test.pdf。打印侧会通过[onStartLayoutWrite](#ZH-CN_TOPIC_0000002529285499__onstartlayoutwrite11)接口将空的pdf文件的fd传给接口调用方，由调用方使用新的打印参数更新待打印文件。printAdapter[PrintDocumentAdapter](#ZH-CN_TOPIC_0000002529285499__printdocumentadapter11)是表示三方应用实现的[PrintDocumentAdapter](#ZH-CN_TOPIC_0000002529285499__printdocumentadapter11)接口实例。printAttributes[PrintAttributes](#ZH-CN_TOPIC_0000002529285499__printattributes11)是表示打印参数。contextContext是用于拉起系统打印界面的UIAbilityContext。

**返回值：**

**类型****说明**Promise<[PrintTask](#ZH-CN_TOPIC_0000002529285499__printtask)>打印完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

#### PrintAttributes11+

定义打印参数的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**copyNumbernumber否是表示文件打印份数。默认值为1。pageRange[PrintPageRange](#ZH-CN_TOPIC_0000002529285499__printpagerange11)否是表示待打印文件的页面范围。pageSize[PrintPageSize](#ZH-CN_TOPIC_0000002529285499__printpagesize11) | [PrintPageType](#ZH-CN_TOPIC_0000002529285499__printpagetype11)否是表示待打印文件的纸张类型。directionMode[PrintDirectionMode](#ZH-CN_TOPIC_0000002529285499__printdirectionmode11)否是表示待打印文件的方向。colorMode[PrintColorMode](#ZH-CN_TOPIC_0000002529285499__printcolormode11)否是表示待打印文件的色彩模式。duplexMode[PrintDuplexMode](#ZH-CN_TOPIC_0000002529285499__printduplexmode11)否是表示待打印文件的单双面模式。

#### PrintPageRange11+

定义打印范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**startPagenumber否是表示起始页。默认值为1。endPagenumber否是表示结束页。默认值为待打印文件的最大页数。pagesArray<number>否是表示待打印的页面范围的集合。默认值为空。

#### PrintPageSize11+

定义打印页面尺寸的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**idstring否否表示纸张类型ID。namestring否否表示纸张类型名称。widthnumber否否表示页面宽度，单位：毫米。heightnumber否否表示页面高度，单位：毫米。

#### PrintDirectionMode11+

打印纸张方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**DIRECTION_MODE_AUTO0表示自动选择纸张方向。DIRECTION_MODE_PORTRAIT1表示纵向打印。DIRECTION_MODE_LANDSCAPE2表示横向打印。

#### PrintColorMode11+

打印色彩模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**COLOR_MODE_MONOCHROME0表示黑白打印。COLOR_MODE_COLOR1表示彩色打印。

#### PrintDuplexMode11+

打印单双面模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**DUPLEX_MODE_NONE0表示单面打印。DUPLEX_MODE_LONG_EDGE1表示双面打印沿长边翻转。DUPLEX_MODE_SHORT_EDGE2表示双面打印沿短边翻转。

#### PrintPageType11+

打印纸张类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PAGE_ISO_A30表示A3。PAGE_ISO_A41表示A4。PAGE_ISO_A52表示A5。PAGE_JIS_B53表示B5。PAGE_ISO_C54表示C5。PAGE_ISO_DL5表示DL。PAGE_LETTER6表示Letter。PAGE_LEGAL7表示Legal。PAGE_PHOTO_4X68表示4x6相纸。PAGE_PHOTO_5X79表示5x7相纸。PAGE_INT_DL_ENVELOPE10表示INT DL ENVELOPE。PAGE_B_TABLOID11表示B Tabloid。

#### PrintDocumentAdapterState11+

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PREVIEW_DESTROY0表示预览失败。PRINT_TASK_SUCCEED1表示打印任务成功。PRINT_TASK_FAIL2表示打印任务失败。PRINT_TASK_CANCEL3表示打印任务取消。PRINT_TASK_BLOCK4表示打印任务阻塞。

#### PrintFileCreationState11+

打印文件创建状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PRINT_FILE_CREATED0表示打印文件创建成功。PRINT_FILE_CREATION_FAILED1表示打印文件创建失败。PRINT_FILE_CREATED_UNRENDERED2表示打印文件创建成功但未渲染。

#### PrinterState14+

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PRINTER_ADDED0表示新打印机到达。PRINTER_REMOVED1表示打印机丢失。PRINTER_CAPABILITY_UPDATED2表示打印机更新。PRINTER_CONNECTED3表示打印机已连接。PRINTER_DISCONNECTED4表示打印机已断开连接。PRINTER_RUNNING5表示打印机正在运行。

#### PrintJobState14+

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PRINT_JOB_PREPARE0表示打印任务的初始状态。PRINT_JOB_QUEUED1表示打印任务传送到打印机。PRINT_JOB_RUNNING2表示执行打印任务。PRINT_JOB_BLOCKED3表示打印任务已被阻止。PRINT_JOB_COMPLETED4表示打印任务完成。

#### PrintJobSubState14+

打印任务子状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PRINT_JOB_COMPLETED_SUCCESS0表示打印任务成功。PRINT_JOB_COMPLETED_FAILED1表示打印任务失败。PRINT_JOB_COMPLETED_CANCELLED2表示打印任务已取消。PRINT_JOB_COMPLETED_FILE_CORRUPTED3表示打印文件已损坏。PRINT_JOB_BLOCK_OFFLINE4表示打印处于离线状态。PRINT_JOB_BLOCK_BUSY5表示打印被其他进程占用。PRINT_JOB_BLOCK_CANCELLED6表示打印任务已取消。PRINT_JOB_BLOCK_OUT_OF_PAPER7表示打印纸张用完。PRINT_JOB_BLOCK_OUT_OF_INK8表示打印墨水用完。PRINT_JOB_BLOCK_OUT_OF_TONER9表示打印墨粉用完。PRINT_JOB_BLOCK_JAMMED10表示打印卡纸。PRINT_JOB_BLOCK_DOOR_OPEN11表示打印盖开启。PRINT_JOB_BLOCK_SERVICE_REQUEST12表示打印服务请求。PRINT_JOB_BLOCK_LOW_ON_INK13表示打印墨水不足。PRINT_JOB_BLOCK_LOW_ON_TONER14表示打印墨粉不足。PRINT_JOB_BLOCK_REALLY_LOW_ON_INK15表示打印墨水量非常低。PRINT_JOB_BLOCK_BAD_CERTIFICATE16表示打印证书有误。PRINT_JOB_BLOCK_DRIVER_EXCEPTION20+17表示打印驱动异常。PRINT_JOB_BLOCK_ACCOUNT_ERROR18表示打印账户时出错。PRINT_JOB_BLOCK_PRINT_PERMISSION_ERROR19表示打印许可异常。PRINT_JOB_BLOCK_PRINT_COLOR_PERMISSION_ERROR20表示彩色打印权限异常。PRINT_JOB_BLOCK_NETWORK_ERROR21表示设备未连接到网络。PRINT_JOB_BLOCK_SERVER_CONNECTION_ERROR22表示无法连接服务器。PRINT_JOB_BLOCK_LARGE_FILE_ERROR23表示打印大文件异常。PRINT_JOB_BLOCK_FILE_PARSING_ERROR24表示文件分析异常。PRINT_JOB_BLOCK_SLOW_FILE_CONVERSION25表示文件转换太慢。PRINT_JOB_RUNNING_UPLOADING_FILES26表示正在上传文件。PRINT_JOB_RUNNING_CONVERTING_FILES27表示正在转换文件。PRINT_JOB_BLOCK_FILE_UPLOADING_ERROR18+30表示文件上传失败。PRINT_JOB_BLOCK_DRIVER_MISSING20+34表示打印驱动缺失。PRINT_JOB_BLOCK_INTERRUPT20+35表示打印任务中断。PRINT_JOB_BLOCK_PRINTER_UNAVAILABLE20+98表示打印机不可用。PRINT_JOB_BLOCK_UNKNOWN99表示打印未知问题。

#### PrintErrorCode14+

打印错误代码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**E_PRINT_NONE0表示没有错误。E_PRINT_NO_PERMISSION201表示没有许可。E_PRINT_INVALID_PARAMETER401表示无效的参数。E_PRINT_GENERIC_FAILURE13100001表示一般打印失败。E_PRINT_RPC_FAILURE13100002表示RPC失败。E_PRINT_SERVER_FAILURE13100003表示打印服务失败。E_PRINT_INVALID_EXTENSION13100004表示打印扩展无效。E_PRINT_INVALID_PRINTER13100005表示打印机无效。E_PRINT_INVALID_PRINT_JOB13100006表示打印任务无效。E_PRINT_FILE_IO13100007表示文件输入/输出错误。E_PRINT_TOO_MANY_FILES18+13100010表示文件数量超过上限，当前上限99个。

#### ApplicationEvent14+

打印应用事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**APPLICATION_CREATED0表示打印应用被拉起的事件。APPLICATION_CLOSED_FOR_STARTED1表示由于点击打印而关闭打印应用的事件。APPLICATION_CLOSED_FOR_CANCELED2表示由于点击取消而关闭打印应用的事件。

#### print.addPrinterToDiscovery14+

addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>

添加打印机到系统打印机发现列表，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

**参数名****类型****必填****说明**printerInformation[PrinterInformation](#ZH-CN_TOPIC_0000002529285499__printerinformation14)是表示新发现的打印机。

**返回值：**

**类型****说明**Promise<void>添加打印机到系统打印机发现列表完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**printerInformation[PrinterInformation](#ZH-CN_TOPIC_0000002529285499__printerinformation14)是表示待更新能力的打印机。

**返回值：**

**类型****说明**Promise<void>更新打印机能力到系统打印机发现列表完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**printerIdstring是表示待移除的打印机。

**返回值：**

**类型****说明**Promise<void>从系统打印机发现列表里移除打印机完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**printerIdstring是表示待获取信息的打印机id。

**返回值：**

**类型****说明**Promise<[PrinterInformation](#ZH-CN_TOPIC_0000002529285499__printerinformation14)>根据打印机id获取的对应打印机信息。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**名称****类型****只读****可选****说明**printerIdstring否否表示打印机ID。printerNamestring否否表示打印机名称。printerStatus[PrinterStatus](#ZH-CN_TOPIC_0000002529285499__printerstatus14)否否表示当前打印机状态。descriptionstring否是表示打印机说明。capability[PrinterCapabilities](#ZH-CN_TOPIC_0000002529285499__printercapabilities14)否是表示打印机能力。uristring否是表示打印机uri。printerMakestring否是表示打印机型号。preferences18+[PrinterPreferences](#ZH-CN_TOPIC_0000002529285499__printerpreferences18)否是表示打印机首选项。alias18+string否是表示打印机别名。optionsstring否是表示打印机详细信息。

#### PrinterCapabilities14+

定义打印机能力的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**supportedPageSizesArray<[PrintPageSize](#ZH-CN_TOPIC_0000002529285499__printpagesize11)>否否表示打印机支持的纸张尺寸列表。supportedColorModesArray<[PrintColorMode](#ZH-CN_TOPIC_0000002529285499__printcolormode11)>否否表示打印机支持的色彩模式列表。supportedDuplexModesArray<[PrintDuplexMode](#ZH-CN_TOPIC_0000002529285499__printduplexmode11)>否否表示打印机支持的单双面模式列表。supportedMediaTypesArray<string>否是表示打印机支持的纸张类型列表。supportedQualitiesArray<[PrintQuality](#ZH-CN_TOPIC_0000002529285499__printquality14)>否是表示打印机支持的打印质量列表。supportedOrientationsArray<[PrintOrientationMode](#ZH-CN_TOPIC_0000002529285499__printorientationmode14)>否是表示打印机支持的打印方向列表。optionsstring否是表示打印机能力详细信息。

#### PrintQuality14+

打印质量的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**QUALITY_DRAFT3表示经济的打印质量。QUALITY_NORMAL4表示标准的打印质量。QUALITY_HIGH5表示最佳的打印质量。

#### PrintOrientationMode14+

打印方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**ORIENTATION_MODE_PORTRAIT0表示纵向打印。ORIENTATION_MODE_LANDSCAPE1表示横向打印。ORIENTATION_MODE_REVERSE_LANDSCAPE2表示横向翻转打印。ORIENTATION_MODE_REVERSE_PORTRAIT3表示纵向翻转打印。ORIENTATION_MODE_NONE4表示自适应方向打印。

#### PrinterStatus14+

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PRINTER_IDLE0表示打印机空闲状态。PRINTER_BUSY1表示打印机忙碌状态。PRINTER_UNAVAILABLE2表示打印机脱机状态。

#### PrinterPreferences18+

定义打印机首选项的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**defaultDuplexMode[PrintDuplexMode](#ZH-CN_TOPIC_0000002529285499__printduplexmode11)否是表示默认单双面模式。defaultPrintQuality[PrintQuality](#ZH-CN_TOPIC_0000002529285499__printquality14)否是表示默认打印质量。defaultMediaTypestring否是表示默认纸张类型。defaultPageSizeIdstring否是表示默认纸张尺寸的ID，其范围包含国际标准化组织定义的标准纸张尺寸，如ISO_A4，和系统中定义的非标准的纸张尺寸，如Custom.178x254mm，表示这种纸张尺寸为178毫米 x 254毫米。defaultOrientation[PrintOrientationMode](#ZH-CN_TOPIC_0000002529285499__printorientationmode14)否是表示默认打印方向。borderlessboolean否是表示是否无边距打印，true表示无边距，false表示有边距。默认值为false。optionsstring否是表示打印机首选项中不在以上字段中的其他字段，查询打印机或者从打印机驱动获取，以json格式存储在string中。

#### PrinterEvent18+

打印机相关事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**PRINTER_EVENT_ADDED0表示打印机添加事件。PRINTER_EVENT_DELETED1表示打印机删除事件。PRINTER_EVENT_STATE_CHANGED2表示打印机状态变化事件。PRINTER_EVENT_INFO_CHANGED3表示打印机信息变化事件。PRINTER_EVENT_PREFERENCE_CHANGED4表示打印机首选项变化事件。PRINTER_EVENT_LAST_USED_PRINTER_CHANGED5表示上次使用的打印机的变化事件。

#### DefaultPrinterType18+

默认打印类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**DEFAULT_PRINTER_TYPE_SET_BY_USER0表示将用户手动设置的默认打印机作为当前默认打印机。DEFAULT_PRINTER_TYPE_LAST_USED_PRINTER1表示自动将上次使用的打印机作为当前默认打印机。

#### print.getAddedPrinters18+

getAddedPrinters(): Promise<Array<string>>

获取系统中已添加的打印机列表，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

**类型****说明**Promise<Array<string>>获取系统中已添加的打印机列表的完成结果回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.

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

**参数名****类型****必填****说明**event[PrinterEvent](#ZH-CN_TOPIC_0000002529285499__printerevent18)是表示打印机事件。printerInformation[PrinterInformation](#ZH-CN_TOPIC_0000002529285499__printerinformation14)是表示打印机信息。

#### print.on18+

on(type: 'printerChange', callback: PrinterChangeCallback): void

注册打印机变动事件回调，使用callback回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

**参数名****类型****必填****说明**type'printerChange'是表示打印机变动事件。callback[PrinterChangeCallback](#ZH-CN_TOPIC_0000002529285499__printerchangecallback18)是打印机变动之后的回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**type'printerChange'是表示打印机变动事件。callback[PrinterChangeCallback](#ZH-CN_TOPIC_0000002529285499__printerchangecallback18)否表示取消注册打印机变动事件后的回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

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

**参数名****类型****必填****说明**extensionListArray<string>是要加载的[打印扩展能力](@ohos.app.ability.PrintExtensionAbility (打印扩展能力).md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。callbackAsyncCallback<void>是异步开始发现打印机之后的回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.

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

**参数名****类型****必填****说明**extensionListArray<string>是要加载的[打印扩展能力](@ohos.app.ability.PrintExtensionAbility (打印扩展能力).md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。

**返回值：**

**类型****说明**Promise<void>开始发现打印机的完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.

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

**参数名****类型****必填****说明**callbackAsyncCallback<void>是停止发现打印机的异步回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.

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

**类型****说明**Promise<void>停止发现打印机的完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.

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

**参数名****类型****必填****说明**printerIdstring是打印机ID。callbackAsyncCallback<void>是通过打印机ID异步连接打印机的回调。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.

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

**参数名****类型****必填****说明**printerIdstring是打印机ID

**返回值：**

**类型****说明**Promise<void>通过打印机ID连接打印机完成结果。

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](../../errors/打印服务错误码.md)。

错误码ID错误信息201the application does not have permission to call this function.

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