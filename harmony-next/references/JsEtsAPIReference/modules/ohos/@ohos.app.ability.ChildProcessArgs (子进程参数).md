# @ohos.app.ability.ChildProcessArgs (子进程参数)

传递到子进程的参数。[childProcessManager](@ohos.app.ability.childProcessManager (子进程管理).md)启动子进程时，可以通过ChildProcessArgs传递参数到子进程中。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { ChildProcessArgs } from '@kit.AbilityKit';
```

#### ChildProcessArgs

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entryParams | string | 否 | 是 | 开发者自定义参数，透传到子进程中。可以在ChildProcess.onStart方法中通过args.entryParams获取，entryParams支持传输的最大数据量为150KB。 |
| fds | Record<string, number> | 否 | 是 | 文件描述符句柄集合，用于主进程和子进程通信，通过key-value的形式传入到子进程中，其中key为自定义字符串，value为文件描述符句柄。可以在ChildProcess.onStart方法中通过args.fds获取fd句柄。 说明： - fds最多支持16组，每组key的最大长度为20字符。 - 传递到子进程中句柄数字可能会变，但是指向的文件是一致的。 |

**示例：**

示例中的context的获取方式请参见[获取UIAbility的上下文信息](../../guides/UIAbility组件基本用法.md#获取uiability的上下文信息)。

```ets
// 主进程中:
import { common, ChildProcessArgs, childProcessManager } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

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
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let path = context.filesDir + "/test.txt";
            let file = fileIo.openSync(path, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
            let args: ChildProcessArgs = {
              entryParams: "testParam",
              fds: {
                "key1": file.fd
              }
            };
            childProcessManager.startArkChildProcess("entry/./ets/process/DemoProcess.ets", args);
          });
      }
      .width('100%')
    }
    .height('100%')
  }
```

```ets
// 子进程中:
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ..
  }
```