# @Entry：页面入口

@Entry装饰的自定义组件将作为UI页面的入口。

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### @Entry

在单个UI页面中，仅允许存在一个由@Entry装饰的自定义组件作为页面的入口。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
@Entry
@Component
struct Index {
  build() {
    Text('@Entry Test')
  }
}
```

#### EntryOptions10+

命名路由跳转选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明routeNamestring否是

表示作为命名路由页面的名字。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

storage[LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage)否是

页面级的UI状态存储。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

useSharedStorage12+boolean否是

是否使用[loadContent](../../types/interfaces/Interface (WindowStage).md#ZH-CN_TOPIC_0000002497444824__loadcontent9)传入的LocalStorage实例对象。默认值false。true：使用共享的LocalStorage实例对象。false：不使用共享的LocalStorage实例对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**示例：**

```ets
@Entry({routeName: 'myPage'})
@Component
struct Index {
  build() {
    Text('Index')
  }
}
```