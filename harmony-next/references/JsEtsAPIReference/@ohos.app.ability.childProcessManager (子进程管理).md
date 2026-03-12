# @ohos.app.ability.childProcessManager (子进程管理)

childProcessManager模块提供子进程管理能力，支持子进程创建和启动操作。

创建的子进程会随着父进程的退出而退出，无法脱离父进程独立运行。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 约束限制

-

通过本模块中接口创建的子进程有如下限制:

  - 创建的子进程不支持创建UI界面。
  - 创建的子进程不支持依赖Context的API调用（包括Context模块自身API及将Context实例作为入参的API）。
  - 创建的子进程内不支持再次创建子进程。

-

通过本模块中定义的创建子进程的接口和[native_child_process.h](native_child_process.h.md)中定义的创建子进程的接口启动的子进程总数最大为512个（系统资源充足情况下），其中[startChildProcess](#ZH-CN_TOPIC_0000002529284575__childprocessmanagerstartchildprocess)接口在SELF_FORK模式下启动的子进程不计入总数内。

#### 导入模块

```ets
import { childProcessManager } from '@kit.AbilityKit';
```

#### StartMode

子进程启动模式枚举。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明SELF_FORK0从App自身进程Fork子进程。以该模式启动的子进程会继承父进程资源，不能使用Binder IPC和其他进程通信，否则会导致子进程崩溃退出。APP_SPAWN_FORK1从AppSpawn Fork子进程。以该模式启动的子进程不会继承父进程资源，可以使用Binder IPC和其他进程通信。

#### childProcessManager.startChildProcess

startChildProcess(srcEntry: string, startMode: StartMode): Promise<number>

启动[ArkTS子进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#arkts子进程)。使用Promise异步回调。

调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](@ohos.app.ability.ChildProcess (子进程基类).md#ZH-CN_TOPIC_0000002497444604__childprocessonstart)函数，[ChildProcess.onStart](@ohos.app.ability.ChildProcess (子进程基类).md#ZH-CN_TOPIC_0000002497444604__childprocessonstart)函数执行完后子进程会自动销毁。

调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**参数：**

参数名类型必填说明srcEntrystring是

子进程源文件路径，只支持源文件放在entry类型的模块中，以src/main为根目录。例如子进程文件在entry模块下src/main/ets/process/DemoProcess.ets，则srcEntry为"./ets/process/DemoProcess.ets"。

另外，需要确保子进程源文件被其它文件引用到，防止被构建工具优化掉。（详见下方示例代码）

startMode[StartMode](#ZH-CN_TOPIC_0000002529284575__startmode)是子进程启动模式。

**返回值：**

类型说明Promise<number>Promise对象，返回子进程pid。

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.16000050Internal error.16000061Operation not supported.16000062The number of child processes exceeds the upper limit.

**示例：**

```ets
// 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
// entry/src/main/ets/process/DemoProcess.ets
import { ChildProcess } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {
  onStart() {
    console.info('DemoProcess OnStart() called');
  }
}
```

```ets
// 使用childProcessManager.startChildProcess方法启动子进程:
// entry/src/main/ets/tool/Tool.ets
import { childProcessManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import DemoProcess from '../process/DemoProcess';

try {
  DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
  childProcessManager.startChildProcess("./ets/process/DemoProcess.ets", childProcessManager.StartMode.SELF_FORK)
    .then((data) => {
      console.info(`startChildProcess success, pid: ${data}`);
    }, (err: BusinessError) => {
      console.error(`startChildProcess error, errorCode: ${err.code}`);
    })
} catch (err) {
  console.error(`startChildProcess error, errorCode: ${(err as BusinessError).code}, errorMsg: ${(err as BusinessError).message}.`);
}
```

#### childProcessManager.startChildProcess

startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<number>): void

启动[ArkTS子进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#arkts子进程)。使用callback异步回调。

调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](@ohos.app.ability.ChildProcess (子进程基类).md#ZH-CN_TOPIC_0000002497444604__childprocessonstart)函数，[ChildProcess.onStart](@ohos.app.ability.ChildProcess (子进程基类).md#ZH-CN_TOPIC_0000002497444604__childprocessonstart)函数执行完后子进程会自动销毁。

调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**参数：**

参数名类型必填说明srcEntrystring是

子进程源文件路径，只支持源文件放在entry类型的模块中，以src/main为根目录。例如子进程文件在entry模块下src/main/ets/process/DemoProcess.ets，则srcEntry为"./ets/process/DemoProcess.ets"。

另外，需要确保子进程源文件被其它文件引用到，防止被构建工具优化掉。（详见下方示例代码）

startMode[StartMode](#ZH-CN_TOPIC_0000002529284575__startmode)是子进程启动模式。callbackAsyncCallback<number>是回调函数。当子进程启动成功，err为undefined，data为获取到的子进程pid；否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.16000050Internal error.16000061Operation not supported.16000062The number of child processes exceeds the upper limit.

**示例：**

```ets
// 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
// entry/src/main/ets/process/DemoProcess.ets
import { ChildProcess } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {
  onStart() {
    console.info('DemoProcess OnStart() called');
  }
}
```

```ets
// 使用childProcessManager.startChildProcess方法启动子进程:
// entry/src/main/ets/tool/Tool.ets
import { childProcessManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import DemoProcess from '../process/DemoProcess';

try {
  DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
  childProcessManager.startChildProcess("./ets/process/DemoProcess.ets", childProcessManager.StartMode.SELF_FORK, (err, data) => {
    if (data) {
      console.info(`startChildProcess success, pid: ${data}`);
    } else {
      console.error(`startChildProcess error, errorCode: ${err.code}`);
    }
  });
} catch (err) {
  console.error(`startChildProcess error, errorCode: ${(err as BusinessError).code}, errorMsg: ${(err as BusinessError).message}.`);
}
```

#### childProcessManager.startArkChildProcess12+

startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>

启动[ArkTS子进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#arkts子进程)。使用Promise异步回调。

调用该接口创建的子进程不会继承父进程资源，子进程创建成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](@ohos.app.ability.ChildProcess (子进程基类).md#ZH-CN_TOPIC_0000002497444604__childprocessonstart)函数。[ChildProcess.onStart](@ohos.app.ability.ChildProcess (子进程基类).md#ZH-CN_TOPIC_0000002497444604__childprocessonstart)函数执行完后子进程不会自动销毁，需要子进程调用[process.abort](@ohos.process (获取进程相关的信息).md#ZH-CN_TOPIC_0000002497604752__processabort)销毁。调用该接口的进程销毁后，所创建的子进程也会一并销毁。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明srcEntrystring是

子进程源文件路径，不支持源文件放在HAR类型的模块中。由“模块名” + “/” + “文件路径”组成，文件路径以src/main为根目录。例如子进程文件在module1模块下src/main/ets/process/DemoProcess.ets，则srcEntry为"module1/ets/process/DemoProcess.ets"。

另外，需要确保子进程源文件被其它文件引用到，防止被构建工具优化掉。（详见下方示例代码）

args[ChildProcessArgs](@ohos.app.ability.ChildProcessArgs (子进程参数).md)是传递到子进程的参数。options[ChildProcessOptions](@ohos.app.ability.ChildProcessOptions (子进程启动选项).md)否子进程的启动配置选项。

**返回值：**

类型说明Promise<number>Promise对象，返回子进程pid。

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.801Capability not supported.16000050Internal error.16000061Operation not supported.16000062The number of child processes exceeds the upper limit.

**示例：**

子进程部分：

```ets
// 在module1模块的src/main/ets/process下创建DemoProcess.ets子进程类:
// module1/src/main/ets/process/DemoProcess.ets
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ..
  }
}
```

主进程部分，示例中的context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)：

```ets
// 使用childProcessManager.startArkChildProcess方法启动子进程:
// module1/src/main/ets/tool/Tool.ets
import { common, ChildProcessArgs, ChildProcessOptions, childProcessManager } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import DemoProcess from '../process/DemoProcess';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('Click')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let path = context.filesDir + "/test.txt";
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
              let args: ChildProcessArgs = {
                entryParams: "testParam",
                fds: {
                  "key1": file.fd
                }
              };
              let options: ChildProcessOptions = {
                isolationMode: false
              };
              childProcessManager.startArkChildProcess("module1/ets/process/DemoProcess.ets", args, options)
                .then((pid) => {
                  console.info(`startChildProcess success, pid: ${pid}`);
                })
                .catch((err: BusinessError) => {
                  console.error(`startChildProcess business error, errorCode: ${err.code}, errorMsg:${err.message}`);
                })
            } catch (err) {
              console.error(`startChildProcess error, errorCode: ${err.code}, errorMsg:${err.message}`);
            }
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### childProcessManager.startNativeChildProcess13+

startNativeChildProcess(entryPoint: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>

启动[Native子进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#native子进程)。使用Promise异步回调。

调用该接口创建的子进程不会继承父进程资源，子进程创建成功会返回子进程pid，然后加载参数中指定的动态链接库文件并执行子进程的入口函数，入口函数执行完后子进程会自动销毁。调用该接口的进程销毁后，所创建的子进程也会一并销毁。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明entryPointstring是子进程中调用动态库的符号和入口函数，中间用“:”隔开（例如“libentry.so:Main”)。args[ChildProcessArgs](@ohos.app.ability.ChildProcessArgs (子进程参数).md)是传递到子进程的参数。options[ChildProcessOptions](@ohos.app.ability.ChildProcessOptions (子进程启动选项).md)否子进程的启动配置选项。

**返回值：**

类型说明Promise<number>Promise对象，返回子进程pid。

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.801Capability not supported. Failed to call the API due to limited device capabilities.16000050Internal error.16000061Operation not supported.16000062The number of child processes exceeds the upper limit.

**示例：**

子进程部分，详见[Native子进程开发指导（C/C++）- 创建支持参数传递的Native子进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi_nativechildprocess_development_guideline#创建支持参数传递的native子进程)：

```ets
#include <AbilityKit/native_child_process.h>

extern "C" {

/**
 * 子进程的入口函数，实现子进程的业务逻辑
 * 函数名称可以自定义，在主进程调用OH_Ability_StartNativeChildProcess方法时指定，此示例中为Main
 * 函数返回后子进程退出
 */
void Main(NativeChildProcess_Args args)
{
    // 获取传入的entryPrams
    char *entryParams = args.entryParams;
    // 获取传入的fd列表，对应ChildProcessArgs中的args.fds
    NativeChildProcess_Fd *current = args.fdList.head;
    while (current != nullptr) {
        char *fdName = current->fdName;
        int32_t fd = current->fd;
        current = current->next;
        // 业务逻辑..
    }
}
} // extern "C"
```

主进程部分，示例中的context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)：

```ets
// 主进程：
// 使用childProcessManager.startNativeChildProcess方法启动子进程:
import { common, ChildProcessArgs, ChildProcessOptions, childProcessManager } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('Click')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let path = context.filesDir + "/test.txt";
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
              let args: ChildProcessArgs = {
                entryParams: "testParam",
                fds: {
                  "key1": file.fd
                }
              };
              let options: ChildProcessOptions = {
                isolationMode: false
              };
              childProcessManager.startNativeChildProcess("libentry.so:Main", args, options)
                .then((pid) => {
                  console.info(`startChildProcess success, pid: ${pid}`);
                })
                .catch((err: BusinessError) => {
                  console.error(`startChildProcess business error, errorCode: ${err.code}, errorMsg:${err.message}`);
                })
            } catch (err) {
              console.error(`startChildProcess error, errorCode: ${err.code}, errorMsg:${err.message}`);
            }
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}
```