# @ohos.app.ability.ChildProcess (子进程基类)

开发者自定义子进程的基类。通过[childProcessManager](@ohos.app.ability.childProcessManager (子进程管理).md)启动子进程时，需要继承此类并重写入口方法。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { ChildProcess } from '@kit.AbilityKit';
```

#### ChildProcess.onStart

onStart(args?: ChildProcessArgs): void

子进程的入口方法，通过[childProcessManager](@ohos.app.ability.childProcessManager (子进程管理).md)启动子进程后调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明args12+[ChildProcessArgs](@ohos.app.ability.ChildProcessArgs (子进程参数).md)否传递到子进程的参数。

**示例：**

```ets
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ..
  }
}
```