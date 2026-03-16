# Class (MediaQuery)

提供根据不同媒体类型定义不同的样式。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 10开始支持。

-

以下API需先使用UIContext中的[getMediaQuery()](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getmediaquery)方法获取到MediaQuery对象，再通过该对象调用对应方法。

#### matchMediaSync

matchMediaSync(condition: string): mediaQuery.MediaQueryListener

设置媒体查询的查询条件，并返回对应的监听句柄。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明conditionstring是媒体事件的匹配条件，具体可参考[媒体查询语法规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query#语法规则)。

**返回值：**

类型说明[mediaQuery.MediaQueryListener](../../modules/ohos/@ohos.mediaquery (媒体查询).md#ZH-CN_TOPIC_0000002497604790__mediaquerylistener)媒体事件监听句柄，用于注册和去注册监听回调。

**示例：**

完整示例请参考[mediaquery示例](../../modules/ohos/@ohos.mediaquery (媒体查询).md#ZH-CN_TOPIC_0000002497604790__示例)。