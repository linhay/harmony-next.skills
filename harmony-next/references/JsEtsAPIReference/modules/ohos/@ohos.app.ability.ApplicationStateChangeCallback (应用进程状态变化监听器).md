# @ohos.app.ability.ApplicationStateChangeCallback (应用进程状态变化监听器)

本模块用于监听当前应用进程的状态变化。为了便于表述，下文中将“应用进程”简称为“进程”。

开发者可调用[ApplicationContext.on('applicationStateChange')](ApplicationContext (应用上下文).md#ZH-CN_TOPIC_0000002553360493__applicationcontextonapplicationstatechange10)方法传入自定义ApplicationStateChangeCallback来监听当前进程的前后台状态变化，从而根据进程前后台状态变化来执行某些操作。例如，统计进程前后台时长、或者当进程退到后台时清理内存缓存。


本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 约束限制

该模块仅支持监听当前进程的前后台状态变化。如果需要监听整个应用的前后台状态变化，可使用[ApplicationStateObserver.onForegroundApplicationChanged](ApplicationStateObserver.md#ZH-CN_TOPIC_0000002522240570__applicationstateobserveronforegroundapplicationchanged)。


进程的前后台状态不同于应用的前后台状态，两者的差别如下：

- 进程的前后台状态：如果进程中存在任何前台状态的UIAbility/UIExtensionAbility或可见窗口，则认为进程状态为前台，反之为后台。
- 应用的前后台状态：如果应用下有任何一个进程状态为前台，则认为应用状态为前台，反之为后台。

#### 导入模块

```ets
import { ApplicationStateChangeCallback } from '@kit.AbilityKit';
```

#### ApplicationStateChangeCallback.onApplicationForeground

onApplicationForeground(): void

当前进程从后台切换到前台时触发回调。当该回调触发时，并不表示进程已完全处于前台状态，而是即将进入前台状态，此时无法执行需要依赖前台状态的操作（例如启动其他UIAbility）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

参见[onApplicationBackground](#ZH-CN_TOPIC_0000002553200491__applicationstatechangecallbackonapplicationbackground)。

#### ApplicationStateChangeCallback.onApplicationBackground

onApplicationBackground(): void

当前进程从前台切换到后台时触发回调。当该回调触发时，表示进程已完全处于后台状态，可以执行适合在后台状态下完成的操作（例如清理内存缓存）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```ets
import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateChangeCallback: ApplicationStateChangeCallback = {
  onApplicationForeground() {
    console.info('applicationStateChangeCallback onApplicationForeground');
  },
  onApplicationBackground() {
    console.info('applicationStateChangeCallback onApplicationBackground');
  }
};

export default class MyAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    // 1.获取applicationContext
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2.通过applicationContext注册当前进程状态监听
      if (applicationContext != undefined) {
        applicationContext.on('applicationStateChange', applicationStateChangeCallback);
      }
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
    console.info('Register applicationStateChangeCallback');
  }
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      // 1.通过applicationContext解除注册当前进程状态监听
      if (applicationContext != undefined) {
        applicationContext.off('applicationStateChange', applicationStateChangeCallback);
      }
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
```