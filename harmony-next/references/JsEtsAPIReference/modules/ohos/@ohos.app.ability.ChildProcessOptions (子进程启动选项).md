# @ohos.app.ability.ChildProcessOptions (子进程启动选项)

子进程的启动配置选项。通过[childProcessManager](@ohos.app.ability.childProcessManager (子进程管理).md)启动子进程时，可以通过ChildProcessOptions配置子进程启动选项。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { ChildProcessOptions } from '@kit.AbilityKit';
```

#### ChildProcessOptions

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isolationMode | boolean | 否 | 是 | 控制子进程的沙箱隔离级别及网络访问权限。true表示子进程运行在独立沙箱环境中，且无法访问网络；false表示子进程与主进程共享沙箱和网络环境。默认为false。 |
| isolationUid21+ | boolean | 否 | 是 | 控制子进程是否使用独立的uid。true表示子进程运行拥有独立的uid；false表示子进程与主进程拥有相同uid。默认为false。仅在isolationMode为true时生效。 |

**示例：**

子进程部分：

```ets
// 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
// entry/src/main/ets/process/DemoProcess.ets
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {
  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    //子进程代码逻辑
}
```

主进程部分：

```ets
// 使用childProcessManager.startArkChildProcess方法启动子进程:
// entry/src/main/ets/pages/Index.ets
import { ChildProcessArgs, ChildProcessOptions, childProcessManager } from '@kit.AbilityKit';
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
              DemoProcess.toString(); // 这里调用DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
              let options: ChildProcessOptions = {
                isolationMode: false,
                isolationUid: false
              };
              let args: ChildProcessArgs = {
                entryParams: "testParam",
              };
              childProcessManager.startArkChildProcess("entry/ets/process/DemoProcess.ets", args, options)
                .then((pid) => {
                  console.info(`startChildProcess success, pid: ${pid}`);
                })
                .catch((err: BusinessError) => {
                  console.error(`startChildProcess business error, errorCode: ${err.code}, errorMsg:${err.message}`);
                });
            } catch (err) {
              console.error(`startChildProcess error, errorCode: ${err.code}, errorMsg:${err.message}`);
            }
          });
      }
      .width('100%')
    }
    .height('100%')
  }
```