# 应用启动框架AppStartup

本文根据华为开发者官网 `app-startup` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup>
更新时间：2026-04-30 06:29:39


## 概述
应用启动时通常需要执行一系列初始化启动任务，如果将启动任务都放在HAP的UIAbility组件的onCreate生命周期中，那么只能在主线程中依次执行，不但影响应用的启动速度，而且当启动任务过多时，任务之间复杂的依赖关系还会使得代码难以维护。
AppStartup提供了一种简单高效的应用启动方式，可以支持任务的异步启动，加快应用启动速度。同时，通过在一个配置文件中统一设置多个启动任务的执行顺序以及依赖关系，让执行启动任务的代码变得更加简洁清晰、容易维护。

## 约束限制
- 使用启动框架必须在HAP的module.json5配置文件中开启启动框架。
- ExtensionAbility组件启动场景单一，使用启动框架会带来额外开销，因此不支持ExtensionAbility组件启动时拉起启动框架。
- 启动任务之间或so预加载任务之间不允许存在循环依赖。

## 开发流程
- 定义启动框架配置文件：在资源文件目录下创建并定义启动框架配置文件。 创建启动框架配置文件：在资源文件目录下创建启动框架配置文件，并在module.json5配置文件中引用。
- 定义启动参数配置：在启动框架配置文件中添加启动参数的配置信息。
- 定义启动任务配置：在启动框架配置文件中添加启动任务的配置信息
- 定义预加载so任务配置：在启动框架配置文件中添加预加载so任务的配置信息。
- 设置启动参数：在启动参数文件中，设置超时时间和启动任务的监听器等参数。
- 为每个待初始化功能组件添加启动任务：通过实现StartupTask接口，启动框架将会按顺序执行初始化流程。
- 可选操作：开发者可以在复杂场景下更精细地控制启动框架的行为。 HSP与HAR中使用启动框架：在HSP与HAR中配置启动任务、so预加载任务。实现跨模块的启动任务依赖管理，提升大型应用的启动效率和代码可维护性。
- 修改启动模式：将启动任务、so预加载任务修改为手动模式，灵活控制任务执行时机，避免不必要的启动开销。
- 添加任务匹配规则：根据场景通过匹配规则过滤启动任务。精准控制任务执行范围，避免加载无关任务。
- 设置启动任务调度阶段：设置启动任务的调度阶段，提前执行任务，节省启动时间。

## 定义启动参数配置
在启动框架配置文件startup_config.json中，可以添加启动参数的配置信息。
- 在工程的“ets”目录下创建“startup”文件夹，并在“ets/startup”路径下创建启动参数配置文件。本例中，启动参数配置文件的文件名为StartupConfig.ets。
- 在启动框架配置文件startup_config.json中，添加启动参数配置文件的相关信息。 startup_config.json文件示例如下： ``` { "startupTasks": [ // 启动任务 ], "appPreloadHintStartupTasks": [ // 预加载so任务 ], "configEntry": "./ets/startup/StartupConfig.ets" // 启动参数的配置 } ```
表1 startup_config.json配置文件标签说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| startupTasks | 启动任务配置信息，详见定义启动任务配置。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| appPreloadHintStartupTasks | 预加载so任务配置信息，详见定义预加载so任务配置。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| configEntry | 启动参数配置文件所在路径。详见设置启动参数。 说明： - HSP、HAR中不允许配置configEntry字段。 - 如果应用开启了文件名混淆，则需要将文件路径添加到保留白名单中。具体操作详见ArkGuard混淆原理及功能的-keep-file-name部分。 | 字符串 | 该标签不可缺省。 |

## 设置启动参数
在启动参数配置文件（本文为“ets/startup/StartupConfig.ets”文件）中，使用StartupConfigEntry接口实现启动框架公共参数的配置，包括超时时间和启动任务的监听器等参数，其中需要用到如下接口：
- StartupConfig：用于设置任务超时时间和启动框架的监听器。
- StartupListener：用于监听启动任务是否执行成功。
```
import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
export default class MyStartupConfigEntry extends StartupConfigEntry {
onConfig() {
hilog.info(0x0000, 'testTag', `onConfig`);
let onCompletedCallback = (error: BusinessError) => {
hilog.info(0x0000, 'testTag', `onCompletedCallback`);
if (error) {
hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
error.message);
} else {
hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
}
};
let startupListener: StartupListener = {
'onCompleted': onCompletedCallback
};
let config: StartupConfig = {
'timeoutMs': 10000,
'startupListener': startupListener
};
return config;
}
// ···
}
```

## 添加任务匹配规则
在通过卡片、通知、意图调用等方式拉起某个页面时，为了实现功能服务一步直达，可以通过添加matchRules匹配规则，仅加载与当前场景相关的部分启动任务，无需加载全部默认的自动启动任务，以提高启动性能。
可以通过以下两种方式添加匹配规则：
- 通过matchRules中的uris、actions、insightIntents字段，根据UIAbility启动时的uri、action或意图名称，匹配不同场景启动任务及预加载so任务。
- 如果上述方式不能满足需求，可以通过matchRules中的customization自定义匹配规则。 表5 matchRules标签说明 | 属性名称 | 含义 | 数据类型 | 是否可缺省 | 适用场景 | | uris | 表示自动模式执行的任务的uri取值范围。当UIAbility启动时，会将Want中携带的uri属性，与此处配置的uris数组取值进行匹配。格式为scheme://host/path，uri中的其它内容会被忽略（如port、fragment等）。 | 字符串数组 | 可缺省，缺省值为空。 | 通过特定uri拉起UIAbility的场景。 | | actions | 表示自动模式执行的任务的action取值范围。当UIAbility启动时，会将Want中携带的action属性，与此处配置的actions数组取值进行匹配。 | 字符串数组 | 可缺省，缺省值为空。 | 通过特定action拉起UIAbility的场景。 | | insightIntents | 表示自动模式执行的任务的意图名称取值范围。当UIAbility启动时，会将意图名称与此处配置的insightIntents数组取值进行匹配。 | 字符串数组 | 可缺省，缺省值为空。 | 通过特定意图名称拉起UIAbility的场景。 | | customization | 表示自动模式执行的任务的自定义规则取值范围。通过实现StartupConfigEntry的onRequestCustomMatchRule接口返回自定义规则值。当UIAbility启动时，会将自定义规则值与此处配置的customization数组取值进行匹配。 说明： 仅支持startupTasks中的任务配置。 | 字符串数组 | 可缺省，缺省值为空。 | 如果使用uris、actions、insightIntents字段无法满足要求，可以使用customization自定义规则。 | uris、insightIntents、actions、customization任一属性匹配成功即为任务匹配成功。
- 匹配成功的任务及其依赖任务都将在自动模式执行。
- 所有任务均匹配失败，则按任务的excludeFromAutoStart配置处理。
下面以uri匹配（action和意图名称类似）和customization匹配来举例，介绍如何实现添加任务匹配规则来筛选启动任务。
场景1：uri匹配
假定需要用户点击通知消息跳转到通知详情页面时，仅自动执行StartupTask_004和libentry_006任务。若启动通知详情UIAbility时Want中的uri属性为test://com.example.startupdemo/notification，可以通过uri匹配。示例如下：
- 对定义启动任务配置步骤中的startup_config.json文件进行修改，增加StartupTask_004任务和libentry_006任务的matchRules配置。 ``` { "startupTasks": [ { "name": "StartupTask_004", "srcEntry": "./ets/startup/StartupTask_004.ets", "runOnThread": "taskPool", "waitOnMainThread": false, "matchRules": { "uris": [ "test://com.example.startupdemo/notification" ] } }, ], "appPreloadHintStartupTasks": [ { "name": "libentry_006", "srcEntry": "libentry_006.so", "runOnThread": "taskPool", "excludeFromAutoStart": true, "matchRules": { "uris": [ "test://com.example.startupdemo/notification" ] } } ], "configEntry": "./ets/startup/StartupConfig.ets" } ```
场景2：customization匹配
假定需要用户点击天气卡片跳转到天气界面时，仅自动执行StartupTask_006启动任务和excludeFromAutoStart=false配置的预加载so任务。若启动天气UIAbility时Want中传入的自定义参数fromType为card，可以通过customization匹配。示例如下：
- 对设置启动参数步骤中的MyStartupConfigEntry.ets文件进行修改，新增onRequestCustomMatchRule方法。 ``` import { StartupConfigEntry, Want } from '@kit.AbilityKit'; // ··· export default class MyStartupConfigEntry extends StartupConfigEntry { // ··· onRequestCustomMatchRule(want: Want): string { if (want?.parameters?.fromType == 'card') { return 'ruleCard'; } return ''; } } ```
- 对定义启动任务配置步骤中的startup_config.json文件进行修改，增加StartupTask_006任务的matchRules配置。预加载so任务不支持customization字段，按任务原有的excludeFromAutoStart配置处理。 ``` { "startupTasks": [ { "name": "StartupTask_006", "srcEntry": "./ets/startup/StartupTask_006.ets", "runOnThread": "mainThread", "waitOnMainThread": false, "excludeFromAutoStart": true, "matchRules": { "customization": [ "ruleCard" ] } } ], "configEntry": "./ets/startup/StartupConfig.ets" } ```
