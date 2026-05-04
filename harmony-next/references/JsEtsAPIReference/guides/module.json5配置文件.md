# module.json5配置文件

本文根据华为开发者官网 `module-configuration-file` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file>
更新时间：2026-04-30 06:24:23


## 配置文件示例
通过一个示例，整体了解module.json5配置文件。
```
{
"module": {
"name": "entry",
"type": "entry",
"description": "$string:module_desc",
"mainElement": "EntryAbility",
"deviceTypes": [
"tv",
"tablet"
],
"deliveryWithInstall": true,
"pages": "$profile:main_pages", // 资源配置，指向profile下面定义的配置文件main_pages.json
"appStartup": "$profile:app_startup_config",
"metadata": [
{
"name": "string",
"value": "string",
"resource": "$profile:distributionFilter_config"
},
// ...
],
"abilities": [
{
"name": "EntryAbility",
"srcEntry": "./ets/entryability/EntryAbility.ets",
"description": "$string:EntryAbility_desc",
"icon": "$media:layered_image",
"label": "$string:EntryAbility_label",
"startWindow": "$profile:start_window",
"startWindowIcon": "$media:icon",
"startWindowBackground": "$color:start_window_background",
"exported": true,
"skills": [
// ...
{
"entities": [
"entity.system.home"
],
"actions": [
"ohos.want.action.home"
]
}
],
// ...
"continueType": [
"continueType1"
],
"continueBundleName": [
"com.example.myapplication1",
"com.example.myapplication2"
],
}
],
"requestPermissions": [
{
"name": "ohos.permission.ACCESS_BLUETOOTH",
"reason": "$string:reason",
"usedScene": {
"abilities": [
"EntryAbility"
],
"when": "inuse"
}
}
],
"querySchemes": [
"app1Scheme",
"app2Scheme"
],
"routerMap": "$profile:router_map",
"appEnvironments": [
{
"name": "name1",
"value": "value1"
}
],
"fileContextMenu": "$profile:menu", // 资源配置，指向profile下面定义的配置文件menu.json
"crossAppSharedConfig": "$profile:shared_config",
// ...
}
}
```

## deviceTypes标签
表2 deviceTypes标签说明
| 设备类型 | 枚举值 | 说明 |
| 手机 | phone | - |
| 平板 | tablet | - |
| PC/2in1 | 2in1 | 即PC设备，主要交互方式以多窗口、多任务及键盘鼠标操作为主，充分发挥设备的生产力属性。在HarmonyOS文档中，所有“2in1”均代表“PC/2in1”。 |
| 智慧屏 | tv | - |
| 智能手表 | wearable | 系统能力较丰富的手表，具备电话功能。 |
| 车机 | car | - |
| 默认设备 | default | 配置为default类型的应用，虽然可以正常编译构建，但是不支持发布上架。建议使用phone替代。 |
deviceTypes示例：
```
{
"module": {
"name": "myHapName",
"type": "feature",
"deviceTypes": [
"tv",
"tablet"
],
// ...
}
}
```

## pages标签
该标签是一个profile文件资源，用于指定描述页面信息的配置文件。
```
{
"module": {
// ...
"pages": "$profile:main_pages", // 资源配置，指向profile下面定义的配置文件main_pages.json
// ...
}
}
```
在开发视图的resources/base/profile下面定义配置文件main_pages.json，其中文件名"main_pages"可自定义，需要和pages标签指定的信息对应。配置文件中列举了当前应用组件中的页面信息，包含页面的路由信息和显示窗口相关的配置。
表3 pages标签说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| src | 标识当前Module中所有页面的路由信息，包括页面路径和页面名称。其中，页面路径是以当前Module的src/main/ets为基准。该标签取值为一个字符串数组，其中每个元素表示一个页面。 | 字符串数组 | 该标签不可缺省。 |
| window | 标识用于定义与显示窗口相关的配置。 | 对象 | 该标签可缺省，缺省值为空。 |
表4 window标签说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| designWidth | 标识页面设计基准宽度。以此为基准，根据实际设备宽度来缩放元素大小。 | 数值 | 可缺省，缺省值为720px。 |
| autoDesignWidth | 标识页面设计基准宽度是否自动计算。当配置为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。当配置为false时，设计基准宽度为designWidth。 | 布尔值 | 可缺省，缺省值为false。 |
```
{
"src": [
"pages/Index"
],
"window": {
"designWidth": 720,
"autoDesignWidth": false
}
}
```

## metadata标签
该标签标识HAP的自定义元信息，标签值为数组类型，包含name、value、resource三个子标签。
表5 metadata标签说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| name | 标识数据项的名称，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| value | 标识数据项的值，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| resource | 标识了用户自定义数据，取值为长度不超过255字节的字符串，内容为该数据的资源索引，例如配置成$profile:shortcuts_config，表示指向了/resources/base/profile/shortcuts_config.json配置文件。 | 字符串 | 该标签可缺省，缺省值为空。 |
```
{
"module": {
// ...
"metadata": [
// ...
{
"name": "pageConfig",
"value": "main page config of application",
"resource": "$profile:main_pages" // 资源配置，指向profile下面定义的配置文件main_pages.json
}
],
// ...
}
}
```

## abilities标签
abilities标签描述UIAbility组件的配置信息，标签值为数组类型，该标签下的配置只对当前UIAbility生效。
表6 abilities标签说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| name | 标识当前UIAbility组件的名称，确保该名称在整个应用中唯一。取值为长度不超过127字节的字符串，以字母开头，可包含字母、数字、下划线（_）或点号（.）。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 标识当前UIAbility的代码路径，取值为长度不超过127字节的字符串。 | 字符串 | 该标签不可缺省。 |
| launchType | 标识当前UIAbility组件的启动模式，支持的取值如下： - multiton：多实例模式，每次启动创建一个新实例。 - singleton：单实例模式，仅第一次启动创建新实例。 - specified：指定实例模式，运行时由开发者决定是否创建新实例。 - standard：multiton的曾用名，效果与多实例模式一致。 说明： 元服务启动模式需要设置为单例模式，详情请参考元服务规格要求。 | 字符串 | 该标签可缺省，该标签缺省为“singleton”。 |
| description | 标识当前UIAbility组件的描述信息，开发者可以通过该标签描述当前组件的功能与作用，取值为长度不超过255字节的字符串。建议采用描述信息的资源索引，以支持多语言。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon | 标识当前UIAbility组件的图标，取值为图标资源文件的索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| label | 标识当前UIAbility组件对用户显示的名称，取值为字符串资源的索引，以支持多语言，长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| permissions | 标识当前UIAbility组件的权限信息。其他应用访问该UIAbility时，需要申请相应的权限。 一个数组元素为一个权限名称，不超过255字节，取值请参考应用权限列表。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| metadata | 标识当前UIAbility组件的元信息，典型使用场景详见窗口元数据配置中的metadata标签。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| exported | 标识当前UIAbility组件是否可以被其他应用拉起。 - true：表示可以被其他应用拉起（入口UIAbility建议配置为true）。 - false：只能由同应用或者具有ohos.permission.START_INVISIBLE_ABILITY权限（该权限仅系统应用支持申请）的应用拉起。 例如，配置为false时，桌面具备该权限，桌面图标、快捷方式或push通知消息可以拉起当前UIAbility组件，但aa命令行工具没有权限无法拉起。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| continuable | 标识当前UIAbility组件是否支持跨端迁移。 - true：表示支持迁移。 - false：表示不支持迁移。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| skills | 标识当前UIAbility组件能够接收的Want特征集，为数组格式。 配置规则： - 对于Entry类型的HAP，应用可以配置多个具有入口能力的skills标签（即配置了ohos.want.action.home和entity.system.home）。 - 对于Feature类型的HAP，只有应用可以配置具有入口能力的skills标签，服务不允许配置。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| backgroundModes | 标识当前UIAbility组件的长时任务集合，指定用于满足特定类型的长时任务。 长时任务类型详情参考长时任务类型表。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| startWindow | 标识当前UIAbility组件启动页面profile资源，取值为长度不超过255字节的字符串，如果配置了该标签，startWindowIcon和startWindowBackground标签均不生效。 说明： 从API version 19开始，支持使用该字段配置增强启动页。 | 字符串 | 该标签可缺省，缺省值为空。 |
| startWindowIcon | 标识当前UIAbility组件启动页面图标资源文件的索引，取值为长度不超过255字节的字符串。 | 字符串 | 该标签不可缺省。 |
| startWindowBackground | 标识当前UIAbility组件启动页面背景颜色资源文件的索引，取值为长度不超过255字节的字符串。 取值示例：$color:red。 | 字符串 | 该标签不可缺省。 |
| removeMissionAfterTerminate | 标识当前UIAbility组件销毁后，是否从任务列表中移除任务。 - true表示销毁后移除任务。 - false表示销毁后不移除任务。 说明： 2in1设备和平板设备的自由多窗模式下配置不生效，默认移除任务。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| allowSelfRedirect | 标识应用是否允许通过App Linking跳转自己。 - true表示允许通过App Linking跳转自己。 - false表示不允许通过App Linking跳转自己。 说明： 从API version 23开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省值为true。 |
| orientation | 标识当前UIAbility组件启动时的方向，支持配置枚举，或启动方向资源索引。 启动方向枚举支持的取值如下： - unspecified：未指定方向，由系统自动判断显示方向。 - landscape：横屏。 - portrait：竖屏。 - follow_recent：跟随背景窗口的旋转模式。 - landscape_inverted：反向横屏。 - portrait_inverted：反向竖屏。 - auto_rotation：随传感器旋转。 - auto_rotation_landscape：传感器横屏旋转，包括横屏和反向横屏。 - auto_rotation_portrait：传感器竖屏旋转，包括竖屏和反向竖屏。 - auto_rotation_restricted：传感器开关打开，方向可随传感器旋转。 - auto_rotation_landscape_restricted：传感器开关打开，方向可随传感器旋转为横屏，包括横屏和反向横屏。 - auto_rotation_portrait_restricted：传感器开关打开，方向可随传感器旋转为竖屏，包括竖屏和反向竖屏。 - locked：传感器开关关闭，方向锁定。 - auto_rotation_unspecified：受开关控制和由系统判定的自动旋转模式。 - follow_desktop：跟随桌面的旋转模式。 配置启动方向的资源索引时，取值为长度不超过255字节的字符串，配置示例：$string:orientation。 说明： - 从API version 14开始，支持配置启动方向资源索引。 | 字符串 | 该标签可缺省，缺省值为unspecified。 |
| supportWindowMode | 标识当前UIAbility组件所支持的窗口模式。支持的取值如下： - fullscreen：全屏模式。 - split：分屏模式。 - floating：悬浮窗模式。 在自由窗口状态下同时配置fullscreen和split时，如果应用的targetAPIVersion小于15，窗口将以悬浮窗模式启动；如果应用的targetAPIVersion大于等于15，窗口将以全屏模式启动。 此外，还可以通过metadata配置窗口模式，具体的配置规则和优先级请参考metadata。 | 字符串数组 | 该标签可缺省，缺省值为 ["fullscreen", "split", "floating"]。 |
| maxWindowRatio | 标识当前UIAbility组件支持的最大的宽高比。该标签最小取值为0。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的宽高比。 |
| minWindowRatio | 标识当前UIAbility组件支持的最小的宽高比。该标签最小取值为0。 | 数值 | 该标签可缺省，缺省值为平台支持的最小的宽高比。 |
| maxWindowWidth | 标识当前UIAbility组件支持的最大的窗口宽度，宽度单位为vp。 最小取值为minWindowWidth，最大取值为平台支持的最大窗口宽度。窗口尺寸可以参考窗口大小限制。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的窗口宽度。 |
| minWindowWidth | 标识当前UIAbility组件支持的最小的窗口宽度， 宽度单位为vp。 最小取值为平台支持的最小窗口宽度，最大取值为maxWindowWidth。窗口尺寸可以参考窗口大小限制。 | 数值 | 该标签可缺省，缺省值为平台支持的最小的窗口宽度。 |
| maxWindowHeight | 标识当前UIAbility组件支持的最大的窗口高度， 高度单位为vp。 最小取值为minWindowHeight，最大取值为平台支持的最大窗口高度。 窗口尺寸可以参考窗口大小限制。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的窗口高度。 |
| minWindowHeight | 标识当前UIAbility组件支持的最小的窗口高度， 高度单位为vp。 最小取值为平台支持的最小窗口高度，最大取值为maxWindowHeight。窗口尺寸可以参考窗口大小限制。 | 数值 | 该标签可缺省，缺省值为平台支持的最小的窗口高度。 |
| excludeFromMissions | 标识当前UIAbility组件是否在最近任务列表中显示。 - true：表示不在任务列表中显示。 - false：表示在任务列表中显示。 说明： 三方应用的配置不生效，当前配置仅在系统应用中有效，若要使系统应用配置生效，需申请应用特权，特权申请不对三方应用开放。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| recoverable | 标识当前UIAbility组件是否支持在检测到应用故障后，恢复到应用原界面。 - true：支持检测到出现故障后，恢复到原界面。 - false：不支持检测到出现故障后，恢复到原界面。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| isolationProcess | 标识组件能否运行在独立的进程中。 - true：表示能运行在独立的进程中。 - false：表示不能运行在独立的进程中。 说明： 仅2in1和tablet设备支持将UIAbility设置为独立进程。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| excludeFromDock | 标识当前UIAbility组件是否支持从dock区域隐藏图标。 - true：表示在dock区域隐藏。 - false：表示不能在dock区域隐藏。 说明： 该标签配置不生效。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| preferMultiWindowOrientation | 标识当前UIAbility组件多窗布局方向： - default：缺省值，参数不配置默认值，建议其他应用类配置。 - portrait：多窗布局方向为竖向，建议竖向游戏类应用配置。 - landscape：多窗布局方向为横向，配置后支持横屏悬浮窗和上下分屏，建议横向游戏类应用配置。 - landscape_auto：多窗布局动态可变为横向，需要配合API enableLandScapeMultiWindow/disableLandScapeMultiWindow使用，建议视频类应用配置。 | 字符串 | 该标签可缺省，缺省值为default。 |
| continueType | 标识当前UIAbility组件的跨端迁移类型。 | 字符串数组 | 该标签可缺省，缺省值为当前组件的名称。 |
| continueBundleName | 标识当前应用支持跨端迁移的其它应用名称列表。 说明： 不能配置为本应用包名，仅为了做异包名迁移使用。 从API version 13开始，支持该标签。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| process | 标识组件的进程名称。具体使用方式参考进程模型定义中的"静态指定进程"。 说明： 1. 仅在PC/2in1和Tablet设备上生效。 2. UIAbility组件和type为embeddedUI的ExtensionAbility组件标签一致时运行在同一个进程中。 3. 从API version 14开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
abilities示例：
```
{
// ...
"abilities": [
{
"name": "EntryAbility",
"srcEntry": "./ets/entryability/EntryAbility.ets",
"launchType": "singleton",
"description": "$string:description_main_ability",
"icon": "$media:layered_image",
"label": "$string:EntryAbility_label",
"permissions": [],
"metadata": [],
"exported": true,
"continuable": true,
"skills": [
{
"actions": [
"ohos.want.action.home"
],
"entities": [
"entity.system.home"
],
"uris": []
}
],
"backgroundModes": [
"dataTransfer"
],
"startWindowIcon": "$media:icon",
"startWindowBackground": "$color:red",
"removeMissionAfterTerminate": true,
"allowSelfRedirect": true, // 从API version 23开始，支持该标签
"orientation": "$string:orientation",
"supportWindowMode": [
"fullscreen",
"split",
"floating"
],
"maxWindowRatio": 3.5,
"minWindowRatio": 0.5,
"maxWindowWidth": 2560,
"minWindowWidth": 1400,
"maxWindowHeight": 300,
"minWindowHeight": 200,
"excludeFromMissions": false,
"preferMultiWindowOrientation": "default",
"isolationProcess": false,
"continueType": [
"continueType1",
"continueType2"
],
"continueBundleName": [
"com.example.myapplication1",
"com.example.myapplication2"
],
"process": ":processTag"
}
],
// ...
}
```

## skills标签
该标签标识UIAbility组件或者ExtensionAbility组件能够接收的Want的特征。
例如：在浏览器中下载PDF文件时，可以通过配置skills标签选择并打开该PDF文件。详情请参考拉起文件处理类应用。
表7 skills标签说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| actions | 标识能够接收的Action值集合，取值通常为系统预定义的action值，也允许自定义。 一个skill中不建议配置多个action，否则可能导致无法匹配预期场景。详情请参考常见action与entities。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| entities | 标识能够接收的Entity值的集合。 一个skill中不建议配置多个entity，否则可能导致无法匹配预期场景。详情请参考常见action与entities。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| uris | 标识与Want中URI（Uniform Resource Identifier）相匹配的集合。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| permissions | 标识当前UIAbility或ExtensionAbility组件的权限信息。其他应用访问该组件时，需要申请相应的权限。 一个数组元素为一个权限名称，不超过255字节，取值请参考应用权限列表。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| domainVerify | 标识是否开启域名校验，详情请参考在module.json5中配置关联的网址域名。 - true：表示开启域名校验。 - false：表示不开启域名校验。 | 布尔值 | 该标签可缺省，缺省值为false。 |
表8 uris标签说明
以下字符串类型的标签不支持使用资源索引的方式（$string）配置。
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| scheme | 标识URI的协议名部分，常见的有http、https、file、ftp等。 说明： 从API 18开始，该标签在参与隐式Want匹配时不区分大小写。 | 字符串 | uris中仅配置type时可以缺省，缺省值为空，否则不可缺省。 |
| host | 标识URI的主机地址部分，该标签只有当scheme配置时才生效。常见的方式： - 域名方式，如example.com。 - IP地址方式，如10.10.10.1。 说明： 从API 18开始，该标签在参与隐式Want匹配时不区分大小写。 | 字符串 | 该标签可缺省，缺省值为空。 |
| port | 标识URI的端口部分。如http默认端口为80，https默认端口是443，ftp默认端口是21。该标签只有当scheme和host都配置时才生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| path | pathStartWith | pathRegex | 标识URI的路径部分，path、pathStartWith和pathRegex配置时三选一。path标识URI与want中的路径部分全匹配，pathStartWith标识URI与want中的路径部分允许前缀匹配，pathRegex标识URI与want中的路径部分允许正则匹配。该标签只有当scheme和host都配置时才生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| type | 标识与Want相匹配的数据类型，使用MIME（Multipurpose Internet Mail Extensions）类型规范和UniformDataType类型规范。可以与scheme同时配置，也可以单独配置。 | 字符串 | 该标签可缺省，缺省值为空。 |
| utd | 标识与Want相匹配的标准化数据类型，适用于分享等场景。 | 字符串 | 该标签可缺省，缺省值为空。 |
| maxFileSupported | 对于指定类型的文件，标识一次能接收或打开的最大数量，适用于分享等场景，需要与utd配合使用。 | 整数 | 该标签可缺省，缺省值为0。 |
| linkFeature | 标识URI提供的功能类型（如文件打开、分享、导航等），用于实现应用间跳转。取值为长度不超过127字节的字符串，不支持中文。同一Bundle中声明的linkFeature数量不能超过150个。详情见linkFeature标签说明。 | 字符串 | 该标签可缺省，缺省值为空。 |
skills示例：
如下示例为通用配置，部分组件和模块在实际配置时存在差异，例如点击消息进入应用首页的限制，具体请参考对应文档说明。
```
{
// ...
"abilities": [
{
// ...
"skills": [
{
"actions": [
"ohos.want.action.home"
],
"entities": [
"entity.system.home"
],
"uris": [
{
"scheme":"http",
"host":"example.com",
"port":"80",
"path":"path",
"type": "text/*",
"linkFeature": "Login"
}
],
"permissions": [],
"domainVerify": false
},
// ...
],
// ...
}
],
// ...
}
```

## extensionAbilities标签
描述extensionAbilities的配置信息，标签值为数组类型，该标签下的配置只对当前extensionAbilities生效。
表9 extensionAbilities标签说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| name | 标识当前ExtensionAbility组件的名称，确保该名称在整个应用中唯一，取值为长度不超过127字节的字符串。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 标识当前ExtensionAbility组件所对应的代码路径，取值为长度不超过127字节的字符串。 | 字符串 | 该标签不可缺省。 |
| description | 标识当前ExtensionAbility组件的描述，开发者可以通过该标签描述当前组件的功能与作用，取值为长度不超过255字节的字符串，可以是对描述内容的资源索引，用于支持多语言。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon | 标识当前ExtensionAbility组件的图标，取值为资源文件的索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| label | 标识当前ExtensionAbility组件对用户显示的名称，取值为该名称的资源索引，以支持多语言，字符串长度不超过255字节。 | 字符串 | 该标签可缺省，缺省值为空。 |
| type | 标识当前ExtensionAbility组件的类型，支持的取值如下： - form：卡片的ExtensionAbility。 - workScheduler：延时任务的ExtensionAbility。 - inputMethod：输入法的ExtensionAbility。 - share：提供内容分享处理功能的ShareExtensionAbility。 - service：后台运行的service组件，三方配置无法安装应用，需要申请特权，特权申请不对三方应用开放。 - accessibility：辅助能力的ExtensionAbility。 - fileAccess：公共数据访问的ExtensionAbility，允许应用程序提供文件和文件夹给文件管理类应用展示，三方应用配置不生效，当前配置仅在系统应用中有效。 - dataShare：数据共享的ExtensionAbility，三方配置无法安装应用，需要申请特权，特权申请不对三方应用开放。 - staticSubscriber：静态广播的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - fileShare：文件共享的ExtensionAbility。 - vpn：为开发者提供VPN能力的ExtensionAbility。 - wallpaper：壁纸的ExtensionAbility。 - backup：数据备份的ExtensionAbility。 - enterpriseAdmin：企业设备管理的ExtensionAbility。企业设备管理应用必须拥有此类型的ExtensionAbility。 - window：该ExtensionAbility会在启动过程中创建一个window，为开发者提供界面开发。开发者开发出来的界面将通过UIExtensionComponent控件组合到其他应用的窗口中，三方应用配置不生效，当前配置仅在系统应用中有效。 - thumbnail：获取文件缩略图的ExtensionAbility，开发者可以对自定义文件类型的文件提供缩略。 - preview：该ExtensionAbility会将文件解析后在一个窗口中显示，开发者可以通过将此窗口组合到其他应用窗口中。 - print：打印框架的ExtensionAbility。 - push：推送的ExtensionAbility。 - driver：驱动框架的ExtensionAbility。应用配置了driver类型的ExtensionAbility后会被视为驱动应用，驱动应用在安装、卸载和恢复时不会区分用户，且创建新用户时也会安装设备上已有的驱动应用。例如，创建子用户时会默认安装主用户已有的驱动应用，在子用户上卸载驱动应用时，主用户上对应的驱动应用也会同时被卸载。 - remoteNotification：远程通知的ExtensionAbility。 - remoteLocation：远程定位的ExtensionAbility。 - voip：网络音视频通话的ExtensionAbility。 - action：自定义操作业务模板的ExtensionAbility，为开发者提供基于UIExtension的自定义操作业务模板。 - adsService：广告业务的ExtensionAbility，提供广告业务框架，三方应用配置不生效，当前配置仅在系统应用中有效。 - embeddedCashier：支付业务的ExtensionAbility，与CashierComponent控件组合使用，将支付页面展示到其他应用中。从API version 23开始，支持该标签。三方应用配置不生效，当前配置仅在系统应用中有效，仅支持TV设备使用，其他设备配置不生效。 - embeddedUI：嵌入式UI扩展能力，提供跨进程界面嵌入的能力。 - insightIntentUI：为开发者提供能被小艺意图调用，以窗口形态呈现内容的扩展能力。 - ads：广告业务的ExtensionAbility，与AdComponent控件组合使用，将广告页面展示到其他应用中。仅支持设备厂商使用。 - photoEditor：图片编辑业务的ExtensionAbility，为开发者提供基于UIExtension的图片编辑业务模版。 - appAccountAuthorization：应用账号授权扩展能力的ExtensionAbility，用于处理账号授权请求，比如账号登录授权。 - autoFill/password：用于账号和密码自动填充业务的ExtensionAbility，支持数据的保存、填充能力。 - hms/account：应用账号管理能力的ExtensionAbility。 - sysDialog/atomicServicePanel：提供构建元服务服务面板的基础能力的ExtensionAbility，使用时基于UIExtensionAbility实现，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysDialog/userAuth：本地用户鉴权的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysDialog/common：通用弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysDialog/power：关机重启弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysDialog/print：打印模态弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysDialog/meetimeCall：畅连通话的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysDialog/meetimeContact：畅连联系人的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysDialog/meetimeMessage：畅连消息的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/meetimeContact：畅连联系人列表的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/meetimeCallLog：畅连通话记录列表的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/share：系统分享的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/mediaControl：投播组件的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/photoPicker：三方应用通过对应的UIExtensionType拉起图库picker界面，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/filePicker：文件下载弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/audioPicker：音频管理弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/photoEditor：图片编辑弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sys/commonUI：非通用的ExtensionAbility，提供业务属性强相关的嵌入式显示或弹框，三方应用配置不生效，当前配置仅在系统应用中有效。 - autoFill/smart：用于情景化场景自动填充业务的ExtensionAbility，支持数据的保存、填充能力。 - uiService：弹窗服务组件，在启动过程中会创建window，并支持双向通信，三方应用配置不生效，当前配置仅在系统应用中有效。 - statusBarView：状态栏开放服务的ExtensionAbility。 - liveViewLockScreen：实况窗锁屏沉浸态的ExtensionAbility。 - accountLogout：华为账号登出能力的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/navigation：拉起系统导航类应用面板的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sysPicker/appSelector：拉起系统应用选择弹框的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - sys/visualExtension : 原生智能图片类控件视觉搜索的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。 - screenTimeGuard：屏幕时间守护开放服务的ExtensionAbility。 从API version 20开始，支持该配置。 - recentPhoto：最近照片推荐的ExtensionAbility。 - fence：地理围栏的ExtensionAbility。 - callerInfoQuery：企业联系人查询的ExtensionAbility。 - assetAcceleration：资源预下载的ExtensionAbility。 - formEdit：卡片编辑的ExtensionAbility。 - distributed：分布式扩展的ExtensionAbility。 - liveForm：互动卡片的ExtensionAbility。从API version 20开始，支持该标签。 - appService：为应用提供后台服务相关扩展能力AppServiceExtensionAbility，包括后台服务的创建、销毁、连接、断开等生命周期回调。从API version 20开始，支持该标签。 - webNativeMessaging：为开发者提供Web原生消息通信能力的ExtensionAbility。从API version 21开始，支持该标签。 - faultLog：故障延迟通知的ExtensionAbility。从API version 21开始，支持该标签。 - notificationSubscriber：提供通知订阅相关功能的ExtensionAbility。从API version 22开始，支持该标签。 - crypto：外部密钥管理扩展的ExtensionAbility。从API version 22开始，支持该标签。 - partnerAgent：基于蓝牙通信技术，提供设备发现与设备下线的通知功能的ExtensionAbility。从API version 23开始，支持该标签。 - contentEmbed：对象插入编辑框架的ExtensionAbility。从API version 23 开始，支持该标签。 - selection：划词扩展的ExtensionAbility。从API version 20开始，仅支持系统应用配置，三方应用配置不生效。从API version 24开始，支持三方应用配置。 - awc/webpage：通用网页浏览的ExtensionAbility。 - awc/newsfeed：信息流资讯业务的ExtensionAbility。 | 字符串 | 该标签不可缺省。 |
| permissions | 标识当前ExtensionAbility组件的权限信息。当其他应用访问该ExtensionAbility时，需要申请相应的权限。 一个数组元素为一个权限名称。不超过255字节，取值请参考应用权限列表。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| appIdentifierAllowList | 标识允许启动此ExtensionAbility的应用程序列表。 一个数组元素为一个应用程序的appIdentifier，appIdentifier信息可参考什么是appIdentifier。 说明： 仅当ExtensionAbility组件的type为appService时支持配置该标签。 从API version 20开始，支持该标签。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| readPermission | 标识读取当前ExtensionAbility组件数据所需的权限，取值为长度不超过255字节的字符串。仅当预置的系统应用ExtensionAbility的type配置为dataShare时，该标签生效。dataShare类型仅支持系统应用支持配置，三方应用配置不生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| writePermission | 标识向当前ExtensionAbility组件写数据所需的权限，取值为长度不超过255字节的字符串。仅当预置的系统应用ExtensionAbility的type配置为dataShare时，该标签生效。dataShare类型仅支持系统应用支持配置，三方应用配置不生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| uri | 标识当前ExtensionAbility组件提供的数据URI，取值为长度不超过255字节的字符数组，用反向域名的格式表示。 说明： 该标签在type为dataShare类型的ExtensionAbility时，不可缺省。 | 字符串 | 该标签可缺省，缺省值为空。 |
| skills | 标识当前ExtensionAbility组件能够接收的Want的特征集。 配置规则：entry包可以配置多个具有入口能力的skills标签（配置了ohos.want.action.home和entity.system.home）的ExtensionAbility，其中第一个配置了skills标签的ExtensionAbility中的label和icon作为服务或应用的label和icon。 说明： 服务的Feature包不支持配置具有入口能力的skills标签。 应用的Feature包支持配置具有入口能力的skills标签。 | 数组 | 该标签可缺省，缺省值为空。 |
| metadata | 标识当前ExtensionAbility组件的元信息。 说明： 该标签在type为form时，不可缺省，且必须存在一个name为ohos.extension.form的对象值，其对应的resource值不能缺省，为服务卡片的二级资源引用。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| exported | 标识当前ExtensionAbility组件是否可以被其他应用调用。 - true：表示可以被其他应用调用。 - false：表示不可以被其他应用调用，包括无法被aa工具命令拉起应用。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| extensionProcessMode | 标识当前ExtensionAbility组件的多进程实例模型,当前只对UIExtensionAbility以及从UIExtensionAbility扩展的ExtensionAbility生效。 - instance：表示该ExtensionAbility每个实例一个进程。 - type：表示该ExtensionAbility实例都运行在同一个进程里，与其他ExtensionAbility分离进程。 - bundle：表示该ExtensionAbility实例都运行在应用统一进程里，与其他配置了bundle模型的ExtensionAbility共进程。 - runWithMainProcess：表示该ExtensionAbility和应用主进程共进程，只有状态栏开放服务的ExtensionAbility可以配置runWithMainProcess。 | 字符串 | 该标签可缺省，缺省值为空。 |
| dataGroupIds | 标识当前ExtensionAbility组件的dataGroupId集合。如果当前ExtensionAbility组件所在的应用在应用市场申请的证书里groupIds也申请了某个dataGroupId，那么当前ExtensionAbility组件可以和应用共享这一个dataGroupId生成的目录，所以ExtensionAbility组件的dataGroupId需要是应用的签名证书中groupIds标签里配置的才能生效。 且该标签仅在当前ExtensionAbility组件存在独立的沙箱目录时生效。详见共享沙箱介绍第3点共享沙箱的配置流程中的步骤a申请data-group-id。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| process | 标识组件的进程名称，只有type为embeddedUI时可以配置该标签。具体使用方式参考进程模型定义中的"静态指定进程"。 说明： 1. 仅在PC/2in1和Tablet设备上生效。 2. UIAbility组件和ExtensionAbility组件标签一致时运行在同一个进程中。 3. 从API version 14开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
| isolationProcess | 标识ExtensionAbility组件能否运行在独立的进程中。 - true：表示能运行在独立的进程中。 - false：表示不能运行在独立的进程中。 说明： 仅当ExtensionAbility组件的type为"sys/commonUI"时该标签配置生效，且仅支持由系统应用配置type为"sys/commonUI"。 从API version 20开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省值为false。 |
extensionAbilities示例：
```
{
// ...
"extensionAbilities": [
{
"name": "FormName",
"srcEntry": "./ets/form/MyForm.ets",
"icon": "$media:icon",
"label" : "$string:extension_name",
"description": "$string:form_description",
"type": "form",
"permissions": ["ohos.permission.ACCESS_BLUETOOTH"],
"exported": true,
"uri":"scheme://authority/path/query",
"skills": [{
"actions": [],
"entities": [],
"uris": [],
"permissions": []
}],
"metadata": [
{
"name": "ohos.extension.form",
"resource": "$profile:form_config",
}
],
"extensionProcessMode": "instance",
"dataGroupIds": [
"testGroupId1"
]
}
],
// ...
}
```

## shortcuts标签
shortcuts标识应用的快捷方式信息。标签值为数组，包含四个子标签shortcutId、label、icon、wants。
metadata中指定shortcut信息，其中：
- name：指定shortcuts的名称，使用ohos.ability.shortcuts作为shortcuts信息的标识。
- resource：指定shortcuts信息的资源位置。
桌面展示快捷方式的数量有上限要求，最多展示4个。
表10 shortcuts标签说明
| 属性名称 | 含义 | 类型 | 是否可缺省 |
| shortcutId | 标识快捷方式的ID，取值为长度不超过63字节的字符串。不支持通过资源索引的方式（$string）配置该标签。 | 字符串 | 该标签不可缺省。 |
| label | 标识快捷方式的标签信息，即快捷方式对外显示的文字描述信息。取值为长度不超过255字节的字符串，可以是描述性内容，也可以是标识label的资源索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon | 标识快捷方式的图标，取值为资源文件的索引。 说明： 图标分为单层图标和分层图标，单层图标包含一个图片，分层图标包含前景图和背景图，推荐使用如下配置的分层图标： 1.前景图：图标显示大小为450*450px，资源大小为1024*1024px的透明图层。 2.背景图：大小为1024*1024px。 | 字符串 | 该标签可缺省，缺省值为空。 |
| visible | 标识快捷方式是否显示，取值为true时显示快捷方式，取值为false时不显示快捷方式。 说明： 1.从API version 20开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省为true。 |
| wants | 标识快捷方式内定义的目标wants信息集合，在调用launcherBundleManager的startShortcut接口时，会拉起wants标签里的第一个目标组件，推荐只配置一个wants元素。 | 对象 | 该标签可缺省，缺省为空。 |
- 在/resources/base/profile/目录下配置shortcuts_config.json配置文件。 ``` { "shortcuts": [ { "shortcutId": "id_test1", "label": "$string:shortcut", "icon": "$media:aa_icon", "visible": true, "wants": [ { "bundleName": "com.ohos.hello", "moduleName": "entry", "abilityName": "EntryAbility", "parameters": { "testKey": "testValue" } } ] } ] } ```
- 在module.json5配置文件的abilities标签中，针对需要添加快捷方式的UIAbility进行配置metadata标签，使shortcut配置文件对该UIAbility生效。 ``` { "module": { // ... "abilities": [ { "name": "EntryAbility", "srcEntry": "./ets/entryability/EntryAbility.ets", // ... "skills": [ // ... { "entities": [ "entity.system.home" ], "actions": [ "ohos.want.action.home" ] } ], "metadata": [ { "name": "ohos.ability.shortcuts", "resource": "$profile:shortcuts_config" } ], // ... } ], // ... } } ```

## wants标签
此标签用于标识快捷方式内定义的目标wants信息集合。
表11 wants标签说明
| 属性名称 | 含义 | 类型 | 是否可缺省 |
| bundleName | 表示快捷方式的目标包名。 | 字符串 | 该标签可缺省。 |
| moduleName | 表示快捷方式的目标模块名。 | 字符串 | 该标签可缺省。 |
| abilityName | 表示快捷方式的目标组件名。 | 字符串 | 该标签可缺省。 |
| parameters | 表示拉起快捷方式时的自定义数据，仅支持配置字符串类型的数据。其中键值均最大支持1024长度的字符串。 | 对象 | 该标签可缺省。 |
wants标签示例：
```
{
"wants": [
{
"bundleName": "com.ohos.hello",
"moduleName": "entry",
"abilityName": "EntryAbility",
"parameters": {
"testKey": "testValue"
}
}
]
}
```
