# FormLink

提供静态卡片交互组件，用于静态卡片内部和卡片提供方应用间的交互，当前支持router、message和call三种类型的事件。

-

该组件从API Version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

该组件仅可以在静态卡片中使用。

-

本文仅提供静态卡片开发指导，其他卡片相关内容请参考[卡片开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/formkit-overview)。

#### 权限

无

#### 子组件

支持单个子组件。

#### 接口

FormLink(options: FormLinkOptions)

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[FormLinkOptions](#ZH-CN_TOPIC_0000002497604938__formlinkoptions对象说明)是定义卡片信息

#### FormLinkOptions对象说明

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明actionstring否否

action的类型，支持三种预定义的类型：

- router：跳转到提供方应用的指定UIAbility。

- message：自定义消息，触发后会调用提供方FormExtensionAbility的[onFormEvent()](@ohos.app.form.FormExtensionAbility (FormExtensionAbility).md#ZH-CN_TOPIC_0000002497605278__formextensionabilityonformevent)生命周期回调。

- call：后台启动提供方应用。触发后会拉起提供方应用的指定UIAbility（仅支持launchType为[singleton](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type#singleton启动模式)的UIAbility，即启动模式为单实例的UIAbility），但不会调度到前台。提供方应用需要具备后台运行权限([ohos.permission.KEEP_BACKGROUND_RUNNING](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionkeep_background_running))。

**说明：**

不推荐使用router事件刷新卡片UI。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

moduleNamestring否是

action为router / call 类型时跳转的模块名。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

bundleNamestring否是

action为router / call 类型时跳转的包名。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

abilityNamestring否是

action为router / call 类型时跳转的UIAbility名。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

uri11+string否是

action为router 类型时跳转的UIAbility的统一资源标识符。uri和abilityName同时存在时，abilityName优先。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

paramsObject否是

当前action携带的额外参数，内容使用JSON格式的键值对形式。call 类型时需填入参数'method'，且类型需要为string类型，用于触发UIAbility中对应的方法。

**说明：**

不建议通过params传递卡片内部的状态变量。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

#### 属性

支持[通用属性](通用属性.md)。

#### 事件

不支持[通用事件](通用事件.md)。

#### 示例

```ets
@Entry
@Component
struct FormLinkDemo {
  build() {
    Column() {
      Text("这是一个静态卡片").fontSize(20).margin(10)

      // router事件用于静态卡片跳转到对应的UIAbility
      FormLink({
        action: "router",
        abilityName: "EntryAbility",
        params: {
          'message': 'testForRouter' // 自定义要发送的message
        }
      }) {
        Button("router event").width(120)
      }.margin(10)

      // message事件触发FormExtensionAbility的onFormEvent生命周期
      FormLink({
        action: "message",
        abilityName: "EntryAbility",
        params: {
          'message': 'messageEvent' // 自定义要发送的message
        }
      }) {
        Button("message event").width(120)
      }.margin(10)

      // call事件用于触发UIAbility中对应的方法
      FormLink({
        action: "call",
        abilityName: "EntryAbility",
        params: {
          'method': 'funA', // 在EntryAbility中调用的方法名
          'num': 1 // 需要传递的其他参数
        }
      }) {
        Button("call event").width(120)
      }.margin(10)

      // router事件用于静态卡片deeplink跳转到对应的UIAbility
      FormLink({
        action: "router",
        uri: 'example://uri.ohos.com/link_page',
        params: {
          message: 'router msg for static uri deeplink' // 自定义要发送的message
        }
      }) {
        Button("deeplink event").width(120)
      }.margin(10)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%').height('100%')
  }
}
```

**待跳转应用 [module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#skills标签) uris 配置示例：**

```ets
"abilities": [
  {
    "skills": [
      {
        "uris": [
          {
            "scheme": "example",
            "host": "uri.ohos.com",
            "path": "link_page"
          },
        ]
      }
    ],
  }
]
```